"""CSV store 测试：write_aggregators 写入去重。"""
import csv

from modules.store.csv_store import write_aggregators


def test_write_aggregators_dedup(tmp_path):
    path = str(tmp_path / "aggregators.csv")
    rows = [
        {"id": "a", "link": "https://a.example"},
        {"id": "a", "link": "https://a.example"},
        {"id": "b", "link": "https://b.example"},
    ]
    write_aggregators(path, rows, {}, "2026-08-20")
    with open(path, encoding="utf-8-sig") as f:
        content = list(csv.DictReader(f))
    assert [r["id"] for r in content] == ["a", "b"]
    assert content[0]["link"] == "https://a.example"


def test_write_aggregators_keeps_unique(tmp_path):
    path = str(tmp_path / "aggregators.csv")
    rows = [
        {"id": "x", "link": "https://x.example"},
        {"id": "y", "link": "https://y.example"},
    ]
    write_aggregators(path, rows, {}, "2026-08-20")
    with open(path, encoding="utf-8-sig") as f:
        content = list(csv.DictReader(f))
    assert [r["id"] for r in content] == ["x", "y"]
