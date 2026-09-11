"""junk_keywords：垃圾关键词过滤。

匹配 name 与 server（子串匹配，大小写不敏感）。关键词来自 config，可增删。
默认清单保守，仅收明显垃圾/广告/测试/占位词。
"""
from __future__ import annotations

from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult


class JunkKeywordsRule(Rule):
    rule_id = "junk_keywords"
    category = RuleCategory.JUNK

    def __init__(self, keywords: list[str]) -> None:
        # 防御：YAML 的 [null] 会解析为 [None]，若直接 str(None) 会得到 "none"
        # 成为真实关键词；空值/None 一律视为"无此关键词"
        self._keywords = []
        for k in keywords or []:
            if k is None:
                continue
            s = str(k).strip()
            if s:
                self._keywords.append(s.lower())

    def evaluate(self, node: Node) -> RuleResult:
        if not self._keywords:
            return RuleResult.pass_()
        haystack = f"{node.name} {node.server}".lower()
        for kw in self._keywords:
            if kw in haystack:
                return RuleResult.reject(RejectReason.JUNK_KEYWORD)
        return RuleResult.pass_()
