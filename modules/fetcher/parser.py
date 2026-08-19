"""订阅内容解析：Clash YAML / base64 列表 / 明文 URI 行。

容错原则（DESIGN.md §8）：逐条尽力而为，部分成功 = 成功（产出 = 提取条数）。
解析层只负责"能解析出结构"，字段有效性交给 pipeline 的 validity 规则。
"""
from __future__ import annotations

import base64
import binascii
import json
import re
import urllib.parse
from typing import Optional

import yaml

from ..common.node import Node

# 支持的 URI 前缀（含协议别名）
_URI_PREFIXES = (
    "vmess://",
    "vless://",
    "trojan://",
    "ss://",
    "ssr://",
    "hysteria2://",
    "hy2://",
    "hysteria://",
)

# clash yaml 中支持的 proxy 类型
_CLASH_TYPES = ("vmess", "vless", "trojan", "ss", "hysteria2")


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------

def b64_decode(s: str) -> bytes | None:
    """宽容的 base64 解码：容忍换行、缺失 padding、标准/url-safe 两种表。"""
    s = re.sub(r"\s+", "", s)
    if not s:
        return None
    pad = "=" * ((4 - len(s) % 4) % 4)
    for decode in (base64.b64decode, base64.urlsafe_b64decode):
        try:
            return decode(s + pad)
        except (binascii.Error, ValueError):
            continue
    return None


def b64_decode_str(s: str) -> str | None:
    data = b64_decode(s)
    if data is None:
        return None
    for encoding in ("utf-8", "gb18030", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return None


def split_host_port(hostport: str) -> tuple[str, int] | None:
    """分割 host:port，支持 [IPv6]:port 与裸 IPv6。非法返回 None。"""
    hostport = hostport.strip()
    if not hostport:
        return None
    if hostport.startswith("["):
        m = re.match(r"^\[([^\]]+)\](?::(\d+))?$", hostport)
        if not m:
            return None
        host, port = m.group(1), m.group(2)
    elif hostport.count(":") == 1:
        host, _, port = hostport.partition(":")
    else:
        # 无端口的裸地址
        host, port = hostport, ""
    if not host:
        return None
    if port:
        try:
            port_int = int(port)
        except ValueError:
            return None
        if not (0 < port_int <= 65535):
            return None
        return host, port_int
    return None


def looks_like_uri(text: str) -> bool:
    return text.lstrip().lower().startswith(_URI_PREFIXES)


# ---------------------------------------------------------------------------
# URI 行解析
# ---------------------------------------------------------------------------

def parse_uri_line(line: str) -> Optional[Node]:
    """解析单行订阅链接，无法识别时返回 None。"""
    line = line.strip()
    if not line:
        return None
    low = line.lower()
    try:
        if low.startswith("vmess://"):
            return _parse_vmess(line)
        if low.startswith("vless://"):
            return _parse_vless(line)
        if low.startswith("trojan://"):
            return _parse_trojan(line)
        if low.startswith("ss://"):
            return _parse_ss(line)
        if low.startswith("hysteria2://") or low.startswith("hy2://"):
            return _parse_hysteria2(line)
    except Exception:
        return None
    return None


def _parse_vmess(uri: str) -> Optional[Node]:
    """vmess://base64(JSON)，JSON 常见字段见 DESIGN.md §3.1。"""
    body = uri[len("vmess://"):]
    decoded = b64_decode_str(body)
    if decoded is None:
        return None
    try:
        data = json.loads(decoded)
    except (json.JSONDecodeError, ValueError):
        return None
    if not isinstance(data, dict):
        return None
    server = str(data.get("add") or data.get("address") or "").strip()
    try:
        port = int(data.get("port"))
    except (TypeError, ValueError):
        return None
    if not server or not (0 < port <= 65535):
        return None
    name = str(data.get("ps") or server)
    tls = data.get("tls") in ("tls", "true", True)
    raw = {
        "uuid": str(data.get("id") or ""),
        "alterId": int(data.get("aid") or data.get("alterId") or 0),
        "cipher": str(data.get("cipher") or "auto"),
        "tls": tls,
        "sni": str(data.get("sni") or data.get("host") or ""),
    }
    return Node(protocol="vmess", server=server, port=port, name=name, raw=raw)


def _parse_vless(uri: str) -> Optional[Node]:
    """vless://uuid@host:port?params#name"""
    body = uri[len("vless://"):]
    rest, _, frag = body.partition("#")
    name = urllib.parse.unquote(frag) if frag else ""
    uuid, sep, hostpart = rest.partition("@")
    if not sep or not uuid or not hostpart:
        return None
    hostport, _, query = hostpart.partition("?")
    splitted = split_host_port(hostport)
    if splitted is None:
        return None
    server, port = splitted
    params = urllib.parse.parse_qs(query)
    security = _q(params, "security", "none")
    raw = {
        "uuid": uuid,
        "tls": security in ("tls", "xtls"),
        "reality": bool(security == "reality"),
        "flow": _q(params, "flow", ""),
        "sni": _q(params, "sni", ""),
        "allowInsecure": _q(params, "allowInsecure", "0") in ("1", "true", "yes"),
        "pbk": _q(params, "pbk", ""),
        "sid": _q(params, "sid", ""),
    }
    node_name = name or f"{server}:{port}"
    return Node(protocol="vless", server=server, port=port, name=node_name, raw=raw)


def _parse_trojan(uri: str) -> Optional[Node]:
    """trojan://password@host:port?params#name"""
    body = uri[len("trojan://"):]
    rest, _, frag = body.partition("#")
    name = urllib.parse.unquote(frag) if frag else ""
    password, sep, hostpart = rest.partition("@")
    if not sep or not password or not hostpart:
        return None
    hostport, _, query = hostpart.partition("?")
    splitted = split_host_port(hostport)
    if splitted is None:
        return None
    server, port = splitted
    params = urllib.parse.parse_qs(query)
    raw = {
        "password": password,
        "tls": True,  # trojan 协议本身基于 TLS
        "sni": _q(params, "sni", "") or _q(params, "peer", ""),
        "allowInsecure": _q(params, "allowInsecure", "0") in ("1", "true", "yes"),
    }
    node_name = name or f"{server}:{port}"
    return Node(protocol="trojan", server=server, port=port, name=node_name, raw=raw)


def _parse_ss(uri: str) -> Optional[Node]:
    """shadowsocks 链接，兼容 SIP002 与 legacy 两种形式：
    - ss://base64(method:password)@host:port?plugin=...#name
    - ss://base64(method:password@host:port)#name
    - ss://method:password@host:port#name （明文）
    """
    body = uri[len("ss://"):]
    rest, _, frag = body.partition("#")
    name = urllib.parse.unquote(frag) if frag else ""

    if "@" in rest:
        userinfo, _, hostpart = rest.partition("@")
        hostport = hostpart.split("?")[0] if "?" in hostpart else hostpart
        splitted = split_host_port(hostport)
        if splitted is None:
            return None
        server, port = splitted
        if ":" in userinfo and not _is_b64_encoded_userinfo(userinfo):
            # 明文 method:password
            method, _, password = userinfo.partition(":")
        else:
            decoded = b64_decode_str(userinfo)
            if decoded is None or ":" not in decoded:
                return None
            method, _, password = decoded.partition(":")
        plugin = ""
        if "?" in hostpart:
            params = urllib.parse.parse_qs(hostpart.split("?", 1)[1])
            plugin = _q(params, "plugin", "")
    else:
        decoded = b64_decode_str(rest)
        if decoded is None:
            return None
        userinfo, _, hostpart = decoded.partition("@")
        if not hostpart or ":" not in userinfo:
            return None
        method, _, password = userinfo.partition(":")
        splitted = split_host_port(hostpart)
        if splitted is None:
            return None
        server, port = splitted
        plugin = ""

    if not method or not server:
        return None
    raw = {"method": method, "password": password, "plugin": plugin}
    node_name = name or f"{server}:{port}"
    return Node(protocol="ss", server=server, port=port, name=node_name, raw=raw)


def _is_b64_encoded_userinfo(userinfo: str) -> bool:
    """判断 userinfo 是否为 base64 编码（含可解码出 method:password）。"""
    decoded = b64_decode_str(userinfo)
    return decoded is not None and ":" in decoded


def _parse_hysteria2(uri: str) -> Optional[Node]:
    """hysteria2://password@host:port?params#name"""
    body = uri.split("://", 1)[1]
    rest, _, frag = body.partition("#")
    name = urllib.parse.unquote(frag) if frag else ""
    password, sep, hostpart = rest.partition("@")
    if not sep or not hostpart:
        return None
    hostport, _, query = hostpart.partition("?")
    splitted = split_host_port(hostport)
    if splitted is None:
        return None
    server, port = splitted
    params = urllib.parse.parse_qs(query)
    raw = {
        "password": password or "",
        "sni": _q(params, "sni", ""),
        "insecure": _q(params, "insecure", "0") in ("1", "true", "yes"),
    }
    node_name = name or f"{server}:{port}"
    return Node(protocol="hysteria2", server=server, port=port, name=node_name, raw=raw)


def _q(params: dict, key: str, default: str = "") -> str:
    vals = params.get(key)
    if not vals:
        return default
    return vals[0]


# ---------------------------------------------------------------------------
# Clash YAML 解析
# ---------------------------------------------------------------------------

def parse_clash_yaml(content: str) -> list[Node]:
    """解析 Clash YAML 的 proxies 列表；解析失败返回空列表。"""
    try:
        data = yaml.safe_load(content)
    except yaml.YAMLError:
        return []
    if not isinstance(data, dict):
        return []
    proxies = data.get("proxies") or []
    if not isinstance(proxies, list):
        return []
    nodes: list[Node] = []
    for item in proxies:
        if not isinstance(item, dict):
            continue
        node = _clash_proxy_to_node(item)
        if node is not None:
            nodes.append(node)
    return nodes


def _clash_proxy_to_node(p: dict) -> Optional[Node]:
    ptype = str(p.get("type", "")).lower()
    if ptype not in _CLASH_TYPES:
        return None
    server = str(p.get("server", "")).strip()
    try:
        port = int(p.get("port", 0))
    except (TypeError, ValueError):
        return None
    if not server or not (0 < port <= 65535):
        return None
    name = str(p.get("name") or f"{server}:{port}")
    tls = p.get("tls", False) in (True, "true", "tls")

    if ptype == "vmess":
        raw = {
            "uuid": str(p.get("uuid", "")),
            "alterId": int(p.get("alterId", p.get("alter-id", 0)) or 0),
            "cipher": str(p.get("cipher", "auto")),
            "tls": tls,
            "sni": str(p.get("servername") or p.get("sni") or ""),
        }
    elif ptype == "vless":
        reality = p.get("reality-opts") or p.get("realityOpts")
        raw = {
            "uuid": str(p.get("uuid", "")),
            "tls": tls,
            "reality": bool(reality),
            "flow": str(p.get("flow", "")),
            "sni": str(p.get("servername") or p.get("sni") or ""),
            "allowInsecure": p.get("skip-cert-verify", False) in (True, "true"),
        }
    elif ptype == "trojan":
        raw = {
            "password": str(p.get("password", "")),
            "tls": tls,
            "sni": str(p.get("servername") or p.get("sni") or ""),
            "allowInsecure": p.get("skip-cert-verify", False) in (True, "true"),
        }
    elif ptype == "ss":
        raw = {
            "method": str(p.get("cipher", "")),
            "password": str(p.get("password", "")),
            "plugin": str(p.get("plugin", "")),
        }
    else:  # hysteria2
        raw = {
            "password": str(p.get("password", "")),
            "sni": str(p.get("sni") or p.get("servername") or ""),
            "insecure": p.get("skip-cert-verify", False) in (True, "true"),
        }
    return Node(protocol=ptype, server=server, port=port, name=name, raw=raw)


# ---------------------------------------------------------------------------
# 整体内容解析
# ---------------------------------------------------------------------------

def parse_content(content: str) -> list[Node]:
    """解析订阅内容，返回节点列表（尽力而为，可能为空）。"""
    if not content or not content.strip():
        return []

    # 1) Clash YAML
    stripped = content.lstrip()
    if stripped.startswith("proxies:") or re.search(r"^proxies:\s*$", content, re.M):
        nodes = parse_clash_yaml(content)
        if nodes:
            return nodes

    # 2) 整体 base64（解码后为多行 URI）
    decoded = b64_decode_str(content.strip())
    if decoded:
        lines = [ln.strip() for ln in decoded.splitlines() if ln.strip()]
        nodes = [parse_uri_line(ln) for ln in lines]
        nodes = [n for n in nodes if n is not None]
        if nodes:
            return nodes

    # 3) 明文多行 URI
    lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
    nodes = [parse_uri_line(ln) for ln in lines]
    return [n for n in nodes if n is not None]


def extract_links(content: str) -> list[str]:
    """从聚合源内容中提取订阅链接（http/https），去重保序。"""
    seen: set[str] = set()
    links: list[str] = []
    pattern = re.compile(r"https?://[^\s<>\"']+")
    for m in pattern.finditer(content):
        url = m.group(0).rstrip(".,;)]}")
        if url not in seen:
            seen.add(url)
            links.append(url)
    return links
