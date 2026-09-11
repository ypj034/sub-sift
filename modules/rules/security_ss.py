"""security_ss：shadowsocks 安全基线。

安全 method 集合（代码内固定，DESIGN.md §5.4）：
aes-128-gcm / aes-256-gcm / chacha20-ietf-poly1305 / xchacha20-ietf-poly1305
/ shadowsocks-2022 系列。method 为空或非安全集合 → 不安全。
"""
from __future__ import annotations

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult

_SAFE_METHODS = {
    "aes-128-gcm",
    "aes-256-gcm",
    "chacha20-ietf-poly1305",
    "xchacha20-ietf-poly1305",
    "2022-blake3-aes-128-gcm",
    "2022-blake3-aes-256-gcm",
    "2022-blake3-chacha20-poly1305",
}


class SecuritySsRule(Rule):
    rule_id = "security_ss"
    category = RuleCategory.SECURITY

    def evaluate(self, node: Node) -> RuleResult:
        if node.protocol != "ss":
            return RuleResult.pass_()
        raw = node.raw or {}
        method = str(raw.get("method") or "").lower()
        if method not in _SAFE_METHODS:
            return RuleResult.reject(RejectReason.UNSAFE_WEAK_CIPHER)
        return RuleResult.pass_()
