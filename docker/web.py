"""本地 Docker 模式 web 服务：订阅分发 + 主清单/聚合源维护。

免鉴权：GET /sub/{fmt}、GET /report —— 供局域网设备订阅与查看报告
需登录：/api/*（WEB_TOKEN 未设置时同样免鉴权，仅限可信局域网）

编辑流程（不破坏"数据以服务器为准"）：
    1. git checkout -- data output    丢弃本地运行产生的统计改动
    2. 应用编辑（只改 link / sources 两列）
    3. commit + push                  提交内容只有人工编辑，不污染服务器统计
    4. 本地运行 main.py               编辑立即在本地 output 生效
    5. syncer.request_sync()          立即进入检测窗口，等 Actions 产出快照
"""
from __future__ import annotations

import csv
import hashlib
import os
import subprocess
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse
from pydantic import BaseModel

from sync import Syncer

REPO_DIR = Path(os.environ.get("REPO_DIR", "/app"))
OUTPUT_DIR = REPO_DIR / os.environ.get("OUTPUT_DIR", "output")
DATA_DIR = REPO_DIR / "data"
BRANCH = os.environ.get("REPO_BRANCH", "main")
WEB_TOKEN = os.environ.get("WEB_TOKEN", "")
PUSH_TOKEN = os.environ.get("GIT_PUSH_TOKEN", "")
EDIT_TRIGGER_ACTIONS = os.environ.get("EDIT_TRIGGER_ACTIONS", "true").lower() in (
    "1", "true", "yes", "on",
)
COOKIE_NAME = "sub_sift_session"
COOKIE_MAX_AGE = 30 * 24 * 3600

SUB_PATH = DATA_DIR / "subscriptions.csv"
AGG_PATH = DATA_DIR / "aggregators.csv"

# 输出格式 → 文件名（与 modules/store/output.py 保持一致）
FORMAT_FILES = {"clash": "clash.yaml", "v2ray": "v2ray.txt", "plain": "plain.txt"}
# 程序维护列：新增行时给中性初值，避免污染统计口径
NEUTRAL_VALUES = {"state": "active", "pass_rate": "-", "avg": "0.0", "last": "0", "domain": "0"}

syncer = Syncer()
app = FastAPI(title="sub-sift", docs_url="/api/docs", openapi_url="/api/openapi.json")


# ---------------------------------------------------------------------------
# 鉴权（cookie 内只存 token 的 sha256，不存明文）
# ---------------------------------------------------------------------------

def _session_value() -> str:
    return hashlib.sha256(WEB_TOKEN.encode("utf-8")).hexdigest()


def _require(cookies: dict[str, str]) -> None:
    if not WEB_TOKEN:
        return
    if cookies.get(COOKIE_NAME) != _session_value():
        raise HTTPException(status_code=401, detail="未登录")


# ---------------------------------------------------------------------------
# CSV 行级读写（只改人工列，其余列原样保留）
# ---------------------------------------------------------------------------

def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        return [], []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        header = list(reader.fieldnames or [])
        return header, [dict(r) for r in reader]


def _write_csv(path: Path, header: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in rows:
            writer.writerow({h: row.get(h, "") for h in header})


def _blank_row(header: list[str], values: dict[str, str]) -> dict[str, str]:
    """按表头构造新行：程序维护列填中性初值，其余填 0。"""
    row = {h: "0" for h in header}
    row["last_run"] = ""
    for key, default in NEUTRAL_VALUES.items():
        if key in row:
            row[key] = default
    row.update(values)
    return row


def _sources_cell(sources: list[str] | None) -> str:
    return ";".join(s.strip() for s in (sources or []) if s.strip()) or "manual"


# ---------------------------------------------------------------------------
# 编辑落库：丢弃本地残留 → 应用编辑 → 提交推送 → 本地运行 → 请求同步
# ---------------------------------------------------------------------------

def _git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(REPO_DIR), *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace", check=check,
    )


def _commit_and_push(message: str) -> tuple[bool, str]:
    if not PUSH_TOKEN:
        return False, "未配置 GIT_PUSH_TOKEN，改动仅存本地（下次同步会被覆盖）"
    _git("add", "data/subscriptions.csv", "data/aggregators.csv")
    if _git("diff", "--cached", "--quiet").returncode == 0:
        return False, "没有需要提交的改动"
    _git("commit", "-m", message)
    # 用 extraheader 传递令牌，避免令牌出现在 URL 中
    proc = subprocess.run(
        ["git", "-c", f"http.extraheader=AUTHORIZATION: bearer {PUSH_TOKEN}",
         "-C", str(REPO_DIR), "push", "origin", BRANCH],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if proc.returncode != 0:
        return False, f"推送失败: {proc.stderr.strip()[-300:]}"
    return True, "已推送"


def _apply_and_publish(summary: str, mutate) -> dict[str, Any]:
    """统一的编辑落库流程：mutate 在干净工作区上执行 CSV 修改。"""
    # 丢弃本地运行残留，保证提交内容只有人工编辑
    _git("checkout", "--", "data", "output", check=False)
    result = mutate()
    if not result.get("changed"):
        return result
    message = f"chore(data): {summary}"
    if not EDIT_TRIGGER_ACTIONS:
        message += " [skip ci]"
    pushed, push_msg = _commit_and_push(message)
    ok, tail = syncer.run_local()
    syncer.request_sync()
    return {**result, "pushed": pushed, "push_message": push_msg, "local_run": ok, "output": tail}


# ---------------------------------------------------------------------------
# 订阅与报告（免鉴权，供局域网设备使用）
# ---------------------------------------------------------------------------

@app.get("/sub/{fmt}")
def get_subscription(fmt: str) -> PlainTextResponse:
    name = FORMAT_FILES.get(fmt)
    if not name:
        raise HTTPException(status_code=404, detail=f"不支持的格式: {fmt}")
    path = OUTPUT_DIR / name
    if not path.is_file():
        raise HTTPException(status_code=404, detail=f"尚未生成 {name}")
    media = "application/yaml" if name.endswith(".yaml") else "text/plain"
    return PlainTextResponse(path.read_text(encoding="utf-8"), media_type=media)


@app.get("/report")
def get_report() -> PlainTextResponse:
    path = OUTPUT_DIR / "report.md"
    if not path.is_file():
        raise HTTPException(status_code=404, detail="尚未生成 report.md")
    return PlainTextResponse(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# 登录 / 登出
# ---------------------------------------------------------------------------

class LoginIn(BaseModel):
    token: str = ""


@app.post("/api/login")
def login(data: LoginIn, response: Response) -> dict[str, str]:
    if not WEB_TOKEN:
        return {"status": "免鉴权模式"}
    if data.token != WEB_TOKEN:
        raise HTTPException(status_code=401, detail="口令错误")
    response.set_cookie(
        COOKIE_NAME, _session_value(), max_age=COOKIE_MAX_AGE,
        httponly=True, samesite="lax",
    )
    return {"status": "ok"}


@app.post("/api/logout")
def logout(response: Response) -> dict[str, str]:
    response.delete_cookie(COOKIE_NAME)
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# 状态与手动同步
# ---------------------------------------------------------------------------

@app.get("/api/status")
def status(request: Request) -> dict[str, Any]:
    _require(request.cookies)
    return {
        "auth_required": bool(WEB_TOKEN),
        "push_configured": bool(PUSH_TOKEN),
        "repo_ready": syncer.repo_ready(),
        "sync": syncer.state,
    }


@app.post("/api/sync")
def trigger_sync(request: Request) -> dict[str, str]:
    _require(request.cookies)
    syncer.request_sync()
    return {"status": "已请求立即同步"}


class SyncConfigIn(BaseModel):
    """同步参数；留空表示不修改该项。"""
    interval_hours: float | None = None
    buffer_minutes: float | None = None
    poll_seconds: float | None = None
    max_wait_minutes: float | None = None


@app.get("/api/config")
def get_sync_config(request: Request) -> dict[str, Any]:
    _require(request.cookies)
    return {"config": syncer.config()}


@app.put("/api/config")
def update_sync_config(data: SyncConfigIn, request: Request) -> dict[str, Any]:
    _require(request.cookies)
    patch: dict[str, float] = {}
    for key in ("interval_hours", "buffer_minutes", "poll_seconds", "max_wait_minutes"):
        value = getattr(data, key, None)
        if value is not None:
            patch[key] = value
    return {"config": syncer.update_config(patch)}


# ---------------------------------------------------------------------------
# 主清单（subscriptions.csv）
# ---------------------------------------------------------------------------

class SubIn(BaseModel):
    link: str = ""
    sources: list[str] | None = None


@app.get("/api/subscriptions")
def list_subscriptions(request: Request) -> dict[str, Any]:
    _require(request.cookies)
    _, rows = _read_csv(SUB_PATH)
    return {"rows": [{"link": r.get("link", ""), "sources": r.get("sources", "")} for r in rows]}


@app.post("/api/subscriptions/add")
def add_subscription(data: SubIn, request: Request) -> dict[str, Any]:
    _require(request.cookies)
    link = data.link.strip()
    if not link:
        raise HTTPException(status_code=400, detail="link 不能为空")

    def mutate() -> dict[str, Any]:
        header, rows = _read_csv(SUB_PATH)
        if not header:
            return {"changed": False, "message": "主清单为空，无法新增"}
        if any(r.get("link") == link for r in rows):
            return {"changed": False, "message": "该链接已存在"}
        rows.append(_blank_row(header, {"link": link, "sources": _sources_cell(data.sources)}))
        _write_csv(SUB_PATH, header, rows)
        return {"changed": True, "message": f"已新增 {link}"}

    return _apply_and_publish(f"add subscription {link[:40]}", mutate)


@app.post("/api/subscriptions/update")
def update_subscription(data: SubIn, request: Request) -> dict[str, Any]:
    _require(request.cookies)
    link = data.link.strip()
    if not link:
        raise HTTPException(status_code=400, detail="link 不能为空")

    def mutate() -> dict[str, Any]:
        header, rows = _read_csv(SUB_PATH)
        for row in rows:
            if row.get("link") == link:
                row["sources"] = _sources_cell(data.sources)
                _write_csv(SUB_PATH, header, rows)
                return {"changed": True, "message": f"已更新来源 {link}"}
        return {"changed": False, "message": "未找到该链接"}

    return _apply_and_publish(f"update subscription {link[:40]}", mutate)


@app.post("/api/subscriptions/delete")
def delete_subscription(data: SubIn, request: Request) -> dict[str, Any]:
    _require(request.cookies)
    link = data.link.strip()

    def mutate() -> dict[str, Any]:
        header, rows = _read_csv(SUB_PATH)
        kept = [r for r in rows if r.get("link") != link]
        if len(kept) == len(rows):
            return {"changed": False, "message": "未找到该链接"}
        _write_csv(SUB_PATH, header, kept)
        return {"changed": True, "message": f"已删除 {link}"}

    return _apply_and_publish(f"remove subscription {link[:40]}", mutate)


# ---------------------------------------------------------------------------
# 聚合源（aggregators.csv）
# ---------------------------------------------------------------------------

class AggIn(BaseModel):
    id: str = ""
    link: str = ""


@app.get("/api/aggregators")
def list_aggregators(request: Request) -> dict[str, Any]:
    _require(request.cookies)
    _, rows = _read_csv(AGG_PATH)
    return {"rows": [{"id": r.get("id", ""), "link": r.get("link", "")} for r in rows]}


@app.post("/api/aggregators/add")
def add_aggregator(data: AggIn, request: Request) -> dict[str, Any]:
    _require(request.cookies)
    agg_id = data.id.strip()
    link = data.link.strip()
    if not agg_id or not link:
        raise HTTPException(status_code=400, detail="id 与 link 均不能为空")

    def mutate() -> dict[str, Any]:
        header, rows = _read_csv(AGG_PATH)
        if not header:
            return {"changed": False, "message": "聚合源表为空，无法新增"}
        if any(r.get("id") == agg_id for r in rows):
            return {"changed": False, "message": "该 id 已存在"}
        rows.append(_blank_row(header, {"id": agg_id, "link": link}))
        _write_csv(AGG_PATH, header, rows)
        return {"changed": True, "message": f"已新增聚合源 {agg_id}"}

    return _apply_and_publish(f"add aggregator {agg_id}", mutate)


@app.post("/api/aggregators/update")
def update_aggregator(data: AggIn, request: Request) -> dict[str, Any]:
    _require(request.cookies)
    agg_id = data.id.strip()
    link = data.link.strip()
    if not agg_id:
        raise HTTPException(status_code=400, detail="id 不能为空")

    def mutate() -> dict[str, Any]:
        header, rows = _read_csv(AGG_PATH)
        for row in rows:
            if row.get("id") == agg_id:
                row["link"] = link
                _write_csv(AGG_PATH, header, rows)
                return {"changed": True, "message": f"已更新聚合源 {agg_id}"}
        return {"changed": False, "message": "未找到该 id"}

    return _apply_and_publish(f"update aggregator {agg_id}", mutate)


@app.post("/api/aggregators/delete")
def delete_aggregator(data: AggIn, request: Request) -> dict[str, Any]:
    _require(request.cookies)
    agg_id = data.id.strip()

    def mutate() -> dict[str, Any]:
        header, rows = _read_csv(AGG_PATH)
        kept = [r for r in rows if r.get("id") != agg_id]
        if len(kept) == len(rows):
            return {"changed": False, "message": "未找到该 id"}
        _write_csv(AGG_PATH, header, kept)
        return {"changed": True, "message": f"已删除聚合源 {agg_id}"}

    return _apply_and_publish(f"remove aggregator {agg_id}", mutate)


# ---------------------------------------------------------------------------
# 页面
# ---------------------------------------------------------------------------

PAGE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>sub-sift 本地模式</title>
<style>
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:0;padding:20px;background:#f6f8fa;color:#24292f}
h1{font-size:20px}h2{font-size:15px;margin:0 0 10px}
.card{background:#fff;border:1px solid #d0d7de;border-radius:6px;padding:16px;margin-bottom:16px}
table{width:100%;border-collapse:collapse;font-size:13px;margin-top:10px}
th,td{border:1px solid #d0d7de;padding:6px 8px;text-align:left;word-break:break-all;vertical-align:middle}
th{background:#f6f8fa}
input{padding:6px;border:1px solid #d0d7de;border-radius:4px;margin:0 6px 6px 0}
button{padding:6px 12px;border:1px solid #d0d7de;border-radius:4px;background:#f6f8fa;cursor:pointer}
button:hover{background:#eaeef2}
.muted{color:#57606a;font-size:12px}.err{color:#cf222e}.ok{color:#1a7f37}
code{background:#f6f8fa;padding:2px 5px;border-radius:3px}
</style>
</head>
<body>
<h1>sub-sift 本地模式</h1>
<div class="card" id="status">加载中…</div>
<div class="card" id="login" style="display:none">
  <h2>登录</h2>
  <input id="token" type="password" placeholder="WEB_TOKEN">
  <button onclick="doLogin()">登录</button>
  <span class="err" id="loginErr"></span>
</div>
<div id="main" style="display:none">
  <div class="card">
    <h2>订阅地址（可复制到 Clash 等客户端）</h2>
    <div id="subs" class="muted"></div>
  </div>
  <div class="card">
    <h2>同步参数</h2>
    <div>
      间隔 <input id="cfgInterval" type="number" step="0.5" min="0" style="width:80px"> 小时
      <span id="cfgIntervalNote" class="muted"></span>
      等待 <input id="cfgBuffer" type="number" step="1" min="1" style="width:80px"> 分钟
      轮询 <input id="cfgPoll" type="number" step="30" min="30" style="width:90px"> 秒
      <button onclick="saveCfg()">保存</button>
      <button onclick="doSync()">立即检测同步</button>
    </div>
    <div class="muted" style="margin-top:6px">
      间隔填 <b>0</b> = 自动跟随 ci.yml 的 schedule.cron（推荐）；填具体数字则手动指定。
      下次检测时间 = 上次 Actions 快照时间 + 间隔 + 等待。<br>
      「等待」需略大于 Actions 单次运行耗时（实测 2-3 分钟），太短会空跑一轮。<br>
      「轮询」= 进入检测窗口后每隔多久检查一次；若窗口内一直没等到快照，
      超过 2 小时则放弃本轮、按新参数重算下一个窗口。
    </div>
  </div>
  <div class="card">
    <h2>主清单 subscriptions.csv</h2>
    <div>
      <input id="newLink" placeholder="订阅链接（支持 {Ymd} 等占位符）" style="width:46%">
      <input id="newSources" placeholder="来源（可选，多个用分号）">
      <button onclick="addSub()">新增</button>
    </div>
    <table id="subTable"></table>
  </div>
  <div class="card">
    <h2>聚合源 aggregators.csv</h2>
    <div>
      <input id="newId" placeholder="id">
      <input id="newAggLink" placeholder="聚合源链接" style="width:46%">
      <button onclick="addAgg()">新增</button>
    </div>
    <table id="aggTable"></table>
  </div>
</div>
<script>
const $ = id => document.getElementById(id);

async function api(path, options) {
  const res = await fetch(path, options);
  if (res.status === 401) throw new Error('未登录');
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.detail || ('HTTP ' + res.status));
  return data;
}

async function post(path, body) {
  return api(path, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  });
}

function renderStatus(s) {
  const sync = s.sync || {};
  $('status').innerHTML =
    '仓库就绪: ' + (s.repo_ready ? '是' : '否') +
    ' ｜ PAT 已配置: ' + (s.push_configured ? '是' : '<span class="err">否（编辑不会回推）</span>') +
    ' ｜ 鉴权: ' + (s.auth_required ? '开' : '关') + '<br>' +
    '同步状态: ' + (sync.status || '-') +
    ' ｜ 上次同步: ' + (sync.last_sync || '-') +
    ' ｜ 下次窗口: ' + (sync.next_window || '-') +
    (sync.last_error ? '<br><span class="err">错误: ' + sync.last_error + '</span>' : '') +
    '<br><button style="margin-top:8px" onclick="doSync()">立即同步</button>' +
    ' <button onclick="doLogout()">退出</button>';
}

function renderSubLinks() {
  const base = location.origin;
  $('subs').innerHTML = ['plain', 'v2ray', 'clash']
    .map(f => '<code>' + base + '/sub/' + f + '</code>').join('<br>');
}

function renderSubs(rows) {
  $('subTable').innerHTML = '<tr><th>链接</th><th>来源</th><th style="width:60px">操作</th></tr>' +
    rows.map((r, i) => '<tr><td>' + r.link + '</td><td>' + r.sources +
      '</td><td><button onclick="delSub(' + i + ')">删除</button></td></tr>').join('');
}

function renderAggs(rows) {
  $('aggTable').innerHTML = '<tr><th>id</th><th>链接</th><th style="width:60px">操作</th></tr>' +
    rows.map((r, i) => '<tr><td>' + r.id + '</td><td>' + r.link +
      '</td><td><button onclick="delAgg(' + i + ')">删除</button></td></tr>').join('');
}

let subs = [], aggs = [];

async function loadAll() {
  subs = (await api('/api/subscriptions')).rows || [];
  aggs = (await api('/api/aggregators')).rows || [];
  renderSubs(subs);
  renderAggs(aggs);
}

async function boot() {
  try {
    renderStatus(await api('/api/status'));
    $('login').style.display = 'none';
    $('main').style.display = '';
    renderSubLinks();
    await loadCfg();
    await loadAll();
  } catch (e) {
    $('login').style.display = '';
    $('status').textContent = '未登录或无法访问';
  }
}

async function doLogin() {
  try {
    await post('/api/login', {token: $('token').value});
    $('loginErr').textContent = '';
    boot();
  } catch (e) {
    $('loginErr').textContent = e.message;
  }
}

async function doLogout() {
  await post('/api/logout', {}).catch(() => {});
  location.reload();
}

async function doSync() {
  await post('/api/sync', {});
  alert('已进入检测窗口，发现新快照会自动拉取并重跑');
  setTimeout(boot, 1500);
}

async function loadCfg() {
  const c = (await api('/api/config')).config || {};
  $('cfgInterval').value = c.interval_hours || 0;
  $('cfgBuffer').value = c.buffer_minutes;
  $('cfgPoll').value = c.poll_seconds;
  const notes = {
    cron: '自动（ci.yml → ' + c.effective_interval_hours + 'h）',
    manual: '手动指定',
    fallback: '解析失败，回退 6h'
  };
  $('cfgIntervalNote').textContent = notes[c.interval_source] || '';
}

async function saveCfg() {
  await api('/api/config', {
    method: 'PUT',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      interval_hours: parseFloat($('cfgInterval').value),
      buffer_minutes: parseFloat($('cfgBuffer').value),
      poll_seconds: parseFloat($('cfgPoll').value)
    })
  });
  alert('已保存，将按新参数重算下次检测窗口');
  boot();
}

async function addSub() {
  const link = $('newLink').value.trim();
  if (!link) return;
  const sources = $('newSources').value.split(';').map(s => s.trim()).filter(Boolean);
  const r = await post('/api/subscriptions/add', {link, sources});
  alert(r.message + '\\n推送: ' + (r.push_message || '无'));
  $('newLink').value = ''; $('newSources').value = '';
  await loadAll();
}

async function delSub(i) {
  if (!confirm('删除该订阅链接？')) return;
  const r = await post('/api/subscriptions/delete', {link: subs[i].link});
  alert(r.message + '\\n推送: ' + (r.push_message || '无'));
  await loadAll();
}

async function addAgg() {
  const id = $('newId').value.trim(), link = $('newAggLink').value.trim();
  if (!id || !link) return;
  const r = await post('/api/aggregators/add', {id, link});
  alert(r.message + '\\n推送: ' + (r.push_message || '无'));
  $('newId').value = ''; $('newAggLink').value = '';
  await loadAll();
}

async function delAgg(i) {
  if (!confirm('删除该聚合源？（已沉淀进主清单的链接不受影响）')) return;
  const r = await post('/api/aggregators/delete', {id: aggs[i].id});
  alert(r.message + '\\n推送: ' + (r.push_message || '无'));
  await loadAll();
}

boot();
</script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return PAGE


@app.on_event("startup")
def _startup() -> None:
    if syncer.repo_ready():
        syncer.start()
    else:
        print("[web] 仓库未就绪，同步线程暂不启动", flush=True)
