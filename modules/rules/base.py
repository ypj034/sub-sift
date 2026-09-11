"""Rule 基类与结果类型。

契约（DESIGN.md §5.1）：
- 无状态纯函数：evaluate(node) -> RuleResult
- REJECT 必须带原因（全局枚举，聚合键）
- 无中间态；规则自身异常由 pipeline 引擎按 fail-closed 处理
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node


@dataclass(frozen=True)
class RuleResult:
    rejected: bool
    reason: Optional[RejectReason] = None

    @classmethod
    def pass_(cls) -> "RuleResult":
        return cls(rejected=False)

    @classmethod
    def reject(cls, reason: RejectReason) -> "RuleResult":
        return cls(rejected=True, reason=reason)


class Rule(ABC):
    """规则基类。子类需声明 rule_id、category 并实现 evaluate。"""

    rule_id: str = "rule"
    category: Optional[RuleCategory] = None

    @abstractmethod
    def evaluate(self, node: Node) -> RuleResult:
        """对单个节点求值，返回 PASS 或 REJECT(原因)。"""
