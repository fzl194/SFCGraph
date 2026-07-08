# assets/ 维护准则（Typed LLM Wiki）

> 本文件是 assets/ 的 **CLAUDE.md**——指导 Agent 如何维护这个 typed wiki。
> 它让 Agent 成为"有纪律的 wiki 维护者"而非通用 chatbot。随实践共演化。
> 体系总方案：`../docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md`
> Schema 权威：`../改进后三层图谱定义.md`

---

## 1. 体系定位（一句话）

assets/ 是 **类型化的 LLM Wiki**：一个对象 = 一个 md，关系用 `[[wiki]]` 承载，页面类型按预定义 Schema 约束。它是**唯一对外暴露面**——源在 builder 目录不外泄，配置生成通过服务化取子集。

## 2. 三层架构（你工作在 wiki 层）

| 层 | 你能做 |
|---|---|
| **Raw Sources**（`output/`、`CommandGraph/data`、`FeatureGraph/data`、任意知识） | **只读**。读不改。 |
| **Wiki**（assets/，本目录） | **你拥有**：写 typed md、维护 `[[wiki]]`、维护 index/log。人审你的产出。 |
| **Schema**（`改进后三层图谱定义.md` + 本 CLAUDE.md） | 遵守。Schema 字段/关系的演进由人主导，你可提议。 |

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
1. **识别对象类型**：它对应 Schema 的哪些对象类型（命令/特性/业务域/方案/Task…）。
2. **凝练/投影成 md**：按该对象类型的 typed 模板（见 `schema/`）写一个 md。
   - 原料结构化（jsonl）→ **投影**（字段直接映射）
   - 原料非结构化（产品文档/任意知识）→ **按 Schema 凝练**对象与关系，标注 `source_evidence_ids` 回指原料
3. **维护交叉引用**：更新被本对象引用的、以及引用本对象的现有页的 `[[wiki]]`。
4. **更新 index.md**：本页加一行（链接 + 类型 + 一句话摘要）。
5. **追加 log.md**：`## [YYYY-MM-DD] ingest | <对象id>` + 动作摘要。
6. 多源触动：一个源可能更新 10-15 个页（如新增一条命令 → 更新引用它的 Task/特性页）。

### 4.2 Query（取子集 → 配置生成 → 回填）
- **先读 index.md 定位**相关页 → 按需取（或服务化打包子场景子集）。
- 配置生成中产出的**好综合**（方案对比、决策理由、踩坑、新发现的连接）→ **回填**为新页或更新现有页 → 更新 index/log。这是体系复利增长的关键，不要让好综合消失在对话里。

### 4.3 Lint（静态体检）
定期（或人触发）体检 assets/：
- **矛盾**：页面间相互冲突的声明
- **过时**：被新源推翻但未更新的旧声明
- **孤立页**：无任何入链的页
- **缺页**：被多处 `[[引用]]` 但无独立页的概念
- **缺交叉引用**：应当互链却没链的相关页
- **Schema 不合规**：typed 页缺字段/关系类型不对
- **数据缺口**：可用新原料填的空缺
→ 发现即触发 Compile 修复，记入 log。

---

## 5. typed md 通用约定（所有对象类型共有）

- **文件名 = 对象唯一 ID**（沿用现有编号：`BD-BSA-01` / `NS-CH-01` / `CS-CH-03` / `GWFD-010171` / 命令名 / `task-1-00003`）。
- **一个 md = 一个对象**：内聚该对象所有知识。
- **结构**：
  - `YAML front matter`：自身属性 + 路由维度（`id` / `type` / `name` / `status` + `nf`/`version` 或 `scenario`/`domain`）。**不放关系**。
  - `markdown 正文`：人读叙述 + 表格。
  - `[[wiki 链接]]`：承载所有关系，每种链接对应 Schema 一种关系类型。
- **共享 vs 独占**：
  - 被多对象引用的**共享对象**（ConfigObject、License）→ 独立 md，被 `[[wiki]]` 引用（DRY）。
  - 对象**独占的信息**（如命令的参数）→ 内聚进该对象 md。
- **每个对象类型的具体字段模板**：在 `schema/` 下该类型的模板文件定义，Compile 该层时落地。本准则只定通用原则。

## 6. 基建文件维护

- **index.md**：每次 Compile/Ingest **必须**更新。按类别分区，每页一行 `- [[id]] · 类型 — 一句话摘要`。Query 先读它。
- **log.md**：**append-only**，不删改历史。一致前缀 `## [YYYY-MM-DD] <ingest|query|lint> | <对象/操作>`，便于 `grep "^## \[" log.md`。

## 7. 边界（硬约束）

- **可写**：仅 `assets/`（typed md + index.md + log.md + 本 CLAUDE.md + `schema/` 模板）。
- **只读**：`output/`、`CommandGraph/data`、`FeatureGraph/data`、`ConfigTask/assert`、`business-graph`、`../改进后三层图谱定义.md`、`../docs/superpowers/specs/`。源不改、Schema 不擅改。
- 每次写前自检：路径在 `assets/` 下吗？
- 跨层/跨场景一致性：靠 `[[wiki]]` 串联 + Lint 查断链，不靠复制。

## 8. 状态约定
- typed 页 front matter 的 `status`：`draft`（刚 Compile，待人审）→ `active`（人审过）→ `stale`（Lint 标记需更新）。高层对象只引用 `active` 下层。
