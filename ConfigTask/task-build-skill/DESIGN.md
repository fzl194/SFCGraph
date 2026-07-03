# ConfigTask Task 层 Agent 构建体系 — 设计文档

> 日期：2026-06-30
> 状态：设计稿 v2（brainstorming 产出，已过 1 轮 spec 评审并修正，待人工评审 → writing-plans）
> 权威 schema：根目录 `改进后三层图谱定义.md`（静态三层 + 动态 Task 层，§4-§8）
> 前作（已 superseded）：`ConfigTask/builder/` 代码 pipeline、`CONFIGTASK_SCHEMA.md`、`UNIFIED_TASK_SCHEMA.md`

---

## 1. 目标与非目标

### 1.1 目标
构建一套 **Agent 工作准则（Skill）+ Task 资产目录约定**，让 Agent 自底向上、迭代演进地构建动态 Task 层的 5 类对象（`Task / TaskParameterBinding / TaskRule / DecisionPoint / TaskRelation`），**人只做审查与持续校准**。

核心特性：
- **Agent 构建，不是代码 pipeline**。旧 `builder/` 那套 scan→split→cluster→merge 代码流水线废弃。
- **自底向上、特性内垂直**：处理一个特性时，先建全它用到的命令 atom，再凝练 compound，再建 feature task，最后跨特性凝练 generalized/solution。
- **迭代演进、可修正**：同一命令/步骤被多个特性用到时增量补全；每一层都可能演进与合并。
- **闭环 + 持续人工校准**：Agent 自带审查与自改；正确性由"抽取出来的资产效果"判定，人工持续校准渐进改进，不是一蹴而就。
- **Skill 由实战反推**：先起草准则 → 在试点特性下真做 → 派生 review Agent → 人工评审 → 反推修正 Skill。

### 1.2 非目标（YAGNI）
- 不做"一键全量抽取 220 特性"的自动化。特性逐个处理，逐个审查。
- 不引入新的 schema 对象（`variable_source` 除外，见 §4.3，待 schema 定夺）。5 类对象严格对齐《改进后三层图谱定义》§4-§7。
- 不改静态三层（业务/特性/命令图谱）。Task 层通过 `ref` 只读引用静态层。
- 本期不做 Skill 之外的工程化封装（Web 看板、API）。看板类工具按需另立。

---

## 2. 边界规则（硬约束）

| 目录 | 权限 | 用途 |
|---|---|---|
| `ConfigTask/` | **可自由读写删（工作目录）** | Skill 本体、Task 资产、archive |
| 根目录 `改进后三层图谱定义.md` | **只读** | schema 唯一权威 |
| `FeatureGraph/data/legacy/` | **只读** | 特性清单与每特性文件清单（CSV） |
| `CommandGraph/data/assets/{nf}/{version}/` | **只读** | MML 命令资产 |
| `output/…产品文档…/` | **只读** | 原始产品 md |

> 所有写入只落在 `ConfigTask/` 下。Skill 与资产都住在此目录。

### 2.1 产品文档入口（只读语料）

| 网元 | 入口 |
|---|---|
| UDG（用户面） | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/`（特性概述/激活/原理/调测/参考信息）；`…/OM参考/命令/UDG MML命令/` |
| UNC（控制面） | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/`；`…/OM参考/命令/UNC MML命令/` |

---

## 3. 体系定位

```
静态三层（不动，只读引用）        动态 Task 层（本体系构建，写入 ConfigTask/）
─────────────────────────       ─────────────────────────────────────
业务图谱                          ConfigurationSolution
  BD / NS / CS / SO                     │ uses_task
特性图谱                                ▼
  Feature / SubFeature / License   Solution Task
命令图谱                                │
  MMLCommand / CommandParameter     Feature Task  ← 强制 anchor（每特性必建）
  / ConfigObject                        │
                                   Compound Task ← Agent 凝练（步骤级）
                                        │
                                   Atom Task     ← 强制 anchor（每配置类命令必建）
                                        │ ref
                                        ▼
                                   MMLCommand（静态）
```

- 动态层是配置/Agent 执行时**唯一消费**的图；通过 `ref` 回查静态层（《改进后三层图谱定义》§11）。
- 静态→动态是**投影**关系（§6.4）：静态事实（参数引用、条件必选、License）投影成 TaskParameterBinding / DecisionPoint / TaskRule。

---

## 4. 权威 schema 与对象模型（摘要，权威以根目录定义为准）

5 类动态对象，字段严格遵循《改进后三层图谱定义》§4-§7：

| 对象 | 关键字段 | 挂载 |
|---|---|---|
| `Task` | task_id, nf, version, task_logical_name, **task_layer**(atom/compound/feature/solution/generalized), task_intent, **task_category**(plan/configure/verify/activate/rollback/delete/query), **ref**(单字段，指向静态对象), parameter_bindings, status, source_evidence_ids, confidence(optional), notes(optional) | — |
| `TaskParameterBinding` | **binding_id**, task_ref, parameter_ref, **binding_type**(fixed/variable/reference/decision_driven/derived/optional), value, source_ref, decision_ref, **requiredness**(required/optional/conditional), source_evidence_ids | 内嵌于所属 atom task |
| `TaskRule` | rule_id, owner_task_ref, rule_name, **rule_type**(12 类枚举), **rule_scope**(task/relation/parameter/feature/solution), condition, constraint, severity, rule_expression_mode(explicit/inferred/projected), rule_source_kind, source_static_refs | 挂 owner_task_ref |
| `DecisionPoint` | decision_id, owner_task_ref, decision_name, decision_question, decision_type, requiredness, options[].impacts[](target_type: task/command/parameter/feature/solution/decision_point/semantic_object/config_object；effect_type: adds/skips/excludes/requires/sets_value_pattern/changes_command_set/selects_option…), default_option(optional) | 挂 owner_task_ref |
| `TaskRelation` | relation_id, from_task_ref, to_task_ref, relation_type(precedes/depends_on/must_be_last/excludes/fallback_to/parallel_with/expands_to/contains), requiredness, condition_ref, propagated_context | 内嵌于父 task（from→to，不建独立文件） |

> 字段名以 `改进后三层图谱定义.md` §4-§7 为准；上方为速查摘要，冲突时以权威 schema 为准。

### 4.1 状态流转（迭代 + 稳定度门控）
```
draft（Agent 刚建）→ inferred（投影补全/待审）→ active（人工审过 = stable）→ deprecated
```
- **高层 task 只能引用 active 的下层 task**——这是"先把底层建好再往上"的可操作门控。
- 任何下层 task 被演进（补配法/改 binding/合并）后，status 回 `inferred`，依赖它的高层连锁复审。
- **连锁依赖查找算法**（找到谁依赖了被改的下层 task）：扫描全部 `task_relations`（`to_task_ref` 或 `from_task_ref` 命中）+ 全部 `DecisionPoint.impacts[].target_ref` 命中 + 全部 `TaskRule` 引用该 task 的，得到 dependent 集合，逐个降级复审。为加速，`task-index.md` 维护 `referenced_by` 列（见 §5）。

### 4.2 atom 拆法准则（已定）
**一条配置类命令 = 一个 atom task**。配法差异（如 ADD URR 在线/离线/融合）用挂在 atom（或上层）的 `DecisionPoint` + `decision_driven` 参数表达，**不拆多个 atom**（对齐《改进后三层图谱定义》§4.4.1 DP-B）。atom 身份是命令级、跨特性可复用。`binding_id` 命名：`{task_id}:{PARAM_NAME}`（如 `UDG@20.15.2@Task@0-00001:URRNAME`）。

### 4.3 TaskParameterBinding 字段对齐说明（⚠️ 待 schema 定夺）
权威 schema §4.2 的 TaskParameterBinding 字段为：`binding_id / task_ref / parameter_ref / binding_type / value / source_ref / decision_ref / requiredness / source_evidence_ids`。

**缺口**：命令 md 的 `parameter_description` 有 `数据来源` 列（全网规划/本端规划/与对端协商/已配置数据中获取），seed 也用了 `variable_source(global_planned/local_planned/peer_planned)`——这是配置生成的高价值信号（告诉工程师"值从哪来"），但**权威 schema §4.2 无对应字段**。

**处置（已定：A，schema 已改）**：在 `改进后三层图谱定义.md` §4.2 增 `variable_source` 字段（已应用）。枚举：`global_planned / local_planned / peer_planned / reference / decision_driven`。本体系按此实现——`variable` 类绑定写 `variable_source`；`fixed` 绑定固定值写 `value`；`reference` 写 `source_ref`。

---

## 5. 资产模型与目录结构（写入 `ConfigTask/`）

```
ConfigTask/
├── task-build-skill/                 # ← Skill 本体（实战反推成形）
│   ├── DESIGN.md                     #   本文件（设计）
│   ├── SKILL.md                      #   Agent 工作准则（实现期产出，持续修正）
│   ├── procedures/                   #   细则（特性 pass 流程、合并判据、投影规则、审查清单）
│   └── templates/                    #   yaml 模板（5 类对象）
│
├── task-assets/{nf}/{version}/       # ← Task 资产（照搬 CommandGraph 的 nf×版本 隔离）
│   ├── tasks/{TaskID}.yaml           #   atom/compound/feature/solution/generalized
│   │                                 #     （atom 内嵌 parameter_bindings）
│   ├── decision_points/{DPID}.yaml
│   ├── task_rules/{RuleID}.yaml
│   ├── task_relations/{RelID}.yaml
│   ├── review/                       #   每次 pass 的自审 + 人工校准记录
│   │   └── {feature-id}-pass-{N}.md
│   └── task-index.md                 #   每行一个 task（见 §5.1）
│
└── archive/                          # ← superseded 文档留底（见 §10）
```

- **每对象一个 yaml**（人审友好）。`{nf}` ∈ {UDG, UNC}，`{version}` = 20.15.2。
- Skill 是 Agent "拥有相关 task 基本知识"的入口：每次 pass 开始先查 `task-index.md`。

### 5.1 命名、ID 与索引
- **实例键**：`{nf}@{version}@{ObjectType}@{编号}`，如 `UDG@20.15.2@Task@00001`、`@DecisionPoint@00001`、`@TaskRule@00001`、`@TaskRelation@00001`。
- **编号段**（层前缀 + 5 位顺序号，每层各自从 00001 起）：
  - atom `0-00001`～（seed 00001~00018 → `0-00001`~`0-00018`）
  - compound `1-00001`～（seed 00101~00104 → `1-00001`~`1-00004`）
  - feature `2-00001`～（seed 00201~00204 → `2-00001`~`2-00004`）
  - solution `3-00001`～
  - generalized `4-00001`～（seed 00301 → `4-00001`）
- **实例键示例**：`UDG@20.15.2@Task@0-00001`（atom）、`@Task@1-00001`（compound）、`@Task@2-00001`（feature）、`@Task@4-00001`（generalized）。
- **文件名→ID**：`tasks/task-{编号}.yaml`（编号如 `0-00001`）、`decision_points/dp-{编号}.yaml`、`task_rules/rule-{编号}.yaml`、`task_relations/rel-{编号}.yaml`。
- **task-index.md 列**：`task_id | layer | task_intent | ref | status | referenced_by`。`referenced_by` = 反向依赖（被哪些 task 经 task_relations / DP impacts / TaskRule 引用），供 §4.1 连锁查找；每次 pass 末尾增量更新。

---

## 6. 核心构建准则

### 6.1 强制 anchor vs Agent 凝练
| 层 | 产出方式 | 触发 |
|---|---|---|
| **atom** | **强制必建** | 特性激活/部署 md 中出现的**配置类命令**（ADD/SET/DEL/MOD 等配置动作）→ 必有 atom |
| **feature** | **强制必建** | 每个被处理的特性 → 必有 feature task（ref→Feature） |
| compound | Agent 凝练/演化 | 特性内多命令聚成命名业务阶段 |
| generalized/solution | Agent 凝练/演化 | 跨特性组合时抽象 |

> 查询类命令（DSP/LST/SHOW）默认不建 atom。**例外**：若某特性的**验证步骤**必须依赖某 DSP 命令的输出来驱动决策（如 eDRX 验证），则建 `task_category: verify` 的 atom，并在 review md 注明理由。

### 6.2 同批 co-build
建一个 task 时，**连带建挂在其下的 TaskRule 与 DecisionPoint**。一次 pass 的产物是"task + 其 rule + 其 DP"的组合，不是孤立 task。

### 6.3 每一层都演进、都会合并（可操作判据）
- **atom 级（命令重用演进）**：同一命令只有一个 atom（§4.2），新特性用到时**只能演进**（补配法→加 DP option；补证据→加 source_evidence_ids；修正 binding），不新建不合并。改动后 status 回 `inferred`。
- **compound / generalized 级（C vs C1：合并 | reference | 新建）**——按下面可操作判据：
  1. 计算"意图重合度"：候选 compound 与现有某 compound 是否 `task_logical_name` 同义（或 task_intent 短语重合）**且** 命令集 Jaccard ≥ 0.7。
  2. **合并**：意图同义 + 命令集 Jaccard ≥ 0.7 → 并入现有 compound，累加 source_evidence_ids，status 回 `inferred`。
  3. **reference**：意图相近（共享部分命令）但 Jaccard 0.3~0.7 → 新建，但用 `task_relations` 引用共享子 atom，差异部分独立。
  4. **新建**：Jaccard < 0.3 或意图不同 → 独立新建。
  5. **决策权**：Agent 提出合并/引用建议并给置信度；合并（步骤 2）需在 review md 标注待人工确认；其余 Agent 自决。
- **feature 间组合**：多特性共享底座（如都用 ADD APN）→ 抽 generalized；共享 atom 经 task-index 发现复用，不复制。

### 6.4 静态投影（《改进后三层图谱定义》§8）
建 atom 时，把命令图谱静态事实投影进动态层。投影产出的是 **`rule_type` 取值**（不是新字段名）：

| 静态事实（CommandGraph） | 动态投影（TaskRule.rule_type / 其他对象） |
|---|---|
| `parameter_references`（跨命令引用） | `TaskParameterBinding.binding_type=reference` + `source_ref`；`TaskRelation.propagated_context` |
| `parameter_conditional_required`（条件必选） | `DecisionPoint`（条件→option→参数 adds）+ `decision_driven` 绑定 |
| 命令 `references`/`refers_to`（对象间） | `TaskRule`，**rule_type: binding_rule**（跨命令绑定强制） |
| 命令 notes（规格/唯一性/上限） | `TaskRule`，**rule_type: cardinality_rule / uniqueness_rule** |
| 特性 `requires_license`/`depends_on` | feature task 的 `TaskRule`，**rule_type: dependency_rule**，`rule_source_kind=projected` |

---

## 7. 一次特性 pass 的标准流程（Skill 核心程序）

```
输入：
  - 该特性的全部相关 md（清单来自 FeatureGraph/data/legacy/{nf}_feature_files.csv，按 feature_id 过滤）
    · 主源：部署/激活 md（命令、配置意图、操作流程、数据规划表）
    · 辅源：特性概述/实现原理/参考信息/调测 md（决策维度、约束规格、补充证据）
  - 涉及命令的 CommandGraph mml_commands.jsonl（参数细节：数据来源/可选必选/取值范围/配置原则）
  - task-index.md（现有 task 全景 + referenced_by）

0. 检索复用：扫 task-index.md，本特性涉及的命令/步骤哪些已存在、status 如何
1. 建全底部 atom（强制，一命令一 atom）：
   对每条配置类命令：
   - parameter_bindings（每条带 binding_id = {task_id}:{PARAM}）：
       数据来源(全网/本端/对端) → variable_source (§4.3，待 schema 定夺)
       可选必选说明(必选/可选/条件必选) → requiredness(required/optional/conditional)
       取值范围/默认 → fixed 的 value 或 variable
   - 静态投影：parameter_references→reference；conditional_required→DecisionPoint（§6.4）
   - co-build：挂该 atom 的 TaskRule（notes→rule_type: uniqueness/cardinality 等）+ DecisionPoint（配法分叉）
   - 已存在 atom：增量演进（补 DP option / 补证据 / 改 binding），status 回 inferred
   - ⚠️ 命令不在 CommandGraph：见 §8.1 缺命令处置
   产出全部 status=draft/inferred
2. 凝练 compound（Agent 抽象）：
   按特性的业务阶段把 atom 聚成命名步骤；每个候选先查现有 compound，按 §6.3 判据：合并/reference/新建
   建 task_relations（precedes/contains + propagated_context）
   co-build compound 级 TaskRule（rule_type: consistency_rule 等）
3. 建 feature task（强制）：ref→Feature，task_relations 编排本特性的 compound/atom
   co-build feature 级 TaskRule（rule_type: consistency/dependency_rule）+ DecisionPoint（特性级选择）
4. 跨特性凝练（当本特性与已有特性可组合）：generalized/solution，按 §6.3 演化合并

输出：本特性全栈 task（bottom-up）+ 更新 task-index.md（含 referenced_by），全部 status=draft/inferred 等审
```

> 本期试点限定 **UDG**（计费/IPSec/eDRX 均为 UDG 特性）。UNC 的 `FeatureGraph/data/legacy/UNC_feature_files.csv` 与 `CommandGraph/data/assets/UNC/20.15.2/` 已存在，后续特性同流程可跑，本期不展开。

---

## 8. 审查闭环（持续校准，非一蹴而就）

```
┌──────────────────────────────────────────────────────────────────┐
│  Agent 按 §7 提取（status=draft/inferred）                        │
│        │                                                          │
│        ▼                                                          │
│  Agent 自审（派 review subagent，按审查清单）：                    │
│    · schema 合规（5 类对象字段/枚举/挂载）                         │
│    · ref / parameter_ref 命中静态层（命令/特性/参数真实存在）       │
│    · 证据可追溯（source_evidence_ids 指向真实 md 段）              │
│    · 投影正确（reference/conditional_required/规格 投影对齐 §6.4） │
│    · 合并合理（§6.3 判据执行正确，合并项已标注待确认）             │
│    · ★正向实例化验收（§8.1）                                      │
│        │                                                          │
│        ▼                                                          │
│  Agent 按自审意见自修 → 重审直到自审通过                           │
│        │                                                          │
│        ▼                                                          │
│  交人工校准：人工看抽取效果，给意见 → 通过则 status=active         │
│    · 驳回 → 回炉（回到提取/自审）                                  │
│    · 人工意见同时反哺 Skill 准则（§9，结构化记录见 §8.2）          │
│        │                                                          │
│        ▼                                                          │
│  下一轮 pass 带着改进后的准则 + active 资产继续（永续闭环）         │
└──────────────────────────────────────────────────────────────────┘
```

### 8.1 正向实例化验收（硬验收）+ 缺命令处置
- **硬验收**：给定一个 feature task + 选定其 DecisionPoint 的若干 option，按 task_relations 递归展开，**生成的命令序列 + 参数规划必须能复现该特性 md 中的真实配置示例/任务示例脚本**（《改进后三层图谱定义》§4.4 运行模型）。复现不了 = 抽取有缺，必须修。这是"准则准不准"的客观判据。
- **缺命令处置**：若特性 md 中的某配置类命令**不在** CommandGraph `mml_commands.jsonl`：
  - 仍建该 atom，`ref` 写预期 ID `UDG@20.15.2@MMLCommand@<name>`、`status: draft`；
  - 挂一条 `TaskRule`（rule_type: `dependency_rule`，severity: `warning`，rule_logic 标"命令图谱缺该命令，待 CommandGraph 补"）；
  - 在 review md 记入"缺命令清单"，供 CommandGraph 维护者回填。
  - **不阻塞**本特性 pass；参数细节暂从命令 md 手册（`output/…/MML命令/`）抽，记入 source_evidence_ids。
  - **ref 一致性**：CommandGraph 回填该命令时，若最终 `MMLCommand` ID 与本 atom 预写的 `ref` 不一致，需同步更新该 atom 的 `ref`（属只读边界外动作，由 CommandGraph 维护者协调或在 review md 标注）。

### 8.2 审查记录与人工校准格式
每次 pass 在 `task-assets/{nf}/{version}/review/{feature-id}-pass-{N}.md` 留：
- `## 自审发现` / `## 修改记录` / `## 缺命令清单`（如有）
- `## 人工校准`（结构化，便于 §9 反哺 Skill 挖掘）：
  ```
  - 意见: <人工指出的问题>
    影响: <task_id 列表>
    反哺Skill条款: <对应 SKILL.md/procedures 的哪条准则需修正>
  ```

---

## 9. Skill 载体与派生方式（实战反推）

Skill 不是凭空写的，按下面循环成形（实现期动作）：

```
1. 起草 Skill v0：把 §6-§8 准则 + §7 流程 + yaml 模板写进
   ConfigTask/task-build-skill/SKILL.md（+ procedures/ + templates/）
2. 选试点特性：计费（seed 已有，做字段映射与回归）+ IPSec + eDRX
3. 执行 Agent（我）在试点特性下真跑 §7 流程，产出真实 task 资产
4. 派生 review Agent 评审 + 人工评审（§8）
5. 把"实战+评审"暴露的准则缺陷（挖 §8.2 的"反哺Skill条款"）反推修正 Skill → v1
6. 再试点、再修正……直到准则稳定（连续 2 个新特性 pass 人工免改或仅微调）
```

Skill 内容大纲（v0 起草、持续修正）：定位与边界（§2-§3）/ 对象模型与状态（§4）/ 资产目录与命名（§5）/ 构建准则（§6）/ 特性 pass 流程（§7）/ 审查清单与正向实例化（§8）/ 演进合并判据（§6.3）/ yaml 模板（templates/）。

---

## 10. 旧代码与旧资产清理（实现期执行；仅落在 ConfigTask/）

| 处置 | 对象 | 说明 |
|---|---|---|
| **删除** | `builder/`、`build_all.py`、`pipeline.yaml`、`tests/`、`PIPELINE_RUNBOOK.md` | 旧代码 pipeline |
| **删除** | `data/`（含 UDG/UNC 的 doc_steps/task_candidates/clusters/agent_prompts/agent_outputs 及其中分析 md） | 旧 schema 产物 |
| **删除** | `CONFIGTASK_SCHEMA.md`、`UNIFIED_TASK_SCHEMA.md` | 被 `改进后三层图谱定义.md` 取代 |
| **删除** | `计费场景-task资产/build_charging_assets.py`、`build_dashboard.py` | 硬编码生成器；seed 迁移后不再需要 |
| **归档→`archive/`** | `ARCHITECTURE_REVIEW.md`、`ConfigTask设计.md`、`抽取指令-ConfigTask对象.md`、`审视报告-12特性.md`、`样板-内容计费-统一task架构.md`、`样板-计费功能-统一task架构.md`、`样例-IPSec@20.15.2-任务层实例.md`、`样例-内容计费@20.15.2-任务层实例.md` | 有可复用设计思考，留底 |
| **保留并迁入** | `计费场景-task资产/*.yaml`（27 task/4 DP/10 rule）→ `task-assets/UDG/20.15.2/` | 按 §10.1 字段映射，作 seed |

> 清理仅作用于 `ConfigTask/`。只读目录不动。

### 10.1 seed → 新 schema 字段映射表
| seed 字段 | 新 schema 字段 | 说明 |
|---|---|---|
| `task_id` | `task_id` | 不变 |
| `task_logical_name` | `task_logical_name` | 不变 |
| `task_layer` | `task_layer` | generalized 等枚举值对齐 |
| `command_ref` / `feature_ref` | `ref` | 合并为单字段 |
| `task_summary` | `task_intent` | 语义对齐 |
| `task_category: 配置`（中文） | `task_category: configure` | 中文→英文枚举 |
| `parameters[]` | `parameter_bindings[]` | 改容器名 |
| `parameters[].parameter_ref` | `parameter_bindings[].parameter_ref` | 不变 |
| `parameters[].binding_type` | `parameter_bindings[].binding_type` | 枚举对齐 |
| `parameters[].variable_source` | `parameter_bindings[].variable_source`（§4.3 待定夺） | 见 §4.3 |
| `parameters[].fixed_value` | `parameter_bindings[].value` | fixed 值进 value |
| `parameters[].source_ref`（reference） | `parameter_bindings[].source_ref` | 不变 |
| `parameters[].note` | Task.`notes`（聚合） | schema 无 per-binding note |
| 缺 `binding_id` | 新增 `{task_id}:{PARAM}` | §4.2 |
| 缺 `requiredness` | 从命令 md 可选必选补 | §7 |
| 缺 `task_intent` | 由 `task_summary` 映射 | — |
| 缺 `source_evidence_ids` | 补 `[部署UPF_28493406.md]` 等 | — |
| `status: active` | 重置为 `inferred`（迁入后待人审） | §4.1 |
| `task_relations[]`（内嵌） | 拆为独立 `TaskRelation` 对象（rel-*.yaml） | 加 relation_id |
| `decision_points`: `owner_ref` | `owner_task_ref` | 字段名对齐 |
| `rules`: `task_ref` | `owner_task_ref` | 字段名对齐 |

---

## 11. 试点与落地顺序（写入后续 implementation plan）

1. **清理与脚手架**：执行 §10 清理；建 `task-build-skill/`、`task-assets/UDG/20.15.2/`、`archive/` 骨架。
2. **seed 迁移**：计费 27 task/4 DP/10 rule 按 §10.1 迁入 + 字段映射 + 过自审（回归基线）。
3. **Skill v0 起草**：写 SKILL.md + procedures/ + templates/。
4. **试点 1：计费回归**（已迁入）→ 正向实例化验收 → 自审 → 人工校准。
5. **试点 2：IPSec**（多场景同骨架，强 DP）→ 全流程 → 校准 → 反哺 Skill。
6. **试点 3：eDRX**（配置范围决策 + 跨层优先级 rule + verify 类命令）→ 全流程 → 校准 → 反哺 Skill。
7. **Skill 定稿**：连续试点验证后，SKILL.md 收敛为稳定准则。
8. **持续运营**：按 Skill 逐特性处理剩余特性，人工持续校准。

---

## 12. 风险与对策

| 风险 | 对策 |
|---|---|
| Skill v0 准则不准 | §9 实战反推 + §8.1 正向实例化硬验收兜底 |
| 演进导致高层连锁失效 | status 流转 + "高层只引 active 下层"门控 + §4.1 连锁查找算法 |
| 合并误判（把不同步骤合一） | §6.3 可操作判据（Jaccard + 意图重合）+ 合并项人工确认 + 自审 |
| 特性 md 命令不在 CommandGraph | §8.1 缺命令处置：建 draft atom + flag TaskRule + 不阻塞 |
| 命令 jsonl 缺参数细节 | 以命令 md 手册（output/…/MML命令/）补；记 source_evidence_ids |
| `variable_source` schema 缺口 | §4.3 待 schema 定夺（建议 A：扩字段）|
| 只读边界误写 | 所有写路径限定 `ConfigTask/`；Skill 首条即边界规则 |

---

## 13. 待人工评审确认的开放项

1. **查询类命令默认不建 atom**（verify 步骤例外建 `task_category: verify`）——是否符合预期？
2. **`variable_source` schema 缺口**（§4.3）：权威 schema §4.2 无此字段，但 seed 与命令 md `数据来源` 列都用。建议 (A) 由你在 `改进后三层图谱定义.md` §4.2 增 `variable_source` 字段；或 (B) 过渡期写进 `value` token。**请拍 A 还是 B。**
3. **compound/generalized 编号段**（atom 0xxxx / compound 1xxxx / feature 2xxxx / solution+generalized 3xxxx+，与 seed 一致）——采纳？
4. **试点特性 IPSec + eDRX** 是否合适，或换别的？
5. **归档 vs 直接删除**：§10 的 B/C 类文档同意"归档"而非删？
