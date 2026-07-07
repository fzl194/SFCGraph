# ConfigTask 抽取架构审视报告

> 日期：2026-06-27
> 对照基准：**`ConfigTask/CONFIGTASK_SCHEMA.md` v0.1（§3 对象总表 = 3 个对象：ConfigTask / TaskRule / DecisionPoint）+ 实例（内容计费 5 task / IPSec 1 task 多场景）**
> 上层 `业务图谱体系/三层图谱Schema-最终版-v0.1.md` 不作为本层评估基准（那是业务/特性/命令/证据四层全集的视图，含 6 个对象；本层只关心其中 3 个）
> 审视范围：`builder/steps/*.py` 全 11 步 + 真实产物（UDG 20.15.2 已产出 2 task）
> 目标：判断当前抽取架构支持了什么、差什么、是否合适

---

## 0. TL;DR

| 维度 | 结论 |
|---|---|
| **支持的字段** | §4 ConfigTask 必选字段 100% 覆盖（task_id / task_logical_name / task_goal / task_summary / commands / source_evidence_ids）；可选 task_category / nf / version / business_domains / status 全有 |
| **支持的子结构** | `commands[].parameters[]` 三类（fixed/variable/reference）+ variable_source 四值 100% 抽取；reference / decision_driven source_ref 留白（设计如此） |
| **缺失** | **2 个独立对象未抽取**：TaskRule / DecisionPoint（pipeline.yaml 末尾 3 步 extract_rules / verify_rules / assemble 全是桩 `print("(待实现)")`，对应只产 1/3 对象）|
| **架构评估** | **不完整**：本层 Schema §3 明确 3 类对象，当前只产 1 个。TaskRule 实例佐证 4 类规则已在样例中明确（binding/relative_value/conditional_param/consistency），DecisionPoint 在 2 个样例中都有结构化实例——抽取入口未建 |
| **横向关系** | 上层特性层 `Feature decomposes_to ConfigTask` 由上层做，本层不在评估范围；FeatureRule.constrains_task 上层做 |

---

## 1. 当前架构支持的字段（vs `CONFIGTASK_SCHEMA.md` §4 + §7）

### 1.1 ConfigTask 必选字段检查（UDG 真实产出）

抽 `data/UDG/20.15.2/config_tasks.jsonl` 第一条做字段级体检（对照 `CONFIGTASK_SCHEMA.md §4 ConfigTask 字段表 + §7 关系存储方向）：

| Schema §4 字段 | 当前产出 | 来源步 | 评估 |
|---|---|---|---|
| `task_id`（`UDG@20.15.2@ConfigTask@00001`）| ✅ | merge_fields.parse_output L104 | 满足 |
| `task_logical_name` | ✅ "配置计费三件套(URR-URRGROUP-PCCPOLICYGRP)" | merge_fields Agent 输出 | 满足 |
| `nf` / `version` | ✅ | parse_output L110-111 | 满足 |
| `task_goal` | ✅ | Agent 输出 | 满足 |
| `task_summary` | ✅ | Agent 输出 | 满足 |
| `commands` | ✅ 3 条 ADD URR/URRGROUP/PCCPOLICYGRP | merge_fields Agent | 满足 |
| `source_evidence_ids` | ✅ 19 个 doc_path | finalize_fields L52-63 | 满足 |

注：本层 `CONFIGTASK_SCHEMA.md §4` 字段表中 `task_scope_type` / `input_contract` / `output_contract` / `task_category` / `status` 都是**非必选**（"否"列），已检查的 7 个必选项全部 100% 覆盖。`status` 硬编码 "active"（`parse_output` L115）。

### 1.2 ConfigTask 可选字段

| 字段 | 当前产出 | 评估 |
|---|---|---|
| `nf` / `version` | ✅ | 满足 |
| `task_category` | ✅ "配置"（硬编码 L114）| 仅覆盖配置类，缺"验证类"分支（runbook 提到"验证类来自调测文档，下一步纳入"）|
| `commands[].command_ref` 全键 | ✅ `UDG@20.15.2@MMLCommand@ADD URR` | finalize_fields L41-50 补齐 |
| `commands[].parameters[].parameter_ref` 全键 | ❌ **裸名**（URRNAME 等）| **缺**：finalize_fields 注释明写"留给内网程序"。当前 schema 要求 `UDG@20.15.2@CommandParameter@ADD URR:URRNAME` |
| `binding_type` / `variable_source` / `fixed_value` | ✅ | merge_fields Agent 输出 + verify_merge 校验 |

### 1.3 中间态字段（设计明确，不算缺）

- `_decision_points` / `_split_notes`：merge_fields Agent 顺手产出（前瞻到 TaskRule/DecisionPoint 抽取），finalize_fields 加 `_` 前缀区分中间态。
- `cluster_id` / `source_cluster_members` / `extraction_method` / `business_domains`：pipeline 自有元数据，承载关键链路。
- `raw_steps_text`：用户明确"弃用"，已从 schema 删除。

---

## 2. 缺失项（vs `CONFIGTASK_SCHEMA.md` §3 对象总表 + 实例佐证）

### 2.1 **TaskRule 抽取入口未建**（P0 缺）

`extract_rules.py` 不存在。pipeline.yaml 第 13/22 步 `extract_rules` 是桩，verify_rules / assemble 同为桩。

`CONFIGTASK_SCHEMA.md §5 TaskRule` 必选字段 + §5 规则类型表 4 类 + 实例佐证（内容计费 4 条 + IPSec 2 条）：

| rule_type | 实例出处 | 抽法 |
|---|---|---|
| `binding_rule` | TaskRule@00003（FLOWFILTER 必须绑定 filter/l7filter 否则 Rule 无效）| 跨命令引用→值未填→警告 |
| `relative_value_rule` | TaskRule@00004（RULE 优先级：L34<L7<any=65000）| 跨 member 同一参数取值规律 → 相对约束 |
| `conditional_param_rule` | TaskRule@00001/00002（URRGROUP 必须配在线+离线 URR）| 同一 task 内 conditional_param+配置语境 |
| `consistency_rule` | TaskRule@00001（IPSec VNRS↔IPsec 微服务双配）/ 00002（PSK 必填）| 跨 command 配对、删改配对 |

**当前 merge_fields Agent 已包含规则信号**：`_decision_points` 字段内容已经是 DecisionPoint 的种子；`_split_notes` 已包含"使能前置/可选后续"等 TaskRule 信号。可直接基于现有 config_tasks.jsonl + cluster 证据做规则抽取（不需要回读 md）。

**抽取路径建议**：
- 输入：`config_tasks.jsonl` + `task_clusters_enriched.jsonl`（含 param_rows 的 obtain_method/note 字段，规则证据主要在这里）
- 输出：`task_rules.jsonl` + `decision_points.jsonl`（独立文件，per-task）
- Agent 步：per-cluster 写 prompt，输出回填（同 merge_fields 模式）

### 2.2 **DecisionPoint 抽取入口未建**（P0 缺）

`CONFIGTASK_SCHEMA.md §6 DecisionPoint`：跨层通用决策结构（`owner_layer` 可为 business/feature/task，本层实例=task）。一个决策点 = 一个问题 + 若干分支，每分支扇出**多个影响**，影响可落在任意层的任意对象上。

`options[].impacts[]` 4 维（target_layer / target_ref / effect_type / effect_detail）—— content 计费实例有 2 个 DecisionPoint（计费方式选择 3 option × 4 impacts，过滤模式选择 4 option），IPSec 实例有 1 个 9 option DecisionPoint。

**当前 _decision_points 是文本数组**（5 条短描述），不是结构化对象。需要：
- 把 `_decision_points` 文本拆解成 `decision_question + option_set + impacts[]`
- 跨 member 取值差异 → 判定 option
- 关联的 command_ref / parameter_ref → target_ref 全键

### 2.3 **顺序承载：本层 schema 不引入编排边对象**

上层 `三层图谱Schema-最终版-v0.1.md §10.5` 含 `TaskCommandOrderEdge`，但本层 `CONFIGTASK_SCHEMA.md §3 对象总表` 只列 3 个对象（ConfigTask / TaskRule / DecisionPoint），**明确不含编排边对象**。本层用 `commands` 有序列表承载顺序（`CONFIGTASK_SCHEMA §1.8` 设计原则第 8 条："命令顺序 = commands 有序列表，不单建编排边对象"）。

**评估**：本层 schema 设计如此，**不是抽取架构缺**。带条件的顺序约束（如 REFRESHSRV 必须最后执行）目前未独立表达，淹没在 `_split_notes` 文本里——需要时应补到 TaskRule（按本层归口，rule_type 加 `sequential_constraint`，不开新对象）。

### 2.4 **parameter_ref 全键未补**（P1 缺）

`finalize_fields` L71 注释明写："留给内网程序"。当前 `commands[].parameters[].parameter_ref` 是裸英文名（URRNAME、URRID 等），不是 `UDG@20.15.2@CommandParameter@ADD URR:URRNAME`（`CONFIGTASK_SCHEMA.md §4 commands[].parameters[].parameter_ref` 明确要求全键格式）。

**影响**：下游消费方（如前端）无法跨文档 join 到命令图谱。**本步可补**——命令图谱 `command_parameters.jsonl` 在外网是否可用？需检查 `command_graph_dir` 下文件清单。

### 2.5 **source_ref 未填**（P1 缺）

- `decision_driven` → 应填 DecisionPoint 全键
- `reference` → 应填源 command.参数

`finalize_fields` L71 同上不补。当前两个 source_ref 都是空。**依赖 TaskRule/DecisionPoint 抽取先建**——有了 DecisionPoint 全键才能填 decision_driven 的 source_ref。

### 2.6 **task_scope_type 未抽**（P2 缺）

**`CONFIGTASK_SCHEMA.md §3 对象总表` 含 `task_scope_type` 字段（枚举 `feature_specific / cross_feature / generic`，对应 §1.4 设计原则第 4 条 "task 不强制隶属于某个 Feature"）**。当前用 cluster.member_count 做侧面推断（跨多 member=可能 cross_feature），未独立字段。**优先级低**——前端展示场景能用，业务推理也能从 member 数推。

---

## 3. 架构评估

### 3.1 链路 8 步设计合理

```
scan → extract_steps → split_tasks(Agent) → verify_split
     → cluster → enrich → merge_fields(Agent) → finalize_fields → verify_merge
     → extract_rules(Agent, 桩) → verify_rules(桩) → assemble(桩)
```

**优点**：
- 数据隔离（`data/{nf}/{version}/`，已修复）
- Agent 步 prep/pause/ingest 模型（半自动外网可跑、内网换 LLM 即可）
- enrich 步把证据内联进 cluster member，merge_fields 不读 md——既保证 LLM 推理有原文，又防止 md 二次散落
- 命令图谱 command_ref 全键的补齐交给 finalize_fields（一次过，幂等）

**可议**：
- verify_split 是 split_tasks 的下游，verify_merge 是 merge_fields 的下游，**verify_rules 没有同位置的 extract_rules 上游**——命名/位置略不一致
- enrich 后输出文件 decoupled 到 `task_clusters_enriched.jsonl` 是对的，但 cluster 产物（`task_clusters.jsonl`）和 enriched 同时存在，后续 extract_rules 应读哪个？建议读 enriched（param_rows 还在）

### 3.2 数据形态抽样（UDG 已跑出的 1 条）

```
task_id: UDG@20.15.2@ConfigTask@00001
cluster_id: cluster-003
task_logical_name: 配置计费三件套(URR-URRGROUP-PCCPOLICYGRP)
task_goal: 配置内容/业务计费的使用量上报规则... (LLM 扩写)
task_summary: ADD URR... ADD URRGROUP... ADD PCCPOLICYGRP... (LLM 扩写)
nf/version: UDG / 20.15.2
business_domains: ["计费"]
commands: 3 条命令, 15 个参数, 全部 binding_type 枚举正确
task_category: "配置" (硬编码)
status: "active"
source_cluster_members: 19
extraction_method: "inline_enriched"
source_evidence_ids: 19 个 doc_path (来自 cluster member.doc_path)
_decision_points: 5 条文本描述
_split_notes: 长文本（前置/可选后续/同一task不拆分理由）
```

**问题**：
1. `_decision_points` 是文本数组，不是 `CONFIGTASK_SCHEMA.md §6 DecisionPoint` 要求的结构化对象（缺 `decision_question` / `option_set` / `impacts[]`）。**这是当前最严重的 schema 不符**。
2. `task_category` 硬编码为"配置"，无法覆盖"验证类"task（runbook 第 9.5 行提到但未实现）。
3. `task_goal / task_summary` 是 LLM 扩写文，不是原始 step 摘抄——可读性好但偏离原始证据。

### 3.3 横向接口（上/下/横向）

| 接口 | 状态 |
|---|---|
| 下方接命令图谱 | ✅ command_ref 全键已补（finalize_fields），但 parameter_ref 全键未补 |
| 下方接特征/特性图谱 | ❌ `Feature decomposes_to ConfigTask` 边未建；用 `task_logical_name` 跨层锚点已定（schema §2）|
| 横向跨网元/版本 | ❌ 当前不跨版本/跨网元合并（schema §2 明确"当下不去重合并，演进靠 diff"）—— 满足 |
| 横向跨簇 | ⚠️ cluster_id 留存可追溯，但同 task_logical_name 是否跨簇合并由 cluster 算法决定（Jaccard > 0.7 + core_commands 精确匹配）|

---

## 4. 当前架构 vs 实例要求

| 实例 | 要求 | 当前架构支持 |
|---|---|---|
| 内容计费 5 task | task 拆分 + 命令聚合 + 命令顺序 + source_evidence_ids | ✅ 全部 |
| 内容计费 4 TaskRule | 4 类规则实例化 | ❌ 未抽取（信号已在 _decision_points/_split_notes）|
| 内容计费 2 DecisionPoint | 结构化决策 + option × impact 跨层扇出 | ❌ 未抽取（信号已在 _decision_points）|
| IPSec 1 task + 9 场景 | 1 簇 9 member → 1 task，场景由 DecisionPoint 表达 | ✅ 聚类已正确合并 9 变体；DecisionPoint 未结构化 |

---

## 5. 建议（按优先级）

### P0（必须做，否则不算 v1.0 完成）

1. **建 extract_rules step**：
   - 输入：`config_tasks.jsonl` + `task_clusters_enriched.jsonl`（含 param_rows）
   - Agent 步：per-task，写 prompt 到 `data/agent_prompts/extract_rules/<task_id>.txt`
   - 输出：解析到 `task_rules.jsonl` + `decision_points.jsonl` 两个独立文件
   - 复用 merge_fields 的 prep/pause/ingest 模型（pipeline 已支持 `@step(agent=True)` + PAUSE）

2. **建 verify_rules step**（不能继续是桩）：
   - HARD：task_rule_id / task_ref 必填且 task_ref 存在；decision_id / owner_ref 必填；rule_type / effect_type 枚举合法
   - WARN：缺 owner_ref 路由；缺 source_evidence_ids；decision option 空

3. **补 task_scope_type 字段**：在 merge_fields Agent 输出 schema 中加，verify_merge 校验（`CONFIGTASK_SCHEMA.md §3 对象总表` 含此字段，按 §1.4 设计原则 task 不强制隶属 Feature，需要此字段承载 cross_feature 关系）

### P1（内网可补，做了对前端更友好）

4. **finalize_fields 补 parameter_ref 全键**：检查 `command_graph_dir/command_parameters.jsonl` 在外网是否可用；若可，加 ④ 同 command_ref 一样的全键化逻辑
5. **source_ref 回填**：依赖 TaskRule/DecisionPoint 全键，extract_rules 之后做一次后处理补齐

### P2（架构层面思考）

6. **task_category 覆盖验证类**：在 split_tasks prompt 加"验证类步骤请 candidate_desc 标[验证]"，merge_fields 识别后输出 `task_category: "验证"`（不能硬编码）

7. **task_goal / task_summary 形态**：考虑加 `_raw_task_goal` / `_raw_task_summary` 留原始 step 摘抄，权威字段用 LLM 扩写——目前 LLM 扩写文本无法回溯到具体步骤

8. **带条件顺序约束**：must_be_last（REFRESHSRV）/must_be_first 等条件顺序约束目前淹没在 `_split_notes` 文本里。如业务提出需要结构化承载，按本层归口补到 TaskRule（rule_type 加 `sequential_constraint`，不是新建 TaskCommandOrderEdge 对象——本层 schema 只 3 个对象，不引入编排边）

---

## 6. 文件变更清单（建议落档后执行）

| 操作 | 文件 | 说明 |
|---|---|---|
| NEW | `builder/steps/extract_rules.py` | per-task Agent 步，产出 task_rules.jsonl + decision_points.jsonl |
| NEW | `tests/test_extract_rules.py` | prep/ingest 单测（参照 merge_fields 测试）|
| MODIFY | `builder/steps/verify_rules.py` | 当前是 stub，补真实校验逻辑 |
| MODIFY | `builder/steps/assemble.py` | 当前是 stub，输出 `assets/{nf}/{version}/` 拆分文件（task/rules/decisions） |
| MODIFY | `builder/agent/prompts.py` | 加 EXTRACT_RULES_PROMPT（per-task，包含 task_id/commands/parameters/param_rows/signals）|
| MODIFY | `builder/steps/finalize_fields.py` | 补 parameter_ref 全键（若 command_parameters.jsonl 外网可用）|
| MODIFY | `CONFIGTASK_SCHEMA.md` | 标记 `_decision_points` 当前是"DecisionPoint 抽取的种子文本"，下一步需结构化 |

---

## 7. 一句话总结

> **链路 + ConfigTask 单对象抽取成熟可用**，但 **`CONFIGTASK_SCHEMA.md §3 对象总表` 要求 3 类对象（ConfigTask / TaskRule / DecisionPoint），当前只产 1 个**——TaskRule/DecisionPoint 抽取入口未建是当前最大缺口。链路已为此铺好（enrich 内联 param_rows、finalize_fields 全键化、Agent 步 prep/pause/ingest 模板），补 extract_rules + verify_rules 两步即可凑齐本层 v0.1。