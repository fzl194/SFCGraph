# 业务层构建 SOP 设计（业务域/场景/方案）

> 日期：2026-07-10
> 状态：设计稿（待 spec 评审 + 人审）
> 作用：在 `assets/` 内构建**业务层 typed wiki**——业务域(BD)→场景(NS)→方案(CS) 三类对象 + 配套构建 SOP + 审视流程。
> 镜像：`assets/task/特性步骤级构建SOP.md`（特性层 SOP）+ `assets/task/特性task_wiki审视流程.md`（特性审视）。
> 范围：仅业务层对象（BD/NS/CS）。feature/compound/atom task（`2-`/`1-`/`0-`）已在 `assets/task/{nf}/{ver}/` 建好，本 SOP 在其之上构建业务层编排。

---

## 0. 背景与动机

特性层 task wiki（feature `2-` → compound `1-` → atom `0-`）已逐步建好（UDG 22 feature / UNC 7 feature）。特性层回答"**单个特性怎么配**"。但真实业务场景是**多网元、多特性协同**（如计费 = UDG 用户面 URR 执行 + UNC 控制面 SMF/CHF 对接），需要一层**业务对象**来编排特性、沉淀跨网元协同知识与配置级决策/约束。

现有 `业务图谱体系/` 下已有一版计费/带宽三层图谱，但有三个问题：
1. **只读且编号废弃**：`业务图谱体系/` 是 assets/ 外的只读参考，其中 CS/DP/BR 用旧编号（`CS-CH-01`/`DP-CH-01`），已由 `assets/CLAUDE.md` §5.4 废弃，改 §5.2 两段式。
2. **揉在一个文件**：`01-business-graph.md` 把 BD/NS/CS/DP/BR/SO/Scope/Participant 全塞一个文件，违反 §6「一个 md = 一个对象」。
3. **写死字段填表**：CS 用强制定义的表格字段（solution_id/design_intent/core_mechanism_combo/scopes/participants/uses_semantic_object/constrained_by/has_decision）去填，是"字段填表"而非"知识沉淀"。

本设计**不沿用旧三层图谱的写死字段**，改为**镜像特性 task 的叙述式知识骨架**：表达清"对象是啥 / 配置里有啥决策点 / 怎么配 / 约束 / 向下引用哪些 task"，模板跨对象一致，知识够用即可。

---

## 1. 产物层级与定位（镜像特性 SOP §0）

| 层 | 对象类型 | 回答的问题 | ref / 引用 |
|---|---|---|---|
| 业务域 **BD** | BusinessDomain | 这个业务域是干啥的（含哪些场景） | null（根） |
| 场景 **NS** | NetworkScenario | 这个场景解决什么业务问题（边界/判断依据/产出） | 含于 BD |
| 方案 **CS** | ConfigurationSolution | 这个方案**怎么配**（编排哪些特性/步骤/命令 task、跨网元协同、配置级 DP/约束） | 含于 NS + **向下引用** feature `2-`/compound `1-`/atom `0-` |

**关系链**：`BD →(contains)→ NS →(instantiated_as)→ CS →(引用)→ feature task 2- → compound 1- → atom 0-`

**纯树结构**：BD/NS/CS 是包含树；CS 是叶子，向下引用 task wiki（跨网元 UDG+UNC 的 feature/compound/atom task，仍在 `task/`）。

**关键决策：不建 `3-` solution task 对象类型。** CS 本身就是方案对象（ConfigurationSolution 类型），承载"是什么"+"怎么配"，不拆"静态 CS + 方案级 task"。`3-`/`4-` task 前缀（§5.1 预留）本层不用——业务层对象是 BD/NS/CS（§5.2 两段式 ID），不是 Task 类型。

**编排原则（镜像特性 SOP §0 编排原则）**：CS 编排若干"步骤"——多特性的可复用步骤模块 → 引用已有 compound `1-`；单命令 → 直接引用 atom `0-`；方案特有的额外步骤（跨网元协同的、不属于任何特性的命令）→ 单命令建新 atom `0-`、多命令可复用建新 compound `1-`（建进 `task/`，CS 引用）。即 **CS 可直接含 atom，compound 仅为"可复用多命令模块"而建，不是 CS→atom 的必经层**。

---

## 2. 编号与目录

- BD/NS/CS 用 `assets/CLAUDE.md` §5.2 **两段式 ID**（不带 nf@version，业务层横跨 UDG+UNC）：
  - `BusinessDomain@business-awareness`
  - `NetworkScenario@charging`
  - `ConfigurationSolution@charging-converged`（语义 slug，见 §4 命名）
- 目录（§5.5）：`assets/business/<domain>/<scenario>/`，**一个 md = 一个对象**（§6）：
  - `assets/business/business-awareness/BusinessDomain@business-awareness.md`
  - `assets/business/business-awareness/charging/NetworkScenario@charging.md`
  - `assets/business/business-awareness/charging/ConfigurationSolution@charging-converged.md`（每个方案一个 md）
- **业务层不进 `task/`**：`task/{nf}/{ver}/` 仍只放网元内 feature/compound/atom；CS 引用它们时用 assets 根路径（跨网元全路径，§5.5），如 `[在线计费](task/UDG/20.15.2/2-00004.md)`、`[计费三件套](task/UDG/20.15.2/1-00010.md)`、`[费率标识链](task/UNC/20.15.2/1-00009.md)`。
- **业务层 index**：`assets/business/index.md`（业务层全景）。格式镜像 `assets/task/{nf}/{ver}/index.md` 风格，分三段：`## 业务域（BD）` / `## 场景（NS，按域分组）` / `## 方案（CS，按场景分组）`，每行 `- [对象名](assets根路径.md) · 一句话摘要`。

---

## 3. 单方案构建流程（一次 pass，镜像特性 SOP §2）

```
0. 收集资产
   - 已有业务图谱参考（业务图谱体系/{场景}/，只读）→ CS/DP/BR 知识草稿来源（非拷贝，参考重写）
   - 原始产品文档 md（业务专题/方案文档）→ ★主源
   - 方案涉及的 feature task（查 assets/task/{nf}/{ver}/index.md）
1. ★前置门（critical）：核对方案涉及的 feature task 2- 是否全建完（UDG + UNC 两侧）
   - 全建完 → 继续
   - 有缺口 → 先补建 feature task（按特性 SOP），或该 CS 降级待建；不带着断链占位硬建
2. 理解方案：解决什么业务问题 + 跨哪些网元/特性协同 + 核心机制 + 配置级决策维度
   ★ 主源 = 原始产品文档方案/业务专题章节（非凝练版图谱 md）
3. 设计 CS 编排：编排哪些 feature task + 可复用 compound + 单命令 atom + 方案特有额外步骤
   - 每个候选 compound 先查 task 复用库（assets/task/{nf}/{ver}/index.md compound 段）
   - 额外步骤：单命令→新 atom 0-（进 task/，编号按 _numbering.json）；多命令可复用→新 compound 1-（进 task/，入复用库）
4. 建 CS wiki（模板 §4）：叙述式知识沉淀 + 向下引用 task
5. 拷证据：方案/业务专题 md → assets/evidence/business/{场景}/（自包含，§7）
6. 双向链接回填：被引用的 feature task / compound 的"被引用于"小节追加本 CS
7. 更新 assets/business/index.md（业务层全景）+ task 侧 index.md（"被引用于"）
```

---

## 4. wiki 模板（★叙述式，镜像 feature task，非字段填表）

### 4.1 统一骨架（BD/NS/CS 共用，按对象填相关段，知识够用即可）

```markdown
---
id: {两段式ID}
type: {BusinessDomain|NetworkScenario|ConfigurationSolution}
name: {对象名}
domain: {业务域slug}            # BD 自身无 domain；NS/CS 填所属域
scenario: {场景slug}            # NS 自身填；CS 填所属场景；BD 无
status: draft
source_evidence_ids: [EV-...]
---

# {对象名}
> {一句话定位}。{BD/NS: 包含哪些 NS/CS；CS: 属于哪个 NS，编排哪些 task}。

## 概览
{对象是什么 + 解决什么问题 + 边界(覆盖/不覆盖)}。
{CS 额外：跨网元/多特性协同骨架——UDG 用户面干啥、UNC 控制面干啥}。1-2 段叙述。

## 配置与协同                         ← 镜像 feature task「配置流程」
- CS：方案怎么配——编排哪些 feature task 2- + 可复用 compound 1- + 单命令 atom 0- + 方案特有额外步骤；
       跨网元协同顺序(UDG 用户面 vs UNC 控制面)。每步"干啥 + 引用哪个 task"，人不点链接就懂。
       格式：1. **{步骤名}**（{一句话干啥}）：`{命令提示}` → [{task-id}](链接)
- BD/NS：本层不含直接配置，列 contains 的 NS/CS 即可（可略此段或写"本层为容器"）。

## 决策点                             ← 镜像 feature DP 表 | 选项/场景 | 影响 |
- CS 为主（如计费方式/计量方式/配额耗尽动作选择 → 影响：选哪些 feature task / 走哪个 compound / 跨网元路径 / 关键参数）。
- NS 可记场景级选择（如计费方式→选哪个 CS）。

## 约束                               ← bullet: - **{规则名}**({severity}): {约束} — {后果}
- CS 为主（跨网元一致性约束、License 前置、时序）；severity 用 critical/warning/info。
- BD/NS 可略。

## 关联
- 上游：{BD/NS 包含关系}
- 下游：{CS 引用的 feature task / compound / atom，带命令提示}
- 证据：{evidence 链接}
```

### 4.2 三条模板准则（用户拍板）

1. **模板一致性 = 同一套叙述骨架，不是写死字段填表。** BD/NS 轻（概览+关联为主），CS 最全（向下引用 task）。各段按对象相关度填写，非每段必填。
2. **旧三层图谱的有价值概念融入叙述，不复活写死字段表格。** 跨网元 participants（UDG 用户面/UNC 控制面角色）、核心机制 mechanism、语义对象——写进「概览」「配置与协同」的散文，**不**用 scopes/participants/uses_semantic_object/constrained_by 等表格字段。
3. **CS「配置与协同」段是表达"怎么配"的方式**：镜像 feature task 的「配置流程」，每步"干啥 + 引用哪个 task"（含方案特有额外步骤）。不另设 solution task 对象。

### 4.3 命名（语义 slug）

- BD：`{domain-slug}`（如 `business-awareness` 业务感知）
- NS：`{scenario-slug}`（如 `charging` 计费）
- CS：`{scenario}-{solution-slug}`（如 `charging-converged` 计费-融合、`charging-online` 计费-在线、`charging-offline` 计费-离线、`charging-content` 计费-内容、`charging-metering` 计费-计量增强、`charging-quota-exhaust` 计费-配额降速、`charging-fallback` 计费-兜底）

---

## 5. 复用机制（镜像特性 SOP §3）

- **CS 复用下层 task**（feature `2-`/compound `1-`/atom `0-`）= 业务层复用核心。建 CS 前先查 `assets/task/{nf}/{ver}/index.md` 的 compound 复用库段。
- **复用判定**（沿用特性 SOP §3.2）：方案某步所需命令集，已有 compound 覆盖（命令集 Jaccard≥0.75 且相位同义）→ 复用引用；0.4–0.75 → reference（共享子 atom）；<0.4 → 新建。
- **方案特有额外步骤**（跨网元协同的、不属于任何特性的命令）：
  - 单命令 → 新 atom `0-`（进 `task/{nf}/{ver}/`，编号按 `_numbering.json`，补建流程同特性 SOP §2 步骤 2）
  - 多命令可复用 → 新 compound `1-`（进 `task/{nf}/{ver}/`，入复用库 index.md）
- **复用差异双向回填**（防假通用，镜像特性 SOP §3.5）：CS 引入的下层 task 差异（参数变种/专属命令/协同约束），若该 task「场景差异」未记，须回填到该 task，不能只写进 CS。判定：CS 有的核心差异维度，被复用 task 场景差异是否有对应条目？无 → 假通用（须补 task）。

---

## 6. 决策点记录规范（镜像特性 SOP §5）

- 多方案/多配置方法的差异**用 DP 组织**，不建多套流程。
- CS 的 DP 每个 option 的影响**必须全记**——否则配置生成不知编哪条路径。影响维度（按需）：选哪些 feature task / 走哪个 compound / 跨网元路径（UDG only / UNC only / 双侧协同）/ 是否需某命令 / 关键联动参数 / 是否刷新。
- NS 的 DP 记场景级选择（如计费方式→选哪个 CS）。
- DP 表统一格式 `| 选项/场景 | 影响（参数/命令/联动） |`。

---

## 7. 硬约束（镜像特性 SOP §6）

- **前置门（critical）**：CS 涉及的 feature task `2-`（UDG + UNC 两侧）必须先全建完，才能开建 CS。有缺口 → 先补建或降级待建，不带着断链占位硬建。"建完"= 结构完整、内容齐全、无 `[[占位]]`（**结构口径**）；front matter `status` 升 `active` 是单独的人审步骤，可后置，不影响 CS 开建（**不要求**被引用 feature task 已是 active）。
- **额外步骤进 task（critical）**：方案特有的命令不空写在 CS 叙述里——单命令建 atom `0-`、多命令建 compound `1-`，进 `task/`，CS 引用。CS「配置与协同」里每个命令/参数要可追溯到 task 或证据。
- **叙述式非字段填表（critical）**：不沿用旧三层图谱写死字段（scopes/participants/uses_semantic_object/constrained_by/has_decision 表格）。用 §4 叙述骨架。
- **证据自包含**：方案/业务专题 md 拷进 `assets/evidence/business/{场景}/`（CLAUDE.md §7 可剥离）。evidence 文件命名沿用现有惯例（`{描述名}_{原始文档ID}.md`，如 `融合计费方案_93400212.md`）；front matter `source_evidence_ids` 用 `EV-BIZ-{场景slug}-{NN}`（如 `EV-BIZ-charging-01`），与现有 EV- 前缀族对齐。证据同时在「关联」段以 markdown 链接列出（镜像 feature task 关联段）。
- **双向链接闭环**：CS ↔ 被引用的 feature task/compound（task 侧"被引用于"追加本 CS）。Grep 新文件无 `[[` 残留占位、无断链。
- **跨网元引用全路径**：CS 引用 UDG/UNC task 用 assets 根路径（§5.5）。
- **引用规则**（§5.5）：已建 `[..](.md)` 带 .md；未建 `[[ID]]` 占位（但前置门要求 feature task 已建，故 CS 不应有 feature task 占位）。
- **主源是原始产品文档**：方案知识以原始产品文档「业务专题/方案」章节为准，非凝练版图谱 md（后者仅参考）。

---

## 8. 验收清单（单 CS pass 完成自检，镜像特性 SOP §7）

- [ ] CS 1 md（两段式 ID，`assets/business/<domain>/<scenario>/` 下）
- [ ] 前置门通过：涉及 feature task（UDG+UNC）全建完
- [ ] CS 向下引用 feature/compound/atom task 全有效（无断链、无 feature task 占位）
- [ ] 方案特有额外步骤已建 atom/compound 进 task（非空写在 CS 叙述）
- [ ] CS 决策点影响表完整、约束 severity 标注
- [ ] 证据拷入 `assets/evidence/business/{场景}/`
- [ ] 双向链接闭环（被引用 task 的"被引用于"追加本 CS）
- [ ] `assets/business/index.md` 同步 + task 侧 index.md "被引用于" 同步
- [ ] 叙述式（无旧三层图谱写死字段表格）

---

## 9. 范本：计费场景（前置门已通过 ★）

### 9.1 前置门审查结果（2026-07-10 实查磁盘，非信进度表）

> `_features-to-build.md` 严重过时（写"UNC 0/13"，实际 UNC 已建 7 feature/16 compound/209 atom）。以下为磁盘实查。

**UDG 计费相关 9 特性：全齐 ✓**
| feature | task |
|---|---|
| GWFD-020301 内容计费 | 2-00003 |
| GWFD-020300 在线计费 | 2-00004 |
| GWFD-010171 离线计费 | 2-00005 |
| GWFD-010173 融合计费 | 2-00006 |
| GWFD-020302 时长计费 | 2-00007 |
| GWFD-020303 流量计费 | 2-00008 |
| GWFD-020306 事件计费 | 2-00009 |
| GWFD-020351 PCC基本功能 | 2-00018 |
| GWFD-110101 SA-Basic | 2-00019 |

**UNC 计费相关 5 特性：全齐 ✓**
| feature | task |
|---|---|
| WSFD-011201 离线计费 | 2-00001 |
| WSFD-011202 热计费 | 2-00002 |
| WSFD-011206 融合计费 | 2-00003 |
| WSFD-109002 内容计费 | 2-00004 |
| WSFD-109101 PCC基本功能 | 2-00005 |

### 9.2 范本范围（7 CS，全部零占位可建）

参考现有 `业务图谱体系/计费场景/three-layer-graph/01-business-graph.md` 的 7 CS 划分（用叙述式重写，不拷旧字段）：

| CS | 名称 | UDG task | UNC task |
|---|---|---|---|
| CS-1 | 离线计费 | 2-00005, 2-00003 | 2-00001 |
| CS-2 | 在线计费 | 2-00004, 2-00003, 2-00009 | — |
| CS-3 | 融合计费 | 2-00006, 2-00003 | 2-00003 |
| CS-4 | 内容计费基础 | 2-00019, 2-00003, 2-00018 | 2-00005, 2-00004 |
| CS-5 | 计量形态增强 | 2-00003, 2-00007, 2-00008, 2-00009 | — |
| CS-6 | 配额降速与体验切换 | 2-00004, 2-00006 | 2-00003 |
| CS-7 | 兜底默认计费 | 2-00003, 2-00018 | — |

加 BD（业务感知）+ NS（计费）= 范本共 9 个对象。

### 9.3 族内构建顺序（镜像特性 SOP §8 经验）

**先建最复杂的 CS-3 融合计费**（跨网元 UDG+UNC、双 URR、CHF 协同最全），把跨网元协同知识 + 复用 compound 的场景差异一次沉淀到位；再建简单 CS（纯参数变种）复用即可。避免先建简单 CS（单视角）导致协同知识欠债。

### 9.4 每批后自审

每完成一批 CS，按 §10 审视流程 R1 执行，critical 即修，经验回填本 SOP。

---

## 10. 配套审视流程（镜像 特性task_wiki审视流程.md）

> 目的：对已建 CS wiki 做独立批判性审视，补构建者自检盲区。核心关切：**task 覆盖度**、**复用是否抹平差异**、**跨网元协同是否完整**。每完成一族/一批 CS 后执行。

### R1 核心审视维度（必做）

- **R1.1 task 覆盖度**（防遗漏）：方案应编排的 feature/步骤/命令 task 是否都引用了？方案特有的额外步骤是否都建了 atom/compound（非空写在 CS 叙述里）？复用 compound 时，打开该 compound 确认命令集真包含方案这步所需。
- **R1.2 复用合理性**（防一刀切）：CS 引用的 compound 是否真覆盖方案这步所需全部命令？跨网元协同差异（参数变种/专属命令/协同约束）是否回填到下层 task 场景差异（防假通用，§5）？有无假复用（命令集重合<0.75 却强行复用）？
- **R1.3 跨网元协同完整性**（业务层特有）：CS 是否表达清 UDG 用户面 + UNC 控制面的协同（顺序/一致性约束/CP-UP 参数对齐）？有无只写一侧漏另一侧？
- **R1.4 前置门**：CS 涉及的 feature task 是否真建完（非 `[[占位]]`）？
- **R1.5 证据链**：CS「配置与协同」的命令/参数可追溯到 task 或 evidence；方案级 DP/约束的叙述性知识标 evidence 出处。无证据结论须穷尽搜索（原始文档/特性 wiki/官方差异表/软件参数文档/命令 wiki 全文）后再判 critical（镜像特性审视警示）。

### R2 辅助维度

- R2.1 命令完整性：方案涉及命令是否都有 atom？
- R2.2 DP 影响表：每 option 影响全记？跨网元路径维度有？
- R2.3 双向链接：CS ↔ task 闭环；无 `[[占位]]` 残留；无断链。

### R3 严重度

- **critical**：前置门未过 / task 覆盖遗漏 / 假复用致命令丢失 / 跨网元一致性约束未记 → 必须修
- **warning**：差异未进场景差异 / DP 影响不全 / 协同一侧漏写 → 应修
- **info**：措辞/链接/格式 → 可选

---

## 11. 待铺开范围

- **首批范本**：计费场景（前置门已过，§9）。BD 业务感知 + NS 计费 + 7 CS。
- **后续**：带宽控制场景（UDG 已建 BWM 2-00001 + PCC 2-00018 + SA 2-00019；其余带宽 feature 待补齐后建）、访问限制场景（UDG 已建 URL过滤 2-00002 + 头增强族 2-00010~13 + 重定向族 2-00014~17；UNC 访问限制 feature 待补）。
- 同法铺其余——**每建一个 CS，优先复用已有 compound，逐步沉淀跨域通用协同知识**。

> 构建中如发现本 SOP 有缺陷，挖审查意见 → 修正本文件 → 版本号 +1。准则稳定判据：连续 2 个新 CS pass 人工免改或仅微调。

---

## 12. 落地产物清单（实现阶段产出）

1. `assets/task/业务层级构建SOP.md`（本 SOP 落地，镜像特性 SOP 结构）
2. `assets/task/业务层级wiki审视流程.md`（§10 落地）
3. `assets/business/index.md`（业务层全景）
4. `assets/business/business-awareness/BusinessDomain@business-awareness.md`（BD）
5. `assets/business/business-awareness/charging/NetworkScenario@charging.md`（NS）
6. `assets/business/business-awareness/charging/ConfigurationSolution@charging-*.md`（7 CS，先建融合）
7. 证据拷入 `assets/evidence/business/charging/`
8. 双向链接回填到 `assets/task/{UDG,UNC}/20.15.2/index.md` 的"被引用于"
9. `assets/CLAUDE.md` 补业务层目录约定（如需）

---

## 13. 与现有体系的关系

- **`业务图谱体系/`**（只读参考）：提供 CS/DP/BR 知识草稿 + 7 CS 划分参考。不拷其旧编号、不拷其写死字段。主源仍是原始产品文档。
- **`assets/task/`**（特性层，已有）：CS 向下引用的 feature/compound/atom task 所在。CS 不改动 task 内容，只在"被引用于"追加反向链接。
- **`assets/CLAUDE.md`**（总准则）：§5.2 两段式 ID、§5.5 引用路径、§6 一对象一 md、§7 自包含、§9 边界——全部遵守。
- **ConfigTask**（只读）：跨域通用 compound 划分对齐 ConfigTask backbone（特性 SOP §3.6），本层复用时沿用。
