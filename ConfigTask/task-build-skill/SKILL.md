# Task 层构建 Skill

> 版本：v3（2026-07-03，compound/feature 层稳定抽取管线：A 段 6 步流程 + 复用双闸 + per-DP-分支覆盖硬闸 + 事件驱动攒批人审。完整流程见 `procedures/compound-extraction.md`，设计见 `docs/superpowers/specs/2026-07-02-compound-feature-extraction-design.md`）
> 　v2（2026-06-30）：TaskRelation 全内嵌、variable_source 命令级 fallback、跨特性复用与演进
> 作用对象：动态 Task 层（5 类对象：Task / TaskParameterBinding / TaskRule / DecisionPoint / TaskRelation）
> 权威 schema：根目录 `改进后三层图谱定义.md` §4-§8（冲突时以它为准）
> 设计依据：同目录 `DESIGN.md`

这是一份 **Agent 工作准则**：按它逐特性、自底向上、迭代演进地构建 Task 层资产，**人只做审查与持续校准**。

---

## 0. 边界规则（首条，硬约束）

- **可写**：仅 `ConfigTask/`（本目录）。所有资产、Skill、archive 都在此。
- **只读**（只查不改）：根目录 `改进后三层图谱定义.md`、`FeatureGraph/data/legacy/`、`CommandGraph/data/assets/`、`output/…产品文档…/`。
- 每次写文件前自检：路径是否在 `ConfigTask/` 下。越界即停。

---

## 1. 体系定位（一句话）

静态三层（业务/特性/命令图谱，只读）之上，Task 层是配置执行时**唯一消费**的图，通过 `ref` 回查静态层。本 Skill 只建 Task 层，不动静态层。

```
Solution/Generalized Task → Feature Task → Compound Task → Atom Task --ref--> MMLCommand(静态)
```

---

## 2. 对象模型速查（权威见 schema §4-§7）

| 对象 | 必备字段（速查） |
|---|---|
| Task | task_id, nf, version, task_logical_name, task_layer(atom/compound/feature/solution/generalized), task_intent, task_category(plan/configure/verify/activate/rollback/delete/query), ref, status, source_evidence_ids |
| TaskParameterBinding（内嵌于 atom Task） | binding_id(`{task_id}:{PARAM}`), parameter_ref, binding_type(fixed/variable/reference/decision_driven/derived/optional), variable_source(global_planned/local_planned/peer_planned/reference/decision_driven), value, source_ref, decision_ref, requiredness(required/optional/conditional) |
| TaskRule | rule_id, owner_task_ref, rule_name, rule_type(12类), rule_scope(task/relation/parameter/feature/solution), condition, constraint, severity, rule_expression_mode(explicit/inferred/projected), rule_source_kind, source_static_refs, source_evidence_ids |
| DecisionPoint | decision_id, owner_task_ref, decision_name, decision_question, decision_type(single_choice/multi_choice/boolean/value_selection/object_selection), requiredness, options[].impacts[], default_option |
| TaskRelation | relation_id, from_task_ref, to_task_ref, relation_type(precedes/depends_on/must_be_last/excludes/fallback_to/parallel_with/expands_to/contains), requiredness, condition_ref, propagated_context |

**impacts[].target_type**：task/command/parameter/feature/solution/decision_point/semantic_object/config_object
**impacts[].effect_type**：adds/skips/excludes/requires/sets_value_pattern/changes_command_set/selects_option/selects_solution/selects_feature/changes_scope

### 2.1 status 流转 + 稳定度门控
```
draft（刚建）→ inferred（投影/待审）→ active（人审过=stable）→ deprecated
```
- **高层只引用 active 下层**。下层被演进 → status 回 `inferred` → 连锁找依赖（见 §7.2）并复审。

### 2.2 ID 与编号
- 实例键 `{nf}@{version}@{ObjectType}@{编号}`，编号 = 层前缀 + 5 位：
  - atom `0-00001`～ / compound `1-00001`～ / feature `2-00001`～ / solution `3-00001`～ / generalized `4-00001`～
  - DecisionPoint/TaskRule/TaskRelation：各自独立 `0-00001`～ 起编号（不分层前缀，按类型流水）。
- 文件名：`tasks/task-{编号}.yaml`、`decision_points/dp-{编号}.yaml`、`task_rules/rule-{编号}.yaml`、`task_relations/rel-{编号}.yaml`。

---

## 3. 资产目录

```
ConfigTask/assert/{nf}/{version}/
├── tasks/{编号}.yaml               # atom 内嵌 parameter_bindings
├── decision_points/{编号}.yaml
├── task_rules/{编号}.yaml
├── task_relations/                  # 不用（TaskRelation 只内嵌在父 task，见下）
├── review/{feature-id}-pass-{N}.md # 每次 pass 的自审+人工校准记录
└── task-index.md                   # 全景索引（每行一个 task）
```

**task-index.md 列**：`task_id | layer | task_intent | ref | status | referenced_by`
- 每次 pass 末尾增量更新；新建/演进/状态变更都要同步。
- `referenced_by` = 反向依赖集合（被哪些 task 经 task_relations / DP impacts / TaskRule 引用）。

**TaskRelation 存储约定（v2 澄清）**：TaskRelation **只内嵌**在父 task yaml 的 `task_relations[]` 数组里（schema §4.3.1 示例即此形式），**不建独立文件**——避免空目录困惑、保持"审查一个父 task 时一个文件看全它的边"。`relation_id` 必填；连锁查找（§7.2）扫描所有 task 的内嵌数组。

---

## 4. 构建准则

### 4.1 强制 anchor vs Agent 凝练
| 层 | 方式 | 触发 |
|---|---|---|
| **atom** | 强制必建 | 特性 md 出现的**配置类命令**（ADD/SET/DEL/MOD 等配置动作）→ 必有 atom |
| **feature** | 强制必建 | 每个被处理的特性 → 必有 feature task（ref→Feature） |
| compound | Agent 凝练/演化 | 特性内多命令聚成命名业务阶段 |
| solution/generalized | Agent 凝练/演化 | 跨特性组合时抽象 |

> 查询类命令（DSP/LST/SHOW）默认不建 atom。**例外**：验证步骤必须依赖 DSP 输出驱动决策时，建 `task_category: verify` 的 atom，review md 注明理由。

### 4.2 一命令 = 一 atom（不拆）
配法差异（如 ADD URR 在线/离线/融合）用 `DecisionPoint` + `decision_driven` 绑定表达，**不拆多个 atom**。

### 4.3 co-build（同批）
建一个 task 时连带建挂在其下的 TaskRule + DecisionPoint。一次 pass 产物 = "task + 其 rule + 其 DP"组合。

### 4.4 静态投影（建 atom 时自动带出，详见 `procedures/static-projection.md`）
| 静态事实（CommandGraph） | 动态投影 |
|---|---|
| `parameter_references` | binding_type=reference + source_ref；task_relations.propagated_context |
| `parameter_conditional_required` | DecisionPoint（条件→option→参数 adds）+ decision_driven |
| 命令 `references`/`refers_to` | TaskRule（rule_type: **binding_rule**） |
| 命令 notes（规格/唯一性/上限） | TaskRule（rule_type: **cardinality_rule / uniqueness_rule**） |
| 特性 requires_license/depends_on | feature task 的 TaskRule（rule_type: **dependency_rule**, rule_source_kind=projected） |

> `binding_rule`/`cardinality_rule` 等是 **rule_type 取值**，不是字段名。

### 4.5 variable_source 语义（v1 澄清，试点反推）
`variable_source` **只回答"值从哪来"**（取自命令 md / 数据规划表的"数据来源/获取方法"列）："值受什么决策/约束影响"由 `decision_ref` / TaskRule 表达，**不污染 variable_source**。

| 数据来源列（md） | variable_source |
|---|---|
| 全网规划 | `global_planned` |
| 本端规划 | `local_planned` |
| 与对端协商 | `peer_planned` |
| 已配置数据中获取 | `reference`（同时 binding_type=reference + source_ref） |
| 来源本身跨场景分叉（如某参数 A 场景=全网、B 场景=本端） | `decision_driven` |

- 仅当**取值来源本身随场景分叉**时才用 `decision_driven`（例：URRGROUPNAME 在 URL 场景=全网、其余=本端；FILTERIPV6 端口 IMS=对端、any=本端）。
- "来源固定但具体值由决策点选"（如 USAGERPTMODE：来源全网规划一致，但 ONLINE/OFFLINE 由计费方式 DP 选）→ `variable_source=global_planned` + `binding_type=decision_driven` + `decision_ref`，**不是** `variable_source=decision_driven`。
- "来源固定但取值受规则约束"（如 RULE.PRIORITY：来源本端规划，受优先级相对约束）→ `variable_source=local_planned`，约束交给 TaskRule。
- **命令级 fallback（v2 加，pass-2 反推）**：SET 类全局命令（SET URRFAILACTION/UPDEFAULTQUOTA/UPGLBCHGPARA 等）的特性 md 数据规划表**通常不列其参数行**（只列 ADD 类业务命令）。此时 variable_source 取证顺序：① 先查特性 md"获取方法"列 → ② 没有则查 `mml_commands.jsonl` 的 `parameter_description`（常含"全网规划/本端规划"提示）→ ③ 仍无则默认 `local_planned`（保守，全局开关类多为本端运维配置），并在 atom `notes` 注明"来源未在特性 md 明示，按命令级推断"，`source_evidence_ids` 指向命令 jsonl。

---

## 5. 一次特性 pass 的标准流程

```
输入：
  · 该特性全部相关 md（清单来自 FeatureGraph/data/legacy/{nf}_feature_files.csv，按 feature_id 过滤）
      主源：部署/激活 md（命令、配置意图、操作流程、数据规划表）
      辅源：概述/原理/参考信息/调测 md（决策维度、约束规格、证据）
  · 涉及命令的 CommandGraph mml_commands.jsonl（parameter_description：数据来源/可选必选/取值范围/配置原则）
  · task-index.md（全景 + referenced_by）

0. 检索复用：扫 task-index.md，本特性涉及的命令/步骤哪些已存在、status 如何
1. 建全底部 atom（强制，一命令一 atom）：
   对每条配置类命令：
   · parameter_bindings（每条 binding_id = {task_id}:{PARAM}）：
       数据来源(全网/本端/对端/已配置) → variable_source(global_planned/local_planned/peer_planned/reference)
       可选必选说明(必选/可选/条件必选) → requiredness(required/optional/conditional)
       取值范围/默认 → fixed 写 value；否则 variable + variable_source
   · 静态投影（§4.4）
   · co-build：该 atom 的 TaskRule（notes→uniqueness/cardinality）+ DecisionPoint（配法分叉）
   · 已存在 atom：增量演进（补 DP option / 补证据 / 改 binding），status 回 inferred
   · 命令不在 CommandGraph：见 §6 缺命令处置
   产出 status=draft/inferred
2. 凝练 compound（Agent 抽象）—— **完整流程见 `procedures/compound-extraction.md`（A 段 6 步）**：
   按业务阶段把 atom 聚成命名步骤；每个候选按 procedures §2 **复用双闸**（命令集 Jaccard + 相位用途）判：复用/演进 / reference / 新建 / 降级直挂
   建 task_relations（precedes/contains + propagated_context）
   co-build compound 级 TaskRule（rule_type: consistency_rule 等）
   变体配法 → 挂 DP（最底层，feature 及以下，见 procedures §3）
   **收尾跑 per-DP-分支覆盖校验**（procedures §5 / `scripts/check_feature_coverage.py`），不等回炉
3. 建 feature task（强制）：ref→Feature，task_relations 编排本特性的 compound/atom
   co-build feature 级 TaskRule（consistency/dependency_rule）+ DecisionPoint（特性级选择）
4. 跨特性凝练（当本特性与已有可组合）：generalized/solution，按 §7.1 演化合并

输出：本特性全栈 task（bottom-up）+ 更新 task-index.md（含 referenced_by），status=draft/inferred 等审
然后进入 §8 审查闭环。
```

---

## 6. 缺命令/缺参数处置（v1 扩展，试点反推）
静态 CommandGraph 有两类缺口，都**不阻塞** Task 层 pass：

**A. 缺命令**：特性 md 中某配置类命令不在 `mml_commands.jsonl`
1. 仍建 atom，`ref` 写预期 ID `UDG@20.15.2@MMLCommand@<name>`、`status: draft`；
2. 挂 TaskRule（rule_type: `dependency_rule`，severity: `warning`，标"命令图谱缺该命令，待补"）；
3. 参数细节暂从命令 md 手册抽，记 source_evidence_ids。

**B. 缺参数（命令在 mml_commands，但 CommandParameter 不在 command_parameters.jsonl）**——试点实测常见
1. `Task.ref` 仍指向该命令（命中 mml_commands 即可）；
2. `parameter_ref` 仍按预期 ID `UDG@20.15.2@CommandParameter@<cmd>:<param>` 写（基于 mml_commands 的 `parameter_description` 文本 + 数据规划表）；
3. 在该 feature task（或受影响 atom）挂 `dependency_rule`（severity: `warning`，标"该命令的 CommandParameter 结构化对象待 CommandGraph 抽取"）；集中标记时挂在 feature task 上更经济；
4. 参数细节（variable_source/requiredness/value）从特性 md 数据规划表 + mml_commands 的 parameter_description 文本抽，记 source_evidence_ids。

**C. 通用**：review md 记入"**缺静态对象清单**"（命令/参数分别列），供 CommandGraph 维护者回填。CommandGraph 回填时若 ID 与预写 ref/parameter_ref 不一致，需同步对应 atom。

---

## 7. 演进与合并

### 7.1 合并判据（compound / generalized 层；atom 层只演进不合并）
> **完整复用判定见 `procedures/compound-extraction.md` §2（双闸签名，取代本节旧单 Jaccard 判据）**。
> 阈值收紧：旧 0.7/0.3 → 新 **0.75/0.4**（加相位闸后命令集闸可收紧）。atom 层豁免保留（同命令一 atom，只演进不合并）。

判定 = (命令集 Jaccard ≥ 阈值) **且** (相位/用途同义) 双闸：
1. ≥0.75 且相位同义 → **复用/合并**（并入现有，差异挂 DP option 或演进，status 回 inferred；合并项 review md 标待人工确认）
2. 0.4–0.75 或相位近义 → **reference**（新建，共享子 atom，差异独立）
3. <0.4 或相位不同 → **新建**
- atom 层：同命令只有一个 atom，新特性用到只能演进（§5 step 1），Jaccard 判据**不适用** atom。

### 7.2 连锁依赖查找（下层演进后找谁要复审）
扫描全部 task_relations（to/from_task_ref 命中该 task）+ 全部 DecisionPoint.impacts[].target_ref 命中 + 全部 TaskRule 引用该 task → dependent 集合 → 逐个 status 回 inferred 复审。（task-index.md 的 referenced_by 列加速此查找。）
**atom 内部连带（v2 加）**：atom 某 binding 演进时（如 URRNAME global→decision_driven），还要检查同 atom 内其他 binding 是否连带演进（同命令参数获取方法可能一起分叉）。

---

## 8. 审查闭环（持续校准）

```
Agent 按 §5 提取（status=draft/inferred）
  → Agent 自审（派 review subagent，按 §8.1 清单）
  → 按自审意见自修 → 重审直到通过
  → 交人工校准 → 通过则 status=active；驳回则回炉
  → 人工意见结构化记入 review md（§8.2），反哺本 Skill（§9）
下一轮 pass 带改进后准则 + active 资产继续（永续闭环）
```

### 8.1 自审清单
- [ ] schema 合规：5 类对象字段/枚举/挂载（owner_task_ref 等）
- [ ] ref / parameter_ref 命中静态层（命令/特性/参数真实存在）
- [ ] **静态层命中度报告（v1 加）**：统计 Task.ref 命中 mml_commands 的比率、parameter_ref 命中 command_parameters 的比率、dangling endpoint 数；未命中的按 §6 缺命令/缺参数处置标记并在 review md 记入"缺静态对象清单"。避免静态层缺口被 Task 层掩盖。
- [ ] variable_source 准确：逐 atom 对照 md"获取方法"列（§4.5 语义），重点查"来源固定但受决策/约束"的参数是否被误标 decision_driven
- [ ] 证据可追溯：source_evidence_ids 指向真实 md 段
- [ ] 投影正确：reference/conditional_required/规格 投影对齐 §4.4
- [ ] 合并合理：§7.1 判据执行正确，合并项已标注待确认
- [ ] **per-DP-分支覆盖校验通过**（procedures §5 / `scripts/check_feature_coverage.py`）：每个 md 证实变体的 active 命令集 == md_required；compound 间无环
- [ ] **正向实例化验收（§8.3）通过**

### 8.2 review md 格式
`review/{feature-id}-pass-{N}.md`：
- `## 自审发现` / `## 修改记录` / `## 缺命令清单`（如有）
- `## 正向实例化`（选 option → 命令序列，对比 md 示例）
- `## 人工校准`（结构化，供 §9 反哺）：
  ```
  - 意见: <问题>
    影响: <task_id 列表>
    反哺Skill条款: <SKILL.md/procedures 的哪条需修正>
  ```

### 8.3 正向实例化（硬验收）
给定 feature task + 选定其 DecisionPoint 若干 option，按 task_relations 递归展开，**生成的命令序列+参数规划必须复现该特性 md 的真实配置示例/任务示例脚本**。复现不了 = 抽取有缺，必须修。这是"准则准不准"的客观判据。

### 8.4 人审攒批（事件驱动）
人审不每 feature 走一刀，按"**复用库结构变更**"事件分流（详见 `procedures/compound-extraction.md` §6 + spec §10）：
- **原样复用** → 自动放行（per-DP 覆盖校验已把关）
- **新建 compound** → 【待审·新建】队列（附复用证据表）
- **演进已有 compound** → 【待审·变更】队列（高优先，爆炸半径——别的 feature 已引用它）

攒批节奏：每个业务域（批次）收尾审一次；通过 → status `active`，驳回 → 回炉带意见。队列文件：`review/compound-review-queue-{业务域}.md`。

---

## 9. Skill 自身演进（实战反推）
试点中发现准则缺陷 → 挖 review md 的"反哺Skill条款" → 修正本 SKILL.md / procedures/ → 版本号 +1。准则稳定判据：连续 2 个新特性 pass 人工免改或仅微调。

---

## 10. 模板
- `templates/task.yaml` — Task（atom 含 parameter_bindings / compound / feature / generalized 注释切换）
- `templates/decision_point.yaml`
- `templates/task_rule.yaml`
- `templates/task_relation.yaml`

---

## 11. 约束备忘
- 每对象一个 yaml；atom 内嵌 parameter_bindings；TaskRule/DecisionPoint 挂 owner_task_ref；TaskRelation 只内嵌在父 task（见 §3，不建独立文件）。
- 中文 task_category（"配置"）必须转英文枚举（`configure`）。
- 所有 status 初始为 draft/inferred，**不预设 active**（active 只由人工校准赋予）。
- 跨网元/跨版本不合并，演进靠 diff。

---

## 12. 跨场景流程与场景闭包层

> 本 Skill 建 canonical Task 层（`ConfigTask/`）；场景层（业务闭包）在人+Agent 协同下**消费**它。本节定两者接口与流程定位。**不引入新对象类型或字段**——对象模型仍以 §2 + 根目录 `改进后三层图谱定义.md` §4-§8 为准。

### 12.1 MVP = 单个方案
- 不管什么图谱/场景，工作单元始终是一个 `ConfigurationSolution`（方案）。规模靠"加方案"线性扩展。
- 方案间复用由 Task 层承载（§7.1 双闸 + 改进后 §4.5.2 合并），方案本身不互相耦合。
- 本 Skill 的"逐特性 pass"（§5）是方案内部的下沉路径之一；方案也可直接组合已有 feature-task / compound-task / atom-task。

### 12.2 拆解选择顺序（自顶向下；对应 §4.1 强制 anchor）
给定一个方案或上层 task 往下拆，按顺序选子节点粒度：

1. 能映射到已有 Feature？ → `feature-task`（`feature_ref`）
2. 否则，几条专属命令的组合？ → `compound-task`（再递归）
3. 否则，单命令？ → `atom-task`（叶子）

- feature-task 继续往下拆（"特性即小方案"，走同一 SOP）；叶子恒为 atom-task，缺命令按 §6 终止。

### 12.3 业务顶层（人+Agent，场景级，不在本 Skill 可写范围）
- BD→NS→CS 由人+Agent 一次性定，落 `业务图谱体系/{场景}/business/`（jsonl：BD/NS 静态对象 + CS 定义）。
- §0 的可写边界（`ConfigTask/`）不变；业务顶层产物（CS 定义）作为方案 MVP 的**输入契约**喂给本 Skill。

### 12.4 场景闭包层
- **Solution Task 本体在 `ConfigTask/`**（§0 可写范围、§2.2 的 `3-` 前缀、按 `{NF}/{version}` 隔离）。
- **场景闭包** = 薄引用层，落 `业务图谱体系/{场景}/closures/cs-{id}-closure.yaml`：组合跨 NF 的 Solution Task ID + 跨侧场景级 DP/Rule + 指向 `docs/` 的 md 残留。
- 闭包**不重抽** canonical；其 DP/Rule 优先 **ID 引用** canonical（`owner_task_ref` 指回 `ConfigTask` 的 Solution Task），仅跨侧无 canonical 宿主时才内嵌。
- md 残留（design_intent 叙述、端到端走查、证据原文、合并评估、审查报告）落 `业务图谱体系/{场景}/docs/`。

### 12.5 现有 md 场景的迁移（一次性，按方案增量）
现有 `业务图谱体系/{场景}/three-layer-graph/*.md`：
- CS → `business/cs-definitions.jsonl` + ConfigTask 里对应 Solution Task；
- 可投影的 DP/BR/SO 按 §8 投影为 Solution Task 的 DecisionPoint/TaskRule（BR→TaskRule 是语义映射，非搬运）；
- 不可投影的纯业务叙述 → `docs/`；
- 手写的 feature/command/task 重复内容迁入结构化资产后，降级为只读视图或废弃。
