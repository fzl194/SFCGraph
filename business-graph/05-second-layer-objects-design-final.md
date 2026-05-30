# 业务图谱第二层对象最终 Schema 定义

## 文件说明

本文件承接 `04-schema-final-v2.md`，定义业务图谱第二层对象的最终 schema。

第二层对象不回答“业务域有哪些主链对象”，而回答：

1. 方案由谁参与
2. 方案对谁、在哪些边界下生效
3. 场景或方案在哪些稳定点发生分支
4. 方案如何组织验收
5. 方案受哪些业务级规则治理

每个对象包含两部分：
1. **Schema 定义**：属性、边、约束
2. **业务感知域实例**：具体实例化内容 + 原始文档证据链

---

## 已确认的决策（S1-S6 汇总）

| 编号 | 决策 |
|------|------|
| S1 | `Participant` 保留，主挂 `DeliverySolution` |
| S2 | `Scope` 保留，主挂 `DeliverySolution`，不与 `UserProfile` 合并 |
| S3 | `DecisionPoint` 保留，允许 `NetworkScenario` 与 `DeliverySolution` 双层挂载 |
| S4 | `RuntimeFlow` 删除，不再作为第二层独立对象保留 |
| S5 | `ValidationPlan` 保留，并与 `EngineeringTask(phase=verify)` 建立“验什么 / 怎么验”的分层关系 |
| S6 | `DiagnosisRule` 与 `RiskConstraint` 不再平行保留，统一收敛为 `BusinessRule`，以 `rule_type` 分型 |

## 第二层结构

```text
DeliverySolution
  ├─ involves ───────> Participant
  ├─ applies_to ─────> Scope
  ├─ has_decision ───> DecisionPoint
  ├─ validated_by ───> ValidationPlan
  └─ governed_by ────> BusinessRule

NetworkScenario
  └─ has_decision ───> DecisionPoint

DecisionPoint
  └─ conditioned_by ─> Scope

ValidationPlan
  ├─ executed_by ────> EngineeringTask   (phase=verify)
  └─ uses_rule ──────> BusinessRule
```

第二层对象数量：5 个（Participant、Scope、DecisionPoint、ValidationPlan、BusinessRule）

---

## 第二层关系总表

| 关系标识 | 中文关系名 | 起点对象 | 终点对象 | 基数 | 业务含义 |
|----------|------------|----------|----------|------|----------|
| `involves` | 涉及参与方 | `DeliverySolution` | `Participant` | M:N | 一套方案由哪些参与方协同完成 |
| `applies_to` | 作用于 | `DeliverySolution` | `Scope` | M:N | 一套方案对谁、在哪些边界下生效 |
| `has_decision` | 包含决策点 | `NetworkScenario` | `DecisionPoint` | 1:N | 某类场景天然存在的稳定分支 |
| `has_decision` | 包含决策点 | `DeliverySolution` | `DecisionPoint` | 1:N | 某个方案内部需要做的稳定选择 |
| `conditioned_by` | 受范围条件约束 | `DecisionPoint` | `Scope` | M:N | 某些分支只有在特定边界下才成立 |
| `validated_by` | 由其验收 | `DeliverySolution` | `ValidationPlan` | 1:N | 一套方案需要哪些验收模板 |
| `executed_by` | 由其执行 | `ValidationPlan` | `EngineeringTask` | 1:N | 验收计划由哪些验证态 Task 具体执行 |
| `uses_rule` | 使用规则 | `ValidationPlan` | `BusinessRule` | 1:N | 验收计划内部依赖哪些判断规则 |
| `governed_by` | 受规则治理 | `DeliverySolution` | `BusinessRule` | 1:N | 一套方案受哪些核查/约束/诊断规则治理 |

> `RuntimeFlow` 已按 S4 删除，因此第二层关系中不再出现运行流程对象。

---

## 1. Participant（参与方）

### 1.1 Schema 定义

**定位**：在某个 `DeliverySolution` 的形成、生效、更新、计费、验证过程中承担稳定职责的参与方。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| participant_id | string | 是 | 唯一标识 |
| participant_name | string | 是 | 参与方名称 |
| participant_type | string | 是 | 类型：`endpoint / network_function / external_system / service_endpoint / access_side` |
| responsibility_summary | string | 是 | 一句话说明其稳定职责 |
| plane_or_side | string | 否 | 所在侧：`control_plane / user_plane / external / terminal_side / service_side` |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
DeliverySolution --involves--> Participant
```

> 第二层最小关系集中，`Participant` 当前只保留与 `DeliverySolution` 的主关系。

### 1.2 业务感知域核心实例

| participant_id | participant_name | participant_type | plane_or_side | responsibility_summary | status |
|------|------|------|------|------|------|
| P-01 | PCF | network_function | control_plane | 生成或选择策略，并向 SMF 下发策略控制信息 | active |
| P-02 | SMF | network_function | control_plane | 编排会话、翻译策略、协调控制面与用户面 | active |
| P-03 | UPF | network_function | user_plane | 识别业务流、执行策略、上报使用信息 | active |
| P-04 | CHF | external_system | external | 处理计费、配额、重授权触发 | active |
| P-05 | UE/用户 | endpoint | terminal_side | 发起会话与业务访问，产生待识别业务流 | active |
| P-06 | AMF | network_function | control_plane | 在分流和会话修改场景中承接接入侧信令协同 | active |
| P-07 | UL CL UPF | network_function | user_plane | 在本地分流场景中承接分流规则并执行上行分类转发 | active |
| P-08 | 主锚点UPF | network_function | user_plane | 承接中心 DN 业务和分流前常规 PDU 会话 | active |
| P-09 | 辅锚点UPF | network_function | user_plane | 承接本地 DN 业务和分流后本地业务转发 | active |
| P-10 | 中心DN/本地DN/业务服务器 | service_endpoint | service_side | 作为业务目的地接收业务流量 | active |

### 1.3 证据链

| 实例 | 证据来源 | 关键引用 |
|------|---------|---------|
| PCF / SMF / UPF / 用户 / 基站 / 业务服务器 | `业务感知过程_92407889.md` | “PCF下发规则…SMF翻译…UPF解析识别/规则匹配/策略执行…数据转发到网络/业务服务器” |
| PCF / SMF / UPF / CHF | `业务感知场景举例_92407896.md` | “SMF 将用户信息发送给 PCF…UPF 定期上报使用量，经 SMF 到达 CHF…CHF 通知 SMF” |
| SMF / CHF / PCF / UPF / UDM / NRF | `融合计费概述_42995681.md` | 表1“涉及NF / 功能说明” |
| UE / AMF / SMF / PCF / UL CL UPF / 主辅锚点UPF / DN | `How分流_58273329.md` | 分流策略来源、UPF 选择与插入、分流流程 Step1-Step5 |

---

## 2. Scope（作用范围）

### 2.1 Schema 定义

**定位**：描述某个 `DeliverySolution` 或某类策略对“谁、哪类接入、哪类位置、哪类会话条件”生效的边界对象。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| scope_id | string | 是 | 唯一标识 |
| scope_name | string | 是 | 范围名称 |
| scope_summary | string | 是 | 一句话说明该范围含义 |
| scope_type | string | 是 | 范围类别，如 `subscriber / subscription / access / location / slice / service-selection` |
| scope_expression | string | 否 | 原始表达或归一化表达 |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
DeliverySolution --applies_to--> Scope
DecisionPoint --conditioned_by--> Scope
```

> `UserProfile` 是范围的工程承载点，不直接等同于 `Scope`。

### 2.2 业务感知域核心实例

| scope_id | scope_name | scope_type | scope_expression | scope_summary | status |
|------|------|------|------|------|------|
| S-01 | 用户级范围 | subscriber | 普通用户 / 特定用户 | 方案按用户粒度生效 | active |
| S-02 | APN/DNN范围 | access | APN1 / 指定DNN | 方案按接入点或数据网名称生效 | active |
| S-03 | 切片范围 | slice | 用户切片信息 | 方案按切片粒度生效 | active |
| S-04 | 位置/PRA范围 | location | 位置区 / PRA | 方案按位置或指定区域生效 | active |
| S-05 | DNAI/本地DN导向范围 | service-selection | DNAI / 本地DN | 方案按本地业务导向条件生效 | active |
| S-06 | UserProfile承载范围 | subscription | UserProfile1 | 用于承载规则绑定和最终生效边界 | active |

### 2.3 证据链

| 实例 | 证据来源 | 关键引用 |
|------|---------|---------|
| 用户级范围 | `业务感知场景举例_92407896.md` | “用户类型：普通用户” |
| APN/DNN范围 | `业务感知场景举例_92407896.md` | “配置 APN1…User Profile1 进一步绑定到 APN1 下” |
| 切片范围 | `How分流_58273329.md` | “用户DNN与切片信息”“用户切片信息” |
| 位置/PRA范围 | `How分流_58273329.md` | “用户位置区信息”“DNN+位置组合满足分流触发条件”“PRA” |
| DNAI/本地DN导向范围 | `How分流_58273329.md` | “DNAI信息”“完成用户与本地DN之间的业务” |
| UserProfile承载范围 | `套餐2：带宽控制_94838085.md` | “将多条 Rule 绑定到同一个 UserProfile 下，形成最终业务套餐” |

---

## 3. DecisionPoint（决策点）

### 3.1 Schema 定义

**定位**：在某个 `NetworkScenario` 或 `DeliverySolution` 中，会导致后续任务、动作路径或方案实现方式发生分支变化的稳定选择点。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| decision_id | string | 是 | 唯一标识 |
| decision_name | string | 是 | 决策点名称 |
| decision_question | string | 是 | 该决策实际在回答什么问题 |
| option_set | list[string] | 是 | 可选分支集合 |
| trigger_condition | string | 否 | 在什么条件下需要做该决策 |
| impact_summary | string | 是 | 不同分支会影响哪些后续任务或方案结构 |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
NetworkScenario --has_decision--> DecisionPoint
DeliverySolution --has_decision--> DecisionPoint
DecisionPoint --conditioned_by--> Scope
```

### 3.2 业务感知域核心实例

| decision_id | decision_name | 挂载层级 | decision_question | option_set | trigger_condition | status |
|------|------|------|------|------|------|------|
| DP-01 | 计费方式选择 | NetworkScenario(NS-01) | 当前计费场景采用哪种计费方式 | `["离线计费","在线计费","融合计费"]` | 进入计费场景时 | active |
| DP-02 | 配额耗尽后动作选择 | DeliverySolution(DS-01) | 用户配额耗尽后如何处理业务体验 | `["BLOCK","REDIRECT","FORWARD"]` | 在线计费配额耗尽 | active |
| DP-03 | 分流策略来源选择 | NetworkScenario(NS-04) | 分流策略最终由谁下发给 UL CL UPF | `["PCF下发","SMF下发","PCF经SMF下发","MPF下发"]` | 进入本地分流场景时 | active |
| DP-04 | 分流触发与 UPF 选择 | DeliverySolution(DS-04) | 何时触发分流，以及选择哪类 UPF | `["仅主锚点","插入UL CL","插入辅锚点","UL CL+辅锚点"]` | 满足 DNN/位置/PRA/DNAI/能力条件时 | active |
| DP-05 | 访问限制动作选择 | DeliverySolution(DS-02) | 命中目标业务流后采用哪种处理路径 | `["DISCARD","HEADEN","IPREDIR","REDIRECT"]` | 规则命中后 | active |

### 3.3 证据链

| 实例 | 证据来源 | 关键引用 |
|------|---------|---------|
| 计费方式选择 | `计费解决方案概述_90776649.md` | “离线计费 / 在线计费 / 融合计费” |
| 配额耗尽后动作选择 | `业务感知场景举例_92407896.md` | “流量耗尽后…停用 Rule2，启用 Rule3…重定向用户到充值页面” |
| 分流策略来源选择 | `How分流_58273329.md` | “UL CL UPF 获取分流策略有四种方式” |
| 分流触发与 UPF 选择 | `How分流_58273329.md` | “DNN+位置组合满足分流触发条件…选择 UL CL UPF 和辅锚点 UPF” |
| 访问限制动作选择 | `套餐3_94838086.md` | “PCC阻塞 / HEADEN / IPREDIR / PCC重定向” |

---

## 4. ValidationPlan（验收计划）

### 4.1 Schema 定义

**定位**：针对某个 `DeliverySolution` 或某类关键业务目标的验收检查模板。

它回答“验什么”，不直接回答“怎么逐条执行检查”。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| validation_id | string | 是 | 唯一标识 |
| validation_name | string | 是 | 验收计划名称 |
| validation_goal | string | 是 | 验收目标 |
| target_objects | list[string] | 是 | 需要观察/检查的对象集合 |
| pass_condition | string | 是 | 通过条件 |
| expected_result | string | 是 | 预期现象或结果 |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
DeliverySolution --validated_by--> ValidationPlan
ValidationPlan --executed_by--> EngineeringTask
  约束: EngineeringTask.phase = verify
ValidationPlan --uses_rule--> BusinessRule
```

### 4.2 业务感知域核心实例

| validation_id | validation_name | 对应方案 | validation_goal | target_objects | pass_condition | expected_result | status |
|------|------|------|------|------|------|------|------|
| VP-01 | 差异化计费验收 | DS-01 | 确认计费链、URR 绑定与 PFCP 上报符合预期 | `["LICENSESWITCH","RULEBINDING","RULE","URR","PFCP Session Report"]` | License 开启、配置链正确、URR ID 与上报一致 | 业务流被正确识别并按预期计费/上报 | active |
| VP-02 | 访问限制验收 | DS-02 | 确认阻塞、头增强、重定向链路生效 | `["RULEBINDING","RULE","PCCPOLICYGRP","PCCACTIONPROP","HEADEN","L7FILTER","FILTER"]` | 配置链完整、动作参数正确、门控/导向符合预期 | 业务被阻塞、增强或重定向到指定目标 | active |
| VP-03 | 带宽控制验收 | DS-03 | 确认 BWM 策略链和速率参数生效 | `["RULEBINDING","RULE","CATEGORYPROP","BWMSERVICE","BWMCONTROLLER","BWMRULE"]` | 策略链完整、控制器参数符合规划、绑定关系正确 | 业务获得预期限速/保障/整形效果 | active |
| VP-04 | 本地分流与独立计费验收 | DS-04 | 确认分流触发、UPF 选择和独立计费链符合规划 | `["DNN/位置条件","UL CL/辅锚点选择结果","UPF配额行为"]` | 触发条件命中、分流路径符合规划、多 UPF 计费行为正确 | 业务被导向本地DN/中心DN，计费路径与 UPF 分工一致 | planned |

### 4.3 证据链

| 实例 | 证据来源 | 关键引用 |
|------|---------|---------|
| 差异化计费验收 | `04-schema-final-v2.md` / `调测内容计费_08957400` | 已抽出 `T-VERIFY-001/002/003` |
| 访问限制验收 | `04-schema-final-v2.md` | 已抽出 `T-VERIFY-004/005` |
| 带宽控制验收 | `04-schema-final-v2.md` | 已抽出 `T-VERIFY-006` |
| 本地分流与独立计费验收 | `How分流_58273329.md` / 计费与多 UPF 配额相关材料 | 触发分流、UPF 选择、多 UPF 配额申请与下发 |

---

## 5. BusinessRule（业务规则）

### 5.1 Schema 定义

**定位**：用于表达业务级核查、约束断言和异常定位逻辑的统一规则对象。

它统一承载原先分散的：

- `DiagnosisRule`
- `RiskConstraint`

并扩展出统一的规则分型。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| rule_id | string | 是 | 唯一标识 |
| rule_name | string | 是 | 规则名称 |
| rule_type | string | 是 | `validation_rule / diagnosis_rule / constraint_rule` |
| rule_purpose | string | 是 | 规则用途 |
| trigger_condition | string | 否 | 何时触发该规则 |
| check_target | string | 是 | 检查对象或观察对象 |
| check_logic | string | 是 | 判断逻辑 |
| expected_result | string | 否 | 满足时的预期结果，适用于 validation_rule |
| violation_effect | string | 否 | 违反后的影响，适用于 constraint_rule |
| next_action | string | 否 | 下一步排查动作，适用于 diagnosis_rule |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
ValidationPlan --uses_rule--> BusinessRule
DeliverySolution --governed_by--> BusinessRule
```

### 5.2 业务感知域核心实例

| rule_id | rule_name | rule_type | 对应方案/计划 | check_target | check_logic | expected_result / violation_effect / next_action | status |
|------|------|------|------|------|------|------|------|
| BR-01 | SA基础License开启断言 | constraint_rule | DS-01 / VP-01 | LICENSESWITCH | SA-Basic 与相关内容计费能力开关必须为 ENABLE | violation_effect: 业务感知能力不可用 | active |
| BR-02 | 配置链逐层一致性校验 | validation_rule | VP-01 / VP-02 / VP-03 | RULEBINDING→RULE→对象链 | 各层对象名称、绑定关系、关键参数与规划值一致 | expected_result: 配置链完整且参数一致 | active |
| BR-03 | PFCP Usage Report一致性校验 | validation_rule | VP-01 | PFCP Session Report / URR ID | Usage Report 中 URR ID 应与业务规则绑定一致 | expected_result: 计费流量被正确识别和上报 | active |
| BR-04 | CP/UP URR一致性诊断 | diagnosis_rule | DS-01 | CP/UP URR 配置 | 如果计费结果异常，先比对两侧 URR 名称和关键属性是否一致 | next_action: 回查 CP/UP URR 配置与绑定链 | active |
| BR-05 | Trigger未上报排查规则 | diagnosis_rule | DS-01 / DS-04 | Trigger / 会话更新 | 若未触发预期计费或配额更新，检查 Trigger 上报和会话更新链路 | next_action: 检查 Trigger 条件、会话更新与 CHF 交互 | active |
| BR-06 | N40计费流量一致性校验 | diagnosis_rule | DS-01 | N40 / CHF 结果 | 若业务被放通但未形成预期计费结果，检查 N40 侧计费流量与实际流量是否一致 | next_action: 检查 CHF / N40 流量上报链 | active |
| BR-07 | UL CL仅支持融合计费约束 | constraint_rule | DS-04 | 分流模式与计费方式 | UL CL 方案与计费方式必须满足产品约束 | violation_effect: UL CL 分流功能无法正常使用 | active |
| BR-08 | default quota异常处理规则 | diagnosis_rule | DS-01 | default quota 行为 | 当默认配额路径异常时，先检查 default quota 参数与配额更新行为 | next_action: 回查 default quota 相关配置和更新链 | active |

### 5.3 证据链

| 实例 | 证据来源 | 关键引用 |
|------|---------|---------|
| SA基础License开启断言 | `04-schema-final-v2.md` | 已抽出 `T-VERIFY-001 验证 License 开关` |
| 配置链逐层一致性校验 | `04-schema-final-v2.md` | 已抽出 `T-VERIFY-002/004/005/006` |
| PFCP Usage Report一致性校验 | `04-schema-final-v2.md` / `调测内容计费_08957400` | 已抽出 `T-VERIFY-003` |
| CP/UP URR一致性诊断 | `19-business-awareness-business-graph-final_v2.md` / `03-schema-design.md` | “CP/UP URR配置不一致” |
| Trigger未上报排查规则 | `19-business-awareness-business-graph-final_v2.md` / `03-schema-design.md` | “Trigger未上报” |
| N40计费流量一致性校验 | `19-business-awareness-business-graph-final_v2.md` / `03-schema-design.md` | “业务被放通未上报CHF”“N40接口计费流量与实际流量不一致” |
| UL CL仅支持融合计费约束 | `03-schema-design.md` | “UL CL方案只支持融合计费，否则UL CL分流功能无法正常使用” |
| default quota异常处理规则 | `19-business-awareness-business-graph-final_v2.md` / `03-schema-design.md` | “default quota” |

---

## 第二层对象与第一层主链的关系

| 第二层对象 | 与 BusinessDomain 的关系 | 与 NetworkScenario 的关系 | 与 DeliverySolution 的关系 | 与 EngineeringTask 的关系 |
|------|------|------|------|------|
| Participant | 不主挂，避免退化为背景说明 | 可间接体现不同场景参与方簇 | **主挂载点**：方案由哪些参与方协同完成 | 间接相关，当前不单独建边 |
| Scope | 不主挂，域不是生效边界 | 决策上间接体现某些场景常见范围 | **主挂载点**：方案对谁、在什么边界下生效 | 间接相关，体现在 plan/verify task 输入中 |
| DecisionPoint | 不主挂 | **主挂载点之一**：场景级稳定分支 | **主挂载点之一**：方案内部分支 | 当前不直接建边，后续可影响 task 编排 |
| ValidationPlan | 不主挂 | 不主挂 | **主挂载点**：方案需要哪些验收模板 | **显式建边**：由 verify Task 执行 |
| BusinessRule | 不主挂 | 可间接约束场景 | **主挂载点**：方案受哪些规则治理 | 间接相关，规则可被 verify Task 落地执行 |

---

## 本轮结论

1. 第二层最终保留 5 个对象：`Participant`、`Scope`、`DecisionPoint`、`ValidationPlan`、`BusinessRule`。
2. `RuntimeFlow` 删除，不再作为第二层独立对象保留。
3. `Participant` 与 `Scope` 都以 `DeliverySolution` 为主挂载点，分别回答“谁参与”和“对谁生效”。
4. `DecisionPoint` 允许 `NetworkScenario` 与 `DeliverySolution` 双层挂载，分别表达场景级分支和方案级分支。
5. `ValidationPlan` 与 `EngineeringTask(phase=verify)` 形成“验什么 / 怎么验”的清晰分层。
6. 原先的 `DiagnosisRule` 与 `RiskConstraint` 统一收敛为 `BusinessRule`，以 `rule_type` 区分校验、诊断、约束三类规则。
7. 第二层对象之间的关系已收敛为 9 条最小关系，足以支撑方案解释、配置核查和后续代码底座设计。
