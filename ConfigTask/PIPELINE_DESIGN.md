# ConfigTask 抽取 Pipeline 设计

> 版本：v1.0（基于 Codex 提案 + 5 处实证修正）
> 日期：2026-06-26
> 替代：旧的"抽取指令-ConfigTask对象.md"和"规则pipeline说明.md"（已删）
> 实证基础：`语料精读追踪.md`（4 轮 40 篇 UDG 精读 + 三视角交叉验证）

---

## 目标

从 659 份配置文档（UDG 165 + UNC 494）中：
1. 发现 ConfigTask 候选（每份文档内的 task 分段）。
2. 跨文档归并（相同意图+命令骨架 → 同一个 task）。
3. 在簇级深抽参数/TaskRule/DecisionPoint（汇总所有配置案例 + 命令图谱 notes + 特性概述）。

**核心原则**（来自实证）：
- task 是跨特性复用的原子，不是单特性产物。
- 命令图谱 notes 是约束的权威源（激活文档是辅助）。
- 固参/变参只有跨案例聚合才能判定（单特性内的"fixed"可能是 decision_driven）。
- Agent 输入追溯到原始 md（不只看结构化字段）。

---

## 架构总览

```text
659 份配置文档
  │
  ▼ Step 0：语料预筛（规则）
  │  过滤 + 标记特殊类型 → doc_manifest.filtered.jsonl
  │
  ▼ Step 1：抽步骤三元组（规则）
  │  每份文档 → [(step_num, step_desc, commands[])] + 原文切片 + doc_path
  │
  ▼ Step 2：单文档内切 Task 候选（规则 or Agent）
  │  双模式：有操作流程→规则切 / 无操作流程→Agent 切
  │  → task_candidates.jsonl
  │
  ▼ Step 3：跨文档聚类（Agent 归一化 + 算法聚类）
  │  3a Agent 归一化 candidate_desc → 标准意图
  │  3b 按（标准意图 + 核心命令骨架）聚类
  │  → task_clusters.jsonl
  │
  ▼ Step 4：每簇深抽 ConfigTask（Agent）
  │  Agent 读：簇内所有成员原始 md + 步骤切片 + 命令骨架
  │  → config_tasks.jsonl
  │
  ▼ Step 5：每簇深抽 TaskRule（Agent + 命令图谱）
  │  权威源：命令 notes > 激活文档 > 参数表
  │  → task_rules.jsonl
  │
  ▼ Step 6：每簇深抽 DecisionPoint（Agent）
  │  文档内显式决策 + 跨文档聚合决策
  │  → decision_points.jsonl
  │
  ▼ Step 7：组装最终资产
    config_tasks.full.jsonl + task_rules.jsonl + decision_points.jsonl
```

---

## Step 0：语料预筛（规则）

**做什么**：从 659 份文档中筛出真正适合抽 task 的，标记特殊类型。

**怎么做**：
- 保留有"操作步骤"段的文档（已有 `corpus_manifest.csv` 的 `has_operation_steps=True`）。
- 标记特殊类型：
  - `standard`：标准配置文档（大多数）。
  - `license_only`：只有 SET LICENSESWITCH（如 GWFD-020451）。
  - `difference_only`：差异配置，标 `depends_on_baseline`（如 GWFD-020307 "参考部署UPF"）。
  - `no_steps`：无明确步骤编号（极少，标记跳过）。

**产出**：`data/doc_manifest.filtered.jsonl`

**现有代码**：`scripts/scan_corpus.py` 已做语料扫描。补充特殊类型标记。

---

## Step 1：抽步骤三元组（规则）

**做什么**：从每份文档的"操作步骤"段抽 `(step_num, step_desc, commands[])` 三元组。

**怎么做**：
- md_reader 切出"操作步骤"段（已实现）。
- 按 `^\d+\.` 切步骤，每步抽描述（步骤标题文本）+ 命令名（正则 `(ADD|SET|MOD|DEL|...) \w+`）。
- 保留原文切片（step 的完整文本，含子步骤和说明块）。
- 保留 doc_path + feature_id。

**产出**：`data/doc_steps.jsonl`
```json
{
  "doc_path": ".../部署UPF_28493406.md",
  "feature_id": "GWFD-020301",
  "doc_type": "standard",
  "steps": [
    {"step_num": 1, "step_desc": "配置使用量上报规则组属性", "commands": ["ADD URR", "ADD URRGROUP"], "raw_text": "1. 配置使用量上报规则组属性。\n  a. 配置URR。\n **ADD URR**..."},
    {"step_num": 2, "step_desc": "配置PCC策略组", "commands": ["ADD PCCPOLICYGRP"], "raw_text": "..."}
  ]
}
```

**关键**：**不切 task 边界**（Step 2 做）、**不抽参数**（Step 4 做）。这步只产结构化步骤。

**现有代码**：`builder/core/commands.py` 的 `parse_step_commands` + `steps_text_for_range` 可复用。新增 step_desc 抽取。

---

## Step 2：单文档内切 Task 候选（规则 or Agent）

**做什么**：在每份文档内部，把步骤列表切成 task candidate。

**双模式**（★ 实证修正 R1）：

| 条件 | 模式 | 信号 |
|---|---|---|
| 文档有"操作流程"段（~42 份） | **规则切** | phase→step 映射（`flow_parser` + `cut_tasks_by_phases` 已实现）|
| 文档无"操作流程"段（~617 份） | **Agent 切** | 读 step_desc 语义 + 命令链 + 原文上下文 |

**Agent 切的输入**：step 三元组列表 + 原文操作步骤段。
**Agent 切的输出**：task candidate 列表，每个含 step_range + candidate_desc + commands。

**切分原则**：
- 一个 candidate = 一个连贯配置动作（产出一个可命名的配置对象集）。
- 不把纯收尾命令（REFRESHSRV / SPECURRGRPLIST）轻易切成独立 task——并入前段。
- 差异配置文档（`difference_only`）：Agent 读时**需同时读基线文档**补充上下文（★ 修正 R3）。

**产出**：`data/task_candidates.jsonl`
```json
{
  "doc_path": ".../部署UPF_28493406.md",
  "feature_id": "GWFD-020301",
  "candidate_id": "GWFD-020301#cand-01",
  "step_range": [1, 2],
  "candidate_desc": "配置业务费率",
  "commands": ["ADD URR", "ADD URRGROUP", "ADD PCCPOLICYGRP"],
  "boundary_source": "flow"  // or "agent"
}
```

**现有代码**：`flow_parser.py` + `cut_tasks.py` + `cut_boundaries.py`（规则模式）可复用。Agent 模式待实现。

---

## Step 3：跨文档聚类（Agent 归一化 + 算法聚类）

**做什么**：把不同文档里的 task candidate 归并成"同一个 ConfigTask"。

**3a：Agent 归一化意图**（★ 修正 R2）
- Agent 读每个 candidate 的 `candidate_desc` + `commands` → 归一化为**标准意图标签**。
- 例如："配置过滤条件" / "配置流过滤器" / "绑定过滤器" → 归一成 "配置过滤规则"。
- 这是语义任务，必须 Agent 做（不是规则匹配）。

**3b：按三层键聚类**
1. **主键**：归一化后的标准意图。
2. **次键**：核心命令骨架（去掉可选命令 SET LICENSESWITCH / SET REFRESHSRV 后的命令集）。
3. **弱特征**：可选命令差异不拆簇；场景分支差异留给 DecisionPoint。

**聚类判据**：意图相近 + 核心骨架高度相似 = 同簇。

**产出**：`data/task_clusters.jsonl`
```json
{
  "cluster_id": "UDG@20.15.2@cluster-014",
  "normalized_task_name": "配置过滤规则",
  "members": [{"candidate_id": "GWFD-020301#cand-02", "doc_path": "...", "feature_id": "..."}, ...],
  "core_commands": ["ADD FILTER", "ADD L7FILTER", "ADD FLOWFILTER", "ADD FLTBINDFLOWF", "ADD PROTBINDFLOWF"],
  "optional_commands": ["SET REFRESHSRV"]
}
```

---

## Step 4：每簇深抽 ConfigTask（Agent）

**做什么**：对每个簇，汇总所有配置案例，产出完整 ConfigTask。

**Agent 输入**（★ 修正 R5：必须含原始 md）：
- 簇内所有成员的**原始 md 路径**（Agent 追溯原文）。
- 簇内所有成员的步骤切片。
- 核心命令骨架 + 可选命令。
- 命令图谱 mml_commands.jsonl 中对应命令的 notes + parameter_description。

**Agent 抽取**：
- `task_logical_name`：簇的归一化名（Step 3 已产，Agent 确认/细化）。
- `task_goal` / `task_summary`。
- `commands`：有序命令列表 + 每命令的参数（从命令图谱 + 所有案例的参数表 + 脚本合并）。
- 参数 `binding_type`：
  - `reference`：来自已配置对象（命令图谱"配置原则"字段）。
  - `fixed`：**跨所有案例零例外地稳定不变**（★ 修正 R4）。
  - `variable`：其余。如果跨案例变化明显 → 标 `decision_driven`（可能需要 DecisionPoint）。

**参数来源**（命令图谱权威 3 值 + 激活文档 hint）：
- 命令图谱"数据来源"：本端规划 / 全网规划 / 对端规划。
- 激活文档"获取方法"：降级为 hint（不直接信任，有主观性）。
- "已配置数据中获取" → 映射到命令图谱"配置原则"字段 → reference 关系。

**产出**：`data/config_tasks.jsonl`

---

## Step 5：每簇深抽 TaskRule（Agent + 命令图谱）

**做什么**：抽 task 内部的跨命令约束。

**权威源优先级**（实证确定）：
1. **命令图谱 notes**（最高权威——技术化、具体、强约束原文）。
2. 操作步骤说明块（`> 说明`）。
3. 参数表说明列。
4. 前提条件段。
5. 操作流程段 blockquote（IPSec 双配原则等）。

**Agent 输入**：簇内文档 + 命令图谱 notes + 特性概述。

**TaskRule 类型**（实证 10+ 类）：
- `binding_rule`（FLOWFILTER 必须绑定 filter）
- `relative_value_rule`（RULE 优先级相对约束）
- `conditional_param_rule`（需计费→URRGROUPNAME 必填）
- `consistency_rule`（URRGROUP 在线+离线同时绑定）
- `license_required` / `refresh_after_l7filter` / `refreshtype_binding`
- `param_formula_constraint`（CIR=0.5*PIR）
- `enum_no_subset`（WLR 不能拆 WLR_SP）
- `idempotent_skip`（LOD SIGNATUREDB 已加载则跳过）

**产出**：`data/task_rules.jsonl`

---

## Step 6：每簇深抽 DecisionPoint（Agent）

**做什么**：抽 task 的配置变体和决策分支。

**两类决策**：

| 类型 | 来源 | 例子 |
|---|---|---|
| **文档内显式决策** | 单份文档内的场景/可选/条件 | 在线/离线、IPv4/IPv6、主备、探测方式(PING/DNS/Tracert) |
| **跨文档聚合决策** | 簇内不同案例之间的参数差异 | POLICYTYPE=PCC/ADC/SMARTREDIRECT、METERINGTYPE=VOLUME/DURATION/EVENT |

**Agent 输入**：簇内所有案例的参数表 + 脚本 + 命令图谱。

**DecisionPoint 结构**（options[].impacts[]，见 CONFIGTASK_SCHEMA §6）：
- 每个 option = 一个分支。
- impacts = 该分支影响哪些参数/命令/task。

**产出**：`data/decision_points.jsonl`

---

## Step 7：组装最终资产

**做什么**：把 ConfigTask / TaskRule / DecisionPoint 组装成任务层正式资产。

**产出**：
- `data/assets/{nf}/{version}/config_tasks.full.jsonl`
- `data/assets/{nf}/{version}/task_rules.jsonl`
- `data/assets/{nf}/{version}/decision_points.jsonl`

**关系存储**（schema §7）：
- TaskRule.task_ref → ConfigTask（子侧 FK）。
- DecisionPoint.owner_ref → ConfigTask（子侧 FK）。
- ConfigTask.commands → MMLCommand / CommandParameter（字段）。
- DecisionPoint.options[].impacts[] → 任意层对象。

---

## 与 Codex 原方案的 5 处实证修正

| # | Codex 原方案 | 修正（实证依据）|
|---|---|---|
| R1 | Step 2 信号列了 5 种 | **补操作流程**：有操作流程的文档（42 份）用规则切（最可靠），无的用 Agent 切 |
| R2 | Step 3"意图归一化"未说怎么做 | **明确 Agent 做**：3a 步 Agent 归一化 candidate_desc → 标准意图 |
| R3 | difference_only 只标记 | **补充处理**：Agent 切 candidate 时需读基线文档补上下文 |
| R4 | Step 4 "fixed = 跨案例稳定不变" | **修正阈值**：有任何一个案例不同 → decision_driven（零例外才 fixed）|
| R5 | Step 4/5/6 Agent 读"簇内文档" | **强调读原始 md**：不只读三元组，Agent 输入必须追溯原始文档 |

---

## 与现有代码/资产的关系

| 现有资产 | 在新 pipeline 中的角色 |
|---|---|
| `scripts/scan_corpus.py` | Step 0 语料预筛的基础 |
| `builder/core/md_reader.py` | Step 1 切操作步骤段 |
| `builder/core/commands.py` | Step 1 抽命令 + step_desc |
| `builder/core/flow_parser.py` + `cut_tasks.py` | Step 2 规则模式（有操作流程的文档）|
| `builder/core/csv_loader.py` | Step 0 读 CSV |
| `builder/steps/*` | Step 2 的 cut_boundaries step（规则模式）可复用 |
| `data/corpus_manifest.csv` | Step 0 输入 |
| `data/task_example_docs_{UDG,UNC}.csv` | Step 0 输入（已按网元拆分）|
| `CONFIGTASK_SCHEMA.md` | 对象/字段/关系定义（variable_source 待按交叉验证修正）|
| `语料精读追踪.md` | 实证依据（参数分类/task 模式/TaskRule/交叉验证修正）|
| `样例-内容计费/IPSec` | Step 4 验收基准 |

---

## 实施路线

| 阶段 | 内容 | 方式 |
|---|---|---|
| **Phase 1** | Step 0 + Step 1（语料预筛 + 抽步骤三元组） | 规则代码，复用现有 md_reader/commands |
| **Phase 2** | Step 2（单文档切 candidate） | 规则模式复用 + Agent 模式实现 |
| **Phase 3** | Step 3（跨文档聚类） | Agent 归一化 + 算法聚类 |
| **Phase 4** | Step 4-6（簇级深抽） | Agent 逐簇深抽 |
| **Phase 5** | Step 7（组装）+ 验收 | 规则组装 + 对照样例 |
