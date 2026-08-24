"""状态机引擎（参数化，DESIGN.md §6）。

流程：连续失败 cooldown_failures 次 → 冷却 cooldown_days[0] 天
     → 再连续失败 cooldown_failures 次 → 冷却 cooldown_days[1] 天
     → 再连续失败 disable_failures 次 → 永久禁用
约定：
- 冷却/禁用期间跳过拉取，跳过的运行不入窗口
- 成功完全重置状态机（连续失败归零、冷却解除、冷却计数归零）
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class WindowEntry:
    ts: str
    ok: bool
    count: int


@dataclass
class SubscriptionState:
    link: str
    window: list[WindowEntry] = field(default_factory=list)
    consecutive_failures: int = 0
    cooldown_count: int = 0
    cooldown_until: str | None = None  # ISO 日期 YYYY-MM-DD
    disabled: bool = False


class StateMachine:
    def __init__(
        self,
        window_size: int = 30,
        cooldown_failures: int = 4,
        cooldown_days: list[int] | None = None,
        disable_failures: int = 4,
    ) -> None:
        self._window_size = window_size
        self._cooldown_failures = cooldown_failures
        self._cooldown_days = list(cooldown_days or [3, 7])
        self._disable_failures = disable_failures

    # ------------------------------------------------------------------ 查询

    def should_fetch(self, state: SubscriptionState, today: date) -> bool:
        """冷却/禁用期间返回 False（跳过拉取）。"""
        if state.disabled:
            return False
        if state.cooldown_until:
            try:
                cooldown = date.fromisoformat(state.cooldown_until)
            except ValueError:
                cooldown = today
            if today <= cooldown:
                return False
        return True

    # ------------------------------------------------------------------ 记录

    def record_result(
        self, state: SubscriptionState, ok: bool, count: int, today: date
    ) -> None:
        """记录一次实际执行的运行结果（冷却/禁用跳过的运行不调用本方法）。"""
        state.window.append(
            WindowEntry(ts=today.isoformat(), ok=ok, count=count if ok else 0)
        )
        if len(state.window) > self._window_size:
            del state.window[: len(state.window) - self._window_size]

        if ok:
            state.consecutive_failures = 0
            state.cooldown_count = 0
            state.cooldown_until = None
        else:
            self._record_failure(state, today)

    def _record_failure(self, state: SubscriptionState, today: date) -> None:
        state.consecutive_failures += 1
        # 冷却期间不应有记录，但防御性处理：冷却期内失败不重复触发
        if state.cooldown_until:
            try:
                if today <= date.fromisoformat(state.cooldown_until):
                    return
            except ValueError:
                pass

        if state.cooldown_count >= len(self._cooldown_days):
            # 已用完全部冷却等级：再连续失败 disable_failures 次 → 永久禁用
            if state.consecutive_failures >= self._disable_failures:
                state.disabled = True
        else:
            if state.consecutive_failures >= self._cooldown_failures:
                level = state.cooldown_count  # 0 → 冷却 cooldown_days[0]
                state.cooldown_count += 1
                state.cooldown_until = (today + timedelta(days=self._cooldown_days[level])).isoformat()
                state.consecutive_failures = 0

    # ------------------------------------------------------------------ 统计

    def success_rate(self, state: SubscriptionState) -> str:
        """返回 '成功数/实际执行数'，如 '25/30'；无执行记录时返回 '-'。"""
        total = len(state.window)
        if total == 0:
            return "-"
        ok = sum(1 for w in state.window if w.ok)
        return f"{ok}/{total}"

    def last_count(self, state: SubscriptionState) -> int:
        return state.window[-1].count if state.window else 0

    def avg_count(self, state: SubscriptionState) -> float:
        if not state.window:
            return 0.0
        return sum(w.count for w in state.window) / len(state.window)

    def total_count(self, state: SubscriptionState) -> int:
        """近 N 次窗口内节点总数（主清单排序键）。"""
        return sum(w.count for w in state.window)
