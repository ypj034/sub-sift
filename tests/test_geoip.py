"""GeoIP 查询测试：内置表兜底与 mmdb 降级。"""
import os

from modules.common.geoip import GeoIP


def test_builtin_fallback_when_no_mmdb(tmp_path):
    g = GeoIP(mmdb_path=str(tmp_path / "nope.mmdb"))
    assert g.source == "builtin"


def test_lookup_specific_segment_wins(tmp_path):
    """小段（HK 14.198/16）优先于大段（CN 14.0.0.0/8）匹配。"""
    g = GeoIP(mmdb_path=str(tmp_path / "nope.mmdb"))
    assert g.lookup("14.198.1.1") == "HK"


def test_lookup_hit_and_miss(tmp_path):
    g = GeoIP(mmdb_path=str(tmp_path / "nope.mmdb"))
    assert g.lookup("45.255.255.1") == "US"
    assert g.lookup("1.1.1.1") is None  # 未命中


def test_lookup_invalid_ip(tmp_path):
    g = GeoIP(mmdb_path=str(tmp_path / "nope.mmdb"))
    assert g.lookup("not-an-ip") is None


def test_lookup_ipv6_builtin_none(tmp_path):
    """内置表不含 IPv6，返回 None 且不抛异常。"""
    g = GeoIP(mmdb_path=str(tmp_path / "nope.mmdb"))
    assert g.lookup("2001:4860:4860::8888") is None


def test_corrupt_mmdb_falls_back_to_builtin(tmp_path):
    p = tmp_path / "bad.mmdb"
    p.write_bytes(b"this is not a mmdb file")
    g = GeoIP(mmdb_path=str(p))
    assert g.source == "builtin"
    assert g.lookup("45.255.255.1") == "US"
