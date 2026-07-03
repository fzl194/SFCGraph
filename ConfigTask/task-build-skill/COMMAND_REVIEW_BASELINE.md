# 命令级审查基线（COMMAND_REVIEW_BASELINE）

> 对象：UDG@20.15.2 命令层 atom（187 个）+ 每个 atom 挂的 TaskRule / DecisionPoint。
> 性质：**重构/校准**（把已有的 atom + 其 rule + 其 DP 改对），命令级完整性 + 准确性。
> 权威 schema：根目录 `改进后三层图谱定义.md` §4-§8；构建准则：同目录 `SKILL.md`。
> 生成于 2026-07-02，基于与用户对齐的 3 项决策。

---

## 0. 为什么做命令级审查（背景）

P1 步骤层重构（特性→步骤→命令）已闭环 90 特性，但审查视角是**特性**——发现不了**单命令**自身的问题：
- **参数完整度**：atom 只绑了建它时用到的参数，命令原始 md 的其余"通用配置"参数可能漏绑（例：ADD URR 现绑 5 个，命令有 12 个参数，DFTQUOTA*/CFGDOMAINNAME 等通用参数未绑）。
- **参数准确性**：`variable_source` / `requiredness` / `binding_type` 是否对齐命令原始 md 的"数据来源/必选可选/取值范围"。
- **rule/DP 投影**：命令原始 md 的 notes（规格/唯一性/上限）是否投影成 atom rule；conditional_required 是否投影成 atom DP。
- **跨特性一致性**：同一命令在不同特性里配法分叉（如 URRNAME 内容计费=全网、在线计费=本端）是否正确升为 `decision_driven`。

特性级审查（SKILL §8.1）覆盖不到这些——本基线补这个缺口。

---

## 1. 审查单元（per command）

**一个命令 = 一个审查单元**，同步审视三件事（不割裂）：
1. 该命令的 **atom task**（`tasks/task-0-NNNNN.yaml`，含 `parameter_bindings`）。
2. 该 atom **挂的 TaskRule**（`owner_task_ref = 该 atom`）。
3. 该 atom **挂的 DecisionPoint**（`owner_task_ref = 该 atom`）。

> **范围决策（已锁定）**：rule/DP 只看 `owner_task_ref = 该 atom` 的（不含 feature 挂的 dependency_rule 等）。
> 现状：187 atom 中仅 4 个有 atom-挂 rule、7 个有 atom-挂 DP——多数 atom 审查以参数绑定为主，有 rule/DP 的一并审。

---

## 2. 三个输入（每命令）

| 输入 | 内容 | 来源 |
|---|---|---|
| ① 已抽 yaml | atom task + atom 挂的 rule/DP | `task-assets/.../tasks/task-0-*.yaml` + `task_rules/rule-*.yaml` + `decision_points/dp-*.yaml` |
| ② 命令证据 md | 该命令在各特性激活/配置 md 里**怎么配**（数据规划表"获取方法"列、任务示例脚本）| `output/.../特性部署/特性指南/.../激活*.md`（由 `command-review-index.json` 的 `feature_evidence` 给出清单）|
| ③ 命令原始 md + 参数真相 | 命令功能/参数表（数据来源/必选可选/取值范围/默认）/notes（规格/唯一性/上限）/原始 md 路径 | `CommandGraph/data/assets/UDG/20.15.2/mml_commands.jsonl` 的 `parameter_description` + `notes` + `source_evidence_ids` |

---

## 3. 预处理工具（已建，两件）

### 3.1 审查索引（command-review-index.json）
**脚本**：`task-build-skill/scripts/build_command_review_index.py`
**产物**：`task-assets/UDG/20.15.2/command-review-index.json`（187 个审查卡，key=atom 短 id）
每卡汇总：atom+rule/DP、命令真相参数（精确解析）、已绑 vs 缺口、用该命令的特性清单。供**批次规划/统计**用。

### 3.2 结构化证据包（审查主输入）★
**脚本**：`task-build-skill/scripts/build_command_evidence.py`
**产物**：`task-assets/UDG/20.15.2/command-evidence/{atom短id}.md`（187 个，每命令一个）

每包 = 一个命令的全部审查资料，含**两部分**：
- **代码组织的上下文**（agent 直接审）：
  - ① atom + atom-挂 rule/DP（yaml 原文）
  - ② 命令真相（功能/notes/参数表：数据来源/必选/取值范围/默认，精确解析自 mml_commands.jsonl）
  - ③ 各特性的配置范式：数据规划表里**该命令的参数行**（精确匹配，参数/取值样例/获取方法/说明）+ 任务示例脚本里**该命令的代码行** + 操作步骤里**该命令的±2行上下文**
  - ④ 自动比对：已绑 vs 命令真相 vs 缺口 + 跨特性"获取方法"分布（提示 decision_driven）
- **原始 md 片段**：③ 的步骤上下文/脚本原文即原始 md 摘录；② 的参数表=命令原始 md 的结构化产物。

> 重建：`python task-build-skill/scripts/build_command_evidence.py UDG 20.15.2`
> 单命令预览：`python build_command_evidence.py UDG 20.15.2 --only 0-00001`

---

## 4. 审查清单（per command，逐条过）

### 4.1 参数完整度（核心）
- [ ] `missing_params_in_atom` 里的参数，**逐个判**是否"通用配置"：
  - 命令真相标 **必选** → 必须绑。
  - 在某特性激活 md 的**数据规划表里出现**（实际用到）→ 绑。
  - 命令真相标可选、且无特性用到（冷门）→ **不绑**（保持现状，避免臃肿）。
- > **参数门槛决策（已锁定）**：只绑通用配置参数（用到或必选），不要求全量。很多参数 UDG 场景用不到。

### 4.2 参数准确性（每条 binding 对照命令真相 + 特性 md）
- [ ] `variable_source`：对齐命令 md"获取方法"列（全网/本端/对端/已配置 → global/local/peer/reference）。跨特性来源分叉 → `decision_driven`（SKILL §4.5）。
- [ ] `requiredness`：对齐命令真相（必选/可选/条件必选）。
- [ ] `binding_type` + `value`：固定值写 fixed+value；余 variable；受决策写 decision_driven+decision_ref。
- [ ] `decision_driven` 的 binding：其 `decision_ref` 指向的 DP 存在，且该 DP 的 options 覆盖该参数取值。

### 4.3 rule/DP 投影（SKILL §4.4）
- [ ] 命令 `notes` 的规格/唯一性/上限 → 是否投影成 atom-挂 rule（`cardinality_rule` / `uniqueness_rule`）？漏的补。
- [ ] 命令 `parameter_conditional_required`（条件必选）→ 是否投影成 atom-挂 DP？漏的补。
- [ ] 现有 atom-挂 rule/DP 内容是否对齐命令真相（无臆造、无过期）。

### 4.4 证据与一致性
- [ ] atom `source_evidence_ids` 覆盖该命令的主要用法（不只有建 atom 时的那一个特性 md）。
- [ ] 跨特性配法分叉已用 DP/decision_driven 表达，未硬编码单一取值。

---

## 5. 审查流程（per command）

```
1. 读该命令的证据包：command-evidence/{atom短id}.md（已含 ①atom+rule/DP ②命令真相 ③各特性配置范式 ④比对）。
2. 按 §4 清单逐条审 → 直接改 atom/rule/DP yaml（命令级 refactor）。
   - 需要看完整原始 md 时：按证据包顶部的"原始命令 md"路径读 output/.../OM参考/命令/.../<命令>.md。
3. 自验：改后 atom 的 parameter_bindings 与命令真相 + 特性配置范式一致；rule/DP 投影完整；无 dangling ref。
4. 在 command-review-log.md 记一节（发现→改动→依据）。
```

> 证据包已经把"代码读 md + 抽上下文"做完了，审查者无需再逐个翻特性激活 md——只在需要更多上下文时回查原始 md。

---

## 6. 产出与记录

- **直接改**：`tasks/task-0-*.yaml`（atom）+ `task_rules/rule-*.yaml` + `decision_points/dp-*.yaml`。
- **审查日志**：`review/command-review-log.md`（每命令一节：发现 → 改动 → 依据）。结构同 SKILL §8.2。
- **批次进度**：`task-assets/UDG/20.15.2/command-review-tracker.md`（187 atom 逐行，标 ✅done/⏳，含命令名/参数数/有无 rule·DP）。
- 每批末重建 `command-review-index.json`（验证缺口收敛）+ `index.json`。

---

## 7. 批次划分（建议）

按命令功能域分批（语义连贯，便于跨命令对齐同族参数）。批次大小 ≈ 2 并行 Agent × N 命令。建议：

| 批 | 功能域 | 命令示例 | 预估 atom 数 |
|---|---|---|---|
| C1 | 计费/PCC（URR/URRGROUP/PCCPOLICYGRP/FILTER/RULE/USERPROFILE 等）| ADD URR, ADD RULE | ~25 |
| C2 | 接入/地址池/APN | ADD APN, ADD POOL, ADD SECTION | ~20 |
| C3 | 路由/接口/VPN | ADD OSPF, ADD INTERFACE, ADD VPNINST | ~30 |
| C4 | QoS/ACL/BWM | ADD MQCPOLICY, ADD ACLGROUP | ~25 |
| C5 | 业务感知/HTTP/过滤 | ADD L7FILTER, ADD HOST, ADD CFTEMPLATE | ~25 |
| C6 | 网管/IPSec/eDRX/其他 | ADD NTPSVR, ADD IKEPEER, SET IOTCAPABILITY | ~30 |

> 精确命令清单由 `command-review-index.json` 的 command_name 聚合得出，开批前生成。

---

## 8. 边界（硬约束）

- **可写**：仅 `ConfigTask/`。`改进后三层图谱定义.md`、`FeatureGraph/data/legacy/`、`CommandGraph/data/assets/`、`output/…产品文档…/` 只读。
- 不新建 atom（命令已全量存在）；不新建 compound/feature。
- 命令真相以 `mml_commands.jsonl` + 命令原始 md 为准；特性用法以激活 md 为准。冲突按 SKILL §0（schema 为权威）。
- 每命令审查独立可并行（atom 间无写冲突）；rule/DP 按 owner 归属，不跨 atom 改。
