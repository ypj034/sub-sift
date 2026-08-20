"""报告生成测试：主清单规则分组列、状态分组排序、排序键。"""
import textwrap
from datetime import date

from modules.common.config import Config, load_config
from modules.report.generator import (
    _main_sort_key,
    _rule_group_cells,
    _state_rank,
    generate_report,
)
from modules.statemachine.engine import SubscriptionState, WindowEntry
from modules.store.csv_store import SubscriptionRow


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


def test_rule_group_cells():
    # 未拉取（None）→ 5 列全部留空
    assert _rule_group_cells(None) == ["", "", "", "", ""]
    # 分组聚合：validity 两规则并入"无效"，security_vless 入"非加密"，rejected 为合计
    info = {
        "rejected": 42,
        "rule_counts": {
            "validity_target": 20,
            "validity_fields": 10,
            "security_vless": 12,
        },
    }
    assert _rule_group_cells(info) == ["30", "12", "0", "0", "42"]
    # 无 rule_counts → 各列 0，合计取 rejected
    assert _rule_group_cells({"rejected": 5}) == ["0", "0", "0", "0", "5"]


def test_state_rank_group_order():
    today = date(2026, 8, 20)
    active = SubscriptionState(link="a")
    cooldown = SubscriptionState(link="b", cooldown_until="2026-08-25")
    disabled = SubscriptionState(link="c", disabled=True)
    assert _state_rank(active, today) == 0
    assert _state_rank(cooldown, today) == 1
    assert _state_rank(disabled, today) == 2
    assert _state_rank(None, today) == 0
    # 冷却已过 → 归 active 组
    expired = SubscriptionState(link="d", cooldown_until="2026-08-10")
    assert _state_rank(expired, today) == 0


def _state_with(entries) -> SubscriptionState:
    s = SubscriptionState(link="x")
    for ok, count in entries:
        s.window.append(WindowEntry(ts="2026-08-01", ok=ok, count=count))
    return s


def test_main_sort_key_avg_desc_then_success_rate():
    today = date(2026, 8, 20)
    high_avg = _state_with([(True, 100), (True, 120)])
    low_avg = _state_with([(True, 10), (True, 20)])
    # avg 降序：高 avg 排前
    assert _main_sort_key(high_avg, today) < _main_sort_key(low_avg, today)

    same_avg_better_sr = _state_with([(True, 10), (True, 20)])
    same_avg_worse_sr = _state_with([(True, 10), (False, 20)])
    # 同 avg（15）时 success_rate 高者排前
    assert _main_sort_key(same_avg_better_sr, today) < _main_sort_key(same_avg_worse_sr, today)

    # 无记录排组尾
    assert _main_sort_key(None, today) > _main_sort_key(same_avg_worse_sr, today)


def test_generate_report_structure(tmp_path):
    cfg = _load_cfg(tmp_path)
    today = date(2026, 8, 20)

    sub_rows = [
        SubscriptionRow(link="https://disabled.example/x", sources=["manual"]),
        SubscriptionRow(link="https://active.example/y", sources=["manual"]),
    ]
    sub_states = {
        "https://active.example/y": _state_with([(True, 100), (True, 50)]),
        "https://disabled.example/x": SubscriptionState(
            link="https://disabled.example/x",
            window=[WindowEntry(ts="2026-08-01", ok=True, count=1000)],
            disabled=True,
        ),
    }
    ctx = {
        "run_time": "2026-08-20 12:00:00 CST",
        "today": today,
        "sub_rows": sub_rows,
        "sub_states": sub_states,
        "per_link": {
            "https://active.example/y": {
                "ok": True,
                "count": 150,
                "rejected": 42,
                "rule_counts": {"validity_target": 30, "security_vless": 12},
            },
        },
        "skipped": 0,
        "merged_count": 0,
        "geoip_source": "-",
        "agg_rows": [],
        "agg_windows": {},
        "output_files": {"plain": "plain.txt"},
    }
    path = generate_report(cfg, ctx)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # 规则计数器章节已删除（含规则级中文名、异常计数）
    assert "## 规则计数器" not in content
    assert "字段有效性" not in content
    assert "validity_target" not in content
    assert "validity_fields" not in content

    # 主清单：中文表头、状态/成功率列居中、规则分组列、无 total 列、无重叠度章节
    assert "| 链接 | 状态 | 成功率 | 最近 | 平均 | 无效 | 非加密 | 排除协议 | 排除地区 | 排除合计 |" in content
    assert "| --- | :---: | :---: | --- | --- | --- | --- | --- | --- | --- |" in content
    assert "total" not in content
    assert "## 重叠度" not in content
    assert "## 主清单（active → 冷却 → disabled；组内按 avg 降序）" in content
    # 排序：active 组在 disabled 组之前
    assert content.index("https://active.example/y") < content.index("https://disabled.example/x")

    # 规则列：已拉取链接显示分组聚合值，未拉取（禁用）链接留空
    line_active = next(l for l in content.splitlines() if "https://active.example/y" in l)
    cells_active = [c.strip() for c in line_active.split("|")]
    assert cells_active[6:11] == ["30", "12", "0", "0", "42"]
    line_disabled = next(l for l in content.splitlines() if "https://disabled.example/x" in l)
    cells_disabled = [c.strip() for c in line_disabled.split("|")]
    assert cells_disabled[6:11] == ["", "", "", "", ""]
