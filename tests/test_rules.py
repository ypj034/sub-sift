"""规则行为测试：每条规则 PASS/REJECT 语义。"""
from modules.common.enums import RejectReason
from modules.common.node import Node
from modules.rules.junk_keywords import JunkKeywordsRule
from modules.rules.protocol_allowlist import ProtocolAllowlistRule
from modules.rules.region_allowlist import RegionAllowlistRule
from modules.rules.security_hysteria2 import SecurityHysteria2Rule
from modules.rules.security_ss import SecuritySsRule
from modules.rules.security_trojan import SecurityTrojanRule
from modules.rules.security_vless import SecurityVlessRule
from modules.rules.security_vmess import SecurityVmessRule
from modules.rules.validity_fields import ValidityFieldsRule
from modules.rules.validity_target import ValidityTargetRule

UUID = "123e4567-e89b-12d3-a456-426614174000"


def node(protocol="vless", server="1.2.3.4", port=443, name="n", raw=None):
    return Node(protocol=protocol, server=server, port=port, name=name, raw=raw or {})


def test_protocol_allowlist():
    rule = ProtocolAllowlistRule(["vless", "trojan"])
    assert rule.evaluate(node(protocol="vless")).rejected is False
    r = rule.evaluate(node(protocol="ss"))
    assert r.rejected is True
    assert r.reason == RejectReason.PROTOCOL_NOT_ALLOWED


def test_validity_target_private_ip():
    rule = ValidityTargetRule()
    r = rule.evaluate(node(server="127.0.0.1"))
    assert r.rejected and r.reason == RejectReason.INVALID_TARGET
    r = rule.evaluate(node(server="192.168.1.1"))
    assert r.rejected
    r = rule.evaluate(node(server="10.0.0.1"))
    assert r.rejected


def test_validity_target_reserved_domain():
    rule = ValidityTargetRule()
    assert rule.evaluate(node(server="example.com")).rejected
    assert rule.evaluate(node(server="localhost")).rejected
    assert rule.evaluate(node(server="sub.test")).rejected
    assert rule.evaluate(node(server="ok.example.com")).rejected


def test_validity_target_valid_domain():
    rule = ValidityTargetRule()
    assert rule.evaluate(node(server="cdn.example.net.cn")).rejected is False


def test_validity_fields_uuid():
    rule = ValidityFieldsRule()
    bad = node(protocol="vless", raw={"uuid": "not-a-uuid"})
    assert rule.evaluate(bad).rejected
    zero = node(protocol="vless", raw={"uuid": "00000000-0000-0000-0000-000000000000"})
    assert rule.evaluate(zero).rejected
    ok = node(protocol="vless", raw={"uuid": UUID})
    assert rule.evaluate(ok).rejected is False


def test_validity_fields_password():
    rule = ValidityFieldsRule()
    assert rule.evaluate(node(protocol="trojan", raw={"password": ""})).rejected
    assert rule.evaluate(node(protocol="trojan", raw={"password": "0000"})).rejected
    assert rule.evaluate(node(protocol="trojan", raw={"password": "good-pw"})).rejected is False
    assert rule.evaluate(node(protocol="ss", raw={"method": "", "password": "x"})).rejected


def test_security_vmess():
    rule = SecurityVmessRule()
    ok = node(protocol="vmess", raw={"cipher": "auto", "tls": True})
    assert rule.evaluate(ok).rejected is False
    weak = node(protocol="vmess", raw={"cipher": "aes-128-cfb", "tls": True})
    assert rule.evaluate(weak).rejected and rule.evaluate(weak).reason == RejectReason.UNSAFE_WEAK_CIPHER
    notls = node(protocol="vmess", raw={"cipher": "auto", "tls": False})
    assert rule.evaluate(notls).rejected and rule.evaluate(notls).reason == RejectReason.UNSAFE_NO_TLS


def test_security_vless():
    rule = SecurityVlessRule()
    ok = node(protocol="vless", raw={"tls": True, "allowInsecure": False})
    assert rule.evaluate(ok).rejected is False
    plain = node(protocol="vless", raw={"tls": False, "reality": False})
    assert rule.evaluate(plain).rejected and rule.evaluate(plain).reason == RejectReason.UNSAFE_NO_TLS
    reality = node(protocol="vless", raw={"tls": False, "reality": True})
    assert rule.evaluate(reality).rejected is False
    insecure = node(protocol="vless", raw={"tls": True, "allowInsecure": True})
    assert rule.evaluate(insecure).rejected and rule.evaluate(insecure).reason == RejectReason.UNSAFE_ALLOW_INSECURE


def test_security_trojan():
    rule = SecurityTrojanRule()
    ok = node(protocol="trojan", raw={"tls": True, "allowInsecure": False})
    assert rule.evaluate(ok).rejected is False
    notls = node(protocol="trojan", raw={"tls": False})
    assert rule.evaluate(notls).rejected and rule.evaluate(notls).reason == RejectReason.UNSAFE_NO_TLS
    insecure = node(protocol="trojan", raw={"tls": True, "allowInsecure": True})
    assert rule.evaluate(insecure).rejected and rule.evaluate(insecure).reason == RejectReason.UNSAFE_ALLOW_INSECURE


def test_security_ss():
    rule = SecuritySsRule()
    ok = node(protocol="ss", raw={"method": "aes-256-gcm"})
    assert rule.evaluate(ok).rejected is False
    weak = node(protocol="ss", raw={"method": "rc4-md5"})
    assert rule.evaluate(weak).rejected and rule.evaluate(weak).reason == RejectReason.UNSAFE_WEAK_CIPHER
    empty = node(protocol="ss", raw={"method": ""})
    assert rule.evaluate(empty).rejected


def test_security_hysteria2():
    rule = SecurityHysteria2Rule()
    ok = node(protocol="hysteria2", raw={"insecure": False})
    assert rule.evaluate(ok).rejected is False
    bad = node(protocol="hysteria2", raw={"insecure": True})
    assert rule.evaluate(bad).rejected and rule.evaluate(bad).reason == RejectReason.UNSAFE_ALLOW_INSECURE


def test_junk_keywords():
    rule = JunkKeywordsRule(["free", "测试"])
    assert rule.evaluate(node(name="免费机场-测试节点")).rejected
    assert rule.evaluate(node(name="free-test")).rejected
    assert rule.evaluate(node(server="freecdn.example.com")).rejected
    assert rule.evaluate(node(name="香港 01", server="hk01.example.com")).rejected is False


class _FakeGeoIP:
    def __init__(self, table):
        self._table = table

    def lookup(self, ip):
        return self._table.get(ip)


def test_region_allowlist():
    geoip = _FakeGeoIP({"1.2.3.4": "JP"})
    rule = RegionAllowlistRule(["JP", "SG"], geoip)
    ok = node(server="1.2.3.4")
    result = rule.evaluate(ok)
    assert result.rejected is False
    assert ok.region == "JP"
    # IP 不在白名单
    geoip2 = _FakeGeoIP({"5.6.7.8": "US"})
    rule2 = RegionAllowlistRule(["JP"], geoip2)
    r = rule2.evaluate(node(server="5.6.7.8"))
    assert r.rejected and r.reason == RejectReason.REGION_NOT_ALLOWED
    # IP 查不到
    rule3 = RegionAllowlistRule(["JP"], _FakeGeoIP({}))
    r = rule3.evaluate(node(server="9.9.9.9"))
    assert r.rejected
    # 域名型跳过
    r = rule.evaluate(node(server="example.net.cn"))
    assert r.rejected is False


def test_security_rules_skip_other_protocol():
    """安全规则只对自己协议的节点生效。"""
    rule = SecurityVmessRule()
    assert rule.evaluate(node(protocol="trojan", raw={"tls": False})).rejected is False
