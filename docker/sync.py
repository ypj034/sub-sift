"""快照同步循环（本地 Docker 模式）。

双触发：
  A 定时：按"上次数据快照提交时间 + SYNC_INTERVAL_HOURS"推算下一个检测窗口
  B 编辑：web 端编辑推送成功后调用 request_sync()，立即进入检测窗口

窗口内每 SYNC_POLL_SECONDS 检测远端是否出现新的数据快照提交
（commit message 含 SNAPSHOT_MARK），发现后：
    丢弃本地 data/ output/ 改动 → pull → 运行 main.py

由此始终"以服务器数据为准"：本地运行只重新生成 output/ 供局域网订阅，
统计结果不回写 git。
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

REPO_DIR = Path(os.environ.get("REPO_DIR", "/app"))
BRANCH = os.environ.get("REPO_BRANCH", "main")

# Actions 提交数据快照时使用的 commit message 标记
SNAPSHOT_MARK = "chore(data)"

# 同步参数：环境变量为默认值，运行期可被配置文件覆盖（web 页面修改落在这里）。
# 配置文件放在 /app/data 下（卷内持久），且为未跟踪文件，不会被同步覆盖。
# buffer_minutes 需略大于 Actions 单次运行耗时（实测 2-3 分钟）。
CONFIG_PATH = Path(os.environ.get("SYNC_CONFIG_PATH", "/app/data/.sync-config.json"))


def _env_defaults() -> dict[str, float]:
    return {
        # 0 = 自动跟随 .github/workflows/ci.yml 的 schedule.cron
        "interval_hours": float(os.environ.get("SYNC_INTERVAL_HOURS", "0")),
        "buffer_minutes": float(os.environ.get("SYNC_BUFFER_MINUTES", "5")),
        "poll_seconds": float(os.environ.get("SYNC_POLL_SECONDS", "180")),
        "max_wait_minutes": float(os.environ.get("SYNC_MAX_WAIT_MINUTES", "120")),
    }


def load_config() -> dict[str, float]:
    """环境变量默认值 + 本地配置文件覆盖。"""
    cfg = _env_defaults()
    if CONFIG_PATH.is_file():
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                saved = json.load(f)
            if isinstance(saved, dict):
                for key in cfg:
                    if key in saved:
                        try:
                            cfg[key] = float(saved[key])
                        except (TypeError, ValueError):
                            pass
        except (OSError, ValueError):
            pass
    return cfg


def save_config(patch: dict) -> dict[str, float]:
    """合并并写回配置文件，返回合并后的完整配置。"""
    cfg = load_config()
    for key, value in (patch or {}).items():
        if key in cfg:
            try:
                cfg[key] = float(value)
            except (TypeError, ValueError):
                continue
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    return cfg


# ---------------------------------------------------------------------------
# 运行间隔：优先从 ci.yml 的 schedule.cron 解析（cron 是事实源）
# ---------------------------------------------------------------------------

def _cron_hour_interval(expr: str) -> float | None:
    """解析 cron 表达式的小时字段，返回间隔小时数。

    支持 `*/N`（每 N 小时）与逗号分隔的小时列表（取相邻最小间隔，含跨天）；
    无法识别时返回 None。
    """
    parts = expr.split()
    if len(parts) < 5:
        return None
    field = parts[1]  # cron 段序：分 时 日 月 周 → 小时为第 2 段

    if field == "*":
        return 1.0  # 每小时

    step = re.fullmatch(r"\*/(\d+)", field)
    if step:
        hours = int(step.group(1))
        return float(hours) if 1 <= hours <= 24 else None

    if re.fullmatch(r"[\d,]+", field):
        values = sorted({int(x) for x in field.split(",") if x.isdigit()})
        values = [v for v in values if 0 <= v <= 23]
        if not values:
            return None
        if len(values) == 1:
            return 24.0
        gaps = [values[i + 1] - values[i] for i in range(len(values) - 1)]
        gaps.append(24 - values[-1] + values[0])  # 跨天
        positive = [g for g in gaps if g > 0]
        return float(min(positive)) if positive else None
    return None


def detect_interval_hours(repo_dir: Path | None = None) -> float | None:
    """从 ci.yml 的 schedule.cron 解析运行间隔（小时）。

    多个 cron 取最小间隔；无法解析时返回 None（调用方回退到配置值）。
    """
    base = repo_dir or REPO_DIR
    path = base / ".github" / "workflows" / "ci.yml"
    if not path.is_file():
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    found: list[float] = []
    for expr in re.findall(r"cron:\s*[\"']([^\"']+)[\"']", text):
        hours = _cron_hour_interval(expr)
        if hours:
            found.append(hours)
    return min(found) if found else None


def effective_interval_hours(cfg: dict) -> float:
    """实际生效的间隔：配置值 > 0 时手动优先，否则跟随 cron，最后回退 6 小时。"""
    manual = cfg.get("interval_hours", 0) or 0
    if manual > 0:
        return float(manual)
    return detect_interval_hours() or 6.0


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _log(msg: str) -> None:
    print(f"[sync] {_now():%Y-%m-%d %H:%M:%S} {msg}", flush=True)


class Syncer:
    """后台同步线程：定时推算 + 可被编辑事件唤醒。"""

    def __init__(self) -> None:
        self._wakeup = threading.Event()
        self._lock = threading.Lock()
        self._state: dict[str, Any] = {"status": "idle", "last_error": ""}
        self._thread: threading.Thread | None = None

    # ---------------------------------------------------------------- 生命周期

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._thread = threading.Thread(target=self._run, daemon=True, name="sync")
        self._thread.start()

    def request_sync(self) -> None:
        """外部请求立即进入检测窗口（web 编辑推送成功后调用）。"""
        _log("收到立即同步请求")
        self._wakeup.set()

    # ---------------------------------------------------------------- 运行期配置

    def config(self) -> dict[str, Any]:
        """当前生效的同步参数 + 间隔来源（供 web 展示）。"""
        cfg = load_config()
        detected = detect_interval_hours()
        manual = (cfg.get("interval_hours") or 0) > 0
        if manual:
            source = "manual"
        elif detected:
            source = "cron"
        else:
            source = "fallback"
        return {
            **cfg,
            "interval_source": source,
            "detected_interval_hours": detected,
            "effective_interval_hours": effective_interval_hours(cfg),
        }

    def update_config(self, patch: dict) -> dict[str, float]:
        """修改同步参数并立即按新参数重算窗口。"""
        cfg = save_config(patch)
        _log(f"配置已更新: {cfg}")
        self._wakeup.set()
        return cfg

    # -------------------------------------------------------------------- 状态

    @property
    def state(self) -> dict[str, Any]:
        with self._lock:
            return dict(self._state)

    def _set_state(self, **kw: Any) -> None:
        with self._lock:
            self._state.update(kw)

    # --------------------------------------------------------------------- git

    def _git(self, *args: str, check: bool = True) -> str:
        proc = subprocess.run(
            ["git", "-C", str(REPO_DIR), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if check and proc.returncode != 0:
            raise RuntimeError(f"git {' '.join(args)} 失败: {proc.stderr.strip()}")
        return proc.stdout.strip()

    def repo_ready(self) -> bool:
        return (REPO_DIR / ".git").is_dir()

    def _snapshot_hash(self, rev: str) -> str:
        """最近一条数据快照提交的 hash，没有则返回空串。"""
        try:
            return self._git("log", "-1", "--format=%H", f"--grep={SNAPSHOT_MARK}", rev)
        except RuntimeError:
            return ""

    def _snapshot_time(self, rev: str) -> datetime | None:
        """最近一条数据快照提交的 UTC 时间。"""
        try:
            raw = self._git("log", "-1", "--format=%cI", f"--grep={SNAPSHOT_MARK}", rev)
        except RuntimeError:
            return None
        if not raw:
            return None
        try:
            return datetime.fromisoformat(raw).astimezone(timezone.utc)
        except ValueError:
            return None

    def has_new_snapshot(self) -> bool:
        """fetch 后比对本地与远端的最新数据快照。"""
        self._git("fetch", "--depth=1", "origin", BRANCH)
        return self._snapshot_hash("HEAD") != self._snapshot_hash(f"origin/{BRANCH}")

    # --------------------------------------------------------------------- 同步

    def sync_once(self) -> bool:
        """丢弃本地数据改动 → 拉取 → 运行主流程。"""
        if not self.repo_ready():
            _log("仓库未就绪，跳过本次同步")
            return False
        _log("检测到新的数据快照，开始同步")
        self._set_state(status="syncing", last_check=_now().isoformat())
        try:
            # 以服务器为准：丢弃本地运行产生的 data/ output/ 改动
            self._git("checkout", "--", "data", "output", check=False)
            self._git("pull", "--ff-only", "origin", BRANCH)
            # mmdb 更新失败不阻塞（沿用旧库或内置表）
            subprocess.run(
                ["python", "main.py", "config.yaml", "--update-geo"],
                cwd=str(REPO_DIR),
                check=False,
            )
            proc = subprocess.run(
                ["python", "main.py", "config.yaml"],
                cwd=str(REPO_DIR),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            for line in (proc.stdout or "").splitlines():
                print(line, flush=True)
            if proc.returncode != 0:
                raise RuntimeError((proc.stderr or "").strip()[-500:])
            self._set_state(
                status="ok",
                last_error="",
                last_sync=_now().isoformat(),
                snapshot=self._snapshot_hash("HEAD"),
            )
            _log("同步完成")
            return True
        except Exception as exc:  # noqa: BLE001 —— 记录后继续循环
            self._set_state(status="error", last_error=str(exc))
            _log(f"同步失败: {exc}")
            return False

    def run_local(self) -> tuple[bool, str]:
        """不拉取，直接本地运行一次（编辑后立即生效）。

        返回 (是否成功, 输出尾部)。
        """
        _log("本地运行 main.py")
        proc = subprocess.run(
            ["python", "main.py", "config.yaml"],
            cwd=str(REPO_DIR),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        tail = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode == 0, tail[-2000:]

    # --------------------------------------------------------------------- 循环

    def _next_window_time(self) -> datetime:
        """上次快照时间 + 间隔 + 缓冲（缓冲需覆盖 Actions 单次运行耗时）。"""
        cfg = load_config()
        base = (
            self._snapshot_time("HEAD")
            or self._snapshot_time(f"origin/{BRANCH}")
            or _now()
        )
        return base + timedelta(
            hours=effective_interval_hours(cfg), minutes=cfg["buffer_minutes"]
        )

    def _sleep_until(self, target: datetime) -> None:
        """睡到目标时刻；期间被 request_sync() 唤醒则立即返回。"""
        while True:
            remaining = (target - _now()).total_seconds()
            if remaining <= 0:
                return
            if self._wakeup.wait(min(remaining, 30)):
                self._wakeup.clear()
                _log("被唤醒，提前进入检测窗口")
                return

    def _poll_window(self) -> None:
        """窗口内轮询，直到发现新快照或超时。"""
        cfg = load_config()
        deadline = _now() + timedelta(minutes=cfg["max_wait_minutes"])
        max_wait = cfg["max_wait_minutes"]
        while _now() < deadline:
            try:
                if self.has_new_snapshot():
                    self.sync_once()
                    return
            except Exception as exc:  # noqa: BLE001
                _log(f"检测失败: {exc}")
                self._set_state(status="error", last_error=str(exc))
            self._set_state(last_check=_now().isoformat())
            # 每次等待都重读配置，使参数修改立即生效
            if self._wakeup.wait(load_config()["poll_seconds"]):
                self._wakeup.clear()
        _log(f"窗口内未检测到新快照（已等待 {max_wait} 分钟）")

    def _run(self) -> None:
        cfg = load_config()
        _log("同步线程启动（间隔 %.1fh，缓冲 %.1fm，轮询 %.0fs）" % (
            effective_interval_hours(cfg), cfg["buffer_minutes"], cfg["poll_seconds"]
        ))
        while True:
            try:
                if self.repo_ready():
                    target = self._next_window_time()
                    self._set_state(next_window=target.isoformat(), status="idle")
                    _log(f"下次检测窗口: {target:%Y-%m-%d %H:%M:%S} UTC")
                    self._sleep_until(target)
                    self._poll_window()
                else:
                    self._wakeup.wait(60)
            except Exception as exc:  # noqa: BLE001 —— 兜底，避免线程退出
                _log(f"同步循环异常: {exc}")
                self._set_state(status="error", last_error=str(exc))
                self._wakeup.wait(60)
