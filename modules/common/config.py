"""配置加载、环境变量覆盖与全量校验。

设计约束（DESIGN.md §4）：
- config.yaml 进仓库，schema_version 校验
- 环境变量 SQM_<SECTION>_<KEY> 覆盖配置（敏感信息必须用环境变量）
- 启动时全量校验，任一非法即终止运行
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any

import yaml

SCHEMA_VERSION = 1
ENV_PREFIX = "SQM_"

SUPPORTED_PROTOCOLS = ("vless", "vmess", "trojan", "ss", "hysteria2")
SUPPORTED_FORMATS = ("clash", "v2ray", "plain")

# 模板占位符白名单全集（代码内固定，映射关系见 fetcher.subscription.placeholder_values）
# 注意 {ymd} 是 {Ymd} 的小写变体，填充值相同（如 20260820）
KNOWN_PLACEHOLDERS = ("{Y}", "{m}", "{mm}", "{d}", "{dd}", "{Ymd}", "{ymd}")

# 协议 → 安全规则 ID 映射（规则完整性校验用）
PROTOCOL_SECURITY_RULE = {
    "vless": "security_vless",
    "vmess": "security_vmess",
    "trojan": "security_trojan",
    "ss": "security_ss",
    "hysteria2": "security_hysteria2",
}

# 已知规则 ID 全集
KNOWN_RULES = (
    "protocol_allowlist",
    "validity_target",
    "validity_fields",
    "security_vmess",
    "security_vless",
    "security_trojan",
    "security_ss",
    "security_hysteria2",
    "junk_keywords",
    "region_allowlist",
)


class ConfigError(Exception):
    """配置非法，启动即终止。"""


@dataclass
class Config:
    schema_version: int
    timezone: str
    concurrency: int
    timeout_sec: int
    template_placeholders: list[str]
    window_size: int
    cooldown_failures: int
    cooldown_days: list[int]
    disable_failures: int
    rules: dict[str, dict[str, Any]]
    output_formats: list[str]
    output_directory: str
    geo_mmdb_url: str

    # 便捷访问 ------------------------------------------------------------------

    @property
    def active_rules(self) -> list[str]:
        """按配置顺序返回启用的规则 ID。"""
        return [rid for rid, cfg in self.rules.items() if cfg.get("enabled", True)]

    @property
    def protocol_allowlist(self) -> list[str]:
        return list(self.rules["protocol_allowlist"].get("allow", []))

    @property
    def region_allowlist(self) -> list[str]:
        return list(self.rules["region_allowlist"].get("allow", []))

    @property
    def junk_keywords(self) -> list[str]:
        return list(self.rules["junk_keywords"].get("keywords", []))


def load_config(path: str = "config.yaml") -> Config:
    """加载配置文件并返回校验后的 Config。"""
    raw = _read_yaml(path)
    _apply_env_overrides(raw)
    return _validate(raw)


def _read_yaml(path: str) -> dict:
    if not os.path.isfile(path):
        raise ConfigError(f"配置文件不存在: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ConfigError(f"配置文件 YAML 解析失败: {e}") from e
    if not isinstance(data, dict):
        raise ConfigError("配置文件的顶层必须是键值映射")
    return data


def _apply_env_overrides(raw: dict) -> None:
    """SQM_<SECTION>_<KEY>=<VALUE> 覆盖顶层 section 的标量配置。

    示例: SQM_FETCHER_CONCURRENCY=8 覆盖 fetcher.concurrency。
    仅支持 section 下的直接子键（rules 内规则参数不支持 env 覆盖）。
    """
    for name, value in os.environ.items():
        if not name.startswith(ENV_PREFIX):
            continue
        parts = name[len(ENV_PREFIX):].lower().split("_", 1)
        if len(parts) != 2:
            continue
        section, key = parts
        if section not in raw or not isinstance(raw[section], dict):
            continue
        if key in raw[section]:
            target = raw[section][key]
            if isinstance(target, list):
                raw[section][key] = _cast_list(value)
            elif isinstance(target, bool):
                raw[section][key] = _cast_bool(value)
            elif isinstance(target, int):
                raw[section][key] = _cast_int(value)
            else:
                raw[section][key] = value


def _cast_int(v: str) -> int:
    try:
        return int(v)
    except ValueError as e:
        raise ConfigError(f"环境变量 {v!r} 无法转换为整数") from e


def _cast_bool(v: str) -> bool:
    return v.strip().lower() in ("1", "true", "yes", "on")


def _cast_list(v: str) -> list[str]:
    return [item.strip() for item in v.split(",") if item.strip()]


def _validate(raw: dict) -> Config:
    errors: list[str] = []

    def err(msg: str) -> None:
        errors.append(msg)

    # schema_version
    sv = raw.get("schema_version")
    if sv != SCHEMA_VERSION:
        err(f"schema_version 必须为 {SCHEMA_VERSION}，当前为 {sv!r}")

    timezone = raw.get("timezone", "Asia/Shanghai")
    if not isinstance(timezone, str) or not timezone:
        err("timezone 必须是非空字符串")

    # fetcher
    fetcher = raw.get("fetcher", {})
    concurrency = _int(fetcher.get("concurrency", 5), "fetcher.concurrency", err)
    timeout_sec = _int(fetcher.get("timeout_sec", 20), "fetcher.timeout_sec", err)
    if concurrency is not None and concurrency < 1:
        err("fetcher.concurrency 必须 >= 1")
    if timeout_sec is not None and not (5 <= timeout_sec <= 300):
        err("fetcher.timeout_sec 建议在 15-30 之间，允许范围 5-300")
    placeholders = fetcher.get("template_placeholders", ["{Ymd}"])
    if not isinstance(placeholders, list) or not all(
        isinstance(p, str) and p.startswith("{") and p.endswith("}") for p in placeholders
    ):
        err("fetcher.template_placeholders 必须是占位符字符串列表（形如 {Ymd}）")
    else:
        unknown_ph = [p for p in placeholders if p not in KNOWN_PLACEHOLDERS]
        if unknown_ph:
            err(f"fetcher.template_placeholders 含未知占位符: {unknown_ph}（可选: {KNOWN_PLACEHOLDERS}）")

    # geo
    geo = raw.get("geo", {})
    mmdb_url = geo.get("mmdb_url", "")
    if not isinstance(mmdb_url, str):
        err("geo.mmdb_url 必须是字符串（留空 = 禁用 mmdb 自动更新）")
    elif mmdb_url and not (mmdb_url.startswith("http://") or mmdb_url.startswith("https://")):
        err("geo.mmdb_url 必须是 http/https 地址，或留空禁用 mmdb 更新")

    # stats
    stats = raw.get("stats", {})
    window_size = _int(stats.get("window_size", 30), "stats.window_size", err)
    if window_size is not None and not (1 <= window_size <= 100):
        err("stats.window_size 必须在 1-100 之间")

    # state_machine
    sm = raw.get("state_machine", {})
    cooldown_failures = _int(sm.get("cooldown_failures", 4), "state_machine.cooldown_failures", err)
    disable_failures = _int(sm.get("disable_failures", 4), "state_machine.disable_failures", err)
    cooldown_days = sm.get("cooldown_days", [3, 7])
    if not isinstance(cooldown_days, list) or not all(
        isinstance(d, int) and d > 0 for d in cooldown_days
    ):
        err("state_machine.cooldown_days 必须是正整数列表（如 [3, 7]）")
    if cooldown_failures is not None and cooldown_failures < 1:
        err("state_machine.cooldown_failures 必须 >= 1")
    if disable_failures is not None and disable_failures < 1:
        err("state_machine.disable_failures 必须 >= 1")

    # rules
    rules = raw.get("rules")
    if not isinstance(rules, dict):
        err("rules 必须是映射")
    else:
        unknown = [rid for rid in rules if rid not in KNOWN_RULES]
        if unknown:
            err(f"rules 包含未知规则 ID: {unknown}")

        proto_cfg = rules.get("protocol_allowlist", {})
        allow = proto_cfg.get("allow", [])
        if not isinstance(allow, list) or not allow:
            err("rules.protocol_allowlist.allow 不能为空")
        else:
            bad = [p for p in allow if p not in SUPPORTED_PROTOCOLS]
            if bad:
                err(f"protocol_allowlist.allow 包含不支持的协议: {bad}（可选: {SUPPORTED_PROTOCOLS}）")
            elif proto_cfg.get("enabled", True):
                # 规则完整性：白名单内协议必须存在对应安全规则且启用
                for proto in allow:
                    sec_rule = PROTOCOL_SECURITY_RULE[proto]
                    sec_cfg = rules.get(sec_rule, {})
                    if not sec_cfg.get("enabled", True):
                        err(f"协议 {proto} 在协议白名单中，但 {sec_rule} 未启用")

        reg_cfg = rules.get("region_allowlist", {})
        if reg_cfg.get("enabled", True):
            reg_allow = reg_cfg.get("allow", [])
            if not isinstance(reg_allow, list) or not reg_allow:
                err("rules.region_allowlist.allow 不能为空（地区过滤启用时）")

        kw_cfg = rules.get("junk_keywords", {})
        if kw_cfg.get("enabled", True):
            keywords = kw_cfg.get("keywords", [])
            if not isinstance(keywords, list):
                err("rules.junk_keywords.keywords 必须是列表（留空 [] = 启用规则但不过滤）")

    # output
    output = raw.get("output", {})
    formats = output.get("formats", ["clash"])
    if not isinstance(formats, list) or not formats:
        err("output.formats 不能为空")
    else:
        bad = [f for f in formats if f not in SUPPORTED_FORMATS]
        if bad:
            err(f"output.formats 包含不支持的格式: {bad}（可选: {SUPPORTED_FORMATS}）")
    output_dir = output.get("directory", "output")
    if not isinstance(output_dir, str) or not output_dir:
        err("output.directory 必须是非空字符串")

    if errors:
        raise ConfigError("配置校验失败:\n  - " + "\n  - ".join(errors))

    return Config(
        schema_version=sv,
        timezone=timezone,
        concurrency=concurrency,
        timeout_sec=timeout_sec,
        template_placeholders=list(placeholders),
        window_size=window_size,
        cooldown_failures=cooldown_failures,
        cooldown_days=list(cooldown_days),
        disable_failures=disable_failures,
        rules=rules,
        output_formats=list(formats),
        output_directory=output_dir,
        geo_mmdb_url=mmdb_url,
    )


def _int(value: Any, key: str, err) -> int | None:
    if not isinstance(value, int):
        err(f"{key} 必须是整数")
        return None
    return value
