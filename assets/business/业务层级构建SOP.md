# 业务层 Wiki 构建 SOP（核心准则）

> 作用：指导 Agent 在 `assets/business/` 下构建**业务域(BD)→场景(NS)→方案(CS)** 三类业务层 typed wiki。
> 这是特性层 task wiki（feature `2-`/compound `1-`/atom `0-`，在 `assets/task/{nf}/{ver}/`）之上的**业务层编排**准则。
> 镜像：`assets/task/特性步骤级构建SOP.md`（特性层 SOP）。配套：`assets/business/业务层级wiki审视流程.md`（审视 R1）。
> 首个完整范本：**计费场景**（BD 业务感知 + NS 计费 + 7 CS，先建 CS-3 融合）。
> 设计依据：`docs/superpowers/specs/2026-07-10-business-layer-sop-design.md`（已基线）。

---

## 0. 产物层级与定位

| 层 | 对象类型 | 回答的问题 | ref / 引用 |
|---|---|---|---|
| 业务域 **BD** | BusinessDomain | 这个业务域是干啥的（含哪些场景） | null（根） |
| 场景 **NS** | NetworkScenario | 这个场景解决什么业务问题（边界/判断依据/产出） | 含于 BD |
| 方案 **CS** | ConfigurationSolution | 这个方案**怎么配**（编排哪些特性/步骤/命令 task、跨网元协同、配置级 DP/约束） | 含于 NS + **向下引用** feature `2-`/compound `1-`/atom `0-` |

关系链：`BD →(contains)→ NS →(instantiated_as)→ CS →(引用)→ feature task 2- → compound 1- → atom 0-`

**纯树结构**：BD/NS/CS 是包含树；CS 是叶子，向下引用 task wiki（跨网元 UDG+UNC 的 feature/compound/atom task，仍在 `assets/task/`）。

**不建 `3-` solution task 对象**：CS 本身（ConfigurationSolution 类型）就是方案对象，承载"是什么"+"怎么配"。业务层只有 BD/NS/CS 三类。

**编排原则（镜像特性 SOP §0）**：CS 编排若干"步骤"——多特性的可复用步骤模块 → 引用已有 compound `1-`；单命令 → 直接引用 atom `0-`；方案特有的额外步骤（跨网元协同的、不属于任何特性的命令）→ 单命令建新 atom `0-`、多命令可复用建新 compound `1-`（建进 `task/`，CS 引用）。即 **CS 可直接含 atom，compound 仅为"可复用多命令模块"而建，不是 CS→atom 的必经层**。

---

## 1. 编号与目录（遵守 CLAUDE.md §5.2/§5.5）

- BD/NS/CS 用**两段式 ID**（不带 nf@version，业务层横跨 UDG+UNC）：
  - `BusinessDomain@business-awareness`
  - `NetworkScenario@charging`
  - `ConfigurationSolution@charging-converged`（语义 slug，见 §4 命名）
- 目录：`assets/business/<domain>/<scenario>/`，**一个 md = 一个对象**（CLAUDE.md §6）：
  - `assets/business/business-awareness/BusinessDomain@business-awareness.md`
  - `assets/business/business-awareness/charging/NetworkScenario@charging.md`
  - `assets/business/business-awareness/charging/ConfigurationSolution@charging-converged.md`
- **业务层不进 `task/`**：`task/{nf}/{ver}/` 只放网元内 feature/compound/atom；CS 引用它们用 assets 根路径（跨网元全路径，§5.5），如 `[在线计费](task/UDG/20.15.2/2-00004.md)`、`[费率标识链](task/UNC/20.15.2/1-00009.md)`。
- **业务层 index**：`assets/business/index.md`（全景，分 BD/NS/CS 三段）。

---

## 2. 单方案构建流程（一次 pass，镜像特性 SOP §2）

```
0. 收集资产
   - 已有业务图谱参考（业务图谱体系/{场景}/，只读）→ CS/DP/BR 知识草稿来源（参考重写，非拷贝）
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
5. 拷证据：方案/业务专题 md → assets/evidence/business/{场景}/（自包含）
6. 双向链接回填：被引用的 feature task / compound 的 `## 关联` → `- 被引用于:` 行追加本 CS（per-task-md，非 index.md）
7. 更新 assets/business/index.md（标 done）+ task 侧 per-task-md 被引用于（主流程做，非并行 Agent）
```

---

## 3. 复用机制（镜像特性 SOP §3）

- **CS 复用下层 task**（feature `2-`/compound `1-`/atom `0-`）= 业务层复用核心。建 CS 前先查 `assets/task/{nf}/{ver}/index.md` 的 compound 复用库段。
- **复用判定**（沿用特性 SOP §3.2）：方案某步所需命令集，已有 compound 覆盖（命令集 Jaccard≥0.75 且相位同义）→ 复用引用；0.4–0.75 → reference（共享子 atom）；<0.4 → 新建。
- **方案特有额外步骤**（跨网元协同的、不属于任何特性的命令）：
  - 单命令 → 新 atom `0-`（进 `task/{nf}/{ver}/`，编号按 `_numbering.json`，补建流程同特性 SOP §2 步骤 2）
  - 多命令可复用 → 新 compound `1-`（进 `task/{nf}/{ver}/`，入复用库 index.md）
- **复用差异双向回填（硬约束，防假通用）**：CS 引入的下层 task 差异（参数变种/专属命令/协同约束），若该 task「场景差异」未记，须回填到该 task，不能只写进 CS。判定：CS 有的核心差异维度，被复用 task 场景差异是否有对应条目？无 → 假通用（须补 task）。

---

## 4. wiki 模板（★叙述式，镜像 feature task，非字段填表）

### 4.1 设计原则（风格一致 + 结构按层级差异化）

- **风格一致**：三层都是叙述式知识沉淀（人能看懂、好审查），**不**用旧三层图谱的写死字段表格（scopes/participants/uses_semantic_object/constrained_by 等）。
- **配置流程只在 CS，决策点/约束不限层**：BD/NS 太抽象、不涉及具体配置——**不设**「配置与协同」（配置流程）段，只有 CS 才进配置层；但「决策点」「约束」**可在 BD/NS/CS 任意层**——决策与约束不限于某个对象层级，哪里有就记哪里（NS 记场景级决策如选哪个 CS、CS 记配置级决策如走哪个 compound）。各层段填该层相关知识，知识够用即可，非每段必填。
- **旧三层图谱的有价值概念融入叙述**：跨网元 participants（UDG 用户面/UNC 控制面角色）、核心机制 mechanism、语义对象——写进相关层散文，不复活表格字段。
- **特性优先（CS 配置编排核心 ★）**：CS「配置与协同」以**特性为中心**——方案第一关注用了哪些特性。对每特性说明其**标准配置方法**（摘要自 feature task）+ 本方案**用法（走标准 / 变种）**。引用优先级：**feature task (2-) 为主 > compound (1-) 次之 > atom (0-) 末之**。compound/atom 仅在「标准配置方法摘要」+「变种点」出现，**不重复罗列 feature task 内部步骤**（那些已在 feature task 里）。
- **特性关系语义（★防"都得配"误解）**：CS 编排多个特性时，**禁止平铺成"编排特性"清单**——必须先给「**特性关系矩阵**」明确每特性的**角色 + 必配性 + 关系**，回答"哪些必配 / 哪些可选 / 谁包含谁 / 谁正交"。多特性常是以下关系之一（追溯原始产品文档「与其他特性的交互」段 + feature task 依赖声明判定）：
  - **核心**：方案主体（如"在线计费 CS"的在线计费特性）——必配。
  - **基础/依赖前提**：核心特性依赖的底层能力（如 SA-Basic 是业务识别前提；内容计费是费率三件套结构基础）——必配，但配置常与核心**重叠**（配核心时基础结构已含，不需额外配一遍）。
  - **维度增强**：正交维度的可选叠加（如计费模式"在线/离线/融合"三选一；计量方式"流量/时长/事件"可选——两个维度正交）——按业务诉求选配。
  - **跨网元对端**：同一能力在另一网元的对应特性（如 UDG 计费 + UNC 计费）——组合关系，两侧同配。
  - **二选一/触发链**：互斥路径（如配额降速的"在线触发链 OR 融合触发链"）——按上层场景选其一。
  > **配置重叠判定**：若两特性的配置对象集高度重合（如内容计费与在线/离线/融合都改 URR 费率三件套），则配核心特性时基础结构已隐含——矩阵「关系」列必须注明"重叠，配 X 时已含，不需额外配 Y"。

### 4.2 三层模板（差异化）

**共同 front matter**（三层一致，仅路由字段）：

```yaml
---
id: {两段式ID}
type: {BusinessDomain|NetworkScenario|ConfigurationSolution}
name: {对象名}
domain: {业务域slug}       # BD 自身无；NS/CS 填所属域
scenario: {场景slug}       # NS 自身填；CS 填所属场景；BD 无
status: draft
---
```

**类型-字段必填对照**（防字段漏填，便于 `_GROUP_FIELDS` 取到 `domain` 进 categories 分组 / 左树按 domain 渲染）：

| 类型 | `id` | `type` | `name` | `domain` | `scenario` | `status` |
|---|---|---|---|---|---|---|
| **BD** | 必填 | 必填 | 必填 | **必填**（自身域 slug） | — | 必填 |
| **NS** | 必填 | 必填 | 必填 | **必填**（所属 BD slug） | **必填**（自身场景 slug） | 必填 |
| **CS** | 必填 | 必填 | 必填 | **必填**（所属 BD slug） | **必填**（所属场景 slug） | 必填 |

> **R1 校验**：建完后 `grep` 校验——BD 必须有 `domain:` 行，NS 必须有 `domain:` + `scenario:` 行，CS 必须有 `domain:` + `scenario:` 行（slug 与 id 第二段一致）。漏填阻塞后续 categories 分组 / 左树渲染。

**BD 模板（业务域·定义层，最抽象，不涉及配置）**

```markdown
# {业务域名}
> {一句话定义}。含 {N} 个场景。

## 概览
{业务域是干啥的——定义/价值/核心能力}。1-2 段。

## 范围与边界
- 含场景：{NS 链接列表}
- 不属于本域：{相邻域区分}

## 决策点（可选，罕见）
{域级决策，若有}

## 约束（可选）
{域级约束，若有}

## 关联
- 下游场景：{NS 链接}
- 证据
```

**NS 模板（场景·问题/边界层，不涉及具体配置）**

```markdown
# {场景名}
> {一句话：解决什么业务问题}。属于 {BD}。含 {N} 个方案。

## 概览
{场景定义 + 判断依据（什么业务需求触发本场景）+ 典型产出}。1-2 段。

## 边界
- 覆盖：{网元/接口/控制维度}
- 不覆盖：{相邻场景区分（如计费 vs 带宽控制 vs 访问限制）}

## 决策点                             ← 场景级决策（如选哪个 CS）
{场景级决策——什么业务诉求选哪个 CS、场景级方案路由}
| 选项/场景 | 影响 |

## 约束（可选）
{场景级约束，若有}

## 关联
- 上游域：{BD}
- 下游方案：{CS 链接列表}
- 证据
```

**CS 模板（方案·配置层 ★，向下引用 task）**

```markdown
# {方案名}
> {一句话：这个方案怎么配}。属于 {NS}。编排 {feature/compound} task。

## 概览
{方案是什么 + 用了哪些特性（跨网元 UDG+UNC）+ 协同骨架}。1-2 段。

## 配置与协同                         ← 特性优先：仅详述本方案的特性级变种/排除 + 跨特性协同
本方案编排 {N} 个特性：{feature task 链接}。

**特性关系矩阵**（★必填——回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档「与其他特性的交互」段 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| {feature-task} | 核心 / 基础(依赖前提) / 维度增强 / 跨网元对端 / 二选一 | 必配 / 可选(条件) | {与核心的重叠/正交/组合/包含关系；配置是否重叠，配 X 时是否已含 Y} |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task，使用者直接按 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### {网元} 侧：{特性名}（[{feature-task-id}](task/{nf}/{ver}/{id}.md)）
走标准配置方法（见 feature task）。若有**变种/排除**（方案独有）：详述差异点（参数/命令/组装）+ 原因，引到 compound 场景差异；标准里有但本方案不用的命令注明排除 + 原因。无变种则一句"走标准配置方法，无特性级变种"。

### 跨网元/跨特性协同
{特性间协同顺序 + 一致性约束 + 参数对齐 —— 方案独有，详述}

## 决策点                             ← 配置级 DP | 选项/场景 | 影响 |
{如计费方式/计量方式/配额耗尽动作 → 影响：选哪些 feature task / 走哪个 compound / 跨网元路径 / 关键参数}
| 选项/场景 | 影响（参数/命令/联动） |

## 约束                               ← bullet: - **{规则名}**({severity}): {约束} — {后果}
{跨网元一致性约束、License 前置、时序}；severity 用 critical/warning/info。

## 关联
- 上游场景：{NS}
- 编排特性（feature task，优先）：{2-xxxxx 链接}
- 复用步骤/命令（compound/atom，按需）：{1-/0- 链接}
- 证据：{evidence 链接}
```

> **CS「配置与协同」段是表达"怎么配"的方式**：**特性优先**——以特性为单元，但**不重复描述 feature task 的标准配置**（使用者直接按 feature task）；CS 仅详述本方案的**特性级变种/排除项** + **跨特性协同**（方案独有部分）。compound/atom 仅在变种点引用。不另设 solution task 对象。

### 4.3 命名（语义 slug）

- BD：`{domain-slug}`（如 `business-awareness` 业务感知）
- NS：`{scenario-slug}`（如 `charging` 计费）
- CS：`{scenario}-{solution-slug}`（如 `charging-converged` 融合、`charging-online` 在线、`charging-offline` 离线、`charging-content` 内容、`charging-metering` 计量增强、`charging-quota-exhaust` 配额降速、`charging-fallback` 兜底）

---

## 5. 决策点记录规范（硬约束）

- 决策点（DP）**可在 BD/NS/CS 任意层**——决策不限于某个对象层级，哪里有决策哪里记。
- DP 每个 option 的影响**必须全记**——否则配置生成不知编哪条路径。统一表格式 `| 选项/场景 | 影响 |`，影响内容按层不同：
  - **NS**：场景级决策（如计费方式→选哪个 CS、场景级方案路由）。
  - **CS**：配置级决策（选哪些 feature task / 走哪个 compound / 跨网元路径 UDG only / UNC only / 双侧协同 / 关键联动参数 / 是否刷新）。
  - **BD**：罕见（域级决策，若有则记）。
- 多方案/多配置方法的差异**用 DP 组织**，不建多套流程。
- **配置流程（「配置与协同」段）仍只在 CS**——具体配置流程沉淀在方案里更清晰。

---

## 6. 硬约束（构建完整，非 MVP）

- **前置门（critical）**：CS 涉及的 feature task `2-`（UDG + UNC 两侧）必须先全建完，才能开建 CS。有缺口 → 先补建或降级待建，不带着断链占位硬建。"建完"= 结构完整、内容齐全、无 `[[占位]]`（结构口径）；`status` 升 `active` 是单独的人审步骤，可后置。
- **额外步骤进 task（critical）**：方案特有的命令不空写在 CS 叙述里——单命令建 atom `0-`、多命令建 compound `1-`，进 `task/`，CS 引用。CS「配置与协同」里每个命令/参数要可追溯到 task 或证据。
- **叙述式非字段填表（critical）**：不沿用旧三层图谱写死字段（scopes/participants/uses_semantic_object/constrained_by/has_decision 表格）。用 §4 叙述骨架。
- **证据自包含**：方案/业务专题 md 拷进 `assets/evidence/business/{场景}/`（CLAUDE.md §7 可剥离）。evidence 文件命名 `{描述名}_{原始文档ID}.md`。证据**在「关联」段以 markdown 链接列出**（镜像 feature task，**不设 front matter source_evidence_ids**，避免与关联冗余）。
- **双向链接闭环**：CS ↔ 被引用的 feature task/compound（**per-task-md** 的 `## 关联` → `- 被引用于:` 追加本 CS，不是 index.md）。Grep 新文件无 `[[` 残留占位、无断链。
- **跨网元引用全路径**：CS 引用 UDG/UNC task 用 assets 根路径（§5.5）。
- **引用规则**（§5.5）：已建 `[..](.md)` 带 .md；未建 `[[ID]]` 占位（但前置门要求 feature task 已建，故 CS 不应有 feature task 占位）。
- **主源是原始产品文档**：方案知识以原始产品文档「业务专题/方案」章节为准，非凝练版图谱 md（后者仅参考）。

---

## 7. 验收清单（单 CS pass 完成自检）

- [ ] CS 1 md（两段式 ID，`assets/business/<domain>/<scenario>/` 下）
- [ ] 前置门通过：涉及 feature task（UDG+UNC）全建完
- [ ] CS 向下引用 feature/compound/atom task 全有效（无断链、无 feature task 占位）
- [ ] 方案特有额外步骤已建 atom/compound 进 task（非空写在 CS 叙述）
- [ ] CS 决策点影响表完整、约束 severity 标注
- [ ] 证据拷入 `assets/evidence/business/{场景}/`
- [ ] 双向链接闭环（被引用 task 的 per-task-md"被引用于"追加本 CS）
- [ ] `assets/business/index.md` 同步（标 done）
- [ ] 叙述式（无旧三层图谱写死字段表格）

---

## 8. 待铺开范围 + 族内顺序

- **首批范本**：计费场景（前置门已过：UDG 9/9 + UNC 5/5 实查磁盘）。BD 业务感知 + NS 计费 + 7 CS。
- **后续**：带宽控制场景（UDG BWM/PCC/SA 已建，其余带宽 feature 待补齐后建）、访问限制场景（UDG URL过滤+头增强+重定向族已建；UNC 访问限制 feature 待补）。
- 同法铺其余——**每建一个 CS，优先复用已有 compound，逐步沉淀跨域通用协同知识**。

> **族内构建顺序（经验，镜像特性 SOP §8）**：同族多 CS（如计费族 7 CS）构建时，**先建差异最全的最复杂 CS**（计费族=CS-3 融合计费，跨网元 UDG+UNC、双 URR、CHF 协同最全），把跨网元协同知识 + 复用 compound 场景差异一次沉淀到位；再建简单 CS（纯参数变种）复用即可。避免先建简单 CS（单视角）导致协同知识欠债、后续不断回头补。
>
> **每批后自审**：每完成一族（或一批）CS，按 `assets/business/业务层级wiki审视流程.md` R1 审视（task 覆盖度/复用合理性/跨网元协同完整性/前置门/证据链），critical 即修，经验回填本 SOP。

> 构建中如发现本 SOP 有缺陷，挖审查意见 → 修正本文件 → 版本号 +1。准则稳定判据：连续 2 个新 CS pass 人工免改或仅微调。
