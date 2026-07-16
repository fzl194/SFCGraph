# 图谱资产管理平台 v1 设计

> 日期：2026-07-16
> 状态：设计待评审（r4：以"三层图谱构建规范/command"为权威，订正 ID/目录/边/版本解析）
> 范围：v1（导入导出 + 通用解析 + 读API + 只读三栏前端）

---

## 1. 背景与目标

### 1.1 现状（来自上下文梳理）

- **platform-next**：成熟的"只读知识库浏览器"（Vue3+TS / FastAPI 内存单例、无 DB）。已有"单对象 + 单跳(BFS子图)"读 API，查询架构干净**可复用**。但写侧全空，且**强耦合**具体项目资产（business_graph 写死 `business-graph/*/three-layer-graph/` + 1228 行专用 `graph_parser`；command/feature 读 jsonl；task 读 yaml），不可通用。
- **三层图谱构建规范/command（本平台资产格式的权威依据）**：command 层端到端跑通。其锁定的资产约定（`需求与路线.md` §6/§7、`字段定义.md`、`check.md`、`build_commands.py` 实测一致）：
  - 对象 **ID = 3 段 `{nf}@{Type}@{local}`，不带版本**（如 `UDG@MMLCommand@ADD URR`）。
  - **目录 `{Layer}/{nf}/{version}/` 带版本**；**frontmatter `nf`/`version` 字段带版本**；**文件名 = 完整逻辑ID `{nf}@{Type}@{local}.md`**（带 nf、不带版本、保留空格）。
  - **边 = md 底部 `## 边` 章节**，格式 `- {关系}: [[{nf}@{Type}@{local}]]`（wikilink，不带版本）。
  - 引用/边**不带版本**，解析时**动态选版本**——但规范**未定义**选版本的算法（留平台设计，见 §6.4）。
- **资产现实**：现有 `assets/` 是规范资产的"编译后"形态（wikilink 已被替换成 markdown 路径链接、ID 带 version），与本平台遵循的**源规范**不同；全仓零导入导出工具。

### 1.2 目标

构建一个**完全独立**的图谱资产管理平台：上传 md 资产包 → 平台**自动解压、分析、归类**合并进**唯一统一资产库** → 用**通用机制**承载对象/边（遵循 command 规范的 ID/目录/`## 边` 约定）→ 提供**读 API（单对象/单跳）**与**只读三栏前端**浏览游走 → 可导出。

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
| **S1 资产包导入/导出** | bundle = zip(md 文件，**无 manifest**)；import **按 frontmatter 自动归类并合并进统一资产库**（多次上传累积，同 id 后传即更新）；export 导出资产库（可按 nf/version/domain 切片） |
| **S2 通用对象/边模型 + 解析器** | frontmatter+正文+`## 边` → 通用 Object + 动态解析 Edge；对象类型注册表（平台默认 + bundle 可扩展）；边解析（`## 边` wikilink 为主）；**版本双模解析（默认/指定）** |
| **S3 读 API** | 单对象 / 单跳(BFS) / 列表(+搜索) / 子图 / 原始 md / 统计 |
| **前端** | 三栏只读浏览器：左=对象索引(按类型分组+搜索)，中=选中对象 md，右=节点图(单跳)+邻居清单；顶栏含版本选择器 |

### 2.2 排除（二期，预留扣子）

- S4 写 API + 在线 md 编辑
- S5 资产内容级版本管理
- S6 变更评审回路 + Agent 同步关联知识

---

## 3. 核心设计决策（锁定）

1. **完全独立 + 统一资产库**：平台与仓库 `assets/` 无任何关系；平台内部是**唯一一份统一资产库**（不是每份导入一个隔离工作区）；多次上传**累积合并**进同一份库（同 id 后传覆盖先传 = 更新）；上传有记录但资产统一一份；导入单向吃入、导出单向吐出。
2. **资产格式以 `三层图谱构建规范/command` 为权威**（不是现有 assets/ 的编译后形态）。
3. **图谱 = 一堆 md 文件**：YAML frontmatter + 正文 + 底部 `## 边` 章节（边用 wikilink `[[...]]`）。
4. **对象 ID 版本无关**：NF 隔离类 **3 段 `{nf}@{Type}@{local}`**（有 nf、无 version）；跨 NF 类 **2 段 `{Type}@{semantic}`**。**版本只出现在目录和 frontmatter 字段，不出现在 ID/文件名语义/引用里。**
5. **目录/文件名**：NF 隔离类 `{Layer}/{nf}/{version}/{nf}@{Type}@{local}.md`（层目录 PascalCase、版本在目录）；跨 NF 类 `Business/{domain}/[{scenario}/]{Type}@{semantic}.md`。**文件名 = 版本无关逻辑ID**。
6. **边 = `## 边` 章节 wikilink** `- {关系}: [[{nf}@{Type}@{local}]]`（不带版本）。平台只**解析**已构建的 `## 边`（派生由上游规范 builder 完成，平台不重新派生）。
7. **版本解析（默认/指定，填规范空白）**：图谱节点 = **(id, version)，每版本一独立节点**；`## 边` 的版本无关引用 `[[id]]` 与 `GET /objects/{id}`（不带版本）**默认解析为该 id 最新现存版本**（语义化排序；常见≈网元最新，若 id 仅存旧版本则落到其最新现存——**不把确实存在的对象判 404**）；**显式切换**（`?version=`/前端选择器）指向指定版本，指定版本不存在则 404 + 列出可用版本。
8. **单人优先**，API/存储/数据结构按日后可加登录与多人并发设计（留扣子）。
9. **存储 = 纯文件目录**（统一资产库）+ **内存解析索引**；不绑 git、不引入 DB。
10. **类型注册表 = 平台默认 + bundle 可扩展**；新增对象类型 = 注册表加一条，不改码。
11. **复用**：platform-next 的"内存图 + BFS 子图"读模式；command 规范的 ID/目录/`## 边` 约定；platform-next 前端三栏/vis-network UI 风格（精简，不照搬其项目特定模块）。

---

## 4. 架构（分层）

```
┌─────────────────────────────────────────────────────────────┐
│  前端 Vue3+TS (三栏只读浏览器 + 版本选择器)                     │
│  对象索引(类型分组+搜索) · 对象md · 节点图(单跳)+邻居清单        │
├─────────────────────────────────────────────────────────────┤
│  ⑤ 读 API (S3)   单对象/单跳(BFS)/列表/子图/raw md/统计(+?version=)│
│  ④ 内存索引层    md解析→对象/边图→邻接表; 节点=版本无关id        │
│  ③ 通用模型+解析层 (S2)  类型注册表+归类器+ ##边 解析 + 版本双模解析│
│  ② 存储层        唯一一份统一资产库(纯文件系统, 遵循command规范)   │
│  ① 资产包格式层 (S1)   bundle=zip(md),导入自动归类合并,唯一解耦边界│
├─────────────────────────────────────────────────────────────┤
│  〔预留二期〕S4写API/编辑 · S5版本 · S6评审回路+Agent  接在②之上 │
└─────────────────────────────────────────────────────────────┘
   平台只认：①bundle=md压缩包 ②frontmatter+正文+##边约定 ③类型注册表
   不认任何具体业务（计费/带宽/SFCGraph 一概不知）
```

**解耦边界**：平台唯一对外契约是 ① bundle（md 压缩包，无 manifest）+ ② frontmatter/正文/`## 边` 约定 + ③ 类型注册表。除此之外对任何具体业务领域一无所知。

---

## 5. 资产包格式与导入归类（Bundle）— S1

### 5.1 bundle 是什么

bundle = **一个 zip，里面就是一堆 md 文件**（每个对象一个 md）。**不需要 manifest**。平台读取每个 md 的 frontmatter `id`/`type`，自动分析归类，**合并进平台唯一的统一资产库**（§5.4）。多次上传累积：同 id 的对象后传覆盖先传（=更新）。

zip 内文件可以是任意原始排布（平铺、旧目录、混合）——平台**不关心源文件名/源路径，只认 frontmatter**，导入时统一归一化重写到标准资产目录。

### 5.2 md 格式（每个对象一个 md，遵循 command 规范）

```
---
id: UDG@MMLCommand@ADD URR          # 3段逻辑ID（版本无关；= 文件名 = 引用键）
type: MMLCommand
name: ADD URR
nf: UDG                             # frontmatter 字段：带版本信息
version: 20.15.2
source: output/.../ADD URR_xxx.md
status: active
...其它字段（因 type 而异）
---
# ADD URR
（正文：原始 md 原文 / 类型化模板）

## 边                               # 底部专章：对象间关系
- 操作配置对象: [[UDG@ConfigObject@URR]]
- 参见: [[UDG@MMLCommand@MOD URR]]
```

- frontmatter `id`+`type` 为权威身份；`nf`/`version` 字段带版本（用于目录与版本解析）。
- **边只在底部 `## 边` 章节**，用 wikilink `[[{nf}@{Type}@{local}]]`（**不带版本**）；正文不重复关系。
- 无 `## 边` 的对象（如未构建边的）→ 出向边为空，不报错。

### 5.3 两类对象（所有命名差异的根源）

| 类别 | ID（版本无关） | 资产目录 | 文件名 | 对象 |
|---|---|---|---|---|
| **NF 隔离类** | 3 段 `{nf}@{Type}@{local}` | `{Layer}/{nf}/{version}/` | `{nf}@{Type}@{local}.md` | 命令(MMLCommand)、配置对象(ConfigObject)、特性(Feature)、license、task |
| **跨 NF 类** | 2 段 `{Type}@{semantic}` | `Business/{domain}/[{scenario}/]` | `{Type}@{semantic}.md` | 业务域(BusinessDomain)、场景(NetworkScenario)、方案(ConfigurationSolution) |

- `Layer` 由 `type` 经注册表派生，**PascalCase**：MMLCommand→Command、ConfigObject→ConfigObject、Feature→Feature、License→License、Task→Task、业务三类→Business。
- NF 缩写全大写（UDG/UNC），版本点分字符串（20.15.2）。
- **关键：版本只在 NF 隔离类的目录里，不在 ID/文件名里**；跨 NF 类无版本概念。

### 5.4 自动归类规则（导入时按 frontmatter 派生路径 + 文件名）

**文件名 = 版本无关逻辑ID**（NF 隔离类 `{nf}@{Type}@{local}.md`；跨 NF 类 `{Type}@{semantic}.md`）。

- **NF 隔离类**：从 3 段 id 取 `nf`/`local`，从 frontmatter `version` 取版本，路径 `{Layer}/{nf}/{version}/{id}.md`。
  - 例：id `UDG@MMLCommand@ADD URR` + version `20.15.2` → `Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md`
- **跨 NF 类（业务层 = 固有树结构 domain ⊃ scenario ⊃ solution，目录即树的层级）**：id 只有 2 段，路径从 frontmatter `domain`/`scenario` 取：
```
Business/
  {domain}/
    BusinessDomain@{domain}.md              ← 业务域对象（domain 层）
    {scenario}/
      NetworkScenario@{scenario}.md         ← 场景对象（scenario 层，该节点本身）
      ConfigurationSolution@{semantic}.md   ← 方案对象（solution 层 = scenario 的子节点，可多个）
```
  - BusinessDomain（只有 domain）：`Business/{domain}/BusinessDomain@{domain}.md`
  - NetworkScenario（domain+scenario）：`Business/{domain}/{scenario}/NetworkScenario@{scenario}.md`
  - ConfigurationSolution（domain+scenario）：`Business/{domain}/{scenario}/ConfigurationSolution@{semantic}.md`（semantic 即 id 末段；多个方案共处同一 scenario 目录，是该 scenario 的子节点）
  - **目录树只承载物理组织**（domain/scenario/solution 的包含层级）；对象间的**图谱关系**（NS↔CS、CS→task 等跨层引用）一律由 `## 边` wikilink 表达，与目录无关。
- **evidence 等非对象文件**：无 frontmatter `id` 的 md（证据、index 等）按原相对位置放到 `Evidence/...`，**不作为图谱对象索引**（仅作溯源引用目标，对应 frontmatter `source` 字段）。

### 5.5 导入流程

1. 上传 zip → 解包到临时区。
2. **先**扫描 bundle 内 `types/`（若有）合并进注册表，**再**逐个 md：解析 frontmatter；须有 `id`+`type`，且 `type` 在合并后的注册表。
3. 按 §5.4 规则**派生标准路径 + 文件名（=逻辑ID）**，归一化写入**统一资产库** `<data>/assets/`。与库中已有对象同 id 同版本（同路径）→ **后传覆盖先传 = 更新**，记 `updated`；新对象记 `added`；同 id 不同版本 → 新增一条版本记录（多版本共存）。同 bundle 内撞同路径（重复）→ 告警 + 后者覆盖。
4. 非 object md（无 id）→ 按 evidence 约定放置，不索引。
5. 追加写**上传记录**（append-only：时间、added/updated 计数、归类告警、悬空边）。
6. 增量/全量重建索引与版本聚合。
7. 失败策略：md 缺 `id`/`type` 或 `type` 未注册 → 该文件记入校验报告并跳过（不阻塞整包）；整包无任何有效对象 → 拒绝导入。

### 5.6 导出流程

1. 导出**统一资产库**（可选过滤：`?nf=&version=&domain=&scenario=` 切片；不传 = 全量）。
2. 把命中目录（已归一化的标准资产目录）打 zip 流式下载。
3. 无损：导出 = 目录快照，不改任何 md。
4. 导出的 zip 可被本平台再次导入还原（往返一致）。

---

## 6. 通用对象/边模型 + 解析器 — S2

### 6.1 Object（通用结构，不写死类型）

```
Object = {
  id:           str           # 版本无关逻辑ID（NF 3段 / 跨NF 2段）
  type:         str           # frontmatter type
  layer:        str           # 由 type 经注册表派生（Command/ConfigObject/.../Business）
  scope:        "nf" | "cross"
  nf:           str | None    # NF隔离类有
  version:      str | None    # 本实例版本（frontmatter version）；(id,version) 共同决定一个图谱节点
  versions:     [str]         # 该 id 的全部兄弟版本（多版本时>1）
  domain:       str | None    # 跨NF类有
  scenario:     str | None
  frontmatter:  dict          # 原始 YAML（除 id 外透传）
  body_md:      str           # 正文（去 frontmatter 与 ## 边 章节）
  raw_md:       str           # 原始全文（API /md）
  source_path:  str           # 资产库内归一化相对路径
}
```

### 6.2 Edge（不存储，动态解析）

```
Edge = { from: (id,version), relation: str, to: id }   # from=源节点(具体版本); to=版本无关id(展示时按§6.4解析到版本节点)
```

- **来源**：md 底部 `## 边` 章节，每行 `- {relation}: [[{to_id}]]`（command 规范约定）。
- 平台只**解析**已构建的 `## 边`（边的**派生**由上游"三层图谱构建规范"builder 完成，平台 v1 不重新派生）。
- `from` = 该 md 所属节点 `(id, version)`；`to_id` = 版本无关逻辑ID，展示/遍历时按 §6.4 解析到具体版本节点（默认目标网元最新 / 显式 `?version=`）。
- 可选解析插件：补充解析正文内联 markdown 链接等其它形式（v1 默认仅 `## 边`）。
- 去重：同 `(from, relation, to)` 多源命中保留一条。

### 6.3 对象类型注册表（数据驱动，可扩展）

平台内置默认注册表（对齐 command 规范对象类型），每类型声明：`layer`/`scope`/`id_segments`/`path_fields`/`frontmatter_required`/`edge_source`。

```yaml
object_types:
  MMLCommand:    { layer: Command,      scope: nf,    id_segments: 3, frontmatter_required: [id,type,name,nf,version,source,status], edge_source: "##边" }
  ConfigObject:  { layer: ConfigObject, scope: nf,    id_segments: 3, frontmatter_required: [id,type,name,nf,version,object_kind,source,status], edge_source: "##边" }
  Feature:       { layer: Feature,      scope: nf,    id_segments: 3, frontmatter_required: [id,type,nf,version], edge_source: "##边" }
  License:       { layer: License,      scope: nf,    id_segments: 3, frontmatter_required: [id,type,nf,version], edge_source: "##边" }
  Task:          { layer: Task,         scope: nf,    id_segments: 3, frontmatter_required: [id,type,nf,version], edge_source: "##边" }
  BusinessDomain:        { layer: Business, scope: cross, id_segments: 2, path_fields: [domain],          frontmatter_required: [id,type,domain],          edge_source: "##边" }
  NetworkScenario:       { layer: Business, scope: cross, id_segments: 2, path_fields: [domain,scenario],  frontmatter_required: [id,type,domain,scenario], edge_source: "##边" }
  ConfigurationSolution: { layer: Business, scope: cross, id_segments: 2, path_fields: [domain,scenario],  frontmatter_required: [id,type,domain,scenario], edge_source: "##边" }
```

- NF 隔离类路径由 id(取 nf) + frontmatter(version) 派生；跨 NF 类路径由 frontmatter `path_fields` 派生。
- **新增对象类型 = 注册表加一条**，不改码。

#### 6.3.1 扩展类型声明（bundle 携带，可选）

bundle 可在 `types/` 下带扩展类型，每类型一文件 `types/{TypeName}.yaml`，复用 §6.3 字段。导入时合并进注册表；同名 bundle 扩展覆盖默认 + 告警。

### 6.4 版本解析（默认/指定 — 填规范空白，重点）

command 规范要求"引用不带版本、解析时动态选版本"，但未定义选法。本平台按用户拍板：

- **图谱节点 = (id, version)，每版本一个独立节点**：展示时 `UDG@MMLCommand@ADD URR` 在 20.15.2 与 20.16.0 是**两个节点**。`versions[]` 记录该 id 全部兄弟版本。
- **默认版本 = 该 id 最新现存版本**（语义化点分段数值排序取最大；**无配置文件**）。常见情况下对象跟上网元最新版本，故≈"网元最新"；**若某 id 仅存于旧版本**（如命令未跟上新版本），默认落到其最新现存版本——**不把确实存在的对象判 404**。
- **引用（边）解析**：`## 边` 里的 `[[id]]`（不带版本）**默认指向目标 id 最新现存版本节点**；**显式版本切换**（API `?version=X` 或前端版本选择器）则指向 X 版本节点，X 不在 `versions[]` → 404 + 列出可用版本。
- **单对象查询**：`GET /objects/{id}` 不带版本 → 返回**该 id 最新现存版本**节点内容 + `versions[]`；带 `?version=X` → 该版本节点（不存在则 404）。
- **边与版本**：边存储为 `(from节点, relation, to_id版本无关)`；遍历时 `to_id` 按上述规则解析到具体版本节点。
- **跨版本天然成立**：业务层引用下层不带版本，默认连最新；不受版本绑死。

### 6.5 边 target 解析（极简）

`## 边` 里的 `[[{to_id}]]` 中 `to_id` 就是版本无关逻辑ID，**无需路径推断/文件名 sanitized 匹配**（采用 `## 边` wikilink 的好处）。命中即连；具体指向哪个版本节点由 §6.4 决定（默认最新 / 显式指定）；`to_id` 完全不存在 → 悬空边告警（不阻断）。

---

## 7. 存储与索引

### 7.1 目录布局（平台内部，遵循 command 规范）

```
<data>/assets/                       # 唯一统一资产库（多次上传累积合并）
  Command/{nf}/{version}/{nf}@MMLCommand@{local}.md        # NF隔离类
  ConfigObject/{nf}/{version}/{nf}@ConfigObject@{local}.md
  Feature/{nf}/{version}/{nf}@Feature@{local}.md
  License/{nf}/{version}/{nf}@License@{local}.md
  Task/{nf}/{version}/{nf}@Task@{local}.md
  Business/{domain}/BusinessDomain@{domain}.md
  Business/{domain}/{scenario}/NetworkScenario@{scenario}.md
  Business/{domain}/{scenario}/ConfigurationSolution@{semantic}.md
  Evidence/...                                              # 非对象（溯源）
  _imports.log                     # append-only 上传记录
  _index/                          # (可选) 解析索引缓存，可从 md 重建
```

- `<data>` 由配置指定（默认 `./platform-data/`，平台自管，与仓库 assets/ 无关）。
- **一份资产库**，多次上传按 §5.4 归类累积进同一目录树；层目录 PascalCase；NF 隔离类按版本分目录（同 id 多版本 = 多个版本目录下各一份）。

### 7.2 内存索引（启动/导入时全量或增量建）

- 遍历资产库所有 md → 解析为 Object（一个 md = 一个 (id,version) 节点）→ 按 id 聚合 `versions[]` → 解析 `## 边` → 产出 Edge 列表。
- 邻接表按**节点 (id,version)** 建：`out_edges[(id,version)] = [Edge]`、`in_edges[(id,version)] = [Edge]`（反链）；遍历时 `to_id` 按 §6.4 解析到版本节点。
- 索引结构：`nodes_by_(id,version)`、`latest_version_by_nf`（nf→最新版本）、`objects_by_type`、`out_edges`、`in_edges`。
- 统一资产库：单一索引；上传后增量或全量重建。
- 规模：单网元 ~4600 命令 + ~2200 配置对象，全库万级对象，内存索引可接受（参考 platform-next 实测）。

---

## 8. 读 API — S3

读端点全部 `GET`、只读；另含上传端点（`import`）。前缀 `/api/v1`。**无 `gid`**——平台只有一份统一资产库。`{id}` 为版本无关逻辑ID；`?version=` 可选（显式切换版本，否则用该网元**最新版本**，见 §6.4）。

| 端点 | 职责 | 关键参数/响应 |
|---|---|---|
| `POST /import` | 上传 bundle，合并进资产库 | multipart zip → `{added, updated, warnings[], counts}` |
| `GET /imports` | 上传记录（可选） | `[{time, added, updated, warnings_n}]` |
| `GET /export` | 导出资产库 | `?nf=&version=&domain=&scenario=`（可选过滤）→ 流式 zip |
| `GET /stats` | 统计 | `{object_counts_by_type, edge_count, nfs[], versions_per_nf}` |
| `GET /objects` | 列对象（按 id 聚合，含 versions[]） | `?type=&q=&nf=&domain=&page=&size=` → `[{id, type, nf|domain, versions, name}]` |
| `GET /objects/{id}` | **单对象**（不带版本=最新；`?version=`指定） | `?version=` → `{...Object, versions[], out_edges[]}` |
| `GET /objects/{id}/neighbors` | **单跳**（边的 to_id 按 §6.4 解析版本） | `?hops=1&version=` → `{center, out[], in[]}` |
| `GET /objects/{id}/md` | 原始 md（不带版本=最新；`?version=`指定） | `?version=` → `text/markdown`（`raw_md`） |
| `GET /subgraph` | N 跳子图 | `?center=&hops=&type=&version=` → `{nodes[], edges[]}` |

### 8.1 对象 id 编码（URL）

- 路径里 `{id}` 含 `@` 与可能的空格，须 URL-encode（`%40`、`%20`）。例：`/objects/UDG%40MMLCommand%40ADD%20URR`。
- 别名（更 URL 友好）：`?type=&nf=&local=`（NF 隔离类，3 段拆参）或 `?type=&domain=&scenario=&semantic=`（跨 NF 类）。

### 8.2 错误处理

- 对象不存在 → 404 + 提示最近匹配（可选）。
- 指定版本不存在（`?version=X` 但 X 不在该 id 的 `versions[]`）→ 404 + 列出可用版本。
- 导入校验失败 → 400 + 校验报告（缺字段/类型未注册的 md 清单）。

### 8.3 二期预留

- 写端点（`POST/PUT/DELETE /objects`）、版本管理端点、CR 端点——v1 不暴露，路由命名空间预留。

---

## 9. 前端（三栏只读浏览器 + 版本选择器）

### 9.1 布局

```
┌──────────┬───────────────────────┬─────────────────┐
│ 对象索引  │  对象 md（选中）        │ 节点图 (1跳)      │
│ 🔍搜索   │ ───────────────────── │    ●当前          │
│ ▾命令    │ # ADD URR              │   / | \          │
│ ▾配置对象 │ frontmatter...         │  ●   ●  ●邻居    │
│ ▾特性    │ 正文...                 │ 点邻居→跳转       │
│ ▾task    │ ## 边                   │ + 邻居清单        │
│ ▾业务对象 │ - 操作:[[..URR]]       │  • URR(配置对象)  │
└──────────┴───────────────────────┴─────────────────┘
 顶栏：导入/导出 + [版本选择器：UDG▼20.15.2  UNC▼20.15.2] + 统计
```

### 9.2 组件与交互

- **左栏 对象索引**：按 `type` 分组折叠树，每组显示计数；顶部搜索框（`/objects?q=` 子串匹配 id/name）。点击对象 → 中栏+右栏联动。
- **中栏 md**：渲染选中对象在**当前选定版本**的 `raw_md`（markdown-it + DOMPurify，复用 platform-next）。顶部 type/nf/version badge；若该 id 多版本，显示版本切换。
- **右栏 节点图**：vis-network 渲染单跳邻居（`/neighbors?hops=1`），中心=当前对象，邻居可点击 → 切换中心（联动中栏）。下方邻居清单列 relation + 目标。
- **顶栏**：导入/导出 + **版本选择器**（按 nf 显式切换版本，驱动 `?version=`；不选=用最新）+ 统计概览。
- URL 驱动：`/o/{id}?version=X` 可分享/刷新定位。

### 9.3 不做（v1）

- 在线编辑器、CR/diff 视图、版本历史 UI、命令三级漏斗/特性/任务/业务等 platform-next 项目特定 tab。

---

## 10. 二期预留扣子

| 二期能力 | 接入点 | 说明 |
|---|---|---|
| S4 写 API + 在线编辑 | 存储层之上 | 存储层本就读写文件；加 POST/PUT/DELETE 端点 + 前端编辑器；触发索引重建 |
| S5 版本管理 | 存储层实现可换 | 现纯文件目录；二期换 git/快照做历史/回滚/published 版本，上层不动 |
| S6 变更评审回路 | 存储层之上 | CR=一批提议文件改动 → diff → 专家对比视图 → approve(写回+重建索引)/reject；不依赖版本管理 |
| Agent 同步关联知识 | CR 提交侧（平台外） | 平台只承载 CR+diff+决策；Agent 平台外算好改动集再提交；与具体 LLM 解耦 |
| 多用户/鉴权 | API 层 | 路由/数据结构按可加鉴权设计 |

---

## 11. 技术栈

- **后端**：Python + FastAPI + uvicorn（复用 platform-next 模式：单例 service + 内存索引）。依赖：fastapi、uvicorn、pyyaml、python-multipart（上传）。无 DB。
- **前端**：Vue 3 + TypeScript + Vite + Element Plus + vis-network + markdown-it + DOMPurify（复用 platform-next 技术栈与组件风格，精简）。
- **部署**：单进程本地启动；前端构建产物由后端静态托管（同 platform-next）。

---

## 12. 测试策略

- **单元**：frontmatter 解析器、`## 边` wikilink 解析器、归类器（id+frontmatter → 路径+文件名=逻辑ID）、版本聚合（id → versions[]）、默认版本解析（id 最新现存）、类型注册表查找/扩展合并、邻接表/BFS。
- **集成**：读 API 端点（单对象/单跳/子图/列表/搜索/`?version=`）正确性；导入合并（同 id 更新/多版本共存）；导入校验失败路径；导出无损（导入→导出→再导入一致）。
- **端到端**：用样例 bundle（§13）导入 → 三栏前端浏览游走（含版本切换）→ 导出比对。
- **覆盖率目标**：核心解析/索引/API ≥ 80%。

---

## 13. 样例 bundle（验证用）

v1 需要一个真实样例验证。鉴于平台与 `assets/` 解耦，样例 bundle 作为**一次性测试夹具**：
- 用"三层图谱构建规范/command"的 builder 产出一个小 bundle（某网元命令 + 配置对象 + 若干特性 + 一个业务域/场景/方案，~50 对象），格式 = frontmatter(id/type/nf/version/...) + 正文 + `## 边` wikilink（**无 manifest**）。
- 仅用于开发/测试，不构成平台对任何项目的依赖。

---

## 14. 验收标准（v1）

1. 能导入符合 §5 格式的样例 bundle（md zip，无 manifest），归类正确，合并进统一资产库为标准目录。
2. `单对象` API 返回正确 frontmatter+正文+`## 边` 出向边；`单跳` API 返回正确邻居（含反链）。
3. **版本解析**：每 (id,version) 独立节点；不带版本时对象/边解析到该网元**最新版本**；`?version=` 显式切换生效；`versions[]` 正确列出。
4. 三栏前端：索引+搜索可用；点对象联动 md + 节点图；点邻居游走；版本选择器切换生效。
5. 导出后再导入，对象/边与原一致（无损往返）。
6. 导入非法 md（缺 id/type、未知类型）返回校验报告并跳过该文件，不阻塞整包。
7. 平台代码不含任何对具体业务（计费/带宽/SFCGraph 命名）的硬编码引用。

---

## 15. 开放问题 / 风险

| 项 | 说明 | v1 处置 |
|---|---|---|
| 版本解析 | 规范留白，已按用户拍板 | 节点=(id,version)每版本一节点；边默认指目标 id 最新现存版本；显式 `?version=`/选择器切换；默认版本=id 最新现存（≈网元最新，不 404 现存对象；无配置） |
| 样例 bundle 来源 | 用 command builder 产出 | 开发期制作为测试夹具 |
| 层目录大小写 | command 规范用 PascalCase（Command/...） | 平台沿用 PascalCase 层目录 |
| 多版本同 id 节点数 | 已定：每版本一节点 | v1：每 (id,version) 一个节点；边默认连目标最新版本 |
| 边的派生 vs 解析 | 边由上游 builder 派生进 `## 边`，平台只解析 | v1 平台不派生；若 bundle 无 `## 边` 则出向边为空 |
| 大图谱性能 | 万级对象全量解析 | 参考 platform-next 实测可接受 |
| 类型注册表扩展机制 | bundle 携带扩展类型合并/覆盖 | v1 简单合并 + 同名告警 |
| 平台代码仓库位置 | 建议新建顶层 `graph-asset-platform/` | plan 启动时确认 |
