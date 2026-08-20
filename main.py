#!/usr/bin/env python3
"""sub-sift 入口：编排一次完整运行。

用法: python main.py [config.yaml] [--update-geo]

流程（DESIGN.md §2.3）：
聚合源拉取 → 合并主清单 → 状态机过滤 → 逐链接拉取/解析 → pipeline 筛选
→ 指纹去重/改名 → 输出订阅文件 → 写 CSV/state/report

--update-geo: 仅检查并更新 GeoLite2 mmdb（HEAD 对比 Last-Modified，
有更新才下载，失败不阻塞），完成后退出。
"""
from __future__ import annotations

import argparse
import concurrent.futures
import sys
from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

from modules.common.config import Config, ConfigError, load_config
from modules.common.geoip import GeoIP
from modules.common.node import Node
from modules.fetcher.aggregator import fetch_all_aggregators
from modules.fetcher.subscription import extract_placeholders, fetch_subscription_nodes
from modules.pipeline import RuleStats, deduplicate, rename_unique, run_pipeline
from modules.report.generator import generate_report
from modules.rules import build_rules
from modules.statemachine.engine import StateMachine, SubscriptionState, WindowEntry
from modules.store import csv_store, output as output_store
from modules.store import state_store


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="sub-sift", description="订阅质量管理器")
    parser.add_argument("config_path", nargs="?", default="config.yaml")
    parser.add_argument(
        "--update-geo",
        action="store_true",
        help="检查并更新 GeoLite2 mmdb（有更新才下载，失败不阻塞）后退出",
    )
    ns = parser.parse_args(argv)

    try:
        config = load_config(ns.config_path)
    except ConfigError as e:
        print(f"[sub-sift] 配置错误: {e}", file=sys.stderr)
        return 1

    # --------------------------------------------------- 0. 可选：仅更新 mmdb
    if ns.update_geo:
        from modules.fetcher.geo_updater import update_geo

        status = update_geo(
            config.geo_mmdb_url, data_dir="data", timeout_sec=config.timeout_sec
        )
        print(f"[sub-sift] geo update: {status}")
        return 0

    tz = ZoneInfo(config.timezone)
    now = datetime.now(tz)
    today = now.date()
    today_str = now.strftime("%Y%m%d")

    # -------------------------------------------------------------- 1. 事实源
    sub_rows = csv_store.read_subscription_rows()
    agg_rows = csv_store.read_aggregator_rows()
    sub_states, agg_windows = state_store.load_states()
    agg_id_by_link = {r["link"]: r["id"] for r in agg_rows}

    # CSV 是事实源：状态文件里已删除的链接/聚合源同步清理，避免残留
    valid_sub_links = {r.link for r in sub_rows}
    for link in list(sub_states):
        if link not in valid_sub_links:
            del sub_states[link]
    valid_agg_ids = {r["id"] for r in agg_rows}
    for agg_id in list(agg_windows):
        if agg_id not in valid_agg_ids:
            del agg_windows[agg_id]

    # 链接占位符预校验：出现即必须在 config 白名单内，否则配置错误
    allowed = set(config.template_placeholders)
    bad_links = []
    for link in [r.link for r in sub_rows] + [r["link"] for r in agg_rows]:
        extra = extract_placeholders(link) - allowed
        if extra:
            bad_links.append((link, sorted(extra)))
    if bad_links:
        for link, extra in bad_links:
            print(f"[sub-sift] 链接含未列入白名单的占位符 {extra}: {link}", file=sys.stderr)
        print(
            "[sub-sift] 请将占位符加入 config.yaml 的 fetcher.template_placeholders "
            f"(可选: {sorted(allowed)})",
            file=sys.stderr,
        )
        return 1

    # -------------------------------------------------- 2. 聚合源 → 合并主清单
    agg_results = fetch_all_aggregators(config)
    for link, result in agg_results.items():
        agg_id = agg_id_by_link.get(link)
        if agg_id is None:
            continue  # 聚合源不在 CSV（配置异常），跳过
        if isinstance(result, Exception):
            continue  # 单源失败，跳过，不影响主清单
        for found in result:
            _merge_link(sub_rows, found, agg_id)

    # 手动新增的裸行（只有 link、sources 为空）自动补 [manual]
    for row in sub_rows:
        if not row.sources:
            row.sources = ["manual"]

    # ----------------------------------------------- 3. 状态机过滤 + 规则构建
    geoip = GeoIP()
    sm = StateMachine(
        window_size=config.window_size,
        cooldown_failures=config.cooldown_failures,
        cooldown_days=config.cooldown_days,
        disable_failures=config.disable_failures,
    )
    rules = build_rules(config, geoip)

    plan: list[csv_store.SubscriptionRow] = []
    skipped = 0
    for row in sub_rows:
        state = sub_states.get(row.link)
        if state is None:
            state = SubscriptionState(link=row.link)
            sub_states[row.link] = state
        if sm.should_fetch(state, today):
            plan.append(row)
        else:
            skipped += 1

    # ------------------------------------ 4. 并发拉取 + pipeline + 统计
    run_stats = RuleStats()
    per_link: dict[str, dict] = {}
    all_passed: list[Node] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=config.concurrency) as pool:
        futures = {
            pool.submit(fetch_subscription_nodes, row.link, config, today): row.link
            for row in plan
        }
        for future in concurrent.futures.as_completed(futures):
            link = futures[future]
            ok, nodes = future.result()
            passed, stats = run_pipeline(nodes, rules)
            _merge_stats(run_stats, stats)
            all_passed.extend(passed)
            counts = _count_distribution(passed, config)
            per_link[link] = {
                "ok": ok,
                "count": len(passed),
                "counts": counts,
                "rejected": stats.total_rejected(),
            }
            state = sub_states[link]
            sm.record_result(state, ok, len(passed), today)

    # -------------------------------------------- 5. 去重/改名 → 输出文件
    merged = deduplicate(all_passed)
    rename_unique(merged)
    written = output_store.write_output_files(merged, config.output_directory, config.output_formats)

    # ------------------------------------------- 6. 聚合源窗口更新
    for link, result in agg_results.items():
        agg_id = agg_id_by_link.get(link)
        if agg_id is None:
            continue
        window = agg_windows.setdefault(agg_id, [])
        if isinstance(result, Exception):
            window.append(WindowEntry(ts=today.isoformat(), ok=False, count=0))
        else:
            # 统计口径：该源拉取出的、主清单中状态正常且有效节点数>0 的订阅链接数。
            # 冷却/禁用（本次未拉取）或拉取失败/有效节点为 0 的链接不计入。
            ok_links = sum(
                1
                for found in result
                if (info := per_link.get(found)) is not None
                and info["ok"]
                and info["count"] > 0
            )
            window.append(WindowEntry(ts=today.isoformat(), ok=True, count=ok_links))
        if len(window) > config.window_size:
            del window[: len(window) - config.window_size]

    # -------------------------------------------- 7. 写 CSV / state / report
    run_counts = {link: info["counts"] for link, info in per_link.items()}
    csv_store.write_subscriptions(
        "data/subscriptions.csv", sub_rows, sub_states, run_counts, today_str, config
    )
    csv_store.write_aggregators("data/aggregators.csv", agg_rows, agg_windows, today_str)
    state_store.save_states(sub_states, agg_windows)

    report_path = generate_report(
        config,
        {
            "run_time": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "today": today,
            "sub_rows": sub_rows,
            "sub_states": sub_states,
            "per_link": per_link,
            "skipped": skipped,
            "stats": run_stats,
            "rule_order": [r.rule_id for r in rules],
            "merged_count": len(merged),
            "agg_rows": agg_rows,
            "agg_windows": agg_windows,
            "geoip_source": geoip.source,
            "output_files": written,
        },
    )

    # 概要输出
    print(f"[sub-sift] 运行完成: {now:%Y-%m-%d %H:%M:%S}")
    print(f"[sub-sift] 主清单 {len(sub_rows)} 链接，拉取 {len(plan)}（跳过 {skipped}），"
          f"成功 {sum(1 for i in per_link.values() if i['ok'])}")
    print(f"[sub-sift] 有效节点 {len(all_passed)}，去重后输出 {len(merged)}，"
          f"规则拒绝 {run_stats.total_rejected()}")
    print(f"[sub-sift] 输出: {', '.join(written.values())}")
    print(f"[sub-sift] 报告: {report_path}")
    return 0


# ---------------------------------------------------------------------------
# 内部工具
# ---------------------------------------------------------------------------

def _merge_link(rows: list[csv_store.SubscriptionRow], link: str, agg_id: str) -> None:
    """把聚合源拉到的链接合并进主清单（链接级去重，DESIGN.md §8）。"""
    for row in rows:
        if row.link == link:
            if agg_id not in row.sources:
                row.sources.append(agg_id)
            return
    rows.append(csv_store.SubscriptionRow(link=link, sources=[agg_id]))


def _merge_stats(target: RuleStats, src: RuleStats) -> None:
    for rule_id, bucket in src.counts.items():
        target_bucket = target.counts.setdefault(rule_id, {})
        for reason, count in bucket.items():
            target_bucket[reason] = target_bucket.get(reason, 0) + count
    for rule_id, count in src.errors.items():
        target.errors[rule_id] = target.errors.get(rule_id, 0) + count


def _count_distribution(nodes: list[Node], config: Config) -> dict[str, int]:
    """统计筛选后（去重前）节点的协议/地区分布。

    域名型 server 自动跳过地区判定，计入 domain 列；
    IP 型 server 未命中白名单地区在规则层已被 REJECT（地区过滤），
    因此通过集合中不存在该情况，无需 other_ip 兜底列。
    """
    counts: dict[str, int] = {col: 0 for col in config.protocol_allowlist}
    for col in config.region_allowlist:
        counts[col] = 0
    counts["domain"] = 0
    for n in nodes:
        if n.protocol in config.protocol_allowlist:
            counts[n.protocol] += 1
        if n.region and n.region in config.region_allowlist:
            counts[n.region] += 1
        elif not n.is_ip:
            counts["domain"] += 1
    return counts


if __name__ == "__main__":
    sys.exit(main())
