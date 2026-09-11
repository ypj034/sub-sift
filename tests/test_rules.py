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
from modules.rules.server_denylist import ServerDenylistRule
from modules.rules.suspicious_pattern import SuspiciousPatternRule
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


def test_validity_fields_jamming_marker():
    """伊朗反 v2ray 干扰标记（密码内嵌 banv2ray）必须 REJECT。"""
    rule = ValidityFieldsRule()
    for proto in ("trojan", "hysteria2", "ss"):
        bad = node(protocol=proto, raw={"password": "-----------BanV2ray-----------", "method": "aes-128-gcm"})
        assert rule.evaluate(bad).rejected
    # 大小写不敏感
    mixed = node(protocol="trojan", raw={"password": "xx-banv2ray-yy"})
    assert rule.evaluate(mixed).rejected
    # URL 编码形式（%42%61%6e%56%32%72%61%79 = BanV2ray）必须同样 REJECT
    for enc in ("%42%61%6e%56%32%72%61%79", "-----Ban%56%32ray-----"):
        encoded = node(protocol="trojan", raw={"password": enc})
        assert rule.evaluate(encoded).rejected
    # 正常密码不受影响
    ok = node(protocol="trojan", raw={"password": "normal-password-123"})
    assert rule.evaluate(ok).rejected is False


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


def test_junk_keywords_null_config_no_filter():
    """config 留空 [] 或误写 [null] 都不得产生 'none' 关键词。"""
    empty = JunkKeywordsRule([])
    null_entry = JunkKeywordsRule([None])
    assert empty.evaluate(node(name="none-named-node")).rejected is False
    assert null_entry.evaluate(node(name="none-named-node")).rejected is False


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


def test_server_denylist_speedtest():
    """测速站注册域（含任意子域）必须 REJECT，原因 fake_server。"""
    rule = ServerDenylistRule()
    for server in ("speedtest.net", "www.speedtest.net", "3.speedtest.net",
                   "fast.com", "openspeedtest.com", "speedtest.org",
                   "xxx.speedtestcustom.com"):
        r = rule.evaluate(node(server=server))
        assert r.rejected and r.reason == RejectReason.FAKE_SERVER, server


def test_server_denylist_connectivity_host():
    """知名服务子域走完整 host 精确匹配，品牌域本身不受影响。"""
    rule = ServerDenylistRule()
    for server in ("speed.cloudflare.com", "connectivitycheck.gstatic.com",
                   "captive.apple.com", "detectportal.firefox.com",
                   "cp.cloudflare.com", "neverssl.com"):
        r = rule.evaluate(node(server=server))
        assert r.rejected and r.reason == RejectReason.FAKE_SERVER, server
    # 品牌域与无关子域必须 PASS（防止误杀整个 cloudflare/google/apple）
    for server in ("cloudflare.com", "sub.cloudflare.com", "workers.dev",
                   "google.com", "gstatic.com", "apple.com", "clients3.example.com"):
        assert rule.evaluate(node(server=server)).rejected is False, server


def test_server_denylist_poison_domain():
    """已知投毒域名（A2）必须 REJECT。"""
    rule = ServerDenylistRule()
    for server in ("poki-pakipon.ir", "ededed-66.poki-pakipon.ir",
                   "165c182d369eb7bc.mbcloudy.ir", "omdr.whooisthebest.ir"):
        r = rule.evaluate(node(server=server))
        assert r.rejected and r.reason == RejectReason.FAKE_SERVER, server


def test_server_denylist_no_substring_false_positive():
    """绝不用子串匹配：合法注册域带 speedtest 字样不得误伤。"""
    rule = ServerDenylistRule()
    for server in ("speedtesty.xyz", "myspeedtest.net", "speedtest-custom.example.com"):
        assert rule.evaluate(node(server=server)).rejected is False, server


def test_server_denylist_skip_ip_and_extra():
    """IP/IPv6 不适用；config 追加项生效。"""
    rule = ServerDenylistRule()
    assert rule.evaluate(node(server="1.2.3.4")).rejected is False
    assert rule.evaluate(node(server="2001:db8::1")).rejected is False

    rule2 = ServerDenylistRule(
        extra_domains=["evil.test"],
        extra_hosts=["speed.example.com"],
    )
    assert rule2.evaluate(node(server="sub.evil.test")).rejected
    assert rule2.evaluate(node(server="speed.example.com")).rejected
    # 追加项只精确匹配自身，不扩大范围
    assert rule2.evaluate(node(server="other.example.com")).rejected is False
    assert rule2.evaluate(node(server="evil2.test")).rejected is False


def test_suspicious_pattern_triple_hit():
    """三条件同时命中（长随机域名 + sni 知名站 + 非标端口）→ REJECT。"""
    rule = SuspiciousPatternRule()
    n = node(server="random-random-random12345.example.com", port=9999,
             raw={"sni": "play.google.com"})
    r = rule.evaluate(n)
    assert r.rejected and r.reason == RejectReason.HEURISTIC_POISON
    # sni 子域同理
    n2 = node(server="abc-def-ghi-jklm.example.com", port=18020,
              raw={"sni": "dl.google.com"})
    assert rule.evaluate(n2).rejected


def test_suspicious_pattern_no_false_positive():
    """任何一条条件不满足都不得 REJECT（正常 Reality/中转节点）。"""
    rule = SuspiciousPatternRule()
    long_host = "long-random-host-123456789.example.com"
    # 条件3 排除：标准端口 443
    assert rule.evaluate(node(server=long_host, port=443,
                              raw={"sni": "google.com"})).rejected is False
    # 条件3 排除：其他常见代理端口
    assert rule.evaluate(node(server=long_host, port=8080,
                              raw={"sni": "apple.com"})).rejected is False
    # 条件1 排除：短域名
    assert rule.evaluate(node(server="abc.example.com", port=9999,
                              raw={"sni": "google.com"})).rejected is False
    # 条件1 排除：server 是 IP（Reality 标准形态）
    assert rule.evaluate(node(server="1.2.3.4", port=9999,
                              raw={"sni": "google.com"})).rejected is False
    # 条件2 排除：sni 是自家域名（CDN 中转形态）
    assert rule.evaluate(node(server=long_host, port=9999,
                              raw={"sni": "mydomain.example"})).rejected is False
    # 条件2 排除：无 sni
    assert rule.evaluate(node(server=long_host, port=9999)).rejected is False


def test_suspicious_pattern_extra():
    """config 追加标准端口 / 知名站生效。"""
    rule = SuspiciousPatternRule(extra_std_ports=[9999])
    assert rule.evaluate(node(server="long-random-host-123456789.example.com",
                              port=9999, raw={"sni": "google.com"})).rejected is False
    rule2 = SuspiciousPatternRule(extra_famous_hosts=["example.edu.cn"])
    assert rule2.evaluate(node(server="long-random-host-123456789.example.com",
                               port=9999, raw={"sni": "www.example.edu.cn"})).rejected
