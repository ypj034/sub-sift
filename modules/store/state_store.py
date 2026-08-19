"""subscription-state.json 读写（程序独占，单向派生自 CSV）。

DESIGN.md §3.4：
- subscriptions: 主清单订阅链接的窗口明细 + 状态机字段
- aggregators: 聚合源的窗口明细（无状态机）
"""
from __future__ import annotations

import json
import os

from ..statemachine.engine import SubscriptionState, WindowEntry

DEFAULT_PATH = "data/subscription-state.json"


def load_states(path: str = DEFAULT_PATH) -> tuple[dict[str, SubscriptionState], dict[str, list[WindowEntry]]]:
    """加载 state 文件，返回 (订阅状态表, 聚合源窗口表)。文件缺失返回空。"""
    subs: dict[str, SubscriptionState] = {}
    aggs: dict[str, list[WindowEntry]] = {}
    if not os.path.isfile(path):
        return subs, aggs
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return subs, aggs

    for item in data.get("subscriptions", []):
        link = item.get("link")
        if not link:
            continue
        subs[link] = SubscriptionState(
            link=link,
            window=[WindowEntry(**w) for w in item.get("window", []) if isinstance(w, dict)],
            consecutive_failures=int(item.get("consecutive_failures", 0)),
            cooldown_count=int(item.get("cooldown_count", 0)),
            cooldown_until=item.get("cooldown_until"),
            disabled=bool(item.get("disabled", False)),
        )
    for item in data.get("aggregators", []):
        agg_id = item.get("id")
        if not agg_id:
            continue
        aggs[agg_id] = [
            WindowEntry(**w) for w in item.get("window", []) if isinstance(w, dict)
        ]
    return subs, aggs


def save_states(
    subs: dict[str, SubscriptionState],
    aggs: dict[str, list[WindowEntry]],
    path: str = DEFAULT_PATH,
) -> None:
    """序列化并保存 state 文件。"""
    data = {
        "subscriptions": [_serialize_sub(s) for s in sorted(subs.values(), key=lambda x: x.link)],
        "aggregators": [
            {
                "id": agg_id,
                "window": [w.__dict__ for w in window],
            }
            for agg_id, window in sorted(aggs.items())
        ],
    }
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _serialize_sub(s: SubscriptionState) -> dict:
    return {
        "link": s.link,
        "window": [w.__dict__ for w in s.window],
        "consecutive_failures": s.consecutive_failures,
        "cooldown_count": s.cooldown_count,
        "cooldown_until": s.cooldown_until,
        "disabled": s.disabled,
    }
