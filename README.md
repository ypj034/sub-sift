# sub-sift

订阅质量管理器（Subscription Quality Manager）：定期从多个聚合源收集订阅链接，拉取节点并依据可配置规则筛选，产出干净、通用的订阅文件，供 Clash / v2ray 等客户端订阅。

> 定位：**订阅源质量管理工具**，不是节点测速器，也不是 Clash 管理器。只做"满足规则或删除"的筛选，不做评分/加权。

## 特性

- **Pipeline 数据流**：聚合源 → 主清单 → 状态机过滤 → 逐链接拉取 → 规则筛选（短路）→ 指纹去重 → 改名 → 输出
- **10 条内置规则**（5 分类）：协议白名单 / 地址与字段有效性 / 安全（TLS、弱加密、明文）/ 垃圾关键词 / 地区白名单；全部可开关、顺序即执行顺序
- **协议差异化去重指纹**：`protocol + server:port + 协议身份字段`（vmess/vless 用 uuid，trojan 用 sni+password 等）
- **状态机**：连续失败冷却（3 天 → 7 天 → 永久禁用），冷却期间跳过拉取
- **GeoIP 自动更新**：`--update-geo` 从配置地址定期拉取国家地区库（有更新才下载，失败不阻塞），mmdb 缺失时内置表兜底
- **三份持久化**：`subscriptions.csv`（事实源）、`subscription-state.json`（历史窗口）、`report.md`（人读报告）
- **GitHub Actions**：每 6 小时自动运行，产物 commit 回仓库，可直接被客户端订阅

## 快速开始

```bash
pip install -r requirements.txt   # Windows 另需 tzdata（已写入 requirements）
python main.py config.yaml --update-geo   # 可选：下载/更新地区判定库
python main.py config.yaml
```

首次运行前准备 `data/subscriptions.csv`：

```csv
link,sources
https://example.com/sub,manual
https://example.com/sub2,
```

- `sources` 留空会自动标记为 `manual`；聚合源拉到的链接自动补充来源标签
- 聚合源可选：编辑 `data/aggregators.csv`（列：`id,link`）

运行后产出：

- `output/clash.yaml`、`output/v2ray.txt`、`output/plain.txt` — 订阅文件（格式在 config 的 `output.formats` 配置）
- `output/report.md` — 本次运行报告（规则拒绝分布、主清单排序表、聚合源统计）
- `data/` 下 CSV 与 state.json 自动更新

模板链接（含占位符）：订阅链接可包含 `{Y}`、`{m}`、`{mm}`、`{d}`、`{dd}`、`{Ymd}`、`{ymd}` 占位符，按当天日期分别替换，如 `https://xxx/uploads/{Y}/{mm}/0-{Ymd}.yaml`。其中 `{ymd}` 是 `{Ymd}` 的小写变体，填充值相同（如 `20260820`）。出现但未列入 `fetcher.template_placeholders` 白名单的占位符会导致启动报错（预校验）。含占位符的原串作为链接身份用于去重/统计，填充后的 URL 仅用于访问。

## 目录结构

```
sub-sift/
├── config.yaml              # 全部配置（含逐项中文注释）
├── main.py                  # 入口编排
├── modules/
│   ├── common/              # 配置/枚举/Node/GeoIP
│   ├── fetcher/             # 拉取与解析（5 协议 + Clash + base64）
│   ├── rules/               # 规则实现（每个规则一个文件）
│   ├── pipeline/            # Pipeline 引擎、去重、改名
│   ├── statemachine/        # 冷却/禁用状态机
│   ├── store/               # CSV / state.json / 订阅文件输出
│   └── report/              # report.md 生成
├── data/                    # 运行时数据（事实源，commit 回 git；mmdb 不进 git）
├── output/                  # 订阅文件与报告（commit 回 git）
├── tests/                   # 单元测试
└── docs/DESIGN.md           # 完整设计文档（v1.0）
```

## 配置

所有配置在 `config.yaml`，启动时全量校验，环境变量可覆盖（`SQM_<SECTION>_<KEY>`，如 `SQM_FETCHER_CONCURRENCY`）。敏感信息（如需要鉴权的订阅链接）建议使用环境变量注入链接文件。

关键项：

| 配置 | 说明 |
|---|---|
| `fetcher.concurrency` | 并发拉取线程数 |
| `fetcher.timeout_sec` | 单订阅拉取超时 |
| `stats.window_size` | 近 N 次滚动窗口 |
| `state_machine.*` | 冷却/禁用参数 |
| `rules.*` | 10 条规则的开关与参数（含注释） |
| `output.formats` | 输出格式：`clash` / `v2ray` / `plain`（明文，可多选） |
| `geo.mmdb_url` | 国家地区库下载地址；留空禁用 mmdb（内置表兜底） |
| `fetcher.template_placeholders` | 订阅链接允许出现的占位符白名单 |

## GitHub Actions

`.github/workflows/ci.yml` 每 6 小时运行一次：

- `test`：`compileall` + `pytest`（fork PR 只跑此 job）
- `run`：先 `--update-geo` 更新地区库（下载物不进 git），再执行 `main.py`，将 `data/`、`output/` 变更 commit 回仓库，使订阅地址保持最新

## 本地开发

```bash
python -m pytest tests/ -q
```

新增规则：在 `modules/rules/` 下新建文件，实现 `evaluate(node) -> RuleResult`（PASS 或 REJECT(原因)），在 `__init__.py` 中注册即可。

详细设计见 [docs/DESIGN.md](docs/DESIGN.md)。
