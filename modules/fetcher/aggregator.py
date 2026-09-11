"""聚合源拉取：抓取聚合链接 → 提取订阅链接列表。

容错（DESIGN.md §8）：单源失败跳过，不影响其他源；聚合文件整体失效不影响主清单。
"""
from __future__ import annotations

from ..common.config import Config
from .http import FetchError, fetch_text
from .parser import extract_links


def fetch_aggregator_links(link: str, timeout: int = 20) -> list[str]:
    """拉取单个聚合源，返回提取出的订阅链接列表；失败抛 FetchError。"""
    content = fetch_text(link, timeout)
    return extract_links(content)


def fetch_all_aggregators(config: Config) -> dict[str, list[str] | Exception]:
    """并发拉取全部聚合源。

    返回 {聚合源链接: 链接列表 或 异常对象}。单个失败不影响其他源，
    由调用方决定整体成败（DESIGN：聚合源失败不影响主清单流程）。
    """
    import concurrent.futures

    results: dict[str, list[str] | Exception] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=config.concurrency) as pool:
        futures = {
            pool.submit(fetch_aggregator_links, link, config.timeout_sec): link
            for link in _all_aggregator_links(config)
        }
        for future in concurrent.futures.as_completed(futures):
            link = futures[future]
            try:
                results[link] = future.result()
            except Exception as e:  # noqa: BLE001 - 单源失败记录异常，不中断
                results[link] = e
    return results


def _all_aggregator_links(config: Config) -> list[str]:
    """聚合源列表来源：data/aggregators.csv 的 link 列（由 store 模块解析）。

    为避免循环依赖，这里通过延迟导入 store 获取。若文件不存在返回空。
    """
    from ..store.csv_store import read_aggregator_links

    return read_aggregator_links()
