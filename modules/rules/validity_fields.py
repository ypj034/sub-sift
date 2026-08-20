"""validity_fields：协议特有字段格式有效性。

统一 REASON_INVALID_FIELD（DESIGN.md：无效节点直接丢弃，不细分原因）。
判据：uuid 格式、password 空串/占位、method 空串。
"""
from __future__ import annotations

import re

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult

_UUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)
_ALL_ZERO_UUID = "00000000-0000-0000-0000-000000000000"

# 已知干扰节点标记（硬编码，与 config 关键词解耦）：
# 伊朗反 v2ray 组织会在订阅里投毒，密码/ID 内嵌此类标记的节点为干扰节点。
# 不放进 junk_keywords：关键词可被禁用/留空，干扰标记必须始终拦截。
_JAMMING_MARKERS = ("banv2ray", "ban v2ray")


def _is_placeholder(s: str) -> bool:
    """占位/无效判定：空串、全空白、全相同字符、过短。"""
    s = s or ""
    stripped = s.strip()
    if not stripped:
        return True
    if len(stripped) < 4:
        return True
    if len(set(stripped)) == 1:  # 全 0 / 全 a / 全 * 等
        return True
    return False


def _has_jamming_marker(s: str) -> bool:
    """含已知干扰标记（大小写不敏感，子串匹配）。"""
    low = (s or "").lower()
    return any(m in low for m in _JAMMING_MARKERS)


class ValidityFieldsRule(Rule):
    rule_id = "validity_fields"
    category = RuleCategory.VALIDITY

    def evaluate(self, node: Node) -> RuleResult:
        proto = node.protocol
        raw = node.raw or {}

        if proto in ("vmess", "vless"):
            uuid = str(raw.get("uuid") or "")
            if not _UUID_RE.match(uuid):
                return RuleResult.reject(RejectReason.INVALID_FIELD)
            if uuid.replace("-", "").strip("0") == "":
                return RuleResult.reject(RejectReason.INVALID_FIELD)
            if _has_jamming_marker(uuid):
                return RuleResult.reject(RejectReason.INVALID_FIELD)
        elif proto == "ss":
            method = str(raw.get("method") or "")
            if not method.strip():
                return RuleResult.reject(RejectReason.INVALID_FIELD)
            password = str(raw.get("password") or "")
            if _is_placeholder(password):
                return RuleResult.reject(RejectReason.INVALID_FIELD)
            if _has_jamming_marker(password):
                return RuleResult.reject(RejectReason.INVALID_FIELD)
        elif proto in ("trojan", "hysteria2"):
            password = str(raw.get("password") or "")
            if _is_placeholder(password):
                return RuleResult.reject(RejectReason.INVALID_FIELD)
            if _has_jamming_marker(password):
                return RuleResult.reject(RejectReason.INVALID_FIELD)

        return RuleResult.pass_()
