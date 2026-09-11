"""subscription-state.json 读写测试（含模板日期偏移记忆）。"""
import json

from modules.statemachine.engine import SubscriptionState, WindowEntry
from modules.store.state_store import load_states, save_states


def test_last_date_offset_roundtrip(tmp_path):
    path = str(tmp_path / "state.json")
    link = "https://x/uploads/{Ymd}.txt"
    st = SubscriptionState(
        link=link,
        window=[WindowEntry(ts="2026-08-20", ok=True, count=3)],
        last_date_offset=-1,
    )
    save_states({link: st}, {}, path)
    subs, _ = load_states(path)
    assert subs[link].last_date_offset == -1


def test_missing_last_date_offset_defaults_none(tmp_path):
    """老 state 文件（无该字段）加载后为 None，向后兼容。"""
    path = str(tmp_path / "state.json")
    data = {
        "subscriptions": [
            {"link": "https://plain.example/sub", "window": [], "disabled": False}
        ],
        "aggregators": [],
    }
    (tmp_path / "state.json").write_text(json.dumps(data), encoding="utf-8")
    subs, _ = load_states(path)
    assert subs["https://plain.example/sub"].last_date_offset is None
