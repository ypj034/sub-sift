"""订阅输出序列化测试：IPv6 方括号包裹、格式正确性。"""
from modules.common.node import Node
from modules.store.output import _host, node_to_uri


def make_node(protocol, server, port=443, name="n", raw=None):
    return Node(
        protocol=protocol,
        server=server,
        port=port,
        name=name,
        raw=raw or {},
    )


def test_host_ipv6_wrapped():
    assert _host("2001:db8::1") == "[2001:db8::1]"
    assert _host("1.2.3.4") == "1.2.3.4"
    assert _host("cdn.example.com") == "cdn.example.com"


def test_node_to_uri_ipv6_vless():
    n = make_node(
        "vless",
        "2001:19f0:7001:150:5400:6ff:fe44:1cfd",
        443,
        "ipv6-node",
        {"uuid": "123e4567-e89b-12d3-a456-426614174000", "tls": True},
    )
    uri = node_to_uri(n)
    assert uri.startswith("vless://123e4567-e89b-12d3-a456-426614174000@[2001:19f0:7001:150:5400:6ff:fe44:1cfd]:443?")
    assert "#ipv6-node" in uri


def test_node_to_uri_ipv6_trojan():
    n = make_node(
        "trojan",
        "2401:c080:1000:1443:5400:6ff:fe41:a334",
        443,
        "tj6",
        {"password": "pw-123", "sni": "x.example.com"},
    )
    uri = node_to_uri(n)
    assert uri.startswith("trojan://pw-123@[2401:c080:1000:1443:5400:6ff:fe41:a334]:443?")


def test_node_to_uri_ipv4_and_domain_unchanged():
    v4 = make_node("vless", "1.2.3.4", 443, "v4", {"uuid": "123e4567-e89b-12d3-a456-426614174000"})
    assert "@1.2.3.4:443?" in node_to_uri(v4)
    dom = make_node("vless", "cdn.example.com", 8443, "dom", {"uuid": "123e4567-e89b-12d3-a456-426614174000"})
    assert "@cdn.example.com:8443?" in node_to_uri(dom)
