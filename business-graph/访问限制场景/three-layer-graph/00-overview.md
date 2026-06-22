# 访问限制场景三层图谱 · 总览（00-overview）

> **文件定位**：`three-layer-graph/00-overview.md`
> **作用**：五层架构导航、对象计数统计、端到端链路示例、双轨道+五子轨架构总览、三场景差异对比、文档索引
> **配套Schema**：`三层图谱Schema-最终版-v0.1.md`
> **配套本体**：`三层图谱本体标准定义.md`、`三层图谱对象与关系设计.md`
> **Wave4 总览文件**：汇总 01~06 六层文档，是访问限制场景三层图谱的入口

---

## 1. 一句话定位

访问限制场景（业务感知套餐3）三层图谱是**面向5G核心网访问控制**（PCC 阻塞 / 头增强 / URL 重定向 / URL 过滤 / 接入控制）的领域知识图谱，以 **RULE.POLICYTYPE 为动作轨道总开关（★双轨道+五子轨架构）**，把分散在 UDG（用户面 11 独有特性）与 UNC（控制面）共 **19 特性**、31 份知识资产中的配置知识，组织成可追溯、可推理、可复用的结构化资产。

> **★ 双轨道+五子轨架构（访问限制独有）**：RULE.POLICYTYPE 取值 `ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY` 形成五种动作子轨（轨道 A 内），配合轨道 B（URL 过滤体系 CFTEMPLATE/CONTCATEGBIND.ACTION 显式 BLOCK/PERMIT/REDIRECT）构成"轨道 A 五子轨 + 轨道 B 独立"的双轨道动作路由体系，是本场景区别于计费（固定 CHARGING）和带宽控制（BWM/PCC/QOS/ADC 四策略类型）的标志性架构。
>
> **★ P5 批次 1~3 计数同步**：特性数从 15 修正为 19（U-H-02 补 4 个 UNC 接入控制辅助特性 WSFD-106003/105003/106005/105006，见 `02` §1.9）；MMLCommand 从 62 修正为 68（U-H-04，UDG 48 含 PCC 规则与策略 6 命令）；Evidence 从 27 修正为 31（U-H-03 补 EV-CA-D1~D4 + U-H-02/批次3 补 EV-FK-AC-16~19）。本总览各章节计数已全部同步。

---

## 2. 五层架构总览

```
┌─────────────────────────────────────────────────────────────────────┐
│  第1层 业务图谱 BusinessGraph                                        │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ BD(1) → NS(1) → CS(9) 配置方案闭包（★三场景最多）              │  │
│  │                     ↓                                        │  │
│  │     DP(8) ←→ BR(10) ←→ SO(7)  语义对象                       │  │
│  │     Scope(5) + Participant(8)                                │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ uses_feature(30) / uses_task(9)                         │
├─────────────────────────────────────────────────────────────────────┤
│  第2层 特性图谱 FeatureGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Feature(19: UDG11+UNC8) ──depends_on(21)──→ Feature          │  │
│  │     │                                                         │  │
│  │     ├─ requires_license(15) ──→ License(15)                   │  │
│  │     ├─ constrained_by(8) ──→ FeatureRule(8)                   │  │
│  │     └─ decomposes_to(19) ──→ ConfigTask (跨层边)              │  │
│  │     └─ task_order(25) ──→ FeatureTaskOrderEdge                │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ decomposes_to / task_order                              │
├─────────────────────────────────────────────────────────────────────┤
│  第3层 任务原子层 TaskLayer                                          │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ ConfigTask(17: generic8 + 独有9)                              │  │
│  │   ├─ 轨道A独有7（T-AC-101~107 头增强/重定向/ADC/PCC动作组）    │  │
│  │   ├─ 轨道B独有1（T-AC-108 URL过滤）                           │  │
│  │   └─ UNC侧独有1（T-AC-109 位置触发）                          │  │
│  │     │                                                         │  │
│  │     ├─ constrained_by(8) ──→ TaskRule(8)                      │  │
│  │     ├─ has_decision(3) ──→ DP(3)                              │  │
│  │     ├─ invokes(~68) ──→ MMLCommand (跨层边)                   │  │
│  │     ├─ targets(~45) ──→ SO / ConfigObject (跨层边)            │  │
│  │     └─ orchestrates(59) ──→ TaskCommandOrderEdge              │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ invokes                                                 │
├─────────────────────────────────────────────────────────────────────┤
│  第4层 命令图谱 CommandGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ MMLCommand(68: UDG48 + UNC20)                                 │  │
│  │     │                                                         │  │
│  │     ├─ operates_on(65) ──→ ConfigObject(41)                   │  │
│  │     │                      ├─ 共享18（三场景通用骨架）         │  │
│  │     │                      └─ 独有23（双轨道+五子轨动作对象族+UNC侧2） │  │
│  │     │                      └─ contains/refers等(39) ──→ Obj   │  │
│  │     └─ governed_by ←── CommandRule(14)                        │  │
│  └───────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────┤
│  第5层 跨层映射 CrossLayerMapping                                    │
│  CS↔Feature(30) + CS↔Task(9) + Feature↔Task(19)                    │
│  + Task↔Cmd(~68) + Task↔SO/Obj(~45) + DP↔CS/Task(9)               │
│  + DP↔Param(6) + refined_by(8)                                      │
│  跨层边总计：~190                                                    │
├─────────────────────────────────────────────────────────────────────┤
│  第6层 证据层 EvidenceLayer                                          │
│  EvidenceSource(35) ←── source_evidence_ids ── 所有图谱对象         │
│  含 19 EV-FK-AC + 8 EV-TK-AC + 2 EV-CA-AC + 4 EV-CA-D + 2 EV-BS = 35│
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. 对象计数统计

### 3.1 各层对象总数

| 层级 | 对象类型 | 数量 | 文件 |
|------|---------|------|------|
| **第1层 业务图谱** | BusinessDomain (BD) | 1（BD-AC-01=BD-CH-01=BD-BW-01，三场景共享） | `01-business-graph.md` |
| | NetworkScenario (NS) | 1（NS-AC-01） | |
| | ConfigurationSolution (CS) | 9（CS-AC-01~09，★三场景最多） | |
| | DecisionPoint (DP) | 8（DP-AC-01~08） | |
| | BusinessRule (BR) | 10（BR-AC-01~10） | |
| | SemanticObject (SO) | 7（SO-AC-01~07，无协议栈） | |
| | Scope（子对象） | 5（subscriber/subscription/access/service_selection/location） | |
| | Participant（子对象） | 8（UPF/SMF/AMF/PCF/ICAP Server/IPFarm/ADC-SA/RAN-UE） | |
| | **业务层小计** | **49** | |
| **第2层 特性图谱** | Feature | 19（UDG 独有 11 + UNC 独有 1+4 接入控制辅助 + 三场景共享 3，★ P5 批次 1 补 4 个 UNC 辅助特性） | `02-feature-graph.md` |
| | License | 15（UDG 12 + UNC 3，全部需 License；4 个 UNC 接入控制辅助特性无独立 License） | |
| | FeatureRule | 8（FR-AC-01~08） | |
| | depends_on 边 | 21（UDG 14 + UNC 7，含 4 个 UNC 辅助特性的 4 条 depends_on） | |
| | FeatureTaskOrderEdge | 25（FTOE-AC-001~025，5 个核心 Feature） | |
| | **特性层小计** | **67 对象 + 69 关系边** | |
| **第3层 任务原子层** | ConfigTask（generic） | 8（T-001~T-008，三场景共享） | `03-task-layer.md` |
| | ConfigTask（轨道A独有） | 7（T-AC-101~107 头增强/重定向族/ADC/PCC动作组） | |
| | ConfigTask（轨道B独有） | 1（T-AC-108 URL 过滤） | |
| | ConfigTask（UNC侧独有） | 1（T-AC-109 位置触发） | |
| | TaskRule | 8（TR-AC-01~08） | |
| | DecisionPoint（任务层，★ ID 与业务层复用，owner_layer=task 区分） | 3（DP-AC-01/02/03，详见 03 §6 ID 复用说明） | |
| | TaskCommandOrderEdge | 59（§7 Task内部50 + §8 跨Task场景链9） | |
| | **任务层小计** | **60 对象 + 59 编排边** | |
| **第4层 命令图谱** | MMLCommand | 68（CMD-UDG-001~048 全 48 含 PCC 规则与策略 6 命令 + CMD-UNC-001~020 共 20，★ P5 修正 U-H-04） | `04-command-graph.md` |
| | ConfigObject | 41（共享18 OBJ-RULE等通用 + 独有23 OBJ-AC-*） | |
| | CommandRule | 14（CR-AC-01~14） | |
| | ConfigObject contains/refers_to/depends_on/conflicts_with/activates 边 | 39（通用9 + 轨道A(PCC)3 + 轨道D(HEADEN)4 + 轨道C(SMARTREDIRECT)8 + 轨道B-1(WEBPROXY)7 + 轨道B-2(URL过滤)10 + 接入控制4） | |
| | operates_on 边 | 65（UDG 45 + UNC 20） | |
| | **命令层小计** | **~227** | |
| **第5层 跨层映射** | 跨层边 | ~190（★ P5 批次 3：uses_feature 26→30、decomposes_to 15→19、invokes 62→68） | `05-cross-layer-mapping.md` |
| **第6层 证据层** | EvidenceSource | 35（EV-FK-AC 19 含 4 UNC 辅助 + EV-TK-AC 8 + EV-CA-AC 2 + EV-CA-D 4 + EV-BS-AC 2，★ P5 批次 3 新增 EV-FK-AC-16~19） | `06-evidence-index.md` |
| **图谱对象总计** | — | **约 432**（不含跨层边；计入跨层边约 622 节点+边） | — |

> **计数核对**：01 (49) + 02 (67) + 03 (60) + 04 (227) + 06 (35) = **438 对象**（含 EvidenceSource 35）；跨层边 05 (~190)。所有数字均从 01~06 实际文件提取，未编造。

### 3.2 关键关系边总数

| 关系类型 | 数量 | 所在文件 |
|---------|------|---------|
| BD contains NS | 1 | `01-business-graph.md` |
| NS instantiated_as CS | 9 | `01-business-graph.md` |
| CS uses_feature | 30（★ P5 批次 3：26+4 UNC 辅助特性边） | `05-cross-layer-mapping.md` |
| CS uses_task（闭包级） | 9 | `05-cross-layer-mapping.md` |
| CS has_decision（DP归属） | 14 | `01-business-graph.md` |
| CS constrained_by BR | 27 | `01-business-graph.md` |
| CS uses_semantic_object | 31 | `01-business-graph.md` |
| DP selects CS/Task | 9 | `05-cross-layer-mapping.md` |
| DP sets_value_pattern | 6 | `05-cross-layer-mapping.md` |
| Feature depends_on | 21（★ P5 批次 1：17+4 UNC 辅助特性 depends_on） | `02-feature-graph.md` |
| Feature requires_license | 15（4 个 UNC 辅助特性无独立 License） | `02-feature-graph.md` |
| Feature constrained_by（FeatureRule） | 8 | `02-feature-graph.md` |
| Feature decomposes_to Task | 19（★ P5 批次 3：15+4 UNC 辅助特性 Task 映射） | `05-cross-layer-mapping.md` |
| Feature task_order（FTOE） | 25 | `02-feature-graph.md` |
| ConfigTask constrained_by（TaskRule） | 8 | `03-task-layer.md` |
| ConfigTask has_decision（任务层DP） | 3 | `03-task-layer.md` |
| ConfigTask orchestrates（TCOE） | 59 | `03-task-layer.md` |
| ConfigTask invokes MMLCommand | ~68（★ P5 修正 U-H-04） | `05-cross-layer-mapping.md` |
| ConfigTask targets SO/ConfigObject | ~45 | `05-cross-layer-mapping.md` |
| ConfigObject contains/refers_to/depends_on/conflicts_with/activates | 39 | `04-command-graph.md` |
| MMLCommand operates_on ConfigObject | 65 | `04-command-graph.md` |
| MMLCommand governed_by CommandRule | 14 | `04-command-graph.md` |
| BR/TR/FR refined_by | 8 | `05-cross-layer-mapping.md` |
| 图谱对象 source_evidence_ids | 全对象覆盖 | `06-evidence-index.md` |

---

## 4. 九大方案闭包（第1层核心，★按双轨道+五子轨分类）

| 方案ID | 方案名称 | 核心机制 | 主用特性 | 动作轨道 |
|--------|---------|---------|---------|---------|
| **CS-AC-01** | **PCC 阻塞方案** | FILTER/FLOWFILTER → RULE(POLICYTYPE=PCC) → PCCPOLICYGRP → DISCARD 兜底阻塞 | GWFD-020351, WSFD-109101, GWFD-020357 | ★轨道A-PCC |
| **CS-AC-02** | **头增强方案** | FILTER/L7FILTER → HEADEN（含ANTIFRAUD/GRAYLIST） → RULE(POLICYTYPE=HEADEN) → 字段插入 | GWFD-110261/262/263, GWFD-110401, GWFD-020357 | ★轨道D-HEADEN |
| **CS-AC-03** | **HTTP 重定向方案** | EXTENDEDFILTER+ERRORCODE → SMARTHTTPREDIR → RULE(POLICYTYPE=SMARTREDIRECT) → HTTP响应改写 | GWFD-110284, GWFD-020357 | ★轨道C-SMARTREDIRECT |
| **CS-AC-04** | **DNS 重定向方案** | EXTENDEDFILTER+ERRORCODE(NXDOMAIN) → DNSOVERWRITING → RULE(POLICYTYPE=SMARTREDIRECT) → DNS响应改写 | GWFD-110283, GWFD-020357 | ★轨道C-SMARTREDIRECT |
| **CS-AC-05** | **Portal/WebProxy 重定向方案** | Portal: IPFARM+CAPMODETHRES captive; WebProxy: IPFARM+BLACKLISTRULE+RULE(POLICYTYPE=WEBPROXY) L3 IP NAT（唯一支持HTTPS） | GWFD-110281, GWFD-110282, GWFD-020357 | ★轨道C-SMARTREDIRECT + ★轨道B-1-WEBPROXY |
| **CS-AC-06** | **URL 过滤方案（轨道 B）** | VPNInst+ICAPSERVER+CFTEMPLATE/CONTCATEGBIND.ACTION 显式 BLOCK/PERMIT/REDIRECT；唯一显式 PERMIT | GWFD-110471, GWFD-020357 | ★轨道B-2-URL过滤（独立） |
| **CS-AC-07** | **接入控制方案（UNC 侧）** | AMF 的 SAR/区域漫游/ODB；SMF 服务区域限制；USRLOCATION+USRLOCATIONGRP 位置触发策略下发 | WSFD-211001, WSFD-106003, WSFD-105003, WSFD-106005, WSFD-105006 | ★轨道A-PCC（UNC侧位置触发） |
| **CS-AC-08** | **配额耗尽重定向方案** | URR 配额耗尽触发 US_RE/NO_CREDIT → PCF 决策 RedirectInformation → N7→N4→UPF 执行 | GWFD-020351, WSFD-109101, GWFD-110284 | ★轨道A-PCC（PCF 决策） |
| **CS-AC-09** | **区域引导重定向方案** | WSFD-211001 PRA/PLMN 变化触发 → PCF 重定向策略 → 套餐订购/验证页 | WSFD-211001, GWFD-110284, GWFD-110281 | ★轨道A-PCC（PCF 决策 + 位置触发） |

> **双轨道+五子轨动作分布**：
> - **轨道 A（PCC 体系，RULE.POLICYTYPE 隐式驱动）**：CS-AC-01（PCC）/ CS-AC-02（HEADEN）/ CS-AC-03/04（SMARTREDIRECT）/ CS-AC-05-Portal（SMARTREDIRECT）/ CS-AC-05-WebProxy（WEBPROXY）/ CS-AC-07（PCC 位置触发）/ CS-AC-08（PCC PCF 决策）/ CS-AC-09（PCC PCF+位置）
> - **轨道 B-1（WEBPROXY/Portal 独立体系，L3 IP NAT）**：CS-AC-05-WebProxy 子链
> - **轨道 B-2（URL 过滤体系，CFTEMPLATE/CONTCATEGBIND.ACTION 显式）**：CS-AC-06（唯一显式 PERMIT）
> - **轨道 C（SMARTREDIRECT，POLICYNAME 区分 HTTP 重定向 vs DNS 纠错）**：CS-AC-03/04
> - **轨道 D（HEADEN）**：CS-AC-02

---

## 5. 端到端链路示例（三层贯通，★覆盖双轨道+五子轨）

### 5.1 链路 A：PCC 阻塞 / 接入控制（轨道 A，DISCARD 动作）

```
[业务] BD-AC-01 业务感知（= BD-CH-01 = BD-BW-01，三场景共享）
  → NS-AC-01 访问限制场景
    → CS-AC-01 PCC 阻塞方案（或 CS-AC-07 UNC 接入控制）
      → DP-AC-01 选择 DISCARD 动作
      → DP-AC-03 选择轨道 A（PCC 体系）
      → DP-AC-02 选择规则类型（动态/预定义/本地）
      → BR-AC-01 预定义规则三网元一致性
      → BR-AC-07 RULE.POLICYTYPE 决定动作轨道（双轨道+五子轨）
      → SO-AC-01（DISCARD）, SO-AC-02（过滤条件）, SO-AC-06（规则语义）, SO-AC-07（轨道A）

[特性] CS-AC-01 uses_feature
  → GWFD-020351 PCC(UDG)（策略载体）
  → WSFD-109101 PCC(UNC)（策略下发承载）
  → GWFD-020357 ADC(UDG)（L7 横切前置 + 兜底阻塞）

[任务] GWFD-020357 decomposes_to（FTOE-AC-001~005）
  → T-007 License 开启（LKV3G5ADCF01 + LKV3G5PCCB01）
  → T-008 SA 特征库加载（LOD SIGNATUREDB + LOD PARSERDB）
  → T-AC-101 配置 ADC（ADD ADCPARA + RULE:POLICYTYPE=ADC）★ 兜底阻塞
  → T-AC-107 配置 PCC 动作组（ADD URR + URRGROUP + PCCPOLICYGRP）
  → T-002 配置流过滤器（ADD FLOWFILTER + FLTBINDFLOWF）
  → T-003 配置 PCC 规则（ADD RULE:POLICYTYPE=PCC, POLICYNAME=PCCPOLICYGRP）★ 核心规则
  → T-004 配置用户模板（ADD USERPROFILE + RULEBINDING）
  → T-006 SET REFRESHSRV（must_be_last，60s 生效）

[命令] T-003 invokes → ADD RULE (CMD-UDG-043)
  → operates_on → ConfigObject: RULE（OBJ-RULE）
    → 关键参数: RULENAME, POLICYTYPE=PCC, PRIORITY, FLOWFILTERNAME, POLICYNAME=PCCPOLICYGRP
  → constrained_by → CR-AC-02 POLICYTYPE 决定动作对象链（PCC→PCCPOLICYGRP）
  → constrained_by → CR-AC-09 预定义规则名三网元一致
  → impacted_by → DP-AC-03 sets_value_pattern(POLICYTYPE=PCC)

[证据] CS-AC-01 → [EV-CA-AC-01, EV-FK-AC-02, EV-FK-AC-04, EV-TK-AC-01/02/04]
  ADD RULE → [EV-FK-AC-CFA=EV-CA-AC-01, EV-CA-D1]
```

### 5.2 链路 B：URL 过滤（★轨道 B-2，BLOCK/PERMIT/REDIRECT 显式动作，唯一 PERMIT）

```
[业务] BD-AC-01 → NS-AC-01
  → CS-AC-06 URL 过滤方案（轨道 B 独立体系）
    → DP-AC-01 选择 BLOCK/PERMIT/REDIRECT
    → DP-AC-03 选择轨道 B（URL 过滤体系，独立于 PCC）★
    → DP-AC-05 选择 L7 匹配（URL 分类）
    → BR-AC-05 REFRESHSRV 最后执行
    → BR-AC-10 PERMIT 唯一性（URL 过滤独有）
    → SO-AC-01（BLOCK/PERMIT/REDIRECT）, SO-AC-02（URL 分类）, SO-AC-07（轨道B）

[特性] CS-AC-06 uses_feature
  → GWFD-110471 URL 过滤基本功能（轨道 B 核心，唯一显式 PERMIT）
  → GWFD-020357 ADC(UDG)（URL 提取前置，HTTPS 仅 SNI）

[任务] GWFD-110471 decomposes_to（FTOE-AC-016~021）
  → T-007 License 开启（LKV3G5UFBF01，82200FCP）
  → T-008 SA 特征库加载
  → T-AC-108 配置 URL 过滤 ★ 完整独立链（TE-AC-108-1~16）
    ├─ ① ICAP 互通前置层：VPNINST → LOGICINF → ICAPSERVER → ICAPLOCALINFO → ICAPSVRGRP → ICAPSVRBINDISG
    ├─ ② APN 开关：ADD APN + SET APNCFFUNC
    ├─ ③ CF 业务层：CFPROFILE → CFTEMPLATE(ACTION) → APNCFTEMPLATE → CFPROFBINDCFT
    ├─ ④ 分类级动作：CONTCATEGROUP → CONTCATEGBIND(ACTION，覆盖模板级缺省)
    ├─ ⑤ 共用 PCC 触发层：URR → URRGROUP → PCCPOLICYGRP → RULE(POLICYTYPE=PCC 仅触发)
    └─ ⑥ 辅助：CFCACHEPARA, GLBCFFUNC, CFWHITEURLLST, CFIPWHITELIST
  → T-006 SET REFRESHSRV（must_be_last）

[命令] T-AC-108 invokes → ADD CFTEMPLATE (CMD-UDG-033) + ADD CONTCATEGBIND (CMD-UDG-037)
  → operates_on → ConfigObject: CFTEMPLATE（OBJ-AC-CFTEMPLATE）/ CONTCATEGBIND（OBJ-AC-CONTCATEGBIND）
    → 关键参数: CFTEMPLATENAME, ICAPSRVGMNAME, ACTION=BLOCK/PERMIT/REDIRECT（模板级缺省）
    → 关键参数: CFPROFILENAME, CONTCATEGNAME, ACTION（分类级精确，覆盖模板级）
  → constrained_by → CR-AC-05 ICAP Server 必需（前置链路）
  → constrained_by → CR-AC-06 PERMIT 动作唯一性（仅轨道 B 显式支持）
  → constrained_by → CR-AC-14 双轨可并存（轨道 A + 轨道 B）
  → impacted_by → DP-AC-03 sets_value_pattern(轨道 B → CFTEMPLATE.ACTION)

[证据] CS-AC-06 → [EV-CA-AC-01, EV-FK-AC-09, EV-TK-AC-07]
  ADD CFTEMPLATE → [EV-FK-AC-14, EV-CA-D1]
```

### 5.3 链路 C：HTTP 重定向（★轨道 C，SMARTREDIRECT）

```
[业务] BD-AC-01 → NS-AC-01
  → CS-AC-03 HTTP 重定向方案
    → DP-AC-01 选择 REDIRECT
    → DP-AC-03 选择轨道 A（PCC 体系，POLICYTYPE=SMARTREDIRECT 子轨）
    → DP-AC-06 选择重定向目标（第三方服务器）
    → DP-AC-07 选择协议（仅 HTTP1.x）
    → BR-AC-07 RULE.POLICYTYPE=SMARTREDIRECT
    → BR-AC-09 加密协议仅 WebProxy 可处理（HTTP 重定向不支持 HTTPS）
    → SO-AC-01（REDIRECT）, SO-AC-03（SMARTHTTPREDIR）, SO-AC-07（SMARTREDIRECT）

[特性] CS-AC-03 uses_feature
  → GWFD-110284 HTTP 智能重定向（L7 HTTP 响应改写）
  → GWFD-020357 ADC(UDG)（L7 解析前置）
  → GWFD-110261 HTTP 头增强（可选，REDIRAPPENDINFO 携带 MSISDN/IMSI）

[任务] GWFD-110284 decomposes_to（FTOE-AC-012~015）
  → T-007 License 开启（LKV3G5SHPR01，82209783）
  → T-008 SA 特征库加载
  → T-001 规划业务分类（EXTENDEDFILTER + ERRORCODE，多条件 AND）
  → T-AC-103 配置 HTTP 智能重定向 ★
    ├─ ADD EXTENDEDFILTER（URL/UserAgent/ContentType/URLPostfix 多维）
    ├─ ADD ERRORCODE（HTTP 错误码 GT 400）
    ├─ ADD REDIRAPPENDINFO（携带 MSISDN/IMSI/IMEI，可选）
    ├─ ADD SMARTHTTPREDIR（绑定 EXTFLT + ERRORCODE + APPENDINFO）
    └─ ADD RULE:POLICYTYPE=SMARTREDIRECT, POLICYNAME=SMARTHTTPREDIR
  → T-002/T-004/T-006 流过滤+用户模板+刷新

[命令] T-AC-103 invokes → ADD SMARTHTTPREDIR (CMD-UDG-016) + ADD RULE (043)
  → operates_on → ConfigObject: SMARTHTTPREDIR（OBJ-AC-SMARTHTTPREDIR）
    → 关键参数: SMTHTTPREDINAME, SERVERURL, EXTFLTTYPE1/2(AND), EXTFLTNAME1/2, APPENDINFONAME, BINDErrCODENAME
  → constrained_by → CR-AC-02 POLICYTYPE=SMARTREDIRECT → POLICYNAME 指向 SMARTHTTPREDIR
  → constrained_by → CR-AC-03 SMARTREDIRECT 两子类型共用 POLICYTYPE（区分点在 POLICYNAME 指向 SMARTHTTPREDIR vs DNSOVERWRITING）
  → constrained_by → CR-AC-10 HTTPS/HTTP2.0 加密盲区（HTTP 重定向不支持）

[证据] CS-AC-03 → [EV-CA-AC-01, EV-FK-AC-05, EV-TK-AC-06]
  ADD SMARTHTTPREDIR → [EV-FK-AC-13, EV-CA-D3]
```

### 5.4 链路 D：头增强（★轨道 D，HEADEN，含防欺诈强耦合）

```
[业务] BD-AC-01 → NS-AC-01
  → CS-AC-02 头增强方案
    → DP-AC-01 选择 HEADEN
    → DP-AC-03 选择轨道 A（PCC 体系，POLICYTYPE=HEADEN 子轨）
    → DP-AC-05 选择 L7 匹配（URL/SNI/Method）
    → DP-AC-07 选择协议（HTTP1.x / HTTPS / RTSP 三选一）
    → DP-AC-02（任务层）头防欺诈使能决策（ENABLE 需双开 License）
    → BR-AC-04 License 前置门控（头防欺诈 82209786 + 头增强 82209777 双开）
    → BR-AC-06 头防欺诈依赖头增强
    → BR-AC-08 字段加密与编码约束
    → SO-AC-01（HEADEN）, SO-AC-04（头增强字段）, SO-AC-06（规则语义）

[特性] CS-AC-02 uses_feature
  → GWFD-110261 HTTP 头增强（HTTP1.x，支持防欺诈）
  → GWFD-110262 RTSP 头增强（RTSP，不支持防欺诈，族内唯一例外）
  → GWFD-110263 HTTPS 头增强（SSL Extension TLV，支持防欺诈）
  → GWFD-110401 HTTP 头防欺诈（强耦合 110261）
  → GWFD-020357 ADC(UDG)（L7 解析前置）

[任务] GWFD-110261 + GWFD-110401 decomposes_to（FTOE-AC-006~011，含防欺诈强耦合）
  → T-007 License 双开（LKV3G5HTHE01 头增强 + LKV3G5HHAS01 头防欺诈）
  → T-008 SA 特征库 + 协议解析库加载
  → T-001 规划业务分类（FILTER + L7FILTER + WELLKNOWNPORT）
  → T-AC-102 配置头增强对象（ADD HEADEN:ANTIFRAUD=ENABLE/GRAYLIST=ENABLE）★ 核心
    ├─ ADD WELLKNOWNPORT（识别 HTTP 端口 80/8080）
    ├─ ADD HEADEN（DATATYPE=IMSI1/MSISDN1, ENCRYALGORI=AES128/SHA256, ANTIFRAUD=ENABLE）
    └─ 防欺诈子模式：检测→字段纠正/冗余清理→头增强插入（BIT1030 控制顺序）
  → T-003 配置 PCC 规则（ADD RULE:POLICYTYPE=HEADEN, POLICYNAME=HEADEN 对象名）
  → T-004/T-006 用户模板+刷新

[命令] T-AC-102 invokes → ADD HEADEN (CMD-UDG-014) + ADD RULE (043)
  → operates_on → ConfigObject: HEADEN（OBJ-AC-HEADEN）
    → 关键参数: HEADERENNAME, DATATYPE, PREFIXNAME, ENCRYALGORI, PSWDKEY, ANTIFRAUD(ENABLE/DISABLE), GRAYLIST(ENABLE/DISABLE)
  → constrained_by → CR-AC-02 POLICYTYPE=HEADEN → POLICYNAME 指向 HEADEN 对象
  → constrained_by → CR-AC-04 头防欺诈强依赖头增强（License 双开）
  → constrained_by → CR-AC-11 RTSP 不支持头防欺诈（族内唯一例外）

[证据] CS-AC-02 → [EV-CA-AC-01, EV-CA-AC-02, EV-FK-AC-03/04, EV-TK-AC-05/08]
  ADD HEADEN → [EV-FK-AC-06/07/08/13, EV-CA-D2]
```

### 5.5 补充链路：WebProxy 重定向（★轨道 B-1，唯一支持 HTTPS/HTTP2.0）

```
[业务] BD-AC-01 → NS-AC-01
  → CS-AC-05 Portal/WebProxy 重定向方案（WebProxy 子链）
    → DP-AC-06 选择重定向目标=Proxy 服务器
    → DP-AC-07 选择协议=任意 TCP（含 HTTPS/HTTP2.0）★ 唯一
    → BR-AC-09 加密协议仅 WebProxy 可处理
    → SO-AC-01（REDIRECT）, SO-AC-03（IPFarm-Proxy）, SO-AC-07（WEBPROXY 独立体系）

[特性] CS-AC-05 uses_feature → GWFD-110282 WebProxy（L3 IP NAT，支持加密协议）

[任务] GWFD-110282 decomposes_to
  → T-007 License 开启（LKV3G5WEBP01，82209781）
  → T-AC-106 配置 WebProxy ★ 双规则链
    ├─ ADD LOGICINF + IPFARM + IPFARMSERVER + BLACKLISTRULE（Proxy 服务器集群）
    ├─ ADD URR + URRGROUP + PCCPOLICYGRP（计费属性）
    ├─ ADD RULE:POLICYTYPE=WEBPROXY, POLICYNAME=IPFARM ★ 重定向规则
    └─ ADD RULE:POLICYTYPE=PCC, POLICYNAME=PCCPOLICYGRP ★ 计费规则（同一 FLOWFILTER，不同 RULENAME）

[命令] T-AC-106 invokes → ADD RULE×2 (CMD-UDG-043)
  → constrained_by → CR-AC-02 POLICYTYPE=WEBPROXY → POLICYNAME 指向 IPFARM
  → constrained_by → TR-AC-06 WebProxy 双规则约束（WEBPROXY+PCC）
  → constrained_by → CR-AC-14 双轨可并存
```

> **双轨道+五子轨覆盖核查**：
> - 轨道 A（PCC 体系）：链路 A（PCC 阻塞）+ 链路 D（HEADEN 子轨）+ 链路 C（SMARTREDIRECT 子轨）✅
> - 轨道 B-1（WEBPROXY/Portal 独立体系，L3 IP NAT）：补充链路（WebProxy）✅
> - 轨道 B-2（URL 过滤体系，CFTEMPLATE.ACTION 显式）：链路 B（URL 过滤）✅
> - 轨道 C（SMARTREDIRECT）：链路 C（HTTP 重定向）+ DNS 纠错子链（共用 SMARTREDIRECT，POLICYNAME 区分）✅
> - 轨道 D（HEADEN）：链路 D（头增强）✅

---

## 6. 关键决策点（第1层 8 个）

| 决策点 | 决策问题 | 影响 |
|--------|---------|------|
| DP-AC-01 | 动作类型选择（DISCARD/HEADEN/REDIRECT/PERMIT-仅URL过滤） | 决定 CS 闭包（CS-AC-01/02/03~05/06/08/09）和动作对象；决定 RULE.POLICYTYPE 或 CFTEMPLATE.ACTION 路径 |
| DP-AC-02 | 规则类型选择（动态/预定义/本地） | 决定规则生命周期、三网元一致性要求、是否支持 L7；URL 过滤/定向业务必须用预定义（PCF 无 L7 能力） |
| **DP-AC-03** ★ | **动作轨道选择（轨道 A PCC 体系 vs 轨道 B URL 过滤体系）** | **决定 ConfigObject 体系（RULE vs CFTEMPLATE）、动作指定方式（隐式 vs 显式）、外部依赖（可选 PCRF vs 必需 ICAP）、是否支持 PERMIT；★sets_value_pattern RULE.POLICYTYPE 体现双轨道+五子轨核心** |
| DP-AC-04 | 网元范围选择（UPF执行/SMF翻译/AMF接入控制/主辅锚点） | 决定规则生效范围；UNC 侧粗粒度接入控制 vs UDG 侧细粒度业务控制 |
| DP-AC-05 | 匹配层次选择（L3/L4/L7/DNS层/应用层） | 决定 Filter 类型（FILTER/L7FILTER/EXTENDEDFILTER）、SA 依赖；HTTPS 场景 L7 只能基于 SNI |
| DP-AC-06 | 重定向目标选择（充值页/套餐订购页/Portal/Proxy/第三方/DNS Platform） | 决定重定向特性选择（HTTP 重定向/DNS/Portal/WebProxy）、IP Farm 需求 |
| DP-AC-07 | 协议支持选择（仅HTTP1.x/HTTP+HTTPS/HTTP+RTSP/任意TCP含HTTPS/DNS） | 决定特性选择、SA 依赖、加密算法需求；仅 WebProxy 能处理加密协议 |
| DP-AC-08 | PCF 容灾决策（回落本地PCC/会话失败/DNN粒度混合） | 决定访问限制策略的可靠性、容灾能力 |

> **★ DP-AC-03 是访问限制场景的核心决策点**：它通过 `sets_value_pattern RULE.POLICYTYPE` 体现"动作轨道双轨道+五子轨"机制，是本场景区别于计费（固定 CHARGING）和带宽控制（动态 BWM/PCC/QOS/ADC）的标志性架构。

---

## 7. ★ 与计费 / 带宽控制场景的差异（三场景对比表）

| 维度 | 计费场景 | 带宽控制场景 | 访问限制场景 |
|------|---------|------------|------------|
| **共享根对象** | BD-CH-01=业务感知 | BD-BW-01=业务感知 | BD-AC-01=业务感知（三场景同根） |
| **ConfigurationSolution 数量** | 7 | 7 | **9（三场景最多，按动作类型×轨道×触发维度分）** |
| **核心机制** | SA识别→Rule→PCC/URR计费链→Ga/Gy/N40上报→配额闭环 | SA识别→BWM限速→CAR/Shaping/FUP/GBR | **SA识别→双轨动作（PCC隐式/URL过滤显式）→DISCARD/HEADEN/REDIRECT/PERMIT** |
| **独有特性族** | 计费三件套（URR/URRGROUP/PCCPOLICYGRP）、融合计费 | BWM 三级控制体系（用户级/组级/全局级） | **重定向族（SMARTHTTPREDIR/DNSOVERWRITING/IPFarm）、头增强族（HEADEN）、URL过滤（CFTEMPLATE/CONTCATEGBIND/ICAP*）、接入控制（USRLOCATION/SAR/ODB）** |
| **独有 ConfigObject** | URRGRPBINDING, DIAMCONNGRP, DCCTEMPLATE, CCT, CHARGECHAR 等 10 个 | BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE 等 9 个 | **23 个独有**：HEADEN + SMARTREDIRECT族3（SMARTHTTPREDIR/REDIRAPPENDINFO/DNSOVERWRITING）+ WEBPROXY/Portal族5（IPFARMGLOBAL/IPFARM/IPFARMSERVER/LOGICINF/BLACKLISTRULE）+ URL过滤轨道10（VPNINST/ICAPSERVER/ICAPLOCALINFO/ICAPSVRGRP/ICAPSVRBINDISG/CFPROFILE/CFTEMPLATE/CONTCATEGROUP/CONTCATEGBIND + 绑定3）+ 接入控制2（USRLOCATION/USRLOCATIONGRP）+ 辅助3（EXTENDEDFILTER/ERRORCODE/WELLKNOWNPORT） |
| **★ POLICYTYPE 语义** | CHARGING（固定单值） | BWM/PCC/QOS/ADC（4策略类型分支） | **★ PCC/SMARTREDIRECT/HEADEN/WEBPROXY/ADC（5子轨）+ 轨道 B CFTEMPLATE.ACTION（BLOCK/PERMIT/REDIRECT 显式）——双轨道+五子轨架构最丰富** |
| **Feature 数量** | 14（UDG 9 + UNC 5） | 24（UDG 16 + UNC 8） | **19（UDG 11 + UNC 8：UNC 位置触发 1 + UNC 接入控制辅助 4 + 三场景共享 3；★ P5 批次 1 补 4 UNC 辅助特性 U-H-02）** |
| **License 数量** | 11（4 无需 License） | 24（全部需 License） | **15（UDG 12 + UNC 3，全部需 License；4 个 UNC 接入控制辅助特性无独立 License）** |
| **DecisionPoint 数量** | 8 | 8 | **8（业务层 DP-AC-01~08，含★双轨道核心 DP-AC-03）+ 任务层 3（owner_layer=task 区分，详见 03 §6）** |
| **BusinessRule 数量** | 16 | 6 | **10（含★双轨道+五子轨 BR-AC-07、PERMIT 唯一性 BR-AC-10）** |
| **SemanticObject 数量** | 12（含协议栈 2） | 8（无协议栈） | **7（无协议栈，含动作轨道 SO-AC-07；与带宽一致无独立协议层，但有 ICAP 外部协议）** |
| **ConfigTask 数量** | 27（generic 8 + 独有 19） | 32（generic 8 + 独有 24） | **17（generic 8 复用 + 独有 9：轨道A 7 + 轨道B 1 + UNC侧 1）** |
| **MMLCommand 数量** | 87（UDG 41 + UNC 46） | 55（UDG 30 + UNC 25） | **68（UDG 48 含 PCC 规则与策略 6 + UNC 20，★ P5 修正 U-H-04）** |
| **ConfigObject 数量** | 55 | 29 | **41（共享 18 + 独有 23）** |
| **CommandRule 数量** | 14 | 5 | **14** |
| **Evidence 数量** | 32（含协议知识） | 59（24 特性 + 32 主题） | **35（19 特性 EV-FK-AC 含 4 UNC 辅助 + 8 主题 + 2 跨分析 + 4 附录D + 2 场景清单；★ P5 批次 2/3 修正）** |
| **跨层边数量** | ~130 | ~149 | **~190（三场景最多，因双轨道+五子轨路径分支多；★ P5 批次 3 修正）** |
| **共享 generic Task** | T-001~T-008 | T-001~T-008（T-008=SA特征库） | **T-001~T-008（T-008=SA特征库，与带宽相同；三场景可合并为同一 generic 节点）** |
| **PERMIT 支持** | 不适用（计费无放行概念） | 不显式支持 | **仅轨道 B 显式支持 PERMIT（CR-AC-06，URL 过滤独有）** |

> **★ 三场景对比核心结论**：
> 1. **访问限制的★双轨道+五子轨 POLICYTYPE 架构**是区别于计费（单轨 CHARGING）和带宽（四策略类型 BWM/PCC/QOS/ADC）的**标志性特征**。
> 2. 三场景共享 `业务感知` 根对象（BD-AC-01=BD-CH-01=BD-BW-01）和 8 个 generic Task（T-001~T-008）以及 18 个通用 ConfigObject（RULE/USERPROFILE/RULEBINDING/USRPROFGROUP/UPBINDUPG/APNUSRPROFG/PCCPOLICYGRP + FLOWFILTER族6 + URR/URRGROUP + ADCPARA + CATEGORYPROP）。
> 3. 独有部分通过编号段隔离（T-AC-101~109）天然无冲突，可无缝合并。
> 4. URR 跨场景复用但语义不同：计费用于差异化费率，带宽用于 FUP 阈值监控，**访问限制用于 ADC/Portal/WebProxy/URL 过滤的计费属性绑定（非主用途）**。

---

## 8. 文档索引

| 文件 | 内容 | 关键统计 | 对应Schema章节 |
|------|------|---------|---------------|
| `00-overview.md` | 本文件：五层导航 + 对象计数 + 双轨道+五子轨链路 + 三场景对比 | 约 438 对象 + 190 跨层边 | — |
| `01-business-graph.md` | 第1层：BD/NS/CS/DP/BR/SO 实例化 | BD(1) + NS(1) + CS(9) + DP(8) + BR(10) + SO(7) + Scope(5) + Participant(8) = 49 | §8.1-8.12 |
| `02-feature-graph.md` | 第2层：19 Feature + 15 License + 8 FeatureRule + depends_on/FTOE | Feature(19, ★ P5 批次 1 U-H-02) + License(15) + FeatureRule(8) + depends_on(21) + FTOE(25) = 67 + 69 关系边 | §9.3-9.8 |
| `03-task-layer.md` | 第3层：17 ConfigTask + 8 TaskRule + 3 任务层DP + 59 TCOE | ConfigTask(17: generic8+独有9) + TaskRule(8) + 任务层DP(3, owner_layer=task) + TCOE(59) = 60 + 59 边 | §10.1-10.6 |
| `04-command-graph.md` | 第4层：68 MMLCommand + 41 ConfigObject + 14 CommandRule + 双轨道+五子轨 ConfigObject 链 | MMLCommand(68, ★ P5 U-H-04) + ConfigObject(41) + CommandRule(14) + 对象关系(39) + operates_on(65) = ~227 | §11.1-11.7 |
| `05-cross-layer-mapping.md` | 第5层：跨层映射关系总表 + 端到端链路验证（4+1 覆盖双轨道+五子轨） | uses_feature(30) + uses_task(9) + decomposes_to(19) + invokes(~68) + targets(~45) + selects(9) + sets_value_pattern(6) + refined_by(8) = ~190 | §12.1-12.5 + §13 |
| `06-evidence-index.md` | 第6层：证据层索引（双层命名：主ID + 别名） | EV-FK-AC(19, ★ P5 批次 3) + EV-TK-AC(8) + EV-CA-AC(2) + EV-CA-D(4) + EV-BS-AC(2) = 35 EvidenceSource | §8.11 |

---

## 9. 合规检查清单

### 9.1 Schema 合规

- [x] 所有对象类型严格匹配 Schema §8-§12 定义
- [x] 所有关系边严格匹配 Schema §8.12/§9.8/§10.6/§11.7/§12 定义
- [x] 无 Schema §13 列出的禁止关系（CS→ConfigObject 直接绑定、Feature→MMLCommand 直接绑定、BR→CommandParameter 直接写死等，详见 `05` §9 七项核查全部通过）
- [x] 所有对象包含 `source_evidence_ids` 字段

### 9.2 端到端链路完整性（★覆盖双轨道+五子轨）

- [x] 路径 A（轨道 A-PCC 阻塞）：BD→NS→CS-AC-01→GWFD-020357→T-AC-101/T-003→ADD RULE(POLICYTYPE=PCC)→RULE
- [x] 路径 B（★轨道 B-2 URL 过滤）：BD→NS→CS-AC-06→GWFD-110471→T-AC-108→ADD CFTEMPLATE/CONTCATEGBIND→CFTEMPLATE/CONTCATEGBIND
- [x] 路径 C（★轨道 C SMARTREDIRECT）：BD→NS→CS-AC-03→GWFD-110284→T-AC-103→ADD SMARTHTTPREDIR→SMARTHTTPREDIR
- [x] 路径 D（★轨道 D HEADEN）：BD→NS→CS-AC-02→GWFD-110261→T-AC-102→ADD HEADEN→HEADEN
- [x] 补充路径（★轨道 B-1 WebProxy）：BD→NS→CS-AC-05→GWFD-110282→T-AC-106→ADD RULE(POLICYTYPE=WEBPROXY)→IPFARM

### 9.3 ★ 四轨 ConfigObject 链完整度（命令层 §9.1 核查）

- [x] 轨道 A（PCC 体系）：FILTER→FLOWFILTER→RULE(POLICYTYPE=PCC)→PCCPOLICYGRP→URRGROUP→URR ✅ 完整
- [x] 轨道 A（ADC 子轨）：FILTER→FLOWFILTER→RULE(POLICYTYPE=ADC)→ADCPARA ✅ 完整
- [x] 轨道 D（HEADEN）：FILTER→FLOWFILTER→RULE(POLICYTYPE=HEADEN)→HEADEN（含ANTIFRAUD/GRAYLIST）✅ 完整
- [x] 轨道 C（SMARTREDIRECT）：EXTENDEDFILTER+ERRORCODE→SMARTHTTPREDIR/DNSOVERWRITING←RULE(POLICYTYPE=SMARTREDIRECT) ✅ 完整
- [x] 轨道 B-1（WEBPROXY/Portal）：FILTER→FLOWFILTER→RULE(POLICYTYPE=WEBPROXY)→IPFARM→IPFARMSERVER ✅ 完整
- [x] 轨道 B-2（URL 过滤）：ICAP链+CFTEMPLATE/CONTCATEGBIND.ACTION（独立动作）✅ 完整
- [x] 接入控制触发：USRLOCATION→USRLOCATIONGRP→UPBINDUPG→USRPROFGROUP→APNUSRPROFG ✅ 完整

### 9.4 证据可追溯

- [x] 每个图谱对象的 `source_evidence_ids` 指向真实存在的知识文档
- [x] 证据索引覆盖 19 EV-FK-AC + 8 EV-TK-AC + 2 EV-CA-AC + 4 EV-CA-D + 2 EV-BS-AC = 35 份（★ P5 批次 2 补 EV-CA-D1~D4、批次 3 补 EV-FK-AC-16~19）
- [x] 核心方案 CS-AC-01~09 至少引用 1 份 direct 证据 + 1 份 supporting 证据
- [x] 所有 Feature 对象引用对应 EV-FK-AC-*（19 特性全覆盖，含 4 UNC 辅助特性 EV-FK-AC-16~19）
- [x] **引用一致性核查通过**：被引用 33 个 EV ID ⊆ 已注册 35 个 EV ID，别名全覆盖（`06` §6.2 核查结论）
- [x] **★ 命名异类已修复**：P5 批次 2 全局统一 `04` 的 `EV-FK-AC-XXXXXX`（特性编号别名，14 个）+ `EV-FK-AC-CFA` + `EV-CA-01` 简写为序号主形式，`06` §0.1/§0.3 别名表保留为向后兼容说明
- [x] 证据可追溯链路完整（图谱对象→本索引→知识文档→原始产品文档）

### 9.5 跨层一致性验证

- [x] 所有 CS 的 uses_feature 指向真实存在的 Feature（19 个：UDG 11 + UNC 8，含 4 个 UNC 接入控制辅助特性 U-H-02 补全）
- [x] 所有 Feature 的 decomposes_to 指向真实存在的 ConfigTask（17 个：8 generic + 9 独有）
- [x] 所有 ConfigTask 的 invokes 指向真实存在的 MMLCommand（68 个：UDG 48 含 PCC 规则策略 6 + UNC 20，★ P5 修正）
- [x] 所有 MMLCommand 的 operates_on 指向真实存在的 ConfigObject（41 个：共享 18 + 独有 23）
- [x] 所有 ConfigTask 的 targets 指向真实存在的 SemanticObject（7 个）或 ConfigObject
- [x] 所有 DP 的 selects 指向真实存在的 CS（9 个）或 Task（17 个）
- [x] **★ generic Task 三场景共享**：T-001~T-008 与计费/带宽场景编号相同、语义相同，三场景合并时可合并为同一 generic 节点
- [x] **★ DP-AC-03 动作轨道选择的 sets_value_pattern 体现 RULE.POLICYTYPE 双轨道+五子轨机制**
- [x] 无 §13 禁止关系

---

## 10. 图谱使用场景

本图谱可支撑以下下游应用：

| 应用场景 | 使用方式 |
|---------|---------|
| **配置生成** | 给定业务需求 → 定位 CS → 遍历 uses_task → 按 FTOE/TCOE 顺序生成 MML 命令序列（★双轨道+五子轨分别生成不同动作对象链） |
| **影响分析** | 给定特性变更（如 GWFD-110401 头防欺诈）→ 反查 uses_feature 的 CS → 评估影响范围（含强耦合 License 双开） |
| **故障诊断** | 给定命令失败 → 查 CommandRule（CR-AC-02/04/05 等）→ 回溯 ConfigTask → 定位 Feature/CS（★区分轨道 A/B 故障） |
| **方案推荐** | 给定业务目标（如"加密协议场景重定向"）→ 遍历 DP 决策点 → 推荐唯一可行的 WebProxy（轨道 B-1，BR-AC-09） |
| **License 规划** | 给定目标特性集 → 聚合 requires_license → 输出 License 清单（★注意头防欺诈+头增强双开、ADC+SA-Basic+PCC 三件套） |
| **★ 双轨道+五子轨动作路由** | 通过 DP-AC-03 动作轨道选择 → sets_value_pattern RULE.POLICYTYPE → 自动路由到不同 Task/ConfigObject 体系（轨道 A vs B） |
| **访问控制架构理解** | 通过 SO-AC-01~07 语义对象 → 理解 DISCARD/HEADEN/REDIRECT/PERMIT 四种动作 + 动作轨道五子轨 |
| **加密协议适配** | 通过 BR-AC-09 + CR-AC-10 → 快速识别 HTTPS/HTTP2.0 场景下唯一可行的 WebProxy / HTTPS头增强 / URL过滤 SNI |
| **三场景融合** | 共享 BD 根 + generic Task + 通用 ConfigObject → 计费+带宽+访问限制三场景叠加配置（类型独立原则，一条报文可同时命中 PCC阻塞+BWM限速+HEADEN插头） |
| **知识问答** | 给定问题 → 通过图谱对象关系导航 → 返回结构化答案 |

---

## 11. 后续演进

| 演进方向 | 说明 |
|---------|------|
| **★ P5 统一命名** | 统一 `04-command-graph.md` 的 `EV-FK-AC-XXXXXX` 特性编号别名到主形式 `EV-FK-AC-NN`（可选优化项，非阻塞；当前通过 `06` §0.1 别名表桥接） |
| **P5 审查修复** | 按 P5 计划对 01~06 进行批量审查，修复细节问题（如个别字段的证据强度等级补全、个别关系的双向核查等） |
| **与计费/带宽场景融合** | 共享 BD 根对象，通过 BD-level 的 contains NS 边连接三场景；generic Task 加场景前缀（T-CH-001/T-BW-001/T-AC-001）避免节点重复，但语义可直接合并；独有 Task 通过编号段隔离天然无冲突 |
| **三场景叠加配置生成** | 基于三场景 CS 闭包 + Task 链，自动生成端到端 MML 命令脚本（含类型独立原则叠加：一条报文可同时命中三场景动作） |
| **图数据库落地** | Schema 定义的对象/边可直接映射为 Neo4j/JanusGraph 的 Node/Edge（★双轨道+五子轨 POLICYTYPE 可作为关键索引属性） |
| **算子层接入** | 在图谱之上构建服务层算子，按§10使用场景封装查询 API（★双轨道+五子轨路由 API、加密协议适配 API、强耦合 License 检查 API） |
| **跨场景冲突检测** | 基于三场景 ConflictPair 设计，自动检测跨场景 RULENAME 冲突、POLICYTYPE 冲突、FlowFilter 复用冲突 |

---

> 本总览文件是访问限制场景三层图谱的入口文档。阅读顺序建议：**先读本文件理解全局（★重点关注双轨道+五子轨架构与三场景差异）→ 按需深入各层文件 → 通过 `06-evidence-index.md` 回溯证据**。
>
> **核心架构一句话**：访问限制场景三层图谱以 **RULE.POLICYTYPE 双轨道+五子轨架构**（ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY 五子轨 + URL 过滤 CFTEMPLATE.ACTION 独立轨道 B）为动作路由核心，通过 DP-AC-03 的 sets_value_pattern 显式表达，是三场景中动作类型最丰富、配置对象体系最多元、跨层路径分支最多的图谱。
