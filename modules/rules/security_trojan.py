"""security_trojan：trojan 安全基线。

trojan 协议本身基于 TLS，tls=false → 不安全；allowInsecure=true → 不安全。
"""
from __future__ import annotations

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult


class SecurityTrojanRule(Rule):
    rule_id = "security_trojan"
    category = RuleCategory.SECURITY

    def evaluate(self, node: Node) -> RuleResult:
        if node.protocol != "trojan":
            return RuleResult.pass_()
        raw = node.raw or {}
        if not raw.get("tls"):
            return RuleResult.reject(RejectReason.UNSAFE_NO_TLS)
        if raw.get("allowInsecure"):
            return RuleResult.reject(RejectReason.UNSAFE_ALLOW_INSECURE)
        return RuleResult.pass_()
