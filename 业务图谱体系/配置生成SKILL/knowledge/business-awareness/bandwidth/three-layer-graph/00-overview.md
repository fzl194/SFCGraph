# 带宽控制场景三层图谱 · 总览（00-overview）

> **文件定位**：`three-layer-graph/00-overview.md`
> **作用**：五层架构导航、对象计数统计、端到端链路示例、文档索引
> **配套Schema**：`三层图谱Schema-最终版-v0.1.md`
> **配套本体**：`三层图谱本体标准定义.md`

---

## 1. 一句话定位

带宽控制场景（业务感知套餐2）三层图谱是**面向5G核心网带宽差异化控制**的领域知识图谱，以"业务→特性→任务→命令"四层对象 + 跨层映射 + 证据层为骨架，把分散在UDG（用户面，16特性）与UNC（控制面，8特性）共24个特性、317份源文档中的配置知识，组织成可追溯、可推理、可复用的结构化资产。

---

## 2. 五层架构总览

```
┌─────────────────────────────────────────────────────────────────────┐
│  第1层 业务图谱 BusinessGraph                                        │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ BD(1) → NS(1) → CS(7) 配置方案闭包                            │  │
│  │                     ↓                                        │  │
│  │     DP(8) ←→ BR(6) ←→ SO(8) 语义对象                        │  │
│  │     Scope(5) + Participant(5)                                │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ uses_feature(25) / uses_task(7)                         │
├─────────────────────────────────────────────────────────────────────┤
│  第2层 特性图谱 FeatureGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Feature(24: UDG16+UNC8) ──depends_on(26)──→ Feature          │  │
│  │     │                                                         │  │
│  │     ├─ requires_license(24) ──→ License(24)                   │  │
│  │     ├─ constrained_by(5) ──→ FeatureRule(5)                   │  │
│  │     └─ decomposes_to(24) ──→ ConfigTask (跨层边)              │  │
│  │     └─ task_order(25) ──→ FeatureTaskOrderEdge                │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ decomposes_to / task_order                              │
├─────────────────────────────────────────────────────────────────────┤
│  第3层 任务原子层 TaskLayer                                          │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ ConfigTask(32: generic8+specific24)                           │  │
│  │     │                                                         │  │
│  │     ├─ constrained_by(6) ──→ TaskRule(6)                      │  │
│  │     ├─ invokes(~50) ──→ MMLCommand (跨层边)                   │  │
│  │     └─ targets(~30) ──→ SO / ConfigObject (跨层边)            │  │
│  │     └─ command_order(16) ──→ TaskCommandOrderEdge             │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ invokes                                                 │
├─────────────────────────────────────────────────────────────────────┤
│  第4层 命令图谱 CommandGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ MMLCommand(55: UDG30+UNC25)                                   │  │
│  │     │                                                         │  │
│  │     ├─ operates_on(50) ──→ ConfigObject(29)                   │  │
│  │     │                      └─ contains(17) ──→ ConfigObject    │  │
│  │     └─ governed_by ←── CommandRule(5)                         │  │
│  └───────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────┤
│  第5层 跨层映射 CrossLayerMapping                                    │
│  CS↔Feature(25) + CS↔Task(7) + Feature↔Task(24) + Task↔Cmd(~50)    │
│  + Task↔SO/Obj(~30) + DP↔CS(4) + DP↔Param(3) + refined_by(6)      │
│  跨层边总计：~149                                                    │
├─────────────────────────────────────────────────────────────────────┤
│  第6层 证据层 EvidenceLayer                                          │
│  EvidenceSource(59) ←── source_evidence_ids ── 所有图谱对象         │
│  含24 EV-FK + 32 EV-TK + 2 EV-CA + 1 EV-BS = 59份                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. 对象计数统计

### 3.1 各层对象总数

| 层级 | 对象类型 | 数量 | 文件 |
|------|---------|------|------|
| **第1层 业务图谱** | BusinessDomain (BD) | 1 | `01-business-graph.md` |
| | NetworkScenario (NS) | 1 | |
| | ConfigurationSolution (CS) | 7 | |
| | DecisionPoint (DP) | 8 | |
| | BusinessRule (BR) | 6 | |
| | SemanticObject (SO) | 8 | |
| | Scope（子对象） | 5 | |
| | Participant（子对象） | 5 | |
| | **业务层小计** | **41** | |
| **第2层 特性图谱** | Feature | 24（UDG 16 + UNC 8） | `02-feature-graph.md` |
| | License | 24（UDG 16 + UNC 8） | |
| | FeatureRule | 5 | |
| | depends_on 边 | 26（UDG 20 + UNC 6） | |
| | FeatureTaskOrderEdge | 25 | |
| | **特性层小计** | **104** | |
| **第3层 任务原子层** | ConfigTask（generic） | 8（T-001~T-008） | `03-task-layer.md` |
| | ConfigTask（feature_specific） | 24（T-101~T-603） | |
| | TaskRule | 6 | |
| | TaskCommandOrderEdge | 16 | |
| | **任务层小计** | **54** | |
| **第4层 命令图谱** | MMLCommand | 55（UDG 30 + UNC 25） | `04-command-graph.md` |
| | ConfigObject | 29 | |
| | CommandRule | 5 | |
| | ConfigObject contains/refers_to 边 | 17 | |
| | operates_on 边 | 50（UDG 28 + UNC 22） | |
| | **命令层小计** | **~156** | |
| **第5层 跨层映射** | 跨层边 | ~149 | `05-cross-layer-mapping.md` |
| **第6层 证据层** | EvidenceSource | 59（24 EV-FK + 32 EV-TK + 2 EV-CA + 1 EV-BS） | `06-evidence-index.md` |
| **图谱对象总计** | — | **~563** | — |

### 3.2 关键关系边总数

| 关系类型 | 数量 | 所在文件 |
|---------|------|---------|
| BD contains NS | 1 | `01-business-graph.md` |
| NS instantiated_as CS | 7 | `01-business-graph.md` |
| CS uses_feature | 25 | `05-cross-layer-mapping.md` |
| CS uses_task（闭包级） | 7 | `05-cross-layer-mapping.md` |
| CS has_decision（DP归属） | ~10 | `01-business-graph.md` |
| CS constrained_by BR | ~20 | `01-business-graph.md` |
| CS uses_semantic_object | 7 | `01-business-graph.md` |
| DP selects CS | 4 | `05-cross-layer-mapping.md` |
| DP sets_value_pattern | 3 | `05-cross-layer-mapping.md` |
| Feature depends_on | 26 | `02-feature-graph.md` |
| Feature requires_license | 24 | `02-feature-graph.md` |
| Feature constrained_by（FeatureRule） | 5 | `02-feature-graph.md` |
| Feature decomposes_to Task | 24 | `05-cross-layer-mapping.md` |
| Feature task_order（FTOE） | 25 | `02-feature-graph.md` |
| ConfigTask constrained_by（TaskRule） | 6 | `03-task-layer.md` |
| ConfigTask invokes MMLCommand | ~50 | `05-cross-layer-mapping.md` |
| ConfigTask targets SO/ConfigObject | ~30 | `05-cross-layer-mapping.md` |
| ConfigObject contains/refers_to ConfigObject | 17 | `04-command-graph.md` |
| MMLCommand operates_on ConfigObject | 50 | `04-command-graph.md` |
| MMLCommand governed_by CommandRule | 5 | `04-command-graph.md` |
| BR/TR/CR refined_by | 6 | `05-cross-layer-mapping.md` |
| 图谱对象 source_evidence_ids | 全对象覆盖 | `06-evidence-index.md` |

---

## 4. 七大方案闭包（第1层核心）

| 方案ID | 方案名称 | 核心机制 | 主用特性 |
|--------|---------|---------|---------|
| CS-BW-01 | **SA-BWM带宽控制方案** | SA识别→BWM CAR/Shaping三级控制（用户级/组级/全局级） | GWFD-110311, WSFD-211005, GWFD-110101 |
| CS-BW-02 | **FUP配额降速方案** | URR累计→配额耗尽→高优先级降速规则覆盖 | GWFD-020353, WSFD-109104, GWFD-110312 |
| CS-BW-03 | **GBR带宽保证方案** | SA识别→专有承载/QoS Flow→GBR资源预留 | GWFD-020358, WSFD-109107 |
| CS-BW-04 | **ADC应用感知动态带宽方案** | APP_STA/STO→三策略组（Normal/Start/Stop）动态切换QoS | GWFD-020357, WSFD-109102 |
| CS-BW-05 | **小区负荷动态带宽方案** | RAN负荷等级→PCRF策略→动态调整BWM | GWFD-110332, WSFD-211101 |
| CS-BW-06 | **位置区域差异化带宽方案** | 位置变化感知→预定义差异化带宽规则激活 | WSFD-109108 |
| CS-BW-07 | **无线资源优化标记方案** | DSCP/FPI标记/终端OS差异化→影响无线调度 | GWFD-020359, GWFD-110331, GWFD-110301 |

---

## 5. 端到端链路示例（三层贯通）

### 5.1 链路A：SA-BWM带宽控制（CS-BW-01）

```
[业务] BD-BW-01 业务感知
  → NS-BW-01 带宽控制场景
    → CS-BW-01 SA-BWM带宽控制方案
      → DP-BW-01 选择CAR限速
      → DP-BW-02 选择用户级控制（SUBSCRIBER_SPECIFIC）
      → DP-BW-05 选择CAR-CIR保障（CIR/PIR/CBS/PBS）
      → BR-BW-01 预定义规则三网元一致性
      → BR-BW-03 BWM与PCC独立匹配
      → BR-BW-05 REFRESHSRV必须最后执行
      → SO-BW-01 带宽控制策略（CIR/PIR参数集）
      → SO-BW-02 业务识别条件（SVC/APP）

[特性] CS-BW-01 uses_feature
  → GWFD-110311 基于业务感知的带宽控制（UDG三级控制体系）
  → GWFD-110101 SA-Basic（业务识别基础）
  → GWFD-020351 PCC基本功能（UDG PCC框架）
  → WSFD-211005 基于业务感知的带宽控制（UNC BWM规则）
  → WSFD-109101 PCC基本功能（UNC PCC框架）

[任务] GWFD-110311 decomposes_to（FTOE-BW-001~008）
  → T-007 License开启（LKV3G5TCSA01）
  → T-008 SA特征库加载
  → T-101 规划BWM控制策略
  → T-102 ADD BWMSERVICE
  → T-103 ADD BWMCONTROLLER（CTRLTYPE=CAR, CIR/PIR/CBS/PBS）★ 核心
  → T-104 ADD BWMUSERGROUP
  → T-105 ADD BWMRULE（BWMRULETYPE=SUBSCRIBER_SPECIFIC）
  → T-106 ADD APNBINDBWMUSRG
  → T-006 SET REFRESHSRV（must_be_last）

[命令] T-103 invokes → ADD BWMCONTROLLER
  → operates_on → ConfigObject: BWMCONTROLLER
    → 关键参数: BWMCNAME, CTRLTYPE=CAR, CIR, PIR, CBS, PBS, GREENACT, YELLOWACT, REDACT
  → constrained_by → CR-BW-02 CTRLTYPE决定参数集
  → constrained_by → CR-BW-03 CAR与Shaping不可同对象叠加
  → impacted_by → DP-BW-05 sets_value_pattern(CTRLTYPE=CAR)

[证据] 全链路可追溯：
  CS-BW-01 → [EV-FK-04, EV-FK-01, EV-FK-03, EV-CA-01]
  GWFD-110311 → [EV-FK-04, EV-CA-01]
  ADD BWMCONTROLLER → [EV-FK-04, EV-CA-01]
```

### 5.2 链路B：FUP配额降速（CS-BW-02）

```
[业务] CS-BW-02 FUP配额降速方案
  → DP-BW-06 选择会话级FUP（SESSION_LEVEL）
  → BR-BW-02 超额降速优先级覆盖 ★ 核心
  → BR-BW-01 预定义规则三网元一致性
  → SO-BW-03 流量配额（VolumeThreshold）
  → SO-BW-04 限速等级（高速→降速切换）

[特性] CS-BW-02 uses_feature
  → GWFD-020353 基于累计流量的策略控制（UDG会话级FUP）
  → WSFD-109104 基于累计流量的策略控制（UNC会话级FUP）
  → GWFD-110312 基于业务累计流量的策略控制（UDG业务级FUP，可选）
  → WSFD-211009 基于业务累计流量的策略控制（UNC业务级FUP，可选）

[任务] GWFD-020353 decomposes_to（FTOE-BW-009~013）
  → T-007 License开启（LKV3G5PCBT01）
  → T-201 规划FUP配额策略
  → T-202 ADD URR（USAGERPTMODE=ONLINE, VOLUMETHRESHOLD）★ 核心
  → T-203 ADD URRGROUP（UPURRNAME1引用URR）
  → T-204 ADD PCCPOLICYGRP（URRGROUP→策略组）★ FUP三件套完成
  → T-006 SET REFRESHSRV

[命令] T-202 invokes → ADD URR
  → operates_on → ConfigObject: URR
    → 关键参数: URRID, USAGERPTMODE=ONLINE, MEASUREMENTMETHOD=VOLUME, VOLUMETHRESHOLD
  → constrained_by → TR-BW-04 URR模式校验（会话FUP=ONLINE）
  → constrained_by → TR-BW-03 FUP三件套链（URR→URRGROUP→PCCPOLICYGRP）
  → impacted_by → DP-BW-06 sets_value_pattern(SESSION_LEVEL)

[证据] CS-BW-02 → [EV-FK-07, EV-FK-18, EV-CA-01, EV-CA-02]
  ADD URR → [EV-FK-07, EV-CA-01]
```

### 5.3 链路C：ADC应用感知动态带宽（CS-BW-04）

```
[业务] CS-BW-04 ADC应用感知动态带宽方案
  → DP-BW-07 需L7识别→预定义规则
  → BR-BW-01 预定义规则三网元一致性（ADCPARA+RULENAME+FLOWFILTERNAME全网一致）
  → BR-BW-04 RULENAME跨策略类型不冲突
  → SO-BW-06 应用检测事件（APP_STA/APP_STO）
  → SO-BW-05 QoS参数集（三策略组QoS差异）

[特性] CS-BW-04 uses_feature
  → GWFD-020357 增强的ADC基本功能（UDG侧L7 DPI检测）
  → WSFD-109102 ADC基本功能（UNC侧三策略组+承载管理）

[任务] GWFD-020357 decomposes_to
  → T-007 License开启（LKV3G5ADCF01）
  → T-008 SA特征库加载
  → T-401 ADD ADCPARA ★ ADC检测参数
  → T-006 SET REFRESHSRV

[任务] WSFD-109102 decomposes_to
  → T-501 配置PCRF组
  → T-401 ADD ADCPARA（UNC侧，三网元一致）
  → T-402 ADD RULE x3（Normal/Start/Stop三策略组）★ 核心ADC策略
  → T-003/T-004/T-005 规则+模板+绑定链

[命令] T-401 invokes → ADD ADCPARA
  → operates_on → ConfigObject: ADCPARA
    → 关键参数: ADCPARANAME, APPNAME, MATCHMODE
  → constrained_by → CR-BW-05 预定义规则名全网唯一（ADCPARA+RULENAME三网元一致）

[证据] CS-BW-04 → [EV-FK-09, EV-FK-21, EV-CA-02]
  ADD ADCPARA → [EV-FK-09, EV-CA-01]
```

---

## 6. 关键决策点（第1层）

| 决策点 | 决策问题 | 影响 |
|--------|---------|------|
| DP-BW-01 | 带宽控制机制选择（CAR限速/Shaping整形/GBR保证/FUP降速/门控阻断） | 决定使用哪些CS（CS-BW-01~05）和Feature；决定BWMCONTROLLER.CTRLTYPE或QOSPROP路径 |
| DP-BW-02 | 控制粒度选择（会话级/业务级/用户组级/全局级） | 决定BWMRULETYPE（SUBSCRIBER_SPECIFIC/GROUP_SPECIFIC/GLOBAL）和URR绑定方式 |
| DP-BW-03 | 规则类型选择（动态规则/预定义规则/本地规则） | 决定配置路径和三网元一致性要求；定向业务必须用预定义（PCF无L7能力） |
| DP-BW-04 | 接口代际选择（Gx 4G / N7 5G） | 决定参数体系（QCI/MBR vs 5QI/Session-AMBR）和信令映射；FUP Gx需额外配置UMCH |
| DP-BW-05 | BWM控制类型选择（CAR-CIR保障/CAR-PIR限速/SHAPING整形） | 决定BWMCONTROLLER参数模式（CIR/PIR/CBS/PBS vs RATE/QUEDEPTH） |
| DP-BW-06 | FUP累计粒度选择（会话级FUP/业务级FUP） | 决定URR的Monitoring-Level（SESSION_LEVEL vs PCC_RULE_LEVEL）和SA依赖 |
| DP-BW-07 | 应用识别需求（需L7识别→预定义规则 / 仅L3L4→可用动态规则） | 决定规则类型和SA依赖；定向业务/ADC必须用预定义规则 |
| DP-BW-08 | 产品面配置分工（UDG执行面/UNC控制面/双产品协作） | 决定配置入口和N4下发链路 |

---

## 7. 与计费场景图谱的差异

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| **共享根对象** | BD-CH-01=BD-BW-01=业务感知 | 同左 |
| **ConfigurationSolution数量** | 7个（按计费方式/计量/兜底分） | 7个（按控制机制分） |
| **核心机制** | SA识别→Rule→PCC/URR计费链→Ga/Gy/N40上报→配额闭环 | SA识别→BWM限速→CAR/Shaping/FUP/GBR |
| **独有特性族** | 计费三件套(URR/URRGROUP/PCCPOLICYGRP)、融合计费(CCT/CHF选择) | BWM三级控制体系（用户级/组级/全局级） |
| **Feature数量** | 14（UDG 9 + UNC 5） | 24（UDG 16 + UNC 8） |
| **License数量** | 11（含4无需License） | 24（全部需License） |
| **独有ConfigObject** | URRGRPBINDING, DIAMCONNGRP, DCCTEMPLATE, CCT, CHARGECHAR, CHGMODE, CHFINIT, TNFGRP, SELECTCHFGBYCC, CG | BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE, BWMRULEGLOBAL, BCSRVLEVELPLY, CATEGORYPROP, APNBINDBWMUSRG, APNDEACTQFPLCY |
| **共享ConfigObject** | RULE, USERPROFILE, PCCPOLICYGRP, FLOWFILTER, **URR, URRGROUP** | 同左（含URR/URRGROUP共享，但参数语义不同） |
| **独有协议知识** | Ga/Gy/DCC/N40/PFCP/Gx（6协议，1422行，SO-CH-10/11） | 无独立协议层SemanticObject |
| **URR语义差异** | RG/USAGERPTMODE/METERINGTYPE差异化计费 | VOLUMETHRESHOLD触发降速（FUP），QOS模式触发专载事件上报 |
| **POLICYTYPE** | CHARGING（计费场景固定） | BWM/PCC/QOS/ADC（按策略类型分支） |
| **DecisionPoint** | 8个（计费方式/配额/计量/兜底/跨网元） | 8个（带宽机制/控制粒度/规则类型/接口代际） |
| **BusinessRule** | 16条 | 6条 |
| **SemanticObject** | 12个（含协议栈2个） | 8个（无协议栈） |
| **共享ConfigTask** | T-001分类, T-002流过滤, T-003 PCC规则, T-004用户模板, T-005 APN绑定, T-006刷新, T-007 License | 同左（复用7个通用Task，T-008不同：计费=协议绑定，带宽=SA特征库加载） |
| **MMLCommand** | 87（UDG 41 + UNC 46） | 55（UDG 30 + UNC 25） |
| **ConfigObject** | 55 | 29 |
| **CommandRule** | 14 | 5 |
| **证据层** | 32份（含2协议知识） | 59份（24特性+32主题+2跨层分析+1业务图谱） |
| **跨层边总计** | ~130 | ~149 |

> 两场景图谱独立构建，不互相依赖；共享部分限于 `业务感知` 根对象、7个通用ConfigTask（T-001~T-007）和通用ConfigObject（含URR/URRGROUP，但参数语义不同）。

---

## 8. 文档索引

| 文件 | 内容 | 关键统计 | 对应Schema章节 |
|------|------|---------|---------------|
| `00-overview.md` | 本文件：五层导航 + 对象计数 + 链路示例 + 差异对比 | — | — |
| `01-business-graph.md` | 第1层：BD/NS/CS/DP/BR/SO 实例化 | BD(1) + NS(1) + CS(7) + DP(8) + BR(6) + SO(8) + Scope(5) + Participant(5) = 41 | §8.1-8.12 |
| `02-feature-graph.md` | 第2层：24 Feature + 24 License + 5 FeatureRule + 26 depends_on + 25 FTOE | Feature(24) + License(24) + FeatureRule(5) + depends_on(26) + FTOE(25) = 104 | §9.3-9.5 |
| `03-task-layer.md` | 第3层：32 ConfigTask + 6 TaskRule + 16 TCOE | ConfigTask(32: generic8+specific24) + TaskRule(6) + TCOE(16) = 54 | §10.1-10.3 |
| `04-command-graph.md` | 第4层：55 MMLCommand + 29 ConfigObject + 5 CommandRule | MMLCommand(55) + ConfigObject(29) + CommandRule(5) + contains(17) + operates_on(50) = 156 | §11.1-11.7 |
| `05-cross-layer-mapping.md` | 第5层：跨层映射关系总表 + 端到端链路验证 | uses_feature(25) + uses_task(7) + decomposes_to(24) + invokes(~50) + targets(~30) + selects(4) + sets_value_pattern(3) + refined_by(6) = ~149 | §12.1-12.5 |
| `06-evidence-index.md` | 第6层：证据层索引 | EV-FK(24) + EV-TK(32) + EV-CA(2) + EV-BS(1) = 59 EvidenceSource | §10 EvidenceSource |

---

## 9. 合规检查清单

### 9.1 Schema合规

- [x] 所有对象类型严格匹配 Schema §8-§12 定义
- [x] 所有关系边严格匹配 Schema §8.12/§9.5/§10.3/§11.7/§12 定义
- [x] 无 Schema §13 列出的禁止关系（CS→ConfigObject 直接绑定、Feature→MMLCommand 直接绑定等）
- [x] 所有对象包含 `source_evidence_ids` 字段

### 9.2 端到端链路完整性

- [x] 路径A (SA-BWM): BD→NS→CS-BW-01→GWFD-110311→T-103→ADD BWMCONTROLLER→BWMCONTROLLER
- [x] 路径B (FUP): BD→NS→CS-BW-02→GWFD-020353→T-202→ADD URR→URR
- [x] 路径C (ADC): BD→NS→CS-BW-04→GWFD-020357→T-401→ADD ADCPARA→ADCPARA

### 9.3 证据可追溯

- [x] 每个图谱对象的 `source_evidence_ids` 指向真实存在的知识文档
- [x] 证据索引覆盖 24 EV-FK + 32 EV-TK + 2 EV-CA + 1 EV-BS = 59份
- [x] 核心方案 CS-BW-01~07 至少引用 1份 direct 证据 + 1份 supporting 证据
- [x] 所有 Feature 对象引用对应 EV-FK-*
- [x] 证据可追溯链路完整（图谱对象→本索引→知识文档→原始产品文档）

### 9.4 跨层一致性验证

- [x] 所有CS的uses_feature指向真实存在的Feature（24个）
- [x] 所有Feature的decomposes_to指向真实存在的ConfigTask（32个）
- [x] 所有ConfigTask的invokes指向真实存在的MMLCommand（55个）
- [x] 所有MMLCommand的operates_on指向真实存在的ConfigObject（29个）
- [x] 所有ConfigTask的targets指向真实存在的SemanticObject（8个）或ConfigObject
- [x] 所有DP的selects指向真实存在的CS（7个）
- [x] 无 §13 禁止关系

---

## 10. 图谱使用场景

本图谱可支撑以下下游应用：

| 应用场景 | 使用方式 |
|---------|---------|
| **配置生成** | 给定业务需求 → 定位CS → 遍历uses_task → 生成命令序列 |
| **影响分析** | 给定特性变更 → 反查uses_feature的CS → 评估影响范围 |
| **故障诊断** | 给定命令失败 → 查CommandRule → 回溯ConfigTask → 定位Feature/CS |
| **方案推荐** | 给定业务目标 → 遍历DP决策点 → 推荐CS组合 → 输出配置蓝图 |
| **License规划** | 给定目标特性集 → 聚合requires_license → 输出License清单 |
| **带宽架构理解** | 通过SO-BW-01~08语义对象 → 理解BWM/FUP/GBR/ADC/位置控制等机制 |
| **降速控制设计** | CS-BW-02 → 理解会话级/业务级FUP两种配额降速闭环 |
| **知识问答** | 给定问题 → 通过图谱对象关系导航 → 返回结构化答案 |

---

## 11. 后续演进

| 演进方向 | 说明 |
|---------|------|
| 与计费场景图谱融合 | 共享BD根对象，通过BD-level的contains NS边连接两个场景；通用Task需加场景前缀避免编号冲突 |
| 访问限制场景接入 | 套餐3图谱独立构建后，三场景共享业务感知根，形成业务感知全景 |
| 图数据库落地 | Schema定义的对象/边可直接映射为 Neo4j/JanusGraph 的Node/Edge |
| 算子层接入 | 在图谱之上构建服务层算子，按§10使用场景封装查询API |
| 配置生成自动化 | 基于CS闭包+Task链，自动生成端到端MML命令脚本 |

---

> 本总览文件是带宽控制场景三层图谱的入口文档。阅读顺序建议：**先读本文件理解全局 → 按需深入各层文件 → 通过06-evidence-index回溯证据**。
