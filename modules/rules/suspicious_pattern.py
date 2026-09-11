"""suspicious_pattern：形态启发式识别结构投毒节点（A3）。

原理：投毒节点需要"注册域名 + 伪装成访问知名站 + 常用随机高位端口"，
而正常 Reality / TLS 节点 sni 指向知名站时，server 要么是 IP、要么是
短域名且端口通常为 443 等标准端口。因此三条件**同时**命中才 REJECT：

- 条件1：server 是域名且长度 >= _MIN_HOST_LEN（排除 IP 与短域名）
- 条件2：sni 的注册域命中知名站清单（正常 Reality 也命中，需配合条件1/3）
- 条件3：端口不在标准代理端口集合（挡开 443 等正常节点）

任何一条不满足都不判，结构性保证正常节点误伤趋近 0：
- server=IP + sni 知名站（Reality 标准形态）→ 条件1 排除
- server=域名 + sni 知名站 + 443 → 条件3 排除
- server=xxx.pages.dev + sni=自家域名（CDN 中转）→ 条件2 排除
"""
from __future__ import annotations

from ..common.domain import reg_domain
from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult

# 条件1：server 域名长度阈值（投毒者随机子域普遍 >= 20 字符）
_MIN_HOST_LEN = 20

# 条件2：sni 知名站清单（注册域末两段匹配；Reality 常用伪装目标）
_FAMOUS_SNI = frozenset({
    "google.com", "googleusercontent.com", "googleapis.com", "gstatic.com",
    "apple.com", "icloud.com", "yahoo.com", "yahoo.co.jp", "deepl.com",
    "cloudflare.com", "cloudfront.net", "netflix.com", "amazon.com",
    "amazonaws.com", "microsoft.com", "bing.com", "facebook.com",
    "instagram.com", "whatsapp.com", "x.com", "twitter.com", "youtube.com",
    "github.com", "tiktok.com", "openai.com", "anthropic.com",
    "stackoverflow.com", "wikipedia.org", "telegram.org", "spotify.com",
    "nvidia.com", "adobe.com", "linkedin.com", "reddit.com",
})

# 条件3：标准/常见代理端口（在集合内 = 不触发端口条件）
_STD_PORTS = frozenset({
    443, 80, 8080, 8888, 8443, 2052, 2053, 2054, 2082, 2083, 2086, 2087,
    2095, 2096, 8880, 8000, 1080,
})


class SuspiciousPatternRule(Rule):
    rule_id = "suspicious_pattern"
    category = RuleCategory.VALIDITY

    def __init__(
        self,
        extra_famous_hosts: list[str] | None = None,
        extra_std_ports: list[int] | None = None,
    ) -> None:
        """extra_famous_hosts: 追加 sni 知名站（完整域名/注册域均可，按注册域匹配）；
        extra_std_ports: 追加标准端口（命中即不触发端口条件，可降低误伤）。
        """
        self._famous = set(_FAMOUS_SNI)
        if extra_famous_hosts:
            self._famous.update(
                reg_domain(h) for h in extra_famous_hosts if h and h.strip()
            )
            self._famous.discard(None)
        self._std_ports = set(_STD_PORTS)
        if extra_std_ports:
            self._std_ports.update(int(p) for p in extra_std_ports if p)

    def evaluate(self, node: Node) -> RuleResult:
        server = (node.server or "").strip().lower()
        if not server or ":" in server or node.is_ip:
            return RuleResult.pass_()  # IP 或 IPv6 不适用（Reality 正常形态）
        if len(server) < _MIN_HOST_LEN:
            return RuleResult.pass_()  # 短域名不判
        sni = (node.raw.get("sni") or "").strip().lower()
        if not sni or reg_domain(sni) not in self._famous:
            return RuleResult.pass_()  # sni 非知名站（CDN 中转等正常形态）
        if node.port in self._std_ports:
            return RuleResult.pass_()  # 标准端口不判（Reality 正常形态）
        return RuleResult.reject(RejectReason.HEURISTIC_POISON)
