"""statemachine 模块：状态机（仅主清单订阅链接生效；聚合源无状态机）。"""
from .engine import StateMachine, SubscriptionState

__all__ = ["StateMachine", "SubscriptionState"]
