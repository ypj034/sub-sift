"""security_vless：vless 安全基线。

无 TLS 且非 Reality → 不安全；allowInsecure=true → 不安全。
"""
from __future__ import annotations

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult


class SecurityVlessRule(Rule):
    rule_id = "security_vless"
    category = RuleCategory.SECURITY

    def evaluate(self, node: Node) -> RuleResult:
        if node.protocol != "vless":
            return RuleResult.pass_()
        raw = node.raw or {}
        if not raw.get("tls") and not raw.get("reality"):
            return RuleResult.reject(RejectReason.UNSAFE_NO_TLS)
        if raw.get("allowInsecure"):
            return RuleResult.reject(RejectReason.UNSAFE_ALLOW_INSECURE)
        return RuleResult.pass_()
