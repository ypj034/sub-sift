# Subscription Quality Manager 设计规格

版本：v1.0（Phase 1-6 收口，Phase 7 实现依据）
状态：已确认

---

## 1. 项目定位与铁律

### 1.1 定位

管理**订阅源质量**（Subscription Quality Manager），不是节点质量测试器、不是测速器、不是 Clash 管理器。

### 1.2 铁律（不可推翻）

1. 数据处理模型 = **Pipeline**，拒绝大量 if-else 堆叠。
2. 每个 Rule 对 Node 只有 `PASS` / `REJECT(原因)`；REJECT 必须带原因。
3. **不存在** Score、权重、机器学习；规则均为"满足或删除"。
4. Node 仅运行时存在，结束即释放，不持久化。

### 1.3 运行环境

- GitHub Actions 每 6 小时定时运行。
- 输出产物需可被 substore 订阅，输出通用订阅格式。
- 公开仓库，本地可复现。

---

## 2. 系统架构

### 2.1 运行形态

- 单 GitHub Actions Job（预留可拆接口）、单可执行程序。
- fetcher 与 pipeline 分离，以纯数据契约为界，为可拆 Job 预留接口。

### 2.2 模块边界

```
app/              入口：加载配置、编排一次运行
modules/
  fetcher/        拉取聚合源与订阅链接、解析节点（容错）
  pipeline/       规则执行（短路）、去重、改名
  rules/          规则实现（每规则一文件，贡献者低门槛）
  statemachine/   状态机（仅主清单）
  store/          CSV / state.json / 输出文件读写
  report/         report.md 生成
  common/         枚举、类型、工具
```

### 2.3 数据流

```
定时触发 → 加载并全量校验 config（环境变量覆盖）
→ fetcher 拉取聚合源 → 提取订阅链接 → 合并进主清单（链接级去重 + manual 检测）
→ statemachine 过滤：跳过冷却中、禁用链接
→ fetcher 逐链接拉取节点（并发、超时、模板填充 {Ymd}，逐条容错）
→ pipeline 规则筛选（短路）→ 指纹去重 → 改名
→ store 更新 subscriptions.csv / aggregators.csv / subscription-state.json / 订阅输出文件
→ report 生成 report.md
→ commit 回 git
```

---

## 3. 数据模型

三个长期对象：**Subscription**（主清单订阅链接）、**Aggregator**（聚合源）、**Node**（仅运行时）。

### 3.1 Node（运行时，不持久化）

| 字段 | 说明 |
|---|---|
| `id` | 节点唯一标识（运行期） |
| `protocol` | 协议 |
| `server` | 服务器地址 |
| `port` | 端口 |
| `name` | 节点名（展示用，可被改名） |
| `region` | 地区（条件字段，域名型可空） |
| `raw` | 协议特有子结构，承载安全判定字段 |

`raw` 协议子结构（安全判定字段）：

| 协议 | 承载字段 |
|---|---|
| vmess | `cipher`、`tls`、`sni/host`、`alterId`、`uuid` |
| vless | `tls`、`reality`(publicKey/shortId)、`flow`、`allowInsecure`、`uuid` |
| trojan | `tls`、`sni`、`allowInsecure`、`password` |
| ss | `method`、`plugin`、`password` |
| hysteria2 | `insecure`、`sni`、`password` |

### 3.2 subscriptions.csv（主清单，事实源）

- 人工维护列：`link`、`sources`；其余列程序维护。
- 行序：程序按**近 N 次总节点数降序**重写。

```
link | sources | success_rate | state | last_node_count | avg_node_count
     | last_run_at | 各协议列(config 白名单镜像) | 各地区列(config 白名单镜像) | other
```

| 列 | 说明 |
|---|---|
| `link` | 订阅链接，唯一键 |
| `sources` | 来源血缘多值列表，含 `manual`；裸行（只有 link、sources 空）自动补 `[manual]`；聚合源写入直接带来源 ID |
| `success_rate` | `成功数/实际执行数`，如 `25/30`；分母 = 实际执行次数 |
| `state` | `active` / `冷却至 M-D` / `disabled`（状态机当前决策） |
| `last_node_count` | 最近一次运行的有效节点数（失败 = 0） |
| `avg_node_count` | 近 N 次平均值（全量平均，只展示不决策） |
| `last_run_at` | 最近运行时间 |
| 协议列 | config 协议白名单镜像，值取最近一次运行，失败全 0 |
| 地区列 | config 地区白名单镜像，值取最近一次运行，失败全 0 |
| `other` | 域名型/无地区节点兜底列 |

### 3.3 aggregators.csv（聚合源，一行一聚合源）

- 行序：按 `avg_count` 降序。
- **无状态机**：失败不冷却不禁用，靠 `success_rate` 人工判断维护。

```
id | link | 状态(25/30) | last_count | avg_count | last_run_at
```

| 列 | 说明 |
|---|---|
| `id` | 英文短 ID，唯一键，必填 |
| `link` | 聚合源 URL |
| `状态` | `成功数/实际执行数`，无冷却禁用标记 |
| `last_count` | 最近一次拉取出的订阅链接数（失败 = 0） |
| `avg_count` | 近 N 次平均拉取数（口径见 §7），只展示不决策 |
| `last_run_at` | 最近运行时间 |

### 3.4 subscription-state.json（程序独占）

- 分 `subscriptions` / `aggregators` 两个 section。
- **单向派生自 CSV**：链接集合以 CSV 为准，窗口数据程序写入。
- 不鼓励人工编辑。

```
{
  "subscriptions": [{
    "link": "...",
    "window": [{"ts": "...", "ok": true, "count": 12}],
    "consecutive_failures": 0,
    "cooldown_until": null,
    "disabled": false
  }],
  "aggregators": [{
    "id": "a1",
    "window": [{"ts": "...", "ok": true, "count": 8}]
  }]
}
```

---

## 4. 配置体系

- `config.yaml` 进仓库，带 `schema_version` + **每项中文注释**（含可选值注释，防止写错）。
- 环境变量 `SQM_*` 覆盖配置（如 `SQM_FETCHER_CONCURRENCY`）；敏感信息（如聚合源 token）必须用环境变量。
- 启动时**全量校验**，任一非法即终止运行。

### 4.1 config.yaml 结构

```yaml
schema_version: 1
timezone: "Asia/Shanghai"   # 基准时区

fetcher:
  concurrency: 5            # 并发拉取数，默认 5，可配置
  timeout_sec: 20           # 单订阅超时，15-30s 区间

stats:
  window_size: 30           # 近N次滚动窗口，默认 30

state_machine:              # 仅主清单生效；聚合源无状态机
  cooldown_failures: 4      # 连续失败次数阈值，触发冷却
  cooldown_days: [3, 7]     # 冷却天数分级：第1次冷却3天，第2次冷却7天
  disable_failures: 4       # 再连续失败该次数 → 永久禁用

rules:                      # 顺序即执行顺序，全局统一（无订阅级覆盖）
  protocol_allowlist:
    enabled: true
    allow: [vless, trojan, vmess, ss, hysteria2]   # 协议白名单；CSV 协议列数据源
  validity_target:
    enabled: true           # server/port 有效性 + 保留 IP/保留域名
  validity_fields:
    enabled: true           # 协议字段格式有效性（uuid/password/method）
  security_vmess:
    enabled: true
  security_vless:
    enabled: true
  security_trojan:
    enabled: true
  security_ss:
    enabled: true
  security_hysteria2:
    enabled: true
  junk_keywords:
    enabled: true
    # 垃圾关键词，匹配 name + server；config 可增删
    keywords: [free, test, demo, example, invalid, null, undefined,
               免费, 测试, 演示, 广告, 优惠, 官网, 购买, 试用]
  region_allowlist:
    enabled: true
    allow: [JP, KR, HK, SG, US, TW]   # 地区白名单；CSV 地区列数据源

output:
  # 订阅输出格式，可选值: clash, v2ray, plain（可多选，逗号分隔）
  # plain = 明文节点链接列表（每行一个链接，不做 base64）
  formats: [clash, v2ray, plain]

geo:
  # mmdb 国家地区库下载地址（无需 key）
  # 留空 = 禁用 mmdb 自动更新（仅用内置表兜底，精度有限）
  mmdb_url: "https://github.com/Loyalsoldier/geoip/releases/latest/download/Country.mmdb"
```

### 4.2 校验规则

1. 白名单内每个协议必须存在对应 `security_*` 规则且 enabled，否则报错。
2. 启用的规则产出的原因枚举必须是全局枚举表内的合法值。
3. 模板占位符白名单 + 预校验；占位符全集与映射为代码内固定标准：
   `{Y}`=2026、`{m}`=8、`{mm}`=08、`{d}`=20、`{dd}`=20、`{Ymd}`=20260820、
   `{ymd}`=20260820（`{Ymd}` 的小写变体，如 v2rayfree 类源 `v{ymd}1`）。
   白名单必须为全集子集；链接中出现未列入白名单的占位符 → 启动报错。
4. 数值参数范围校验（并发 / 超时 / 窗口 / 状态机参数）。
5. `geo.mmdb_url` 必须为 http/https 或空字符串。

### 4.3 GeoIP 地区数据

- 数据源优先级：`data/GeoLite2-Country.mmdb`（存在即优先）→ 内置表（兜底，精度有限）。
- mmdb 由 `python main.py --update-geo` 维护：HEAD 对比 Last-Modified，有更新才下载；
  下载到临时文件 → maxminddb 实际打开验证（兼容标准 GeoLite2 与 mihomo 特化格式）→ 原子替换；
  任何失败仅警告，不阻塞主流程（沿用旧文件/内置表）。
- `mmdb_url` 留空 = 纯内置表模式（离线可跑，CI 可复现）。
- 下载物保存于 `data/` 工作目录，`.gitignore` 排除，不 commit 进 git；CI 每次运行前自动更新。
- 默认源 Loyalsoldier/geoip `Country.mmdb`：标准国家码（ISO 3166-1 alpha-2）。
  注意：Google/Cloudflare 等大型云厂商段在库中标记为组织名（如 GOOGLE、CLOUDFLARE），
  region 规则按"非白名单"处理（不在 allow 即 REJECT）。
- 曾有的 `geoip.csv` 覆盖层已删除（mmdb 已承担精度，CSV 层冗余）。

---

## 5. Pipeline 与规则规格

### 5.1 Rule 契约

- 无状态纯函数：`evaluate(node) -> PASS | REJECT(reason)`。
- REJECT 原因 = 全局枚举（聚合键）。
- 无中间态、无权重、无打分。

### 5.2 执行模型

- 规则顺序 = config.yaml 声明顺序。
- **短路**：节点被 REJECT 立即终止后续规则。
- **fail-closed**：规则异常 → 该节点 `REJECT(REASON_RULE_ERROR)`，计数异常次数并暴露于 report。

### 5.3 规则全集（5 分类 10 条）

执行顺序：`protocol → validity → security → junk → region`（按执行成本递增，短路收益最大化）。

| # | 规则 ID | 分类 | 判定行为 | REJECT 原因 |
|---|---|---|---|---|
| 1 | `protocol_allowlist` | protocol | 协议不在白名单 → REJECT | `REASON_PROTOCOL_NOT_ALLOWED` |
| 2 | `validity_target` | validity | server 为空 / 内网地址 / 保留 IP / RFC 保留域名 / port 非法 → REJECT | `REASON_INVALID_TARGET` |
| 3 | `validity_fields` | validity | uuid 非标准格式或全零占位；password 空串/占位；method 空串 → REJECT | `REASON_INVALID_FIELD` |
| 4 | `security_vmess` | security | cipher 为空/非安全集合 → REJECT；tls 关闭 → REJECT | `REASON_UNSAFE_WEAK_CIPHER` / `REASON_UNSAFE_NO_TLS` |
| 5 | `security_vless` | security | 无 TLS 且非 Reality → REJECT；allowInsecure=true → REJECT | `REASON_UNSAFE_NO_TLS` / `REASON_UNSAFE_ALLOW_INSECURE` |
| 6 | `security_trojan` | security | tls=false → REJECT；allowInsecure=true → REJECT | `REASON_UNSAFE_NO_TLS` / `REASON_UNSAFE_ALLOW_INSECURE` |
| 7 | `security_ss` | security | method 为空/非安全集合 → REJECT | `REASON_UNSAFE_WEAK_CIPHER` |
| 8 | `security_hysteria2` | security | insecure=true → REJECT | `REASON_UNSAFE_ALLOW_INSECURE` |
| 9 | `junk_keywords` | junk | name 或 server 命中关键词 → REJECT | `REASON_JUNK_KEYWORD` |
| 10 | `region_allowlist` | region | region 非空且不在白名单 → REJECT；region 为空（域名型）→ PASS | `REASON_REGION_NOT_ALLOWED` |

### 5.4 安全算法集合（代码内固定，不进 config）

- **vmess 安全 cipher**：`auto`、`aes-128-gcm`、`chacha20-poly1305`。其余（`none`、`aes-128/192/256-cfb`、`chacha20-ietf` 等）不安全。
- **ss 安全 method**：`aes-128-gcm`、`aes-256-gcm`、`chacha20-ietf-poly1305`、`xchacha20-ietf-poly1305`、shadowsocks-2022 系列。其余（`none`、`rc4`、`rc4-md5`、`table`、`bf-cfb`、`salsa20`、`chacha20`、各旧 `cfb`/`camellia`/`seed` 算法）不安全。

### 5.5 保留 IP / 保留域名（代码内固定）

- 保留/内网 IP：`127.*`、`10.*`、`172.16-31.*`、`192.168.*`、`169.254.*`、`0.*`、`::1`、`fc00::/7`、`fe80::/10` 等。
- RFC 保留域名：`example.com`、`example.net`、`example.org`、`example.edu`、`localhost`、`*.test`、`*.invalid`、`*.example`。

### 5.6 原因枚举（全局）

```
REASON_PROTOCOL_NOT_ALLOWED
REASON_INVALID_TARGET
REASON_INVALID_FIELD
REASON_UNSAFE_NO_TLS
REASON_UNSAFE_ALLOW_INSECURE
REASON_UNSAFE_WEAK_CIPHER
REASON_JUNK_KEYWORD
REASON_REGION_NOT_ALLOWED
REASON_RULE_ERROR
```

### 5.7 去重（Pipeline 后置变换）

- 运行期内存指纹，不持久化。
- 指纹 = `protocol + server:port + 协议身份字段`：

| 协议 | 身份字段 |
|---|---|
| vmess / vless | `uuid` |
| trojan | `sni + password` |
| ss | `method + password` |
| hysteria2 | `password` |
| 未知/其他 | 空（退化为 `protocol + server:port`） |

- 身份字段缺失 → 按空串 fallback（粗粒度，保守去重：宁可多去重不漏去重）。
- 指纹定义代码内固定。
- 首见保留。

### 5.8 改名（Pipeline 后置变换）

- 保证输出节点 `name` 全局唯一；重名追加序号后缀（如 `Node-2`）。
- 仅变换展示名，不影响节点身份。

### 5.9 规则级计数器

- 每规则按原因枚举聚合 REJECT 计数，输出 `RuleStats` 进 report。
- 不进判定、不做决策依据。
- 节点级明细不保留。

---

## 6. 状态机（仅主清单生效）

- 连续失败 `cooldown_failures` 次 → 冷却 `cooldown_days[0]` 天
- 冷却结束后再连续失败 `cooldown_failures` 次 → 冷却 `cooldown_days[1]` 天
- 再连续失败 `disable_failures` 次 → **永久禁用**（disabled）
- 默认：4 连败 → 冷却 3 天 → 再 4 连败 → 冷却 7 天 → 再 4 连败 → 永久禁用
- 冷却期间跳过拉取；disabled 不参与输出。
- 聚合源**无状态机**。

---

## 7. 统计口径

- **有效节点** = 筛选后、去重前的节点数。
- 窗口只记录**实际执行的运行**；冷却/禁用跳过的运行不入窗口；分母 = 实际执行次数。
- 失败运行计数 0。
- 成功 = 能拉取且非整体解析失败；部分成功 = 成功（产出 = 提取条数）。
- 平均值 = 近 N 次全量平均（非 EMA），**只展示不参与决策**。
- 聚合源统计 = 从该源拉出的、主清单中状态正常且有效节点数 > 0 的订阅链接数；多源各自计入；禁用及冷却中的链接不计入。
- 重复展示用**重叠度指标**，而非逐条列表。

---

## 8. 容错

1. 聚合源单源拉取失败 → 跳过，不影响其他源。
2. 聚合文件整体失效 → 不影响主清单流程（主清单是核心输入，聚合文件是增量来源）。
3. 订阅内容解析：逐条尽力而为，部分成功 = 成功；全部失败才计失败；格式不可识别 = 整体失败。
4. 解析丢弃记录不进 report.md，仅内部日志。
5. 来源标签 = 血缘历史，保留（不随拉取波动移除）；统计以本次拉取结果为准。
6. 模板链接：模板原串 = 身份（用于匹配统计），填充后 URL = 仅访问用；占位符白名单 + 预校验。
7. 手动重复链接：主动去重删除，重复的补 `manual` 标记。
8. 基准时区 Asia/Shanghai。

---

## 9. 输出产物

1. **订阅输出文件**（output/）：通用订阅格式，可被 substore 订阅。
   - 支持格式：`clash`（Clash YAML）、`v2ray`（v2ray base64）、`plain`（明文链接列表，每行一个）。
   - config 的 `output.formats` 选择，可选值写注释。
2. **report.md**（人读汇总）：运行概览、规则级计数器、排序、重叠度、统计平均值。
3. 全部数据文件与报告 commit 回 git（mmdb 除外，见 4.3）。

---

## 10. GitHub Actions 约束

- 单 Job（预留可拆接口），单次运行目标 ≤ 10 分钟。
- 单订阅超时 15-30s（默认 20s）。
- 并发拉取默认 5，可配置。
- 优先使用 GITHUB_TOKEN，不用 PAT。
- fork PR 只跑 lint / 测试。
- 运行前执行 `--update-geo` 更新地区库（下载物不进 git）。
- 数据 commit 回 git；公开仓库。

---

## 11. 可扩展性

| 变更 | 改动位置 |
|---|---|
| 新增协议 | `raw` 子结构 + `security_*` 规则 + `protocol_allowlist` 添加（校验强制规则完整性） |
| 新增规则 | `rules/` 下新文件 + config 声明 + 需要时新增原因枚举 |
| 新增输出格式 | output 模块加转换器 + config `formats` 可选值注释 |
| 拆分 fetcher Job | fetcher 与 pipeline 纯数据契约已预留，改 CI 编排即可 |

---

## 12. 关键决策记录

- 存储三层：CSV（事实源）+ state.json（历史明细）+ report.md（人读汇总）。
- 聚合源统计"多源计入"，否决"首见归属"。
- 生命周期解耦：删除聚合源不影响主清单已有链接。
- 平均值只展示不决策（红线）。
- 状态机参数化进 config；聚合源无状态机。
- 规则异常 fail-closed（安全优先）。
- 去重指纹按协议差异化身份字段。
- 协议/地区 CSV 动态列 = config 白名单镜像，值取最近一次。
- GeoIP：mmdb（可配置 URL + HEAD 更新检查 + 下载不进 git）优先，内置表兜底；删除 geoip.csv 层。
- 输出新增 `plain` 明文格式。
- 占位符 7 种（`{Y}`/`{m}`/`{mm}`/`{d}`/`{dd}`/`{Ymd}`/`{ymd}`）各自按日期片段替换（修正早期"全部替换为 Ymd"的缺陷），`{ymd}` 为 `{Ymd}` 的小写变体，白名单预校验。
- `data/` 提供空表头 CSV 模板（`subscriptions.csv` / `aggregators.csv`）。
