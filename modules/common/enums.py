"""全局枚举定义。

- RejectReason: REJECT 原因（全局聚合键），rule 产出的原因必须是其中之一。
- RuleCategory: 规则分类。
"""
from enum import Enum


class RejectReason(str, Enum):
    """REJECT 原因枚举，作为规则级计数器的聚合键。"""

    PROTOCOL_NOT_ALLOWED = "protocol_not_allowed"
    INVALID_TARGET = "invalid_target"
    INVALID_FIELD = "invalid_field"
    UNSAFE_NO_TLS = "unsafe_no_tls"
    UNSAFE_ALLOW_INSECURE = "unsafe_allow_insecure"
    UNSAFE_WEAK_CIPHER = "unsafe_weak_cipher"
    JUNK_KEYWORD = "junk_keyword"
    REGION_NOT_ALLOWED = "region_not_allowed"
    RULE_ERROR = "rule_error"

    def __str__(self) -> str:  # pragma: no cover - 便于日志展示
        return self.value


class RuleCategory(str, Enum):
    """规则分类，与 DESIGN.md §5.3 一致。"""

    PROTOCOL = "protocol"
    VALIDITY = "validity"
    SECURITY = "security"
    JUNK = "junk"
    REGION = "region"
