"""配置加载与校验测试。"""
import os
import textwrap

import pytest

from modules.common.config import ConfigError, load_config

VALID = textwrap.dedent("""\
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
      protocol_allowlist: {enabled: true, allow: [vless, trojan, vmess, ss, hysteria2]}
      validity_target: {enabled: true}
      validity_fields: {enabled: true}
      security_vmess: {enabled: true}
      security_vless: {enabled: true}
      security_trojan: {enabled: true}
      security_ss: {enabled: true}
      security_hysteria2: {enabled: true}
      junk_keywords: {enabled: true, keywords: [free, test]}
      region_allowlist: {enabled: true, allow: [JP, SG]}
    output:
      formats: [clash, v2ray]
""")


def _write(tmp_path, content):
    p = tmp_path / "config.yaml"
    p.write_text(content, encoding="utf-8")
    return str(p)


def test_valid_config(tmp_path):
    cfg = load_config(_write(tmp_path, VALID))
    assert cfg.concurrency == 5
    assert cfg.timeout_sec == 20
    assert cfg.window_size == 30
    assert cfg.active_rules[0] == "protocol_allowlist"
    assert cfg.output_formats == ["clash", "v2ray"]
    assert "JP" in cfg.region_allowlist


def test_schema_version_mismatch(tmp_path):
    bad = VALID.replace("schema_version: 1", "schema_version: 2")
    with pytest.raises(ConfigError, match="schema_version"):
        load_config(_write(tmp_path, bad))


def test_unknown_protocol(tmp_path):
    bad = VALID.replace("allow: [vless, trojan, vmess, ss, hysteria2]",
                        "allow: [vless, socks5]")
    with pytest.raises(ConfigError, match="socks5"):
        load_config(_write(tmp_path, bad))


def test_security_rule_missing(tmp_path):
    """白名单内协议缺少对应安全规则 → 启动报错。"""
    bad = VALID.replace("security_vless: {enabled: true}",
                        "security_vless: {enabled: false}")
    with pytest.raises(ConfigError, match="security_vless"):
        load_config(_write(tmp_path, bad))


def test_invalid_output_format(tmp_path):
    bad = VALID.replace("formats: [clash, v2ray]", "formats: [clash, surge]")
    with pytest.raises(ConfigError, match="surge"):
        load_config(_write(tmp_path, bad))


def test_missing_file(tmp_path):
    with pytest.raises(ConfigError, match="不存在"):
        load_config(str(tmp_path / "nope.yaml"))


def test_env_override(tmp_path, monkeypatch):
    monkeypatch.setenv("SQM_FETCHER_CONCURRENCY", "8")
    cfg = load_config(_write(tmp_path, VALID))
    assert cfg.concurrency == 8


def test_template_placeholder_validation(tmp_path):
    # 未配置时使用默认占位符（合法）
    cfg = load_config(_write(tmp_path, VALID))
    assert cfg.template_placeholders == ["{Ymd}"]


def test_unknown_placeholder_rejected(tmp_path):
    bad = VALID.replace(
        "  timeout_sec: 20\n",
        "  timeout_sec: 20\n  template_placeholders: ['{foo}']\n",
    )
    with pytest.raises(ConfigError, match="占位符"):
        load_config(_write(tmp_path, bad))


def test_known_placeholders_accepted(tmp_path):
    good = VALID.replace(
        "  timeout_sec: 20\n",
        "  timeout_sec: 20\n  template_placeholders: ['{Ymd}', '{Y}', '{mm}', '{d}']\n",
    )
    cfg = load_config(_write(tmp_path, good))
    assert cfg.template_placeholders == ["{Ymd}", "{Y}", "{mm}", "{d}"]


def test_plain_output_format(tmp_path):
    good = VALID.replace(
        "formats: [clash, v2ray]", "formats: [clash, v2ray, plain]"
    )
    cfg = load_config(_write(tmp_path, good))
    assert cfg.output_formats == ["clash", "v2ray", "plain"]


def test_geo_mmdb_url_default(tmp_path):
    cfg = load_config(_write(tmp_path, VALID))
    assert cfg.geo_mmdb_url == ""


def test_geo_mmdb_url_valid(tmp_path):
    good = VALID + 'geo:\n  mmdb_url: "https://example.com/country.mmdb"\n'
    cfg = load_config(_write(tmp_path, good))
    assert cfg.geo_mmdb_url == "https://example.com/country.mmdb"


def test_geo_mmdb_url_invalid(tmp_path):
    bad = VALID + 'geo:\n  mmdb_url: "ftp://example.com/country.mmdb"\n'
    with pytest.raises(ConfigError, match="http"):
        load_config(_write(tmp_path, bad))
