# 计费场景三层图谱 · 总览（00-overview）

> **文件定位**：`three-layer-graph/00-overview.md`
> **作用**：五层架构导航、对象计数统计、端到端链路示例、文档索引
> **配套Schema**：`三层图谱Schema-最终版-v0.1.md`
> **配套本体**：`三层图谱本体标准定义.md`

---

## 1. 一句话定位

计费场景三层图谱是**面向5G核心网差异化计费**的领域知识图谱，以"业务→特性→任务→命令"四层对象 + 跨层映射 + 证据层为骨架，把分散在UDG（用户面）与UNC（控制面）共14个特性、31份源知识文档（含1,422行协议知识）中的配置知识，组织成可追溯、可推理、可复用的结构化资产。

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
│  │ Feature(14) ──depends_on──→ Feature                          │  │
│  │     │                                                         │  │
│  │     ├─ requires_license ──→ License(11)                       │  │
│  │     ├─ has_rule ──→ FeatureRule(8)                            │  │
│  │     └─ decomposes_to ──→ ConfigTask (跨层边)                  │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ decomposes_to / task_order                              │
├─────────────────────────────────────────────────────────────────────┤
│  第3层 任务原子层 TaskLayer                                          │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ ConfigTask(28) ──command_order──→ ConfigTask (内部顺序)      │  │
│  │     │                                                         │  │
│  │     ├─ has_rule ──→ TaskRule(6)                               │  │
│  │     ├─ invokes ──→ MMLCommand (跨层边)                        │  │
│  │     └─ targets ──→ SemanticObject / ConfigObject (跨层边)     │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ invokes                                                 │
├─────────────────────────────────────────────────────────────────────┤
│  第4层 命令图谱 CommandGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ MMLCommand(65) ──has_param──→ CommandParameter               │  │
│  │     │                                                         │  │
│  │     ├─ operates_on ──→ ConfigObject(26)                       │  │
│  │     │                      └─ contains ──→ ConfigObject       │  │
│  │     └─ has_rule ──→ CommandRule(12)                           │  │
│  └───────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────┤
│  第5层 跨层映射 CrossLayerMapping                                    │
│  CS ↔ Feature / Task / DP / BR / SO 的完整映射边                    │
├─────────────────────────────────────────────────────────────────────┤
│  第6层 证据层 EvidenceLayer                                          │
│  EvidenceSource(31) ←── source_evidence_ids ── 所有图谱对象        │
│  ★ 含 2份协议知识证据（Ga/Gy/DCC + N40/PFCP/Gx，1422行）             │
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
| | BusinessRule (BR) | 12 | |
| | SemanticObject (SO) | 12（含2协议栈） | |
| | Scope（子对象） | 5 | |
| | Participant（子对象） | 10 | |
| | **业务层小计** | **56** | |
| **第2层 特性图谱** | Feature | 14（UDG 9 + UNC 5） | `02-feature-graph.md` |
| | License | 11（含4无需License特性） | |
| | FeatureRule | 8 | |
| | **特性层小计** | **33** | |
| **第3层 任务原子层** | ConfigTask | 28（generic 8 + feature_specific 20） | `03-task-layer.md` |
| | TaskRule | 6 | |
| | TaskCommandOrderEdge | 20 | |
| | **任务层小计** | **54** | |
| **第4层 命令图谱** | MMLCommand | 65（UDG 32 + UNC 33） | `04-command-graph.md` |
| | ConfigObject | 26 | |
| | CommandRule | 12 | |
| | ConfigObject contains 边 | 9 | |
| | **命令层小计** | **112** | |
| **第5层 跨层映射** | 跨层边 | ~125 | `05-cross-layer-mapping.md` |
| **第6层 证据层** | EvidenceSource | 31（含2协议知识★） | `06-evidence-index.md` |
| **图谱对象总计** | — | **~411** | — |

### 3.2 关键关系边总数

| 关系类型 | 数量 | 所在文件 |
|---------|------|---------|
| BD contains NS | 1 | `01-business-graph.md` |
| NS contains CS | 7 | `01-business-graph.md` |
| CS uses_feature | 20 | `05-cross-layer-mapping.md` |
| CS uses_task（闭包级） | 7 | `05-cross-layer-mapping.md` |
| CS governed_by DP（has_decision） | 10 | `01-business-graph.md` |
| CS constrained_by BR | ~20 | `01-business-graph.md` |
| CS uses_semantic_object | 7 | `01-business-graph.md` |
| Feature depends_on | 16 | `02-feature-graph.md` |
| Feature requires_license | 11 | `02-feature-graph.md` |
| Feature has_rule（FeatureRule） | 8 | `02-feature-graph.md` |
| Feature decomposes_to Task | 14 | `05-cross-layer-mapping.md` |
| ConfigTask invokes MMLCommand | ~50 | `05-cross-layer-mapping.md` |
| ConfigObject contains ConfigObject | 9 | `04-command-graph.md` |
| DP selects / sets_value_pattern | 6 | `05-cross-layer-mapping.md` |
| 图谱对象 source_evidence_ids | 全对象覆盖 | `06-evidence-index.md` |

---

## 4. 七大方案闭包（第1层核心）

| 方案ID | 方案名称 | 核心机制 | 主用特性 |
|--------|---------|---------|---------|
| CS-CH-01 | **离线计费方案** | URR累计(OFFLINE)→Ga/GTP'→CG→BD结算 | GWFD-010171, GWFD-020301, WSFD-011201 |
| CS-CH-02 | **在线计费方案** | Gy/DCC→OCS配额分配→实时扣费→耗尽动作 | GWFD-020300, GWFD-020301 |
| CS-CH-03 | **融合计费方案** | N40/Nchf→CCT模板→在线RG+离线RG共存→CHF | GWFD-010173, WSFD-011206, GWFD-020301 |
| CS-CH-04 | **内容计费基础方案** | SA识别→FILTER匹配→三件套→RG差异化费率 | GWFD-110101, GWFD-020301, GWFD-020351, WSFD-109101 |
| CS-CH-05 | **计量形态增强方案** | URR.METERINGTYPE参数化（流量/时长/事件） | GWFD-020302, GWFD-020303, GWFD-020306 |
| CS-CH-06 | **配额降速与体验切换方案** | 配额耗尽→Final-Unit-Action→高优先级降速规则覆盖 | GWFD-020300, GWFD-010173, WSFD-011206 |
| CS-CH-07 | **兜底默认计费方案** | DFTURRGRPNAME+DFTSIGURRGNAME+SPECTRAFURRGRP三重兜底 | GWFD-020301, GWFD-020351 |

---

## 5. 端到端链路示例（三层贯通）

### 5.1 链路A：内容计费基础（CS-CH-04）

```
[业务] BD-CH-01 业务感知
  → NS-CH-01 计费场景
    → CS-CH-04 内容计费基础方案
      → DP-CH-03 选择匹配层次（L34+L7混合）
      → DP-CH-05 选择计费粒度（业务级）
      → BR-CH-02 配置链逐层一致性
      → SO-CH-08 计费语义（RG差异化）

[特性] CS-CH-04 uses_feature
  → GWFD-110101 SA-Basic（业务识别基础）
  → GWFD-020301 内容计费（UDG三件套）
  → GWFD-020351 PCC基本功能（UDG PCC框架）

[任务] GWFD-020301 decomposes_to
  → T-101 License开启（LKV3G5BCBC01）
  → T-102 SA特征库加载
  → T-001 规划业务分类（FILTER/L7FILTER）
  → T-006 配置URR与URR组 ★ 核心 (ADD URR)
  → T-007 配置PCC策略组 (ADD PCCPOLICYGRP)
  → T-003 配置PCC规则 (ADD RULE)
  → T-004 配置用户模板与规则绑定
  → T-104 配置URR组绑定与兜底 (DFTURRGRPNAME)
  → T-008 策略刷新生效 (must_be_last)

[命令] T-006 invokes → ADD URR
  → operates_on → ConfigObject: URR
    → 关键参数: URRID, USAGERPTMODE=OFFLINE, OFFMETERINGTYPE=VOLUME, RG
  → constrained_by → CR-01 URRID会话内唯一
                   → CR-02 RG值跨侧一致性
                   → CR-03 三件套绑定完整性

[证据] 全链路可追溯：
  CS-CH-04 → [EV-KB-001(K013,K020-K022), EV-BS-001, EV-KB-002(K214)]
  GWFD-020301 → [EV-FK-Content-UDG, EV-CFA]
  ADD URR → [EV-FK-Content-UDG, EV-CFA, EV-KB-001]
```

### 5.2 链路B：在线计费（CS-CH-02）

```
[业务] CS-CH-02 在线计费方案
  → DP-CH-04 选择配额耗尽动作（BLOCK/REDIRECT/FORWARD）
  → BR-CH-09 配额降速优先级覆盖
  → SO-CH-09 配额语义（GSU/Final-Unit-Action）
  → SO-CH-10 Ga/Gy协议栈 ★

[特性] CS-CH-02 uses_feature
  → GWFD-020300 在线计费（UDG Gy/OCS）
  → GWFD-020301 内容计费（基础）

[任务] GWFD-020300 decomposes_to
  → T-101 License开启（LKV3G5OLCH01）
  → T-006 配置URR（USAGERPTMODE=ONLINE）★ 核心
  → T-201 配置DCC模板与OCS链路 (ADD DIAMCONNGRP/DCCTEMPLATE)
  → T-203 配置Default Quota容灾 (SET UPDEFAULTQUOTA)
  → T-204 配置配额耗尽动作 (ADD QUOTAEXHAUSTACT) ★ 核心
  → T-006 策略刷新生效

[命令] T-204 invokes → ADD QUOTAEXHAUSTACT
  → operates_on → ConfigObject: QUOTAEXHAUSTACT
    → 关键参数: URRID, FACTION(BLOCK/REDIRECT/FORWARD)
  → impacted_by → DP-CH-04 sets_value_pattern(FACTION)

[证据] CS-CH-02 → [EV-KB-001(K028-K048), EV-KB-001(K037,K043-K045)]
```

### 5.3 链路C：融合计费（CS-CH-03）

```
[业务] CS-CH-03 融合计费方案
  → DP-CH-04 配额耗尽动作
  → DP-CH-08 跨网元一致性策略
  → BR-CH-10 SMF融合计费三联前置约束
  → SO-CH-09 配额语义
  → SO-CH-11 N40/PFCP协议栈 ★

[特性] CS-CH-03 uses_feature
  → GWFD-010173 融合计费（UDG N40执行）
  → WSFD-011206 融合计费（UNC Nchf交互）
  → GWFD-020301 内容计费（基础License）

[任务] WSFD-011206 decomposes_to（UNC 18步链）
  → T-301 SET CHGMODE=NchfMode ★ 三联前置之一
  → T-302 SET CHARGECTRL使能 ★ 三联前置之二
  → T-303 SET CHFINIT=SENDREQ + CHF选择链 ★ 三联前置之三
  → T-304 ADD CCT模板
  → T-006~T-005 URR三件套+绑定链

[命令] T-303 invokes → SET CHFINIT + ADD TNFINS/TNFGRP/SELECTCHFGBYCC
  → operates_on → ConfigObject: CHFINIT, TNFGRP, SELECTCHFGBYCC
  → constrained_by → CR-06 三联前置约束
                   → CR-08 跨网元名称一致性

[证据] CS-CH-03 → [EV-KB-001(K001,K101-K121,K201,K202,K105)]
```

---

## 6. 关键决策点（第1层）

| 决策点 | 决策问题 | 影响 |
|--------|---------|------|
| DP-CH-01 | 计费方式选择（离线/在线/融合） | 决定URR的USAGERPTMODE、是否需CCT模板、CHF/OCS/CG交互模式 |
| DP-CH-02 | 配置网元范围选择（UPF+SMF/UPF only/SMF only） | 决定生成UPF执行链、SMF编排链，还是双侧协同链 |
| DP-CH-03 | 匹配层次选择（L34/L7/混合） | 决定是否需要L7FILTER和PROTBINDFLOWF |
| DP-CH-04 | 配额耗尽动作选择（BLOCK/REDIRECT/FORWARD） | 决定QUOTAEXHAUSTACT配置和用户体验切换路径 |
| DP-CH-05 | 计费粒度选择（会话级/业务级/QoS flow级） | 决定是否需要SA识别和RG差异化 |
| DP-CH-06 | 计量方式选择（流量/时长/事件） | 决定URR.METERINGTYPE参数 |
| DP-CH-07 | 兜底策略选择（默认URR组/异常费率/全局兜底） | 决定DFTURRGRPNAME和DFTSIGURRGNAME绑定方案 |
| DP-CH-08 | 跨网元一致性策略（双产品协同/仅UPF本地/SMF动态下发） | 决定配置路径和CP/UP一致性要求 |

---

## 7. 与带宽场景图谱的差异

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| 共享根对象 | BD-CH-01=BD-BW-01=业务感知 | 同左 |
| ConfigurationSolution数量 | 7个（按计费方式/计量/兜底分） | 7个（按控制机制分） |
| 核心机制 | SA识别→Rule→PCC/URR计费链→Ga/Gy/N40上报→配额闭环 | SA识别→BWM限速→CAR/Shaping/FUP/GBR |
| 独有特性族 | 计费三件套(URR/URRGROUP/PCCPOLICYGRP)、融合计费(CCT/CHF选择) | BWM三级控制体系 |
| 独有ConfigObject | URRGRPBINDING, DIAMCONNGRP, DCCTEMPLATE, CCT, CHARGECHAR, CHGMODE, CHFINIT, TNFGRP, SELECTCHFGBYCC, CG | BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE, CATEGORYPROP |
| **共享ConfigObject** | RULE, USERPROFILE, PCCPOLICYGRP, FLOWFILTER, **URR, URRGROUP** | 同左 |
| **独有协议知识** ★ | Ga/Gy/DCC/N40/PFCP/Gx（6协议，1422行，SO-CH-10/11） | 无独立协议层 |
| 核心决策点差异 | 计费方式/配额耗尽动作/计量方式 | 带宽机制/控制粒度/规则类型 |
| 共享ConfigTask | T-002流过滤, T-003 PCC规则, T-004用户模板, T-005 APN绑定, T-007 PCC策略组, T-008刷新 | 同左（复用6个通用Task） |
| 证据层差异 | 31份（含2协议知识★） | 58份（24特性+32主题+2跨层分析） |

> 两场景图谱独立构建，不互相依赖；共享部分限于通用Task（6个）和通用ConfigObject（含URR/URRGROUP，但参数语义不同）。

---

## 8. 文档索引

| 文件 | 内容 | 对应Schema章节 |
|------|------|---------------|
| `00-overview.md` | 本文件：五层导航 + 对象计数 + 链路示例 | — |
| `01-business-graph.md` | 第1层：BD/NS/CS/DP/BR/SO 实例化（7 CS + 8 DP + 12 BR + 12 SO） | §8.1-8.6, §8.12 |
| `02-feature-graph.md` | 第2层：14 Feature + 11 License + 8 FeatureRule + depends_on | §9.3-9.5 |
| `03-task-layer.md` | 第3层：28 ConfigTask + 6 TaskRule + 20 TaskCommandOrderEdge | §10.1-10.3 |
| `04-command-graph.md` | 第4层：65 MMLCommand + 26 ConfigObject + 12 CommandRule | §11.1-11.7 |
| `05-cross-layer-mapping.md` | 第5层：跨层映射关系总表（~125边） | §12.1-12.5 |
| `06-evidence-index.md` | 第6层：证据层索引（31 EvidenceSource，含2协议知识★） | §10 EvidenceSource |

---

## 9. 合规检查清单

### 9.1 Schema合规

- [x] 所有对象类型严格匹配 Schema §8-§12 定义
- [x] 所有关系边严格匹配 Schema §8.12/§9.5/§10.3/§11.7/§12 定义
- [x] 无 Schema §13 列出的禁止关系（CS→ConfigObject 直接绑定、Feature→MMLCommand 直接绑定等）
- [x] 所有对象包含 `source_evidence_ids` 字段

### 9.2 端到端链路完整性

- [x] 路径A (内容计费): BD→NS→CS-CH-04→GWFD-020301→T-006→ADD URR→URR ✓
- [x] 路径B (在线计费): BD→NS→CS-CH-02→GWFD-020300→T-204→ADD QUOTAEXHAUSTACT→QUOTAEXHAUSTACT ✓
- [x] 路径C (融合计费): BD→NS→CS-CH-03→WSFD-011206→T-303→SET CHFINIT→CHFINIT ✓

### 9.3 证据可追溯

- [x] 每个图谱对象的 `source_evidence_ids` 指向真实存在的知识文档
- [x] 证据索引覆盖 15 EV-FK + 3 EV-KB + 2 EV-BS + 2 EV-PK + 5 EV-SK + 1 EV-CFA + 1 EV-FDL + 1 EV-DES + 1 EV-BSA = 31份
- [x] **协议知识完整入图谱**：Ga/Gy/DCC(680行)→SO-CH-10；N40/PFCP/Gx(742行)→SO-CH-11
- [x] 跨层映射中的边与各层文件中的对象引用一致

### 9.4 信息无损验证（相对旧版 `新三层图谱/`）

- [x] **CS拆分**：1个DS-01 → 7个CS闭包（按计费方式/计量/兜底维度）
- [x] **协议知识保留**：1,422行协议知识完整映射到SO-CH-10/11（旧版完全丢失）
- [x] **DP补齐**：4个 → 8个（新增配额耗尽/计量方式/兜底/跨网元一致性）
- [x] **跨层映射建立**：~125条跨层边（旧版无独立文件）
- [x] **证据索引建立**：31份EvidenceSource注册表（旧版无独立文件）
- [x] **端到端链路**：3条完整路径（BD→NS→CS→Feature→Task→Command→Object）

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
| **计费架构理解** | 通过SO-CH-10/11协议栈对象 → 理解Ga/Gy/N40/PFCP协议交互 |
| **配额控制设计** | CS-CH-02/03/06 → 理解在线/融合/降速三种配额闭环 |
| **知识问答** | 给定问题 → 通过图谱对象关系导航 → 返回结构化答案 |

---

## 11. 后续演进

| 演进方向 | 说明 |
|---------|------|
| 与带宽场景图谱融合 | 共享BD根对象，通过BD-level的contains NS边连接两个场景 |
| 访问限制场景接入 | 套餐3图谱独立构建后，三场景共享业务感知根，形成业务感知全景 |
| 图数据库落地 | Schema定义的对象/边可直接映射为 Neo4j/JanusGraph 的Node/Edge |
| 算子层接入 | 在图谱之上构建服务层算子，按§10使用场景封装查询API |
| 配置生成自动化 | 基于CS闭包+Task链，自动生成端到端MML命令脚本 |

---

## 12. 重构说明（相对旧版 `新三层图谱/`）

本图谱为按带宽场景7文件结构重构的完整版，主要改进：

| 改进点 | 旧版（新三层图谱/） | 新版（three-layer-graph/） |
|-------|---------------------|---------------------------|
| 文件数 | 3个（业务+特性+命令） | 7个（+任务层+跨层映射+证据+总览） |
| CS闭包 | 1个 DS-01 | 7个 CS-CH-01~07 |
| DecisionPoint | 4个 | 8个 |
| 协议知识 | 完全丢失 | 2个SO完整映射（1422行） |
| ConfigTask | 17个内嵌 | 28个独立层 |
| 跨层映射 | 无 | ~125条边独立文件 |
| 证据索引 | 无 | 31份EvidenceSource注册表 |
| 端到端链路 | 无 | 3条完整路径 |

> 旧版文件保留在 `新三层图谱/` 目录，未修改未删除，供对比参考。

---

> 本总览文件是计费场景三层图谱的入口文档。阅读顺序建议：**先读本文件理解全局 → 按需深入各层文件 → 通过06-evidence-index回溯证据**。
