# 图谱资产管理平台 v1 设计

> 日期：2026-07-16
> 状态：设计待评审
> 范围：v1（导入导出 + 通用解析 + 读API + 只读三栏前端）

---

## 1. 背景与目标

### 1.1 现状（来自上下文梳理）

- **platform-next**：一个成熟的"只读知识库浏览器"（Vue3+TS / FastAPI 内存单例、无 DB）。已有"单对象 + 单跳(BFS子图)"读 API（command/feature/wiki/task），查询架构干净**可复用**。但：写侧全空（无在线编辑/导入导出/版本/评审），且**强耦合**具体项目资产——business_graph 写死 `business-graph/*/three-layer-graph/` + 7 固定层文件 + 1228 行专用 `graph_parser`（硬编码 ID 正则/关系动词，不可通用）；command/feature 读 jsonl（文件名/ID 规则写死）；task 读 yaml。同一批命令资产在仓库里有 md/jsonl/规范化md 三份异构副本。
- **三层图谱构建规范**（VERSION 0.8.1）：既定义资产格式也定义构建流程；command 层端到端跑通。核心资产格式 = md 三段式（YAML frontmatter + 正文 + 底部 `## 边`，frontmatter **不存边**）；逻辑ID = `{网元}@{Type}@{local}`（带网元、留空格、版本无关）；**边 = 可组装模块**（EDGE_MODULES 注册表，纯函数签名）。演进机制/change-request 只到"写 CR 文件"为止，无自动同步/对比/决策工作流。版本管理只覆盖"规范本身"，不覆盖资产内容。
- **资产现实**：形态不统一、6+ 目录并存；全仓零导入导出/打包工具。

### 1.2 目标

构建一个**完全独立于具体项目资产**的"图谱资产管家"：把一份图谱当成一个可导入导出的 **md 资产包**，平台用**通用机制**承载对象/边（沿用规范的 md 三段式 + `## 边` + EDGE_MODULES 思想），提供**读 API（单对象/单跳）**与**只读三栏前端**浏览游走，可导出。

### 1.3 非目标（明确排除到二期）

- 在线编辑 / 写 API（增改删对象）
- 资产内容级版本管理（draft/published/历史/回滚）
- 变更评审回路（提改→同步关联→专家 diff→决策入库）+ Agent 编排
- 多用户/鉴权/并发（v1 单人本地）

二期能力以"预留扣子"形式保留接入点，v1 不实现但不得堵死。

---

## 2. 范围（v1）

### 2.1 纳入

| 子系统 | 内容 |
|---|---|
| **S1 资产包导入/导出** | 定义 bundle 格式（zip）；import 创建工作区；export 快照打包 |
| **S2 通用对象/边模型 + 解析器** | md 三段式 → 通用 Object + 动态解析 Edge；对象类型注册表（平台默认 + bundle 可扩展）；边解析插件管线（通用 `## 边` 解析 + 可选 EDGE_MODULES 插件） |
| **S3 读 API** | 单对象 / 单跳(BFS) / 列表(+搜索) / 子图 / 原始 md / 统计 |
| **前端** | 三栏只读浏览器：左=对象索引(按类型分组+搜索)，中=选中对象 md，右=节点图(单跳)+邻居清单 |

### 2.2 排除（二期，预留扣子）

- S4 写 API + 在线 md 编辑
- S5 资产内容级版本管理
- S6 变更评审回路 + Agent 同步关联知识

---

## 3. 核心设计决策（锁定）

1. **完全独立**：平台与仓库 `assets/` 无任何关系；导入后平台即该图谱的权威管理者；导入单向吃入、导出单向吐出，不存在"同步回 assets/"。
2. **图谱 = 一堆 md 文件**（规范三段式：YAML frontmatter + 正文 + 底部 `## 边`）。
3. **导入/导出 = bundle（zip）**。
4. **单人优先**，API/存储/数据结构按日后可加登录与多人并发设计（留扣子）。
5. **存储 = 纯文件目录**（每图谱一个 md 目录）+ **内存解析索引**；不绑 git、不引入 DB（二期版本/评审以 git/快照或暂存区叠加）。
6. **对象身份以 frontmatter `id`/`type` 为准**，文件路径仅作存储；解析器对路径/命名变体容错（现实 assets/ 与规范命名略有差异，靠 frontmatter 兜底）。
7. **逻辑 ID 版本无关**：`{网元}@{Type}@{local}`；引用 `[[...]]` 不带版本，版本在解析时动态选择。
8. **边动态解析**（不单独存储）：① 每个 md 的 `## 边` 章节（通用解析器，v1 核心）；② 可组装边解析插件（移植 EDGE_MODULES，v1 带一两个默认，可扩展）。
9. **类型注册表 = 平台默认 + bundle 可扩展**；新增对象类型 = 注册表加一条，不改代码。
10. **复用**：platform-next 的"内存图 + BFS 子图"读模式；规范的 md 三段式 + EDGE_MODULES 可组装边思想；platform-next 前端三栏/vis-network UI 风格（精简，不照搬其项目特定模块）。

---

## 4. 架构（分层）

```
┌─────────────────────────────────────────────────────────────┐
│  前端 Vue3+TS (三栏只读浏览器)                                 │
│  对象索引(类型分组+搜索) · 对象md · 节点图(单跳)+邻居清单        │
├─────────────────────────────────────────────────────────────┤
│  ⑤ 读 API (S3)   单对象/单跳(BFS)/列表/子图/raw md/统计        │
│  ④ 内存索引层    md解析→对象/边图→邻接表，导入时全量建          │
│  ③ 通用模型+解析层 (S2)   对象类型注册表 + 边解析插件管线        │
│  ② 存储层        每图谱=一个托管md目录(纯文件系统)              │
│  ① 资产包格式层 (S1)   bundle=zip(md+manifest)，唯一解耦边界    │
├─────────────────────────────────────────────────────────────┤
│  〔预留二期〕S4写API/编辑 · S5版本 · S6评审回路+Agent  接在②之上 │
└─────────────────────────────────────────────────────────────┘
   平台只认：①bundle格式 ②md三段式约定 ③对象类型注册表+边解析器
   不认任何具体业务（计费/带宽/SFCGraph 一概不知）
```

**解耦边界**：平台唯一对外契约是 ① bundle 格式 + ② md 三段式约定 + ③ 类型注册表/边解析器。除此之外平台对任何具体业务领域（计费、带宽、访问限制、SFCGraph 命名等）一无所知。

---

## 5. 资产包格式（Bundle）— S1

### 5.1 bundle 结构

一个 bundle = 一个 zip，内容：

```
manifest.yaml
{ObjectType}/{nf}/{version}/{nf}@{Type}@{local}.md     # NF 作用域类
{ObjectType}/{Type}@{local}.md                          # 跨 NF 类（业务域/场景/方案）
types/                                                  # (可选) 扩展类型注册表
```

### 5.2 manifest.yaml 字段

| 字段 | 说明 |
|---|---|
| `bundle_format_version` | bundle 格式版本（语义化，便于演进） |
| `graph_id` | 图谱标识（slug，导入时作工作区名） |
| `graph_name` | 人类可读名 |
| `spec_version` | 产出资产所依据的"三层图谱构建规范"版本（溯源） |
| `generated_at` | 生成时间（导入时由打包方写入；平台不依赖运行时时钟生成业务值） |
| `object_counts` | `{ObjectType: 数量}` 概览 |
| `types_ext` | （可选）引用 `types/` 下的扩展类型声明清单 |

### 5.3 md 三段式（每个对象一个 md）

```
---
id: UDG@MMLCommand@ADD URR          # 对象身份（逻辑ID，版本无关）
type: MMLCommand
nf: UDG
version: 20.15.2
...其它 frontmatter 字段（因 type 而异）
---
# ADD URR
（正文：原始 md 原文 / 类型化模板内容）

## 边
- 操作配置对象: [[UDG@ConfigObject@URR]]
- 参见: [[UDG@MMLCommand@MOD URR]]
```

- **frontmatter 不存边**；边只在底部 `## 边` 章节，用 `[[逻辑ID]]`。
- **身份规则**：frontmatter `id` + `type` 为权威；存储路径仅落地用，解析器对路径/命名变体容错。

### 5.4 命名约定（落地，非身份）

- NF 作用域类：`{ObjectType}/{nf}/{version}/{nf}@{Type}@{local}.md`
- 跨 NF 类：`{ObjectType}/{Type}@{local}.md`
- 文件名保留命令原始空格（与规范一致）。

### 5.5 导入流程

1. 上传 zip → 解包到临时区。
2. 校验 manifest（`bundle_format_version` 兼容性、必填字段）。
3. 校验每个 md：能解析 YAML frontmatter、有 `id`+`type`、`type` 在注册表中（默认或扩展）。
4. 落地到 `<data>/graphs/{graph_id}/`；写一份平台侧 `_import_manifest.json`（记录导入时间、源 bundle 版本、对象计数、校验结果）。
5. 全量解析建内存索引。
6. 失败策略：整包校验失败则拒绝导入并返回校验报告（哪些 md 缺字段/类型未注册）；不部分落地。

### 5.6 导出流程

1. 选定图谱工作区 `{gid}`。
2. 收集其下所有 md + 生成 `manifest.yaml`（`object_counts` 实测、`spec_version` 取导入时记录）。
3. 打 zip 返回（流式下载）。
4. 无损保证：导出 = 工作区目录快照，不修改任何 md 内容。

---

## 6. 通用对象/边模型 + 解析器 — S2

### 6.1 Object（通用结构，不写死类型）

```
Object = {
  logical_id:   "{nf}@{Type}@{local}"   # 版本无关身份（来自 frontmatter id）
  type:         str                      # 来自 frontmatter type
  nf:           str | None               # NF 作用域类有；跨 NF 类无
  version:      str | None
  frontmatter:  dict                     # 原始 YAML（除 id/type 外全部字段透传）
  body_md:      str                      # 正文（去掉 frontmatter 与 ## 边 章节后的 md）
  raw_md:       str                      # 原始全文（API /md 返回）
  source_path:  str                      # 工作区内相对路径
}
```

### 6.2 Edge（不存储，动态解析）

```
Edge = { from: logical_id, relation: str, to: logical_id }
```

- 来源 ①：每个 md 的 `## 边` 章节里的 `- {relation}: [[{to_logical_id}]]`（**通用解析器**，v1 核心，对所有类型生效）。
- 来源 ②：**可组装边解析插件**（移植规范 EDGE_MODULES）：纯函数 `(object, ctx) -> [Edge]`，可按 type 启用。v1 默认带：
  - `edge_explicit`（通用，解析 `## 边`）—— 必备。
  - 可选：`edge_cmd_to_configobj`（命令→配置对象，命令名推导）、`edge_cmd_seealso`（命令↔命令参见，正文扫描））—— 作为示例插件，按需启用。
- **新增一种边 = 加一个插件**，不动核心；插件注册在 `edge_resolvers` 列表。
- 去重：同一 `(from, relation, to)` 多源命中只保留一条（保留来源标记用于调试）。

### 6.3 对象类型注册表（数据驱动，可扩展）

平台内置默认注册表（对齐"三层图谱构建规范"对象类型），每个类型一条声明：

```yaml
# 默认注册表示例
object_types:
  MMLCommand:
    scope: nf               # nf 作用域（有 nf/version）| cross（跨 NF）
    frontmatter_required: [id, type, nf, version]
    frontmatter_optional: [verb, object_keyword, command_category, is_dangerous, ...]
    edge_resolvers: [edge_explicit, edge_cmd_to_configobj, edge_cmd_seealso]
  ConfigObject:
    scope: nf
    frontmatter_required: [id, type, nf, version]
    edge_resolvers: [edge_explicit]
  Feature:     { scope: nf, ... }
  License:      { scope: nf, ... }
  Task:         { scope: nf, ... }          # 原子(0-)/步骤(1-)/特性(2-) 统一 Task，layer 字段区分
  DecisionPoint:{ scope: nf, ... }
  BusinessDomain:       { scope: cross, ... }
  NetworkScenario:      { scope: cross, ... }
  ConfigurationSolution:{ scope: cross, ... }
```

- bundle 可在 `types/` 下携带扩展类型声明，导入时合并进注册表（同名类型以 bundle 扩展覆盖默认，记录告警）。
- **新增对象类型 = 注册表加一条**，无需改代码——满足"可能会扩展，但保持一套通用机制"。
- frontmatter 校验：v1 仅校验 `required` 字段存在；`optional` 透传不强校验类型（避免过严阻塞导入）。

### 6.4 版本解析（逻辑ID → 物理文件）

- 逻辑ID 版本无关；引用 `[[UDG@MMLCommand@ADD URR]]` 需解析到具体版本文件。
- v1 规则：同一逻辑ID 若多版本共存，解析为**最新版本**（按 version 字符串排序），并在导入时记录告警。
- v1 局限：多版本精细选择（如按查询参数指定版本）留二期。

---

## 7. 存储与索引

### 7.1 目录布局（平台内部，与仓库 assets/ 无关）

```
<data>/graphs/
  {graph_id}/                       # 一个工作区 = 一份导入的图谱
    manifest.yaml                   # 导入时来自 bundle
    Command/{nf}/{version}/*.md
    ConfigObject/{nf}/{version}/*.md
    Feature/{nf}/{version}/*.md
    ...
    _import_manifest.json           # 平台侧导入记录
    _index/                         # (可选) 解析索引缓存，可从 md 重建
```

- `<data>` 由配置指定（默认 `./platform-data/`，平台自管，不放进仓库 assets/）。

### 7.2 内存索引（启动/导入时全量建）

- 遍历工作区所有 md → 解析为 Object → 运行边解析管线 → 产出 Edge 列表。
- 建邻接表：`out_edges[from] = [Edge]`、`in_edges[to] = [Edge]`（反链）。
- 索引结构：`objects_by_id`、`objects_by_type`、`out_edges`、`in_edges`。
- v1 只读：导入时全量重建即可，无需增量（二期编辑再考虑增量）。
- 规模：单网元 ~4600 命令 + ~2200 配置对象，全图谱万级对象，内存索引+启动全量解析可接受（参考 platform-next 实测）。

---

## 8. 读 API — S3

全部 `GET`、只读；前缀 `/api/v1`。`gid` = 图谱工作区标识。

| 端点 | 职责 | 关键参数/响应 |
|---|---|---|
| `GET /graphs` | 图谱列表 | `[{graph_id, graph_name, object_counts, imported_at}]` |
| `POST /graphs/import` | 导入 bundle | multipart zip → `{graph_id, warnings[], object_counts}` |
| `DELETE /graphs/{gid}` | 删除工作区 | （只读语义外的一个管理动作，v1 提供） |
| `GET /graphs/{gid}/export` | 导出 bundle | 流式 zip 下载 |
| `GET /graphs/{gid}/stats` | 统计 | `{object_counts_by_type, edge_count, ...}` |
| `GET /graphs/{gid}/objects` | 列对象 | `?type=&q=&page=&size=` → `[{logical_id, type, nf, name}]` |
| `GET /graphs/{gid}/objects/{logical_id}` | **单对象** | `{...Object, out_edges[]}` |
| `GET /graphs/{gid}/objects/{logical_id}/neighbors` | **单跳** | `?hops=1`（默认1）→ `{center, out[], in[]}` |
| `GET /graphs/{gid}/objects/{logical_id}/md` | 原始 md | `text/markdown`（`raw_md`） |
| `GET /graphs/{gid}/subgraph` | N 跳子图 | `?center=&hops=&type=` → `{nodes[], edges[]}` |

### 8.1 logical_id 编码

- URL 中 `{logical_id}` 含 `@` 与可能的空格，需 URL-encode（`%40`、`%20`）。
- 别名：v1 同时支持按 `?nf=&type=&local=` 查询参数定位（更 URL 友好），二选一。

### 8.2 错误处理

- 图谱不存在 → 404。
- 对象不存在 → 404 + 提示最近匹配（可选）。
- 导入校验失败 → 400 + 校验报告（缺字段/类型未注册的 md 清单）。
- bundle 格式版本不兼容 → 400 + 明确提示。

### 8.3 二期预留

- 写端点（`POST/PUT/DELETE /objects`）、版本端点、CR 端点——v1 不暴露，但路由命名空间预留（如 `/objects/{id}` 的 POST 留空）。

---

## 9. 前端（三栏只读浏览器）

### 9.1 布局

```
┌──────────┬───────────────────────┬─────────────────┐
│ 对象索引  │  对象 md（选中）        │ 节点图 (1跳)      │
│ 🔍搜索   │ ───────────────────── │    ●当前          │
│ ▾命令    │ # ADD URR              │   / | \          │
│ ▾配置对象 │ frontmatter...         │  ●   ●  ●邻居    │
│ ▾特性    │ 正文...                 │ 点邻居→跳转       │
│ ▾task    │ ## 边                   │ + 邻居清单        │
│ ▾业务对象 │ - 操作:[[URR]]         │  • URR(配置对象)  │
└──────────┴───────────────────────┴─────────────────┘
```

### 9.2 组件与交互

- **左栏 对象索引**：按 `type` 分组折叠树，每组显示计数；顶部搜索框（`/objects?q=` 子串匹配 logical_id/name）。点击对象 → 中栏+右栏联动。
- **中栏 md**：渲染选中对象的 `raw_md`（markdown-it + DOMPurify，复用 platform-next）。顶部显示 type/nf/version badge。只读，无编辑器（二期）。
- **右栏 节点图**：vis-network 渲染单跳邻居（`/neighbors?hops=1`），中心=当前对象，邻居可点击 → 切换中心对象（联动中栏）。下方"邻居清单"列出 relation + 目标，可点击跳转。
- **顶栏**：图谱切换（`/graphs` 下拉）+ 导入/导出按钮。
- URL 驱动：`/g/{gid}/o/{logical_id}` 可分享/刷新定位。

### 9.3 不做（v1）

- 在线编辑器、CR/diff 视图、版本历史 UI、命令三级漏斗/特性/任务/业务等 platform-next 项目特定 tab。

---

## 10. 二期预留扣子

| 二期能力 | 接入点 | 说明 |
|---|---|---|
| S4 写 API + 在线编辑 | 存储层之上 | 存储层本就读写文件；加 POST/PUT/DELETE 端点 + 前端编辑器；触发索引重建 |
| S5 版本管理 | 存储层实现可换 | 现纯文件目录；二期换 git/快照做历史/回滚/published 版本，上层不动 |
| S6 变更评审回路 | 存储层之上 | CR=一批提议文件改动 → diff(提议 vs 当前) → 专家对比视图 → approve(写回+重建索引)/reject(丢弃)；不依赖版本管理 |
| Agent 同步关联知识 | CR 提交侧（平台外） | 平台只承载 CR+diff+决策；Agent 在平台外算好改动集再提交；平台与具体 LLM 解耦 |
| 多用户/鉴权 | API 层 | 路由/数据结构按可加鉴权设计 |

---

## 11. 技术栈

- **后端**：Python + FastAPI + uvicorn（复用 platform-next 模式：单例 service + 内存索引）。依赖：fastapi、uvicorn、pyyaml、python-multipart（上传）、可选 markdown 校验库。无 DB。
- **前端**：Vue 3 + TypeScript + Vite + Element Plus + vis-network + markdown-it + DOMPurify（复用 platform-next 技术栈与组件风格，精简）。
- **部署**：单进程本地启动；前端构建产物由后端静态托管（同 platform-next）。

---

## 12. 测试策略

- **单元**：md 三段式解析器、`## 边` 解析器、EDGE_MODULES 插件、类型注册表查找/扩展合并、版本解析、邻接表/BFS。
- **集成**：读 API 端点（单对象/单跳/子图/列表/搜索）正确性；导入校验失败路径；导出无损（导入→导出→再导入，对象/边一致）。
- **端到端**：用一个样例 bundle（见 §13）导入 → 三栏前端浏览游走 → 导出比对。
- **覆盖率目标**：核心解析/索引/API ≥ 80%。

---

## 13. 样例 bundle（验证用）

v1 需要一个真实样例验证。鉴于平台与 `assets/` 解耦，样例 bundle 作为**一次性测试夹具**（不进入平台运行时）：
- 从仓库现有 `assets/`（或 `三层图谱资产/`）抽样打包一个小 bundle（如某网元命令+配置对象+若干特性，~50 对象），转为规范三段式 + `## 边` + manifest。
- 仅用于开发/测试，不构成平台对任何项目的依赖。

---

## 14. 验收标准（v1）

1. 能导入一个符合 §5 格式的样例 bundle，校验通过，工作区落地。
2. `单对象` API 返回正确 frontmatter+正文+出向边；`单跳` API 返回正确邻居（含反链）。
3. 三栏前端：左索引按类型分组+搜索可用；点对象联动中栏 md + 右栏节点图；点邻居可游走。
4. 导出 bundle 后再导入，对象/边与原一致（无损往返）。
5. 导入非法 bundle（缺字段/未知类型）返回明确校验报告，不部分落地。
6. 平台代码不含任何对具体业务（计费/带宽/SFCGraph 命名）的硬编码引用。

---

## 15. 开放问题 / 风险

| 项 | 说明 | v1 处置 |
|---|---|---|
| 样例 bundle 来源 | 需从现有 assets/ 抽样转换 | 开发期制作为测试夹具 |
| 多版本同逻辑ID | 解析规则 | 取最新版本 + 告警；精细选择留二期 |
| 大图谱性能 | 万级对象全量解析 | 参考 platform-next 实测可接受；超大规模再优化 |
| 类型注册表扩展机制 | bundle 携带扩展类型的合并/覆盖语义 | v1 简单合并 + 同名告警；冲突策略留二期细化 |
| `## 边` relation 词汇 | 不同类型 relation 命名不一 | v1 不强约束词汇，透传字符串；汇总统计供后续规范化 |
| 平台代码仓库位置 | 平台代码放仓库何处 | 实现期决定（plan 阶段） |
