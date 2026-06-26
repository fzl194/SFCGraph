# APN 业务域三层图谱 · 总览（00-overview）

> **文件定位**：`three-layer-graph/00-overview.md`
> **作用**：五层架构导航、对象计数统计、端到端链路示例、文档索引、合规检查、后续演进
> **配套Schema**：`三层图谱Schema-最终版-v0.1.md`
> **配套本体**：`三层图谱本体标准定义.md`、`三层图谱对象与关系设计.md`
> **Stage**：Stage 4 Wave 4（Stage 4 最后一文件，6+1=7 文件全集闭环）

---

## 1. 一句话定位

APN 业务域三层图谱是**面向 5G/4G 核心网"接入与会话管理"**的领域知识图谱，以"业务→特性→任务→命令"四层对象 + 跨层映射 + 证据层为骨架，把分散在 UDG（用户面 UPF/PGW-U，16 特性）与 UNC（控制面 SMF/PGW-C/SGSN/MME/AMF，21 特性）共 37 个特性、45 份源知识资产（含 2 份业务底座）中的配置知识，组织成可追溯、可推理、可复用的结构化资产。

> **★ 独立性核心**：APN 业务域是**独立 BusinessDomain**（`BD-APN-01 接入与会话管理`），非"业务感知"（BD-CH-01 / BD-BW-01）的子场景。APN 解决"UE 如何进入网络、如何获得地址、如何接入目标 DN"，业务感知解决"会话内流量做策略/计费"。两域通过 PDU 会话上下文（SO-APN-SESSION-CONTEXT）协同，但根对象不重叠。

---

## 2. 五层架构总览

```
┌─────────────────────────────────────────────────────────────────────┐
│  第1层 业务图谱 BusinessGraph                                        │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ BD-APN-01 接入与会话管理 → NS-APN-01 APN 开通场景             │  │
│  │                              ↓                                │  │
│  │     CS(9 配置方案闭包：工控/IoT/宽带/VoLTE/AAA/DHCP/L2TP/区域/双栈)│
│  │                              ↓                                │  │
│  │     DP(12) ←→ BR(16) ←→ SO(12)  语义对象                     │  │
│  │     Scope(4) + Participant(7)                                 │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ uses_feature(35) / uses_task(9) / has_decision(12)       │
├─────────────────────────────────────────────────────────────────────┤
│  第2层 特性图谱 FeatureGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Feature(37: UDG16+UNC21) ──depends_on(35)──→ Feature          │  │
│  │     │                                                         │  │
│  │     ├─ requires_license(15) ──→ License(13)                   │  │
│  │     ├─ constrained_by(9) ──→ FeatureRule(9)                   │  │
│  │     ├─ decomposes_to(35) ──→ ConfigTask (跨层边)              │  │
│  │     └─ task_order(36) ──→ FeatureTaskOrderEdge                │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ decomposes_to / task_order                              │
├─────────────────────────────────────────────────────────────────────┤
│  第3层 任务原子层 TaskLayer                                          │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ ConfigTask(61: generic 3 + feature_specific 58)               │  │
│  │     │                                                         │  │
│  │     ├─ constrained_by(13) ──→ TaskRule(13)                    │  │
│  │     ├─ invokes(183) ──→ MMLCommand (跨层边，零悬挂零未映射)   │  │
│  │     ├─ targets(61) ──→ SO / ConfigObject (跨层边)             │  │
│  │     └─ orchestrates(30) ──→ TaskCommandOrderEdge              │  │
│  └───────────────────────────────────────────────────────────────┘  │
│           ↓ invokes                                                 │
├─────────────────────────────────────────────────────────────────────┤
│  第4层 命令图谱 CommandGraph                                         │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ MMLCommand(142: UDG 63 + UNC 79)                              │  │
│  │     │                                                         │  │
│  │     ├─ operates_on(102) ──→ ConfigObject(~65)                 │  │
│  │     │                         ├─ contains(22) ──→ ConfigObject│  │
│  │     │                         ├─ refers_to(16)                │  │
│  │     │                         ├─ depends_on(9)                │  │
│  │     │                         ├─ conflicts_with(3)            │  │
│  │     │                         ├─ activates(4)                 │  │
│  │     │                         └─ composed_by(1)               │  │
│  │     └─ governed_by ←── CommandRule(18)                        │  │
│  └───────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────┤
│  第5层 跨层映射 CrossLayerMapping                                    │
│  CS↔Feature(35) + CS↔Task(9) + Feature↔Task(35) + Task↔Cmd(183)     │
│  + Task↔SO/Obj(61) + SO↔Feature(12) + SO↔Task(12)                  │
│  + DP↔selects(12) + DP↔sets_value_pattern(7) + DP↔scope(4)         │
│  + FeatureRule↔Task(9) + refined_by(16: BR→FR 4 + BR→TR 7 + TR→CR 5)│
│  跨层边总计：~240（不含 orchestrates）；含 orchestrates ~296        │
├─────────────────────────────────────────────────────────────────────┤
│  第6层 证据层 EvidenceLayer                                          │
│  EvidenceSource(45) ←── source_evidence_ids ── 所有图谱对象         │
│  含 37 EV-FK + 4 EV-TK + 2 EV-CA + 2 EV-BS = 45 份                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. 对象计数统计（★ 与 01-06 各层严格一致）

### 3.1 各层对象总数

| 层级 | 对象类型 | 数量 | 文件 |
|------|---------|------|------|
| **第1层 业务图谱** | BusinessDomain (BD) | 1（BD-APN-01） | `01-business-graph.md` |
| | NetworkScenario (NS) | 1（NS-APN-01） | |
| | ConfigurationSolution (CS) | 9（CS-APN-01~09） | |
| | DecisionPoint (DP) | 12 | |
| | BusinessRule (BR) | 16 | |
| | SemanticObject (SO) | 12（无协议栈，含底座签约/网元类） | |
| | Scope（子对象） | 4（subscriber / subscription / access / location） | |
| | Participant（子对象） | 7（UE / UNC-SMF / UDG-UPF / UDM-HSS / Radius-DNAAA / DHCP / 隧道网关+SGSN-MME-AMF） | |
| | **业务层小计（核心）** | **51**（BD 1 + NS 1 + CS 9 + DP 12 + BR 16 + SO 12） | |
| | （业务层含子对象） | （51 + 4 Scope + 7 Participant = 62） | |
| **第2层 特性图谱** | Feature | 37（UDG 16 + UNC 21） | `02-feature-graph.md` |
| | License | 13（UDG 7 + UNC 6，含 2 双 License） | |
| | FeatureRule | 9（FR-APN-01~09） | |
| | depends_on 边 | 35（会话底座 10 + IPv6 串联 8 + 鉴权级联 5 + 接入控制 3 + 网元选择 2 + 隧道 3 + C-U 协同 4） | |
| | requires_license 边 | 15（13 Feature，双 License 计 2 条边） | |
| | FeatureTaskOrderEdge（FTOE） | 36（FTOE-APN-001~036，6 个核心 Feature） | |
| | **特性层小计** | **37 + 13 + 9 + 36 = 95**（不含边） | |
| **第3层 任务原子层** | ConfigTask（generic） | 3（T-001/006/007：VPN 准备/REFRESHSRV/LICENSE） | `03-task-layer.md` |
| | ConfigTask（feature_specific） | 58（地址 4 + 双栈 9 + L2TP-U 8 + Radius 10 + UPF 6 + 接入控制 5 + 隧道 8 + 其他 8） | |
| | ConfigTask 合计 | **61**（T-001~708） | |
| | TaskRule | 13（TR-APN-01~13） | |
| | TaskCommandOrderEdge | 30（Task 内部 24 + 跨 Task 上下文 6） | |
| | **任务层小计** | **61 + 13 + 30 = 104** | |
| **第4层 命令图谱** | MMLCommand | 142（UDG 63 + UNC 79） | `04-command-graph.md` |
| | ConfigObject | ~65（去重，含 ★推导 3 个 MPLS） | |
| | CommandRule | 18（CR-APN-01~18） | |
| | ConfigObject 关系边 | 55（contains 22 + refers_to 16 + depends_on 9 + conflicts_with 3 + activates 4 + composed_by 1） | |
| | operates_on 边 | 102（UDG 43 + UNC 59；REFRESHSRV 动作命令无 ConfigObject） | |
| | governed_by 边 | 18（CR-APN-01~18 各治理若干命令/参数/对象） | |
| | **命令层小计** | **142 + 65 + 18 = ~225**（不含边）/ 含边 ~280 | |
| **第5层 跨层映射** | 跨层边 | **~240**（不含 orchestrates） | `05-cross-layer-mapping.md` |
| **第6层 证据层** | EvidenceSource | 45（37 EV-FK + 4 EV-TK + 2 EV-CA + 2 EV-BS） | `06-evidence-index.md` |
| **图谱对象总计** | — | **~828**（核心对象：51 + 95 + 104 + 225 + 45 = 520；加跨层边 ~240 + 命令层 operates_on/关系/governed_by 边 175 = ~935；按"对象+边"全量约 800~900）| — |

> **★ 计数口径**：
> - **核心对象**（不含任何边）：BD/NS/CS/DP/BR/SO 51 + Feature/License/FeatureRule 59 + ConfigTask/TaskRule 74 + MMLCommand/ConfigObject/CommandRule 225 + EvidenceSource 45 = **454**
> - **核心对象 + 顺序结构边**（FTOE + TaskCommandOrderEdge）：454 + 36 + 30 = **520**
> - **含全量边**（含跨层 ~240 + 命令层 operates_on 102 + ConfigObject 关系 55 + governed_by 18 + 特性层 depends_on 35 + requires_license 15）：**~935**

### 3.2 关键关系边总数

| 关系类型 | 数量 | 所在文件 |
|---------|------|---------|
| BD contains NS | 1 | `01-business-graph.md` |
| NS instantiated_as CS | 9 | `01-business-graph.md` |
| CS uses_feature | 35（9 方案 × 平均 3.9 特性） | `05-cross-layer-mapping.md` |
| CS uses_task（闭包级） | 9 | `05-cross-layer-mapping.md` |
| NS/CS has_decision（DP 归属） | 12（全归 NS-APN-01） | `01-business-graph.md` |
| CS constrained_by BR | ~22（含场景级 + 方案特化） | `01-business-graph.md` |
| NS/CS uses_semantic_object | ~21 | `01-business-graph.md` |
| DP selects Feature/Task/Command/Parameter | 12 | `05-cross-layer-mapping.md` |
| DP sets_value_pattern | 7 | `05-cross-layer-mapping.md` |
| DP conditioned_by_scope | 4 | `05-cross-layer-mapping.md` |
| Feature depends_on Feature | 35 | `02-feature-graph.md` |
| Feature requires_license License | 15 | `02-feature-graph.md` |
| Feature constrained_by FeatureRule | 9 | `02-feature-graph.md` |
| Feature decomposes_to ConfigTask | 35（37 Feature，2 纯描述性底座除外） | `05-cross-layer-mapping.md` |
| Feature task_order（FTOE） | 36 | `02-feature-graph.md` |
| FeatureRule constrains_task | 9 | `05-cross-layer-mapping.md` |
| SO realized_by Feature | 12 | `05-cross-layer-mapping.md` |
| SO realized_by Task | 12 | `05-cross-layer-mapping.md` |
| ConfigTask constrained_by TaskRule | 61 → 13 | `03-task-layer.md` |
| ConfigTask invokes MMLCommand | 183 | `05-cross-layer-mapping.md` |
| ConfigTask targets SO/ConfigObject | 61 | `03-task-layer.md` |
| ConfigTask orchestrates TaskCommandOrderEdge | 30 | `03-task-layer.md` |
| ConfigTask may_require_feature | 58 | `03-task-layer.md` |
| ConfigObject contains/refers_to/depends_on/conflicts_with/activates/composed_by | 55 | `04-command-graph.md` |
| MMLCommand operates_on ConfigObject | 102 | `04-command-graph.md` |
| MMLCommand governed_by CommandRule | 18 | `04-command-graph.md` |
| BR/TR/CR refined_by（BR→FR/TR + TR→CR） | 16 | `05-cross-layer-mapping.md` |
| 图谱对象 source_evidence_ids | 全对象覆盖 | `06-evidence-index.md` |

---

## 4. 九大方案闭包表（第1层核心，CS-APN-01~09）

| 方案ID | 方案名称 | 地址分配 | 鉴权 | 接入 | 地址类型 | 主特性 |
|--------|---------|---------|------|------|---------|--------|
| CS-APN-01 | **工厂工控访问内网方案** | UDM 静态签约（Framed-IP） | NON_TRANS（企业 Radius） | IPSec 隧道 | IPv4 单栈 | WSFD-010502, WSFD-011305, IPFD-015004/016000 |
| CS-APN-02 | **智慧农业传感器上报方案** | UPF-APN/DNN 动态（POOLTYPE=LOCAL） | TRANS_NON_AUTH（透明免鉴权） | NAT 直连 | IPv4 单栈 | GWFD-010105, GWFD-010101, WSFD-010501 |
| CS-APN-03 | **家庭 CPE 宽带方案** | UPF-SMF 动态 | TRANS_NON_AUTH | NAT 直连 | IPv4v6 双栈（LKV3G5VDSA01） | GWFD-010105, GWFD-020403, WSFD-010504 |
| CS-APN-04 | **VoLTE 语音业务方案** | SMF 本地动态 | TRANS_NON_AUTH | 直连（IMS 精确寻址） | IPv4v6 双栈 | WSFD-010502, WSFD-010504, WSFD-104002, GWFD-020403 |
| CS-APN-05 | **企业 AAA 二次鉴权方案** | Radius 下发（Framed-Pool） | NON_TRANS（Radius 级联链 011306→011305→108007） | GRE 隧道（可选）/ 直连 | IPv4 单栈 | WSFD-011305/011306, WSFD-108007/011307, IPFD-015002 |
| CS-APN-06 | **传统企业 DHCP 迁移方案** | DHCP 代理（UNC 转发外部 DHCP Server） | TRANS_NON_AUTH | 直连 | IPv4 单栈 | WSFD-104413, WSFD-010501, GWFD-010101 |
| CS-APN-07 | **企业 L2TP VPN 方案** | LNS 分配（IPCP+RA+IPv6CP，C 决策 U 执行） | NON_TRANS（企业 Radius） | L2TP 隧道 | IPv4v6 双栈（LKV3G5L2TP01 仅 U 侧） | GWFD-020412, WSFD-104410, GWFD-020403 |
| CS-APN-08 | **区域化运营管理方案** | UPF-LOCATION 动态（LAC/TAC→POOLGRPMAP） | TRANS_NON_AUTH | 直连 | IPv4 单栈（LKV3G5LBAA01） | GWFD-020421, GWFD-010105, WSFD-010501 |
| CS-APN-09 | **企业双栈加密接入方案** | UPF-APN/DNN 动态（双 SECTION） | TRANS_NON_AUTH | IPSec 隧道（IPv6 支持 v02 20.8.0+） | IPv4v6 双栈（LKV3G5VDSA01） | GWFD-010105, GWFD-020403, IPFD-015004/016000, WSFD-104002 |

> **★ 9 方案由 4 开通主线维度组合**：地址分配方式 × 鉴权方式 × 接入方式 × 地址类型，每方案是稳定组合 + 主特性集合 + 强约束 BR。
> **★ 与计费/带宽 7 方案差异**：APN 按"业务场景"划分 9 方案，另两场景按"控制/计费机制"划分 7 方案。

---

## 5. 端到端链路示例（三层贯通，来自 05-cross-layer-mapping §7）

### 5.1 链路 A：CS-APN-01 工厂工控访问内网（UDM 静态签约 + IPSec）

```
[业务] BD-APN-01 接入与会话管理
  → NS-APN-01 APN 开通场景
    → CS-APN-01 工厂工控访问内网方案
      → DP-APN-ADDR-MODE 选择"UDM 静态签约"（POOLTYPE=UDM）
      → DP-APN-AUTH-MODE 选择"NON_TRANS 非透明接入"
      → DP-APN-ACCESS-MODE 选择"IPSec 隧道"
      → DP-APN-ADDR-TYPE 选择"IPv4 单栈"
      → BR-APN-RADIUS-CASCADE（Radius 级联强依赖链）
      → BR-APN-GRE-IPSEC-SRC-EXCL（GRE/IPSec 源地址互斥）
      → BR-APN-SECOND-AUTH-PROTO（二次鉴权协议限制）
      → SO-APN-ADDRESS-POOL, SO-APN-AUTH-AAA, SO-APN-TUNNEL, SO-APN-SUBSCRIPTION

[特性] CS-APN-01 uses_feature（6）
  → WSFD-010502 地址分配(C)（UDM 静态签约决策）
  → WSFD-011305 Radius 鉴权接入（NON_TRANS）
  → WSFD-011306 Radius 功能（级联链起点）
  → IPFD-015004 IPSec(UDG)（对称同构）
  → IPFD-016000 IPSec(UNC)（对称同构）
  → WSFD-010301 鉴权功能(AKA)（底层鉴权）

[任务] Feature decomposes_to
  → WSFD-011306 decomposes_to T-301~304,307（Radius 服务器组+绑定+刷新）
  → WSFD-011305 decomposes_to T-305~307（APN 鉴权属性 ACCESSMODE=NON_TRANS）
  → IPFD-015004/016000 decomposes_to T-602~608（IPSec 7 步链）
  → WSFD-010301 decomposes_to T-310（AKA 2/3/4/5G 鉴权）

[命令] T-305 invokes → SET APNAUTHATTR（CMD-UNC-037）
  → operates_on → OBJ-APNAUTHATTR（ACCESSMODE=NON_TRANS）
  → impacted_by → DP-APN-AUTH-MODE sets_value_pattern
T-607 invokes → ADD IPSECPOLICY（CMD-UDG-052）
  → operates_on → OBJ-IPSECPOLICY（聚合 ACL+Proposal+IKE Peer）
  → constrained_by → CR-APN-10（DH 组不能 None）
  → constrained_by → CR-APN-12（GRE 源地址 ≠ IPSec 源地址）

[证据] CS-APN-01 → [EV-TK-01, EV-CA-02, EV-FK-12, EV-FK-24, EV-FK-30]
  WSFD-011305 → [EV-FK-24, EV-CA-01]
  ADD IPSECPOLICY → [EV-FK-30, EV-CA-01]
```

### 5.2 链路 B：CS-APN-07 企业 L2TP VPN（★ C 决策 U 执行典型）

```
[业务] BD-APN-01 → NS-APN-01 → CS-APN-07 企业 L2TP VPN 方案
  → DP-APN-ADDR-MODE 选择"LNS(L2TP) 分配"（C 决策 U 执行）
  → DP-APN-ACCESS-MODE 选择"L2TP 隧道"
  → DP-APN-ADDR-TYPE 选择"IPv4v6 双栈"（LNS IPCP+RA+IPv6CP）
  → BR-APN-L2TP-CU-ASYM（C-U License 不对称，仅 U 侧 LKV3G5L2TP01）
  → BR-APN-LOC-L2TP-EXCL（位置↔L2TP 互斥）
  → BR-APN-L2TP-ADDRAUTO-EXCL（L2TP↔地址检测互斥）
  → BR-APN-DUALSTACK-NEED-LICENSE（双栈 License）
  → SO-APN-TUNNEL（C 决策 U 执行）, SO-APN-ADDRESS-POOL（LNS 远程）, SO-APN-AUTH-AAA

[特性] CS-APN-07 uses_feature（5）
  → GWFD-020412 L2TP VPN(U, LAC)（U 面 LAC 执行，License LKV3G5L2TP01）
  → WSFD-104410 L2TP VPN(C, 决策)（C 面决策，无 License）
  → WSFD-011305/011306 Radius 鉴权链
  → GWFD-020403 IPv4v6 双栈(U)（能力使能层）

[任务] Feature decomposes_to（★ C 决策 U 执行不对称典型）
  [U 侧] GWFD-020412 decomposes_to T-201~208（FTOE-APN-016~022，8 步）
    → T-201 SET LICENSESWITCH(LKV3G5L2TP01)（★仅 U 侧）
    → T-203 SET APNL2TPATTR（★U 面核心 10+ 参数）
    → T-206 SET L2TPN4KEY（★U 侧 N4 加密）
    → T-208 SET REFRESHSRV（must_be_last）
  [C 侧] WSFD-104410 decomposes_to T-706
    → T-706 SET APNL2TPCTRL（★C 面仅 2 参数 APN/L2TPSWITCH）
    → T-706 SET L2TPKEY（★与 U 侧 L2TPN4KEY 须相同）
    → T-706 SET PFCPPVTEXT（下发 LNS 参数经 N4）

[命令] T-203 invokes → SET APNL2TPATTR（CMD-UDG-065）
  → operates_on → OBJ-APNL2TPATTR（10+ 参数）
  → constrained_by → CR-APN-02（U 10+ vs C 2 参数不对称）
T-706 invokes → SET APNL2TPCTRL（CMD-UNC-064）
  → operates_on → OBJ-APNL2TPCTRL（2 参数）
  → constrained_by → CR-APN-02（参数集不对称）
  → constrained_by → CR-APN-03（U+C 密钥必须相同）
  → refined_by → TR-APN-05 → BR-APN-L2TP-CU-ASYM

[证据] CS-APN-07 → [EV-TK-01, EV-CA-02, EV-FK-11, EV-FK-14, EV-FK-16]
  SET APNL2TPATTR → [EV-FK-11, EV-CA-01]
  SET APNL2TPCTRL → [EV-FK-14, EV-CA-01]
```

### 5.3 链路 C：CS-APN-09 企业双栈加密接入（双栈 + IPSec 叠加）

```
[业务] BD-APN-01 → NS-APN-01 → CS-APN-09 企业双栈加密接入方案
  → DP-APN-ADDR-MODE 选择"UPF-APN/DNN 动态"
  → DP-APN-ADDR-TYPE 选择"IPv4v6 双栈"（License LKV3G5VDSA01）
  → DP-APN-ACCESS-MODE 选择"IPSec 隧道"（IPv6 支持 v02 20.8.0+）
  → BR-APN-DUALSTACK-NEED-LICENSE（双栈 License）
  → BR-APN-IPV6-CASCADE（IPv6 承载强依赖链 V6PB01→VDSA01→P6PD01）
  → BR-APN-GRE-IPSEC-SRC-EXCL（GRE/IPSec 源地址互斥）
  → SO-APN-ADDRESS-POOL（双栈地址池）, SO-APN-TUNNEL（IPSec）, SO-APN-SESSION-CONTEXT

[特性] CS-APN-09 uses_feature（5）
  → GWFD-010105 用户面地址分配（POOLTYPE=LOCAL 双池）
  → GWFD-020403 IPv4v6 双栈(U)（能力使能层，LKV3G5VDSA01）
  → IPFD-015004 IPSec(UDG) + IPFD-016000 IPSec(UNC)（对称同构）
  → WSFD-104002 IPv4v6 双栈(C)（UNC 侧）

[任务] Feature decomposes_to
  → GWFD-020403 decomposes_to T-101~109（FTOE-APN-007~015，9 步双栈链）
    → T-101 双 License 使能（V6PB01+VDSA01）
    → T-102 VPN 双实例（IPv4+IPv6 地址族激活）
    → T-103 ADD APN（HASVPN+HASVPNIPV6 双 VPN 绑定）★
    → T-104 双池双段（IPv4 POOL + IPv6 POOL）
    → T-105 双池绑定同组（双优先级算法）
    → T-108 下行路由发布（OSPF+OSPFv3 双进程）
    → T-109 RA 通告（020403 独有）
  → IPFD-015004/016000 decomposes_to T-602~608（IPSec 7 步链）

[命令] T-103 invokes → ADD APN（CMD-UDG-001）
  → operates_on → OBJ-APN-U（HASVPN, VPNINSTANCE, HASVPNIPV6, VPNINSTANCEIPV6）
  → constrained_by → CR-APN-06（IPv6 需 AFTYPE=ipv6uni）
  → impacted_by → DP-APN-ADDR-TYPE sets_value_pattern（双栈）
T-607 invokes → ADD IPSECPOLICY
  → operates_on → OBJ-IPSECPOLICY（聚合 ACL+Proposal+IKE Peer）
  → constrained_by → CR-APN-10（DH 组不能 None）

[证据] CS-APN-09 → [EV-TK-01, EV-CA-02, EV-FK-06, EV-FK-16, EV-FK-30]
  ADD APN → [EV-FK-06, EV-CA-01]
  ADD IPSECPOLICY → [EV-FK-30, EV-CA-01]
```

---

## 6. 关键决策点（12 DP 摘要）

| 决策点 | 决策问题 | 影响 |
|--------|---------|------|
| DP-APN-ADDR-MODE | 地址分配方式（UDM 静态 / UPF-APN 动态 / UPF-LOCATION / UPF-SMF / SMF 本地 / Radius / DHCP / LNS） | 决定 POOLTYPE（LOCAL/UDM/SMF/EXTERNAL）、ALLOCPRECEDENCE、C-U 决策执行分离模式 |
| DP-APN-ADDR-GRANULARITY | 地址分配粒度（APN × LOC × SMF 三维度组合） | 决定三级优先级规则（SET IPALLOCRULE / SET APNIPALLOCRULE）与 POOLGRPMAP 映射 |
| DP-APN-ADDR-TYPE | 地址类型（IPv4 / IPv6 / IPv4v6 双栈） | 决定 SECTION 配置（V4STARTIP/V6PREFIXSTART）、License 触发（IPv6→LKV3G5V6PB01；双栈→LKV3G5VDSA01；PD→LKV3G5P6PD01） |
| DP-APN-AUTH-MODE | 鉴权方式（TRANS_NON_AUTH / TRANS_AUTH / NON_TRANS / LOC_AUTH） | 决定是否调用 AAA（仅 TRANS_AUTH/NON_TRANS 强依赖 Radius）、账密来源 |
| DP-APN-ACCESS-MODE | 接入方式（直连 / NAT / IPSec / GRE / MPLS-VPN / L2TP / GRE-over-IPSec） | 决定隧道封装、C-U 协同模式（对称同构 vs C 决策 U 执行）、License 触发 |
| DP-APN-UPF-SELECT | UPF 选择三轮（必选→优选→权重/负载） | 决定 UPF NF Profile 匹配维度，选定结果直接决定地址分配执行侧 |
| DP-APN-PEER-NF-SELECT | 对等网元 DNS 域名聚合（LAI/RAI/TAI/ZONE） | 决定 AREDNS 配置（DNTYPE + LAC/RAC/TAC RANGE + ZONENAME） |
| DP-APN-ACCESS-PERMISSION | 用户接入权限判定（C 面） | 决定 ARD 记录查询路径（AMF 本地 NGMMSUBDATA vs SGSN/MME GBARD/IUARD/S1ARD） |
| DP-APN-BANDWIDTH-CTRL | U 面带宽流控方式（CAR 丢弃 / Shaping 整形 × 上下行） | 决定 APNQOSATTR 配置（CARSHAPESWUL/DL）；与 C 面接入权限机制完全不同 |
| DP-APN-CONCURRENCY | 多 PDN/PDU 并发允许（EPC ≤11；5GC ≤15） | 决定 APNACTNUM 查询与拒绝原因值 55 |
| DP-APN-ALIAS-APN | 别名 APN 映射（协商 APN→别名 vs 别名→真实 APN） | 决定 ALIASAPNMAP 双向映射查询（两套网元映射方向相反） |
| DP-APN-SECOND-AUTH | DN 二次鉴权（允许/拒绝） | 决定经 UPF N4 GTP-U 隧道转接 DN-AAA 的路径；仅 PAP/CHAP via Radius |

---

## 7. 与计费/带宽场景的差异（★ 三维对比）

| 维度 | 计费场景 | 带宽控制场景 | APN 业务域（本图谱） |
|------|---------|------------|---------------------|
| **BusinessDomain** | `业务感知`（BD-CH-01） | `业务感知`（BD-BW-01） | `接入与会话管理`（**BD-APN-01，★ 独立**） |
| **独立性** | 共享"业务感知"根 | 共享"业务感知"根 | **独立根，与业务感知并列**；通过 SO-APN-SESSION-CONTEXT 协同 |
| **NetworkScenario** | NS-CH-01 计费场景 | NS-BW-01 带宽控制场景 | NS-APN-01 APN 开通场景 |
| **ConfigurationSolution** | 7（按计费方式/计量/兜底分） | 7（按控制机制分） | **9（按业务场景 4 维度组合分）** |
| **核心机制** | SA→Rule→PCC/URR→上报→配额 | SA→BWM→CAR/Shaping/FUP/GBR | **4 维度决策（地址×鉴权×接入×类型）+ 3 底座（会话×网元×权限）** |
| **topic 划分维度** | 按计费/控制机制分批 | 按控制机制分批 | **★ 按意图澄清维度（4 开通主线）划分**，非机械分批 |
| **ConfigurationSolution 数** | 7 | 7 | **9** |
| **DecisionPoint** | 8 | 8 | **12** |
| **BusinessRule** | 16 | 6 | **16** |
| **SemanticObject** | 12（含协议栈 2） | 8（无协议栈） | **12（无协议栈，含底座签约/网元类）** |
| **Feature 总数** | 14（UDG 9 + UNC 5） | 24（UDG 16 + UNC 8） | **37（UDG 16 + UNC 21）** |
| **License 数** | 11（含 4 无需） | 24（全部需） | **13（24 个无需 License）** |
| **独有特性族** | 计费三件套 + 融合计费 | BWM 三级控制体系 | **会话管理底座（纯描述性 5）+ 地址分配 6×3 正交矩阵 + 4 隧道 + IPv6 承载 License 串联链 + Radius 三件套级联** |
| **配置树修正项** | 协议知识完整入图（1422 行） | — | **★ 11 处修正**：双栈能力使能层单向 / C 决策 U 执行 / 非 C-U 对称 / 会话底座纯描述性 / 双特性合一（106003, 107010）/ 双视角反转（106203 别名 APN）/ MPLS 文档缺口 / Radius 声明矛盾修正 / 位置↔L2TP 互斥 / L2TP↔地址检测互斥 / GRE↔IPSec 源地址互斥 |
| **★ C-U 协同模式** | — | — | **★ 4 模式**：①决策执行分离 5（UNC 决策→UDG 执行）②对称同构 4（同命令族，如 GRE/IPSec）③C 决策 U 执行 1（L2TP 典型）④非对称（同名不同义，GWFD-010151 vs WSFD-106003） |
| **APN 域独有 ConfigObject** | — | — | **APNL2TPATTR（U,10+）, APNL2TPCTRL（C,2）, L2TPN4KEY/L2TPKEY, NGMMSUBDATA, GBARD/IUARD/S1ARD, ALIASAPN/APNALIAS, APNACTNUM, AREADNS, PNFPROFILE, RDSSVRGRP/UPLIST4RDS/UPFRDSSVR/UPFRDSCLIENTIP, DHCPBINDPOOLGRP, STATICADDRPARA** 等 |
| **共享 ConfigObject** | RULE, USERPROFILE, PCCPOLICYGRP, FLOWFILTER, URR, URRGROUP | 同左 | **无共享 URR/PCC**（APN 域不依赖 PCC/SA 体系）；共享 ADD APN（跨域共用挂载点）、SET APNADDRESSATTR（U+C 共用命令名）、ADD SECTION（U+C 同命令） |
| **独有协议知识** | Ga/Gy/DCC/N40/PFCP/Gx（6 协议，1422 行） | 无 | 无独立协议层 SemanticObject（协议交互通过 C-U PFCP/N4 体现） |
| **MMLCommand** | 87（UDG 41 + UNC 46） | 55（UDG 30 + UNC 25） | **142（UDG 63 + UNC 79）** |
| **ConfigObject** | 55 | 29 | **~65** |
| **CommandRule** | 14 | 5 | **18** |
| **ConfigTask** | 27 | 32 | **61** |
| **TaskRule** | 6 | 6 | **13** |
| **TaskCommandOrderEdge** | 20 | 16 | **30** |
| **FeatureTaskOrderEdge** | 25 | 25 | **36** |
| **跨层边总计** | ~130 | ~149 | **~240** |
| **EvidenceSource** | 32（含 2 协议知识） | 59 | **45（含 2 业务底座）** |
| **端到端验证路径数** | 6 | 3 | **3（CS-APN-01/07/09）** |
| **核心不对称** | — | — | ★POOL(UDG) vs ADDRPOOL(UNC)、APNL2TPATTR(U,10+) vs APNL2TPCTRL(C,2)、L2TPN4KEY(U) vs L2TPKEY(C) |

> **对比结论**：APN 业务域图谱对象规模最大（Feature 37、ConfigTask 61、MMLCommand 140、跨层边 ~235 均为三场景之最），因其覆盖接入与会话管理全链路。配置树修正项（11 处）和 C-U 协同 4 模式是 APN 域的核心特征，也是 Stage 5 审查重点。

---

## 8. 文档索引（00-06 对应 Schema §8-§13 章节）

| 文件 | 内容 | 关键统计 | 对应 Schema 章节 |
|------|------|---------|---------------|
| `00-overview.md` | 本文件：五层导航 + 对象计数 + 9 方案闭包 + 3 端到端链路 + 12 DP + 三维差异 + 文档索引 + 合规检查 + 后续演进 | — | — |
| `01-business-graph.md` | 第1层：BD/NS/CS/DP/BR/SO 实例化 | BD(1) + NS(1) + CS(9) + DP(12) + BR(16) + SO(12) + Scope(4) + Participant(7) = **62** | §8.1-8.12 |
| `02-feature-graph.md` | 第2层：37 Feature + 13 License + 9 FeatureRule + depends_on + FTOE | Feature(37) + License(13) + FeatureRule(9) + depends_on(35) + requires_license(15) + FTOE(36) = **95（不含边）/ 146（含边）** | §9.3-9.8 |
| `03-task-layer.md` | 第3层：61 ConfigTask + 13 TaskRule + 30 TCOE | ConfigTask(61: generic 3 + specific 58) + TaskRule(13) + TCOE(30) = **104** | §10.1-10.6 |
| `04-command-graph.md` | 第4层：142 MMLCommand + ~65 ConfigObject + 18 CommandRule | MMLCommand(142) + ConfigObject(~65) + CommandRule(18) + ConfigObject 关系边(55) + operates_on(102) + governed_by(18) = **~225（不含边）/ ~300（含边）** | §11.1-11.7 |
| `05-cross-layer-mapping.md` | 第5层：跨层映射关系总表 + 3 端到端链路验证 + 合规清单 | uses_feature(35) + uses_task(9) + decomposes_to(35) + invokes(183) + targets(61) + SO realized_by(24) + DP selects/sets/conditioned(23) + refined_by(16) = **~240** | §12.1-12.5 |
| `06-evidence-index.md` | 第6层：证据层索引 | EV-FK(37) + EV-TK(4) + EV-CA(2) + EV-BS(2) = **45 EvidenceSource** | §8.11 EvidenceSource |

---

## 9. 合规检查清单

### 9.1 Schema §13 禁止关系合规

- [x] **无 CS→ConfigObject 直接绑定**：9 方案 uses_feature 终点全部为 Feature（WSFD-/GWFD-/IPFD- 前缀）
- [x] **无 CS→MMLCommand 直接绑定**：方案到命令经 Feature→ConfigTask→MMLCommand 三跳
- [x] **无 Feature→MMLCommand 直接绑定**：Feature 到命令经 ConfigTask 一跳（decomposes_to）
- [x] **无 Feature→ConfigObject 直接绑定**：Feature 到对象经 ConfigTask（targets）一跳
- [x] **无 Task→Feature 反向绑定**：Task 经 may_require_feature 单向引用 Feature
- [x] **无 ConfigObject→MMLCommand 反向绑定**：operates_on 单向 MMLCommand→ConfigObject

### 9.2 Schema §9.3 Feature 字段完整性

- [x] **`variant_dimensions` 全 Feature 覆盖**：37 Feature 均含 ≥2 维度（代际/产品/地址类型/角色/C-U 模式等）
- [x] **`applicable_nf_map` JSON 格式**：37 Feature 均含 `{"UDG": [...]}` / `{"UNC": [...]}` / 双产品 JSON
- [x] **`constrained_by`（FeatureRule）非 `has_rule`**：9 FeatureRule 经 `constrained_by` 关系引用，字段名为 `constrained_by`
- [x] **`governed_by`（CommandRule）反向**：18 CommandRule 经 MMLCommand.governed_by 反向引用（CR governs → CMD）

### 9.3 证据可追溯

- [x] **每图谱对象 `source_evidence_ids` 指向真实证据**：全部对象引用 `EV-{TYPE}-{NN}` 格式 ID
- [x] **EV ID 编号格式统一**：`EV-FK-01~37` / `EV-TK-01~04` / `EV-CA-01~02` / `EV-BS-01~02`，严格按 `apn-feature-doc-list.md` 顺序
- [x] **证据索引覆盖**：45 份 EvidenceSource 全部登记（37 EV-FK + 4 EV-TK + 2 EV-CA + 2 EV-BS）
- [x] **source_evidence_ids 全对象覆盖**：BD/NS/CS/DP/BR/SO + 37 Feature + 13 License + 61 ConfigTask + 142 MMLCommand + ~65 ConfigObject 全部含 source_evidence_ids
- [x] **核心方案 CS-APN-01~09 至少引用 1 direct + 1 supporting 证据**：每方案均含 EV-TK-01（direct，Batch-14 业务场景方案）+ EV-CA-02 + 若干 EV-FK-NN
- [x] **证据可追溯链路完整**：图谱对象 → 本索引 → 知识文档 → 原始产品文档

### 9.4 端到端链路完整性（★ 至少 3 条）

- [x] **路径 A（CS-APN-01 工厂工控）**：BD-APN-01 → NS-APN-01 → CS-APN-01 → WSFD-011305 → T-305 → SET APNAUTHATTR → OBJ-APNAUTHATTR ✓
- [x] **路径 B（CS-APN-07 L2TP，C 决策 U 执行）**：BD-APN-01 → NS-APN-01 → CS-APN-07 → GWFD-020412/WSFD-104410 → T-203/706 → SET APNL2TPATTR/CTRL → OBJ-APNL2TPATTR/CTRL ✓
- [x] **路径 C（CS-APN-09 双栈加密）**：BD-APN-01 → NS-APN-01 → CS-APN-09 → GWFD-020403 → T-103 → ADD APN → OBJ-APN-U ✓

### 9.5 跨层一致性验证

- [x] 所有 CS 的 uses_feature 指向真实存在的 Feature（37 个）
- [x] 所有 Feature 的 decomposes_to 指向真实存在的 ConfigTask（61 个，2 纯描述性底座除外）
- [x] 所有 ConfigTask 的 invokes 指向真实存在的 MMLCommand（142 个）
- [x] 所有 MMLCommand 的 operates_on 指向真实存在的 ConfigObject（~65 个）
- [x] 所有 ConfigTask 的 targets 指向真实存在的 SemanticObject（12 个）或 ConfigObject
- [x] 所有 DP 的 selects 指向真实存在的 CS/Feature/Task/Command（已核对无悬挂引用，见 `05` §11）
- [x] **跨层边无悬挂引用**（`05-cross-layer-mapping.md` §11 已逐项核对）

### 9.6 跨场景独立性验证

- [x] APN 域 Task 纯数字编号（T-xxx，批次5去APN前缀对齐访问限制graph_parser）与带宽 T-101~T-603、计费 T-101~T-311 在各自文件独立解析不冲突
- [x] APN 域 CS-APN-xx 与计费 CS-CH-xx、带宽 CS-BW-xx 不重叠
- [x] APN 域 BR-APN-xx 与计费 BR-CH-xx、带宽 BR-BW-xx 不重叠
- [x] APN 域无共享 URR/PCC/SA 特性（与计费/带宽独立底座）
- [x] APN 域 generic Task 自定义（T-001/006/007），不复用带宽 T-001~T-008

---

## 10. 已知问题 → Stage 5 审查预告

| 已知问题 | 所在层 | 严重度 | Stage 5 处理方向 |
|---------|--------|--------|-----------------|
| **CR-APN-07 consistency_rule 映射 semantic_rule** | 第4层 CommandRule | warning | CR-APN-07（VPN-POOL 一致性）当前归 validation_rule，Stage 5 评估是否拆为独立 semantic_rule 类型（Schema §11.6 未列 semantic_rule 枚举，可能保持 validation） |
| **MPLS VPN 命令推导**（CMD-UDG-062/063/064） | 第4层 MMLCommand | warning | 9 篇 MPLS 文档无完整 MML 脚本，ConfigTask T-703 status=draft；需命令字典补全 VPNINSTANCE/BGPVPNV4ROUTETARGET/BGPVPNV4PEER 系列 |
| **UPF 选择文档缺口** | 第2层 Feature WSFD-107010 | info | 三轮筛选 7 必选条件部分参数（如 PNFUPFINFO 详细字段）文档未完整列出，依赖配置实例推导 |
| **DHCP 完整激活脚本缺口** | 第2层 Feature WSFD-104413 | info | cross-topic §8.4 标注；CS-APN-06 已注明 Stage 5 不作阻断 |
| **别名 APN 双视角拆分**（WSFD-106203） | 第2层 Feature + FR-APN-08 | info | variant_dimensions 第 1 维度"网元视角"区分两个变体，Stage 5 评估是否物理拆分为两个 Feature ID（Schema §9.1 建议逻辑分离） |
| **接入控制双特性合一**（WSFD-106003 子特性 A/B） | 第2层 Feature + FR-APN-03 | info | variant_dimensions 第 2 维度"子特性"区分 A/B，Stage 5 评估是否物理拆分 |
| **8 对依赖声明矛盾修正** | 第2层 depends_on | info | cross-feature-analysis §4.1-§4.3 已修正建模（如 WSFD-104002 强依赖 WSFD-104001 的"不涉及"声明被忽略），Stage 5 验证修正一致性 |
| **配置树 11 处修正项验证** | 全图谱 | info | 双栈能力使能层单向 / C 决策 U 执行 / 非 C-U 对称 / 会话底座纯描述性 / 双特性合一 / 双视角反转 / MPLS 缺口 / Radius 声明矛盾 / 3 互斥（位置-L2TP/L2TP-地址检测/GRE-IPSec 源地址），Stage 5 逐项核对落图完整性 |

---

## 11. 后续演进

| 演进方向 | 说明 |
|---------|------|
| **图数据库落地** | Schema §8-§12 定义的对象/边可直接映射为 Neo4j/JanusGraph 的 Node/Edge；APN 域对象规模最大（~800），需分批导入（按 feature_group 分批：地址分配 / 双栈 / 隧道 / 鉴权 / 网元 / 接入控制） |
| **算子层接入** | 在图谱之上构建服务层算子：①方案推荐（给业务目标→遍历 DP→推荐 CS）②配置生成（CS→遍历 uses_task→生成 MML 脚本）③影响分析（Feature 变更→反查 CS）④License 清单（特性集→聚合 requires_license） |
| **配置生成自动化** | 基于 CS-APN-01~09 闭包 + Task 链，自动生成端到端 MML 命令脚本；6 个核心 Feature 的 FTOE（36 条）已锁定顺序，可直接作为脚本骨架 |
| **与访问限制场景协同** | 套餐 3（访问限制：URL 过滤/重定向/阻塞）图谱独立构建后，与 APN 域共享 PDU 会话上下文（SO-APN-SESSION-CONTEXT），形成"接入-会话-访问控制"全景 |
| **三场景融合** | 计费（BD-CH-01）+ 带宽（BD-BW-01）+ APN（BD-APN-01）三域通过 PDU 会话上下文 + ADD APN（跨域共用挂载点）协同；通用 ConfigObject（RULE/USERPROFILE）经 PCC 桥接，APN 域作为接入入口承载计费/带宽策略落地 |
| **5G SA 演进** | 当前图谱覆盖 2G/3G/4G/5G 全代际；5G SA 独立组网场景下，S-NSSAI 切片选择、DNN 数据网络、DNAI 边缘计算等 5G 原生维度需在 DP-APN-UPF-SELECT 和 DP-APN-ADDR-MODE 中增强 |

---

## 12. 图谱使用场景

本图谱可支撑以下下游应用：

| 应用场景 | 使用方式 |
|---------|---------|
| **APN 开通配置生成** | 给定业务需求（如"工厂工控固定 IP+IPSec"）→ 定位 CS-APN-01 → 遍历 uses_task → 生成 IPSec+Radius+UDM 静态签约 MML 脚本 |
| **企业接入方案推荐** | 给定企业目标（如"远程办公 L2TP"）→ 遍历 DP-APN-ACCESS-MODE → 推荐 CS-APN-07 → 输出 C 决策 U 执行配置蓝图 |
| **License 规划** | 给定目标特性集（如双栈+IPSec+L2TP）→ 聚合 requires_license → 输出 License 清单（LKV3G5VDSA01 + LKV3G5L2TP01 等） |
| **故障诊断** | 给定命令失败（如 SET APNL2TPATTR 失败）→ 查 CR-APN-02 → 回溯 T-203 → 定位 GWFD-020412 → CS-APN-07 |
| **影响分析** | 给定特性变更（如 GWFD-010105 升级）→ 反查 uses_feature 的 CS（CS-APN-02/03/05/08/09）→ 评估影响范围 |
| **C-U 协同设计** | 通过 4 模式（决策执行分离/对称同构/C 决策 U 执行/非对称）→ 理解 POOL vs ADDRPOOL、APNL2TPATTR vs APNL2TPCTRL 等 C-U 不对称 |
| **接入与会话管理架构理解** | 通过 SO-APN-SESSION-CONTEXT / SO-APN-ADDRESS-POOL / SO-APN-AUTH-AAA / SO-APN-TUNNEL 等 12 语义对象 → 理解 APN 域端到端机制 |
| **知识问答** | 给定问题（如"L2TP 为什么 C 侧无 License"）→ 通过图谱关系导航 BR-APN-L2TP-CU-ASYM → 返回结构化答案 |

---

> 本总览文件是 APN 业务域三层图谱的入口文档。阅读顺序建议：
> 1. **先读本文件**理解全局（五层架构 + 对象计数 + 9 方案闭包 + 3 端到端链路）
> 2. **按需深入各层**（01 业务图谱 → 02 特性图谱 → 03 任务层 → 04 命令图谱 → 05 跨层映射）
> 3. **通过 06 证据索引回溯**原始知识文档（45 份 EvidenceSource 注册表）
>
> **Stage 4 闭环 / Stage 5 收尾**：00-06 共 7 文件已全部完成，图谱对象总计约 **800~900**（核心对象 454 + 顺序结构边 66 + 跨层/命令/特性边 ~385）。Stage 5 批次 5 收尾：SET REFRESHSRV 5 处 Task→CMD 边全部对象化（CMD-UDG-088 / CMD-UNC-087），**命令对象化率 100%（零悬挂、零未映射）**，invokes 边从 178 上调至 183，MMLCommand 从 140 上调至 142。Stage 5 后续审查聚焦：① Schema §13 合规 ②配置树 11 处修正项落图完整性 ③跨层一致性无悬挂引用 ④证据可追溯链路 ⑤剩余已知问题（MPLS 推导/UPF 选择缺口等）闭环。
