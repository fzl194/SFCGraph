# 网元对接三层图谱 · 第2层：特性图谱

> **文件定位**：`three-layer-graph/02-feature-graph.md`
> **业务域**：网元对接（UDG 扮演 UPF / PGW-U / SGW-U）
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §9 特性图谱 / §13 禁止关系
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化对接场景 17 个引用 Feature（含 1 别名归并）+ depends_on 边 + requires_license 边 + License + FeatureRule
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（EV-CA-01，314 行）+ 17 个特性知识文件（EV-FK-01~17）
> **场景特性说明**：对接类场景中特性是**引用支撑**（非主体），图谱主体为第1层对接面 CS。第2层精简表达 17 引用特性 + 依赖 + License + 规则，**不展开命令**（命令在第4层 04-command-graph）。

---

## 0. 特性图谱总览

### 0.1 17 Feature 分组（对接面映射）

| 分组（feature_group） | 数量 | 成员 | 主要对接面 |
|----------------------|------|------|-----------|
| **IPFD 路由转发类** | 10 | IPFD-010000/010001/012000/012003/014000/014001/014002/014003/015004/104403 | CS-4 路由对接（占 ~80% 引用） |
| **GWFD 网关功能类** | 5 | GWFD-010105/010234/020161/020411/020421 | CS-1 控制面 / CS-2 用户面 / CS-4 路由 |
| **NPFD 操作维护类** | 2 | NPFD-010000/010014 | CS-3 网管 / CS-5 基础就绪 |
| **合计** | **17** | — | — |

> 对接面集中度印证图谱主体为 CS-4 路由对接：IPFD 路由类 10 特性累计 112 篇引用 / 140 总引用 ≈ 80%。

### 0.2 License 总览

| 类别 | 数量 | 成员 |
|------|------|------|
| 受控 License | **3** | LKV3G5CUFM01（CU Full Mesh）/ LKV3G5MPLS01（MPLS VPN）/ LKV3G5LBAA01（基于位置地址分配） |
| 无需 License | **14** | 全部 10 IPFD + GWFD-010105/010234 + 全部 2 NPFD |
| License 分布特征 | — | 全部集中在 GWFD 网关类（3/5 GWFD 受控）；IPFD 路由类与 NPFD 运维类完全免费 |

### 0.3 全局字段声明

> **适用范围**：本文件 §1（16 个规范 Feature 节点 + 1 个别名节点）、§3（3 个 License）所有对象。
> **status 字段声明**：除 §1.10 中 IPFD-104403（别名，`status=deprecated`）外，本文件所有 Feature 与 License 的 `status` 字段值均为 `active`。
> **依据**：Schema §9.3（Feature.status 必备）、§9.5（License.status 必备）。
> **parent_feature_id 约定**：附录 A 中父特性如 `GWFD-010100/010220/020160/020410/020420/015000`（17 引用集外的特性目录父节点）不在本图谱建模范围，仅作归属记录；本图谱内建模的目录父节点（IPFD-010000/012000/014000、NPFD-010000）为 4 个。

---

## 1. Feature 实例化（16 个规范节点 + 1 个别名节点）

> **节点数说明**：17 引用特性中 IPFD-104403 为 IPFD-012003 BFD 的历史引用代号（别名），按 §4 FeatureRule FR-UD-04 归并处理。本节建模 16 个规范 Feature 对象（§1.1~1.16）+ 1 个别名说明（§1.17，status=deprecated，不参与 depends_on / requires_license 计数）。

### 1.1 GWFD 网关功能类（5 个）

#### GWFD-010105 用户面地址分配

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010105` |
| `feature_name` | `用户面地址分配` |
| `feature_summary` | UDG 本地为 UE 分配 IPv4/IPv6/IPv4v6 地址并生成下行回程路由，是"配置会话接入数据"的前提特性，决定 UE 能否成功激活接入 PDN/DN |
| `feature_group` | `GWFD 网关功能类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["地址版本(IPv4/IPv6/IPv4v6)","分配规则(IPALLOCRULE)","地址池(POOL/POOLGROUP)"]` |
| `parent_feature_id` | `GWFD-010100` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-01"]` |

#### GWFD-010234 Single IP

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010234` |
| `feature_name` | `Single IP` |
| `feature_summary` | UDG 融合部署（SGW-U/PGW-U/UPF）时让 N3/S1-U、S5-P/S8-P/N9a、S5-S/S8-S/N9c、N4 等多类业务逻辑接口复用一个 IP 地址，是业务接口数据配置的必备前置特性 |
| `feature_group` | `GWFD 网关功能类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["逻辑接口类型(N4if/Saif/Paif/Scif)","地址复用机制"]` |
| `parent_feature_id` | `GWFD-010220` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-02"]` |

> **注**：本特性 `config_relevance=none`（17 特性中唯一），为地址复用机制而非独立配置项，能力通过 ADD LOGICINF 等接口命令隐式生效；图谱保留为特性节点但不强制关联 Task。

#### GWFD-020161 CU Full Mesh 组网

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020161` |
| `feature_name` | `CU Full Mesh 组网` |
| `feature_summary` | C 面（SMF/SGW-C/PGW-C）与 U 面（UPF/SGW-U/PGW-U）在 N4/Sx 接口全互联，支持多对多解耦对接，是 N4 接口配置对接 SMF 时的组网前提 |
| `feature_group` | `GWFD 网关功能类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"]}` |
| `variant_dimensions` | `["C/U 解耦模式","N4/Sx 偶联拓扑","PFCP 协议"]` |
| `parent_feature_id` | `GWFD-020160` |
| `first_release` | — |
| `status` | `active` |
| `requires_license` | `LKV3G5CUFM01` |
| `source_evidence_ids` | `["EV-FK-03"]` |

#### GWFD-020411 MPLS VPN

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020411` |
| `feature_name` | `MPLS VPN` |
| `feature_summary` | UDG 作为 PE 对接 CE/DC-GW 承载 L3VPN，是 VNF 侧对接 PE/DC-GW 的 BGP+MPLS VPN 组网路由方案核心特性，贯穿 SDN/非 SDN/网络加速卡三类部署 |
| `feature_group` | `GWFD 网关功能类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"]}` |
| `variant_dimensions` | `["部署形态(NP卡直连PE/非SDN/网络加速卡/SDN)","L3VPN实例","RT路由目标","MPLS接口"]` |
| `parent_feature_id` | `GWFD-020410` |
| `first_release` | — |
| `status` | `active` |
| `requires_license` | `LKV3G5MPLS01` |
| `source_evidence_ids` | `["EV-FK-04"]` |

#### GWFD-020421 基于位置的地址分配

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020421` |
| `feature_name` | `基于位置的地址分配` |
| `feature_summary` | UDG 按用户 LAC/TAC 动态分配 IP，是"配置会话接入数据"中按区域差异化规划 IP 的可选地址分配特性，与 GWFD-010105 互补（父目录提供基础地址池，本特性叠加位置维度） |
| `feature_group` | `GWFD 网关功能类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"]}` |
| `variant_dimensions` | `["位置维度(LAC/TAC)","地址分段(SECTION)","位置-地址池映射"]` |
| `parent_feature_id` | `GWFD-020420` |
| `first_release` | — |
| `status` | `active` |
| `requires_license` | `LKV3G5LBAA01` |
| `source_evidence_ids` | `["EV-FK-05"]` |

### 1.2 IPFD 接口与可靠性类（3 个，含 2 目录父节点）

#### IPFD-010000 接口与链路（目录父节点）

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-010000` |
| `feature_name` | `接口与链路` |
| `feature_summary` | IP 基本特性下接口与链路分类根（is_directory=true），涵盖虚拟物理接口与逻辑接口；对接场景中作为接口管理/IP 编址能力的父节点，被 MTU、业务接口配置间接引用 |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":"目录父节点(子能力承载具体NF支持)"}` |
| `variant_dimensions` | `["接口分类(虚拟物理/逻辑)"]` |
| `parent_feature_id` | —（根） |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-06"]` |

> **目录父节点说明**：本节点不直接承载 MML 命令，命令由子特性 IPFD-010001 承载（见 §13 禁止关系：Feature 不直接绑 MMLCommand）。

#### IPFD-010001 接口管理

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-010001` |
| `feature_name` | `接口管理` |
| `feature_summary` | 提供逻辑接口/虚拟物理接口的创建与 IP 编址，是 MTU 修改、各业务接口（N4/Pa/Sc/Sa）配置的基础能力 |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["接口类型(逻辑/虚拟物理)","IP编址(IPv4/IPv6)","MTU"]` |
| `parent_feature_id` | `IPFD-010000` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-07"]` |

#### IPFD-012000 IP 可靠性（目录父节点）

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-012000` |
| `feature_name` | `IP 可靠性` |
| `feature_summary` | BFD 等链路检测能力的根（is_directory=true），对接 PE/DC-GW 的动态路由+BFD 组网方案的父能力，被全部 IP 路由方案间接引用 |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":"目录父节点(子能力承载具体NF支持)"}` |
| `variant_dimensions` | `["链路检测机制(BFD/SR-BFD)"]` |
| `parent_feature_id` | —（根） |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-08"]` |

> **目录父节点说明**：本节点不直接承载 MML 命令，命令由子特性 IPFD-012003 BFD 承载。

#### IPFD-012003 BFD

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-012003` |
| `feature_name` | `BFD` |
| `feature_summary` | 快速检测链路/IP 路由连通故障，几乎贯穿所有 VNF 侧 IP 路由组网方案（静态路由+BFD / OSPF+BFD / BGP+BFD），保障对接 PE/DC-GW 的路由快速收敛；引用 20 篇，是可靠性主线 |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["检测模式(BFD/SR-BFD)","部署形态(非SDN/SDN-AUTOSCALINGBFD)","绑定路由协议(OSPF/BGP/静态)"]` |
| `parent_feature_id` | `IPFD-012000` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-09"]` |

> **别名归并说明**：IPFD-104403（BFD 初始配置引用代号）为 IPFD-012003 的历史引用代号，合并引用篇数 20+3=23。规范节点用 IPFD-012003，IPFD-104403 作别名（见 §1.17 + FR-UD-04）。

### 1.3 IPFD 路由功能类（4 个，含 1 目录父节点）

#### IPFD-014000 路由功能（目录父节点）

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-014000` |
| `feature_name` | `路由功能` |
| `feature_summary` | IP 基本特性下路由能力根（is_directory=true），涵盖 OSPF/BGP/静态路由，是所有 VNF 侧 IP 路由对接方案的父能力；引用次数最高（29 篇） |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":"目录父节点(子能力承载具体NF支持)"}` |
| `variant_dimensions` | `["路由协议(OSPF/BGP/静态)","IP版本(IPv4/IPv6)","VPN实例"]` |
| `parent_feature_id` | —（根） |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-10"]` |

> **目录父节点说明**：本节点不直接承载 MML 命令，命令由子特性 IPFD-014001（OSPF）/ 014002（BGP）/ 014003（静态路由）承载。

#### IPFD-014001 支持 OSPF

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-014001` |
| `feature_name` | `支持 OSPF` |
| `feature_summary` | 内部网关动态路由（OSPFv2/v3），用于 UDG 与 PE/DC-GW 三层互通的"动态路由 OSPF+BFD 组网"方案（IPv4/IPv6），NP 卡直连 PE 与非 SDN 两种部署均使用 |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["OSPF版本(v2/v3)","区域(OSPFAREA)","接口(OSPFINTERFACE)","部署形态(NP卡直连PE/非SDN)"]` |
| `parent_feature_id` | `IPFD-014000` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-11"]` |

#### IPFD-014002 支持 BGP

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-014002` |
| `feature_name` | `支持 BGP` |
| `feature_summary` | AS 间动态路由，用于 UDG 与 PE/DC-GW 的 BGP over OSPF/静态路由、BGP+MPLS VPN 等对接方案，承载 VPNv4/IPv4/IPv6 地址族；引用 17 篇 |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["BGP地址族(VPNv4/IPv4/IPv6)","VRF","对等体(BGPPEER)","部署形态(NP卡直连PE/非SDN/网络加速卡/SDN)"]` |
| `parent_feature_id` | `IPFD-014000` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-12"]` |

#### IPFD-014003 静态路由

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-014003` |
| `feature_name` | `静态路由` |
| `feature_summary` | 手工配置目标网段下一跳，用于 UDG 与 PE/DC-GW 简单对接或作为"BGP over 静态路由+BFD"方案的底层路由（SDN/非 SDN/NP 卡三类部署均涉及）；引用 9 篇 |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["IP版本(IPv4/IPv6)","部署形态(NP卡直连PE/非SDN/SDN)","路由引入(IMPORTROUTE)"]` |
| `parent_feature_id` | `IPFD-014000` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-13"]` |

### 1.4 IPFD 安全类（1 个）

#### IPFD-015004 IPSec 功能

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-015004` |
| `feature_name` | `IPSec 功能` |
| `feature_summary` | 对 UDG 与对端（PE/DC-GW/网管）间的 IP 报文提供加密/完整性/防重放保护，是 VNF 侧 IP 路由对接中"配置 IPsec"隧道方案的核心特性（NP 卡直连 PE/非 SDN 两类部署） |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["隧道模式","安全联盟(SA)","部署形态(NP卡直连PE/非SDN)"]` |
| `parent_feature_id` | `IPFD-015000` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-14"]` |

### 1.5 NPFD 操作维护类（2 个，含 1 目录父节点）

#### NPFD-010000 操作维护功能（目录父节点）

| 字段 | 值 |
|------|---|
| `feature_id` | `NPFD-010000` |
| `feature_name` | `操作维护功能` |
| `feature_summary` | 网管特性根（is_directory=true，category=operations），涵盖性能/软件/故障/设备/安全等运维能力；对接场景中作为 NTP 时间同步等基础运维配置的父节点 |
| `feature_group` | `NPFD 操作维护类` |
| `applicable_nf_map` | `{"UDG":"目录父节点(子能力承载具体NF支持)"}` |
| `variant_dimensions` | `["运维能力(性能/软件/故障/设备/安全)"]` |
| `parent_feature_id` | —（根） |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-16"]` |

> **目录父节点说明**：本节点不直接承载 MML 命令，命令由子特性如 NPFD-010014（NTP）承载。

#### NPFD-010014 支持 NTP 功能

| 字段 | 值 |
|------|---|
| `feature_id` | `NPFD-010014` |
| `feature_name` | `支持 NTP 功能` |
| `feature_summary` | UDG 从 OMC/FusionStage 双路同步时间，保障对接信令（证书/Timestamp）与日志时间一致性，是"基础数据配置-配置 NTP 时间同步"的必备项 |
| `feature_group` | `NPFD 操作维护类` |
| `applicable_nf_map` | `{"UDG":["GGSN","SGW-U","PGW-U","UPF"],"NB-IoT":"M"}` |
| `variant_dimensions` | `["时间源(OMC/FusionStage双路)"]` |
| `parent_feature_id` | `NPFD-010000` |
| `first_release` | — |
| `status` | `active` |
| `source_evidence_ids` | `["EV-FK-17"]` |

### 1.6 IPFD-104403 别名节点（deprecated，不参与计数）

#### IPFD-104403 BFD（初始配置引用代号，别名 → IPFD-012003）

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-104403` |
| `feature_name` | `BFD（初始配置引用代号）` |
| `feature_summary` | 初始配置文档中对 BFD 特性的引用代号（文档链接实际指向 IPFD-012000 IP 可靠性 / IPFD-012003 BFD）；仅出现在 SDN 侧"BGP over 静态路由+BFD"三篇（IPv4/IPv4v6/IPv6），本质=BFD 能力在 SDN 路由方案中的引用。**别名归并：规范节点 = IPFD-012003** |
| `feature_group` | `IPFD 路由转发类` |
| `applicable_nf_map` | —（未在 features.jsonl 登记，引用上下文等同 IPFD-012003） |
| `variant_dimensions` | —（别名，归并到 IPFD-012003） |
| `parent_feature_id` | `IPFD-012000` |
| `alias_of` | `IPFD-012003` |
| `status` | **`deprecated`**（别名归并，不单独建规范节点） |
| `source_evidence_ids` | `["EV-FK-15"]` |

> **处理依据**：FR-UD-04（见 §4 FeatureRule）。本节点不参与 depends_on / requires_license / constrained_by 计数；引用证据（3 篇 SDN）已归并到 IPFD-012003。

---

## 2. Feature depends_on 关系边（4 条）

> **数据来源**：cross-feature-analysis.md §3.1（显式 depends_on）。父子目录关系（is_directory 隐含）通过 `parent_feature_id` 字段建模，不计入 depends_on。
> **范围说明**：4 条边中 3 条指向 17 引用集**外部特性**（GWFD-010224 / GWFD-010233），1 条为**集内闭环依赖**（GWFD-020421 → GWFD-010105）。

| 边序号 | 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 | 范围 |
|--------|-----------|------|-------------|----------|----------|------|
| 1 | `GWFD-010105`（用户面地址分配） | `depends_on` | `GWFD-010224`（N4 接口） | mandatory | 地址分配需 N4 接口偶联前提 | 外部特性（不在 17 引用集内） |
| 2 | `GWFD-010105`（用户面地址分配） | `depends_on` | `GWFD-010233`（Sxb 接口） | mandatory | 地址分配需 Sxb 接口前提 | 外部特性 |
| 3 | `GWFD-020161`（CU Full Mesh 组网） | `depends_on` | `GWFD-010224`（N4/Sx 接口 PFCP 协议） | mandatory | CU Full Mesh 建立在 N4/Sx PFCP 之上 | 外部特性 |
| 4 | `GWFD-020421`（基于位置的地址分配） | `depends_on` | `GWFD-010105`（用户面地址分配） | mandatory | 位置维度叠加在基础地址池之上 | **集内闭环依赖** |

### 2.1 依赖图可视化

```
GWFD-010224(N4接口,外部) ←──┐
GWFD-010233(Sxb接口,外部)←──┤
                              ├── GWFD-010105(用户面地址分配) ←── GWFD-020421(基于位置的地址分配)
GWFD-010224(N4/Sx PFCP,外部)─┘
                              └── GWFD-020161(CU Full Mesh组网)

其余 13 特性：基础/目录特性，无显式 depends_on（作为独立特性节点）
```

### 2.2 has_subfeature 关系（父子目录，建模在 parent_feature_id 字段）

> 不单独建边表，已通过 §1 各 Feature 的 `parent_feature_id` 字段表达。本图谱内建模的目录父节点（4 个）：IPFD-010000 / IPFD-012000 / IPFD-014000 / NPFD-010000。

---

## 3. License 实例化（3 个 License + 14 个无需 License 特性）

### 3.1 受 License 控制的 License 对象（3 个）

| `license_id` | `license_name` | `license_summary` | 对应 Feature | `status` | `source_evidence_ids` |
|---------------|----------------|-------------------|-------------|----------|----------------------|
| `LKV3G5CUFM01` | `CU Full Mesh 组网` | 5G 分布式 C/U 解耦全互联组网能力 License | GWFD-020161 | `active` | `["EV-FK-03"]` |
| `LKV3G5MPLS01` | `MPLS VPN` | L3VPN 承载能力 License（BGP+MPLS） | GWFD-020411 | `active` | `["EV-FK-04"]` |
| `LKV3G5LBAA01` | `基于位置的地址分配` | 按 LAC/TAC 差异化地址策略 License | GWFD-020421 | `active` | `["EV-FK-05"]` |

### 3.2 requires_license 关系边（3 条）

| 源 Feature | 关系 | 目标 License |
|-----------|------|-------------|
| `GWFD-020161`（CU Full Mesh 组网） | `requires_license` | `LKV3G5CUFM01` |
| `GWFD-020411`（MPLS VPN） | `requires_license` | `LKV3G5MPLS01` |
| `GWFD-020421`（基于位置的地址分配） | `requires_license` | `LKV3G5LBAA01` |

### 3.3 无需 License 特性（14 个）

| feature_code | 名称 | 类别 | 说明 |
|--------------|------|------|------|
| GWFD-010105 | 用户面地址分配 | GWFD | 基础地址池能力，免费 |
| GWFD-010234 | Single IP | GWFD | 地址复用机制，免费 |
| IPFD-010000 | 接口与链路（目录） | IPFD | 路由类零 License |
| IPFD-010001 | 接口管理 | IPFD | 路由类零 License |
| IPFD-012000 | IP 可靠性（目录） | IPFD | 路由类零 License |
| IPFD-012003 | BFD | IPFD | 路由类零 License |
| IPFD-014000 | 路由功能（目录） | IPFD | 路由类零 License |
| IPFD-014001 | 支持 OSPF | IPFD | 路由类零 License |
| IPFD-014002 | 支持 BGP | IPFD | 路由类零 License |
| IPFD-014003 | 静态路由 | IPFD | 路由类零 License |
| IPFD-015004 | IPSec 功能 | IPFD | 路由类零 License |
| NPFD-010000 | 操作维护功能（目录） | NPFD | 运维类零 License |
| NPFD-010014 | 支持 NTP 功能 | NPFD | 运维类零 License |

> **License 分布特征**：License 全部集中在 GWFD 网关类（3/5 GWFD 受控），IPFD 路由转发类与 NPFD 运维类完全免费。受控特性均为"组网演进/分布式解决方案"增值能力：CU Full Mesh（分布式 C/U 解耦）/ MPLS VPN（L3VPN 承载）/ 基于位置地址分配（差异化地址策略）。CS-4 路由对接主体特性（IPFD 路由类）零 License → 路由对接基线能力免费，仅 MPLS VPN 这一进阶方案收费。

---

## 4. FeatureRule（4 条，归纳共性规则）

> **Schema参考**：Schema §9.6 FeatureRule + §6.1 Rule 共享结构。
> **范围**：本场景特性为引用支撑，FeatureRule 归纳 17 特性的共性约束（不展开命令级规则，命令级规则在第4层 CommandRule）。

| `rule_id` | `owner_ref_type` | `owner_ref` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|------------------|-------------|-------------|-------------|------------------------|--------------------|--------------|-------------------|------------|----------------------|
| `FR-UD-01` | `feature` | `IPFD-014000`（路由功能，目录父节点） | 路由目录父节点不直接承载命令 | `restriction_rule` | `explicit` | `principle` | IPFD-014000（路由功能）、IPFD-012000（IP 可靠性）、IPFD-010000（接口与链路）、NPFD-010000（操作维护）共 4 个目录父节点（is_directory=true）作为"能力分类根"，本身不挂 MML 命令；具体命令由子能力（IPFD-014001/014002/014003、IPFD-012003、IPFD-010001、NPFD-010014）承载 | 父节点挂命令将违反 §13 禁止关系（Feature→MMLCommand 直接强绑定） | critical | `["EV-CA-01", "EV-FK-06", "EV-FK-08", "EV-FK-10", "EV-FK-16"]` |
| `FR-UD-02` | `feature` | `IPFD-012003`（BFD） | IPFD 路由类共享"VPN→协议→BFD"三段式命令模式 | `consistency_rule` | `implicit` | `config` | CS-4 全部路由方案几乎贯穿"`VPN 实例(VPNINST/L3VPNINST) → 路由协议(OSPF/BGP/静态) → BFD 检测`"三段式；BFD（IPFD-012003）被 OSPF/BGP/静态路由方案全部引用（"OSPF+BFD"/"BGP over OSPF+静态路由+BFD"/"静态路由+BFD"），形成"路由+BFD"标准搭档 | 不配置 BFD 将导致路由无法快速收敛，对接 PE/DC-GW 故障检测延迟 | warning | `["EV-CA-01", "EV-FK-09", "EV-FK-11", "EV-FK-12", "EV-FK-13"]` |
| `FR-UD-03` | `feature` | `GWFD-020411`（MPLS VPN） | License 仅约束 GWFD 网关类增值能力 | `restriction_rule` | `explicit` | `restriction` | 17 引用特性中仅 3 个受 License 控制（GWFD-020161 CU Full Mesh / GWFD-020411 MPLS VPN / GWFD-020421 基于位置地址分配），均为"组网演进/分布式解决方案"增值能力；全部 10 IPFD 路由类 + 2 NPFD 运维类 + GWFD-010105/010234 共 14 特性免费。CS-4 路由对接基线能力零 License | 未开启对应 License 时增值方案不可用；路由对接基线（OSPF/BGP/静态/BFD）不受影响 | warning | `["EV-CA-01", "EV-FK-03", "EV-FK-04", "EV-FK-05"]` |
| `FR-UD-04` | `feature` | `IPFD-012003`（BFD） | IPFD-104403 别名归并到 IPFD-012003 | `naming_rule` | `explicit` | `principle` | IPFD-104403 为初始配置文档对 BFD 特性的历史引用代号（文档链接实际指向 IPFD-012000/IPFD-012003），仅出现在 SDN 侧"BGP over 静态路由+BFD"3 篇。规范处理：以 IPFD-012003 BFD 为规范节点（合并引用 20+3=23 篇），IPFD-104403 作 `status=deprecated` 别名节点保留（不参与 depends_on / requires_license 计数），避免重复建模 | 若不归并将导致 BFD 能力被建模为两个节点，引用证据与命令（DSP BFDSESSION / ADD AUTOSCALINGBFD）重复 | info | `["EV-CA-01", "EV-FK-09", "EV-FK-15"]` |

---

## 5. 特性图谱关系边汇总

| 关系类型 | 数量 | 说明 |
|---------|------|------|
| `depends_on` | **4** | 3 条指向外部特性（GWFD-010224/010233）+ 1 条集内闭环（GWFD-020421→GWFD-010105） |
| `requires_license` | **3** | GWFD-020161/020411/020421 各 1 条 |
| `has_subfeature`（parent_feature_id 建模） | 12 | 4 目录父节点 → 子能力（IPFD-010000→010001；IPFD-012000→012003；IPFD-014000→014001/014002/014003；NPFD-010000→010014）+ 别名 IPFD-104403→IPFD-012000 |
| `decomposes_to`（Feature→ConfigTask，Schema §9.8） | **14** | 见 §5.1 decomposes_to 边表（与 05-cross-layer-mapping §3.1 一致） |
| `constrained_by`（FeatureRule） | **4** | FR-UD-01~FR-UD-04 |
| **特性层对象总计** | **16 Feature（规范）+ 1 别名（deprecated）+ 3 License + 4 FeatureRule** | — |

> **§13 禁止关系遵循**：本图谱 Feature 不直接绑 MMLCommand / ConfigObject；特性差异（如部署形态、IP 版本、路由协议）通过 `variant_dimensions` 字段 + FeatureRule 表达；命令与配置对象延后到第4层 04-command-graph。

### 5.1 Feature `decomposes_to` ConfigTask 边表（14 条，Schema §9.8，与 05 §3.1 一致）

> **U-H-03 修复**：补建 Feature→ConfigTask 的 `decomposes_to` 正式关系边，使特性层关系边完整。task_id 为 03-task-layer 权威形式 `T-ND-NN`。
> **范围说明**：目录父节点（IPFD-010000/012000/014000、NPFD-010000）不直接 decomposes_to，由其子能力间接覆盖（符合 FR-UD-01）。别名节点 IPFD-104403（deprecated）不参与。

| 边序号 | 源 Feature | 关系 | 目标 ConfigTask | 说明 |
|--------|-----------|------|-----------------|------|
| 1 | `GWFD-010234`（Single IP） | `decomposes_to` | `T-ND-07`（配置 N4 控制面接口） | Single IP 支持 N4if 抽象合一 |
| 2 | `GWFD-010234`（Single IP） | `decomposes_to` | `T-ND-08`（配置业务用户面接口） | Single IP 支持业务接口抽象合一（Saif/Scif/Paif） |
| 3 | `GWFD-010105`（用户面地址分配） | `decomposes_to` | `T-ND-09`（配置会话接入） | 地址分配是会话接入闭环核心 |
| 4 | `GWFD-020421`（基于位置的地址分配） | `decomposes_to` | `T-ND-09`（配置会话接入） | 位置维度叠加在 IPALLOCRULE |
| 5 | `GWFD-020161`（CU Full Mesh 组网） | `decomposes_to` | `T-ND-07`（配置 N4 控制面接口） | 多 SMF 对接前提 |
| 6 | `GWFD-020161`（CU Full Mesh 组网） | `decomposes_to` | `T-ND-17`（配置 NP 卡级联口） | NP100 多框级联拓扑 |
| 7 | `GWFD-020411`（MPLS VPN） | `decomposes_to` | `T-ND-16`（配置隧道） | MPLS VPN 隧道方案 |
| 8 | `IPFD-014001`（支持 OSPF） | `decomposes_to` | `T-ND-12`（配置 OSPF） | — |
| 9 | `IPFD-014002`（支持 BGP） | `decomposes_to` | `T-ND-13`（配置 BGP） | — |
| 10 | `IPFD-014003`（静态路由） | `decomposes_to` | `T-ND-14`（配置静态路由） | — |
| 11 | `IPFD-012003`（BFD） | `decomposes_to` | `T-ND-15`（配置 BFD） | — |
| 12 | `IPFD-015004`（IPSec 功能） | `decomposes_to` | `T-ND-16`（配置隧道） | IPsec 隧道方案 |
| 13 | `IPFD-010001`（接口管理） | `decomposes_to` | `T-ND-08`（配置业务用户面接口） | 接口创建/IP 编址基础 |
| 14 | `IPFD-010001`（接口管理） | `decomposes_to` | `T-ND-10`（VPN 实例与接口绑定）/ `T-ND-11`（外联口自动部署） | MTU/外联口基础 |
| — | `NPFD-010014`（支持 NTP 功能） | `decomposes_to` | `T-ND-02`（配置 NTP 时间同步） | NTP 时间源 |
| — | `NPFD-010000`（操作维护功能，目录） | `decomposes_to` | `T-ND-03`（修改网元基本信息）/ `T-ND-05`（高危命令二次授权）/ `T-ND-06`（网管对接） | 由目录父节点聚合表达运维 task 归属 |

> **计数说明**：上表显式列出 14 条核心 decomposes_to 边（边序号 1~14，与 05 §3.1 的 14 条映射一一对应）；末两行（NPFD-010014 / NPFD-010000）为运维类特性的补充映射，未计入 14 条主边数（与 05 §3.1 口径一致）。目录父节点 IPFD-010000/012000/014000 由子能力间接覆盖，不单独建边。

---

## 6. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| Feature（规范节点） | **16** | GWFD-010105/010234/020161/020411/020421 + IPFD-010000/010001/012000/012003/014000/014001/014002/014003/015004 + NPFD-010000/010014 |
| Feature（别名节点） | 1（deprecated） | IPFD-104403（= IPFD-012003 别名） |
| License | **3** | LKV3G5CUFM01 / LKV3G5MPLS01 / LKV3G5LBAA01 |
| FeatureRule | **4** | FR-UD-01 ~ FR-UD-04 |
| depends_on 边 | **4** | 3 外部 + 1 集内闭环 |
| requires_license 边 | **3** | 3 GWFD 受控特性 |
| decomposes_to 边（Feature→ConfigTask，U-H-03 补建） | **14** | 见 §5.1，与 05 §3.1 一致 |
| **特性层对象总计** | **41**（16+1+3+4 + 4+3+14，去重边） | — |

---

## 7. 与其他场景特性图谱的差异

| 维度 | 网元对接（UDG/UPF）场景 | 计费场景（标杆） |
|------|----------------------|----------------|
| Feature 数量 | 16 规范 + 1 别名（17 引用） | 14（UDG 9 + UNC 5） |
| 特性定位 | **引用支撑**（非图谱主体，主体=对接面 CS） | 主体（特性驱动配置） |
| 特性族 | IPFD 路由转发类（10）+ GWFD 网关功能类（5）+ NPFD 运维类（2） | 计费三件套 + 协议栈（Ga/Gy/N40） |
| 独有 Feature | IPFD-014001/014002/014003（路由协议）、GWFD-020411（MPLS VPN）、GWFD-020161（CU Full Mesh）等 | GWFD-020300/020301/020302/020303/020306 等 |
| 共享 Feature | （无，本场景为独立特性集） | — |
| License 数 | 3（全部 GWFD） | 11（UDG 7 + UNC 4） |
| 依赖链核心 | GWFD-010224/010233(外部) → GWFD-010105 → GWFD-020421；GWFD-010224 → GWFD-020161 | SA-Basic → PCC → 内容计费 → [在线/离线/融合/计量增强] |
| depends_on 边数 | 4（稀疏，13 特性无显式依赖） | 16（密集依赖链） |
| FeatureRule 数 | 4（共性归纳） | 9（命令级细化） |
| 命令展开 | **不展开**（命令在第4层） | 部分展开（关联 MML 命令列出） |

> **场景特性**：对接类场景特性图谱明显比业务类（计费）更精简——依赖稀疏（基础/目录特性无显式依赖）、License 集中（仅 GWFD 增值能力）、规则归纳共性（不展开命令级）。图谱主体（对接面 CS）在第1层 01-business-graph，本层仅作引用支撑。

---

## 附录 A：17 引用特性索引（EV-FK-01~17）

> 完整索引见 `feature-knowledge/cross-feature-analysis.md` 附录 A。本附录仅列特性 ID 与 EV 编号对应关系，供 source_evidence_ids 追溯。

| EV ID | feature_code | 名称 | feature_group | is_directory | 对接面 | 别名/归并 |
|-------|-------------|------|---------------|-------------|--------|-----------|
| EV-FK-01 | GWFD-010105 | 用户面地址分配 | GWFD | false | CS-2 | — |
| EV-FK-02 | GWFD-010234 | Single IP | GWFD | false | CS-2 | — |
| EV-FK-03 | GWFD-020161 | CU Full Mesh 组网 | GWFD | false | CS-1 | — |
| EV-FK-04 | GWFD-020411 | MPLS VPN | GWFD | false | CS-4 | — |
| EV-FK-05 | GWFD-020421 | 基于位置的地址分配 | GWFD | false | CS-2 | — |
| EV-FK-06 | IPFD-010000 | 接口与链路 | IPFD | **true** | CS-2 | — |
| EV-FK-07 | IPFD-010001 | 接口管理 | IPFD | false | CS-2 | — |
| EV-FK-08 | IPFD-012000 | IP 可靠性 | IPFD | **true** | CS-4 | — |
| EV-FK-09 | IPFD-012003 | BFD | IPFD | false | CS-4 | 规范节点（吸收 IPFD-104403） |
| EV-FK-10 | IPFD-014000 | 路由功能 | IPFD | **true** | CS-4 | — |
| EV-FK-11 | IPFD-014001 | 支持 OSPF | IPFD | false | CS-4 | — |
| EV-FK-12 | IPFD-014002 | 支持 BGP | IPFD | false | CS-4 | — |
| EV-FK-13 | IPFD-014003 | 静态路由 | IPFD | false | CS-4 | — |
| EV-FK-14 | IPFD-015004 | IPSec 功能 | IPFD | false | CS-4 | — |
| EV-FK-15 | IPFD-104403 | BFD（初始配置引用代号） | IPFD | false | CS-4(SDN) | **别名→IPFD-012003**（deprecated） |
| EV-FK-16 | NPFD-010000 | 操作维护功能 | NPFD | **true** | CS-3/CS-5 | — |
| EV-FK-17 | NPFD-010014 | 支持 NTP 功能 | NPFD | false | CS-3/CS-5 | — |

---

> 本文件为网元对接三层图谱第2层。第1层业务图谱、第3层任务原子层、第4层命令图谱、第5层跨层映射、第6层证据索引见同目录其他文件。
