"""GeoLite2 Country mmdb 更新器。

机制（DESIGN.md 已确认）：
- HEAD 请求对比 Last-Modified，有更新才下载，无更新跳过
- 下载到临时文件 → maxminddb 实际打开验证 → 原子替换
- 校验用 maxminddb 打开而非魔数：兼容标准 GeoLite2 与 mihomo
  特化格式（如 MetaCubeX country.mmdb 头部非标准魔数但仍可读），
  HTML 错误页/错误内容无法被 maxminddb 打开，同样会被拦截
- 任何失败仅打印警告，不阻塞主流程（沿用旧文件或内置表兜底）
- 下载物保存在 data/ 工作目录，不 commit 进 git
"""
from __future__ import annotations

import os

from .http import FetchError, download_to_file, head_last_modified

MMDB_FILENAME = "GeoLite2-Country.mmdb"
_META_SUFFIX = ".meta"


def _read_meta(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return ""


def _write_meta(path: str, value: str) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(value)
    except OSError:
        pass


def _cleanup(path: str) -> None:
    try:
        if os.path.isfile(path):
            os.remove(path)
    except OSError:
        pass


def update_geo(mmdb_url: str, data_dir: str = "data", timeout_sec: int = 20) -> str:
    """检查并更新 mmdb，返回状态字符串：

    - "disabled"  : mmdb_url 为空（纯内置表模式）
    - "unchanged" : 无更新，跳过下载
    - "updated"   : 已下载并原子替换
    - "failed"    : 检查/下载/校验失败（不抛异常，不阻塞主流程）
    """
    if not mmdb_url:
        return "disabled"

    os.makedirs(data_dir, exist_ok=True)
    target = os.path.join(data_dir, MMDB_FILENAME)
    meta = target + _META_SUFFIX

    # 1. HEAD 检查更新时间
    last_modified = head_last_modified(mmdb_url, timeout_sec)
    if last_modified:
        if os.path.isfile(target) and _read_meta(meta) == last_modified:
            return "unchanged"
    else:
        # HEAD 拿不到 Last-Modified：保守跳过（避免每次全量下载），
        # 本地无文件时仍尝试下载一次。
        if os.path.isfile(target):
            return "unchanged"

    # 2. 下载到临时文件
    tmp = target + ".tmp"
    _cleanup(tmp)
    try:
        download_to_file(mmdb_url, tmp, timeout_sec)
    except FetchError as e:
        _cleanup(tmp)
        print(f"[sub-sift] mmdb 下载失败: {e}")
        return "failed"

    # 3. maxminddb 实际打开验证（防止下载到错误内容/HTML 错误页）
    try:
        import maxminddb

        reader = maxminddb.open_database(tmp)
        reader.close()
    except Exception as e:
        _cleanup(tmp)
        print(f"[sub-sift] mmdb 文件校验失败（无法读取）: {e}")
        return "failed"

    # 4. 原子替换 + 记录 Last-Modified
    os.replace(tmp, target)
    if last_modified:
        _write_meta(meta, last_modified)
    print(f"[sub-sift] mmdb 已更新: {target}")
    return "updated"
