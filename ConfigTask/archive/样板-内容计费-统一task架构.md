# 内容计费 GWFD-020301 — 统一 Task 架构真实样板

> 日期：2026-06-29
> 数据全部来自真实文档：`部署UPF_28493406.md`（4 场景数据规划表 + 11 步操作步骤 + 任务示例脚本）+ `CommandGraph/data/assets/UDG/20.15.2/mml_commands.jsonl`（命令图谱定义）
> 目的：用真实特性把 UNIFIED_TASK_SCHEMA 讲清楚——atom/compound/feature task、task_relations、DecisionPoint（多种配置方法的载体）、TaskRule，以及实例化与反向识别

---

## 0. 这个特性的真实形态（先看证据）

部署UPF 文档的结构：
- **1 套操作步骤骨架**（11 步，所有场景共用）
- **4 个配置场景**（URL / IMS / any / 异常），每个场景命令实例化不同
- **5 个配置阶段**（操作流程段明确：①业务费率 ②过滤规则 ③规则 ④USERPROFILE ⑤缺省费率）
- **8 条跨命令约束**（散落在数据规划表的"说明"列）

这就是用户说的"一个特性有好几种配置方法"——**骨架固定，分叉点在场景和计费方式上**。

---

## 1. atom task 层（1 条命令 = 1 个 task）

每条命令建 1 个 atom task，挂 command_ref + 该命令的参数规划。

**atom task 清单**（基于 11 步骨架）：

| task_id | task_logical_name | command_ref | 关键参数（binding_type） |
|---|---|---|---|
| `Task@00001` | 配置URR | `MMLCommand@ADD URR` | URRNAME=variable/local_planned；URRID=variable/global_planned；USAGERPTMODE=variable/decision_driven；OFFMETERINGTYPE/ONLMETERINGTYPE=variable/decision_driven |
| `Task@00002` | 配置URR组 | `MMLCommand@ADD URRGROUP` | URRGROUPNAME=variable/local_planned；UP/DOWNURRNAME1/2=reference（←ADD URR） |
| `Task@00003` | 配置PCC策略组 | `MMLCommand@ADD PCCPOLICYGRP` | PCCPOLICYGRPNM=variable/local_planned；URRGROUPNAME=reference（←ADD URRGROUP）；SIGURRGRPNAME=reference（可选） |
| `Task@00004` | 配置三四层过滤器 | `MMLCommand@ADD FILTER` | FILTERNAME=variable/local_planned；L34PROTTYPE=fixed=STRING；L34PROTOCOL/端口=variable/local_planned |
| `Task@00005` | 配置IPv6三四层过滤器 | `MMLCommand@ADD FILTERIPV6` | （场景2/3 用，SVRIPV6 等与对端协商=peer_planned） |
| `Task@00006` | 配置七层过滤器 | `MMLCommand@ADD L7FILTER` | L7FILTERNAME=variable；URLTYPE=fixed=URL；URL=variable（→DP过滤模式） |
| `Task@00007` | 配置流过滤器 | `MMLCommand@ADD FLOWFILTER` | FLOWFILTERNAME=variable/local_planned |
| `Task@00008` | 绑定三四层过滤条件到流过滤器 | `MMLCommand@ADD FLTBINDFLOWF` | FLOWFILTERNAME/FILTERNAME=reference |
| `Task@00009` | 绑定七层过滤条件到流过滤器 | `MMLCommand@ADD PROTBINDFLOWF` | FLOWFILTERNAME/L7FILTERNAME=reference |
| `Task@00010` | 配置规则 | `MMLCommand@ADD RULE` | RULENAME=variable；POLICYTYPE=fixed=PCC；FILTERINGMODE=fixed=FLOWFILTER；FLOWFILTERNAME/POLICYNAME=reference；PRIORITY=variable（受rule约束） |
| `Task@00011` | 配置用户模板 | `MMLCommand@ADD USERPROFILE` | USERPROFILENAME=variable/local_planned |
| `Task@00012` | 绑定规则到用户模板 | `MMLCommand@ADD RULEBINDING` | USERPROFILENAME/RULENAME=reference；POLICYTYPE=reference |
| `Task@00013` | 配置缺省费率 | `MMLCommand@SET URRGRPBINDING` | USERPROFILENAME/DFTURRGRPNAME/DFTSIGURRGNAME=reference |
| `Task@00014` | 配置防欺诈URR列表 | `MMLCommand@ADD SPECURRGRPLIST` | URRGROUPNAME=reference（**可选**，防欺诈开关） |
| `Task@00015` | 刷新生效 | `MMLCommand@SET REFRESHSRV` | REFRESHTYPE=fixed=ALL（must_be_last） |

> **真实字段填充示例（Task@00001 配置URR，完整）**：
> ```yaml
> task_id: UDG@20.15.2@Task@00001
> task_logical_name: 配置URR
> task_layer: atom
> nf: UDG
> version: 20.15.2
> command_ref: UDG@20.15.2@MMLCommand@ADD URR
> parameters:
>   - {parameter_ref: UDG@20.15.2@CommandParameter@ADD URR:URRNAME, binding_type: variable, variable_source: local_planned}
>   - {parameter_ref: ...:URRID, binding_type: variable, variable_source: global_planned}
>   - {parameter_ref: ...:USAGERPTMODE, binding_type: variable, variable_source: decision_driven, source_ref: UDG@20.15.2@DecisionPoint@00001}
>   - {parameter_ref: ...:OFFMETERINGTYPE, binding_type: variable, variable_source: decision_driven, source_ref: UDG@20.15.2@DecisionPoint@00001}
>   - {parameter_ref: ...:ONLMETERINGTYPE, binding_type: variable, variable_source: decision_driven, source_ref: UDG@20.15.2@DecisionPoint@00001}
> task_category: 配置
> status: active
> source_evidence_ids: [部署UPF_28493406.md]
> ```

---

## 2. compound task 层（多命令组合 = 业务阶段）

按操作流程的 5 个阶段，建 4 个 compound task（阶段⑤"缺省费率"并入收尾）：

| task_id | task_logical_name | 编排的 atom task（task_relations） |
|---|---|---|
| `Task@00101` | 配置计费三件套 | Task@00001→Task@00002→Task@00003（URR→URRGROUP→PCCPOLICYGRP 引用链） |
| `Task@00102` | 配置过滤链 | Task@00004/00005/00006→Task@00007→Task@00008/00009（过滤器→流过滤器→绑定） |
| `Task@00103` | 配置规则与用户模板绑定 | Task@00010→Task@00011→Task@00012（规则→用户模板→绑定） |
| `Task@00104` | 配置缺省费率与刷新 | Task@00013→Task@00014(可选)→Task@00015(必须最后) |

**真实字段填充（Task@00101 配置计费三件套，完整）**：
```yaml
task_id: UDG@20.15.2@Task@00101
task_logical_name: 配置计费三件套
task_layer: compound
task_summary: 配置 URR→URRGROUP→PCCPOLICYGRP 三级引用链，建立费率到策略组的绑定
task_relations:
  - {from_task_ref: UDG@20.15.2@Task@00001, to_task_ref: UDG@20.15.2@Task@00002,
     relation_type: precedes, propagated_context: URRNAME}
  - {from_task_ref: UDG@20.15.2@Task@00002, to_task_ref: UDG@20.15.2@Task@00003,
     relation_type: precedes, propagated_context: URRGROUPNAME}
status: active
source_evidence_ids: [部署UPF_28493406.md]
```

> compound task 不含 command_ref，它的"内容"由 task_relations 指向的 atom task 承载。

---

## 3. feature task 层（整特性）

```yaml
task_id: UDG@20.15.2@Task@00201
task_logical_name: 内容计费特性配置
task_layer: feature
feature_ref: UDG@20.15.2@Feature@GWFD-020301
task_summary: UPF 内容计费完整配置流程（业务费率→过滤规则→规则→用户模板→缺省费率）
task_relations:
  - {from_task_ref: Task@00101, to_task_ref: Task@00102, relation_type: precedes}  # 三件套→过滤链
  - {from_task_ref: Task@00102, to_task_ref: Task@00103, relation_type: precedes}  # 过滤链→规则绑定
  - {from_task_ref: Task@00103, to_task_ref: Task@00104, relation_type: precedes}  # 规则绑定→收尾
status: active
source_evidence_ids: [部署UPF_28493406.md]
```

> feature task 的 task_relations 编排的是 compound task；compound 编排 atom；**三层递归，同一套 task_relations 机制**。

---

## 4. DecisionPoint（多种配置方法的载体——核心）

这是"一个特性有好几种配置方法"的落点。内容计费有 3 个分叉点，全部用 DecisionPoint 表达，**不建多套 task 树**。

> **挂载点 = 决策的主要作用域**（本样板的核心设计原则）：
> - 决策主要改**参数值** → 挂 **atom task**（参数级决策）
> - 决策主要**增减子 task** → 挂 **compound/feature task**（task 级决策）
>
> 同一个业务决策若跨层影响，挂在"能覆盖两者的最近公共祖先 task"，impacts 混合 parameter + task。

### DP@00001 计费方式选择（挂 Task@00001 ADD URR —— 参数级决策）

**为什么挂 atom 不挂 compound**：内容计费基本功能里，在线/离线/融合**只改 ADD URR 的参数**（USAGERPTMODE + OFF/ONLMETERINGTYPE），**不增减任何命令**。所以挂最底层 atom task，impacts 全是 parameter 级。

```yaml
decision_id: UDG@20.15.2@DecisionPoint@00001
owner_ref: UDG@20.15.2@Task@00001      # ← 挂 atom task（ADD URR），不是 compound
decision_name: 计费方式选择
decision_question: 该费率采用哪种计费方式？
trigger_condition: 配置 ADD URR 时
options:
  - option_name: 离线
    impacts:
      - {target_type: parameter, target_ref: ...ADD URR:USAGERPTMODE, effect_type: sets_value_pattern, effect_detail: "=OFFLINE"}
      - {target_type: parameter, target_ref: ...ADD URR:OFFMETERINGTYPE, effect_type: adds, effect_detail: "条件出现，按 VOLUME/TIME/EVENT/FREE 取值"}
  - option_name: 在线
    impacts:
      - {target_type: parameter, target_ref: ...ADD URR:USAGERPTMODE, effect_type: sets_value_pattern, effect_detail: "=ONLINE"}
      - {target_type: parameter, target_ref: ...ADD URR:ONLMETERINGTYPE, effect_type: adds, effect_detail: "条件出现，按 VOLUME/TIME/EVENT/FREE 取值"}
  - option_name: 融合
    impacts:
      - {target_type: parameter, target_ref: ...ADD URR:USAGERPTMODE, effect_type: sets_value_pattern, effect_detail: "同组在线+离线URR共存（同URRGROUP下UP/DOWNURRNAME1指离线、UP/DOWNURRNAME2指在线）"}
status: active
```

> **注**：若这是 **在线计费特性(GWFD-020300)** 而非内容计费基本功能，"在线"option 才会 `adds SET URRFAILACTION 子task`（那是另一个特性的命令）。本特性范围内，计费方式纯粹是参数级决策。**决策的 task 级影响是否出现，取决于该特性的真实命令集——不能臆造**。

### DP@00002 过滤模式选择（挂 Task@00102 过滤链 —— task 级决策）

**为什么挂 compound**：4 个过滤场景**增减不同的子 task**（用哪些过滤器、是否七层），所以挂 compound 过滤链，impacts 是 task 级。

```yaml
decision_id: UDG@20.15.2@DecisionPoint@00002
owner_ref: UDG@20.15.2@Task@00102
decision_name: 过滤模式选择
decision_question: 按什么方式识别业务（决定过滤链的命令组合）？
options:
  - option_name: URL场景                    # 场景1
    impacts:
      - {target_type: task, target_ref: Task@00004, effect_type: adds, effect_detail: "配 ADD FILTER 三四层(DNS)"}
      - {target_type: task, target_ref: Task@00006, effect_type: adds, effect_detail: "配 ADD L7FILTER(URLTYPE=URL)"}
      - {target_type: task, target_ref: Task@00009, effect_type: adds, effect_detail: "配 ADD PROTBINDFLOWF 七层绑定"}
  - option_name: IMS场景                    # 场景2
    impacts:
      - {target_type: task, target_ref: Task@00005, effect_type: adds, effect_detail: "配 ADD FILTERIPV6(IPv6 三四层+服务器IP)"}
      - {target_type: task, target_ref: Task@00006, effect_type: excludes, effect_detail: "无七层过滤"}
      - {target_type: task, target_ref: Task@00009, effect_type: excludes, effect_detail: "无七层绑定"}
  - option_name: any场景                    # 场景3
    impacts:
      - {target_type: task, target_ref: Task@00004, effect_type: adds, effect_detail: "配 ADD FILTER(IPv4 any)"}
      - {target_type: task, target_ref: Task@00005, effect_type: adds, effect_detail: "配 ADD FILTERIPV6(IPv6 any)"}
      - {target_type: parameter, target_ref: ...ADD RULE:PRIORITY, effect_type: sets_value_pattern, effect_detail: "=65000 最低优先级"}
  - option_name: 异常场景                    # 场景4
    impacts:
      - {target_type: parameter, target_ref: ...ADD URR:OFFMETERINGTYPE, effect_type: sets_value_pattern, effect_detail: "=FREE 免费标记"}
      - {target_type: parameter, target_ref: ...SET URRGRPBINDING:DFTSIGURRGNAME, effect_type: adds, effect_detail: "配信令缺省URR组"}
```

> **关键**：4 个场景的差异（用哪些过滤器、是否七层、PRIORITY 取值）全部由 option 的 impacts 表达。**过滤链骨架（Task@00102）只有 1 个，4 种配置方法 = DP 的 4 个 option**。

### DP@00003 防欺诈开关（挂 Task@00201 feature task）

```yaml
decision_id: UDG@20.15.2@DecisionPoint@00003
owner_ref: UDG@20.15.2@Task@00201
decision_name: 是否启用计费防欺诈
options:
  - option_name: 启用
    impacts:
      - {target_type: task, target_ref: Task@00014, effect_type: adds, effect_detail: "执行 ADD SPECURRGRPLIST 配防欺诈费率列表"}
      - {target_type: parameter, target_ref: ...ADD RULE:*, effect_type: conditional_rule, effect_detail: "RULE 绑 URL 类型 7层 filter 时必须同时绑三四层 filter"}
  - option_name: 不启用
    impacts:
      - {target_type: task, target_ref: Task@00014, effect_type: excludes, effect_detail: "跳过防欺诈配置"}
```

---

## 5. TaskRule（真实约束，来自数据规划表 note）

全部挂在 task 上（task_ref FK）。证据是数据规划表"说明"列的原文：

| task_ref（挂在哪） | rule_type | rule_name | rule_logic（原文证据） | severity |
|---|---|---|---|---|
| Task@00101 三件套 | consistency_rule | URRGROUP必须同时配在线+离线URR | "URRGROUP下必须配置在线URR和离线URR，只配置一种且与用户计费模式不匹配时无法计费" | warning |
| Task@00101 三件套 | conditional_rule | 融合计费RGAPPLIED=DEFAULT例外 | "SMF融合计费时 SET USRPROFCHARGE/SET APNCHARGECTRL/ADD CHARGEMETHOD 的 RGAPPLIED=DEFAULT 时，URRGROUP下不能同时配离线和在线URR，否则计费冲突" | critical |
| Task@00101 三件套 | cross_nf_sync_rule | URR关键参数跨网元一致 | "URRID、USAGERPTMODE、OFFMETERINGTYPE/ONLMETERINGTYPE 在 SMF 和 UPF 上保持一致" | critical |
| Task@00102 过滤链 | binding_rule | FLOWFILTER必须绑定过滤条件 | "FLOWFILTER必须绑定过滤条件，否则匹配失败，对应Rule为无效配置" | critical |
| Task@00103 规则绑定 | cross_nf_sync_rule | RULE跨网元一致 | "RULENAME及RULE下POLICYTYPE、POLICYNAME 在 SMF 和 UPF 上保持一致" | critical |
| Task@00103 规则绑定 | selection_rule | RULE优先级相对约束 | "只绑三四层filter的RULE优先级应低于绑七层filter的；过滤条件为any的RULE优先级最低(65000)" | info |
| Task@00103 规则绑定 | cross_nf_sync_rule | USERPROFILE跨网元一致 | "USERPROFILE名称在PCF/SMF/UPF间一致，不一致PCF下发策略无法生效" | critical |
| Task@00104 收尾 | ordering_rule | REFRESHSRV必须最后 | "不执行SET REFRESHSRV，FILTER配置变更不生效" | critical |
| Task@00201 feature | conditional_rule | 防欺诈开启时的绑定约束 | "防欺诈开启时，RULE下绑URL类型7层filter必须同时绑三四层filter" | warning |

> **真实字段填充（TaskRule@00001，完整）**：
> ```yaml
> rule_id: UDG@20.15.2@TaskRule@00001
> task_ref: UDG@20.15.2@Task@00101
> rule_name: URRGROUP必须同时配在线+离线URR
> rule_type: consistency_rule
> rule_logic: URRGROUP下UPURRNAME1/DOWNURRNAME1绑离线URR、UPURRNAME2/DOWNURRNAME2绑在线URR，必须同时配置两种；只配一种且与用户计费模式不匹配时无法计费
> violation_effect: 无法计费
> severity: warning
> status: active
> source_evidence_ids: [部署UPF_28493406.md]
> ```

---

## 6. 实例化演示（正向：选 option → 生成命令）

**场景**：某运营商要配"在线计费 + URL识别 + 启用防欺诈"。

实例化流程（递归数据驱动）：
1. 进入 feature task `Task@00201` → 读 task_relations：00101→00102→00103→00104
2. 进入 `Task@00101 计费三件套` → 递归进入子 atom `Task@00001 ADD URR`：
   - 遇 DP@00001 计费方式（挂在该 atom）→ 选 `在线` → impacts 生效：
     - ADD URR.USAGERPTMODE=ONLINE
     - ADD URR.ONLMETERINGTYPE 条件出现（=VOLUME）
     - （本特性无 task 级影响——不 adds 任何子 task）
   - 执行 Task@00001/00002/00003
3. 进入 `Task@00102 过滤链`：
   - 遇 DP@00002 过滤模式（挂该 compound）→ 选 `URL场景` → impacts：adds Task@00004/00006/00009
   - 执行 Task@00004/00006/00007/00008/00009
4. 进入 `Task@00103 规则绑定`：执行 Task@00010/00011/00012（PRIORITY 按约束取 100）
5. 进入 `Task@00104 收尾`：
   - feature 的 DP@00003 防欺诈 → 选 `启用` → adds Task@00014
   - 执行 Task@00013/00014/00015（must_be_last）

**最终生成的命令序列**（与文档任务示例脚本一致）：
```
ADD URR ... (USAGERPTMODE=ONLINE, ONLMETERINGTYPE=VOLUME)   ← DP@00001"在线"(参数级)
ADD URRGROUP ... (UP/DOWNURRNAME1=离线, UP/DOWNURRNAME2=在线)
ADD PCCPOLICYGRP ... (URRGROUPNAME=reference)
ADD FILTER (L34_dns)
ADD L7FILTER (URL, URLTYPE=URL)   ← DP@00002"URL场景"adds(task级)
ADD FLOWFILTER
ADD FLTBINDFLOWF
ADD PROTBINDFLOWF            ← DP@00002"URL场景"adds(task级)
ADD RULE (POLICYTYPE=PCC, PRIORITY=100)
ADD USERPROFILE
ADD RULEBINDING
SET URRGRPBINDING
ADD SPECURRGRPLIST           ← DP@00003"启用"adds(task级)
SET REFRESHSRV (REFRESHTYPE=ALL)   ← must_be_last
```

> **注**：本特性"在线"option 只改参数、不增减命令（与文档一致）。若换成在线计费特性(GWFD-020300)，"在线"才会额外 adds SET URRFAILACTION——那是另一个特性的 task 级影响。

> **核心**：骨架（task_relations）+ 分叉（DecisionPoint option）→ 自动生成正确命令集。**不需要为"在线+URL+防欺诈"这个组合预先存一棵 task 树**——它是实例化时由 option 动态拼出来的。

---

## 7. 反向识别演示（现网命令 → 识别特性）

**给定现网导出的命令集**（4 场景混合，即文档任务示例那段脚本）：
```
ADD URR:URRNAME="URR_URL_offline",USAGERPTMODE=OFFLINE,...
ADD URR:URRNAME="URR_URL_online",USAGERPTMODE=ONLINE,...
ADD URRGROUP:UPURRNAME1="URR_URL_offline",UPURRNAME2="URR_URL_online",...
ADD PCCPOLICYGRP:PCCPOLICYGRNM="PPG_URL",URRGROUPNAME="UrrGp_URL"
ADD L7FILTER:URLTYPE=URL,URL="www.huawei.com"
ADD FLOWFILTER / ADD FLTBINDFLOWF / ADD PROTBINDFLOWF
ADD RULE:POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,PRIORITY=100
ADD USERPROFILE / ADD RULEBINDING / SET URRGRPBINDING / SET REFRESHSRV
...（IMS/any/异常场景同构）
```

**识别过程（指纹匹配，不枚举）**：
1. **命令 → atom task**：`ADD URR:USAGERPTMODE=ONLINE/OFFLINE` 命中 `Task@00001`；`ADD URRGROUP:UP/DOWNURRNAME*` 命中 `Task@00002`；... 每条命令按"命令名+关键参数模式"匹配到 atom task 指纹
2. **atom task 集合 → compound task**：发现 {Task@00001,00002,00003} 命中 `Task@00101 计费三件套`的拓扑（URR→URRGROUP→PCCPOLICYGRP 引用链）；{00004,00006,00007,00008,00009} 命中 `Task@00102 过滤链`
3. **compound task 集合 → feature task**：{00101,00102,00103,00104} 完整覆盖 `Task@00201 内容计费` 的 task_relations → **覆盖率 100%，识别为内容计费特性**
4. **option 还原**：看到 USAGERPTMODE 有 ONLINE+OFFLINE 共存 → DP@00001 选了"融合"；看到 L7FILTER URLTYPE=URL + PROTBINDFLOWF → DP@00002 选了"URL场景"；看到 SPECURRGRPLIST → DP@00003 选了"启用"

> **核心**：反向识别靠 atom task 指纹（命令级，必匹配）+ compound/feature 拓扑覆盖率打分。**现网命令即使有未覆盖的新组合，也能识别出已知部分，剩余命令标记"待抽取 task"反馈回积木库**。

---

## 8. 组合爆炸在这里如何被消化

| 看似无穷的组合 | 实际存储 | 消化方式 |
|---|---|---|
| 3 计费方式 × 4 过滤场景 × 2 防欺诈 = 24 种配置方法 | **0 棵独立 task 树** | 3 个 DecisionPoint 的 option 组合表达 |
| 11 条命令的各种实例化 | 15 个 atom task | 命令级指纹，复用 |
| 5 个阶段的各种编排 | 4 个 compound task + task_relations | 拓扑复用 |
| 整特性的多种部署 | 1 个 feature task | feature_ref 关联静态 Feature |

**存储量**：15 atom + 4 compound + 1 feature + 3 DecisionPoint + 9 TaskRule = **32 个对象**，覆盖 24+ 种配置方法。
**对比**：如果为每种配置方法建独立 task 树，需要 24 棵 × 每棵 ~15 节点 = 360 节点，且高度冗余。

---

## 9. 这份样板验证了什么

1. ✅ **atom/compound/feature 三层 task** 真实可建（命令→阶段→特性）
2. ✅ **task_relations 递归**（feature 编排 compound，compound 编排 atom，同一机制）
3. ✅ **多种配置方法 = DecisionPoint**（计费方式/过滤模式/防欺诈 3 个 DP，不建多套树）
4. ✅ **DecisionPoint impacts 跨层扇出**（option 可 adds/excludes 子 task、sets 参数值）
5. ✅ **TaskRule 全部从真实 note 抽取**（9 条，证据可追溯）
6. ✅ **实例化（正向）** 由骨架+option 自动生成正确命令集
7. ✅ **反向识别** 靠指纹+覆盖率，不要求全量枚举
8. ✅ **组合爆炸被消化**：32 对象覆盖 24+ 配置方法

## 10. 待你确认

这份样板是否符合你说的"真正长什么样子"？
- 若符合 → 我把 §6-7 的"实例化语义 + 反向识别"补进 UNIFIED_TASK_SCHEMA.md 作为正式约定
- 若某处不对（比如你觉得 DP 该挂 feature 而非 compound，或 atom 拆法不对）→ 指出，我改
