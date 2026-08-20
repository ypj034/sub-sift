"""占位符替换与链接预校验工具测试（DESIGN.md §8）。"""
from datetime import date

import pytest

from modules.fetcher.http import FetchError, download_to_file, fetch_bytes
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
