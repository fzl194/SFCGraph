# 网元对接业务域 — UPF网元对接三层图谱构建设计

> 日期：2026-06-29
> 业务域：网元对接（Network Element Docking / 开局基础设施对接）
> 子场景：UPF网元对接
> 标杆参考：计费场景（`业务图谱体系/计费场景/`，完整，93%合规）
> 权威定义：`业务图谱体系/` 下三层图谱Schema v0.1 + 本体标准定义 + 对象与关系设计 + 构建SOP

---

## 1. 背景与目标

### 1.1 背景
业务图谱体系已有4个业务域：计费（完整）、带宽控制（完整）、访问限制（完整）、APN接入与会话管理（构建中）。本次扩展第5个业务域 **网元对接**，首个子场景 **UPF网元对接**。

### 1.2 目标
将 UDG 产品 "初始配置与调测" 文档集合，构建为符合三层图谱Schema v0.1的知识图谱，回答：
- **业务上**：UPF网元开局要打通哪些对接面、各对接面选什么组网方案、有哪些决策分支
- **能力上**：各对接方案由哪些特性（引用）支撑、有哪些可复用配置任务
- **命令上**：每个任务最终落到哪些MML命令、配置对象、参数

### 1.3 原始文档（★权威源，记录完整初始配置流程）
`output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/`（~60个md，6大子主题）。
**该目录本身即完整初始配置流程**，是主题知识的主线权威源，亦是第3层端到端配置链路的来源。

---

## 2. 对接类场景的特殊性（★与计费/带宽的本质差异）

| 维度 | 计费/带宽/访问限制（业务功能域） | **网元对接（基础设施对接域）** |
|------|------|------|
| 配置性质 | 网元**内部业务功能**（开局后配业务策略） | 网元**开局基础设施对接**（打通连通性） |
| 图谱驱动力 | **特性驱动**（特性是图谱主体） | **流程/方案驱动**（特性退为引用支撑） |
| 主链 | BD→NS→CS→**Feature(主体)**→Task→Command | BD→NS→**CS对接方案(主体)**→Feature(引用)→Task→Command |
| 命令风格 | ADD URR/ADD RULE（业务策略） | SET OMIP/ADD L3VPNINST/ADD OSPF/ADD BGPPEER/ADD APN（开局路由/接口） |
| 特性来源 | 特性是组织单位，逐特性建6板块知识 | 特性是**被引用**的，反查FeatureGraph，精简建知识 |
| 文档组织 | 按特性+业务专题 | 按**初始配置流程**（了解架构→License→基础数据→网管对接→组网对接→组网路由→调测） |

> **核心结论**：网元对接图谱的"主角"是**对接方案闭包(CS)与组网模式决策点(DP)**，特性是配角（引用支撑）。

---

## 3. 业务域定位

| 本体对象 | 取值 | 说明 |
|---------|------|------|
| BusinessDomain (BD) | `网元对接` | 开局基础设施对接域，独立于业务感知/接入与会话管理 |
| NetworkScenario (NS) | `UPF网元对接` | UDG扮演 UPF/PGW-U/SGW-U 融合角色，与周边网元对接 |

**UPF网元对接的对接关系**（来自Explore通读）：
- **N4**：UPF ↔ SMF/PGW-C/SGW-C（控制面，PFCP，唯一必须接口）
- **N3**：UPF ↔ gNodeB（用户面上行）
- **N9a/N9c**：UPF ↔ UPF（用户面级联）
- **N6**：PSA UPF ↔ DN（数据网络，外联口物理接口）
- 4G互操作：S1-U/S5/S8/Gn-U/Gp-U 等

---

## 4. 文档范围与特性来源

### 4.1 文档范围（直接用给定目录，不扫描全库）
6大子主题：
1. **了解组网架构/**（3 md）：5G/4G互操作架构、VNF与外部网络互通、逻辑接口（Saif/Scif/Paif/N4if）
2. **License申请与加载/**（4 md）
3. **基础数据配置/**（4 md）：网元基本信息、NTP、高危命令二次授权、公共参数
4. **配置网元和网管对接**（1 md）：网管适配层、北向对接、SNMPv3、TLS
5. **组网对接配置/**（会话接入+业务接口 N4/N3/N9/N6）
6. **组网路由配置/**（静态/OSPF/BGP/MPLS VPN/GRE/IPsec × IPv4/IPv6 × NP卡/加速卡/SDN/非SDN × 自动/手动）
+ 典型配置实例/、调测验证/

### 4.2 引用特性清单（17个，从文档抽取 → 反查特性库）

| 前缀 | 含义 | 唯一数 | 特性ID（按出现频次） |
|------|------|--------|---------------------|
| **IPFD** | IP转发/路由特性 | 10 | 012003(57)、014002(46)、014000(32)、012000(20)、014003(18)、014001(18)、015004(6)、010001(6)、010000(2)、104403(3) |
| **GWFD** | 网关功能特性 | 5 | 010234(10)、020411(5)、020421(4)、010105(4)、020161(3) |
| **NPFD** | 网络处理器转发 | 2 | 010000、010014 |

**反查路径**：
- GWFD（5个）→ `FeatureGraph/data/UDG/20.15.2/features.jsonl`（可直接反查，含依赖/License）
- IPFD/NPFD（12个）→ ⚠️ **待验证**：FeatureGraph主要收录GWFD/WSFD，IPFD/NPFD可能未收录，需另查原始特性目录或标注"未在FeatureGraph收录"

> 特性知识文档**精简**（场景角色为主）：仅写"本对接场景下的角色 + depends_on + License + 关联命令/配置对象"，不强制完整6板块。

---

## 5. 三层图谱对象落位设计

### 5.1 第1层 业务图谱（★主体层）

**ConfigurationSolution（方案闭包，按对接面组织）**：

| CS | 对接面 | 核心内容 | 主要文档 |
|----|--------|---------|---------|
| CS-1 | 控制面对接 | N4(PFCP) ↔ SMF/PGW-C/SGW-C | 组网对接配置/配置N4接口数据 |
| CS-2 | 用户面对接 | N3↔gNB / N9↔UPF / N6↔DN + 会话接入(APN/DNN/地址池) | 组网对接配置/配置业务接口数据 + 配置会话接入数据 |
| CS-3 | 网管对接 | UDG↔MAE/U2020（适配层/SNMPv3/TLS） | 配置网元和网管对接 |
| CS-4 | 路由对接 | VNF侧IP路由（★最大，含全部组网模式分支） | 组网路由配置/ + 典型配置实例/ |
| CS-5 | 基础就绪 | License加载 + 基础数据(NTP/网元信息/高危命令/公共参数) + MTU | License申请与加载/ + 基础数据配置/ + 修改MTU值 |

**DecisionPoint（决策点，组网模式分支，主要挂在CS-4路由对接下）**：
- 硬件：NP卡直连PE / 网络加速卡直连DC-GW / 无NP卡
- 组网形态：SDN / 非SDN
- IP版本：IPv4 / IPv6 / IPv4v6双栈
- 路由协议：静态路由+BFD / OSPF(OSPFv3) / BGP over OSPF / BGP MPLS VPN / GRE隧道 / IPsec
- 部署方式：自动部署(推荐) / 手动部署

**BusinessRule / SemanticObject**：
- SO（语义桥梁）：抽象接口(Saif/Scif/Paif/N4if)、VPN实例、路由协议(OSPF/BGP)、地址池/地址段、BFD会话、隧道(GRE/MPLS/IPsec)
- BR：组网互通原则、路由发布规则、N4必须先于业务面、自动部署优先等

### 5.2 第2层 特性图谱（引用支撑层）
- 17个Feature节点（IPFD路由类为主），反查特性库
- depends_on 边（来自 feature_relations.jsonl）
- requires_license 边（来自 feature_requires_license.jsonl）
- ⚠️ variant_dimensions / applicable_nf_map 字段按Schema §9.3必填（若FeatureGraph数据齐全则继承）

### 5.3 第3层 任务原子层（端到端流程★源自给定目录）
ConfigTask（最小可复用配置原子），编排遵循给定目录的初始配置流程：
```
基础就绪(License/基础数据) → 网管对接 → 组网对接(接口/会话接入) → 组网路由 → 调测验证(FirstCall)
```
典型Task：配置抽象接口 / 配置VPN实例 / 配置OSPF进程 / 配置BGP对等体 / 配置静态路由+BFD / 配置APN / 配置地址池 / 配置网管适配层 / 加载License / 配置NTP …

### 5.4 第4层 命令图谱
- MMLCommand：SET OMIP / SET AUTOCONFIG / SET BFD / ADD L3VPNINST / ADD VPNINST / ADD OSPF(OSPFV3) / ADD OSPFAREA / ADD BGPVRF / ADD BGPPEER / ADD APN / ADD POOL / ADD SECTION / SET IPALLOCRULE / SET NEWCERTSWITCH / LST ME …
- ConfigObject：抽象接口、VPN实例、OSPF进程/区域、BGP对等体/地址族、静态路由、BFD会话、APN/DNN、地址池/段、GRE/MPLS/IPsec隧道、网管适配层
- CommandRule：URRID类唯一性、接口必须绑定VPN、路由引入规则、对象绑定后删除前置等

### 5.5 第5/6层
- 跨层映射边：CS→Feature(uses_feature) / CS→Task(uses_task) / Feature→Task(decomposes_to) / Task→Command(invokes)
- EvidenceSource：给定目录~60个md（EV-FK-{NN}特性知识 + EV-TK-{NN}主题知识 + EV-CA跨分析 + EV-BS业务图谱）

---

## 6. 5阶段Pipeline（对接场景适配版）

| 阶段 | 标准SOP | 对接场景适配 |
|------|---------|-------------|
| **Stage1 文档筛选** | 关键词扫描全库 | ★**直接用给定目录**（不扫描全库）。产出：①对接文档清单（按6子主题×对接面）②17特性清单（标注反查状态）③主题分批计划（按对接面+初始配置流程） |
| **Stage2 知识提取** | 双轨(特性+主题) | **特性轨(轻)**：17特性反查FeatureGraph，精简建知识（场景角色为主）；**主题轨(重)**：按对接面+初始配置流程分批，忠实给定目录 |
| **Stage3 横向分析** | cross-feature + cross-topic | cross-feature（17特性共性/依赖/命令/对象）；**cross-topic★第1层数据源**（对接面方案闭包CS + 组网模式决策树DP + 端到端流程） |
| **Stage4 三层实例化** | 7文件(00-06) | CS按对接面；DP承载组网模式分支；Task编排=初始配置流程 |
| **Stage5 审查修复** | 6类审查 | 同标准，对标计费场景，目标≥90%合规 |

---

## 7. 双轨构建模式应用

### 7.1 特性轨（轻）
- 输入：17引用特性ID
- 动作：反查 `FeatureGraph/data/UDG/20.15.2/features.jsonl`（GWFD可直接查；IPFD/NPFD待验证）
- 产出：`feature-knowledge/{ID}-{name}.md`（精简版：场景角色+依赖+License+关联命令/对象）+ `cross-feature-analysis.md`

### 7.2 主题轨（重）
- 输入：给定目录~60个md
- 分批策略：按对接面（CS-1~CS-5）+ 初始配置流程顺序
- 产出：`topic-knowledge/Batch-{NN}-{对接面}.md` + `cross-topic-analysis.md`
- ★cross-topic的§6直接产出CS方案闭包和DP决策点（第1层数据源）

---

## 8. 目录结构（遵循SOP §7标准）

```
业务图谱体系/网元对接/
├── 网元对接doc-list.md              # Stage1: 对接文档清单（按6子主题×对接面）
├── 网元对接feature-doc-list.md      # Stage1: 17特性清单（含反查状态）
├── topic-batch-plan.md              # Stage1: 主题分批计划
├── feature-knowledge/               # Stage2特性轨 + Stage3 cross-feature
│   ├── {GWFD/IPFD/NPFD}-{ID}-{name}.md  # 17个（精简版）
│   └── cross-feature-analysis.md
├── topic-knowledge/                 # Stage2主题轨
│   └── Batch-{NN}-{对接面}.md
├── cross-topic-analysis.md          # Stage3 跨主题分析（★第1层数据源）
└── three-layer-graph/               # Stage4-5
    ├── 00-overview.md
    ├── 01-business-graph.md         # BD/NS/CS(对接面)/DP(组网模式)/BR/SO
    ├── 02-feature-graph.md          # 17特性(引用)+depends_on+License
    ├── 03-task-layer.md             # 开局配置Task+端到端流程
    ├── 04-command-graph.md          # MMLCommand/ConfigObject/CommandRule
    ├── 05-cross-layer-mapping.md
    ├── 06-evidence-index.md
    └── audit/
```

---

## 9. EV ID命名规范（Stage4前必统一，吸取带宽场景教训）

```
特性知识:    EV-FK-{NN}     (01~17，按特性ID排序)
主题知识:    EV-TK-{NN}     (按Batch编号)
跨特性分析:  EV-CA-01
跨主题分析:  EV-CA-02
业务图谱:    EV-BS-01
```
> 全库统一编号格式，不用语义别名（带宽场景158处修正教训）。

---

## 10. 关键Schema合规要点（吸取已有场景教训）

| 要点 | 要求 |
|------|------|
| variant_dimensions | Feature必填（Schema §9.3） |
| applicable_nf_map | JSON格式 `{"UDG":["UPF","PGW-U","SGW-U"]}` |
| constrained_by | Feature constrained_by FeatureRule |
| governed_by | MMLCommand governed_by CommandRule |
| evidence_type/status | EvidenceSource必填（Schema §8.11） |
| 禁止关系 | 无CS→ConfigObject直接绑定、Feature→MMLCommand直接绑定（Schema §13） |
| source_evidence_ids | 所有对象必填 |

---

## 11. 风险与注意事项

| # | 风险 | 应对 |
|---|------|------|
| 1 | IPFD/NPFD特性可能不在FeatureGraph | Stage1反查时验证；未收录则查原始特性目录或标注，不阻塞主体（特性是配角） |
| 2 | 对接场景特性非主体，易过度投入特性轨 | 特性轨严格精简（场景角色为主），主体精力放主题轨/对接面CS |
| 3 | 组网模式分支组合爆炸（硬件×SDN×IP×路由×部署） | 用DP决策树表达，不每种组合都建独立CS；典型组合放"典型配置实例"作证据 |
| 4 | 给定目录流程即权威 | 主题轨忠实目录流程顺序，不擅自重组 |
| 5 | 与APN域潜在重叠(UPF选择/MPLS VPN/双栈) | 本域=开局连通性对接（路由/接口命令），APN域=会话策略；按命令风格区分，不混建 |
| 6 | 最多2个并行Agent | 独立层并行(01+02)，有依赖串行(05依赖01-04) |

---

## 12. 验收标准

- [ ] 7文件三层图谱完整，CS按5个对接面组织，DP覆盖组网模式分支
- [ ] 17引用特性入库（GWFD反查FeatureGraph；IPFD/NPFD标注反查状态）
- [ ] 端到端链路≥3条验证（BD→NS→CS→Feature→Task→Command→Object）
- [ ] Schema合规率≥90%（对标计费场景）
- [ ] EV ID全库统一编号格式
- [ ] 每对象source_evidence_ids指向给定目录真实md
- [ ] Stage5审查报告 + 分批修复记录文档化

---

## 13. 下一步

本设计确认后 → 进入实现规划（writing-plans），按Stage1→5拆解可执行任务清单。
