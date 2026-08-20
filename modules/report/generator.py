"""report.md 生成：运行概览、规则计数器、排序表、重叠度。

DESIGN.md §9：人读汇总，只展示统计，不做任何决策依据。
"""
from __future__ import annotations

import os
from typing import Any

from ..common.config import Config
from ..pipeline.engine import RuleStats


def generate_report(config: Config, ctx: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# sub-sift 运行报告")
    lines.append("")
    lines.append(f"- 运行时间: {ctx.get('run_time', '-')}")
    lines.append(f"- 主清单订阅链接数: {len(ctx['sub_rows'])}")
    lines.append(f"- 本次实际拉取: {len(ctx['per_link'])}（冷却/禁用跳过: {ctx.get('skipped', 0)}）")
    ok_count = sum(1 for r in ctx["per_link"].values() if r["ok"])
    fail_count = len(ctx["per_link"]) - ok_count
    lines.append(f"- 拉取成功: {ok_count}，失败: {fail_count}")
    lines.append(f"- 有效节点数（筛选后去重前）: {sum(r['count'] for r in ctx['per_link'].values())}")
    lines.append(f"- 输出节点数（去重后）: {ctx.get('merged_count', 0)}")
    lines.append(f"- GeoIP 数据源: {ctx.get('geoip_source', '-')}")
    if ctx.get("output_files"):
        files = ", ".join(ctx["output_files"].values())
        lines.append(f"- 输出文件: {files}")
    lines.append("")

    # 规则计数器（按规则聚合总数，遵循脚本运行时规则声明顺序）
    lines.append("## 规则计数器")
    stats: RuleStats = ctx["stats"]
    order = ctx.get("rule_order") or []
    rows = stats.as_rule_totals(order) if order else []
    if rows:
        lines.append("| 规则 | 拒绝数 |")
        lines.append("|---|---|")
        for rule_id, count in rows:
            lines.append(f"| {rule_id} | {count} |")
    else:
        lines.append("（本轮无节点被规则拒绝）")
    if stats.errors:
        lines.append("")
        lines.append("> 规则异常计数：")
        for rule_id, count in stats.errors.items():
            lines.append(f"> - {rule_id}: {count} 次（fail-closed 已按 REJECT 处理）")
    lines.append("")

    # 主清单排序表
    lines.append("## 主清单（按近 N 次总节点数降序）")
    sub_rows = ctx["sub_rows"]
    sub_states = ctx["sub_states"]
    per_link = ctx["per_link"]
    lines.append("| link | 状态 | success_rate | last | avg | total |")
    lines.append("|---|---|---|---|---|---|")
    for row in sorted(sub_rows, key=lambda r: _total(sub_states.get(r.link)), reverse=True):
        state = sub_states.get(row.link)
        sr = _success_rate(state)
        last = _last_count(state)
        avg = _avg_count(state)
        total = _total(state)
        st = _state_str(state)
        lines.append(f"| {row.link} | {st} | {sr} | {last} | {avg:.1f} | {total} |")
    lines.append("")

    # 聚合源
    lines.append("## 聚合源（按近 N 次平均拉取数降序）")
    agg_rows = ctx["agg_rows"]
    agg_windows = ctx["agg_windows"]
    lines.append("| id | link | success_rate | last | avg |")
    lines.append("|---|---|---|---|---|")
    for row in sorted(agg_rows, key=lambda r: _agg_avg(agg_windows.get(r["id"])), reverse=True):
        window = agg_windows.get(row["id"]) or []
        total = len(window)
        ok = sum(1 for w in window if w.ok)
        last = window[-1].count if window else 0
        avg = (sum(w.count for w in window) / total) if total else 0.0
        lines.append(
            f"| {row['id']} | {row['link']} | {f'{ok}/{total}' if total else '-'} | {last} | {avg:.1f} |"
        )
    lines.append("")

    # 重叠度
    lines.append("## 重叠度")
    multi = sum(1 for r in sub_rows if len(r.sources) >= 2)
    total_rows = len(sub_rows)
    lines.append(f"- 被多个来源（≥2）拉到的订阅链接: {multi} / {total_rows}")
    if total_rows:
        lines.append(f"- 占比: {multi / total_rows * 100:.1f}%")
    lines.append("")

    content = "\n".join(lines)
    directory = config.output_directory
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "report.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


# ---------------------------------------------------------------------------
# 内部辅助（与 csv_store / statemachine 的统计口径保持一致）
# ---------------------------------------------------------------------------

def _total(state) -> int:
    if state is None or not state.window:
        return 0
    return sum(w.count for w in state.window)


def _success_rate(state) -> str:
    if state is None or not state.window:
        return "-"
    total = len(state.window)
    ok = sum(1 for w in state.window if w.ok)
    return f"{ok}/{total}"


def _last_count(state) -> int:
    return state.window[-1].count if state and state.window else 0


def _avg_count(state) -> float:
    if state is None or not state.window:
        return 0.0
    return sum(w.count for w in state.window) / len(state.window)


def _state_str(state) -> str:
    if state is None:
        return "active"
    if state.disabled:
        return "disabled"
    if state.cooldown_until:
        return f"冷却至 {state.cooldown_until[5:]}"
    return "active"


def _agg_avg(window) -> float:
    if not window:
        return 0.0
    return sum(w.count for w in window) / len(window)
