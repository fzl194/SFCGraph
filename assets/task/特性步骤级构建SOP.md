# 特性/步骤级 Task Wiki 构建SOP（核心准则）

> 作用：指导 Agent 在 `assets/task/` 下**逐特性**构建 `feature(2-) → compound(1-) → atom(0-)` 三层 task wiki。
> 这是命令级 atom wiki（187+）之上的**特性级/步骤级**构建准则。
> 首个完整范本：**GWFD-110311**（`2-00001` + `1-00001~1-00008` + `0-00284~0-00289`）。
> 配套：`assets/CLAUDE.md`（总维护准则）、`assets/task/UDG/20.15.2/index.md`（compound 复用库 + 全景）。

---

## 0. 产物层级与定位

| 层 | 编号 | 回答的问题 | ref 指向 |
|---|---|---|---|
| **feature (2-)** | `2-00001~` | 这个特性**怎么配**（编排哪些步骤、9/多种场景如何选） | `Feature` |
| **compound (1-)** | `1-00001~` | 这个业务**步骤**怎么配（多命令组合，**可跨特性复用**） | `null` |
| **atom (0-)** | `0-00001~` | 这条**命令**怎么配（叶子） | `MMLCommand` |

关系链：`feature →(编排)→ compound →(含)→ atom →(ref)→ MMLCommand`

**硬约束：不跳层**——feature 不直连 atom，必须经 compound（除非单命令且无阶段语义，见 §2 注）。

---

## 1. 编号

- `assets/task/` **独立编号，不接 ConfigTask**（ConfigTask 的 compound/feature 是部分抽取资产，仅参考不复用）。
- feature `2-00001~`、compound `1-00001~` 按 assets/task 内顺序自增。
- atom 接续现有：atom 已有 `0-00001~0-00283`（不动），新增从 `0-00284~` 起。
- 文件：`assets/task/UDG/20.15.2/{编号}.md`。

---

## 2. 单特性构建流程（一次 pass）

**输入**：`feature_code` → `FeatureGraph/data/legacy/UDG_feature_files.csv` 映射 → 原始 md 清单（主源 = 「激活/部署」md，含数据规划表 + 任务示例脚本；辅源 = 概述/原理/调测）。

```
0. 收集资产
   - 原始 md 清单（CSV 按 feature_id 过滤）
   - 已有特性知识 md（业务图谱体系/{场景}/feature-knowledge/，仅参考）
   - 该特性涉及的已有 atom（扫 command，对 task-index）
1. 理解特性：核心对象模型 + 通用配置流程 + 多配置方法(场景)的差异维度
2. 补缺失 atom：特性用到但无 atom wiki 的命令 → 补建（读命令 wiki + 证据，编号接续）
3. 设计 compound 拆分（核心，见 §3 复用优先）：
   - 通用骨架 compound（所有场景共享）
   - 场景特化 compound（按场景挂）
   - 每个候选 compound 先查复用库（§3），能复用的引用不新建
4. 建 compound wiki（模板 §4）
5. 建 feature wiki：编排 compound + 特性级 DP 场景影响表（§5，必全）
6. 拷证据：激活方法 md → assets/evidence/UDG/20.15.2/（自包含，§6）
7. 双向链接回填（§6）：atom 回指 compound/feature；被复用 compound 的"被引用于"追加本 feature
8. 更新 index.md（compound 复用库 + feature/atom 段）
```

> **compound 粒度判断**：compound = "业务阶段"（多命令组合，或语义聚合如"前置准备"）。单命令且无阶段语义的（如孤立 SET）可直接在 feature 编排里挂 atom，不必强行建 compound。

---

## 3. compound 复用机制（★核心★）

compound 是**可跨特性复用的步骤**。后续特性的很多步骤（前置 License、过滤链、刷新生效、各种"三件套"）已在前面特性建过——**必须先查复用库，能复用的引用不新建**。

### 3.1 复用层级

| 层级 | 复用范围 | 示例（GWFD-110311 范本） |
|---|---|---|
| **全通用** | 跨一切特性 | License 前置、刷新生效（SET REFRESHSRV） |
| **域通用** | 业务域内多特性 | 过滤链（L7FILTER→FLOWFILTER→PROTBINDFLOWF）、BWM 控制器族、计费三件套 |
| **特性专属** | 单特性 | 切片绑定、时间段控制、分级带宽 |

### 3.2 复用判定（建 compound 前必查）

对每个候选步骤：
1. **扫 index.md 的 compound 复用库段**，按命令集签名找候选。
2. **双闸判定**（沿用 ConfigTask SKILL §7.1）：
   - 命令集 Jaccard ≥ 0.75 **且** 相位/用途同义 → **复用**（feature 编排链接已有 compound，不新建）
   - 0.4–0.75 或相位近义 → **reference**（新建，但共享子 atom）
   - < 0.4 或相位不同 → **新建**
3. 复用时：feature 编排链接已有 compound；**该 compound 关联节"被引用于"追加本 feature**（双向）。

### 3.3 compound 归属语义（重要）

- compound 关联节写 **"被引用于：[feature 集合]"**，**不是**"归属 feature"。
- 通用/域通用 compound 被**多 feature 引用是常态**；特性专属 compound 当前只被 1 feature 引用，后续若被复用则追加。
- > 范本注：GWFD-110311 现有 compound 多为 BWM 域通用/特性专属，当前"被引用于"= {2-00001}。后续带宽其他特性（020354/110313/020353/110312 等）构建时，`1-00002`/`1-00003` 会被复用引用，届时追加。

### 3.4 复用库（index.md compound 段）

每个 compound 条目含：`编号 · 名称 — cmd:命令集签名 | 用于:feature列表 | 层级`。建 feature 前先查此段。

---

## 4. wiki 模板

### atom（0-）— 命令级（已有范式，参考 `0-00033`）
- front matter：`id / type:Task / task_layer:atom / task_logical_name / ref→MMLCommand / task_intent / status`
- 正文：`# 标题` → `> 命令静态知识见 [ADD XXX](command/...)` → `## 配置方法(取值样例表+典型脚本+步骤位置)` → `## 决策点` → `## 约束` → `## 关联(命令wiki+上下游atom+被引用于compound/feature+证据)`

### compound（1-）— 步骤级
- front matter：`id / type:Task / task_layer:compound / task_logical_name / ref:null / task_intent / status`
- 正文：`# 标题` → `> 阶段定位 + 被引用于哪些 feature` → `## 配置方法(命令序列+取值样例+步骤位置)` → `## 决策点(阶段级DP+联动上层feature DP)` → `## 约束` → `## 关联(上下游compound+含atom+被引用于feature+证据)`

### feature（2-）— 特性级
- front matter：`id / type:Task / task_layer:feature / task_logical_name / ref→Feature / task_intent / status`
- 正文：`# 标题` → `> 引用特性 wiki` → `## 配置概览(对象链+场景骨架)` → `## 配置流程(compound 有序编排)` → `## 决策点(特性级DP场景影响表，§5必全)` → `## 约束(特性级rule)` → `## 关联(特性wiki+编排compound+证据)`

---

## 5. 决策点记录规范（硬约束）

- 多配置方法（场景）的差异**必须用 DP 组织**，**不建多套流程**。
- DP 每个 option 的影响**必须全记**——否则实际编排时不知该编哪条路径。
- 影响维度（按需列全）：控制层级 / 业务识别方式 / 规则类型 / 特化 compound / 是否需某命令 / 接入域类型 / 关键联动参数 / 是否刷新。
- **feature 用一张场景影响表**（范本：GWFD-110311 `2-00001` 的 9 场景表）。
- compound 内的 DP 记阶段级选择，并标注与上层 feature DP 的联动关系。

---

## 6. 硬约束（构建完整，非 MVP）

- **缺失命令的 atom 必须补建**（不空占位）；能复用已有 atom 就复用。
- **证据 md 拷进 `assets/evidence/`**（自包含，§7 可剥离）。
- **双向链接闭环**：atom ↔ compound ↔ feature，无断链。Grep 确认新文件无 `[[` 残留占位。
- **构建完整**：一个特性建到能端到端编排（所有 compound 建出，DP 影响全）。
- 引用规则（assets/CLAUDE.md §5.5）：已建 `[..](.md)` 带 .md；未建 `[[ID]]` 占位。

---

## 7. 验收清单（单特性 pass 完成自检）

- [ ] feature 1 个 + compound N 个（通用骨架 + 场景特化）+ 缺失 atom 补齐
- [ ] 特性级 DP 影响表完整（每 option 影响全记）
- [ ] compound 复用已查：该引用的引用，新建的入复用库（index 同步）
- [ ] 证据拷入 `assets/evidence/`
- [ ] 双向链接闭环（Grep 新文件无 `[[`；atom 回指 compound/feature）
- [ ] index.md 同步（feature/compound 复用库/atom 段 + 被引用于更新）

---

## 8. 待铺开范围

首批四场景 UDG 特性去重 **38 个**（计费 9 / 带宽 16 / 访问限制 12 / APN 14）。GWFD-110311 是带宽首个范本。同法铺其余——**每建一个特性，优先复用已有 compound，逐步沉淀全通用/域通用 compound 库**。

> 构建中如发现本 SOP 有缺陷，挖审查意见 → 修正本文件 → 版本号 +1。准则稳定判据：连续 2 个新特性 pass 人工免改或仅微调。
