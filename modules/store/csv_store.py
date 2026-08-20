"""CSV 读写：subscriptions.csv（动态列）与 aggregators.csv。

DESIGN.md §3.2/§3.3：
- subscriptions.csv：link + sources 为人工维护列，其余程序维护，
  按 state（active → 冷却 → disabled）→ avg 降序 → success_rate 降序
  动态列 = config 协议白名单镜像 + 地区白名单镜像 + domain，随配置增减
- aggregators.csv：一行一聚合源，按 avg_count 降序
"""
from __future__ import annotations

import csv
import os
from dataclasses import dataclass, field

from ..common.config import Config
from ..statemachine.engine import SubscriptionState, WindowEntry

SUB_HEADER_BASE = ["link", "sources", "success_rate", "state",
                   "last", "avg", "last_run_at"]
AGG_HEADER = ["id", "link", "success_rate", "last_count", "avg_count", "last_run_at"]


@dataclass
class SubscriptionRow:
    link: str
    sources: list[str] = field(default_factory=list)


def read_subscription_rows(path: str = "data/subscriptions.csv") -> list[SubscriptionRow]:
    """读取主清单（事实源）。文件不存在或为空时返回空列表。"""
    if not os.path.isfile(path):
        return []
    rows: list[SubscriptionRow] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for record in reader:
            link = (record.get("link") or "").strip()
            if not link:
                continue
            sources = [s.strip() for s in (record.get("sources") or "").split(";") if s.strip()]
            rows.append(SubscriptionRow(link=link, sources=sources))
    return rows


def read_aggregator_links(path: str = "data/aggregators.csv") -> list[str]:
    """读取聚合源 link 列表（供 fetcher 使用）。"""
    if not os.path.isfile(path):
        return []
    links: list[str] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for record in reader:
            link = (record.get("link") or "").strip()
            if link:
                links.append(link)
    return links


def read_aggregator_rows(path: str = "data/aggregators.csv") -> list[dict[str, str]]:
    """读取聚合源行（id + link）。"""
    if not os.path.isfile(path):
        return []
    rows: list[dict[str, str]] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for record in reader:
            agg_id = (record.get("id") or "").strip()
            link = (record.get("link") or "").strip()
            if agg_id and link:
                rows.append({"id": agg_id, "link": link})
    return rows


def write_subscriptions(
    path: str,
    rows: list[SubscriptionRow],
    states: dict[str, SubscriptionState],
    run_counts: dict[str, dict[str, int]],
    today_str: str,
    config: Config,
) -> None:
    """重写主清单 CSV。

    - rows: 全部订阅行（link + sources，含本次合并后的新增）
    - states: link → 状态机状态（含本次运行后的窗口）
    - run_counts: link → 本次运行筛选后节点的 {协议: 数量, 地区: 数量}；
      未拉取/失败的链接无该键 → 分布列全 0
    """
    proto_cols = config.protocol_allowlist
    region_cols = list(config.region_allowlist)
    header = SUB_HEADER_BASE + proto_cols + region_cols + ["domain"]

    today_iso = f"{today_str[:4]}-{today_str[4:6]}-{today_str[6:]}"

    def sort_key(row: SubscriptionRow) -> tuple[int, float, float]:
        state = states.get(row.link)
        return (
            _state_rank(state, today_iso),
            -_avg_count(state),
            -_success_rate_value(state),
        )

    ordered = sorted(rows, key=sort_key)

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in ordered:
            state = states.get(row.link)
            counts = run_counts.get(row.link) or {}
            rec = {
                "link": row.link,
                "sources": ";".join(row.sources),
                "success_rate": _success_rate_str(state),
                "state": _state_str(state, today_str),
                "last": str(_last_count(state)),
                "avg": f"{_avg_count(state):.1f}",
                "last_run_at": _last_ts(state),
            }
            for col in proto_cols:
                rec[col] = str(counts.get(col, 0))
            for col in region_cols:
                rec[col] = str(counts.get(col, 0))
            rec["domain"] = str(counts.get("domain", 0))
            writer.writerow(rec)


def write_aggregators(
    path: str,
    rows: list[dict[str, str]],
    windows: dict[str, list[WindowEntry]],
    today_str: str,
) -> None:
    """重写聚合源 CSV。

    - rows: id + link 列表
    - windows: id → 窗口记录 [WindowEntry(ts, ok, count)]（来自 state.json）
    """
    def sort_key(row: dict[str, str]) -> float:
        window = windows.get(row["id"]) or []
        if not window:
            return 0.0
        return sum(w.count for w in window) / len(window)

    ordered = sorted(rows, key=sort_key, reverse=True)

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=AGG_HEADER)
        writer.writeheader()
        for row in ordered:
            window = windows.get(row["id"]) or []
            total = len(window)
            ok = sum(1 for w in window if w.ok)
            last_count = window[-1].count if window else 0
            avg = (sum(w.count for w in window) / total) if total else 0.0
            last_ts = window[-1].ts if window else ""
            writer.writerow({
                "id": row["id"],
                "link": row["link"],
                "success_rate": f"{ok}/{total}" if total else "-",
                "last_count": str(last_count),
                "avg_count": f"{avg:.1f}",
                "last_run_at": last_ts,
            })


# ---------------------------------------------------------------------------
# 内部辅助
# ---------------------------------------------------------------------------

def _state_rank(state: SubscriptionState | None, today_iso: str) -> int:
    """状态分组排序键：active=0 → 冷却=1 → disabled=2。"""
    if state is None:
        return 0
    if state.disabled:
        return 2
    if state.cooldown_until and today_iso <= state.cooldown_until:
        return 1
    return 0


def _success_rate_value(state: SubscriptionState | None) -> float:
    """success_rate 数值化：ok/total；无执行记录按 0（组内排尾）。"""
    if state is None or not state.window:
        return 0.0
    total = len(state.window)
    ok = sum(1 for w in state.window if w.ok)
    return ok / total if total else 0.0


def _success_rate_str(state: SubscriptionState | None) -> str:
    if state is None or not state.window:
        return "-"
    total = len(state.window)
    ok = sum(1 for w in state.window if w.ok)
    return f"{ok}/{total}"


def _state_str(state: SubscriptionState | None, today_str: str) -> str:
    if state is None:
        return "active"
    if state.disabled:
        return "disabled"
    if state.cooldown_until:
        return f"冷却至 {state.cooldown_until[5:].replace('-', '-')}"
    return "active"


def _last_count(state: SubscriptionState | None) -> int:
    return state.window[-1].count if state and state.window else 0


def _avg_count(state: SubscriptionState | None) -> float:
    if state is None or not state.window:
        return 0.0
    return sum(w.count for w in state.window) / len(state.window)


def _last_ts(state: SubscriptionState | None) -> str:
    return state.window[-1].ts if state and state.window else ""
