"""security_vmess：vmess 安全基线。

安全 cipher 集合（代码内固定，DESIGN.md §5.4）：
auto / aes-128-gcm / chacha20-poly1305。
cipher 为空或非安全集合 → 不安全；TLS 关闭 → 不安全。
"""
from __future__ import annotations

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult

_SAFE_CIPHERS = {"auto", "aes-128-gcm", "chacha20-poly1305"}


class SecurityVmessRule(Rule):
    rule_id = "security_vmess"
    category = RuleCategory.SECURITY

    def evaluate(self, node: Node) -> RuleResult:
        if node.protocol != "vmess":
            return RuleResult.pass_()
        raw = node.raw or {}
        cipher = str(raw.get("cipher") or "").lower()
        if cipher not in _SAFE_CIPHERS:
            return RuleResult.reject(RejectReason.UNSAFE_WEAK_CIPHER)
        if not raw.get("tls"):
            return RuleResult.reject(RejectReason.UNSAFE_NO_TLS)
        return RuleResult.pass_()
