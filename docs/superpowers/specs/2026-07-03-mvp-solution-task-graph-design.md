# MVP-方案-任务图谱：流程与场景层设计

> 日期：2026-07-03
> 状态：设计草案（待 spec 审查 + 用户复核）
> **对象模型与构建准则权威**：根目录 `改进后三层图谱定义.md` §3-§8 + `ConfigTask/task-build-skill/SKILL.md` v3。本 spec **不重定义**任何对象/字段/枚举，只补充这两份未覆盖的部分：① 通用构建流程框架；② 场景层目录与闭包引用约定；③ 现有计费场景 md 的迁移方向。

---

## 1. 与现有权威的关系（必读）

| 主题 | 权威出处 | 本 spec 是否重定义 |
|---|---|---|
| 静态业务图谱（BD/NS/CS/SO + 关系） | `改进后三层图谱定义.md` §3.1 | 否，采用 |
| 静态特性图谱（Feature/SubFeature/License + 6 关系） | §3.2 | 否，采用 |
| 静态命令图谱（MMLCommand/Param/ConfigObject + 关系） | §3.3 | 否，采用 |
| 动态 Task 层对象（Task/TaskParameterBinding/TaskRule/DecisionPoint/TaskRelation） | §4-§7 | 否，采用 |
| task_layer 取值（atom/compound/feature/**solution**/generalized）与 ID 前缀（0-/1-/2-/**3-**/4-） | §4 + SKILL.md §2.2 | 否；**`solution` 层已存在，非新增** |
| TaskRelation 8 值 relation_type 枚举（precedes/depends_on/must_be_last/excludes/fallback_to/parallel_with/expands_to/contains） | SKILL.md §2 | 否，采用 |
| TaskRelation 存储（内嵌父 task yaml `task_relations[]`，不建独立文件） | SKILL.md §3 | 否，采用 |
| Task 递归组合 / 父子约束 / 复用合并 | §4.5（含 4.5.1 父 DP 锁子 DP、4.5.2 合并不新增对象类型） | 否，采用 |
| 静态→动态投影（参数条件/命令引用/License/业务方案） | §8（含 §8.4 业务方案→Solution Task） | 否，采用 |
| Task 层逐特性构建流程（atom→compound→feature→跨特性）+ 审查闭环 + 合并双闸 | SKILL.md §5/§7/§8 | 否，采用 |
| 字段命名（`decision_id`、`owner_task_ref`、`task_category` 等） | §4-§7 | 否，采用 |

> **审阅者注**：本表的每一行都是对 v1 草案矛盾/冗余处的明确让位。v1 曾把 relation_type 写成"不冻结"、把 `solution` 写成"新增"、自创 `dp_id/task_ref` 字段名、把 Task 组合边列为顶层对象——均撤回，改引权威。

## 2. 本 spec 真正补充的内容

权威文档定义了"对象是什么、字段是什么、单特性怎么建"，但**没有**定义：
1. 跨场景通用的"按方案 MVP 增量构建"流程框架（§3）；
2. 场景层（业务闭包）的目录结构与"闭包如何引用 canonical Solution Task"（§4）；
3. 现有计费场景 `three-layer-graph/*.md` 的迁移方向（§5）。

其余皆为对权威的引用或复述。

---

## 3. 通用构建流程框架（NEW）

### 3.1 核心原则
1. **MVP 永远 = 单个方案（ConfigurationSolution）**。不管什么图谱/输入，工作单元始终是一个方案；规模靠"加方案"线性扩展。
2. **业务顶层（BD→NS→CS）由人+Agent 一次性定**，每场景独立。产物 = `business/` 下的 CS 定义（id/name/intent/scope/participants/design_intent + 非正式能力预期）。
3. **每个 CS 独立拆解为 Solution Task**（动态层，`task_layer=solution`，ID 前缀 `3-`）。CS 间的复用由 Task 层处理（§4.5.2 合并机制），方案本身不互相耦合。
4. **特性也是小方案**：feature-task 的拆解复用本流程，输入 = 该特性的激活文档（每种配置方式视为该特性的一个"方案"）。
5. **Feature 静态抽取 ‖ feature-task 动态构建 可并行**；同步点 = feature-task 的 `feature_ref` 指向已存在的 FeatureGraph Feature。

### 3.2 拆解选择顺序（复述 SKILL.md §4.1 的强制 anchor，给"选择顺序"表述）

给定任意上层 Task 往下拆，按顺序判定子 Task 粒度：

```
1. 能映射到某个已有 Feature？        → 子 = feature-task（feature_ref → FeatureGraph）
2. 否则，是几条专属命令的组合？       → 子 = compound/step-task（task_layer=compound，再递归）
3. 否则，就一条命令？                → 子 = atom-task（ref → CommandGraph，叶子）
```

- 叶子永远是 atom-task（已建，复用）。
- 命中 1 时，feature-task 继续往下拆（递归）。
- 与 SKILL.md §4.1（atom 强制 / feature 强制 / compound 凝练 / solution-generalized 凝练）一致，本流程是其"自顶向下选择顺序"的对应表述。

### 3.3 DP 放置（复述 §4.5.1 + §6）
- DP 尽量挂在**能覆盖其全部变体的最深 Task** 上。
- 作用域 = 该 Task 及其向下能触及的全部后代（通过 `impacts[].target_ref` 指向子 DP / 子 task / 参数）。
- 父 Task 固定子 Task 配置方法的两条路径（父 DP `selects_option` 子 DP；或父 TaskRule `rule_scope:relation` 约束）已在 §4.5.1 给出，本 spec 不另立。

### 3.4 task 间边（采用 8 值枚举，选择靠推理）
- relation_type 用 SKILL.md §2 的 8 值枚举，**不自由命名**。
- "从内容推理" = 拆解时根据源材料（激活文档/方案定义）判断该用 8 个里的哪一个（如"先 A 再 B"→`precedes`；"A 兜底"→`fallback_to`；"A 含 B"→`contains`）。

---

## 4. 场景层目录与闭包引用（NEW）

权威文档定义了 Solution Task 对象，但未约定**场景层闭包**放哪、如何引用 canonical。本节补这项。

### 4.1 目录约定

```
业务图谱体系/{场景}/                          # 场景专属，人+Agent 维护
├── business/                                # 业务顶层（§3.1 原则 2 产物）
│   ├── bd-ns.jsonl                          # BD/NS 静态对象 + contains/instantiated_as 边
│   └── cs-definitions.jsonl                 # CS 定义（MVP 输入契约：id/name/intent/scope/participants/design_intent/预期能力）
├── closures/                                # 场景闭包：引用 canonical Solution Task + 承载场景特定语义
│   └── cs-{id}-closure.yaml                 # 一个 CS 一个闭包文件
├── docs/                                    # md 残留：design_intent 叙述、端到端走查、证据原文、合并评估、审查报告
└── (保留现有 feature-knowledge/ 等)
```

### 4.2 Solution Task 归属（关键决策）

- **Solution Task 本体在 ConfigTask**（遵 SKILL.md §0"可写仅 ConfigTask/"，ID 前缀 `3-`，按 `{NF}/{version}` 隔离）。
  - 例：UDG 侧"离线计费"= `UDG@20.15.2@Task@3-xxxxx`（solution 层）；UNC 侧同理。
- **场景闭包**（`closures/cs-{id}-closure.yaml`）= **薄引用层**：组合 UDG + UNC 的 Solution Task ID + 跨侧/跨 NF 的场景级 DP/Rule + 指向 `docs/` 的 md 残留。
- 闭包**不重抽** canonical 实体内部；CS 的业务方案投影（§8.4）落在 Solution Task，闭包只做"场景视角的组合 + 引用"。

### 4.3 闭包文件契约（草案）

```yaml
closure_id: CS-CH-01            # 业务层 CS id
scenario: 计费场景
solution_tasks:                 # 引用 canonical（跨 NF）
  - UDG@20.15.2@Task@3-00001
  - UNC@20.15.2@Task@3-00002
decision_points:                # 场景级跨侧 DP（如"配额耗尽动作"跨 UDG/UNC）
  - <DP id 或内嵌>
rules:                          # 场景级规则（跨侧一致性等）
  - <TaskRule 或引用>
docs_refs:                      # md 残留指引
  - docs/cs-ch-01-walkthrough.md
  - docs/cs-ch-01-merge-eval.md
status: draft/inferred/active
```

---

## 5. 计费场景迁移方向（非实施步骤）

1. **保留不动**：`FeatureGraph/`、`CommandGraph/`、`ConfigTask/` 现有 atom/compound/feature Task 资产。
2. **本期构建**（按 §3 流程，MVP = 单个 CS）：
   - feature-task / step-task / solution-task 子树：从特性激活文档 + 现有 `three-layer-graph/*.md` 抽，落 ConfigTask。
   - 场景闭包：新建 `业务图谱体系/计费场景/{business,closures,docs}/`。
3. **改造**：原 `three-layer-graph/01-business-graph.md` 的 CS → `business/cs-definitions.jsonl` + ConfigTask 里对应 Solution Task；DP/BR/SO → 收进 Solution Task 的 DP/Rule（§8 投影），少量进 `docs/`。
4. **退役**：`three-layer-graph/02~05*.md` 里手写的 feature/command/task 重复内容，迁入结构化资产后降为只读视图或废弃；`00-overview.md` 可保留为入口导航。
5. **md 残留入 `docs/`**：design_intent、端到端走查、证据、合并评估、审查报告。

---

## 6. 范围与非目标

**本期范围**
- §3 流程框架 + §4 场景层目录与闭包契约 + §5 迁移方向。
- 计费场景作为首个落地样本，按方案 MVP 增量推进。

**非目标**
- 改 `改进后三层图谱定义.md` / FeatureGraph / CommandGraph 的对象定义。
- 自动化方案合并（SKILL.md §7.1 双闸 + §8.4 人审攒批，保持人工）。
- 一次性迁完所有 md（按 CS 增量）。
- 图数据库落地（后续演进）。

## 7. 待定 / 未来

- `generalized` 层在 §3.2 cascade 中的确切插入点（"能复用通用 task？"是否作为优先级 1.5）——留实施 plan 验证。
- 闭包文件契约（§4.3）字段最终化——随首个 CS 落地校正。
- 跨场景闭包（计费+带宽共享 feature-task）的命名与归属——多场景接入时再定。
- review-ui 如何渲染闭包层。

## 8. 验收（设计层）

- 本 spec 不与 `改进后三层图谱定义.md` §3-§8 或 SKILL.md v3 任何字段/枚举/存储约定冲突。
- §3 流程的每一步都能映射到 SKILL.md §5 的现有 pass 步骤或 §4.5 的递归/合并机制（无悬空动作）。
- §4 闭包契约只引用 canonical ID，不复制 canonical 实体内部字段。
- §5 迁移不要求改 FeatureGraph/CommandGraph 静态字典。
