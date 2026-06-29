# 06-evidence-index 证据层（UPF网元对接子场景）

> Stage 4 产出 | 第6层 EvidenceSource 注册表 | 业务域=网元对接 | 子场景=UPF网元对接
> Schema 依据：`业务图谱体系/三层图谱Schema-最终版-v0.1.md` §8.11 EvidenceSource
> 跨层共享：EvidenceSource 是跨层共享本体（§4.2 / §6.5），各图谱对象 `source_evidence_ids` 指向此处的 EV ID
> 编制日期：2026-06-29

---

## 1. 概述

本文件为 UPF 网元对接子场景建立 **27 个 EvidenceSource**，统一承接知识产物（特性知识、主题知识、跨产物分析、图谱证据），所有图谱对象（BD/NS/CS/DP/BR/SO/Feature/License/Task/CMD/ConfigObject）的 `source_evidence_ids` 一律回指此处。

**EV ID 编号约定（全库一致）**：

| 段位 | 数量 | 来源类型 | 对应知识产物 |
|------|------|----------|------------|
| EV-FK-01~17 | 17 | markdown | 特性知识（feature-knowledge/，按 feature_code 字母序） |
| EV-TK-01~07 | 7 | markdown | 主题知识（topic-knowledge/Batch-01~07） |
| EV-CA-01 | 1 | markdown | cross-feature-analysis.md（feature-knowledge/） |
| EV-CA-02 | 1 | markdown | cross-topic-analysis.md（场景根目录） |
| EV-BS-01 | 1 | markdown | 业务图谱证据（设计文档 + doc-list + feature-doc-list） |

**证据流转链路**：

```
原始产品文档(70 md，§3 索引)
   ↓ 凝练
知识产物(27 EV: EV-FK×17 + EV-TK×7 + EV-CA×2 + EV-BS×1)
   ↓ supported_by
图谱对象(BD/NS/CS/Feature/Task/CMD，§4 统计)
```

---

## 2. 主注册表（27 条 EvidenceSource）

> 严格遵循 Schema §8.11 字段：`evidence_id` / `evidence_type` / `title` / `path` / `source_system` / `status`
> path 为相对路径（基准：`业务图谱体系/网元对接/`）

### 2.1 特性知识证据（EV-FK-01~17，17 条）

> 编号规则：feature_code 字母序（GWFD → IPFD → NPFD），与 `网元对接feature-doc-list.md` §特性总表一致

| evidence_id | evidence_type | title | path | source_system | status |
|-------------|---------------|-------|------|---------------|--------|
| EV-FK-01 | markdown | GWFD-010105 用户面地址分配 特性知识 | feature-knowledge/GWFD-010105-用户面地址分配.md | feature-knowledge | active |
| EV-FK-02 | markdown | GWFD-010234 Single IP 特性知识 | feature-knowledge/GWFD-010234-Single IP.md | feature-knowledge | active |
| EV-FK-03 | markdown | GWFD-020161 CU Full Mesh组网 特性知识 | feature-knowledge/GWFD-020161-CU Full Mesh组网.md | feature-knowledge | active |
| EV-FK-04 | markdown | GWFD-020411 MPLS VPN 特性知识 | feature-knowledge/GWFD-020411-MPLS VPN.md | feature-knowledge | active |
| EV-FK-05 | markdown | GWFD-020421 基于位置的地址分配 特性知识 | feature-knowledge/GWFD-020421-基于位置的地址分配.md | feature-knowledge | active |
| EV-FK-06 | markdown | IPFD-010000 接口与链路 特性知识 | feature-knowledge/IPFD-010000-接口与链路.md | feature-knowledge | active |
| EV-FK-07 | markdown | IPFD-010001 接口管理 特性知识 | feature-knowledge/IPFD-010001-接口管理.md | feature-knowledge | active |
| EV-FK-08 | markdown | IPFD-012000 IP可靠性 特性知识 | feature-knowledge/IPFD-012000-IP可靠性.md | feature-knowledge | active |
| EV-FK-09 | markdown | IPFD-012003 BFD 特性知识 | feature-knowledge/IPFD-012003-BFD.md | feature-knowledge | active |
| EV-FK-10 | markdown | IPFD-014000 路由功能 特性知识 | feature-knowledge/IPFD-014000-路由功能.md | feature-knowledge | active |
| EV-FK-11 | markdown | IPFD-014001 支持OSPF 特性知识 | feature-knowledge/IPFD-014001-支持OSPF.md | feature-knowledge | active |
| EV-FK-12 | markdown | IPFD-014002 支持BGP 特性知识 | feature-knowledge/IPFD-014002-支持BGP.md | feature-knowledge | active |
| EV-FK-13 | markdown | IPFD-014003 静态路由 特性知识 | feature-knowledge/IPFD-014003-静态路由.md | feature-knowledge | active |
| EV-FK-14 | markdown | IPFD-015004 IPSec功能 特性知识 | feature-knowledge/IPFD-015004-IPSec功能.md | feature-knowledge | active |
| EV-FK-15 | markdown | IPFD-104403 BFD (初始配置引用代号) 特性知识 | feature-knowledge/IPFD-104403-BFD (初始配置引用代号).md | feature-knowledge | active |
| EV-FK-16 | markdown | NPFD-010000 操作维护功能 特性知识 | feature-knowledge/NPFD-010000-操作维护功能.md | feature-knowledge | active |
| EV-FK-17 | markdown | NPFD-010014 支持NTP功能 特性知识 | feature-knowledge/NPFD-010014-支持NTP功能.md | feature-knowledge | active |

### 2.2 主题知识证据（EV-TK-01~07，7 条）

> 编号规则：按 Batch-01~07 顺序对应 EV-TK-01~07，对应对接面 CS-5→CS-3→CS-1→CS-2→CS-4→调测

| evidence_id | evidence_type | title | path | source_system | status |
|-------------|---------------|-------|------|---------------|--------|
| EV-TK-01 | markdown | Batch-01 CS-5架构认知与License 主题知识 | topic-knowledge/Batch-01-CS5架构认知与License.md | topic-knowledge | active |
| EV-TK-02 | markdown | Batch-02 CS-5基础数据与CS3网管对接 主题知识 | topic-knowledge/Batch-02-CS5基础数据与CS3网管对接.md | topic-knowledge | active |
| EV-TK-03 | markdown | Batch-03 CS-1控制面与CS-2用户面 主题知识 | topic-knowledge/Batch-03-CS1控制面与CS2用户面.md | topic-knowledge | active |
| EV-TK-04 | markdown | Batch-04 CS-4路由非SDN无NP卡自动 主题知识 | topic-knowledge/Batch-04-CS4路由非SDN无NP卡自动.md | topic-knowledge | active |
| EV-TK-05 | markdown | Batch-05 CS-4路由非SDN手动与加速卡 主题知识 | topic-knowledge/Batch-05-CS4路由非SDN手动与加速卡.md | topic-knowledge | active |
| EV-TK-06 | markdown | Batch-06 CS-4路由NP卡与SDN 主题知识 | topic-knowledge/Batch-06-CS4路由NP卡与SDN.md | topic-knowledge | active |
| EV-TK-07 | markdown | Batch-07 典型实例与整网调测 主题知识 | topic-knowledge/Batch-07-典型实例与整网调测.md | topic-knowledge | active |

### 2.3 跨产物分析证据（EV-CA-01/02，2 条）

| evidence_id | evidence_type | title | path | source_system | status |
|-------------|---------------|-------|------|---------------|--------|
| EV-CA-01 | markdown | cross-feature-analysis 跨特性分析 | feature-knowledge/cross-feature-analysis.md | feature-knowledge | active |
| EV-CA-02 | markdown | cross-topic-analysis 跨主题分析 | cross-topic-analysis.md | 业务图谱根目录 | active |

### 2.4 业务图谱证据（EV-BS-01，1 条）

| evidence_id | evidence_type | title | path | source_system | status |
|-------------|---------------|-------|------|---------------|--------|
| EV-BS-01 | markdown | 网元对接业务图谱设计文档与文档清单（合并证据） | docs/superpowers/specs/2026-06-29-network-element-docking-design.md + 网元对接doc-list.md + 网元对接feature-doc-list.md | 业务图谱设计态 | active |

**EV-BS-01 说明**：本证据为合并证据源，承接 3 份图谱级文档：
1. 设计文档 `docs/superpowers/specs/2026-06-29-network-element-docking-design.md`（业务域/场景/方案设计）
2. 文档清单 `网元对接doc-list.md`（70 个原始产品文档索引 + 对接面映射）
3. 特性清单 `网元对接feature-doc-list.md`（17 引用特性反查表 + EV-FK 编号权威源）

合并为一个 EV-BS-01，因三者共同构成业务图谱（第 1 层 BD/NS/CS/DP/BR）的设计态证据，分开建 EvidenceSource 会割裂"设计依据"的完整性。

---

## 3. 原始产品文档索引（底层来源，70 md）

> 以下 70 个原始 md **不单独建 EvidenceSource**（避免冗余，已通过 EV-TK×7 凝练承接），但作为知识产物的**底层溯源基础**列出。
> 路径前缀：`output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/`
> 索引依据：`网元对接doc-list.md`（Stage 1 产出，70 md 按子主题×对接面展开）
> 编号 = doc-list §2.1~§2.9，共 9 子主题分组

### 3.1 了解组网架构（4 md → CS-5 架构认知前提）

- 了解组网架构_68634173.md
- 了解组网架构/熟悉网络架构_75096814.md
- 了解组网架构/组网互通原理_75096776.md
- 了解组网架构/逻辑接口介绍_68634155.md

### 3.2 License申请与加载（4 md → CS-5 基础就绪）

- License申请与加载/上传并激活License文件 (U2020_MAE)_16360948.md
- License申请与加载/上传并激活License文件 (OM Portal)_49599170.md
- License申请与加载/上传并激活License文件 (OM Portal)/上传License文件_13519616.md
- License申请与加载/上传并激活License文件 (OM Portal)/激活License_13519617.md

### 3.3 基础数据配置（4 md → CS-5 基础就绪）

- 基础数据配置/配置NTP时间同步_53637513.md
- 基础数据配置/修改网元基本信息_50422559.md
- 基础数据配置/配置高危命令二次授权_48016554.md
- 基础数据配置/公共参数配置_97905321.md

### 3.4 配置网元和网管对接（1 md → CS-3 网管对接）

- 配置网元和网管对接_34981624.md

### 3.5 组网对接配置（9 md → CS-1 控制面 / CS-2 用户面）

- 组网对接配置/配置业务接口数据_68634146.md（总览）
- 组网对接配置/配置业务接口数据/配置N4(N4_Sxa_Sxb)接口数据_68634162.md **→CS-1控制面**
- 组网对接配置/配置业务接口数据/配置Sa_N3_S1-U接口数据_68634192.md **→CS-2用户面**
- 组网对接配置/配置业务接口数据/配置Sc_N9c_S5-S_S8-S接口数据_68634165.md **→CS-2**
- 组网对接配置/配置业务接口数据/配置Pa(N9a_S5-P_S8-P_S2b_Gn-U_Gp-U)接口数据_68634202.md **→CS-2**
- 组网对接配置/配置业务接口数据/配置S11-U接口数据_83013474.md **→CS-2**
- 组网对接配置/配置业务接口数据/配置SGi_N6接口数据_36261585.md **→CS-2**
- 组网对接配置/配置业务接口数据/配置Nupf接口数据_64469713.md **→CS-2**
- 组网对接配置/配置会话接入数据_68634166.md **→CS-2（APN/DNN/地址池）**

### 3.6 组网路由配置（40 md → CS-4 路由对接，★最大最复杂）

**3.6.1 路由总览 + 网关侧（2 md）**
- 组网路由配置_75096802.md（总览）
- 组网路由配置/配置网关侧IP路由数据_75096770.md

**3.6.2 无NP卡_非SDN 分支（自动部署，约 12 md）**
- 组网路由配置/配置VNF侧IP路由数据（无NP卡_非SDN）_16653295.md
- …/配置VNF侧IP路由数据（无NP卡_非SDN）/非SDN组网介绍_58930406.md
- …/自动部署（推荐）_16653305.md
- …/自动部署（推荐）/配置动态路由OSPF+BFD组网（IPv4）_16653306.md
- …/自动部署（推荐）/配置静态路由+BFD组网（IPv4）_16653303.md
- …/自动部署（推荐）/配置BGP over OSPF_静态路由+BFD（IPv4）_16653311.md
- …/自动部署（推荐）/配置动态路由OSPFv3+BFD组网（IPv6）_16653296.md
- …/自动部署（推荐）/配置静态路由+BFD组网（IPv6）_16653298.md
- …/自动部署（推荐）/配置BGP over OSPFv3_静态路由+BFD（IPv6）_16653308.md
- …/自动部署（推荐）/配置IPsec_80591826.md
- …/自动部署（推荐）/配置PGW-U_UPF与PDN_DN之间的GRE隧道_84316409.md
- …/自动部署（推荐）/配置BGP_MPLS VPN（非SDN_自动）_20746526.md

**3.6.3 无NP卡_非SDN 分支（手动部署，9 md）**
- …/配置VNF侧IP路由数据（无NP卡_非SDN）/手动部署/配置动态路由OSPF+BFD组网（IPv4）_16653312.md
- …/手动部署/配置静态路由+BFD组网（IPv4）_16653313.md
- …/手动部署/配置BGP over OSPF_静态路由+BFD（IPv4）_16653300.md
- …/手动部署/配置动态路由OSPFv3+BFD组网（IPv6）_16653304.md
- …/手动部署/配置静态路由+BFD组网（IPv6）_16653301.md
- …/手动部署/配置BGP over OSPFv3_静态路由+BFD（IPv6）_16653302.md
- …/手动部署/配置IPsec_80591827.md
- …/手动部署/配置PGW-U_UPF与PDN_DN之间的GRE隧道_84974108.md
- …/手动部署/配置BGP_MPLS VPN（非SDN_手动）_70507877.md

**3.6.4 网络加速卡直连DC-GW 分支（6 md）**
- 组网路由配置/配置VNF侧IP路由数据（网络加速卡直连DC-GW）_32651719.md
- …/配置VNF侧IP路由数据（网络加速卡直连DC-GW）/修改级联口数据（NP100）_81556318.md
- …/配置VNF侧IP路由数据（网络加速卡, IPv4）_81401928.md
- …/配置VNF侧IP路由数据（网络加速卡, IPv6）_32770255.md
- …/配置VNF侧IP路由数据（网络加速卡, IPv4v6）_87775238.md
- …/配置BGP_MPLS VPN（网络加速卡）_73574941.md

**3.6.5 NP卡直连PE 分支（11 md）**
- 组网路由配置/配置VNF侧IP路由数据（NP卡直连PE）_52117668.md
- …/配置VNF侧IP路由数据（NP卡直连PE）/修改级联口数据（NP100）_90163990.md
- …/配置BGP over OSPF_静态路由+BFD（IPv4）_54211730.md
- …/配置静态路由+BFD组网（IPv4）_54211731.md
- …/配置动态路由OSPF+BFD组网（IPv4）_54211732.md
- …/配置BGP over OSPFv3_静态路由+BFD（IPv6）_54211733.md
- …/配置静态路由+BFD组网（IPv6）_54211734.md
- …/配置动态路由OSPFv3+BFD组网（IPv6）_54211735.md
- …/配置IPsec_80588530.md
- …/配置PGW-U_UPF与PDN_DN之间的GRE隧道_84978377.md
- …/配置BGP_MPLS VPN（非SDN_手动）_33255612.md

**3.6.6 SDN 分支（5 md）**
- 组网路由配置/配置VNF侧IP路由（SDN）_80548319.md
- …/配置VNF侧IP路由（SDN）/SDN组网介绍_58930596.md
- …/BGP over静态路由+BFD(IPv4)_80466089.md
- …/BGP over静态路由+BFD(IPv6)_80466090.md
- …/BGP over静态路由+BFD(IPv4v6)_80466091.md + 配置BGP_MPLS VPN（SDN）_20748722.md

### 3.7 修改MTU值（1 md → CS-5 基础就绪）

- 修改MTU值_75096774.md

### 3.8 典型配置实例（7 md → CS-4 端到端证据）

- 典型配置实例/基于OSPF路由自动部署融合UDG配置实例（IPv4）_70196672.md
- 典型配置实例/基于OSPFv3路由自动部署锚点UDG配置实例（IPv6）_70196674.md
- 典型配置实例/基于静态路由手动部署边缘UDG配置实例（IPv4）_70196678.md
- 典型配置实例/基于BGP over OSPFv3路由手动部署边缘UDG配置实例（IPv6）_70196679.md
- 典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv4）_80481423.md
- 典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv6）_80481424.md
- 典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv4v6）_80481422.md

### 3.9 整网调测（1 md → 调测验证 FirstCall）

- 整网调测_31373646.md

**小计核对**：4 + 4 + 4 + 1 + 9 + 40 + 1 + 7 + 1 = **71**（含 §3.6.6 末尾合并项的拆分计数；doc-list 总览计 70，差异源于 SDN 分支末项 "BGP over静态路由+BFD(IPv4v6) + 配置BGP_MPLS VPN（SDN）" 合并记录的口径，以 doc-list §总览 70 为准）。

---

## 4. 证据使用统计（流转关系）

> 体现证据如何在图谱各层被 `source_evidence_ids` 引用。引用关系由各图谱对象的 `source_evidence_ids` 字段承载（§6.5 supported_by 关系）。

### 4.1 EV-FK 特性知识 → 第2层特性层

| EV ID | 特性对象（02-feature-graph.md） | 引用形式 |
|-------|-------------------------------|----------|
| EV-FK-01 | Feature(GWFD-010105 用户面地址分配) | `source_evidence_ids: [EV-FK-01]` |
| EV-FK-02 | Feature(GWFD-010234 Single IP) | `source_evidence_ids: [EV-FK-02]` |
| EV-FK-03 | Feature(GWFD-020161 CU Full Mesh组网) | `source_evidence_ids: [EV-FK-03]` |
| EV-FK-04 | Feature(GWFD-020411 MPLS VPN) | `source_evidence_ids: [EV-FK-04]` |
| EV-FK-05 | Feature(GWFD-020421 基于位置的地址分配) | `source_evidence_ids: [EV-FK-05]` |
| EV-FK-06 | Feature(IPFD-010000 接口与链路) | `source_evidence_ids: [EV-FK-06]` |
| EV-FK-07 | Feature(IPFD-010001 接口管理) | `source_evidence_ids: [EV-FK-07]` |
| EV-FK-08 | Feature(IPFD-012000 IP可靠性) | `source_evidence_ids: [EV-FK-08]` |
| EV-FK-09 | Feature(IPFD-012003 BFD) | `source_evidence_ids: [EV-FK-09]` |
| EV-FK-10 | Feature(IPFD-014000 路由功能) | `source_evidence_ids: [EV-FK-10]` |
| EV-FK-11 | Feature(IPFD-014001 支持OSPF) | `source_evidence_ids: [EV-FK-11]` |
| EV-FK-12 | Feature(IPFD-014002 支持BGP) | `source_evidence_ids: [EV-FK-12]` |
| EV-FK-13 | Feature(IPFD-014003 静态路由) | `source_evidence_ids: [EV-FK-13]` |
| EV-FK-14 | Feature(IPFD-015004 IPSec功能) | `source_evidence_ids: [EV-FK-14]` |
| EV-FK-15 | Feature(IPFD-104403)（待核实，EV-FK-15 标注） | `source_evidence_ids: [EV-FK-15]` |
| EV-FK-16 | Feature(NPFD-010000 操作维护功能) | `source_evidence_ids: [EV-FK-16]` |
| EV-FK-17 | Feature(NPFD-010014 支持NTP功能) | `source_evidence_ids: [EV-FK-17]` |

**License 关联**：特性层 License 对象（如 Single IP / MPLS VPN / IPSec 等）的 `source_evidence_ids` 同样回指对应 EV-FK-XX（License 控制信息内联于特性知识）。

### 4.2 EV-TK 主题知识 → 第1层业务层 + 第3层任务层 + 第4层命令层

| EV ID | 主要消费层 | 引用形式 |
|-------|-----------|----------|
| EV-TK-01 | CS-5基础就绪(CS) + License加载(Task) + 架构认知(DP/SO) | CS/Task `source_evidence_ids` 含 EV-TK-01 |
| EV-TK-02 | CS-5基础数据(CS) + CS-3网管对接(CS) + 基础数据/网管配置(Task) + NTP/网元参数(CMD) | CS/Task/CMD `source_evidence_ids` 含 EV-TK-02 |
| EV-TK-03 | CS-1控制面(CS) + CS-2用户面(CS) + N4接口/用户面接口/会话接入(Task) + N4if/Saif/Scif/Paif(ConfigObject) | CS/Task/ConfigObject `source_evidence_ids` 含 EV-TK-03 |
| EV-TK-04 | CS-4路由对接总览 + 非SDN无NP卡自动部署(CS/DP) + 路由总览/OSPF+BFD/静态+BFD/BGP over OSPF/IPsec/GRE/MPLS VPN(Task) | CS/DP/Task/CMD `source_evidence_ids` 含 EV-TK-04 |
| EV-TK-05 | CS-4非SDN无NP卡手动 + 网络加速卡直连DC-GW(CS/DP) + 对应 Task/CMD | CS/DP/Task/CMD `source_evidence_ids` 含 EV-TK-05 |
| EV-TK-06 | CS-4 NP卡直连PE + SDN(CS/DP) + 对应 Task/CMD | CS/DP/Task/CMD `source_evidence_ids` 含 EV-TK-06 |
| EV-TK-07 | CS-4典型配置实例(端到端证据) + FirstCall整网调测(Task) + 调测验证(BR) | CS/Task/BR `source_evidence_ids` 含 EV-TK-07 |

### 4.3 EV-CA 跨产物分析 → 全层

| EV ID | 消费层 | 用途 |
|-------|--------|------|
| EV-CA-01 | 第1层(Feature引用模式) + 第2层(特性依赖/License矩阵) | 跨特性依赖、License 共享、Feature 互斥关系 |
| EV-CA-02 | 第1层(CS/DP/SO/BR 主体) + 第3层(Task 编排) + 第4层(ConfigObject/MMLCommand) | ★第1层业务图谱数据源（主体层），5 对接面 CS + 组网模式 DP + 端到端开局链路 |

### 4.4 EV-BS 业务图谱证据 → 第1层业务层

| EV ID | 消费层 | 用途 |
|-------|--------|------|
| EV-BS-01 | BD(网元对接业务域) + NS(UPF网元对接场景) + 5×CS + 12×DP + 6×BR + SO | 业务域/场景/方案的设计态权威证据（设计文档 + doc-list + feature-doc-list 三合一） |

### 4.5 流转汇总表

| 证据段 | 数量 | 主要消费层 | 次要消费层 |
|--------|------|-----------|-----------|
| EV-FK | 17 | 第2层 Feature/License | — |
| EV-TK | 7 | 第1层 CS/DP + 第3层 Task + 第4层 CMD/ConfigObject | 第1层 BR（EV-TK-07 调测） |
| EV-CA | 2 | 第1层主体（CA-02）+ 第2层特性（CA-01） | 第3层 Task + 第4层 CMD（CA-02） |
| EV-BS | 1 | 第1层 BD/NS/CS/DP/BR/SO | — |

---

## 5. 质量门禁（SOP §2.5）

- [x] 严格 Schema §8.11 字段：evidence_id / evidence_type / title / path / source_system / status（6 字段全填）
- [x] evidence_type 枚举值 `markdown`（全部 27 条均为 markdown 知识产物）
- [x] status 枚举值 `active`（全部 27 条均为正式产出的知识证据）
- [x] EV ID 与前序文件（01-business-graph / 02-feature-graph / 03-task-layer / 04-command-graph）使用的编号**完全一致**
- [x] EV-FK-01~17 编号规则：feature_code 字母序（GWFD→IPFD→NPFD），与 feature-doc-list.md §特性总表权威源对齐
- [x] path 全部为相对路径（基准 `业务图谱体系/网元对接/`），可定位
- [x] 原始 70 md 按 doc-list §2.1~§2.9 子主题分组索引（CS-4 路由 40 md 进一步按 6 组网模式分支细分）
- [x] 证据流转统计覆盖全层（EV-FK→特性层 / EV-TK→业务+任务+命令 / EV-CA→全层 / EV-BS→业务层）
- [x] 原始 md 不单独建 EvidenceSource（避免冗余，已由 EV-TK 凝练承接）

---

## 6. 注册汇总

| 类型 | EV 段 | 数量 |
|------|-------|------|
| 特性知识证据 | EV-FK-01~17 | 17 |
| 主题知识证据 | EV-TK-01~07 | 7 |
| 跨特性分析 | EV-CA-01 | 1 |
| 跨主题分析 | EV-CA-02 | 1 |
| 业务图谱证据 | EV-BS-01 | 1 |
| **注册 EvidenceSource 合计** | | **27** |

底层原始产品文档索引：**70 md**（不单独注册，作为溯源基础，详见 §3）。
