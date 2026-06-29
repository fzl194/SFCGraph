# 00 总览 Overview — 网元对接业务域 / UPF网元对接子场景

> 三层图谱入口 | 业务域 BD-ND 网元对接 | 子场景 NS-ND-UPF UPF网元对接
> 版本 2026-06-29 | 对标计费场景标杆 | Schema v0.1

---

## 1. 业务域与场景定位

| 对象 | 标识 | 说明 |
|---|---|---|
| BusinessDomain | `BD-ND` 网元对接 | 开局基础设施对接域（云核心网网元如何接入网络、对接周边网元）。第5个业务域，独立于业务感知/带宽控制/访问限制/接入与会话管理(APN) |
| NetworkScenario | `NS-ND-UPF` UPF网元对接 | UDG 扮演 **UPF / PGW-U / SGW-U 融合角色**，与周边网元对接：**N4**(↔SMF/PGW-C/SGW-C 控制面)、**N3**(↔gNodeB)、**N9**(↔UPF)、**N6**(↔DN) |
| 典型结果 | 打通 FirstCall / 用户基本接入 | 软件安装完成 → 初始配置与调测 → 用户接入打通 |

---

## 2. ★对接类场景的特殊性（区别计费/带宽/访问限制）

| 维度 | 计费/带宽/访问限制（业务功能域） | 网元对接（基础设施对接域） |
|---|---|---|
| 配置性质 | 网元内部业务功能（开局后配业务策略） | 网元开局基础设施对接（打通连通性） |
| 图谱驱动力 | 特性驱动（特性是主体） | **流程/方案驱动**（对接方案闭包CS是主体，特性是引用支撑） |
| 主链 | BD→NS→CS→**Feature**→Task→Command | BD→NS→**CS(对接面)**→Feature(引用)→Task→Command |
| 命令风格 | ADD URR/ADD RULE（策略） | SET OMIP/ADD VPNINST/ADD OSPF/ADD BGPPEER/ADD APN（开局路由/接口） |

**主体脉络**：5个对接面 ConfigurationSolution + 组网模式 DecisionPoint（5维决策树）。17个引用特性（IPFD路由类为主）是支撑配角。

---

## 3. 各层对象计数总表

| 层 | 文件 | 对象类型 | 数量 |
|---|---|---|---|
| **第1层 业务图谱** | 01-business-graph | BusinessDomain | 1 |
| | | NetworkScenario | 1 |
| | | ConfigurationSolution（对接面） | **5**（CS-ND-01控制面/02用户面/03网管/04路由/05基础就绪） |
| | | DecisionPoint | **27**（DP-CS1~CS5，含CS4组网模式7决策点） |
| | | BusinessRule | 10 |
| | | SemanticObject | 43 |
| | | Scope/Participant 子对象 | 9 / 22（U-M-03 修正：原 19 漏计 UDM/NWDAF/OMC/FusionStage 等，按 §2.1~2.5 去重实为 22） |
| **第2层 特性图谱** | 02-feature-graph | Feature（引用支撑） | **16**（+IPFD-104403别名deprecated，归并IPFD-012003） |
| | | License | 3（LKV3G5CUFM01/MPLS01/LBAA01，均GWFD） |
| | | FeatureRule | 4 |
| | | depends_on / requires_license 边 | 4 / 3 |
| **第3层 任务原子层** | 03-task-layer | ConfigTask | **18**（T-ND-01~18，generic 10为主） |
| | | TaskRule | 16 |
| | | TaskCommandOrderEdge | 36 |
| | | FeatureTaskOrderEdge（端到端） | 15 |
| **第4层 命令图谱** | 04-command-graph | MMLCommand | **103**（6类：接口/会话接入/网管基础/路由协议/BFD隧道级联/自动部署模板 + 验证） |
| | | CommandParameter | ~50 |
| | | ConfigObject | **58** |
| | | CommandRule | 18 |
| | | ConfigObject关系边 / operates_on | 25 / 47 |
| **第5层 跨层映射** | 05-cross-layer-mapping | 跨层边汇总 + 端到端链路 | 端到端链路 3 条 |
| **第6层 证据层** | 06-evidence-index | EvidenceSource | **27**（EV-FK-17/EV-TK-7/EV-CA-2/EV-BS-1） |

**总计**：~118 业务层对象（Participant 口径修正 +3）+ 23 特性层 + 85 任务层 + ~229 命令层 + 27 证据 = **三层图谱主体 ≈482 对象/边**。

---

## 4. 三层图谱结构

```text
业务图谱(01) ── BD网元对接 → NS UPF网元对接 → CS×5对接面 → DP组网模式 / BR / SO
      │ uses_feature / uses_task
      ▼
特性图谱(02) ── Feature×16(引用) → depends_on / requires_license / FeatureRule
      │ decomposes_to
      ▼
任务原子层(03) ── ConfigTask×18 → TaskRule / TaskCommandOrderEdge / 端到端编排
      │ invokes / targets
      ▼
命令图谱(04) ── MMLCommand×103 → CommandParameter / ConfigObject×58 / CommandRule
      │
证据层(06) ──── EvidenceSource×27（EV-FK/Tk/CA/BS）→ 原始70md（output/UDG初始配置与调测/）

跨层映射(05) ── 汇总上述跨层边 + 3条端到端链路验证
```

---

## 5. 5个对接面 ConfigurationSolution

| CS | 对接面 | 核心机制 | 关键DP |
|---|---|---|---|
| CS-ND-01 | 控制面对接(N4↔SMF) | N4唯一必备接口、N4if强制合一 | 多SMF→CU Full Mesh |
| CS-ND-02 | 用户面对接(N3/N9/N6+会话接入) | 接口层(Saif/Scif/Paif)+会话接入三件套 | UPF角色→接口组合、地址分配LOCAL/EXTERNAL |
| CS-ND-03 | 网管对接 | 5步闭包、密码三元组、TLS/SNMPv3 | 网管类型×认证×协议 |
| CS-ND-04 | 路由对接(★最大) | VPN+路由协议+BFD+外联口，5层共性结构 | **组网模式5维决策树**(硬件×SDN×部署×路由×BFD) |
| CS-ND-05 | 基础就绪(开局第1步) | License+基础数据+架构认知 | License路径、架构模式 |

---

## 6. 组网模式决策树（CS-4 核心，DP-CS4-01~07）

| DP | 决策维度 | 选项 |
|---|---|---|
| DP-CS4-01 | 硬件类型 | 无NP卡标卡 / NP卡直连PE / 网络加速卡直连DC-GW(NP100级联口/NP121) |
| DP-CS4-02 | 组网架构 | 非SDN / SDN(强制BGP over静态+DHCP+单臂BFD) |
| DP-CS4-03 | 部署方式 | 自动(AUTOSCALING模板族,推荐) / 手动(逐条MML) |
| DP-CS4-04 | 路由协议×IP | OSPF/静态/BGP × IPv4/IPv6/双栈 |
| DP-CS4-05 | BFD模式 | 双向 / 单臂Echo(SDN/加速卡强制) |
| DP-CS4-06 | 外联口形态 | 子接口/主接口 × bonding/非bonding |
| DP-CS4-07 | 隧道叠加 | 无 / IPsec / GRE / MPLS VPN |

---

## 7. 端到端开局链路

```text
CS-5基础就绪(License/NTP/公共参数/MTU/二次授权)
  → CS-3网管对接(适配层/北向用户/SNMPv3/TLS)
  → CS-1控制面N4(N4if偶联,唯一必备)
  → CS-2用户面(业务接口Saif/Scif/Paif + 会话接入APN/地址池)
  → CS-4路由对接(VPN+路由协议+BFD+外联口,按组网模式DP)
  → 调测FirstCall(DSP SESSIONINFO 4参数验证)
```

3条完整端到端链路（BD→NS→CS→Feature→Task→Command→Object）见 05-cross-layer-mapping.md §6。

---

## 8. 文件导航

| 文件 | 内容 |
|---|---|
| 00-overview.md | 本文件（总览/计数/导航） |
| 01-business-graph.md | 第1层：BD/NS/CS×5/DP×27/BR×10/SO×43 |
| 02-feature-graph.md | 第2层：Feature×16(引用)/License×3/FeatureRule×4 |
| 03-task-layer.md | 第3层：ConfigTask×18/TaskRule×16/命令编排/端到端 |
| 04-command-graph.md | 第4层：MMLCommand×103/ConfigObject×58/CommandRule×18 |
| 05-cross-layer-mapping.md | 第5层：跨层边汇总 + 端到端链路验证 |
| 06-evidence-index.md | 第6层：EvidenceSource×27 + 原始70md索引 |
| audit/ | Stage5 审查报告 + 分批修复记录 |

---

## 9. 构建产物索引（场景目录）

```
业务图谱体系/网元对接/
├── 网元对接doc-list.md / 网元对接feature-doc-list.md / topic-batch-plan.md  (Stage1)
├── feature-knowledge/  17特性精简知识 + cross-feature-analysis.md(EV-CA-01)  (Stage2特性轨)
├── topic-knowledge/    Batch-01~07 主题知识  (Stage2主题轨)
├── cross-topic-analysis.md  (EV-CA-02, 第1层数据源)  (Stage3)
└── three-layer-graph/  00~06 + audit/  (Stage4-5)
```

---

## 10. Schema 合规声明

- ✅ 严格遵循 `三层图谱Schema-最终版-v0.1.md` §8-§12 字段标准
- ✅ 遵循 §13 禁止关系（CS 不直绑 ConfigObject/MMLCommand；Feature 不跳层；业务层不内建 ConfigObject）
- ✅ EV ID 全库统一（EV-FK-01~17 / EV-TK-01~07 / EV-CA-01/02 / EV-BS-01）
- ✅ Feature 含 variant_dimensions / applicable_nf_map(JSON)
- ✅ EvidenceSource 含 evidence_type/status
- ✅ 端到端链路 3 条贯通到 Object
- ⏳ Stage5 审查目标 ≥90% 合规（对标计费场景 93%）
