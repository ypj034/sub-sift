"""订阅解析测试。"""
import base64
import json

from modules.common.node import Node
from modules.fetcher.parser import (
    b64_decode_str,
    parse_clash_yaml,
    parse_content,
    parse_uri_line,
)

UUID = "123e4567-e89b-12d3-a456-426614174000"


def _node(**kw) -> Node:
    defaults = {"protocol": "vless", "server": "1.2.3.4", "port": 443, "name": "n"}
    defaults.update(kw)
    return Node(**defaults)


def test_vmess():
    payload = json.dumps({
        "v": "2", "ps": "T-01", "add": "1.2.3.4", "port": 443,
        "id": UUID, "aid": 0, "net": "tcp", "type": "none", "tls": "tls",
    })
    uri = "vmess://" + base64.b64encode(payload.encode()).decode()
    node = parse_uri_line(uri)
    assert node is not None
    assert node.protocol == "vmess"
    assert node.server == "1.2.3.4"
    assert node.port == 443
    assert node.raw["tls"] is True
    assert node.raw["uuid"] == UUID


def test_vless():
    uri = f"vless://{UUID}@example.com:443?security=tls&sni=example.com&type=tcp#日本01"
    node = parse_uri_line(uri)
    assert node is not None
    assert node.protocol == "vless"
    assert node.raw["tls"] is True
    assert node.raw["sni"] == "example.com"
    assert node.name == "日本01"


def test_vless_reality():
    uri = f"vless://{UUID}@1.2.3.4:443?security=reality&pbk=abc&sid=1234&type=tcp"
    node = parse_uri_line(uri)
    assert node is not None
    assert node.raw["reality"] is True
    assert node.raw["pbk"] == "abc"


def test_trojan():
    uri = "trojan://pass123@example.com:443?sni=example.com#TW-01"
    node = parse_uri_line(uri)
    assert node is not None
    assert node.protocol == "trojan"
    assert node.raw["password"] == "pass123"
    assert node.raw["tls"] is True


def test_ss_sip002():
    userinfo = base64.b64encode(b"aes-256-gcm:secret").decode()
    uri = f"ss://{userinfo}@example.com:8388#SG-01"
    node = parse_uri_line(uri)
    assert node is not None
    assert node.protocol == "ss"
    assert node.raw["method"] == "aes-256-gcm"
    assert node.raw["password"] == "secret"


def test_ss_legacy():
    inner = base64.b64encode(b"chacha20-ietf-poly1305:pw@1.2.3.4:8388").decode()
    uri = f"ss://{inner}#HK-01"
    node = parse_uri_line(uri)
    assert node is not None
    assert node.protocol == "ss"
    assert node.server == "1.2.3.4"
    assert node.port == 8388


def test_hysteria2():
    uri = "hysteria2://pass@1.2.3.4:443?sni=example.com&insecure=1#US-01"
    node = parse_uri_line(uri)
    assert node is not None
    assert node.protocol == "hysteria2"
    assert node.raw["insecure"] is True


def test_ipv6_host():
    uri = f"vless://{UUID}@[2001:db8::1]:443?type=tcp"
    node = parse_uri_line(uri)
    assert node is not None
    assert node.server == "2001:db8::1"
    assert node.port == 443


def test_bad_lines():
    assert parse_uri_line("") is None
    assert parse_uri_line("garbage text") is None
    assert parse_uri_line("https://example.com/sub") is None


def test_parse_content_clash():
    content = """
proxies:
  - name: "JP1"
    type: vmess
    server: 1.2.3.4
    port: 443
    uuid: 123e4567-e89b-12d3-a456-426614174000
    cipher: auto
    tls: true
"""
    nodes = parse_clash_yaml(content)
    assert len(nodes) == 1
    assert nodes[0].protocol == "vmess"
    assert nodes[0].raw["tls"] is True


def test_parse_content_base64_list():
    lines = [
        f"vless://{UUID}@1.2.3.4:443?type=tcp",
        f"trojan://pw@1.2.3.4:443#n2",
    ]
    payload = base64.b64encode("\n".join(lines).encode()).decode()
    nodes = parse_content(payload)
    assert len(nodes) == 2


def test_parse_content_plain_lines():
    lines = [
        f"vless://{UUID}@1.2.3.4:443?type=tcp#A",
        f"vless://{UUID}@1.2.3.5:443?type=tcp#B",
    ]
    nodes = parse_content("\n".join(lines))
    assert len(nodes) == 2


def test_parse_content_partial_success():
    content = f"bad line\nvless://{UUID}@1.2.3.4:443?type=tcp#OK"
    nodes = parse_content(content)
    assert len(nodes) == 1
    assert nodes[0].name == "OK"


def test_b64_missing_padding():
    assert b64_decode_str("aGVsbG8") == "hello"
