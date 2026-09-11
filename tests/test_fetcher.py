"""占位符替换与链接预校验工具测试（DESIGN.md §8）。"""
from datetime import date

import pytest

from modules.common.config import Config
from modules.fetcher.http import FetchError, download_to_file, fetch_bytes
import modules.fetcher.subscription as sub_mod
from modules.fetcher.subscription import (
    extract_placeholders,
    fill_template,
    placeholder_values,
)

TODAY = date(2026, 8, 20)


def test_placeholder_values():
    v = placeholder_values(TODAY)
    assert v == {
        "{Y}": "2026",
        "{m}": "8",
        "{mm}": "08",
        "{d}": "20",
        "{dd}": "20",
        "{Ymd}": "20260820",
        "{ymd}": "20260820",
    }


def test_extract_placeholders():
    url = "https://xxx/uploads/{Y}/{mm}/0-{Ymd}.yaml"
    assert extract_placeholders(url) == {"{Y}", "{mm}", "{Ymd}"}


def test_extract_placeholders_none():
    assert extract_placeholders("https://plain.example/sub") == set()


def test_fill_template_multi_placeholder():
    url = "https://xxx/uploads/{Y}/{mm}/0-{Ymd}.yaml"
    out = fill_template(url, ["{Y}", "{mm}", "{Ymd}"], TODAY)
    assert out == "https://xxx/uploads/2026/08/0-20260820.yaml"


def test_fill_template_ignores_non_whitelist():
    url = "https://xxx/{Y}/{other}.yaml"
    out = fill_template(url, ["{Y}"], TODAY)
    # 非白名单占位符保留原样（启动预校验会拦截，这里仅验证替换行为）
    assert out == "https://xxx/2026/{other}.yaml"


def test_fill_template_no_placeholder():
    assert fill_template("https://plain.example/sub", [], TODAY) == "https://plain.example/sub"


def _raise(urlopen, exc):
    def fake_urlopen(req, timeout):
        raise exc
    return fake_urlopen


def test_fetch_bytes_converges_remote_disconnected(monkeypatch):
    """RemoteDisconnected（OSError 子类）必须收敛为 FetchError，不能穿透。"""
    from http.client import RemoteDisconnected

    import modules.fetcher.http as http_mod

    monkeypatch.setattr(
        http_mod.urllib.request, "urlopen", _raise("", RemoteDisconnected("remote closed"))
    )
    with pytest.raises(FetchError):
        fetch_bytes("https://example.invalid/sub")


def test_fetch_bytes_converges_connection_reset(monkeypatch):
    """ConnectionResetError 同样收敛（urllib 在部分平台表现为该类型）。"""
    import modules.fetcher.http as http_mod

    monkeypatch.setattr(
        http_mod.urllib.request, "urlopen", _raise("", ConnectionResetError(104))
    )
    with pytest.raises(FetchError):
        fetch_bytes("https://example.invalid/sub")


def test_fetch_bytes_converges_incomplete_read(monkeypatch):
    """IncompleteRead（HTTPException 子类，非 OSError）同样必须收敛。"""
    from http.client import IncompleteRead

    import modules.fetcher.http as http_mod

    monkeypatch.setattr(
        http_mod.urllib.request, "urlopen", _raise("", IncompleteRead(b"x" * 10, 20))
    )
    with pytest.raises(FetchError):
        fetch_bytes("https://example.invalid/sub")


def test_download_to_file_converges_oserror(monkeypatch, tmp_path):
    """download_to_file 的 OSError 兜底同样收敛为 FetchError。"""
    import modules.fetcher.http as http_mod

    monkeypatch.setattr(
        http_mod.urllib.request, "urlopen", _raise("", ConnectionResetError(104))
    )
    with pytest.raises(FetchError):
        download_to_file("https://example.invalid/sub", str(tmp_path / "x.bin"))


# ---------------------------------------------------------------------------
# 模板链接日期容错（config.fetcher.date_offsets，DESIGN.md §8）
# ---------------------------------------------------------------------------

def _cfg(date_offsets=(0, -1, 1)):
    """构造最小 Config（仅含 fetch_subscription_nodes 所需字段）。"""
    return Config(
        schema_version=1,
        timezone="UTC",
        display_timezone="Asia/Shanghai",
        concurrency=1,
        timeout_sec=5,
        template_placeholders=["{Ymd}"],
        date_offsets=list(date_offsets),
        window_size=30,
        cooldown_failures=4,
        cooldown_days=[3, 7],
        disable_failures=4,
        rules={},
        output_formats=["plain"],
        output_directory="output",
        geo_mmdb_url="",
    )


def _patch_fetch(monkeypatch, handler):
    """替换 fetch_text；handler(url) 返回内容或抛 FetchError。"""
    monkeypatch.setattr(sub_mod, "fetch_text", lambda url, timeout: handler(url))


def test_template_hits_today_and_stops(monkeypatch):
    urls = []

    def handler(url):
        urls.append(url)
        if "20260820" in url:
            return "content"
        raise FetchError("miss")

    _patch_fetch(monkeypatch, handler)
    monkeypatch.setattr(sub_mod, "parse_content", lambda c: ["node"])
    ok, nodes, offset = sub_mod.fetch_subscription_nodes(
        "https://x/{Ymd}.txt", _cfg(), TODAY
    )
    assert (ok, nodes, offset) == (True, ["node"], 0)
    assert urls == ["https://x/20260820.txt"]  # 命中即停，不再试其他日期


def test_template_falls_back_to_previous_day(monkeypatch):
    def handler(url):
        if "20260819" in url:  # today - 1
            return "content"
        raise FetchError("miss")

    _patch_fetch(monkeypatch, handler)
    monkeypatch.setattr(sub_mod, "parse_content", lambda c: ["node"])
    ok, nodes, offset = sub_mod.fetch_subscription_nodes(
        "https://x/{Ymd}.txt", _cfg(), TODAY
    )
    assert (ok, nodes, offset) == (True, ["node"], -1)


def test_template_all_offsets_fail(monkeypatch):
    def handler(url):
        raise FetchError("miss")

    _patch_fetch(monkeypatch, handler)
    ok, nodes, offset = sub_mod.fetch_subscription_nodes(
        "https://x/{Ymd}.txt", _cfg(), TODAY
    )
    assert (ok, nodes, offset) == (False, [], None)


def test_preferred_offset_is_tried_first(monkeypatch):
    urls = []

    def handler(url):
        urls.append(url)
        return "content"

    _patch_fetch(monkeypatch, handler)
    monkeypatch.setattr(sub_mod, "parse_content", lambda c: ["node"])
    ok, nodes, offset = sub_mod.fetch_subscription_nodes(
        "https://x/{Ymd}.txt", _cfg(), TODAY, preferred_offset=1
    )
    assert offset == 1
    assert urls == ["https://x/20260821.txt"]  # 记忆偏移优先且命中即停


def test_plain_link_fetches_once(monkeypatch):
    urls = []

    def handler(url):
        urls.append(url)
        return "content"

    _patch_fetch(monkeypatch, handler)
    monkeypatch.setattr(sub_mod, "parse_content", lambda c: [])
    ok, nodes, offset = sub_mod.fetch_subscription_nodes(
        "https://plain.example/sub", _cfg(), TODAY
    )
    assert (ok, offset) == (True, None)  # 非模板链接无日期维度
    assert urls == ["https://plain.example/sub"]


def test_empty_content_continues_to_next_offset(monkeypatch):
    """候选拉取成功但解析出 0 节点 → 继续尝试后续偏移。"""
    urls = []

    def handler(url):
        urls.append(url)
        return "content"

    _patch_fetch(monkeypatch, handler)
    monkeypatch.setattr(sub_mod, "parse_content", lambda c: [])
    ok, nodes, offset = sub_mod.fetch_subscription_nodes(
        "https://x/{Ymd}.txt", _cfg((0, -1)), TODAY
    )
    # 全部候选均无节点 → 取首个拉取成功的候选，保持既有 ok 语义
    assert ok is True
    assert offset == 0
    assert urls == ["https://x/20260820.txt", "https://x/20260819.txt"]
