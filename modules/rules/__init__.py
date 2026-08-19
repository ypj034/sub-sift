"""rules 模块：规则实现（每规则一文件，贡献者低门槛）。

铁律：每个 Rule 对 Node 只有 PASS / REJECT(原因)，无中间态、无权重、无打分。
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from ..common.config import Config
from ..common.geoip import GeoIP
from .base import Rule
from .junk_keywords import JunkKeywordsRule
from .protocol_allowlist import ProtocolAllowlistRule
from .region_allowlist import RegionAllowlistRule
from .security_hysteria2 import SecurityHysteria2Rule
from .security_ss import SecuritySsRule
from .security_trojan import SecurityTrojanRule
from .security_vless import SecurityVlessRule
from .security_vmess import SecurityVmessRule
from .validity_fields import ValidityFieldsRule
from .validity_target import ValidityTargetRule

if TYPE_CHECKING:  # pragma: no cover
    pass


def build_rules(config: Config, geoip: GeoIP | None = None) -> list[Rule]:
    """按 config 声明顺序构建启用的规则列表。

    region_allowlist 需要 GeoIP 实例；若 geoip 为 None 且规则启用，调用方应保证传入。
    """
    built: list[Rule] = []
    for rid in config.active_rules:
        if rid == "protocol_allowlist":
            built.append(ProtocolAllowlistRule(config.protocol_allowlist))
        elif rid == "validity_target":
            built.append(ValidityTargetRule())
        elif rid == "validity_fields":
            built.append(ValidityFieldsRule())
        elif rid == "security_vmess":
            built.append(SecurityVmessRule())
        elif rid == "security_vless":
            built.append(SecurityVlessRule())
        elif rid == "security_trojan":
            built.append(SecurityTrojanRule())
        elif rid == "security_ss":
            built.append(SecuritySsRule())
        elif rid == "security_hysteria2":
            built.append(SecurityHysteria2Rule())
        elif rid == "junk_keywords":
            built.append(JunkKeywordsRule(config.junk_keywords))
        elif rid == "region_allowlist":
            built.append(RegionAllowlistRule(config.region_allowlist, geoip))
    return built


__all__ = [
    "Rule",
    "build_rules",
    "ProtocolAllowlistRule",
    "ValidityTargetRule",
    "ValidityFieldsRule",
    "SecurityVmessRule",
    "SecurityVlessRule",
    "SecurityTrojanRule",
    "SecuritySsRule",
    "SecurityHysteria2Rule",
    "JunkKeywordsRule",
    "RegionAllowlistRule",
]
