# 图谱资产管理平台 v1 设计

> 日期：2026-07-16
> 状态：设计待评审（r2：按"已有 assets/ 约定"纠正资产格式/目录/边解析）
> 范围：v1（导入导出 + 通用解析 + 读API + 只读三栏前端）

---

## 1. 背景与目标

### 1.1 现状（来自上下文梳理）

- **platform-next**：成熟的"只读知识库浏览器"（Vue3+TS / FastAPI 内存单例、无 DB）。已有"单对象 + 单跳(BFS子图)"读 API，查询架构干净**可复用**。但写侧全空，且**强耦合**具体项目资产（business_graph 写死 `business-graph/*/three-layer-graph/` + 1228 行专用 `graph_parser`；command/feature 读 jsonl；task 读 yaml），不可通用。
- **三层图谱构建规范**（VERSION 0.8.1）：定义资产格式 + 构建流程；command 层端到端跑通。资产 = md（YAML frontmatter + 正文）；对象间关系用 `[[...]]`/markdown 链接承载；EDGE_MODULES 是可组装的边构建模块。
- **已有 assets/ 约定（本次设计对齐对象，经实测核实）**：
  - 层目录全小写：`command`/`configobject`/`feature`/`license`/`task`/`business`/`evidence`；NF 缩写全大写（UDG/UNC）。
  - NF 隔离类（命令/配置对象/特性/license/task）：目录 `{layer}/{nf}/{version}/`，frontmatter `id` = **4 段** `{nf}@{version}@{Type}@{semantic}`（如 `UDG@20.15.2@MMLCommand@ADD URR`）。
  - 跨 NF 类（业务域/场景/方案）：目录 `business/{domain}/{scenario}/`，frontmatter `id` = **2 段** `{Type}@{semantic}`，带 `domain`/`scenario` 路由字段。
  - **边 = 正文里的 assets 根路径 markdown 链接** `[显](layer/.../file.md)`；`[[ID]]` 仅作"待建占位"。
- **资产现实**：形态不统一、6+ 目录并存；全仓零导入导出/打包工具。

### 1.2 目标

构建一个**完全独立于具体项目资产**的"图谱资产管家"：上传一份图谱（md 压缩包）→ 平台**自动解压、分析、归类**到标准资产目录 → 用**通用机制**承载对象/边 → 提供**读 API（单对象/单跳）**与**只读三栏前端**浏览游走 → 可导出。

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
| **S1 资产包导入/导出** | bundle = zip(md 文件，**无 manifest**)；import **按 frontmatter 自动归类并合并进统一资产库**（多次上传累积，同 id 即更新）；export 导出资产库（可按 nf/version/domain 过滤） |
| **S2 通用对象/边模型 + 解析器** | frontmatter+正文 → 通用 Object + 动态解析 Edge；对象类型注册表（平台默认 + bundle 可扩展）；边解析插件管线（**markdown 链接 + `[[ID]]`** 解析 + 可选 EDGE_MODULES 插件） |
| **S3 读 API** | 单对象 / 单跳(BFS) / 列表(+搜索) / 子图 / 原始 md / 统计 |
| **前端** | 三栏只读浏览器：左=对象索引(按类型分组+搜索)，中=选中对象 md，右=节点图(单跳)+邻居清单 |

### 2.2 排除（二期，预留扣子）

- S4 写 API + 在线 md 编辑
- S5 资产内容级版本管理
- S6 变更评审回路 + Agent 同步关联知识

---

## 3. 核心设计决策（锁定）

1. **完全独立 + 统一资产库**：平台与仓库 `assets/` 无任何关系；平台内部是**唯一一份统一资产库**（不是每份导入一个隔离工作区）；多次上传**累积合并**进同一份库（同 id 后传覆盖先传 = 更新）；上传有记录但资产统一一份；导入单向吃入、导出单向吐出，不存在"同步回 assets/"。
2. **图谱 = 一堆 md 文件**（YAML frontmatter + 正文；正文内以 **markdown 链接** / `[[ID]]` 占位承载对象间关系，对齐已有 assets/ 约定）。
3. **导入/导出 = bundle（zip）**；bundle **不需要 manifest**，平台按每个 md 的 frontmatter 自动分析归类。
4. **单人优先**，API/存储/数据结构按日后可加登录与多人并发设计（留扣子）。
5. **存储 = 纯文件目录**（每图谱一个 md 目录）+ **内存解析索引**；不绑 git、不引入 DB（二期版本/评审以 git/快照或暂存区叠加）。
6. **对象身份 = frontmatter `id`**：NF 隔离类 4 段 `{nf}@{version}@{Type}@{semantic}`；跨 NF 类 2 段 `{Type}@{semantic}`。**没有"不带版本的 3 段"形态**——版本是身份的一部分，每版本即独立对象，无需版本动态解析。文件路径/文件名仅作落地，由 `id`+`type`+注册表派生。
7. **两类对象是所有命名差异的根源**（见 §5.3 表）：NF 隔离类 vs 跨 NF 类，目录结构、ID 段数、归类方式都据此分叉。
8. **边动态解析**（不单独存储）：① 正文 markdown 链接 `[显](layer/.../file.md)`（**主**，对齐已有 assets/）；② `[[ID]]` 占位（兼容待建）；③ 可组装边解析插件（按 type 启用，移植 EDGE_MODULES 思想）。
9. **类型注册表 = 平台默认 + bundle 可扩展**；新增对象类型 = 注册表加一条，不改码。
10. **复用**：platform-next 的"内存图 + BFS 子图"读模式；已有 assets/ 的目录/命名/链接约定；EDGE_MODULES 可组装边解析思想；platform-next 前端三栏/vis-network UI 风格（精简，不照搬其项目特定模块）。

---

## 4. 架构（分层）

```
┌─────────────────────────────────────────────────────────────┐
│  前端 Vue3+TS (三栏只读浏览器)                                 │
│  对象索引(类型分组+搜索) · 对象md · 节点图(单跳)+邻居清单        │
├─────────────────────────────────────────────────────────────┤
│  ⑤ 读 API (S3)   单对象/单跳(BFS)/列表/子图/raw md/统计        │
│  ④ 内存索引层    md解析→对象/边图→邻接表，导入时全量建          │
│  ③ 通用模型+解析层 (S2)   类型注册表 + 归类器 + 边解析插件管线   │
│  ② 存储层        唯一一份统一资产库(纯文件系统,沿用assets约定,多上传累积)│
│  ① 资产包格式层 (S1)   bundle=zip(md),导入自动归类合并,唯一解耦边界 │
├─────────────────────────────────────────────────────────────┤
│  〔预留二期〕S4写API/编辑 · S5版本 · S6评审回路+Agent  接在②之上 │
└─────────────────────────────────────────────────────────────┘
   平台只认：①bundle=md压缩包 ②frontmatter+正文+链接约定 ③类型注册表+边解析器
   不认任何具体业务（计费/带宽/SFCGraph 一概不知）
```

**解耦边界**：平台唯一对外契约是 ① bundle（md 压缩包，无 manifest）+ ② frontmatter/正文/链接约定 + ③ 类型注册表/边解析器。除此之外平台对任何具体业务领域一无所知。

---

## 5. 资产包格式与导入归类（Bundle）— S1

### 5.1 bundle 是什么

bundle = **一个 zip，里面就是一堆 md 文件**（每个对象一个 md）。**不需要 manifest**。平台读取每个 md 的 frontmatter `id`/`type`，自动分析归类，**合并进平台唯一的统一资产库**（§5.4）。多次上传累积：同 id 的对象后传覆盖先传（=更新）。

zip 内文件可以是任意原始排布（平铺、旧目录、混合）——平台**不关心源文件名/源路径，只认 frontmatter**，导入时统一归一化重写到标准资产目录。

### 5.2 md 格式（每个对象一个 md）

```
---
id: UDG@20.15.2@MMLCommand@ADD URR     # 4段(NF隔离类) / 2段(跨NF类)，见§5.3
type: MMLCommand
nf: UDG
version: 20.15.2
...其它 frontmatter 字段（因 type 而异）
---
# ADD URR
（正文）

## 操作的配置对象
- [URR](configobject/UDG/20.15.2/ConfigObject@URR.md)     # markdown 链接 = 边
## 参见
- [MOD URR](command/UDG/20.15.2/MMLCommand@MOD URR.md)
```

- 对象间关系（边）= 正文里的 **assets 根路径 markdown 链接** `[显](layer/.../Type@semantic.md)`（对齐已有 assets/ 约定）；`[[ID]]` 双括号为"待建占位"，平台一并解析。
- 身份权威 = frontmatter `id` + `type`。

### 5.3 两类对象（所有命名差异的根源）

| 类别 | 带 nf@version | ID 段数 | 资产目录 | 对象 |
|---|---|---|---|---|
| **NF 隔离类** | 是 | 4 段 `{nf}@{version}@{Type}@{semantic}` | `{layer}/{nf}/{version}/` | 命令(MMLCommand)、配置对象(ConfigObject)、特性(Feature)、license、task |
| **跨 NF 类** | 否 | 2 段 `{Type}@{semantic}` | `{layer}/{domain}/{scenario}/` | 业务域(BusinessDomain)、场景(NetworkScenario)、方案(ConfigurationSolution) |

- `layer` 由 `type` 经注册表派生，**全小写**：MMLCommand→command、ConfigObject→configobject、Feature→feature、License→license、Task→task、BusinessDomain/NetworkScenario/ConfigurationSolution→business。
- NF 缩写全大写（UDG/UNC），版本点分字符串（20.15.2）。

### 5.4 自动归类规则（导入时按 frontmatter 派生路径 + 文件名）

文件名统一归一化为 **`{Type}@{semantic}.md`**（semantic = id 末段，保留空格）。

- **NF 隔离类**：从 4 段 id 取 `nf`/`version`，路径 `{layer}/{nf}/{version}/{Type}@{semantic}.md`。
  - 例：id `UDG@20.15.2@MMLCommand@ADD URR` → `command/UDG/20.15.2/MMLCommand@ADD URR.md`
- **跨 NF 类**：从 frontmatter `domain`/`scenario` 字段取路径（id 只有 2 段，不够拆路径，靠字段）：
  - BusinessDomain（只有 domain）：`business/{domain}/BusinessDomain@{domain}.md`
  - NetworkScenario（domain+scenario）：`business/{domain}/{scenario}/NetworkScenario@{scenario}.md`
  - ConfigurationSolution（domain+scenario）：`business/{domain}/{scenario}/ConfigurationSolution@{semantic}.md`（semantic 即 id 末段；惯例写作 `{scenario}-{solution}` 如 `charging-online`，但结构上只是 id 末段，**无需单独 solution 字段**）
  - 例：domain=business-awareness, scenario=charging → `business/business-awareness/charging/ConfigurationSolution@charging-online.md`
- **evidence 等非对象文件**：无 frontmatter `id` 的 md（证据、index 等）按原相对位置放到 `evidence/...`，**不作为图谱对象索引**（仅作溯源引用目标）。

> 注：仓库现有 `assets/business/apn-domain/` 是**偏离约定**的扁平结构（缺 scenario 夹层）。平台按 §5.4 约定归类，不迁就该偏差；若上传的 apn 资产 frontmatter 带 `scenario` 字段，会正确归到 `business/apn-domain/{scenario}/`。

### 5.5 导入流程

1. 上传 zip → 解包到临时区。
2. **先**扫描 bundle 内 `types/`（若有）合并进注册表，**再**逐个 md：解析 frontmatter；须有 `id`+`type`，且 `type` 在合并后的注册表。
3. 按 §5.4 规则**派生标准路径 + 文件名**，归一化写入**统一资产库** `<data>/assets/`（覆盖源文件名/源路径）。与库中已有对象同 id（同路径）→ **后传覆盖先传 = 更新**，记为 `updated`；新对象记为 `added`。同 bundle 内若多个 md 归一化后撞同一路径（重复 id/semantic）→ 告警 + 后者覆盖前者。
4. 非 object md（无 id）→ 按 evidence 约定放置，不索引。
5. 追加写**上传记录**（append-only：时间、added/updated 计数、归类告警、悬空链接）——只记"传了什么"，资产本身是统一的一份。
6. 增量重建受影响对象的索引（或全量重建）。
7. 失败策略：md 缺 `id`/`type` 或 `type` 未注册 → 该文件记入校验报告并跳过（不阻塞整包其它对象）；整包无任何有效对象 → 拒绝导入。

### 5.6 导出流程

1. 导出**统一资产库**（可选过滤：`?nf=&version=&domain=&scenario=` 只导切片；不传 = 全量）。
2. 把命中目录（已归一化的标准资产目录）打 zip 流式下载。
3. 无损：导出 = 目录快照，不改任何 md。
4. 导出的 zip 可被本平台再次导入还原（往返一致）。

---

## 6. 通用对象/边模型 + 解析器 — S2

### 6.1 Object（通用结构，不写死类型）

```
Object = {
  id:           str           # frontmatter id（NF隔离类4段 / 跨NF类2段）——权威身份
  type:         str           # frontmatter type
  layer:        str           # 由 type 经注册表派生（command/configobject/.../business）
  scope:        "nf" | "cross"
  nf:           str | None    # NF隔离类有
  version:      str | None
  domain:       str | None    # 跨NF类有
  scenario:     str | None
  frontmatter:  dict          # 原始 YAML（除 id 外透传）
  body_md:      str           # 正文（去 frontmatter）
  raw_md:       str           # 原始全文（API /md）
  source_path:  str           # 资产库内归一化相对路径
}
```

### 6.2 Edge（不存储，动态解析）

```
Edge = { from: id, relation: str | None, to: id }
```

边从正文解析（对齐已有 assets/ 约定），**可组装插件管线**，纯函数 `(object, ctx) -> [Edge]`，按 type 启用：

- `edge_md_links`（**必备/默认**）：解析正文所有 markdown 链接 `[显](relpath.md)`，relpath 为 assets 根路径 → 解析为目标对象 id（见 §6.5）。
- `edge_wikilinks`（默认）：解析 `[[ID]]` 占位（待建对象）→ 按 id 直连。
- 可选插件（移植 EDGE_MODULES 思想）：如 `edge_cmd_operates`（命令"操作的配置对象"章节链接 → operates_on 关系）、`edge_cmd_seealso`（"参见"章节 → seealso）。**relation 标签**可由"所在章节标题 / 插件规则"派生；v1 无派生时 relation 留空（仅 from→to 邻居，足够前端单跳展示）。

- 新增一种边 = 加一个插件，不动核心。
- 去重：同 `(from, relation, to)` 多源命中保留一条（记来源标记）。
- v1 的 `edge_cmd_operates` 等是平台内置**重实现**，**不导入**规范 EDGE_MODULES 代码；仅借其"按章节/规则派生 relation"的思想。

### 6.3 对象类型注册表（数据驱动，可扩展）

平台内置默认注册表（对齐已有 assets/ 对象类型），每个类型声明：`layer`/`scope`/`id_segments`/`path_fields`/`frontmatter_required`/`edge_resolvers`。

```yaml
object_types:
  MMLCommand:    { layer: command,      scope: nf,    id_segments: 4, frontmatter_required: [id,type,nf,version],                              edge_resolvers: [edge_md_links, edge_wikilinks, edge_cmd_operates, edge_cmd_seealso] }
  ConfigObject:  { layer: configobject, scope: nf,    id_segments: 4, frontmatter_required: [id,type,nf,version],                              edge_resolvers: [edge_md_links, edge_wikilinks] }
  Feature:       { layer: feature,      scope: nf,    id_segments: 4, frontmatter_required: [id,type,nf,version],                              edge_resolvers: [edge_md_links, edge_wikilinks] }
  License:       { layer: license,      scope: nf,    id_segments: 4, frontmatter_required: [id,type,nf,version],                              edge_resolvers: [edge_md_links, edge_wikilinks] }
  Task:          { layer: task,         scope: nf,    id_segments: 4, frontmatter_required: [id,type,nf,version],                              edge_resolvers: [edge_md_links, edge_wikilinks] }
  BusinessDomain:        { layer: business, scope: cross, id_segments: 2, path_fields: [domain],           frontmatter_required: [id,type,domain],           edge_resolvers: [edge_md_links, edge_wikilinks] }
  NetworkScenario:       { layer: business, scope: cross, id_segments: 2, path_fields: [domain,scenario],   frontmatter_required: [id,type,domain,scenario],  edge_resolvers: [edge_md_links, edge_wikilinks] }
  ConfigurationSolution: { layer: business, scope: cross, id_segments: 2, path_fields: [domain,scenario],   frontmatter_required: [id,type,domain,scenario],  edge_resolvers: [edge_md_links, edge_wikilinks] }
```

- NF 隔离类路径由 id 4 段派生（`nf`/`version`）；跨 NF 类路径由 frontmatter `path_fields` 派生（`domain`/`scenario`）。
- **新增对象类型 = 注册表加一条**，不改码。

#### 6.3.1 扩展类型声明（bundle 携带，可选）

bundle 可在 `types/` 下带扩展类型，每类型一文件 `types/{TypeName}.yaml`，复用 §6.3 字段：

```yaml
# types/MyCustomType.yaml
layer: mylayer
scope: nf
id_segments: 4
frontmatter_required: [id, type, nf, version]
edge_resolvers: [edge_md_links]
```

- 导入时合并进注册表；同名类型 bundle 扩展覆盖默认 + 告警。
- `edge_resolvers` 引用未注册插件 → 告警，该类型退化为 `[edge_md_links]`。

### 6.4 版本解析（无需，已简化）

两类对象 id 本身已含版本（NF 隔离类）或不含版本概念（跨 NF 类），**无需"逻辑ID→物理文件"的版本动态解析**。同一语义对象的不同版本 = 不同 id 的独立节点，天然并列。（原 r1 设计的"取最新版本/排序"小节作废。）

### 6.5 链接 target 解析（markdown 链接 → 对象 id）

`edge_md_links` 把链接路径还原为目标对象 id，**对文件名归一化容错**（源文件名可能是旧 sanitized 形式 `ADD-URR.md`，归一化后是 `MMLCommand@ADD URR.md`）。

**路径分段推断 type 与路由键**（business 层有 3 个类型，不能靠 layer 单值推断）：

- NF 隔离类形状 `{layer}/{nf}/{version}/{file}`：layer→type **一对一**（command→MMLCommand、configobject→ConfigObject、feature→Feature、license→License、task→Task）；nf/version 从路径段取；semantic = `file` 去扩展名。
- business 类形状有两种深度：
  - `business/{domain}/{Type}@{slug}`（2 段，BusinessDomain）→ type 从文件名 `{Type}@` 前缀取；domain 从路径段取。
  - `business/{domain}/{scenario}/{Type}@{slug}`（3 段，NetworkScenario / ConfigurationSolution）→ type 从文件名前缀取；domain/scenario 从路径段取。
- 相对路径链接（`./`、`../`）→ 先按所在 md 路径归一化为 assets 根路径再解析；无法归一化 → 告警跳过。

**匹配策略**（先收窄再比对，避免万级对象误连）：

1. 用路径推断出的 (layer, nf, version) 或 (domain, scenario) **收窄候选集**到同一路由桶；
2. 桶内把链接 `file`/`slug` 与候选对象 semantic 做 **sanitized 归一比较**：`sanitize(s) = lowercase 后去除所有非 [a-z0-9] 字符`（`ADD URR` / `ADD-URR` / `addurr` 均归一为 `addurr`）；
3. 命中即连；桶内多义或未命中 → 记悬空链接告警（不阻断）。

这保证 §5.4 的文件名归一化**不会打断**正文里的旧式链接。

---

## 7. 存储与索引

### 7.1 目录布局（平台内部，沿用已有 assets/ 约定）

```
<data>/assets/                       # 唯一统一资产库（多次上传累积合并）
  command/{nf}/{version}/{Type}@{semantic}.md        # NF隔离类
  configobject/{nf}/{version}/{Type}@{semantic}.md
  feature/{nf}/{version}/{Type}@{semantic}.md
  license/{nf}/{version}/{Type}@{semantic}.md
  task/{nf}/{version}/{Type}@{semantic}.md
  business/{domain}/BusinessDomain@{domain}.md
  business/{domain}/{scenario}/NetworkScenario@{scenario}.md
  business/{domain}/{scenario}/ConfigurationSolution@{semantic}.md
  evidence/...                                        # 非对象（溯源）
  _imports.log                     # append-only 上传记录
  _index/                          # (可选) 解析索引缓存，可从 md 重建
```

- `<data>` 由配置指定（默认 `./platform-data/`，平台自管，与仓库 assets/ 无关）。
- **一份资产库**，多次上传按 §5.4 归类累积进同一目录树；层目录全小写。

### 7.2 内存索引（启动/导入时全量建）

- 遍历资产库所有 md → 解析为 Object → 运行边解析管线 → 产出 Edge 列表。
- 建邻接表：`out_edges[from] = [Edge]`、`in_edges[to] = [Edge]`（反链）。
- 索引结构：`objects_by_id`、`objects_by_type`、`out_edges`、`in_edges`。
- v1 只读：导入时全量重建即可，无需增量（二期编辑再考虑增量）。
- 规模：单网元 ~4600 命令 + ~2200 配置对象，全库万级对象，内存索引 + 启动全量解析可接受（参考 platform-next 实测）。
- 统一资产库：单一索引；上传后增量或全量重建。

---

## 8. 读 API — S3

读端点全部 `GET`、只读；另含上传端点（`import`）。前缀 `/api/v1`。**无 `gid`**——平台只有一份统一资产库，所有查询直接打这份库。

| 端点 | 职责 | 关键参数/响应 |
|---|---|---|
| `POST /import` | 上传 bundle，合并进资产库 | multipart zip → `{added, updated, warnings[], counts}` |
| `GET /imports` | 上传记录（可选） | `[{time, added, updated, warnings_n}]` |
| `GET /export` | 导出资产库 | `?nf=&version=&domain=&scenario=`（可选过滤）→ 流式 zip |
| `GET /stats` | 统计 | `{object_counts_by_type, edge_count, ...}` |
| `GET /objects` | 列对象 | `?type=&q=&nf=&version=&domain=&page=&size=` → `[{id, type, nf|domain, name}]` |
| `GET /objects/{id}` | **单对象** | `{...Object, out_edges[]}` |
| `GET /objects/{id}/neighbors` | **单跳** | `?hops=1`（默认1）→ `{center, out[], in[]}` |
| `GET /objects/{id}/md` | 原始 md | `text/markdown`（`raw_md`） |
| `GET /subgraph` | N 跳子图 | `?center=&hops=&type=` → `{nodes[], edges[]}` |

### 8.1 对象 id 编码（URL）

- 路径里 `{id}` 含 `@` 与可能的空格，须 URL-encode（`%40`、`%20`）。例：`/objects/UDG%4020.15.2%40MMLCommand%40ADD%20URR`。
- 别名（更 URL 友好）：按 `?type=&nf=&version=&semantic=`（NF 隔离类）或 `?type=&domain=&scenario=&semantic=`（跨 NF 类）查询参数定位。理论上 semantic 唯一不会撞；若命中多条 → 409 + 候选清单。

### 8.2 错误处理

- 对象不存在 → 404 + 提示最近匹配（可选）。
- 导入校验失败 → 400 + 校验报告（缺字段/类型未注册的 md 清单）。

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
│ ▾特性    │ 正文(含markdown链接)    │ 点邻居→跳转       │
│ ▾task    │ ## 操作的配置对象       │ + 邻居清单        │
│ ▾业务对象 │ - [URR](.../URR.md)    │  • URR(配置对象)  │
└──────────┴───────────────────────┴─────────────────┘
```

### 9.2 组件与交互

- **左栏 对象索引**：按 `type` 分组折叠树，每组显示计数；顶部搜索框（`/objects?q=` 子串匹配 id/name）。点击对象 → 中栏+右栏联动。
- **中栏 md**：渲染选中对象的 `raw_md`（markdown-it + DOMPurify，复用 platform-next）。顶部显示 type/nf/version（或 domain/scenario）badge。只读，无编辑器（二期）。
- **右栏 节点图**：vis-network 渲染单跳邻居（`/neighbors?hops=1`），中心=当前对象，邻居可点击 → 切换中心对象（联动中栏）。下方"邻居清单"列出 relation + 目标，可点击跳转。
- **顶栏**：导入/导出按钮 + 统计概览（无图谱切换，只有一份统一资产库）。
- URL 驱动：`/o/{id}` 可分享/刷新定位。

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

- **后端**：Python + FastAPI + uvicorn（复用 platform-next 模式：单例 service + 内存索引）。依赖：fastapi、uvicorn、pyyaml、python-multipart（上传）。无 DB。
- **前端**：Vue 3 + TypeScript + Vite + Element Plus + vis-network + markdown-it + DOMPurify（复用 platform-next 技术栈与组件风格，精简）。
- **部署**：单进程本地启动；前端构建产物由后端静态托管（同 platform-next）。

---

## 12. 测试策略

- **单元**：frontmatter 解析器、markdown 链接/`[[ID]]` 边解析器、EDGE_MODULES 插件、链接 target 解析（含 sanitized 匹配）、归类器（id/字段 → 路径+文件名）、类型注册表查找/扩展合并、邻接表/BFS。
- **集成**：读 API 端点（单对象/单跳/子图/列表/搜索）正确性；导入校验失败路径；导出无损（导入→导出→再导入，对象/边一致）。
- **端到端**：用一个样例 bundle（见 §13）导入 → 三栏前端浏览游走 → 导出比对。
- **覆盖率目标**：核心解析/索引/API ≥ 80%。

---

## 13. 样例 bundle（验证用）

v1 需要一个真实样例验证。鉴于平台与 `assets/` 解耦，样例 bundle 作为**一次性测试夹具**（不进入平台运行时）：
- 从仓库现有 `assets/` 抽样打包一个小 bundle（某网元命令 + 配置对象 + 若干特性 + 一个业务域/场景/方案，~50 对象），保持 frontmatter(id/type/nf/version/domain/scenario) + 正文 markdown 链接原样（**无需 manifest**）。
- 仅用于开发/测试，不构成平台对任何项目的依赖。

---

## 14. 验收标准（v1）

1. 能导入一个符合 §5 格式的样例 bundle（md zip，无 manifest），归类正确，**合并进统一资产库**为标准资产目录。
2. `单对象` API 返回正确 frontmatter+正文+出向边；`单跳` API 返回正确邻居（含反链）。
3. 三栏前端：左索引按类型分组+搜索可用；点对象联动中栏 md + 右栏节点图；点邻居可游走。
4. 导出 bundle 后再导入，对象/边与原一致（无损往返）。
5. 导入非法 md（缺 id/type、未知类型）返回明确校验报告并跳过该文件，不阻塞整包。
6. 平台代码不含任何对具体业务（计费/带宽/SFCGraph 命名）的硬编码引用。

---

## 15. 开放问题 / 风险

| 项 | 说明 | v1 处置 |
|---|---|---|
| 样例 bundle 来源 | 需从现有 assets/ 抽样 | 开发期制作为测试夹具 |
| 文件名归一化 vs 旧链接 | 归一化为 `{Type}@{semantic}` 可能与旧 sanitized 文件名链接不一致 | 链接 target 用 sanitized 匹配容错（§6.5），不阻断 |
| 层目录大小写 | 现有 assets/ 全小写层目录 | 平台沿用小写层目录（command/configobject/...），Type 用 PascalCase |
| 边 relation 标签 | markdown 链接无结构化 relation 字段 | v1 默认 relation 留空（仅 from→to）；按章节派生 relation 作可选插件 |
| 大图谱性能 | 万级对象全量解析 | 参考 platform-next 实测可接受；超大规模再优化 |
| 类型注册表扩展机制 | bundle 携带扩展类型的合并/覆盖语义 | v1 简单合并 + 同名告警；冲突策略留二期细化 |
| 平台代码仓库位置 | 建议新建顶层 `graph-asset-platform/`（独立于 platform-next 与 assets/） | plan 启动时确认 |
