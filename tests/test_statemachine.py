"""状态机测试：冷却/禁用流程、窗口口径、统计。"""
from datetime import date, timedelta

from modules.statemachine.engine import StateMachine, SubscriptionState


def make_sm(cooldown_failures=4, cooldown_days=None, disable_failures=4, window_size=30):
    return StateMachine(
        window_size=window_size,
        cooldown_failures=cooldown_failures,
        cooldown_days=cooldown_days or [3, 7],
        disable_failures=disable_failures,
    )


def test_initial_fetchable():
    sm = make_sm()
    state = SubscriptionState(link="x")
    assert sm.should_fetch(state, date(2026, 1, 1)) is True


def test_success_resets():
    sm = make_sm()
    state = SubscriptionState(link="x")
    for _ in range(3):
        sm.record_result(state, ok=False, count=0, today=date(2026, 1, 1))
    assert state.consecutive_failures == 3
    sm.record_result(state, ok=True, count=10, today=date(2026, 1, 2))
    assert state.consecutive_failures == 0
    assert state.cooldown_until is None
    assert state.cooldown_count == 0


def test_cooldown_flow():
    sm = make_sm(cooldown_failures=2, cooldown_days=[3, 7], disable_failures=2)
    state = SubscriptionState(link="x")
    d0 = date(2026, 1, 1)

    # 连续 2 次失败 → 冷却 3 天
    sm.record_result(state, False, 0, d0)
    sm.record_result(state, False, 0, d0)
    assert state.cooldown_count == 1
    assert state.cooldown_until == (d0 + timedelta(days=3)).isoformat()
    assert state.consecutive_failures == 0
    # 冷却期间跳过拉取
    assert sm.should_fetch(state, d0 + timedelta(days=1)) is False
    assert sm.should_fetch(state, d0 + timedelta(days=3)) is False
    # 冷却结束后可拉取
    d1 = d0 + timedelta(days=4)
    assert sm.should_fetch(state, d1) is True
    # 冷却后再连续 2 次失败 → 冷却 7 天
    sm.record_result(state, False, 0, d1)
    sm.record_result(state, False, 0, d1)
    assert state.cooldown_count == 2
    assert state.cooldown_until == (d1 + timedelta(days=7)).isoformat()
    # 第三次连续失败阶段 → 禁用
    d2 = d1 + timedelta(days=8)
    assert sm.should_fetch(state, d2) is True
    sm.record_result(state, False, 0, d2)
    sm.record_result(state, False, 0, d2)
    assert state.disabled is True
    assert sm.should_fetch(state, d2 + timedelta(days=1)) is False


def test_window_only_executed_runs():
    sm = make_sm()
    state = SubscriptionState(link="x")
    sm.record_result(state, True, 5, date(2026, 1, 1))
    sm.record_result(state, True, 7, date(2026, 1, 2))
    assert len(state.window) == 2
    assert sm.success_rate(state) == "2/2"
    assert sm.avg_count(state) == 6.0
    assert sm.last_count(state) == 7


def test_window_cap():
    sm = make_sm(window_size=3)
    state = SubscriptionState(link="x")
    for i in range(5):
        sm.record_result(state, True, i, date(2026, 1, 1))
    assert len(state.window) == 3
    assert sm.success_rate(state) == "3/3"
    assert sm.total_count(state) == 2 + 3 + 4


def test_failed_run_counts_zero():
    sm = make_sm()
    state = SubscriptionState(link="x")
    sm.record_result(state, True, 5, date(2026, 1, 1))
    sm.record_result(state, False, 0, date(2026, 1, 2))
    assert sm.last_count(state) == 0
    assert sm.success_rate(state) == "1/2"
