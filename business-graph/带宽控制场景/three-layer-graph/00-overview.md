# 带宽控制场景三层图谱 · 总览（00-overview）

> **文件定位**：`three-layer-graph/00-overview.md`
> **作用**：五层架构导航、对象计数统计、端到端链路示例、文档索引
> **配套Schema**：`三层图谱Schema-最终版-v0.1.md`
> **配套本体**：`三层图谱本体标准定义.md`

---

## 1. 一句话定位

带宽控制场景（业务感知套餐2）三层图谱是**面向5G核心网带宽差异化控制**的领域知识图谱，以"业务→特性→任务→命令"四层对象 + 跨层映射 + 证据层为骨架，把分散在UDG（用户面）与UNC（控制面）共24个特性、317份源文档中的配置知识，组织成可追溯、可推理、可复用的结构化资产。

---

## 2. 五层架构总览

```
┌─────────────────────────────────────────────────────────────────────┐
│  第1层 业务图谱 BusinessGraph                                        │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ BD 业务域 → NS 网络场景 → CS 配置方案闭包                      │  │
│  │                            ↓                                  │  │
│  │            DP 决策点 ←→ BR 业务规则 ←→ SO 语义对象             │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ uses_feature / uses_task / realized_by                  │
├─────────────────────────────────────────────────────────────────────┤
│  第2层 特性图谱 FeatureGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Feature(24) ──depends_on──→ Feature                          │  │
│  │     │                                                         │  │
│  │     ├─ requires_license ──→ License(24)                       │  │
│  │     ├─ has_rule ──→ FeatureRule(5)                            │  │
│  │     └─ decomposes_to ──→ ConfigTask (跨层边)                  │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ decomposes_to / task_order                              │
├─────────────────────────────────────────────────────────────────────┤
│  第3层 任务原子层 TaskLayer                                          │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ ConfigTask(~30) ──command_order──→ ConfigTask (内部顺序)      │  │
│  │     │                                                         │  │
│  │     ├─ has_rule ──→ TaskRule(6)                               │  │
│  │     ├─ invokes ──→ MMLCommand (跨层边)                        │  │
│  │     └─ targets ──→ SemanticObject / ConfigObject (跨层边)     │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ invokes                                                 │
├─────────────────────────────────────────────────────────────────────┤
│  第4层 命令图谱 CommandGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ MMLCommand(55) ──has_param──→ CommandParameter               │  │
│  │     │                                                         │  │
│  │     ├─ operates_on ──→ ConfigObject(~26)                      │  │
│  │     │                      └─ contains ──→ ConfigObject       │  │
│  │     └─ has_rule ──→ CommandRule(5)                            │  │
│  └───────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────┤
│  第5层 跨层映射 CrossLayerMapping                                    │
│  CS ↔ Feature / Task / DP / BR / SO 的完整映射边                    │
├─────────────────────────────────────────────────────────────────────┤
│  第6层 证据层 EvidenceLayer                                          │
│  EvidenceSource(58) ←── source_evidence_ids ── 所有图谱对象        │
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
| | **业务层小计** | **31** | |
| **第2层 特性图谱** | Feature | 24 | `02-feature-graph.md` |
| | License | 24 | |
| | FeatureRule | 5 | |
| | **特性层小计** | **53** | |
| **第3层 任务原子层** | ConfigTask | ~30 | `03-task-layer.md` |
| | TaskRule | 6 | |
| | **任务层小计** | **~36** | |
| **第4层 命令图谱** | MMLCommand | 55 | `04-command-graph.md` |
| | ConfigObject | ~26 | |
| | CommandParameter | 关键参数集 | |
| | CommandRule | 5 | |
| | **命令层小计** | **~91** | |
| **第6层 证据层** | EvidenceSource | 58 | `06-evidence-index.md` |
| **图谱对象总计** | — | **~269** | — |

### 3.2 关键关系边总数

| 关系类型 | 数量 | 所在文件 |
|---------|------|---------|
| BD contains NS | 1 | `01-business-graph.md` |
| NS contains CS | 7 | `01-business-graph.md` |
| CS uses_feature | 22 | `05-cross-layer-mapping.md` |
| CS uses_task | 7（方案闭包级） | `05-cross-layer-mapping.md` |
| CS governed_by DP | 8 | `01-business-graph.md` |
| CS constrained_by BR | 6 | `01-business-graph.md` |
| CS realized_by SO | 8 | `01-business-graph.md` |
| Feature depends_on | 24 | `02-feature-graph.md` |
| Feature requires_license | 24 | `02-feature-graph.md` |
| Feature decomposes_to Task | 24 | `05-cross-layer-mapping.md` |
| ConfigTask invokes MMLCommand | ~30 | `05-cross-layer-mapping.md` |
| ConfigObject contains ConfigObject | 12 | `04-command-graph.md` |
| 图谱对象 source_evidence_ids | 全对象覆盖 | `06-evidence-index.md` |

---

## 4. 七大方案闭包（第1层核心）

| 方案ID | 方案名称 | 核心机制 | 主用特性 |
|--------|---------|---------|---------|
| CS-BW-01 | **SA-BWM带宽控制方案** | SA识别→BWM CAR/Shaping三级控制 | GWFD-110311, WSFD-211005 |
| CS-BW-02 | **FUP配额降速方案** | URR累计→配额耗尽→高优先级降速规则覆盖 | GWFD-020353, GWFD-110312 |
| CS-BW-03 | **GBR带宽保证方案** | SA识别→专有承载/QoS Flow→GBR资源预留 | GWFD-020358, WSFD-109107 |
| CS-BW-04 | **ADC应用感知动态带宽方案** | APP_STA/STO→三策略组动态切换QoS | GWFD-020357, WSFD-109102 |
| CS-BW-05 | **小区负荷动态带宽方案** | 负荷等级→PCRF策略→动态调整BWM | GWFD-110332, WSFD-211101 |
| CS-BW-06 | **位置区域差异化带宽方案** | 位置变化→预定义规则激活 | WSFD-109108 |
| CS-BW-07 | **无线资源优化标记方案** | DSCP/FPI标记→影响无线调度 | GWFD-020359, GWFD-110331 |

---

## 5. 端到端链路示例（三层贯通）

### 5.1 链路A：SA-BWM带宽控制（CS-BW-01）

```
[业务] BD-BW-01 业务感知
  → NS-BW-01 带宽控制场景
    → CS-BW-01 SA-BWM带宽控制方案
      → DP-BW-05 选择BWM控制类型（CAR / Shaping）
      → BR-BW-03 BWM与PCC独立匹配（可叠加）
      → SO-BW-01 带宽控制策略（CIR/PIR/RATE）

[特性] CS-BW-01 uses_feature
  → GWFD-110311 基于业务感知的带宽控制（UDG侧）
  → WSFD-211005 基于业务感知的带宽控制（UNC侧）
  → GWFD-110101 SA-Basic（业务识别基础）
  → GWFD-020351 PCC基本功能（UDG PCC框架）

[任务] GWFD-110311 decomposes_to
  → T-007 License开启
  → T-008 SA特征库加载
  → T-101 规划BWM控制策略
  → T-102 配置BWM服务      (ADD BWMSERVICE)
  → T-103 配置BWM控制器    (ADD BWMCONTROLLER) ★ 核心
  → T-104 配置BWM用户组    (ADD BWMUSERGROUP)
  → T-105 配置BWM规则      (ADD BWMRULE)
  → T-106 配置APN绑定      (ADD APNBINDBWMUSRG)
  → T-006 策略刷新生效      (SET REFRESHSRV, must_be_last)

[命令] T-103 invokes → ADD BWMCONTROLLER
  → operates_on → ConfigObject: BWMCONTROLLER
    → 关键参数: CTRLTYPE (CAR/SHAPING)
              , CIR/PIR/CBS/PBS (CAR模式)
              , RATE/QUEDEPTH (Shaping模式)
  → constrained_by → CR-05 CTRLTYPE决定参数集

[证据] 全链路可追溯：
  CS-BW-01 → [EV-CA-02, EV-TK-19, EV-FK-04]
  GWFD-110311 → [EV-FK-04]
  ADD BWMCONTROLLER → [EV-FK-04, EV-CA-01, EV-TK-19]
```

### 5.2 链路B：FUP配额降速（CS-BW-02）

```
[业务] CS-BW-02 FUP配额降速方案
  → DP-BW-06 选择FUP累计粒度（会话级 / 业务级）
  → BR-BW-02 超额降速优先级覆盖（最高优先级 + FlowFilter完全覆盖）
  → SO-BW-03 流量配额（VolumeThreshold）

[特性] CS-BW-02 uses_feature
  → GWFD-020353 会话级FUP（UDG）
  → GWFD-110312 业务级FUP（UDG，依赖SA）
  → WSFD-109104 会话级FUP（UNC）
  → WSFD-211009 业务级FUP（UNC）

[任务] GWFD-020353 decomposes_to
  → T-201 规划FUP配额策略
  → T-202 配置URR         (ADD URR) ★ 核心
  → T-203 配置URR组       (ADD URRGROUP)
  → T-204 配置FUP PCC策略组 (ADD PCCPOLICYGRP)
  → T-005 配置APN绑定
  → T-006 策略刷新生效

[命令] T-202 invokes → ADD URR
  → operates_on → ConfigObject: URR
    → 关键参数: USAGERPTMODE (QOS/ONLINE/OFFLINE)
              , VOLUMETHRESHOLD (配额阈值)
              , MONITORING-LEVEL (会话/业务)
  → constrained_by → CR-02 URR ID会话内唯一

[证据] 全链路：
  CS-BW-02 → [EV-CA-02, EV-TK-01, EV-TK-19, EV-FK-07, EV-FK-08]
```

### 5.3 链路C：ADC应用感知动态带宽（CS-BW-04）

```
[业务] CS-BW-04 ADC应用感知动态带宽方案
  → DP-BW-07 应用识别需求（L7识别→预定义规则）
  → SO-BW-06 应用检测事件（APP_STA/APP_STO）

[特性] CS-BW-04 uses_feature
  → GWFD-020357 增强的ADC基本功能（UDG）
  → WSFD-109102 ADC基本功能（UNC）

[任务] GWFD-020357 decomposes_to
  → T-401 配置ADC参数      (ADD ADCPARA) ★ 核心
  → T-402 配置ADC三策略组   (ADD RULE Normal/Start/Stop)
  → T-005 配置APN绑定
  → T-006 策略刷新生效

[命令] T-401 invokes → ADD ADCPARA
  → operates_on → ConfigObject: ADCPARA
    → 关键参数: APPID, ACTION (REPORT/...)
  → 三策略组: Normal规则 + Start规则(APP_STA触发) + Stop规则(APP_STO触发)

[证据] 全链路：
  CS-BW-04 → [EV-CA-02, EV-TK-27, EV-TK-28, EV-FK-09, EV-FK-21]
```

---

## 6. 关键决策点（第1层）

| 决策点 | 决策问题 | 影响 |
|--------|---------|------|
| DP-BW-01 | 带宽控制机制选择（CAR/Shaping/GBR/FUP/门控） | 决定使用哪些CS和Feature |
| DP-BW-02 | 控制粒度选择（会话/业务/用户组/全局） | 决定BWMRULETYPE和URR绑定方式 |
| DP-BW-03 | 规则类型选择（动态/预定义/本地） | 决定配置路径和三网元一致性要求 |
| DP-BW-04 | 接口代际选择（Gx 4G / N7 5G） | 决定参数体系和信令映射 |
| DP-BW-05 | BWM控制类型选择（CAR-CIR/PIR / Shaping） | 决定BWMCONTROLLER参数模式 |
| DP-BW-06 | FUP累计粒度选择（会话/业务） | 决定URR的Monitoring-Level和SA依赖 |
| DP-BW-07 | 应用识别需求（L7→预定义 / L3L4→动态） | 决定规则类型和SA依赖 |
| DP-BW-08 | 产品面配置分工（UDG执行面 / UNC控制面） | 决定配置入口和N4下发链路 |

---

## 7. 与计费场景图谱的差异

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| 共享根对象 | BD-BW-01=BD-CH-01=业务感知 | 同左 |
| ConfigurationSolution数量 | ~5个 | 7个 |
| 独有特性族 | 计费（CG/CHF对接） | BWM三级控制体系 |
| 独有ConfigObject | CG, CHF相关 | BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE, CATEGORYPROP |
| 共享ConfigObject | RULE, USERPROFILE, PCCPOLICYGRP, FLOWFILTER, URR | 同左 |
| 核心决策点差异 | 计费触发、批价规则 | 带宽机制、控制粒度、规则类型 |
| 共享ConfigTask | T-002流过滤, T-003 PCC规则, T-004用户模板, T-005 APN绑定 | 同左（复用4个通用Task） |

> 两场景图谱独立构建，不互相依赖；共享部分限于通用Task和通用ConfigObject。

---

## 8. 文档索引

| 文件 | 内容 | 对应Schema章节 |
|------|------|---------------|
| `00-overview.md` | 本文件：五层导航 + 对象计数 + 链路示例 | — |
| `01-business-graph.md` | 第1层：BD/NS/CS/DP/BR/SO 实例化 | §8.1-8.6, §8.12 |
| `02-feature-graph.md` | 第2层：24 Feature + License + FeatureRule | §9.3-9.5 |
| `03-task-layer.md` | 第3层：~30 ConfigTask + TaskRule + OrderEdge | §10.1-10.3 |
| `04-command-graph.md` | 第4层：55 MMLCommand + ConfigObject + CommandRule | §11.1-11.7 |
| `05-cross-layer-mapping.md` | 第5层：跨层映射关系总表 | §12.1-12.5 |
| `06-evidence-index.md` | 第6层：证据层索引（58 EvidenceSource） | §10 EvidenceSource |

---

## 9. 合规检查清单

### 9.1 Schema合规

- [x] 所有对象类型严格匹配 Schema §8-§12 定义
- [x] 所有关系边严格匹配 Schema §8.12/§9.5/§10.3/§11.7/§12 定义
- [x] 无 Schema §13 列出的禁止关系（CS→ConfigObject 直接绑定、Feature→MMLCommand 直接绑定等）
- [x] 所有对象包含 `source_evidence_ids` 字段

### 9.2 端到端链路完整性

- [x] 路径A (SA-BWM): BD→NS→CS-BW-01→GWFD-110311→T-103→ADD BWMCONTROLLER→BWMCONTROLLER ✓
- [x] 路径B (FUP): BD→NS→CS-BW-02→GWFD-020353→T-202→ADD URR→URR ✓
- [x] 路径C (ADC): BD→NS→CS-BW-04→GWFD-020357→T-401→ADD ADCPARA→ADCPARA ✓

### 9.3 证据可追溯

- [x] 每个图谱对象的 `source_evidence_ids` 指向真实存在的知识文档
- [x] 证据索引覆盖 24 EV-FK + 32 EV-TK + 2 EV-CA = 58份
- [x] 跨层映射中的边与各层文件中的对象引用一致

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
| **知识问答** | 给定问题 → 通过图谱对象关系导航 → 返回结构化答案 |

---

## 11. 后续演进

| 演进方向 | 说明 |
|---------|------|
| 与计费场景图谱融合 | 共享BD根对象，通过BD-level的contains NS边连接两个场景 |
| 访问限制场景接入 | 套餐3图谱独立构建后，三场景共享业务感知根，形成业务感知全景 |
| 图数据库落地 | Schema定义的对象/边可直接映射为 Neo4j/JanusGraph 的Node/Edge |
| 算子层接入 | 在图谱之上构建服务层算子，按§10使用场景封装查询API |

---

> 本总览文件是带宽控制场景三层图谱的入口文档。阅读顺序建议：**先读本文件理解全局 → 按需深入各层文件 → 通过06-evidence-index回溯证据**。
