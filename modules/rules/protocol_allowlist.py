"""protocol_allowlist：协议白名单。"""
from __future__ import annotations

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult


class ProtocolAllowlistRule(Rule):
    rule_id = "protocol_allowlist"
    category = RuleCategory.PROTOCOL

    def __init__(self, allow: list[str]) -> None:
        self._allow = set(allow)

    def evaluate(self, node: Node) -> RuleResult:
        if node.protocol not in self._allow:
            return RuleResult.reject(RejectReason.PROTOCOL_NOT_ALLOWED)
        return RuleResult.pass_()
