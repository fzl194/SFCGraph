# 计费场景特性图谱（新 Schema，v0.1）

> 范围：描述计费场景在新三层图谱 schema 下的特性图谱部分。
> 约束：对象、关系、属性命名尽量服从 `三层图谱Schema-最终版-v0.1.md` 与 `三层图谱本体标准定义.md`。
> 说明：本文件将 `Feature / SubFeature / FeatureRule / License / ConfigTask / FeatureTaskOrderEdge` 统一放在特性图谱侧表达；命令细节仍留给后续命令图谱文档。

---

## 0. 适用定义与来源

### 0.1 根定义

- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`
- `计费案例核心概念标准定义.md`

### 0.2 计费场景直接来源

- `business-graph/计费场景/feature-knowledge/cross-feature-analysis.md`
- `business-graph/计费场景/feature-knowledge/GWFD-020301-内容计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-020302-时长计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-020303-流量计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-020306-事件计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-020300-在线计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-010171-离线计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-010173-融合计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-020351-PCC基本功能.md`
- `business-graph/计费场景/feature-knowledge/GWFD-110101-SA-Basic.md`
- `business-graph/计费场景/feature-knowledge/WSFD-109002-内容计费.md`
- `business-graph/计费场景/feature-knowledge/WSFD-011201-离线计费.md`
- `business-graph/计费场景/feature-knowledge/WSFD-011202-热计费.md`
- `business-graph/计费场景/feature-knowledge/WSFD-011206-融合计费.md`
- `business-graph/计费场景/feature-knowledge/WSFD-109101-PCC基本功能.md`
- `business-graph/SKILL/feature/UDG/UPF/GWFD-020301/部署UPF_28493406.md`

---

## 1. 新 schema 对齐范围

本文件保留的新特性图谱对象：

- `Feature`
- `SubFeature`
- `License`
- `FeatureRule`
- `ConfigTask`
- `FeatureTaskOrderEdge`

本文件中的共享引用对象：

- `SemanticObject`
- `DecisionPoint`

本文件不展开：

- `MMLCommand`
- `CommandParameter`
- `ConfigObject`
- `CommandRule`
- `TaskCommandOrderEdge`

这些对象留给后续命令图谱文档。

---

## 2. 特性集合

### 2.1 Feature 判定原则

根据 `计费案例核心概念标准定义.md`：

> 有正式特性编号的，优先判定为 `Feature`，不是 `SubFeature`。

因此在计费场景里，下列对象直接按 `Feature` 处理。

### 2.2 UDG/UPF 侧 Feature

| `feature_id` | `feature_name` | `feature_summary` | `status` | `supported_by` |
|---|---|---|---|---|
| `GWFD-110101` | `SA-Basic` | 业务识别基础，内容计费和策略控制的前置能力 | `active` | `GWFD-110101-SA-Basic.md`, `cross-feature-analysis.md` |
| `GWFD-020351` | `PCC基本功能` | 用户面策略执行骨架，承接策略控制和计费执行 | `active` | `GWFD-020351-PCC基本功能.md`, `cross-feature-analysis.md` |
| `GWFD-020301` | `内容计费基本功能` | 内容计费能力底座，定义计费三件套与匹配规则链 | `active` | `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `GWFD-020302` | `基于业务时长的计费` | 内容计费增强形态，计量方式为 DURATION | `active` | `GWFD-020302-时长计费.md`, `cross-feature-analysis.md` |
| `GWFD-020303` | `基于业务流量的计费` | 内容计费增强形态，计量方式为 VOLUME | `active` | `GWFD-020303-流量计费.md`, `cross-feature-analysis.md` |
| `GWFD-020306` | `支持事件计费` | 内容计费增强形态，计量方式为 EVENT | `active` | `GWFD-020306-事件计费.md`, `cross-feature-analysis.md` |
| `GWFD-010171` | `离线计费` | 非实时计费能力，通过 Ga / GTP' 体系完成 | `active` | `GWFD-010171-离线计费.md`, `cross-feature-analysis.md` |
| `GWFD-020300` | `在线计费` | 实时配额计费能力，通过 Gy / OCS 完成 | `active` | `GWFD-020300-在线计费.md`, `cross-feature-analysis.md` |
| `GWFD-010173` | `融合计费` | 5G 统一计费架构，在同一会话内支持在线与离线 RG | `active` | `GWFD-010173-融合计费.md`, `cross-feature-analysis.md` |

### 2.3 UNC/SMF 侧 Feature

| `feature_id` | `feature_name` | `feature_summary` | `status` | `supported_by` |
|---|---|---|---|---|
| `WSFD-109101` | `PCC基本功能` | 控制面规则框架，接收策略并下发到用户面 | `active` | `WSFD-109101-PCC基本功能.md`, `cross-feature-analysis.md` |
| `WSFD-109002` | `内容计费基本功能` | 控制面计费编排能力，负责规则管理和上报 | `active` | `WSFD-109002-内容计费.md`, `cross-feature-analysis.md` |
| `WSFD-011201` | `支持离线计费` | 控制面离线计费能力，侧重 CG / CDR 路径 | `active` | `WSFD-011201-离线计费.md`, `cross-feature-analysis.md` |
| `WSFD-011202` | `支持热计费` | 离线计费增强形态，强调高优先级话单输出 | `active` | `WSFD-011202-热计费.md`, `cross-feature-analysis.md` |
| `WSFD-011206` | `支持融合计费` | 控制面融合计费能力，包含 CCT、N40、CHF 交互闭环 | `active` | `WSFD-011206-融合计费.md`, `cross-feature-analysis.md` |

---

## 3. 子特性集合

### 3.1 SubFeature 判定原则

根据 `计费案例核心概念标准定义.md`：

> `SubFeature` 是单个正式特性内部的稳定细分形态；必须隶属于某一个 `Feature`，能被稳定重复引用，且没有自己的正式特性编号。

### 3.2 当前保留的 SubFeature

当前仅保留在现有材料中有稳定证据、且确实不存在独立特性编号的细分形态。

| `subfeature_id` | `parent_feature_id` | `subfeature_name` | `subfeature_summary` | `supported_by` |
|---|---|---|---|---|
| `SF-GWFD-020301-URL` | `GWFD-020301` | `基于URL的内容识别计费` | 在内容计费基本功能内部，通过 L7FILTER + URL 条件识别具体网站业务并计费 | `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `SF-GWFD-020301-L34` | `GWFD-020301` | `基于L34的内容识别计费` | 在内容计费基本功能内部，通过 FILTER / FILTERIPV6 的三四层条件识别业务并计费 | `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `SF-GWFD-020301-ANY` | `GWFD-020301` | `默认any兜底计费` | 在内容计费基本功能内部，对未被特定规则命中的基础业务配置默认计费 | `部署UPF_28493406.md` |
| `SF-GWFD-020301-ABNORMAL` | `GWFD-020301` | `异常流量缺省计费` | 在内容计费基本功能内部，对未命中过滤条件的异常场景流量配置默认信令或异常费率 | `部署UPF_28493406.md` |

### 3.3 明确不作为 SubFeature 的对象

下列对象虽然语义上更细，但根据根定义和 `cross-feature-analysis.md`，都应保留为正式 `Feature`：

- `GWFD-020302 基于业务时长的计费`
- `GWFD-020303 基于业务流量的计费`
- `GWFD-020306 支持事件计费`
- `GWFD-010173 融合计费`

---

## 4. License 集合

### 4.1 License 对象

| `license_id` | `license_name` | `license_summary` | `supported_by` |
|---|---|---|---|
| `LKV3G5SABS01` | `SA-Basic` | UDG/UPF 侧 SA-Basic 许可项 | `cross-feature-analysis.md`, `GWFD-110101-SA-Basic.md` |
| `LKV3G5PCCB01` | `PCC基本功能` | UDG/UPF 侧 PCC 基础许可项 | `cross-feature-analysis.md`, `GWFD-020351-PCC基本功能.md` |
| `LKV3G5BCBC01` | `内容计费基本功能` | UDG/UPF 侧内容计费基础许可项 | `cross-feature-analysis.md`, `GWFD-020301-内容计费.md` |
| `LKV3G5TBCS01` | `基于业务时长的计费` | UDG/UPF 侧时长计费许可项 | `cross-feature-analysis.md`, `GWFD-020302-时长计费.md` |
| `LKV3G5VBCS01` | `基于业务流量的计费` | UDG/UPF 侧流量计费许可项 | `cross-feature-analysis.md`, `GWFD-020303-流量计费.md` |
| `LKV3G5EBCS01` | `支持事件计费` | UDG/UPF 侧事件计费许可项 | `cross-feature-analysis.md`, `GWFD-020306-事件计费.md` |
| `LKV3G5OLCH01` | `在线计费` | UDG/UPF 侧在线计费许可项 | `cross-feature-analysis.md`, `GWFD-020300-在线计费.md` |
| `LKV3W9SPCC11` | `PCC基本功能` | UNC/SMF 侧 PCC 许可项 | `cross-feature-analysis.md`, `WSFD-109101-PCC基本功能.md` |
| `LKV3W9BCC12` | `内容计费基本功能` | UNC/SMF 侧内容计费许可项 | `cross-feature-analysis.md`, `WSFD-109002-内容计费.md` |

### 4.2 无需额外 License 的特性

根据现有文档，下列特性作为 `Feature` 保留，但不新增独立 `License` 依赖关系：

- `GWFD-010171 离线计费`
- `GWFD-010173 融合计费`
- `WSFD-011201 支持离线计费`
- `WSFD-011206 支持融合计费`

---

## 5. ConfigTask 集合

### 5.1 ConfigTask 判定原则

根据 `计费案例核心概念标准定义.md`：

> `Task` 是最小可复用配置原子。

根据 `三层图谱本体标准定义.md`：

> `ConfigTask` 是最小可复用配置原子，用于把特性能力与底层命令解耦。

### 5.2 Task 实例表

| `task_id` | `task_name` | `task_scope_type` | `task_goal` | `input_contract` | `output_contract` | `status` | `supported_by` |
|---|---|---|---|---|---|---|---|
| `T-PLAN-001` | `规划生效范围` | `cross_feature` | 确定策略对谁生效，规划 UserProfile、DNN/APN 与默认兜底范围 | 用户范围定义、DNN/APN规划、默认兜底要求 | UserProfile 名称与结构规划、默认绑定规划 | `active` | `01计费场景业务图谱.md` |
| `T-PLAN-002` | `规划识别条件` | `feature_specific` | 将业务描述翻译成 FILTER / L7FILTER / PROTBINDFLOWF 规划 | 业务描述（协议、URL、地址、端口） | 过滤条件规划表 | `active` | `01计费场景业务图谱.md`, `部署UPF_28493406.md` |
| `T-PLAN-003` | `规划Rule与优先级` | `feature_specific` | 决定多业务重叠时的 Rule 层次和优先级 | 多类业务目标、过滤条件交集 | Rule 排序与 OR 合并方案 | `active` | `01计费场景业务图谱.md`, `GWFD-020301-内容计费.md` |
| `T-PLAN-004` | `规划计费对象与费率标识` | `cross_feature` | 规划 URR→URRGROUP→PCCPOLICYGRP 及 RG / SID / URRID | 资费模型、计费方式、RG/SID 规划 | 计费对象规划表 | `active` | `01计费场景业务图谱.md`, `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `T-PLAN-005` | `规划配额耗尽动作` | `feature_specific` | 规划在线或融合计费场景的配额耗尽动作 | 配额控制要求、用户体验要求 | BLOCK / REDIRECT / FORWARD 策略 | `active` | `01计费场景业务图谱.md` |
| `T-EXEC-001` | `配置IP地址列表` | `feature_specific` | 配置 IPLIST 供特定IP匹配使用 | 服务器IP规划 | IPLIST配置 | `active` | `01计费场景业务图谱.md`, `部署UPF_28493406.md` |
| `T-EXEC-002` | `配置三四层过滤条件` | `feature_specific` | 配置 L34 过滤条件 | 过滤条件规划表 | FILTER / FILTERIPV6 配置 | `active` | `01计费场景业务图谱.md`, `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `T-EXEC-003` | `配置七层过滤条件` | `feature_specific` | 配置 L7 URL / Host 过滤条件 | 七层过滤条件规划表 | L7FILTER 配置 | `active` | `01计费场景业务图谱.md`, `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `T-EXEC-004` | `配置流过滤器与绑定` | `feature_specific` | 组合 FILTER / L7FILTER 并绑定到 FLOWFILTER | FILTER、L7FILTER、协议规划 | FLOWFILTER、FLTBINDFLOWF、PROTBINDFLOWF | `active` | `01计费场景业务图谱.md`, `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `T-EXEC-005` | `配置计费动作链` | `cross_feature` | 创建 URR→URRGROUP→PCCPOLICYGRP 计费动作链 | URR/URRGROUP/PCCPOLICYGRP 规划表 | 计费对象链配置 | `active` | `01计费场景业务图谱.md`, `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `T-EXEC-008` | `配置Rule` | `cross_feature` | 绑定 FLOWFILTER 与 PCCPOLICYGRP 并设置优先级 | FLOWFILTER、PCCPOLICYGRP、优先级规划 | RULE 配置 | `active` | `01计费场景业务图谱.md`, `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `T-EXEC-010` | `配置UserProfile与Rule绑定` | `cross_feature` | 创建 USERPROFILE，绑定 RULE 和默认计费组 | Rule、默认URR组、UserProfile规划 | USERPROFILE、RULEBINDING、URRGRPBINDING | `active` | `01计费场景业务图谱.md`, `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `T-EXEC-011` | `核查SMF系统级计费前置` | `feature_specific` | 核查 PCC 开关、计费接口模式、融合计费使能和 CHF 交互前置 | DP-00、DP-01、DNN/APN规划、UserProfile规划 | 系统级前置核查结果 | `active` | `01计费场景业务图谱.md`, `WSFD-011206-融合计费.md` |
| `T-EXEC-012` | `配置SMF到CHF的N40接入与选择链` | `feature_specific` | 配置或核查 SMF 到 CHF 的 SBI/N40 接入对象链 | DP-00、DP-01、CC规划、CHF实例规划 | HTTPLEGRP / SBIAPLE / TNFGRP / SELECTCHFGBYCC 等对象链 | `active` | `01计费场景业务图谱.md`, `WSFD-011206-融合计费.md` |
| `T-EXEC-013` | `配置SMF模板、Trigger与异常处理` | `feature_specific` | 配置或核查 CCT 模板、Trigger、异常处理与缓存策略 | DP-00、DP-01、CC规划、CHF接入结果 | CCT、SELECTCCTBYCC、PDUTRIGGER、RGTRIGGER 等配置 | `active` | `01计费场景业务图谱.md`, `WSFD-011206-融合计费.md` |
| `T-VERIFY-001` | `验证License开关` | `generic` | 验证相关 License 或功能开关状态 | 相关 License 开关对象 | License 验证结果 | `active` | `01计费场景业务图谱.md` |
| `T-VERIFY-002` | `验证配置链逐层回查` | `generic` | 逐层核查配置链对象与绑定关系 | 配置链清单 | 配置链回查结果 | `active` | `01计费场景业务图谱.md` |
| `T-VERIFY-003` | `验证PFCP会话上报与计费流量` | `generic` | 核查 PFCP Session Report 和计费流量上报 | 配置链回查结果、PFCP跟踪任务 | PFCP 上报验证结果 | `active` | `01计费场景业务图谱.md` |

---

## 6. FeatureRule 集合

### 6.1 FeatureRule 定义

根据 `三层图谱本体标准定义.md`：

> `FeatureRule` 是特性层规则。它约束特性依赖关系、子特性选择、task 选择、命名一致性、跨 NF 一致性和特性级限制条件。

### 6.2 Rule 实例表

| `rule_id` | `rule_name` | `rule_scope` | `rule_logic` | `supported_by` |
|---|---|---|---|---|
| `FR-01` | `内容计费依赖SA-Basic` | `GWFD-020301` | 内容计费必须依赖 SA-Basic 提供业务识别能力 | `GWFD-020301-内容计费.md`, `cross-feature-analysis.md` |
| `FR-02` | `内容计费依赖在线或离线计费方式` | `GWFD-020301 / WSFD-109002` | 使用在线计费系统时依赖在线计费特性，使用离线计费系统时依赖离线计费特性 | `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `FR-03` | `跨网元名称一致性` | `GWFD-020301 / WSFD-109002` | USERPROFILENAME、RULENAME、POLICYTYPE、POLICYNAME 等在 PCF/SMF/UPF 之间需保持一致 | `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `FR-04` | `跨网元URR参数一致性` | `GWFD-020301 / WSFD-109002` | URRID、USAGERPTMODE、OFFMETERINGTYPE、ONLMETERINGTYPE 在 SMF 和 UPF 上必须一致 | `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `FR-05` | `默认any兜底规则优先级最低` | `SF-GWFD-020301-ANY` | any 过滤条件的 RULE 优先级应设置为最低，作为兜底策略 | `部署UPF_28493406.md` |
| `FR-06` | `L34规则优先级低于L7规则` | `SF-GWFD-020301-L34 / SF-GWFD-020301-URL` | 只绑定三四层 filter 的 RULE 优先级应低于绑定七层 filter 的 RULE 优先级 | `部署UPF_28493406.md` |
| `FR-07` | `FLOWFILTER必须绑定过滤条件` | `GWFD-020301` | FLOWFILTER 必须绑定过滤条件，否则对应 Rule 为无效配置 | `部署UPF_28493406.md` |
| `FR-08` | `融合计费RGAPPLIED约束` | `GWFD-010173 / WSFD-011206` | RGAPPLIED 取值会改变 URRGROUP 中在线/离线 URR 的组合约束 | `GWFD-010173-融合计费.md`, `WSFD-011206-融合计费.md` |
| `FR-09` | `融合计费不支持多UPF共享在线RG配额` | `WSFD-011206` | 多 UPF 场景不支持共享在线计费 RG 配额 | `WSFD-011206-融合计费.md` |
| `FR-10` | `事件计费仅SCUR模式` | `GWFD-020306` | 事件计费只支持 SCUR 模式，并带特定约束 | `GWFD-020306-事件计费.md`, `cross-feature-analysis.md` |

---

## 7. 关系定义

### 7.1 has_subfeature

| 起点 | 关系 | 终点 |
|---|---|---|
| `GWFD-020301` | `has_subfeature` | `SF-GWFD-020301-URL` |
| `GWFD-020301` | `has_subfeature` | `SF-GWFD-020301-L34` |
| `GWFD-020301` | `has_subfeature` | `SF-GWFD-020301-ANY` |
| `GWFD-020301` | `has_subfeature` | `SF-GWFD-020301-ABNORMAL` |

### 7.2 depends_on

| 起点 | 关系 | 终点 | 说明 |
|---|---|---|---|
| `GWFD-020301` | `depends_on` | `GWFD-110101` | 内容计费依赖 SA-Basic |
| `GWFD-020302` | `depends_on` | `GWFD-020301` | 时长计费是内容计费增强形态 |
| `GWFD-020303` | `depends_on` | `GWFD-020301` | 流量计费是内容计费增强形态 |
| `GWFD-020306` | `depends_on` | `GWFD-020301` | 事件计费是内容计费增强形态 |
| `GWFD-020300` | `depends_on` | `GWFD-020351` | 在线计费需要 PCC 配额控制骨架 |
| `GWFD-010173` | `depends_on` | `GWFD-020301` | 融合计费依赖内容计费底座 |
| `WSFD-109002` | `depends_on` | `WSFD-109101` | 控制面内容计费依赖 PCC 规则框架 |
| `WSFD-011206` | `depends_on` | `WSFD-109002` | 控制面融合计费依赖内容计费编排能力 |

### 7.3 requires_license

| 起点 | 关系 | 终点 |
|---|---|---|
| `GWFD-110101` | `requires_license` | `LKV3G5SABS01` |
| `GWFD-020351` | `requires_license` | `LKV3G5PCCB01` |
| `GWFD-020301` | `requires_license` | `LKV3G5BCBC01` |
| `GWFD-020302` | `requires_license` | `LKV3G5TBCS01` |
| `GWFD-020303` | `requires_license` | `LKV3G5VBCS01` |
| `GWFD-020306` | `requires_license` | `LKV3G5EBCS01` |
| `GWFD-020300` | `requires_license` | `LKV3G5OLCH01` |
| `WSFD-109101` | `requires_license` | `LKV3W9SPCC11` |
| `WSFD-109002` | `requires_license` | `LKV3W9BCC12` |

### 7.4 uses_semantic_object

| 起点 | 关系 | 终点 |
|---|---|---|
| `GWFD-020301` | `uses_semantic_object` | `BA.FilterCondition` |
| `GWFD-020301` | `uses_semantic_object` | `BA.Rule` |
| `GWFD-020301` | `uses_semantic_object` | `BA.Binding` |
| `GWFD-020301` | `uses_semantic_object` | `BA.Charging` |
| `GWFD-020302` | `uses_semantic_object` | `BA.Charging` |
| `GWFD-020303` | `uses_semantic_object` | `BA.Charging` |
| `GWFD-020306` | `uses_semantic_object` | `BA.Charging` |
| `GWFD-010173` | `uses_semantic_object` | `BA.Quota` |
| `WSFD-109002` | `uses_semantic_object` | `BA.Rule` |
| `WSFD-109002` | `uses_semantic_object` | `BA.Charging` |
| `WSFD-011206` | `uses_semantic_object` | `BA.Quota` |

### 7.5 constrained_by

| 起点 | 关系 | 终点 |
|---|---|---|
| `GWFD-020301` | `constrained_by` | `FR-01` |
| `GWFD-020301` | `constrained_by` | `FR-02` |
| `GWFD-020301` | `constrained_by` | `FR-03` |
| `GWFD-020301` | `constrained_by` | `FR-04` |
| `SF-GWFD-020301-ANY` | `constrained_by` | `FR-05` |
| `SF-GWFD-020301-L34` | `constrained_by` | `FR-06` |
| `SF-GWFD-020301-URL` | `constrained_by` | `FR-06` |
| `GWFD-020301` | `constrained_by` | `FR-07` |
| `GWFD-010173` | `constrained_by` | `FR-08` |
| `WSFD-011206` | `constrained_by` | `FR-08` |
| `WSFD-011206` | `constrained_by` | `FR-09` |
| `GWFD-020306` | `constrained_by` | `FR-10` |

### 7.6 decomposes_to

#### 内容计费基础特性

| 起点 | 关系 | 终点 |
|---|---|---|
| `GWFD-020301` | `decomposes_to` | `T-PLAN-001` |
| `GWFD-020301` | `decomposes_to` | `T-PLAN-002` |
| `GWFD-020301` | `decomposes_to` | `T-PLAN-003` |
| `GWFD-020301` | `decomposes_to` | `T-PLAN-004` |
| `GWFD-020301` | `decomposes_to` | `T-EXEC-001` |
| `GWFD-020301` | `decomposes_to` | `T-EXEC-002` |
| `GWFD-020301` | `decomposes_to` | `T-EXEC-003` |
| `GWFD-020301` | `decomposes_to` | `T-EXEC-004` |
| `GWFD-020301` | `decomposes_to` | `T-EXEC-005` |
| `GWFD-020301` | `decomposes_to` | `T-EXEC-008` |
| `GWFD-020301` | `decomposes_to` | `T-EXEC-010` |
| `GWFD-020301` | `decomposes_to` | `T-VERIFY-001` |
| `GWFD-020301` | `decomposes_to` | `T-VERIFY-002` |
| `GWFD-020301` | `decomposes_to` | `T-VERIFY-003` |

#### 内容计费细分形态

| 起点 | 关系 | 终点 |
|---|---|---|
| `SF-GWFD-020301-URL` | `decomposes_to` | `T-EXEC-003` |
| `SF-GWFD-020301-URL` | `decomposes_to` | `T-EXEC-004` |
| `SF-GWFD-020301-L34` | `decomposes_to` | `T-EXEC-001` |
| `SF-GWFD-020301-L34` | `decomposes_to` | `T-EXEC-002` |
| `SF-GWFD-020301-L34` | `decomposes_to` | `T-EXEC-004` |
| `SF-GWFD-020301-ANY` | `decomposes_to` | `T-PLAN-003` |
| `SF-GWFD-020301-ANY` | `decomposes_to` | `T-EXEC-008` |
| `SF-GWFD-020301-ANY` | `decomposes_to` | `T-EXEC-010` |
| `SF-GWFD-020301-ABNORMAL` | `decomposes_to` | `T-EXEC-010` |

#### 计量方式增强特性

| 起点 | 关系 | 终点 |
|---|---|---|
| `GWFD-020302` | `decomposes_to` | `T-PLAN-004` |
| `GWFD-020302` | `decomposes_to` | `T-EXEC-005` |
| `GWFD-020303` | `decomposes_to` | `T-PLAN-004` |
| `GWFD-020303` | `decomposes_to` | `T-EXEC-005` |
| `GWFD-020306` | `decomposes_to` | `T-PLAN-004` |
| `GWFD-020306` | `decomposes_to` | `T-EXEC-005` |

#### 融合计费控制面特性

| 起点 | 关系 | 终点 |
|---|---|---|
| `WSFD-011206` | `decomposes_to` | `T-EXEC-011` |
| `WSFD-011206` | `decomposes_to` | `T-EXEC-012` |
| `WSFD-011206` | `decomposes_to` | `T-EXEC-013` |
| `GWFD-010173` | `decomposes_to` | `T-PLAN-005` |

### 7.7 orchestrates（FeatureTaskOrderEdge）

#### Edge 实例表

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `supported_by` |
|---|---|---|---|---|---|---|---|---|---|
| `FTE-001` | `feature` | `GWFD-020301` | `T-PLAN-002` | `T-PLAN-003` | `precedes` | - | `required` | 识别条件规划结果 | `01计费场景业务图谱.md` |
| `FTE-002` | `feature` | `GWFD-020301` | `T-PLAN-003` | `T-PLAN-004` | `precedes` | - | `required` | Rule与优先级规划 | `01计费场景业务图谱.md` |
| `FTE-003` | `feature` | `GWFD-020301` | `T-EXEC-004` | `T-EXEC-008` | `depends_on` | - | `required` | FLOWFILTER 名称 | `01计费场景业务图谱.md`, `部署UPF_28493406.md` |
| `FTE-004` | `feature` | `GWFD-020301` | `T-EXEC-005` | `T-EXEC-008` | `depends_on` | - | `required` | PCCPOLICYGRP 名称 | `01计费场景业务图谱.md`, `部署UPF_28493406.md` |
| `FTE-005` | `feature` | `GWFD-020301` | `T-EXEC-008` | `T-EXEC-010` | `precedes` | - | `required` | RULE 名称 | `01计费场景业务图谱.md` |
| `FTE-006` | `feature` | `GWFD-020301` | `T-EXEC-010` | `T-VERIFY-002` | `precedes` | - | `required` | USERPROFILE / 绑定关系 | `01计费场景业务图谱.md` |
| `FTE-007` | `subfeature` | `SF-GWFD-020301-ANY` | `T-EXEC-008` | `T-EXEC-010` | `fallback_to` | - | `required` | any兜底 Rule 和默认计费绑定 | `部署UPF_28493406.md` |
| `FTE-008` | `feature` | `WSFD-011206` | `T-EXEC-011` | `T-EXEC-012` | `precedes` | `DP-00` | `required` | CCVALUE / 计费接口模式 | `01计费场景业务图谱.md`, `WSFD-011206-融合计费.md` |
| `FTE-009` | `feature` | `WSFD-011206` | `T-EXEC-012` | `T-EXEC-013` | `precedes` | `DP-01` | `required` | CHF组 / CCT 选择条件 | `01计费场景业务图谱.md`, `WSFD-011206-融合计费.md` |
| `FTE-010` | `feature` | `GWFD-020301` | `T-EXEC-010` | `T-VERIFY-003` | `must_be_last` | - | `required` | 完整计费链和默认绑定完成后再核查PFCP上报 | `01计费场景业务图谱.md` |

---

## 8. 当前边界结论

基于新 schema，计费场景的特性图谱边界明确为：

1. **保留**
   - 正式特性集合
   - 单个特性内部真正稳定的 `SubFeature`
   - `License`
   - `FeatureRule`
   - `ConfigTask`
   - `FeatureTaskOrderEdge`

2. **引用但不展开**
   - `SemanticObject`
   - `DecisionPoint`

3. **不在特性图谱中继续下沉**
   - `MMLCommand`
   - `CommandParameter`
   - `ConfigObject`
   - `CommandRule`

这些命令层对象将由后续命令图谱文档承接。

---

## 9. 对业务图谱的反向补强建议

当前业务图谱已经可以先收口，但要进一步变完整，需要等命令图谱出来后再反向优化以下内容：

1. `ConfigurationSolution -> uses_feature`
   - 需要和本文件的正式 `Feature` 集合完全对齐

2. `ConfigurationSolution -> uses_task`
   - 需要和本文件的 `ConfigTask` 集合完全对齐

3. `ConfigurationSolution / NetworkScenario -> uses_semantic_object`
   - 需要和本文件的 `Feature -> uses_semantic_object` 形成上下贯通

4. `BusinessRule` 与 `FeatureRule`
   - 需要进一步分层，避免业务层继续承接本应属于能力层的规则

---

## 10. 下一步接口

后续 `03-计费场景-命令图谱-新schema-v0.1.md` 需要承接本文中的：

- `ConfigTask.command_refs`
- `TaskCommandOrderEdge`
- `ConfigObject`
- `CommandRule`
- `MMLCommand`
- `CommandParameter`

