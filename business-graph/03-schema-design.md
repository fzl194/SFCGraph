# 业务图谱 Schema 设计

## 1. 设计方法

对每个对象，按以下维度逐一分析：

1. **定义**：这个对象是什么，为什么需要它
2. **原始语料依据**：产品文档中的什么内容支撑这个对象
3. **当前实例**：final_v2 中实例化了什么
4. **边（关系）**：它与其他对象之间有什么连接
5. **内部属性**：它应该有哪些字段
6. **知识分层思考**：同一份源文档的知识如何分布到不同对象

## 2. BusinessDomain（业务域）

### 2.1 定义

**对象定位**：图谱的根节点，限定讨论边界。表示一类长期存在的工程知识空间。

**为什么需要**：业务图谱不是"一篇文档的改写"，而是"一个业务域的完整知识组织"。需要根节点来限定"我们在讨论什么"。

### 2.2 原始语料依据

来源文件：`output/UDG_.../业务感知功能描述/业务感知定义_92407879.md`

产品文档对"业务感知"的定义：
- SA = 在用户会话过程中，对用户数据报文进行解析，区分用户使用的不同业务
- 应用领域：内容计费、带宽控制、安全防护、行为分析
- 策略控制类型：门限控制、流量整形、流量监管、QoS更新、QoS标记、重定向、头增强
- 计费控制类型：在线计费、离线计费、融合计费，基于流量/时长/免费

**知识分层**：这份"定义"文档的知识分布在多个对象中：
- "SA是什么" → BusinessDomain 自身定义
- "应用领域（计费/带宽/安全/行为）" → NetworkScenario 的划分依据
- "策略控制类型" → DomainSemanticObject 的枚举
- "计费控制类型" → DomainSemanticObject 的枚举

### 2.3 当前实例

| 属性 | 值 |
|------|-----|
| domain_id | BD-BA |
| domain_name | 业务感知 |
| domain_summary | 围绕业务流识别、规则控制、计费、动作执行、验收诊断构建的业务域 |
| status | accepted |

成为 BusinessDomain 的 7 个条件（final_v2）：
1. 有明确业务目标
2. 有稳定的组织骨架（过滤条件→规则→策略）
3. 有稳定运行链
4. 有多类稳定业务场景
5. 有明显的控制面/用户面分工
6. 可向下桥接到特性和配置对象
7. 有稳定的产品结构支撑

### 2.4 边（关系）

当前边：
```
BusinessDomain --contains--> NetworkScenario
  "一个业务域由若干稳定业务场景组成"
```

**讨论**：BusinessDomain 是否还需要其他边？

- `BusinessDomain --has_participant--> Participant`？→ 业务域级别的参与方（如 UPF 是 SA 域的核心参与方）
- `BusinessDomain --defines--> DomainSemanticObject`？→ 域级语义对象（如 BA.FilterCondition 是 SA 域定义的）
- `BusinessDomain --supported_by--> Evidence`？→ 证明"业务感知"这个域存在的依据

目前只有 `contains` 一条边。但 final_v2 中第 7 条判断条件"有稳定的产品结构支撑"（PCF/SMF/UPF 分工、UDG 部署方式、License 约束）实际上是 BusinessDomain 级别的知识，不属于任何单个 Scenario。

### 2.5 内部属性

当前 CSV 只有 4 个字段：`domain_id, domain_name, domain_summary, status`

**建议属性**：

| 属性 | 类型 | 说明 | 依据 |
|------|------|------|------|
| domain_id | string | 唯一标识 | 当前已有 |
| domain_name | string | 域名称 | 当前已有 |
| domain_summary | string | 一句话定义 | 当前已有，来自产品文档的定义页 |
| core_mechanism | string | 核心组织骨架 | final_v2 第 2 条条件，如"过滤条件→规则→策略" |
| app_scopes | list[string] | 应用领域 | 产品文档定义页中的列举（计费/带宽/安全/行为） |
| cp_up_split | string | 控制面/用户面分工模式 | final_v2 第 5 条，如"PCF决策-SMF编排-UPF执行" |
| product_structure | string | 产品结构支撑 | final_v2 第 7 条 |
| status | string | 状态 | 当前已有 |

### 2.6 知识分层映射（原始语料 → 图谱对象）

| 源文档 | → BusinessDomain | → NetworkScenario | → DomainSemanticObject | → RuntimeFlow | → Participant | → 其他 |
|--------|-------------------|--------------------|------------------------|---------------|---------------|--------|
| **业务感知产生背景** | SA需求动机 | 场景驱动力 | — | — | — | — |
| **业务感知定义** | 核心定义 | 应用领域划分依据 | 策略控制类型枚举、计费控制类型枚举 | — | — | DecisionPoint |
| **业务感知过程** | 7步流程描述 | — | — | 7阶段主链骨架 | 各步骤参与网元 | Scope |
| **何为业务感知(What)** | SA本质定义 | — | Filter/Rule/Policy核心概念 | 包裹分拣类比 | — | — |
| **使用业务感知(Why)** | SA价值主张 | 场景价值分类 | — | — | — | — |
| **业务感知概览(How)** | 7步概览 | — | — | 7步运行链 | — | — |
| **UDG业务功能** | UDG能力全景 | — | — | — | UDG角色 | Feature |
| **华为5G Core解决方案** | 5GC架构定位 | — | — | — | PCF/SMF/UPF分工 | — |

**关键发现**："业务感知定义"这份文档的知识分布最广，支撑了 BD 自身定义 + NS 分类 + DSO 枚举 + DecisionPoint，这正是知识分层的典型例子。

### 2.7 待讨论

1. `core_mechanism` 是否应该是独立字段还是关联到 DomainSemanticObject？
2. BusinessDomain 是否应该直接连接 Participant（域级参与方）？
3. `app_scopes` 是否和 NetworkScenario 重复？（产品文档列出"内容计费、带宽控制、安全防护、行为分析"，但 NetworkScenario 是"计费、带宽控制、访问限制、本地分流"——**二者不一致**）
4. BusinessDomain 是否需要 `--supported_by--> Evidence` 边？（证明"业务感知"这个域存在的依据）

## 3. NetworkScenario（现网场景）

### 3.1 定义

**对象定位**：BusinessDomain 下的一级业务入口，表示一线工程师在实际网络中遇到的、需要被系统化解决的一类稳定业务问题情境。

**为什么需要**：
1. 一个业务域内部有多类截然不同的业务问题，需要把业务域拆成可讨论、可落地的一级分类
2. 向上承接 BusinessDomain 的边界约束，向下连接 DeliverySolution 和 DomainSemanticObject
3. 是业务主链的第二个节点，承上启下的枢纽

### 3.2 原始语料依据

- **业务感知定义**：SA 四大应用领域（内容计费/带宽控制/安全防护/行为分析）— 场景划分顶层依据
- **使用业务感知(Why)**：三大价值维度（计费精细化/带宽公平/安全防护）— 场景划分价值佐证
- **业务感知场景举例**：差异化计费+免费+配额耗尽重定向的综合闭环 — NS-01 综合原型
- **套餐1：计费场景**：4 个业务规则 + 完整 MML 对象链 — 直接支撑 NS-01
- **套餐2：带宽控制**：5 个业务规则 + BWM 对象链 — 直接支撑 NS-02
- **套餐3：访问限制**：4 个业务规则 + 多种策略类型 — 直接支撑 NS-03
- **Why分流 + How分流**：分流价值论证 + 运行机制（4种策略来源/3种UPF角色/5步流程）— 支撑 NS-04

### 3.3 当前实例

**final_v2 的 4 个粗粒度 NS**：

| 场景 | 业务目标 | 关键策略类型 |
|------|----------|-------------|
| NS-01 计费场景 | 对不同业务流采用不同计费方式，结合免费/默认/配额闭环 | PCC/URR |
| NS-02 带宽控制场景 | 对不同业务/用户施加差异化带宽控制，落实到QoS策略 | BWM |
| NS-03 访问限制场景 | 对指定业务流实施阻塞/重定向/头增强/Portal | PCC/HEADEN/IPREDIR |
| NS-04 本地分流场景 | 将本地业务数据导向本地DN/边缘DN | UL CL/分流规则 |

**CSV data 的 6 个细粒度 NS**（Phase 1 产物）：NS-BA-001~006，粒度与 final_v2 不一致。

### 3.4 边（关系）

```
BusinessDomain --contains--> NetworkScenario
NetworkScenario --instantiated_as--> DeliverySolution
  "一个场景可通过一个或多个方案落地"
NetworkScenario --uses_semantic_object--> DomainSemanticObject
  "该场景依赖哪些稳定语义对象"
```

建议增加：`NetworkScenario --overlaps_with--> NetworkScenario`（场景间交叉关系）

### 3.5 内部属性

建议属性：`scenario_id, scenario_name, scenario_summary, business_goal, judgment_basis(新增), typical_outcome(新增), applicable_policy_types(新增), scenario_group(新增), source_evidence_ids, status`

建议移除：`supporting_feature_codes_json, supporting_command_ids_json, supporting_object_chains_json`（跨层关系，应由关系表承载）

### 3.6 知识分层映射

| 源文档 | → NS | → 其他图谱对象 |
|--------|-------|---------------|
| **业务感知定义** | NS 顶层分类依据 | BD：SA 定义；DSO：策略/计费类型枚举 |
| **套餐1：计费** | NS-01 典型结构 | ConfigObject：完整对象链；Task：规划步骤 |
| **套餐2：带宽控制** | NS-02 典型结构 | ConfigObject：BWM 对象链 |
| **套餐3：访问限制** | NS-03 典型结构 | ConfigObject：PCCACTIONPROP/HEADEN/REDIRECT |
| **How分流** | NS-04 运行机制 | RuntimeFlow；Participant；DecisionPoint |

### 3.7 关键发现

1. **产品文档"应用领域"与 final_v2 NS 不完全一致**：定义页"安全防护"→ final_v2"访问限制"，"行为分析"消失，"本地分流"新增
2. **粒度冲突**：建议采用 final_v2 的 4 个粗粒度 NS，CSV 中的 6 个降级为二级场景
3. **场景划分准则**：独立业务问题 + 独立运行链 + 独立策略类型族
4. **CSV 只实现了 Phase 1**：NS-02 和 NS-04 无实例数据
5. **场景间交叉需要建模**：DS-05 横跨 NS-04+NS-01

### 3.8 待讨论

1. 场景粒度：采用 final_v2 的 4 个粗粒度 NS 还是保留 CSV 的 6 个细粒度 NS？
2. "行为分析"是否应恢复为独立 NS？
3. 场景间交叉关系如何建模？

## 4. DeliverySolution（交付方案）

### 4.1 定义

**对象定位**：业务图谱中**最重要的枢纽节点**。针对某个 NetworkScenario，基于产品文档归纳出的、由多种机制协同工作而形成的可落地方案闭包。

**核心价值不在自身的字段，而在它到其他对象的边**：
- DS 回答"这个场景我应该怎么做"（NS 回答"是什么问题"）
- DS 是连接"业务问题层"和"工程实现层"的枢纽
- DS 把场景推进到"一组机制如何一起工作"

### 4.2 原始语料依据

**核心问题：产品文档中是否有"方案"概念？**

产品文档中存在"方案"概念，但分布在不同层级：

| 文档中的概念 | 与 DS 的关系 |
|---|---|
| "计费解决方案概述" | 直接使用"解决方案"一词，DS-01/DS-02 的架构级依据 |
| "华为融合计费方案一/二/三" | DS 层的 DecisionPoint 依据——同一目标不同部署方案 |
| "业务套餐"（套餐1/2/3） | **配置案例**，不是方案本身。套餐验证 DS 的可行性 |
| "分流策略来源"（4种） | DS-05 的 DecisionPoint 依据 |
| "分流流程"（Step1-5） | DS-05 的 RuntimeFlow 依据 |

**套餐与 DS 的关系**：套餐是 DS 的具体配置验证实例。套餐1 给出了 4 个业务规则的具体参数值，DS-01 从中抽象出"过滤条件 + Rule优先级 + PCC/URR计费链 + 默认URR组"这组机制如何协同工作的模式。

**各源文档对 DS 的核心贡献**：
- **计费解决方案概述**：融合计费架构、计费方式分类、计费场景架构
- **融合计费概述**：三种组网方案、Participant 角色定义、NCG 影响的 RiskConstraint
- **套餐1**：DS-01 核心机制组合（IPLIST→FILTER→L7FILTER→FLOWFILTER→URR→URRGROUP→PCCPOLICYGRP→RULE→USERPROFILE）
- **套餐2**：DS-04 BWM 对象链组织模式
- **套餐3**：DS-03 多策略类型共存模式（PCC+HEADEN+IPREDIR）
- **How分流**：DS-05 完整流程和 Participant 角色
- **PCC静态规则**：DecisionPoint 核心依据（预定义/动态/本地），以及"PCF不具备七层识别能力"的关键约束

### 4.3 当前实例

| DS | 覆盖 NS | 核心机制组合 |
|---|---|---|
| DS-01 差异化计费组合方案 | NS-01 | 过滤条件 + Rule优先级 + PCC/URR计费链 + 默认URR组 + Trigger |
| DS-02 配额耗尽后体验切换方案 | NS-01(交叉) | 在线计费 + 配额管理 + RG级Trigger + 默认动作切换 |
| DS-03 访问限制组合方案 | NS-03 | 过滤条件 + Rule裁决 + PCC/HEADEN/IPREDIR/Portal 处理路径 |
| DS-04 带宽控制与QoS编排方案 | NS-02 | 过滤条件 + 静态/动态规则 + BWM/QoS策略 + QoS Flow映射 |
| DS-05 本地分流与独立计费方案 | NS-04(主)+NS-01(交叉) | App ID/预定义规则/动态规则 + UL CL/辅锚点 + 本地DN导向 + 独立计费 |

### 4.4 边（关系）——DS 的核心

DS 是图谱中边密度最高的节点：

```
NetworkScenario --instantiated_as--> DeliverySolution（M:N，支持交叉覆盖）
DeliverySolution --decomposes_to--> EngineeringTask（13条分解关系）
DeliverySolution --involves--> Participant（未对齐，无 CSV）
DeliverySolution --applies_to--> Scope（未对齐，无 CSV）
DeliverySolution --has_decision--> DecisionPoint（未对齐，无 CSV）
DeliverySolution --has_runtime_flow--> RuntimeFlow
DeliverySolution --validated_by--> ValidationPlan
DeliverySolution --diagnosed_by--> DiagnosisRule
DeliverySolution --constrained_by--> RiskConstraint
DeliverySolution --instantiates_semantic_object--> DomainSemanticObject
DeliverySolution --requires_capability--> Feature/Capability
DeliverySolution --realized_by_config--> ConfigObject（通过 Task 间接承载）
```

**对齐状态**：DS→Task、DS→DSO、DS→Evidence 已对齐（有 CSV）；DS→Participant、DS→Scope、DS→DecisionPoint 未对齐（只在 final_v2 markdown 中）。

### 4.5 内部属性

**原则：DS 自身属性不是核心，边才是。** 但 DS 仍需要基本字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| solution_id | string | 唯一标识 |
| solution_name | string | 方案名称 |
| covered_scenarios | list[NS_ID] | 覆盖的 NS（支持交叉覆盖） |
| core_mechanism_combo | text | 核心机制组合（DS 区别于 NS 名称的关键） |
| udg_focus | text | 用户面执行落点 |
| smf_focus | text | 控制面编排落点 |

### 4.6 知识分层映射

| 源文档 | DS 层获得什么 | 其他层获得什么 |
|---|---|---|
| **套餐1** | DS-01 核心机制组合模式 | NS：判断基础；Task：4个规划步骤；ConfigObject：完整对象链；DSO：FilterCondition/Rule/Priority/Charging |
| **套餐2** | DS-04 BWM 对象链组织 | NS：业务目标；Task：QoS规划；ConfigObject：BWM链；DSO：Policy/QoSOrchestration |
| **套餐3** | DS-03 多策略类型共存模式 | NS：判断基础；Task：导向规划；ConfigObject：PCCACTIONPROP/HEADEN/REDIRECT |
| **计费解决方案概述** | DS-01/DS-02 架构级依据 | DSO：Charging 维度；DecisionPoint：计费方式/粒度选择 |
| **融合计费概述** | DS-01/DS-02 组网方案选择 | Participant：SMF/CHF/UPF角色；RiskConstraint：NCG组网差异 |
| **How分流** | DS-05 完整流程 | RuntimeFlow：Step1-5；Participant：AMF/UL CL UPF；DecisionPoint：分流触发方式 |

**核心发现：一份套餐文档同时贡献了 4-6 个不同图谱对象类型的知识。**

### 4.7 关键发现

1. **DS 是唯一承担"方案"角色的节点**：去掉所有边，DS 退化为方案名；保留边，DS 变成有生命的方案骨架
2. **交叉覆盖是业务现实**：DS-02 跨 NS-01，DS-05 跨 NS-04+NS-01，NS→DS 是 M:N 关系
3. **Participant/Scope/DecisionPoint 三个支撑对象未数据化**：这是 DS 方案闭包语义打折扣的原因
4. **DS → Feature 关系较弱**：DS-01/02/03 的 Feature 依赖通过 Capability 间接实现，应显式补充

### 4.8 待讨论

1. DS 粒度：DS-02 是否应合并到 DS-01 成为一个 DecisionPoint 分支？
2. 交叉覆盖是否需要标注权重（primary/cross-cutting）？
3. DS → ConfigObject 是否应该直接化（不通过 Task 间接承载）？
4. DS 版本管理：产品演进时，DS 是否需要版本概念？

## 5. EngineeringTask（工程任务）

### 5.1 定义

**对象定位**：主链最后一个对象，是 DeliverySolution 分解出的可执行或可检查工作项。回答"具体要做什么事"。

**为什么需要**：DS 回答"一组机制怎么组合起来解决问题"，Task 把方案推进到一线可操作层面：先规划什么，再配置什么，最后验证什么。

**Task 与 DS 的区别**：
- DS = "把识别条件、Rule、计费对象和套餐绑成一条完整链" — 关注机制组合
- Task = "第一步设计识别条件、第二步设计计费对象链、第三步建立 Rule 绑定" — 关注可执行步骤

### 5.2 原始语料依据

**产品文档中的步骤天然分三个阶段**，以套餐1为例：

```
操作场景（= DS 层面）
  ├── 数据（= 规划态 Task）：业务编号/过滤条件/策略类型/策略/优先级的决策表
  ├── 脚本（= 执行态 Task）：8步 ADD 命令序列（IPLIST→FILTER→L7FILTER→FLOWFILTER→URR→RULE→USERPROFILE→RULEBINDING）
  └── 调测（= 验证态 Task）：LST 命令逐层回查配置链 + PFCP 消息验证
```

**三种阶段的知识结构差异显著**：

| 维度 | 规划态 | 执行态 | 验证态 |
|------|--------|--------|--------|
| 输入 | 业务需求描述 | 规划结果 + 对象依赖关系 | 配置结果 + 运行时现象 |
| 输出 | 决策表 | MML 命令序列（带参数值） | 通过/不通过判断 + 定位信息 |
| 使用命令 | 无（纯分析） | ADD/SET（创建修改） | LST（查询） |
| 知识来源 | 套餐文档"数据"部分 | 套餐文档"脚本"部分 | 调测文档"操作步骤"部分 |

### 5.3 当前实例

**final_v2 的 11 个 Task**：

| Task | 任务名称 | 阶段 |
|------|---------|------|
| TASK-01 | 规划生效范围 | plan |
| TASK-02 | 规划识别条件 | plan |
| TASK-03 | 规划 Rule 与优先级 | plan |
| TASK-04 | 规划计费对象与费率标识 | plan |
| TASK-05 | 规划配额耗尽动作 | plan |
| TASK-06 | 验证 CP/UP 一致性 | verify |
| TASK-07 | 规划导向与增强动作 | plan |
| TASK-08 | 规划分流触发与锚点插入 | plan |
| TASK-09 | 规划计费 Trigger 与多 UPF 配额 | plan |
| TASK-10 | 规划 QoS Flow 与策略更新 | plan |
| TASK-11 | 规划 RG 来源与初始配额申请 | plan |

**问题：11 个中只有 TASK-06 是验证态，执行态完全缺失。**

### 5.4 边（关系）

#### 已有

```
DeliverySolution --decomposes_to--> EngineeringTask（13条分解关系）
EngineeringTask --realized_by_config--> ConfigObject（30条映射）
```

#### 缺失的关系

| 缺失关系 | 为什么需要 |
|----------|----------|
| Task `precedes` Task | 套餐文档中 8 步配置有严格顺序依赖 |
| Task `verifies_config` ConfigObject | 验证态 Task 检查对象而非创建对象 |
| Task `references` Feature | 执行态 Task 需要知道要开哪些 License |
| Task `produces_evidence` | 验证态 Task 产生运行时证据（PFCP 消息、告警等） |

### 5.5 内部属性与 phase 讨论

#### 建议：选项 B（加 phase 字段）

理由：
1. 三种 Task 核心身份仍然是"工程任务"，只是阶段不同
2. 共享相同的边（`decomposes_to`、`realized_by_config`）
3. 拆成三个对象会导致 DS→Task 关系表需要三种关系类型
4. phase 字段允许新增阶段而不增加对象类型

#### 推荐属性

| 字段 | 类型 | 说明 |
|------|------|------|
| task_id | string | 唯一标识 |
| task_name | string | 任务名称 |
| task_summary | string | 任务摘要 |
| phase | enum(plan\|execute\|verify) | 阶段标记 |
| task_input | string | 主要输入 |
| task_output | string | 主要输出 |
| precondition | string | 前置条件 |
| config_object_ids | list[string] | 关联的配置对象 |
| source_evidence_ids | list[string] | 证据来源 |
| status | string | 数据状态 |

### 5.6 知识分层映射

| 源文档 | → EngineeringTask | → 其他图谱对象 |
|--------|-------------------|---------------|
| **套餐1 - 数据** | 规划态 Task（划分业务/设计识别条件/设计计费动作/设计Rule） | DS：DS-01；DSO：FilterCondition/Charging/Priority |
| **套餐1 - 脚本** | 执行态 Task（8步 ADD 命令序列） | ConfigObject：完整对象链 |
| **套餐2 - 脚本** | 执行态 Task（6步 BWM 对象链配置） | ConfigObject：BWM 系列对象 |
| **调测内容计费** | 验证态 Task（8步 LST 回查 + PFCP 验证） | RuntimeFlow：PFCP Session Report |
| **CP/UP URR 不一致** | 验证态 Task（故障排查） | DiagnosisRule；RiskConstraint |

### 5.7 关键发现

1. **执行态 Task 是配置生成的核心支撑**：每个执行态 Task 包含命令模板 + 参数槽位 + 依赖顺序，可直接作为配置生成流水线的模板源
2. **验证态 Task 是配置核查的核心支撑**：逐层 LST 命令序列 + 判断条件，可直接作为核查规则引擎的输入
3. **规划态和执行态有参数流转关系**：规划态的输出直接成为执行态的输入，Task 间 `precedes` 顺序依赖的依据
4. **当前 data 缺少执行态 Task**：以计费场景为例，套餐1 有 8 步执行配置，当前 CSV 中完全没有对应实例
5. **TASK-BA-001/006/011 没有 ConfigObject 映射**：纯规划和验证态 Task 不"产出"配置对象，需要不同的关系类型

### 5.8 待讨论

1. 执行态 Task 是否应该与命令图谱的 ProcedureStep 合并？（建议：Task 保留业务语义，ProcedureStep 保留命令语义，Task → ProcedureStep 连接）
2. 执行态 Task 的粒度：按 ConfigObject 类型分步 vs 按语义单元分步？（建议：按语义单元，因为一线工程师就是这么思考的）
3. 验证态 Task 与 ValidationPlan 的关系：ValidationPlan 定义验收策略（查什么/判什么），验证态 Task 执行验收动作（LST 哪个对象/对比什么值）
4. `realized_by_config` 关系是否需要拆分为 `creates_config`（执行态）和 `verifies_config`（验证态）？

## 6. 四对象汇总

### 6.1 主链关系图

```
BusinessDomain ──contains──> NetworkScenario ──instantiated_as──> DeliverySolution ──decomposes_to──> EngineeringTask
       │                          │                                    │                              │
       │                          │                                    │                              │
       │                          ├──uses_semantic_object──> DSO       ├──involves──> Participant      ├──realized_by_config──> ConfigObject
       │                          │                                    ├──applies_to──> Scope          ├──verifies_config──> ConfigObject
       │                          │                                    ├──has_decision──> DecisionPoint ├──precedes──> EngineeringTask
       │                          │                                    ├──has_runtime_flow──> Runtime  ├──references──> Feature
       │                          │                                    ├──validated_by──> Validation   │
       │                          │                                    ├──diagnosed_by──> Diagnosis    │
       │                          │                                    ├──constrained_by──> Risk       │
       │                          │                                    └──requires_capability──> Feature│
       │                          │                                                                    │
       └──supported_by──> Evidence└──supported_by──> Evidence             └──supported_by──> Evidence  └──supported_by──> Evidence
```

### 6.2 边密度分析

| 对象 | 出边数 | 定位 |
|------|--------|------|
| BusinessDomain | 1-4 | 根节点，边少但限定全局 |
| NetworkScenario | 2-3 | 承上启下枢纽 |
| **DeliverySolution** | **10+** | **边密度最高，图谱核心枢纽** |
| EngineeringTask | 2-5 | 终端节点，落地到配置对象 |

### 6.3 对齐状态汇总

| 对象 | 实体表 | 关系表 | 状态 |
|------|--------|--------|------|
| BusinessDomain | ✅ | ✅ | 已对齐 |
| NetworkScenario | ✅ | ✅ | 粒度不一致（4 vs 6） |
| DeliverySolution | ✅ | 部分 | Participant/Scope/DecisionPoint 未数据化 |
| EngineeringTask | ✅ | 部分 | 执行态/验证态严重缺失 |

### 6.4 待决策汇总

| 编号 | 问题 | 影响范围 |
|------|------|----------|
| D1 | NS 粒度：4 个粗粒度 vs 6 个细粒度 | NS 属性、NS→DS 关系 |
| D2 | "行为分析"是否恢复为独立 NS | NS 分类 |
| D3 | DS 粒度：DS-02 是否合并到 DS-01 | DS→Task 分解 |
| D4 | 交叉覆盖权重标注 | scenario_solution_mapping |
| D5 | Task phase 字段：plan/execute/verify | Task 属性、Task→ConfigObject 关系类型 |
| D6 | 执行态 Task 与 ProcedureStep 的关系 | 跨图谱桥接 |
| D7 | BD 是否增加 Participant/DSO/Evidence 边 | BD 边定义 |
| D8 | BD `app_scopes` 与 NS 的重复问题 | BD 属性定义 |

## 7. 决策讨论（基于原始语料的思路）

以下每个决策问题都基于原始产品文档的分析给出思路方向，供进一步讨论。

### D1: NS 粒度 — 4 个粗粒度 vs 6 个细粒度

**推荐：采用 4 个粗粒度 NS**

**语料证据**：
1. 产品文档按"套餐"组织场景，套餐1 同时包含专项计费/免费/兜底，从未将"免费业务"单独成篇
2. SA 定义文档归纳为 4 大应用领域，不是 6 个子类
3. 场景举例文档用一个用户场景就串联了"计费+免费+配额耗尽+重定向"，产品文档认为这些子问题是一个完整业务链路的不同阶段
4. 套餐目录结构只有 3 个文件（套餐1/2/3），对应 3 个粗粒度场景

**逻辑分析**：
- 细粒度 NS-BA-001/002/003 来自同一个套餐的同一次配置，绑定在同一个 UserProfile 上靠优先级协同，拆成独立场景导致 Agent 必须额外理解"这三个场景要合并到同一个套餐"
- 当前 DS-BA-001 = NS-001+002+003 的合并现象本身就是粒度错配的信号
- 粗粒度与产品文档"套餐"组织方式完全对齐，一线工程师说"配一个计费套餐"心里就是套餐1的全部内容

**细粒度知识的去处**：
当前的 6 个细粒度条目降级为 DeliverySolution 的子标签或 ProcedureVariant。检索链路变为：用户说"免费业务" → 语义匹配到 NS-BA-001(计费场景) → 读取 ReferencePattern 中业务3(免费业务)的配置样板 → 生成配置。多了一步但保证配置完整性。

### D2: "行为分析"是否恢复为独立 NS

**推荐：不恢复。"行为分析"不是独立配置场景，是 SA 应用价值的描述性归类。**

**语料证据**：
1. 产品文档中"行为分析"有四层含义：SA应用领域之一（唯一实例是 Tethering）、协议识别技术手段（H-SA）、NWDAF 终端行为分析（无关网元）、报表用户行为分析（数据采集能力）
2. "Why？"文档只列了三个价值维度（计费/带宽/安全），根本没有"行为分析"作为第四大领域
3. Tethering 配置链路依附于其他场景：检测结果最终匹配到规则后执行计费或带宽控制，复用 PCCPOLICYGRP/CATEGORYPROP
4. UDG/UNC 中没有名为"行为分析"的独立特性，Tethering 相关特性归类在"业务感知功能"下

**"行为分析"知识的去处**：
- Tethering 识别配置 → 计费或带宽控制 NS 的扩展子场景
- H-SA 启发式识别 → 特性图谱的 SA-Basic 特性下
- 报表用户行为分析 → 不属于 SA 策略执行范畴

### D3: DS-02 是否合并到 DS-01

**推荐：合并。DS-02 是 DS-01 在在线计费条件下的运行时阶段，不是独立方案。**

**语料证据**：
1. 场景举例文档用一个表格行就覆盖了"免费+计费+配额耗尽重定向"，三者在同一个 UserProfile 下靠 Rule 优先级和运行时状态切换协同工作
2. 在线计费文档将"重定向"列为在线计费的可选功能之一，不是独立业务场景
3. 调测文档明确前置依赖：欠费重定向调测的前提是"已完成配置到OCS的数据"

**配置链路对比**：基础配置对象 100% 重叠（IPLIST/FILTER/L7FILTER/FLOWFILTER/URR/URRGROUP/PCCPOLICYGRP/RULE/USERPROFILE），DS-02 仅额外增加 4 类对象（配额管理开关/在线计费模板/重定向服务器/default quota 参数），是叠加关系而非并列关系

**合并后 DS-01 的 DecisionPoint 设计**：
```
DS-01: 差异化计费组合方案
├── DecisionPoint: 计费模式 → 离线 | 在线
│   └── (在线分支) DecisionPoint: 配额耗尽后动作 → 无动作 | 重定向 | 降速
│       └── DecisionPoint: Default Quota → 启用 | 不启用
```

**DS 数量从 5 个变为 4 个**：DS-01(含配额分支)、DS-03(访问限制)、DS-04(带宽控制)、DS-05(本地分流)

### D4: 交叉覆盖权重标注

**推荐：不用 primary/cross-cutting，改用 dependency_type（required/optional/none）**

**语料证据**：
1. MEC 分流特性文档明确约束："UL CL方案只支持融合计费，否则UL CL分流功能无法正常使用" — 这是硬依赖，不是"顺便覆盖"
2. 分流流程中计费规则随 PFCP 会话建立自动下发，不是可选步骤
3. SA 场景中配额耗尽重定向是规则引擎内部的策略动作（POLICYTYPE=IPREDIR），不构成跨场景映射

**本质**：交叉不是覆盖程度差异，而是依赖方向差异。分流对计费有硬依赖，计费对分流无依赖。

**建议字段**：`dependency_type: required | optional | none`
- DS-05 → NS-04: required（交付目标）
- DS-05 → NS-01: required（硬依赖，没有计费基础设施分流跑不起来）
- DS-01 → NS-01: required（交付目标）
- DS-01 → NS-03: none（重定向是策略动作，不是场景依赖）

### D5: Task phase 字段

**推荐：必须加 phase 字段（plan/execute/verify）**

**语料证据**：
1. 套餐1 文档自身按"数据（规划）→脚本（执行）"两段式组织，这是产品文档对规划的天然分割
2. 调测文档按"前提条件→操作步骤"组织，步骤 7 的 LST 逐层回查（RULEBINDING→RULE→URR→FLOWFILTER），每层都有"与规划值一致/不一致"的分支判断 — 这是验证态的天然结构
3. 目录结构自身按阶段组织：`激活业务感知/`（执行）与 `调测业务感知/`（验证）是平级目录
4. 故障案例文档（现象→可能原因→处理步骤）是验证态的子类型"故障诊断"

**三种阶段的知识差异（5 个维度结构性差异）**：

| 维度 | plan | execute | verify |
|------|------|---------|--------|
| 输入 | 业务需求 | 规划结果+对象依赖 | 配置结果+运行时现象 |
| 输出 | 决策表 | MML 命令序列 | 通过/不通过+定位 |
| 命令角色 | 无 | ADD/SET | LST/EXP |
| ConfigObject 关系 | 无直接映射 | creates_config | verifies_config |
| 文档来源 | 套餐"数据"部分 | 套餐"脚本"部分 | 调测"操作步骤" |

**对使用场景的改善**：
- 配置生成：Agent 查 `phase='execute'` 获得有序执行态 Task → 生成 MML 脚本
- 配置核查：Agent 查 `phase='verify'` 获得验证态 Task → 生成核查报告

**与命令图谱 ProcedureStep 的关系**：两个层级保持分离。一个 execute Task（业务语义）包含多条 ProcedureStep（命令语义），通过 1:N 映射连接。ProcedureStep 在命令图谱中新增。

### D6: 执行态 Task 与 ProcedureStep 的关系

**推荐：分离为两个实体，通过 `task_executed_by_step` 映射关系连接**

**语料证据**：
- 套餐1 脚本步骤粒度 = 一组同类型命令的批量执行（如步骤5 含 12 条 ADD 命令），而非单条命令
- 脚本步骤粒度与 EngineeringTask 近似 1:1：步骤1-3 对应"设计识别条件"，步骤5 对应"设计计费动作"

**分离理由**：
- EngineeringTask 从业务需求分析而来，跨 NF 供应商（同时关联 UDG 和 UNC 的 ConfigObject）
- ProcedureStep 从配置范例/脚本中提取，绑定特定 NF 的命令序列，归属特性图谱层
- 粒度不同但可对齐：一个 execute Task 映射到 1-N 个有序 ProcedureStep

**命令图谱现状**：6 个模型（MMLCommand/CommandParameter/ConfigObject/CommandObjectAction/ConfigObjectRelationCandidate/Evidence），无 ProcedureStep。建议在特性图谱层新增。

### D7: BD 是否增加 Participant/DSO/Evidence 边

**推荐：三条候选边都不需要。**

**`BD --has_participant--> Participant`：不需要**
- PCF/SMF/UPF 分工是网络架构级全局知识（5GC 解决方案文档中描述），不是 SA 域特有
- 参与者角色在具体方案执行时才明确，应通过 `DS --involves--> Participant` 或 RuntimeFlow 承载
- 如果挂在 BD 下，隐含"这套分工是业务感知域特有的"，不准确（PCC、计费、QoS 也用同样的分工）

**`BD --defines--> DomainSemanticObject`：暂不需要**
- 语义上成立（DSO 的 `BA.` 前缀确实是域级概念），但当前只有 1 个 BD，关系退化为平凡
- 现有等价路径：`NS --uses_semantic_object--> DSO` + `DS --instantiates_semantic_object--> DSO` 已对齐
- 多 BD 时再正式化。当前可在 `business_domains.csv` 增加 JSON 字段 `semantic_profile_ref` 替代

**`BD --supported_by--> Evidence`：不需要**
- BD 的存在性由下层对象（NS/DS/Task）的证据网络间接证明，无独立的不可归约证据需求
- 域级文档（如"业务感知定义"）应支撑 DSO 的定义边界，而非 BD 实体

**核心原则**：图的边应该承载不可归约的语义关系。如果信息可从已有边的传递闭包推导，或当前实例使关系退化为平凡，则不需要该边。

### D8: BD `app_scopes` 与 NS 的重复问题

**推荐：保留 `app_scopes`，两者独立共存不做强制对齐**

**"应用领域"和"场景"不是同一个概念**：
- app_scopes = 产品定位/营销视角（"SA 能用在哪"），来自产品文档声明
- NS = 工程交付/操作视角（"一线工程师要配什么"），来自工程实践归纳
- 两者视角不同、来源不同、稳定性不同

**保留理由**：
1. 原始语料溯源 — 直接来自产品文档，删掉就断了溯源
2. 不一致本身有价值 — "安全防护"vs"访问限制"（语义变宽）、"行为分析"消失（非独立场景）、"本地分流"新增（独立语料）
3. 辅助语义检索 — 用户问"SA 安全防护"时，app_scopes 提供直接匹配入口

**具体做法**：
- BD `app_scopes` 保留原值 `["内容计费", "带宽控制", "安全防护", "行为分析"]`，不改
- NS 增加 `positioning_source` 属性：标注溯源自哪个 app_scope（可为 null）
  - NS-01 → "内容计费"，NS-02 → "带宽控制"，NS-03 → "安全防护"，NS-04 → null
- 不一致处恰好是知识边界：查询"行为分析无对应 NS"可定位到 D2 结论
