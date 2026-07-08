# assets/ 维护准则（Typed LLM Wiki）

> 本文件是 assets/ 的 **CLAUDE.md**——指导 Agent 如何维护这个 typed wiki。
> 它让 Agent 成为"有纪律的 wiki 维护者"而非通用 chatbot。随实践共演化。
> 体系总方案：`../docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md`
> Schema 定义（自包含拷贝）：`schema/三层图谱定义.md`（开发期权威源在仓库根 `../改进后三层图谱定义.md`，变更后重新拷贝同步）

---

## 1. 体系定位（一句话）

assets/ 是 **类型化的 LLM Wiki**：一个对象 = 一个 md，关系用 `[[wiki]]` 承载，页面类型按预定义 Schema 约束。它是**自包含、可剥离、唯一对外暴露**的知识面——源在 builder 目录不外泄，配置生成通过服务化取子集。

## 2. 三层架构（你工作在 wiki 层）

| 层 | 你能做 |
|---|---|
| **Raw Sources**（`../output/`、`../CommandGraph/data`、`../FeatureGraph/data`、任意知识） | **只读**。读不改。开发期源，**不进 assets 运行时引用**。 |
| **Wiki**（assets/，本目录） | **你拥有**：写 typed md、维护 `[[wiki]]`、维护 index/log。人审你的产出。 |
| **Schema**（`schema/三层图谱定义.md` + 本 CLAUDE.md） | 遵守。Schema 字段/关系演进由人主导，你可提议。 |

## 3. 你与人的分工

| 角色 | 职责 |
|---|---|
| **你（Agent）** | Compile/Ingest（读原料→凝练/投影→写 typed md）、维护交叉引用、Lint 体检、Query 检索、回填好综合、维护 index/log |
| **人** | sourcing（喂原料/指出文档）、问对问题、**review 你的产出**、纠正/引导、Schema 演进 |

> **你写，人审。不要等人写。** 人的负担是"审 + 喂原料"，不是"写图谱"。

---

## 4. 三操作

### 4.1 Compile / Ingest（raw → typed md）
输入一个 raw source（产品文档 / jsonl 条目 / 任意知识），步骤：
1. **识别对象类型**：对应 Schema 的哪些对象类型。
2. **凝练/投影成 md**：按该对象类型模板写一个 md。
   - 原料结构化（jsonl）→ **投影**（字段映射）
   - 原料非结构化（产品文档/任意知识）→ **按 Schema 凝练**对象与关系
3. **证据内联/拷贝**（§7 可剥离）：证据原文进 assets/，`source_evidence_ids` 指向 assets/ 内拷贝，不指外部。
4. **维护交叉引用**：更新被本对象引用的、以及引用本对象的现有页的 `[[wiki]]`。
5. **更新 index.md** + **追加 log.md**（`## [日期] ingest | <对象id>`）。
6. 一个源可能触动 10-15 个页。

### 4.2 Query（取子集 → 配置生成 → 回填）
- 先读 index.md 定位 → 按需取（或服务化打包子场景子集）。
- 配置生成中的**好综合**（方案对比、决策理由、踩坑、新连接）→ **回填**为新页或更新现有页 → 更新 index/log。不让好综合消失在对话里。

### 4.3 Lint（静态体检）
定期查：矛盾 / 过时声明 / 孤立页（无入链）/ 缺页（被引无独立页）/ 缺交叉引用 / Schema 不合规 / 数据缺口 / Schema 拷贝与源不同步 → 触发 Compile 修复，记 log。

---

## 5. ID 与文件名规范（统一编码，wiki 链接依据）

### 5.1 绑产品对象 → 四段式 `{nf}@{version}@{ObjectType}@{local_id}`
| 对象 | local_id | 示例 |
|---|---|---|
| MMLCommand | 命令全名 | `UDG@20.15.2@MMLCommand@ADD URR` |
| CommandParameter | `<命令>:<参数>` | `UDG@20.15.2@CommandParameter@ADD URR:URRNAME` |
| ConfigObject | 对象名 | `UDG@20.15.2@ConfigObject@URR` |
| Feature | feature_code | `UDG@20.15.2@Feature@GWFD-020301` |
| License | license_code | `UDG@20.15.2@License@LKV6SFVCPU01` |
| Task | `<层前缀>-<5位流水>`（atom `0-`/compound `1-`/feature `2-`/solution `3-`/generalized `4-`） | `UDG@20.15.2@Task@1-00003` |
| 任务级 DecisionPoint / TaskRule | `0-<5位流水>`（按类型独立流水） | `UDG@20.15.2@DecisionPoint@0-00001` |

### 5.2 跨产品对象（业务层 BD/NS/CS）→ 两段式 `{ObjectType}@{语义slug}`
业务层横跨 UDG+UNC，**不带 nf@version**。local 用英文语义 slug（业务层有天然名，同命令用命令名、特性用 feature_code 的惯例）。
| 对象 | 示例 |
|---|---|
| BusinessDomain | `BusinessDomain@business-awareness` |
| NetworkScenario | `NetworkScenario@charging` |
| ConfigurationSolution | `ConfigurationSolution@charging-converged` |

### 5.3 内嵌对象（不单独建 md，不单独 ID）
- 业务级 DecisionPoint：内嵌在 NS/CS md，用 md 内标题 + 锚点引用（`[[NetworkScenario@charging#计费方式选择]]`）。
- TaskRule、任务级 DecisionPoint：内嵌在 Task md。

### 5.4 废弃编号
旧业务编号（`BD-BSA-01` / `NS-CH-01` / `CS-CH-03` / `DP-CH-xx`）**全部废弃**，改用 §5.2 两段式。

### 5.5 文件名与引用路径
- 文件名用 local_id 段（sanitized：空格/特殊字符转 `-`），目录承载 nf@version/type 段：
  - `command/UDG/20.15.2/ADD-URR.md` ← `UDG@20.15.2@MMLCommand@ADD URR`
  - `configobject/UDG/20.15.2/URR.md` ← `UDG@20.15.2@ConfigObject@URR`
  - 业务层（无 nf@version）：`business/<domain>/<scenario>/ConfigurationSolution@charging-converged.md`
- **引用统一用 assets/ 根路径**（从 assets/ 起，**禁文件间相对路径**如 `../`），同证据 `evidence/...`：
  - **已建对象** → 标准 markdown 链接 `[显示名](assets根路径.md)`，**带 .md**：`[URR](configobject/UDG/20.15.2/URR.md)`、`[ADD URR](command/UDG/20.15.2/ADD-URR.md)`
  - **未建对象** → `[[对象ID]]` 占位（**双方括号 = 待建**）：`[0-00001](task/UDG/20.15.2/0-00001.md)`
  - 规则：**`[...](...md)` = 已建可点；`[[...]]` = 占位待建**。Compile/Lint 把已建对象的 `[[ID]]` 占位替换为 markdown 链接。

### 5.6 关系双向链接（硬约束）
每条关系必须在两端 md 互引（正向 + 反向）：
- 命令 `operates_on` ConfigObject → 命令引 ConfigObject，**ConfigObject 反引命令**（"操作本对象的命令组"）。
- Feature `requires_license` → Feature 引 License，License 反引 Feature。
- 方案 `uses_feature`/`uses_task` → 方案引，特性/任务反引。
- ConfigObject `object_refers_to` → 双向。
反向链接由 Compile（建对象 md 时补全）+ Lint（查缺失反向链接）维护。

---

## 6. typed md 通用约定（所有对象共有）

- 一个 md = 一个对象，内聚该对象所有知识。
- 结构：`YAML front matter`（自身属性 + 路由维度：`id`/`type`/`name`/`status` + `nf`/`version` 或 `scenario`/`domain`）+ `markdown 正文`（人读叙述 + 表格）+ `[[wiki 链接]]`（承载 Schema 关系）。
- 关系全用 `[[wiki]]`，不放 front matter。每种链接对应 Schema 一种关系类型（业务层：contains/instantiated_as/uses_feature/uses_task；特性层：requires_license/depends_on；命令层：operates_on/has_parameter；任务层：precedes/contains/ref）。
- 共享对象（ConfigObject、License）独立 md 被 wiki 引用；独占信息（命令参数）内聚。
- 各对象类型的具体字段模板：`schema/` 下定义，Compile 该层时落地。

## 7. 自包含 / 可剥离（硬约束）

assets/ 必须**可整个剥离单独交付/部署**。因此：
- **不依赖外部路径**：所有运行时引用的内容必须在 assets/ 内。
- **证据/原料拷贝**：typed md 的 `source_evidence_ids` 只指 assets/ 内拷贝（证据原文进 `evidence/` 或内联 md"证据"章节），不指 `../output/` 等外部。
- **Schema/SOP 拷贝**：`schema/三层图谱定义.md` 是自包含拷贝；`skill/` 在 P5 切换时拷入 SOP + knowledge。
- **wiki 链接闭环**：所有 `[[wiki]]` 指向 assets/ 内 md，不断链外部。
- 开发期源（`../output/`、`../CommandGraph/data` 等）是 Compile 的**读入方**，不进 assets 运行时。

## 8. 基建文件维护

- **index.md**：每次 Compile/Ingest **必须**更新。按类别分区，每页一行 `- [[id]] · 类型 — 一句话摘要`。
- **log.md**：**append-only**。`## [YYYY-MM-DD] <ingest|query|lint> | <对象/操作>` 前缀便于 grep。

## 9. 边界（硬约束）

- **可写**：仅 `assets/`（typed md + index.md + log.md + 本 CLAUDE.md + `schema/`/`evidence/` 拷贝）。
- **只读**：`../output/`、`../CommandGraph/data`、`../FeatureGraph/data`、`../ConfigTask/assert`、`../business-graph`、`../改进后三层图谱定义.md`、`../docs/superpowers/specs/`。
- 每次写前自检：路径在 `assets/` 下吗？源不改、Schema 不擅改。
- 跨层/跨场景一致性：靠 `[[wiki]]` 串联 + Lint 查断链，不靠复制。

## 10. 状态约定
typed 页 front matter 的 `status`：`draft`（刚 Compile，待人审）→ `active`（人审过）→ `stale`（Lint 标记需更新）。高层对象只引用 `active` 下层。
