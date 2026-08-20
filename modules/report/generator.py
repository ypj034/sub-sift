"""report.md 生成：运行概览、规则计数器、主清单排序表、聚合源统计。

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
    rows = _merge_validity_rows(rows)
    if rows:
        lines.append("| 规则 | 拒绝数 |")
        lines.append("|---|---|")
        for rule_id, count in rows:
            lines.append(f"| {rule_id} | {count} |")
        lines.append(f"| **合计** | **{sum(count for _, count in rows)}** |")
    else:
        lines.append("（本轮无节点被规则拒绝）")
    if stats.errors:
        lines.append("")
        lines.append("> 规则异常计数：")
        for rule_id, count in stats.errors.items():
            lines.append(f"> - {rule_id}: {count} 次（fail-closed 已按 REJECT 处理）")
    lines.append("")

    # 主清单排序表（state 分组 → avg 降序 → success_rate 降序）
    lines.append("## 主清单（active → 冷却 → disabled；组内按 avg 降序）")
    sub_rows = ctx["sub_rows"]
    sub_states = ctx["sub_states"]
    today = ctx["today"]
    lines.append("| link | 状态 | success_rate | last | avg |")
    lines.append("|---|---|---|---|---|")
    for row in sorted(
        sub_rows, key=lambda r: _main_sort_key(sub_states.get(r.link), today)
    ):
        state = sub_states.get(row.link)
        sr = _success_rate(state)
        last = _last_count(state)
        avg = _avg_count(state)
        st = _state_str(state)
        lines.append(f"| {row.link} | {st} | {sr} | {last} | {avg:.1f} |")
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

def _merge_validity_rows(rows: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """展示层合并 validity_target + validity_fields 为一行 validity（规则引擎保持独立）。"""
    merged: dict[str, int] = {}
    for rule_id, count in rows:
        name = "validity" if rule_id in ("validity_target", "validity_fields") else rule_id
        merged[name] = merged.get(name, 0) + count
    return list(merged.items())


def _state_rank(state, today) -> int:
    """状态分组排序键：active=0 → 冷却=1 → disabled=2。"""
    if state is None:
        return 0
    if state.disabled:
        return 2
    if state.cooldown_until and today.isoformat() <= state.cooldown_until:
        return 1
    return 0


def _success_rate_value(state) -> float:
    """success_rate 数值化：ok/total；无执行记录按 0（组内排尾）。"""
    if state is None or not state.window:
        return 0.0
    total = len(state.window)
    ok = sum(1 for w in state.window if w.ok)
    return ok / total if total else 0.0


def _main_sort_key(state, today) -> tuple[int, float, float]:
    """主清单排序键：state 分组 → avg 降序 → success_rate 降序。"""
    return (_state_rank(state, today), -_avg_count(state), -_success_rate_value(state))


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
