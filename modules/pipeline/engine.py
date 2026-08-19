"""规则执行引擎：顺序执行、短路、fail-closed。

DESIGN.md §5.2：
- 规则顺序 = config 声明顺序
- 短路：节点被 REJECT 立即终止后续规则
- fail-closed：规则异常 → REJECT(REASON_RULE_ERROR)，异常计数暴露于 report
- 规则级计数器：按原因枚举聚合，进 report 不进判定
"""
from __future__ import annotations

from dataclasses import dataclass, field

from ..common.enums import RejectReason
from ..common.node import Node
from ..rules.base import Rule


@dataclass
class RuleStats:
    """规则级计数器。counts[rule_id][reason] = 次数。"""

    counts: dict[str, dict[str, int]] = field(default_factory=dict)
    errors: dict[str, int] = field(default_factory=dict)

    def record(self, rule_id: str, reason: RejectReason) -> None:
        bucket = self.counts.setdefault(rule_id, {})
        bucket[reason.value] = bucket.get(reason.value, 0) + 1

    def record_error(self, rule_id: str) -> None:
        self.errors[rule_id] = self.errors.get(rule_id, 0) + 1

    def total_rejected(self) -> int:
        return sum(sum(v.values()) for v in self.counts.values())

    def as_table(self) -> list[tuple[str, str, int]]:
        """返回 [(rule_id, reason, count)] 供报告展示。"""
        rows: list[tuple[str, str, int]] = []
        for rule_id, bucket in self.counts.items():
            for reason, count in bucket.items():
                rows.append((rule_id, reason, count))
        return rows


def run_pipeline(nodes: list[Node], rules: list[Rule]) -> tuple[list[Node], RuleStats]:
    """对节点流执行全部规则，返回（通过节点, 规则级计数器）。"""
    passed: list[Node] = []
    stats = RuleStats()

    for node in nodes:
        for rule in rules:
            try:
                result = rule.evaluate(node)
            except Exception:  # noqa: BLE001 - fail-closed：规则异常按 REJECT 处理
                stats.record_error(rule.rule_id)
                stats.record(rule.rule_id, RejectReason.RULE_ERROR)
                break
            if result.rejected:
                stats.record(rule.rule_id, result.reason)
                break
        else:
            passed.append(node)

    return passed, stats
