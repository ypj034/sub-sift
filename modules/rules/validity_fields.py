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
        elif proto == "ss":
            method = str(raw.get("method") or "")
            if not method.strip():
                return RuleResult.reject(RejectReason.INVALID_FIELD)
            if _is_placeholder(str(raw.get("password") or "")):
                return RuleResult.reject(RejectReason.INVALID_FIELD)
        elif proto in ("trojan", "hysteria2"):
            if _is_placeholder(str(raw.get("password") or "")):
                return RuleResult.reject(RejectReason.INVALID_FIELD)

        return RuleResult.pass_()
