# 计费场景业务图谱（新 Schema，v0.1）

> 范围：仅描述计费场景在新三层图谱 schema 下的业务图谱部分。
> 约束：对象、关系、属性命名尽量服从 `三层图谱Schema-最终版-v0.1.md`。
> 说明：本文件只新增，不回写旧业务图谱文件。

---

## 0. 适用定义与来源

### 0.1 根定义

- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`
- `计费案例核心概念标准定义.md`

### 0.2 计费场景直接来源

- `business-graph/计费场景/01计费场景业务图谱.md`
- `business-graph/计费场景/计费场景统一知识库.md`
- `business-graph/计费场景/SKILL/knowledge/业务感知业务图谱.md`
- `business-graph/计费场景/SKILL/knowledge/计费场景业务图谱.md`
- `business-graph/计费场景/SKILL/knowledge/方案设计-配置全景.md`

---

## 1. 新 schema 对齐范围

本文件只保留新业务图谱主本体：

- `BusinessDomain`
- `NetworkScenario`
- `ConfigurationSolution`
- `BusinessRule`
- `DecisionPoint`
- `SemanticObject`

本文件中的两个子对象：

- `Scope`
- `Participant`

本文件中的外部引用对象：

- `Feature`
- `ConfigTask`

本文件不展开：

- `ConfigObject`
- `MMLCommand`
- `CommandParameter`
- `License`
- `FeatureRule`
- `TaskRule`
- `CommandRule`

这些对象分别留给后续特性图谱和命令图谱文档。

---

## 2. 旧模型到新模型的实例映射

| 旧实例类型 | 旧实例 | 新实例类型 | 新实例 | 处理说明 |
|---|---|---|---|---|
| `BusinessDomain` | `service-awareness / 业务感知` | `BusinessDomain` | 保留 | 无需调整 |
| `NetworkScenario` | `NS-01 计费场景` | `NetworkScenario` | 保留 | 无需调整 |
| `DeliverySolution` | `DS-01 差异化计费组合方案` | `ConfigurationSolution` | 保留 `solution_id=DS-01` | 仅对象类型改名 |
| `EngineeringTask` | `T-PLAN-* / T-EXEC-* / T-VERIFY-*` | `ConfigTask` | 外部引用 | 本文只保留引用关系 |
| `DomainSemanticObject` | `BA.*` 语义对象 | `SemanticObject` | 保留 | 对象类型改名 |
| `Scope` | `S-01/S-02/S-06` | 子对象 | 保留 | 不再作为一级实体 |
| `Participant` | `P-*` 参与方 | 子对象 | 保留 | 不再作为一级实体 |

---

## 3. 对象定义

### 3.1 BusinessDomain

根据 `计费案例核心概念标准定义.md`：

> `业务域` 是一类长期存在、可持续积累、覆盖多个现网场景和多个产品能力的工程知识空间。

#### 实例表

| 字段 | 值 |
|---|---|
| `domain_id` | `service-awareness` |
| `domain_name` | `业务感知` |
| `domain_summary` | 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制 |
| `status` | `accepted` |
| `supported_by` | `业务感知业务图谱.md`，`01计费场景业务图谱.md` |

---

### 3.2 NetworkScenario

根据 `计费案例核心概念标准定义.md`：

> `场景` 是业务域内部反复出现的一类稳定需求情境、问题类型或配置目标模式。

#### 实例表

| 字段 | 值 |
|---|---|
| `scenario_id` | `NS-01` |
| `scenario_name` | `计费场景` |
| `scenario_summary` | 对不同业务流采用不同计费方式，结合默认计费、免费业务和配额动作完成计费闭环 |
| `judgment_basis` | 用户需要按业务粒度差异化计费（离线/在线/融合），或需要按流量/时长/事件统计特定业务的使用量 |
| `typical_outcome` | 专项业务单独计费、免费业务不计费、普通业务默认计费，配额耗尽后切换到阻断或重定向 |
| `status` | `active` |
| `supported_by` | `01计费场景业务图谱.md`，`计费场景统一知识库.md` |

---

### 3.3 ConfigurationSolution

根据 `三层图谱本体标准定义.md`：

> `ConfigurationSolution` 表示某个场景下形成的一套稳定方案闭包。

#### 实例表

| 字段 | 值 |
|---|---|
| `solution_id` | `DS-01` |
| `solution_name` | `差异化计费组合方案（含配额分支）` |
| `solution_summary` | 通过过滤条件识别业务流，按优先级裁决Rule，绑定PCC/URR计费链实现差异化计费、免费业务与默认计费，配额耗尽后通过DecisionPoint切换用户体验 |
| `core_mechanism_combo` | `过滤条件(IPLIST/FILTER/L7FILTER/FLOWFILTER) + Rule优先级裁决 + PCC/URR计费链(PCCPOLICYGRP-URRGROUP-URR) + 默认URR组兜底 + 配额耗尽动作切换(BLOCK/REDIRECT/FORWARD)` |
| `status` | `active` |
| `supported_by` | `01计费场景业务图谱.md`，`业务感知业务图谱.md` |

#### 说明

旧模型里该对象叫 `DeliverySolution`。在新 schema 下，保留原实例和内容，只把对象类型收敛为 `ConfigurationSolution`。

---

### 3.4 DecisionPoint

根据 `三层图谱本体标准定义.md`：

> `DecisionPoint` 表示会引起后续结构分叉的稳定选择点。

#### 实例表

| `decision_id` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `status` |
|---|---|---|---|---|---|---|
| `DP-00` | 配置网元范围选择 | 本次计费场景需要配置或核查哪些网元 | `["UPF+SMF","UPF only","SMF only"]` | 进入计费配置生成或核查任务时 | 决定生成 UPF 执行链、SMF 编排链，还是双侧协同链 | `active` |
| `DP-01` | 计费方式选择 | 当前计费场景采用哪种计费方式 | `["离线计费","在线计费","融合计费"]` | 进入计费场景时 | 决定 URR 计费模式、是否需要 CCT 模板、配额控制机制、CHF 交互模式 | `active` |
| `DP-02` | 配额耗尽后动作选择 | 在线计费配额耗尽后如何处理业务体验 | `["BLOCK","REDIRECT","FORWARD"]` | 在线或融合计费配额耗尽 | 决定是否配置门控、重定向或放行 | `active` |
| `DP-03` | 匹配层次选择 | 业务流通过 L34 层还是 L7 层匹配 | `["L34层匹配","L7层URL匹配","L7层协议匹配","L34+L7混合匹配"]` | 规划识别条件时 | 决定是否需要 L7FILTER 和 PROTBINDFLOWF，影响配置任务链长度 | `active` |

---

### 3.5 BusinessRule

根据 `三层图谱本体标准定义.md`：

> `BusinessRule` 表示业务层的规则对象。

#### 实例表

| `rule_id` | `rule_name` | `rule_type` | `rule_purpose` | `check_target` | `check_logic` | `status` |
|---|---|---|---|---|---|---|
| `BR-01` | SA基础License开启断言 | `constraint_rule` | 确保业务感知底座可用 | `LICENSESWITCH` | LKV3G5SABS01 + LKV3G5BCBC01 + LKV3G5PCCB01 必须为 ENABLE | `active` |
| `BR-02` | 配置链逐层一致性校验 | `validation_rule` | 验证全链路绑定正确 | `RULEBINDING→RULE→PCCPOLICYGRP→URRGROUP→URR→FLOWFILTER→FILTER` | 各层对象名称、绑定关系与规划值一致 | `active` |
| `BR-03` | PFCP Usage Report一致性校验 | `validation_rule` | 验证计费流量正确上报 | `PFCP Session Report / URR ID` | Usage Report 中 URR ID 与配置一致 | `active` |
| `BR-04` | CP/UP URR一致性诊断 | `diagnosis_rule` | 定位 CP/UP 配置不一致导致的计费异常 | `SMF侧URR vs UPF侧URR` | URR 名称、RG 值、URRID 在 SMF 和 UPF 侧必须一致 | `active` |
| `BR-05` | URRID全局唯一约束 | `constraint_rule` | 防止 URRID 冲突导致 PFCP 上报错乱 | `所有URR对象` | URRID 在所有 URR 中唯一 | `active` |
| `BR-06` | 默认URR组必须配置 | `constraint_rule` | 防止未命中流量不计费 | `URRGRPBINDING` | DFTURRGRPNAME 和 DFTSIGURRGNAME 必须同时配置 | `active` |
| `BR-07` | RG值跨侧一致性约束 | `constraint_rule` | 确保费率标识在 UPF 和 SMF 间对齐 | `URR.RG` | UDG.ADD URR.RG = UNC.ADD URR.RG | `active` |
| `BR-08` | REFRESHSRV时序约束 | `constraint_rule` | 确保刷新时机正确 | `REFRESHSRV` | 必须在所有 ADD/SET 完成后执行；执行后 30s 内不允许修改 Filter | `active` |
| `BR-09` | PROTBINDFLOWF协议匹配约束 | `constraint_rule` | 防止协议配置与目标不匹配 | `PROTBINDFLOWF` | PROTOCOLNAME 必须与目标网站实际协议一致 | `active` |
| `BR-10` | SMF融合计费三联前置约束 | `constraint_rule` | 防止 SMF 未进入 N40 融合计费闭环 | `CHGMODE/CHARGECTRL/CHFINIT` | 融合计费需满足 CHGMODE=NchfMode、CHARGECTRL 或绑定使能、CHFINIT=SENDREQ | `active` |
| `BR-11` | SMF/UPF跨网元一致性矩阵 | `validation_rule` | 确认控制面编排对象与用户面执行对象对齐 | `USERPROFILE/RULE/PCCPOLICYGRP/URRGROUP/URR` | USERPROFILENAME、RULENAME、POLICYTYPE+POLICYNAME、URRID、USAGERPTMODE、METERINGTYPE、RG 两侧一致 | `active` |

---

### 3.6 SemanticObject

根据 `三层图谱本体标准定义.md`：

> `SemanticObject` 是业务层向下连接能力和配置的语义桥梁。

#### 实例表

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `typical_landing` |
|---|---|---|---|
| `BA.PacketParsing` | 报文解析 | 如何把原始报文拆解成可读字段 | `FILTER`, `L7FILTER` |
| `BA.ProtocolRecognition` | 协议识别 | 如何识别协议或应用 | `PROTBINDFLOWF` |
| `BA.FilterCondition` | 过滤条件 | 如何组织成可匹配条件 | `FILTER`, `FLOWFILTER`, `FLOWFILTERGRP` |
| `BA.Rule` | 规则语义 | 将匹配条件与计费动作绑定 | `RULE` |
| `BA.Policy` | 策略语义 | 命中后执行的策略类型 | `PCCPOLICYGRP` |
| `BA.Priority` | 优先级语义 | 多规则同时命中时如何裁决 | `RULE.PRIORITY` |
| `BA.Binding` | 绑定语义 | 规则和范围如何绑定 | `USERPROFILE`, `RULEBINDING`, `URRGRPBINDING` |
| `BA.Charging` | 计费语义 | 如何按业务收费 | `URR`, `URRGROUP`, `PCCPOLICYGRP` |
| `BA.Quota` | 配额语义 | 在线或融合计费的配额控制与耗尽动作 | `CCT`, `配额动作相关对象` |
| `BA.ValidationDiagnosis` | 核查与诊断语义 | 如何验证和回查 | `LST全链路`, `PFCP Session Report` |

---

### 3.7 Scope（子对象）

根据 `三层图谱本体标准定义.md`：

> `Scope` 保留语义，但不作为一级本体。

#### 子对象表

| `scope_id` | `scope_name` | `scope_type` | `scope_expression` | `scope_summary` | `status` |
|---|---|---|---|---|---|
| `S-01` | 用户级范围 | `subscriber` | 普通用户/特定用户 | 计费策略按用户粒度生效 | `active` |
| `S-02` | APN/DNN范围 | `access` | APN1/指定DNN | 计费策略按接入点或数据网名称生效 | `active` |
| `S-06` | UserProfile承载范围 | `subscription` | UserProfile名称 | 承载规则绑定和默认计费组，是计费策略的最终生效边界 | `active` |

---

### 3.8 Participant（子对象）

根据 `三层图谱本体标准定义.md`：

> `Participant` 保留语义，但不作为一级本体。

#### 子对象表

| `participant_id` | `participant_name` | `participant_type` | `plane_or_side` | `responsibility_summary` | `status` |
|---|---|---|---|---|---|
| `P-01` | PCF | `network_function` | `control_plane` | 动态规则场景下生成计费策略并下发给 SMF | `active` |
| `P-02` | SMF | `network_function` | `control_plane` | 编排计费策略、与 CHF/OCS 交互、下发计费规则到 UPF、配额管理 | `active` |
| `P-03` | UPF | `network_function` | `user_plane` | 业务识别、流量统计、执行计费规则、上报使用量 | `active` |
| `P-04` | CHF/OCS | `external_system` | `external` | 处理计费请求、配额分配、重授权触发 | `active` |
| `P-05` | UE/用户 | `endpoint` | `terminal_side` | 发起会话与业务访问，产生待计费业务流 | `active` |
| `P-10` | CG | `external_system` | `external` | 接收离线计费 CDR，转发给 BD 域 | `active` |

---

## 4. 外部引用对象（不在本文件展开）

### 4.1 Feature 引用

业务图谱只保留 `uses_feature` 关系，不在本文件展开 `Feature` 详细属性。

#### 当前计费场景直接引用的特性

| `feature_id` | `feature_name` | 业务解释 |
|---|---|---|
| `GWFD-110101` | SA-Basic | 识别底座 |
| `GWFD-020351` | PCC基本功能 | 用户面策略执行骨架 |
| `GWFD-020301` | 内容计费基本功能 | 内容计费能力底座 |
| `GWFD-010171` | 离线计费 | 离线计费方式能力 |
| `GWFD-020300` | 在线计费 | 在线计费方式能力 |
| `GWFD-010173` | 融合计费 | 融合计费方式能力 |
| `WSFD-109101` | PCC基本功能 | SMF 侧 PCC 能力 |
| `WSFD-109002` | 内容计费基本功能 | SMF 侧计费编排能力 |
| `WSFD-011201` | 支持离线计费 | SMF 侧离线计费能力 |
| `WSFD-011206` | 支持融合计费 | SMF 侧融合计费能力 |

### 4.2 ConfigTask 引用

业务图谱只保留 `uses_task` 关系，不在本文件展开 `ConfigTask` 详细属性。

#### 当前计费场景直接引用的 task

| `task_id` | `task_name` | `phase` | 业务解释 |
|---|---|---|---|
| `T-PLAN-001` | 规划生效范围 | `plan` | 规划 UserProfile 与默认兜底范围 |
| `T-PLAN-002` | 规划识别条件 | `plan` | 将业务描述翻译为过滤条件 |
| `T-PLAN-003` | 规划Rule与优先级 | `plan` | 决定规则层次和优先级 |
| `T-PLAN-004` | 规划计费对象与费率标识 | `plan` | 规划 URR→URRGROUP→PCCPOLICYGRP |
| `T-PLAN-005` | 规划配额耗尽动作 | `plan` | 规划 BLOCK / REDIRECT / FORWARD |
| `T-EXEC-001` | 配置IP地址列表 | `execute` | 按需配置特定IP匹配 |
| `T-EXEC-002` | 配置三四层过滤条件 | `execute` | 配置 L34 过滤条件 |
| `T-EXEC-003` | 配置七层过滤条件 | `execute` | 配置 L7 过滤条件 |
| `T-EXEC-004` | 配置流过滤器与绑定 | `execute` | 组合过滤条件 |
| `T-EXEC-005` | 配置计费动作链 | `execute` | 创建 URR→URRGROUP→PCCPOLICYGRP |
| `T-EXEC-008` | 配置Rule | `execute` | 绑定匹配条件与计费策略 |
| `T-EXEC-010` | 配置UserProfile与Rule绑定 | `execute` | 完成规则容器和默认计费绑定 |
| `T-EXEC-011` | 核查SMF系统级计费前置 | `execute` | 核查 SMF 系统级前置 |
| `T-EXEC-012` | 配置SMF到CHF的N40接入与选择链 | `execute` | 配置或核查 N40 接入 |
| `T-EXEC-013` | 配置SMF模板、Trigger与异常处理 | `execute` | 配置模板、触发器和异常处理 |
| `T-VERIFY-001` | 验证License开关 | `verify` | 验证 License |
| `T-VERIFY-002` | 验证配置链逐层回查 | `verify` | 回查配置链 |
| `T-VERIFY-003` | 验证PFCP会话上报与计费流量 | `verify` | 验证 PFCP 上报 |

---

## 5. 关系定义

### 5.1 主链关系

| 起点 | 关系 | 终点 | 说明 |
|---|---|---|---|
| `BusinessDomain(service-awareness)` | `contains` | `NetworkScenario(NS-01)` | 业务感知域中包含计费场景 |
| `NetworkScenario(NS-01)` | `instantiated_as` | `ConfigurationSolution(DS-01)` | 计费场景收敛为差异化计费组合方案 |

### 5.2 Scenario / Solution 到 DecisionPoint

| 起点 | 关系 | 终点 | 说明 |
|---|---|---|---|
| `NS-01` | `has_decision` | `DP-00` | 决定本次涉及哪些网元 |
| `NS-01` | `has_decision` | `DP-01` | 决定采用离线、在线还是融合计费 |
| `DS-01` | `has_decision` | `DP-02` | 决定配额耗尽后的动作 |
| `DS-01` | `has_decision` | `DP-03` | 决定采用 L34 还是 L7 识别路径 |

### 5.3 Scenario / Solution 到 BusinessRule

| 起点 | 关系 | 终点 | 说明 |
|---|---|---|---|
| `DS-01` | `constrained_by` | `BR-01` ~ `BR-11` | 方案受计费约束、校验和诊断规则治理 |

### 5.4 Scenario / Solution 到 SemanticObject

| 起点 | 关系 | 终点 | 说明 |
|---|---|---|---|
| `NS-01` | `uses_semantic_object` | `BA.FilterCondition` | 计费场景先通过过滤条件识别业务流 |
| `NS-01` | `uses_semantic_object` | `BA.Charging` | 计费场景核心语义对象 |
| `DS-01` | `uses_semantic_object` | `BA.FilterCondition` | 方案把业务描述落实为过滤条件链 |
| `DS-01` | `uses_semantic_object` | `BA.Rule` | 方案把匹配条件与计费动作绑定为 RULE |
| `DS-01` | `uses_semantic_object` | `BA.Charging` | 方案把计费语义落实为计费对象链 |
| `DS-01` | `uses_semantic_object` | `BA.Quota` | 在线或融合计费时落实配额控制 |

### 5.5 Solution 到 Feature / ConfigTask

| 起点 | 关系 | 终点 | 说明 |
|---|---|---|---|
| `DS-01` | `uses_feature` | `GWFD-110101` | 需要 SA 识别底座 |
| `DS-01` | `uses_feature` | `GWFD-020351` | 需要 PCC 执行骨架 |
| `DS-01` | `uses_feature` | `GWFD-020301` | 需要内容计费能力 |
| `DS-01` | `uses_feature` | `GWFD-010171 / GWFD-020300 / GWFD-010173` | 需要计费方式能力，按 `DP-01` 选择 |
| `DS-01` | `uses_feature` | `WSFD-109101 / WSFD-109002 / WSFD-011201 / WSFD-011206` | 需要 SMF 侧能力栈 |
| `DS-01` | `uses_task` | `T-PLAN-* / T-EXEC-* / T-VERIFY-*` | 方案通过规划、执行、验证类 task 落地 |

---

## 6. 当前边界结论

基于新 schema，计费场景的业务图谱边界明确为：

1. **保留**
   - 业务域
   - 场景
   - 方案
   - 决策点
   - 业务规则
   - 语义对象
   - `Scope` / `Participant` 子对象

2. **只引用，不展开**
   - `Feature`
   - `ConfigTask`

3. **不保留在业务图谱**
   - `ConfigObject`
   - `MMLCommand`
   - `CommandParameter`
   - 命令级规则

这与根目录定义保持一致：业务图谱负责回答“为什么配”和“方案如何组织”，不直接坠落到底层命令本体。

---

## 7. 下一步接口

后续两份文档需要承接本文中的外部引用：

1. `02-计费场景-特性图谱-新schema-v0.1.md`
   - 展开 `Feature / SubFeature / ConfigTask / FeatureRule / License`

2. `03-计费场景-命令图谱-新schema-v0.1.md`
   - 展开 `MMLCommand / CommandParameter / ConfigObject / CommandRule`

