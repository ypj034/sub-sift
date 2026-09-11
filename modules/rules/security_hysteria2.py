"""security_hysteria2：hysteria2 安全基线。

insecure=true（跳过证书校验）→ 不安全。hysteria2 基于 QUIC 自带加密。
"""
from __future__ import annotations

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult


class SecurityHysteria2Rule(Rule):
    rule_id = "security_hysteria2"
    category = RuleCategory.SECURITY

    def evaluate(self, node: Node) -> RuleResult:
        if node.protocol != "hysteria2":
            return RuleResult.pass_()
        raw = node.raw or {}
        if raw.get("insecure"):
            return RuleResult.reject(RejectReason.UNSAFE_ALLOW_INSECURE)
        return RuleResult.pass_()
