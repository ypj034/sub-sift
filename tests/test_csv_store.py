"""CSV store 测试：聚合源去重、主清单列序与冷却格式。"""
import csv
import textwrap

from modules.common.config import Config, load_config
from modules.statemachine.engine import SubscriptionState, WindowEntry
from modules.store.csv_store import (
    SubscriptionRow,
    write_aggregators,
    write_subscriptions,
)


def _load_cfg(tmp_path) -> Config:
    cfg_text = textwrap.dedent(
        f"""\
        schema_version: 1
        timezone: "Asia/Shanghai"
        fetcher:
          concurrency: 5
          timeout_sec: 20
        stats:
          window_size: 30
        state_machine:
          cooldown_failures: 4
          cooldown_days: [3, 7]
          disable_failures: 4
        rules:
          protocol_allowlist: {{enabled: true, allow: [vless, trojan, vmess, ss, hysteria2]}}
          validity_target: {{enabled: true}}
          validity_fields: {{enabled: true}}
          security_vmess: {{enabled: true}}
          security_vless: {{enabled: true}}
          security_trojan: {{enabled: true}}
          security_ss: {{enabled: true}}
          security_hysteria2: {{enabled: true}}
          junk_keywords: {{enabled: true, keywords: [free, test]}}
          region_allowlist: {{enabled: true, allow: [JP, SG]}}
        output:
          formats: [plain]
          directory: {tmp_path.as_posix()}
        """
    )
    p = tmp_path / "config.yaml"
    p.write_text(cfg_text, encoding="utf-8")
    return load_config(str(p))


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


def test_write_aggregators_header_and_pass_rate(tmp_path):
    path = str(tmp_path / "aggregators.csv")
    rows = [{"id": "a", "link": "https://a.example"}]
    windows = {
        "a": [
            WindowEntry(ts="2026-08-19", ok=True, count=3),
            WindowEntry(ts="2026-08-20", ok=False, count=0),
        ],
    }
    write_aggregators(path, rows, windows, "2026-08-20")
    with open(path, encoding="utf-8-sig") as f:
        lines = list(csv.reader(f))
    assert lines[0] == ["id", "link", "pass_rate", "last_count", "avg_count", "last_run"]
    rec = dict(zip(lines[0], lines[1]))
    assert rec["pass_rate"] == "1/2"
    assert rec["last_count"] == "0"
    assert rec["avg_count"] == "1.5"
    assert rec["last_run"] == "2026-08-20"


def test_write_subscriptions_columns_and_cooldown(tmp_path):
    cfg = _load_cfg(tmp_path)
    rows = [SubscriptionRow(link="https://a.example", sources=["manual"])]
    states = {
        "https://a.example": SubscriptionState(
            link="https://a.example",
            cooldown_until="2026-08-25",
            window=[WindowEntry(ts="2026-08-20", ok=False, count=0)],
        )
    }
    path = str(tmp_path / "subscriptions.csv")
    write_subscriptions(path, rows, states, {}, "20260820", cfg)
    with open(path, encoding="utf-8-sig") as f:
        lines = list(csv.reader(f))
    expected_header = (
        ["link", "sources", "state", "pass_rate", "avg", "last"]
        + cfg.protocol_allowlist
        + list(cfg.region_allowlist)
        + ["domain", "last_run"]
    )
    assert lines[0] == expected_header
    rec = dict(zip(lines[0], lines[1]))
    # 冷却格式 cd_MMDD；列名 pass_rate；last_run 位于最右列
    assert rec["state"] == "cd_0825"
    assert rec["pass_rate"] == "0/1"
    assert rec["last_run"] == "2026-08-20"
