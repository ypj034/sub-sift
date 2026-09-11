"""重名改名：保证输出节点 name 全局唯一。

DESIGN.md §5.8：重名追加序号后缀（Node → Node-2 → Node-3），
仅变换展示名，不影响节点身份。
"""
from __future__ import annotations

from ..common.node import Node


def rename_unique(nodes: list[Node]) -> None:
    """原地修改节点 name，确保唯一。"""
    seen: set[str] = set()
    for node in nodes:
        base = node.name
        candidate = base
        suffix = 2
        while candidate in seen:
            candidate = f"{base}-{suffix}"
            suffix += 1
        seen.add(candidate)
        node.name = candidate
