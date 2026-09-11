"""指纹去重（运行期内存，不持久化）。

DESIGN.md §5.7：指纹 = protocol + server:port + 协议身份字段。
身份字段缺失按空串 fallback（粗粒度，保守去重）。
"""
from __future__ import annotations

from ..common.node import Node


def fingerprint(node: Node) -> str:
    raw = node.raw or {}
    proto = node.protocol
    if proto in ("vmess", "vless"):
        ident = str(raw.get("uuid") or "")
    elif proto == "trojan":
        ident = f"{raw.get('sni', '')}:{raw.get('password', '')}"
    elif proto == "ss":
        ident = f"{raw.get('method', '')}:{raw.get('password', '')}"
    elif proto == "hysteria2":
        ident = str(raw.get("password") or "")
    else:
        ident = ""
    return f"{proto}:{node.server}:{node.port}:{ident}"


def deduplicate(nodes: list[Node]) -> list[Node]:
    """按指纹去重，首见保留。"""
    seen: set[str] = set()
    result: list[Node] = []
    for node in nodes:
        fp = fingerprint(node)
        if fp in seen:
            continue
        seen.add(fp)
        result.append(node)
    return result
