# MVP-方案-任务图谱设计（递归式三层图谱重构）

> 日期：2026-07-03
> 状态：设计草案（待 spec 审查 + 用户复核）
> 范围：计费场景三层图谱的解耦重构，以及一套可扩展到任意场景/图谱的通用构建流程
> 相关：`三层图谱Schema-最终版-v0.1.md`、`FeatureGraph/特性层对象与关系定义.md`、`CommandGraph/COMMAND_GRAPH_SCHEMA.md`、`ConfigTask/task-build-skill/SKILL.md`

---

## 1. 背景与问题

当前三层图谱（以计费场景为样本）存在三类结构性问题：

1. **每层对象与关系只用 md 描述，缺结构化资产**。`业务图谱体系/计费场景/three-layer-graph/*.md` 是纯 markdown，机器不可读、不可推理、不可跨场景复用。
2. **底部三层已有 canonical 结构化资产，但场景 md 把它们又重抽了一遍**，造成两套并行世界：
   - `FeatureGraph/data/{NF}/{ver}/*.jsonl`（Feature/SubFeature/License + 层内边）
   - `CommandGraph/data/assets/{NF}/{ver}/*.jsonl`（MMLCommand/ConfigObject/CommandParameter + 层内边）
   - `ConfigTask/task-assets/{NF}/{ver}/`（Task/Rule/DecisionPoint，已建 UDG）
   - 场景 md 又把这些对象及其关系重新手写一遍。
3. **跨层关系"无家可归"**。`uses_feature` / `decomposes_to` / `FeatureTaskOrderEdge` / `FeatureRule` / `CommandRule` 等只在场景 md 里，canonical 里没有这些对象类型或边。

### 1.1 关系覆盖现状（扫描结论）

**已承载（canonical 里有边/字段）：**
- 特性层：`depends_on` / `conflicts_with`（feature_relations.jsonl）、`requires_license`、`has_subfeature`（parent_feature_code 字段）
- 命令层：`has_parameter` / `operates_on` / `refers_to` / `parameter_references` / `conditional_required`（5 个 edge jsonl）
- 任务层：`invokes Command`（task.ref）、`targets Parameter`（parameter_bindings）、`param→DP`（decision_ref）；TaskRule/DecisionPoint 独立对象

**未承载（只在场景 md 或未建）：**
- 业务层全部（BD/NS/CS/DP/BR/SO + 关联边）
- 跨层组合边（CS→Feature、CS→Task、Feature→Task）
- 编排边（FeatureTaskOrderEdge、TaskCommandOrderEdge）
- 规则对象（FeatureRule、CommandRule——canonical 无此对象类型）
- 决策影响边（DP selects / sets_value_pattern）、跨层精化（refined_by）

## 2. 核心设计原则

1. **MVP 永远 = 单个方案（solution）**。不管构建什么图谱、输入是什么，工作单元始终是一个方案。规模靠"加方案"线性扩展，不靠重设计本体。
2. **动态层对象类型压到最少**：只有 `Task` 一种主对象，`Rule` 与 `DecisionPoint` 挂其上。静态层（Feature / Command / ConfigObject / CommandParameter）保持独立对象类型不变。
3. **结构高度一致、可嵌套迭代**：task 内含子 task，层层拆到底；任何层级遵守同一套拆解 SOP。
4. **递归**：一个特性就是一个小方案，同一套 SOP 适用。
5. **Feature / Command 独立构建**为静态字典，task 层只通过 ID 引用。
6. **跨层连接全走 task 组合**，不建跨层静态边（Feature→Command 不直连）。

## 3. 对象模型

### 3.1 动态层（最小）

| 对象 | 关键字段 | 说明 |
|---|---|---|
| **Task** | `task_id`, `task_layer`(solution/feature/generalized/compound/atom), `task_logical_name`, `task_intent`, `status`, `source_evidence_ids`, `feature_ref?`, `command_ref?`, `nf`, `version` | 统一节点；`task_layer` 已是 ConfigTask 现有字段，仅扩 `solution` 值 |
| **Rule** | `rule_id`, `task_ref`, `rule_type`, `rule_logic`, `severity` | 挂 Task |
| **DecisionPoint** | `dp_id`, `task_ref`, `question`, `options`, `impact_scope` | 挂 Task；`impact_scope` = 该 DP 触及的后代范围 |
| **Task 组合边** | `from_task`, `to_task`, `relation`(推理得出，非冻结枚举), `condition_ref?`(DP) | Task 间 |

### 3.2 静态层（独立、不变）

- `FeatureGraph` — Feature / SubFeature / License + 层内静态边
- `CommandGraph` — MMLCommand / ConfigObject / CommandParameter + 层内静态边

### 3.3 `task_layer` 取值映射

| 现有值 | 含义 | 本设计角色 |
|---|---|---|
| `atom` | 原子，单命令 | command-task（叶子，复用已建） |
| `compound` | 多命令组合 | step-task |
| `feature` | 特性级 | feature-task（"小方案"，递归） |
| `generalized` | 跨特性通用 | 通用 task |
| `solution`（新增） | 方案级 | solution-task（闭包） |

## 4. 拆解优先级链（cascade）

给定任意 task（方案或子 task）往下拆，按顺序判定子节点粒度：

```
1. 能映射到某个已有 Feature？      → 子 = feature-task（feature_ref → FeatureGraph ID）
2. 否则，是几条专属命令的组合？     → 子 = step-task（task_layer=compound，再递归）
3. 否则，就一条命令？              → 子 = command-task（command_ref → CommandGraph ID，原子叶）
```

- 叶子永远是 command-task（已独立建好，复用）。
- 命中 1 时，feature-task 继续往下拆（递归，"特性是小方案"）。
- 命中 2 时，step-task 的子通常是一组 command-task。

## 5. DecisionPoint 放置与作用域

- **放置原则**：DP 尽量往下挂——挂在能覆盖其全部变体的**最深** task 上。
- **作用域**：DP 的影响范围 = 该 task 及其向下能触及的**全部后代**（选子 task、定参数值模式、开关分支）。
- 这保证 DP 局部化、不污染无关分支，又能在必要处统一裁决。

## 6. task 间边的推理（不冻结枚举）

- task↔task 的关系类型（composes / sequential / fallback / must_be_last / branch...）**不预设固定枚举**。
- 边的语义在拆解时**从源材料推理得出**（激活文档/方案定义里"先 A 再 B"、"若 X 则 A"、"A 兜底"等表述）。
- 推理结果记录在边的 `relation` 字段；相同语义自然收敛，不做强约束。

## 7. 文件夹与归属

| 资产 | 位置 | 性质 |
|---|---|---|
| Feature 静态字典 | `FeatureGraph/data/{NF}/{ver}/` | canonical，不变 |
| Command 静态字典 | `CommandGraph/data/assets/{NF}/{ver}/` | canonical，不变 |
| **command-task / step-task / feature-task / generalized-task** | `ConfigTask/task-assets/{NF}/{ver}/` | **canonical，跨场景复用** |
| **solution-task（方案闭包）** | `业务图谱体系/{场景}/closures/` | **场景专属**，组合 canonical task |
| BD / NS 静态对象 | `业务图谱体系/{场景}/business/` | 场景专属，人+Agent 定 |
| md 残留 | `业务图谱体系/{场景}/docs/` | 图承载不了的叙述/原文 |

> 跨场景复用底层三层；场景只 own "BD/NS + solution-task 闭包 + md"。

## 8. 构建流程（可扩展 SOP）

```
Phase A  业务顶层（人+Agent，一次性，每场景）
  输入: 领域知识  →  输出: BD/NS + 每个 CS 的「MVP 方案定义」
  方案定义 = id/name/intent/scope/participants/design_intent + 非正式能力/命令预期

Phase B  方案拆解（每 CS 独立，可并行）
  输入: 一个 MVP 方案定义
  循环: 对当前 task 跑 §4 cascade → 产出子 task + Rule + DP（§5 放置）+ 边（§6 推理）
  终止: 全部叶子命中 command-task
  输出: 该方案的 solution-task 子树（闭包）

Phase C  Feature 双轨并行
  轨1: FeatureGraph 静态字段抽取（产品级，已基本完成，与本期解耦）
  轨2: feature-task 动态构建（本期重点）
        输入 = 该 Feature 的「激活文档」（每种配置方式 = 一个 feature-solution）
        跑同一套 Phase B SOP；多个配置方式可合并为一个 feature-task + DP（人工评估）
  同步点: 轨2 用 feature_ref 指向轨1 已存在的 Feature

Phase D  command-task（已独立建好，UDG 基本完成，复用）
```

### 8.1 递归一致性

- 顶层方案（CS）、feature-task、step-task 都用 Phase B 的 cascade。
- 输入契约统一：一个"方案定义"（顶层=CS定义；feature级=激活文档）。
- 终止统一：叶子全是 command-task。

## 9. 方案合并

- 两个 solution-task 发现结构大量重叠时，**合并 = 产出一个新 solution-task + DP 承载原两方案的差异**。
- 合并需人参与评估（不自动合并）。
- 合并后原两方案可退化为新方案在 DP 不同选项下的两个实例。

## 10. md 残留规则

图无法承载的 → md，挂场景 `docs/`。典型：
- 方案 design_intent 叙述、端到端走查
- 证据原文、特性激活文档原文
- 方案合并评估记录、审查报告
- 领域背景、术语

判定线：**能表达为"节点 + 属性 + 边"的进图；只能叙述/推理/原文的进 md。**

## 11. 对计费场景的迁移含义（方向，非实施步骤）

1. **保留**：FeatureGraph / CommandGraph / ConfigTask 的 command-task 资产不动。
2. **新建（本期）**：feature-task / step-task / solution-task 子树，从现有 `three-layer-graph/*.md` + 特性激活文档抽。
3. **改造**：原 `three-layer-graph/01-business-graph.md` 的 CS → solution-task；DP/BR/SO → 收进 solution-task 的 DP/Rule，少量进 md。
4. **退役**：`three-layer-graph/02~05*.md` 里手写的 feature/command/task 重复内容，迁入结构化资产后降为只读视图或废弃。
5. **保留 md**：`docs/` 承载 design_intent、端到端走查、证据。

## 12. 范围与非目标

**本期范围：**
- 稳定构建动态 Task 层（feature-task / step-task / solution-task）的 SOP 与对象约定。
- 计费场景作为首个落地样本。

**非目标（本期不做）：**
- 改 FeatureGraph / CommandGraph 的静态字典结构。
- 自动化方案合并（人工评估）。
- 把所有 md 内容一次性迁完（按方案 MVP 增量推进）。
- 图数据库落地（先 jsonl，图 DB 是后续演进）。

## 13. 待定 / 未来

- 边的推理具体规则集（Phase B 执行细则，留给实施 plan）。
- `generalized` task 在 cascade 中的确切位置（是否作为第 1.5 优先级："能复用通用 task？→ 用它"）。
- 多场景方案合并的跨场景闭包（如计费+带宽共享某个 feature-task）的命名与归属。
- review-ui 如何渲染新结构。
