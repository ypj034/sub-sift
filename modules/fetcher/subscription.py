"""订阅链接拉取：填充模板 → 拉取内容 → 解析节点。

模板处理（DESIGN.md §8）：模板原串 = 身份（用于匹配统计），填充后 URL = 仅访问用。

占位符 → 日期片段 映射为代码内固定标准（不进 config）：
{Y}=2026  {m}=8  {mm}=08  {d}=20  {dd}=20  {Ymd}=20260820
"""
from __future__ import annotations

import re
from datetime import date, datetime
from typing import Optional

from ..common.config import Config
from ..common.node import Node
from .http import FetchError, fetch_text
from .parser import parse_content

_PLACEHOLDER_RE = re.compile(r"\{[^}]+\}")


def placeholder_values(today: date) -> dict[str, str]:
    """按日期生成各占位符的实际替换值（代码内固定映射）。"""
    return {
        "{Y}": f"{today.year:04d}",
        "{m}": f"{today.month}",
        "{mm}": f"{today.month:02d}",
        "{d}": f"{today.day}",
        "{dd}": f"{today.day:02d}",
        "{Ymd}": today.strftime("%Y%m%d"),
    }


def extract_placeholders(link: str) -> set[str]:
    """提取链接中出现的所有 {xxx} 占位符（用于启动预校验）。"""
    return set(_PLACEHOLDER_RE.findall(link))


def fill_template(identity: str, placeholders: list[str], today: date) -> str:
    """将白名单内的模板占位符替换为各自实际值，生成访问 URL。

    placeholders 为 config.fetcher.template_placeholders（白名单）。
    非白名单占位符保留原样（启动预校验已保证链接中出现的都在白名单内）。
    """
    values = placeholder_values(today)
    url = identity
    for ph in placeholders:
        if ph in values:
            url = url.replace(ph, values[ph])
    return url


def fetch_subscription_nodes(
    identity: str, config: Config, today: date
) -> tuple[bool, list[Node]]:
    """拉取单个订阅并解析节点。

    返回 (ok, nodes)：
    - ok=False 仅当拉取失败（网络/HTTP/超时），视为整体失败
    - 内容解析"逐条尽力而为"，提取条数 > 0 即成功（部分成功 = 成功）
    """
    url = fill_template(identity, config.template_placeholders, today)
    try:
        content = fetch_text(url, config.timeout_sec)
    except FetchError:
        return False, []
    nodes = parse_content(content)
    return True, nodes


def compute_today_str(config: Config) -> str:
    """按配置时区计算今天的日期字符串（用于 {Ymd} 等占位符填充）。"""
    from zoneinfo import ZoneInfo

    return datetime.now(ZoneInfo(config.timezone)).strftime("%Y%m%d")
