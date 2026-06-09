# 带宽控制场景跨层映射关系总表（新 Schema，v0.1）

> 范围：汇总带宽控制场景（业务感知套餐2）五层图谱之间的跨层映射关系。
> 约束：严格服从 `三层图谱Schema-最终版-v0.1.md` §12 跨层映射 + §13 禁止关系。
> 目的：确保端到端链路完整性，验证 BD→NS→CS→Feature→Task→Command→Object 可追溯。

---

## 0. 跨层映射关系全景

```text
BusinessDomain (BD-BW-01 业务感知)
  └─contains→ NetworkScenario (NS-BW-01 带宽控制场景)
       └─instantiated_as→ ConfigurationSolution (CS-BW-01~07)
            ├─uses_feature→ Feature (24个)
            │    └─decomposes_to→ ConfigTask (~30个)
            │         ├─invokes→ MMLCommand (~55个)
            │         └─targets→ SemanticObject/ConfigObject
            ├─uses_task→ ConfigTask (方案直接复用通用task)
            ├─has_decision→ DecisionPoint (DP-BW-01~08)
            ├─constrained_by→ BusinessRule (BR-BW-01~06)
            └─uses_semantic_object→ SemanticObject (SO-BW-01~08)
```

---

## 1. CS → Feature（uses_feature）

| CS | Feature | 关系 | 说明 |
| --- | --- | --- | --- |
| `CS-BW-01` SA-BWM带宽控制方案 | `GWFD-110311` | `uses_feature` | UDG侧BWM核心 |
| `CS-BW-01` | `WSFD-211005` | `uses_feature` | UNC侧BWM规则管理 |
| `CS-BW-01` | `GWFD-110101` | `uses_feature` | SA识别基础 |
| `CS-BW-01` | `GWFD-020351` | `uses_feature` | UDG PCC基础 |
| `CS-BW-01` | `WSFD-109101` | `uses_feature` | UNC PCC基础 |
| `CS-BW-01` | `GWFD-020354` | `uses_feature` | Shaping（可选组合） |
| `CS-BW-01` | `GWFD-110313` | `uses_feature` | 智能Shaping（可选增强） |
| `CS-BW-02` FUP配额降速方案 | `GWFD-020353` | `uses_feature` | UDG会话FUP |
| `CS-BW-02` | `WSFD-109104` | `uses_feature` | UNC会话FUP |
| `CS-BW-02` | `GWFD-110312` | `uses_feature` | UDG业务FUP（可选） |
| `CS-BW-02` | `WSFD-211009` | `uses_feature` | UNC业务FUP（可选） |
| `CS-BW-03` GBR带宽保证方案 | `GWFD-020358` | `uses_feature` | UDG QoS保证 |
| `CS-BW-03` | `WSFD-109107` | `uses_feature` | UNC QoS保证 |
| `CS-BW-04` ADC应用感知动态带宽方案 | `GWFD-020357` | `uses_feature` | UDG ADC |
| `CS-BW-04` | `WSFD-109102` | `uses_feature` | UNC ADC |
| `CS-BW-05` 小区负荷动态带宽方案 | `GWFD-110332` | `uses_feature` | UDG小区负荷 |
| `CS-BW-05` | `WSFD-211101` | `uses_feature` | UNC小区负荷 |
| `CS-BW-06` 位置区域差异化带宽方案 | `WSFD-109108` | `uses_feature` | UNC接入点策略 |
| `CS-BW-07` 无线资源优化标记方案 | `GWFD-020359` | `uses_feature` | IM管控 |
| `CS-BW-07` | `GWFD-110301` | `uses_feature` | 码率差异化 |
| `CS-BW-07` | `GWFD-110302` | `uses_feature` | 视频解耦 |
| `CS-BW-07` | `GWFD-110331` | `uses_feature` | FPI标记 |

> 辅助特性（不单独建方案，通过依赖和规则表达）：`GWFD-020305` 异常检测、`GWFD-111600` SA特征库管控。

---

## 2. CS → ConfigTask（uses_task）

| CS | ConfigTask | 关系 | 说明 |
| --- | --- | --- | --- |
| `CS-BW-01` | `T-007` | `uses_task` | License开启 |
| `CS-BW-01` | `T-008` | `uses_task` | SA特征库加载 |
| `CS-BW-01` | `T-101`~`T-106` | `uses_task` | BWM三级控制配置 |
| `CS-BW-01` | `T-006` | `uses_task` | 策略刷新（must_be_last） |
| `CS-BW-02` | `T-007`, `T-201`~`T-205`, `T-003`~`T-005` | `uses_task` | FUP配置链 |
| `CS-BW-03` | `T-007`, `T-301`~`T-303`, `T-003`~`T-005` | `uses_task` | GBR保证配置 |
| `CS-BW-04` | `T-007`, `T-401`, `T-402`, `T-003`~`T-005` | `uses_task` | ADC配置 |
| `CS-BW-05` | `T-007`, `T-603`, `T-103`~`T-105` | `uses_task` | 小区负荷+BWM动态 |
| `CS-BW-06` | `T-007`, `T-501`~`T-504`, `T-003`~`T-005` | `uses_task` | 位置策略（UNC侧） |
| `CS-BW-07` | `T-007`, `T-601`, `T-602` | `uses_task` | 无线标记配置 |

---

## 3. Feature → ConfigTask（decomposes_to）

| Feature | ConfigTask | 关系 | 说明 |
| --- | --- | --- | --- |
| `GWFD-110101` SA-Basic | `T-008` | `decomposes_to` | 加载特征库 |
| `GWFD-110101` | `T-001` | `decomposes_to` | 规划业务分类 |
| `GWFD-110101` | `T-024`(SET SRVCOMMONPARA 相关) | `decomposes_to` | SA公共参数 |
| `GWFD-111600` | `T-008` | `decomposes_to` | 特征库版本管理 |
| `GWFD-020351` PCC(UDG) | `T-002`, `T-003`, `T-004`, `T-005` | `decomposes_to` | PCC标准链 |
| `WSFD-109101` PCC(UNC) | `T-501`, `T-502`, `T-503`, `T-504` | `decomposes_to` | UNC PCC基础 |
| `GWFD-110311` BWM(UDG) | `T-101`~`T-106` | `decomposes_to` | BWM三级控制 |
| `WSFD-211005` BWM(UNC) | `T-003`, `T-004`, `T-005` | `decomposes_to` | UNC BWM规则(POLICYTYPE=BWM) |
| `GWFD-020354` Shaping | `T-103`(CTRLTYPE=SHAPING) | `decomposes_to` | Shaping控制器 |
| `GWFD-110313` 智能Shaping | `T-103`, `T-107` | `decomposes_to` | 智能Shaping+ServiceLevel |
| `GWFD-020353` 会话FUP(UDG) | `T-201`, `T-202`, `T-203`, `T-204` | `decomposes_to` | 会话FUP配置链 |
| `WSFD-109104` 会话FUP(UNC) | `T-205`, `T-204` | `decomposes_to` | UNC FUP(Gx额外配置) |
| `GWFD-110312` 业务FUP(UDG) | `T-201`, `T-202`, `T-203`, `T-204` | `decomposes_to` | 业务FUP(复用URR链) |
| `WSFD-211009` 业务FUP(UNC) | `T-204` | `decomposes_to` | UNC业务FUP |
| `GWFD-020358` QoS保证(UDG) | `T-301`(QOSTYPE), `T-202`(URR QOS模式) | `decomposes_to` | GBR保证 |
| `WSFD-109107` QoS保证(UNC) | `T-301`, `T-302`, `T-303` | `decomposes_to` | UNC专载管理 |
| `GWFD-110302` 视频解耦 | `T-301`(DECOUPLINGSW) | `decomposes_to` | 复用QoS保证+解耦参数 |
| `GWFD-020357` ADC(UDG) | `T-401` | `decomposes_to` | ADC参数 |
| `WSFD-109102` ADC(UNC) | `T-402`, `T-003`~`T-005` | `decomposes_to` | ADC三策略组 |
| `GWFD-020359` IM管控 | `T-601` | `decomposes_to` | DSCP标记 |
| `GWFD-110301` 码率差异化 | `T-602` | `decomposes_to` | 终端OS开关 |
| `GWFD-110331` FPI标记 | `T-601` | `decomposes_to` | FPI标记 |
| `GWFD-110332` 小区负荷(UDG) | `T-603` | `decomposes_to` | 负荷上报 |
| `WSFD-211101` 小区负荷(UNC) | `T-603` | `decomposes_to` | UNC负荷转发 |
| `WSFD-109108` 接入点策略 | `T-501`~`T-504`, `T-003`~`T-005` | `decomposes_to` | 位置策略 |
| `GWFD-020305` 异常检测 | （复用T-001, T-002） | `decomposes_to` | 异常检测配置 |

---

## 4. ConfigTask → MMLCommand（invokes）

| ConfigTask | MMLCommand | 关系 | 说明 |
| --- | --- | --- | --- |
| `T-007` License开启 | `CMD-UDG-001`, `CMD-UNC-001` | `invokes` | SET LICENSESWITCH |
| `T-008` SA特征库加载 | `CMD-UDG-026`, `CMD-UDG-027` | `invokes` | LOD SIGNATUREDB/PARSERDB |
| `T-001` 规划业务分类 | `CMD-UDG-009`, `CMD-UDG-014`, `CMD-UDG-015` | `invokes` | CATEGORYPROP/FILTER/L7FILTER |
| `T-002` 流过滤器绑定 | `CMD-UDG-013`, `CMD-UDG-016` | `invokes` | FLOWFILTER/FLTBINDFLOWF |
| `T-003` PCC规则 | `CMD-UDG-012`, `CMD-UNC-011` | `invokes` | ADD RULE |
| `T-004` 用户模板绑定 | `CMD-UDG-017`, `CMD-UDG-018`, `CMD-UNC-012`, `CMD-UNC-013` | `invokes` | USERPROFILE/RULEBINDING |
| `T-005` 用户模板组+APN绑定 | `CMD-UDG-030`, `CMD-UNC-014`~`CMD-UNC-016` | `invokes` | USRPROFGROUP/UPBINDUPG/APNUSRPROFG |
| `T-006` 策略刷新 | `CMD-UDG-025` | `invokes` | SET REFRESHSRV |
| `T-101` 规划BWM策略 | （规划task，无命令） | - | - |
| `T-102` BWM服务 | `CMD-UDG-003` | `invokes` | ADD BWMSERVICE |
| `T-103` BWM控制器 | `CMD-UDG-004` | `invokes` | ADD BWMCONTROLLER |
| `T-104` BWM用户组 | `CMD-UDG-005` | `invokes` | ADD BWMUSERGROUP |
| `T-105` BWM规则 | `CMD-UDG-006`, `CMD-UDG-007` | `invokes` | ADD BWMRULE/BWMRULEGLOBAL |
| `T-106` BWM APN绑定 | `CMD-UDG-010` | `invokes` | ADD APNBINDBWMUSRG |
| `T-107` 业务服务等级策略 | `CMD-UDG-008` | `invokes` | ADD BCSRVLEVELPLY |
| `T-201` 规划FUP策略 | （规划task） | - | - |
| `T-202` URR | `CMD-UDG-021`, `CMD-UNC-018` | `invokes` | ADD URR |
| `T-203` URR组 | `CMD-UDG-022`, `CMD-UNC-019` | `invokes` | ADD URRGROUP |
| `T-204` FUP策略组 | `CMD-UDG-019`, `CMD-UNC-017` | `invokes` | ADD PCCPOLICYGRP |
| `T-205` Gx FUP功能(UNC) | `CMD-UNC-002` | `invokes` | SET PCCFUNC + MOD PCRF/PCCPOLICYGRP |
| `T-301` QoS属性 | `CMD-UDG-020`, `CMD-UNC-020` | `invokes` | ADD QOSPROP |
| `T-302` 专有QoS Flow空闲定时器 | `CMD-UNC-023` | `invokes` | SET APNIDLETIME |
| `T-303` 去活QoS Flow策略 | `CMD-UNC-024` | `invokes` | ADD APNDEACTQFPLCY |
| `T-401` ADC参数 | `CMD-UDG-023`, `CMD-UNC-022` | `invokes` | ADD ADCPARA |
| `T-402` ADC三策略组 | `CMD-UNC-011` | `invokes` | ADD RULE(ADC) |
| `T-501` PCRF组与绑定 | `CMD-UNC-004`~`CMD-UNC-007` | `invokes` | ADD PCRF/PCRFGROUP/PCRFBINDGRP |
| `T-502` PCC功能开关 | `CMD-UNC-002`, `CMD-UNC-003` | `invokes` | SET PCCFUNC/APNPCCFUNC |
| `T-503` PCC故障与定时器 | `CMD-UNC-008`, `CMD-UNC-009` | `invokes` | SET PCCFAILACTION/PCCTIMER |
| `T-504` N7属性控制 | （CMD-UNC N7系列） | `invokes` | SET N7RCVATTRCTRL/N7SNDATTRCTRL |
| `T-601` DSCP/FPI标记 | （依特性定） | `invokes` | 特性专属标记命令 |
| `T-602` 终端OS差异化 | `CMD-UDG-028` | `invokes` | SET APNOSLELBWMSW |
| `T-603` 小区负荷上报 | `CMD-UNC-025` | `invokes` | SET APNREPORTATTR |

---

## 5. ConfigTask → SemanticObject/ConfigObject（targets）

| ConfigTask | targets | 目标对象 | 说明 |
| --- | --- | --- | --- |
| `T-001` | `SO-BW-02` 业务识别条件 | `OBJ-CATEGORYPROP`, `OBJ-FILTER`, `OBJ-L7FILTER` | 建立识别条件 |
| `T-002` | `SO-BW-02` | `OBJ-FLOWFILTER`, `OBJ-FILTER`, `OBJ-L7FILTER` | 流匹配条件 |
| `T-003` | `SO-BW-04` 限速等级 | `OBJ-RULE` | 规则定义 |
| `T-004`, `T-005` | - | `OBJ-USERPROFILE`, `OBJ-USRPROFGROUP` | 绑定链 |
| `T-103` | `SO-BW-01` 带宽控制策略 | `OBJ-BWMCONTROLLER` | 限速/整形参数 |
| `T-105` | `SO-BW-04` | `OBJ-BWMRULE` | BWM规则 |
| `T-202` | `SO-BW-03` 流量配额 | `OBJ-URR` | URR配额 |
| `T-301` | `SO-BW-05` QoS参数集 | `OBJ-QOSPROP` | QoS属性 |
| `T-401` | `SO-BW-06` 应用检测事件 | `OBJ-ADCPARA` | ADC参数 |
| `T-603` | `SO-BW-07` 小区负荷等级 | `OBJ-APNREPORTATTR`(SET) | 负荷上报 |

---

## 6. DecisionPoint 影响关系（selects / sets_value_pattern）

| DP | 关系 | 作用对象 | 说明 |
| --- | --- | --- | --- |
| `DP-BW-01` 带宽控制机制选择 | `selects` | `CS-BW-01`~`CS-BW-05`, 对应Feature | 选择控制机制决定方案和特性 |
| `DP-BW-02` 控制粒度选择 | `sets_value_pattern` | `PARA-BWMR-TYPE`(BWMRULETYPE) | 决定 SUBSCRIBER_SPECIFIC/GROUP_SPECIFIC/GLOBAL |
| `DP-BW-03` 规则类型选择 | `selects` | `T-003`(RULE配置路径), 预定义/动态/本地 | 决定配置路径与三网元一致性要求 |
| `DP-BW-04` 接口代际选择 | `sets_value_pattern` | `PARA-QP-TYPE`(QOSTYPE), `T-205`是否需要 | Gx→QOS_BEARER_PARA+额外配置；N7→QOS_FLOW_PARA |
| `DP-BW-05` BWM控制类型选择 | `sets_value_pattern` | `PARA-BWMC-CTRLTYPE`, CIR/PIR vs RATE/QUEDEPTH | 决定BWMCONTROLLER参数模式 |
| `DP-BW-06` FUP累计粒度选择 | `sets_value_pattern` | `PARA-URR-MODE`, Monitoring-Level | 会话级SESSION_LEVEL vs 业务级PCC_RULE_LEVEL |
| `DP-BW-07` 应用识别需求 | `selects` | `T-003`规则类型分支 | 需L7→预定义规则；仅L3L4→可用动态 |
| `DP-BW-08` 产品面配置分工 | `selects` | UDG task(T-101~106) / UNC task(T-501~504) / 双产品 | 决定配置入口 |
| `DP-BW-*` | `conditioned_by_scope` | 各CS的scope子对象 | 决策受方案范围约束 |

---

## 7. 端到端链路验证（3条完整路径）

### 路径A: SA-BWM带宽控制（CS-BW-01）

```text
BD-BW-01(业务感知)
  → NS-BW-01(带宽控制场景)
  → CS-BW-01(SA-BWM带宽控制方案)
  → Feature: GWFD-110311(基于业务感知的带宽控制)
  → ConfigTask: T-103(配置BWM控制器)
  → MMLCommand: CMD-UDG-004(ADD BWMCONTROLLER)
  → ConfigObject: OBJ-BWMCONTROLLER
  → SemanticObject: SO-BW-01(带宽控制策略)

证据链: EV-FK-110311 → feature-knowledge/GWFD-110311-基于业务感知的带宽控制.md
```

### 路径B: FUP配额降速（CS-BW-02）

```text
BD-BW-01(业务感知)
  → NS-BW-01(带宽控制场景)
  → CS-BW-02(FUP配额降速方案)
  → Feature: GWFD-020353(基于累计流量的策略控制)
  → ConfigTask: T-202(配置URR)
  → MMLCommand: CMD-UDG-021(ADD URR)
  → ConfigObject: OBJ-URR
  → SemanticObject: SO-BW-03(流量配额)

证据链: EV-FK-020353 → feature-knowledge/GWFD-020353-基于累计流量的策略控制.md
```

### 路径C: ADC应用感知动态带宽（CS-BW-04）

```text
BD-BW-01(业务感知)
  → NS-BW-01(带宽控制场景)
  → CS-BW-04(ADC应用感知动态带宽方案)
  → Feature: GWFD-020357(增强的ADC基本功能)
  → ConfigTask: T-401(配置ADC参数)
  → MMLCommand: CMD-UDG-023(ADD ADCPARA)
  → ConfigObject: OBJ-ADCPARA
  → SemanticObject: SO-BW-06(应用检测事件)

证据链: EV-FK-020357 → feature-knowledge/GWFD-020357-增强的ADC基本功能.md
```

---

## 8. 禁止关系检查（对照 Schema §13）

| 禁止关系 | 本图谱是否违反 | 说明 |
| --- | --- | --- |
| `ConfigurationSolution -> ConfigObject` | 否 | CS 通过 Feature/Task 间接达到对象 |
| `ConfigurationSolution -> MMLCommand` | 否 | CS 通过 ConfigTask 达到命令 |
| `BusinessRule -> CommandParameter` 直接写死 | 否 | BR 通过 DecisionPoint/TaskRule/CommandRule 影响 |
| `Feature -> MMLCommand` 直接强绑定 | 否 | Feature 通过 ConfigTask 达到命令 |
| `Feature -> ConfigObject` 携带参数差异 | 否 | 差异通过 SemanticObject/FeatureRule 表达 |
| 业务图谱内建 ConfigObject 实体 | 否 | 对象在命令图谱层定义 |
| `CS -> ConfigTask` 完整顺序链 | 否 | 仅保留 uses_task，顺序由 FeatureTaskOrderEdge 承接 |

**结论**: 本图谱未违反 Schema §13 列出的任何禁止关系。

---

## 9. Schema 合规检查清单

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| 对象类型匹配 Schema §8-§12 | 通过 | 全部对象类型为 Schema 定义类型 |
| 关系边匹配 Schema 定义 | 通过 | 所有关系边均在 Schema 关系表中 |
| 无禁止关系（§13） | 通过 | 见§8检查 |
| 端到端链路完整 | 通过 | 3条路径验证通过（§7） |
| 证据可追溯 | 通过 | 所有对象 source_evidence_ids 指向真实知识文档 |
| 跨层映射一致 | 通过 | 本文件对象引用与各层文件一致 |
| Feature 不跳过 task 直接绑命令 | 通过 | Feature→ConfigTask→MMLCommand 链完整 |
| CS 不直接拥有命令实例 | 通过 | CS→ConfigTask→MMLCommand 链完整 |
