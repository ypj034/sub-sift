"""HTTP 拉取工具（标准库 urllib，避免额外依赖）。"""
from __future__ import annotations

import os
import urllib.error
import urllib.request

USER_AGENT = "sub-sift/1.0 (+https://github.com/sub-sift/sub-sift)"


class FetchError(Exception):
    """拉取失败（网络错误、超时、HTTP 错误等）。"""


def fetch_bytes(url: str, timeout: int = 20) -> bytes:
    """拉取 URL 内容，失败抛 FetchError。"""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        raise FetchError(f"HTTP {e.code} for {url}") from e
    except urllib.error.URLError as e:
        raise FetchError(f"网络错误 for {url}: {e.reason}") from e
    except TimeoutError as e:
        raise FetchError(f"超时 for {url}") from e


def fetch_text(url: str, timeout: int = 20) -> str:
    """拉取并解码为文本（容错处理编码）。"""
    data = fetch_bytes(url, timeout)
    for encoding in ("utf-8", "gb18030", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def download_to_file(url: str, dest: str, timeout: int = 20) -> None:
    """流式下载到本地文件（用于 mmdb 等大文件），失败抛 FetchError。"""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp, open(dest, "wb") as f:
            while True:
                chunk = resp.read(64 * 1024)
                if not chunk:
                    break
                f.write(chunk)
    except urllib.error.HTTPError as e:
        raise FetchError(f"HTTP {e.code} for {url}") from e
    except urllib.error.URLError as e:
        raise FetchError(f"网络错误 for {url}: {e.reason}") from e
    except TimeoutError as e:
        raise FetchError(f"超时 for {url}") from e


def head_last_modified(url: str, timeout: int = 20) -> str | None:
    """HEAD 请求，返回 Last-Modified 头；失败或无该头返回 None。

    用于 mmdb 更新检查：GitHub release 资产 URL 会 302 到对象存储，
    urllib 自动跟随重定向，最终响应携带 Last-Modified。
    """
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
        },
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.headers.get("Last-Modified")
    except Exception:
        return None
