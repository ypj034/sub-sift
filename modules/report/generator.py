"""report.md 生成：运行概览、主清单排序表（规则分组列）、聚合源统计。

DESIGN.md §9：人读汇总，只展示统计，不做任何决策依据。
"""
from __future__ import annotations

import os
from typing import Any

from ..common.config import Config

# 主清单规则列分组（列名 → 规则 ID 集合；仅展示层聚合，判定逻辑仍用规则 ID）
_RULE_GROUP_ORDER = ("无效", "非加密", "排除协议", "排除地区")
_RULE_GROUP_RULES = {
    "无效": ("server_denylist", "validity_target", "validity_fields", "suspicious_pattern", "junk_keywords"),
    "非加密": ("security_vmess", "security_vless", "security_trojan", "security_ss", "security_hysteria2"),
    "排除协议": ("protocol_allowlist",),
    "排除地区": ("region_allowlist",),
}


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

    # 主清单排序表（state 分组 → avg 降序 → success_rate 降序；规则列分组聚合）
    lines.append("## 主清单（active → 冷却 → disabled；组内按 avg 降序）")
    sub_rows = ctx["sub_rows"]
    sub_states = ctx["sub_states"]
    per_link = ctx["per_link"]
    today = ctx["today"]
    lines.append("| 链接 | 状态 | 成功率 | 有效率 | 平均 | 最近 | 无效 | 非加密 | 排除协议 | 排除地区 | 排除合计 |")
    lines.append("| --- | :---: | :---: | :---: | --- | --- | --- | --- | --- | --- | --- |")
    for row in sorted(
        sub_rows, key=lambda r: _main_sort_key(sub_states.get(r.link), today)
    ):
        state = sub_states.get(row.link)
        sr = _success_rate(state)
        eff = _effective_rate(per_link.get(row.link))
        last = _last_count(state)
        avg = _avg_count(state)
        st = _state_str(state)
        info = per_link.get(row.link)
        cells = " | ".join(_rule_group_cells(info))
        lines.append(f"| {row.link} | {st} | {sr} | {eff} | {avg:.1f} | {last} | {cells} |")
    lines.append("")

    # 聚合源
    lines.append("## 聚合源（按近 N 次平均拉取数降序）")
    agg_rows = ctx["agg_rows"]
    agg_windows = ctx["agg_windows"]
    lines.append("| id | 链接 | 成功率 | 最近 | 平均 |")
    lines.append("|---|---|:---:|---|---|")
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

def _rule_group_cells(info: dict[str, Any] | None) -> list[str]:
    """主清单规则列：按分组聚合每个链接的拒绝数。

    info 为 None（本轮未拉取，如冷却/禁用）时规则列全部留空；
    否则按 _RULE_GROUP_RULES 分组求和，末尾追加"排除合计"（全部规则拒绝总数）。
    """
    if info is None:
        return ["", "", "", "", ""]
    rc = info.get("rule_counts") or {}
    cells = [str(sum(rc.get(rid, 0) for rid in _RULE_GROUP_RULES[col])) for col in _RULE_GROUP_ORDER]
    cells.append(str(info.get("rejected", 0)))
    return cells


def _effective_rate(info: dict[str, Any] | None) -> str:
    """本轮有效率 = 有效节点数 / 解析出的原始节点数（百分比，1 位小数）。

    未拉取（None）→ 留空；原始节点数为 0 → "-"（分母无意义）。
    """
    if info is None:
        return ""
    raw = info.get("raw") or 0
    count = info.get("count") or 0
    if raw <= 0:
        return "-"
    return f"{count / raw * 100:.1f}%"


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
