"""validity_target：目标地址有效性（server/port）。

代码内固定的客观名单（DESIGN.md §5.5）：
- 内网/保留 IP：依赖 ipaddress 内置属性（private/loopback/link-local/reserved/multicast/unspecified）
- RFC 保留域名：example.* 、localhost 、*.test / *.invalid / *.example
"""
from __future__ import annotations

import ipaddress
import re

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult

_RESERVED_DOMAIN_PATTERNS = (
    r"(^|\.)example\.(com|net|org|edu)$",
    r"^localhost$",
    r"(^|\.)invalid$",
    r"(^|\.)test$",
    r"(^|\.)example$",
)
_RESERVED_DOMAIN_RE = [re.compile(p, re.IGNORECASE) for p in _RESERVED_DOMAIN_PATTERNS]


class ValidityTargetRule(Rule):
    rule_id = "validity_target"
    category = RuleCategory.VALIDITY

    def evaluate(self, node: Node) -> RuleResult:
        server = node.server.strip() if node.server else ""
        if not server:
            return RuleResult.reject(RejectReason.INVALID_TARGET)

        if not (0 < node.port <= 65535):
            return RuleResult.reject(RejectReason.INVALID_TARGET)

        if node.is_ip:
            try:
                addr = ipaddress.ip_address(server)
            except ValueError:
                return RuleResult.reject(RejectReason.INVALID_TARGET)
            if (
                addr.is_private
                or addr.is_loopback
                or addr.is_link_local
                or addr.is_reserved
                or addr.is_multicast
                or addr.is_unspecified
            ):
                return RuleResult.reject(RejectReason.INVALID_TARGET)
        else:
            for pattern in _RESERVED_DOMAIN_RE:
                if pattern.search(server):
                    return RuleResult.reject(RejectReason.INVALID_TARGET)

        return RuleResult.pass_()
