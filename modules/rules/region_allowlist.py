"""region_allowlist：地区白名单。

判定（DESIGN.md §5.3）：
- 域名型 server（非 IP）→ PASS（既定例外），region 留空（统计归入 other 列）
- IP 型 server → 查离线 GeoIP：
  - 地区不在白名单或查不到 → REJECT(REGION_NOT_ALLOWED)
  - 命中白名单 → PASS 并写回 node.region
"""
from __future__ import annotations

from typing import Optional

from ..common.enums import RejectReason, RuleCategory
from ..common.geoip import GeoIP
from ..common.node import Node
from .base import Rule, RuleResult


class RegionAllowlistRule(Rule):
    rule_id = "region_allowlist"
    category = RuleCategory.REGION

    def __init__(self, allow: list[str], geoip: Optional[GeoIP]) -> None:
        self._allow = set(allow)
        self._geoip = geoip

    def evaluate(self, node: Node) -> RuleResult:
        if not node.is_ip:
            # 域名型服务器：跳过地区判定（DESIGN 既定例外）
            return RuleResult.pass_()
        if self._geoip is None:
            # 无 GeoIP 数据且为 IP 型：无法确认地区合规，按不在白名单处理
            return RuleResult.reject(RejectReason.REGION_NOT_ALLOWED)
        region = self._geoip.lookup(node.server)
        if region is None or region not in self._allow:
            return RuleResult.reject(RejectReason.REGION_NOT_ALLOWED)
        node.region = region
        return RuleResult.pass_()
