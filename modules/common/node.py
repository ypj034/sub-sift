"""Node 数据结构（仅运行时存在，不持久化）。

字段约定见 DESIGN.md §3.1：
- id: 运行期唯一标识，由调用方分配
- raw: 协议特有子结构，承载安全判定字段
  vmess:      cipher, tls, sni, alterId, uuid
  vless:      tls, reality, flow, allowInsecure, uuid
  trojan:     tls, sni, allowInsecure, password
  ss:         method, plugin, password
  hysteria2:  insecure, sni, password
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Node:
    protocol: str
    server: str
    port: int
    name: str
    id: str = ""
    region: Optional[str] = None
    raw: dict = field(default_factory=dict)

    @property
    def is_ip(self) -> bool:
        """server 是否为 IP 字面量（IPv4/IPv6），用于地区判定。"""
        import ipaddress

        try:
            ipaddress.ip_address(self.server)
            return True
        except ValueError:
            return False
