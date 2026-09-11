"""域名工具：注册域提取，供规则层复用。

规则层需要区分"server 指向哪个注册域"，以便：
- 精确命中 denylist（测速站 / 已知投毒域名），含任意子域
- 避免子串匹配误伤（如 speedtesty.xyz 不应命中 speedtest.net）
"""
from __future__ import annotations


def reg_domain(host: str) -> str | None:
    """提取 host 的注册域（末两段），统一小写；无法判定时返回 None。

    - IPv4 / IPv6 字面量 → None（规则层对 IP 走其他判定）
    - 空 host / 无点分结构 / 末尾空段（如 "example..com"）→ None
    - 例: "www.speedtest.net" → "speedtest.net"
    - 例: "3.speedtest.net"  → "speedtest.net"
    - 例: "example.com"      → "example.com"
    """
    h = (host or "").strip().lower()
    if not h or ":" in h:  # 空串 / IPv6
        return None
    if h.replace(".", "").replace("-", "").isdigit():  # IPv4 字面量
        return None
    parts = h.split(".")
    if len(parts) < 2:
        return None
    last_two = parts[-2:]
    if not all(last_two):  # 形如 "example..com"
        return None
    return ".".join(last_two)
