"""pipeline 模块：规则执行（短路）、指纹去重、重名改名。"""
from .dedup import deduplicate, fingerprint
from .engine import RuleStats, run_pipeline
from .rename import rename_unique

__all__ = ["RuleStats", "run_pipeline", "deduplicate", "fingerprint", "rename_unique"]
