"""订阅输出文件生成：clash YAML / v2ray base64。

DESIGN.md §9：产物需可被 substore 订阅，输出通用订阅格式。
"""
from __future__ import annotations

import base64
import json
import os
import urllib.parse

import yaml

from ..common.node import Node

_SUPPORTED = ("vmess", "vless", "trojan", "ss", "hysteria2")


# ---------------------------------------------------------------------------
# Clash YAML
# ---------------------------------------------------------------------------

def to_clash_yaml(nodes: list[Node]) -> str:
    proxies = [node_to_clash(n) for n in nodes if n.protocol in _SUPPORTED]
    doc = {
        "mixed-port": 7890,
        "allow-lan": False,
        "mode": "rule",
        "proxies": proxies,
    }
    return yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, default_flow_style=False)


def node_to_clash(node: Node) -> dict:
    raw = node.raw or {}
    base = {
        "name": node.name,
        "type": node.protocol,
        "server": node.server,
        "port": node.port,
    }
    if node.protocol == "vmess":
        base.update({
            "uuid": raw.get("uuid", ""),
            "alterId": int(raw.get("alterId", 0) or 0),
            "cipher": raw.get("cipher", "auto"),
            "tls": bool(raw.get("tls")),
        })
        if raw.get("sni"):
            base["servername"] = raw["sni"]
    elif node.protocol == "vless":
        base.update({
            "uuid": raw.get("uuid", ""),
            "tls": bool(raw.get("tls") or raw.get("reality")),
            "flow": raw.get("flow", ""),
            "network": "tcp",
        })
        if raw.get("sni"):
            base["servername"] = raw["sni"]
        if raw.get("reality"):
            base["reality-opts"] = {
                "public-key": raw.get("pbk", ""),
                "short-id": raw.get("sid", ""),
            }
    elif node.protocol == "trojan":
        base.update({
            "password": raw.get("password", ""),
            "sni": raw.get("sni", ""),
            "skip-cert-verify": bool(raw.get("allowInsecure")),
        })
    elif node.protocol == "ss":
        base.update({
            "cipher": raw.get("method", ""),
            "password": raw.get("password", ""),
        })
        if raw.get("plugin"):
            base["plugin"] = raw["plugin"]
    elif node.protocol == "hysteria2":
        base.update({
            "password": raw.get("password", ""),
            "sni": raw.get("sni", ""),
            "skip-cert-verify": bool(raw.get("insecure")),
        })
    return base


# ---------------------------------------------------------------------------
# v2ray base64（节点链接列表）
# ---------------------------------------------------------------------------

def to_v2ray_base64(nodes: list[Node]) -> str:
    lines = [node_to_uri(n) for n in nodes if n.protocol in _SUPPORTED]
    payload = "\n".join(lines).encode("utf-8")
    return base64.b64encode(payload).decode("ascii")


def to_plain_text(nodes: list[Node]) -> str:
    """明文输出：每行一个节点链接（不做 base64 编码）。"""
    lines = [
        uri for n in nodes if n.protocol in _SUPPORTED and (uri := node_to_uri(n))
    ]
    return "\n".join(lines) + ("\n" if lines else "")


def node_to_uri(node: Node) -> str:
    raw = node.raw or {}
    name = urllib.parse.quote(node.name, safe="")
    if node.protocol == "vmess":
        data = {
            "v": "2",
            "ps": node.name,
            "add": node.server,
            "port": node.port,
            "id": raw.get("uuid", ""),
            "aid": int(raw.get("alterId", 0) or 0),
            "scy": raw.get("cipher", "auto"),
            "net": "tcp",
            "type": "none",
            "host": "",
            "path": "",
            "tls": "tls" if raw.get("tls") else "",
        }
        encoded = base64.b64encode(json.dumps(data, ensure_ascii=False).encode("utf-8")).decode("ascii")
        return f"vmess://{encoded}"
    if node.protocol == "vless":
        params = ["encryption=none"]
        if raw.get("reality"):
            params.append("security=reality")
        elif raw.get("tls"):
            params.append("security=tls")
        else:
            params.append("security=none")
        if raw.get("sni"):
            params.append(f"sni={raw['sni']}")
        if raw.get("flow"):
            params.append(f"flow={raw['flow']}")
        if raw.get("pbk"):
            params.append(f"pbk={raw['pbk']}")
        if raw.get("sid"):
            params.append(f"sid={raw['sid']}")
        params.append("type=tcp")
        return (
            f"vless://{raw.get('uuid', '')}@{node.server}:{node.port}"
            f"?{'&'.join(params)}#{name}"
        )
    if node.protocol == "trojan":
        params = ["security=tls"]
        if raw.get("sni"):
            params.append(f"sni={raw['sni']}")
        if raw.get("allowInsecure"):
            params.append("allowInsecure=1")
        else:
            params.append("allowInsecure=0")
        return (
            f"trojan://{raw.get('password', '')}@{node.server}:{node.port}"
            f"?{'&'.join(params)}#{name}"
        )
    if node.protocol == "ss":
        method = raw.get("method", "")
        password = raw.get("password", "")
        userinfo = base64.b64encode(f"{method}:{password}".encode("utf-8")).decode("ascii")
        return f"ss://{userinfo}@{node.server}:{node.port}#{name}"
    if node.protocol == "hysteria2":
        params = [f"insecure={'1' if raw.get('insecure') else '0'}"]
        if raw.get("sni"):
            params.append(f"sni={raw['sni']}")
        return (
            f"hysteria2://{raw.get('password', '')}@{node.server}:{node.port}"
            f"?{'&'.join(params)}#{name}"
        )
    return ""


# ---------------------------------------------------------------------------
# 写出
# ---------------------------------------------------------------------------

def write_output_files(nodes: list[Node], directory: str, formats: list[str]) -> dict[str, str]:
    """写出订阅输出文件，返回 {格式: 文件名}。"""
    os.makedirs(directory, exist_ok=True)
    written: dict[str, str] = {}
    if "clash" in formats:
        path = os.path.join(directory, "clash.yaml")
        with open(path, "w", encoding="utf-8") as f:
            f.write(to_clash_yaml(nodes))
        written["clash"] = path
    if "v2ray" in formats:
        path = os.path.join(directory, "v2ray.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(to_v2ray_base64(nodes))
        written["v2ray"] = path
    if "plain" in formats:
        path = os.path.join(directory, "plain.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(to_plain_text(nodes))
        written["plain"] = path
    return written
