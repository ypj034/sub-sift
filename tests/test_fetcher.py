"""占位符替换与链接预校验工具测试（DESIGN.md §8）。"""
from datetime import date

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
