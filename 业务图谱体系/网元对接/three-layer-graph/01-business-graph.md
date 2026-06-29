# 网元对接三层图谱 · 第1层：业务图谱

> **文件定位**：`three-layer-graph/01-business-graph.md`
> **业务域**：网元对接（BD-ND） | **子场景**：UPF 网元对接（NS-ND-UPF）
> **UDG 角色**：UPF / PGW-U / SGW-U 融合，对接 N4 / N3 / N9 / N6
> **Schema 参考**：`三层图谱Schema-最终版-v0.1.md` §8 业务图谱 / §13 禁止关系
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化对接场景业务层对象（BD / NS / CS / DP / BR / SO）及其关系边
> **★场景特殊性**：本场景是**对接类场景**，主体是对接方案闭包(CS)与组网模式决策点(DP)，特性是引用支撑（非主体）；CS 按对接面组织（区别计费场景按业务能力组织）
> **数据来源**：
> - `cross-topic-analysis.md`（EV-CA-02，§6 是核心数据源：5 CS 方案闭包 + DP 决策树 + BR + SO；§5 十条 BR；§9 端到端链路）
> - `feature-knowledge/cross-feature-analysis.md`（EV-CA-01，特性→对接面映射）
> - `网元对接doc-list.md`（EV-BS-01，70 篇初始配置文档清单）
> - 7 批主题知识（EV-TK-01~07）、17 特性知识（EV-FK-01~17）

---

## 0. 适用定义与来源

### 0.1 根定义
- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 统一 EV ID 编号（全库一致）
| EV ID | 类型 | 来源 |
|-------|------|------|
| EV-FK-01~17 | 特性知识 | `feature-knowledge/`（17 个 md，已建） |
| EV-TK-01~07 | 主题知识 | `topic-knowledge/Batch-01~07` |
| EV-CA-01 | 横向分析 | `feature-knowledge/cross-feature-analysis.md`（17 引用特性） |
| EV-CA-02 | 横向分析 | `cross-topic-analysis.md`（7 批主题归纳，★主体层） |
| EV-BS-01 | 业务图谱证据 | `网元对接doc-list.md` + 70 篇初始配置流程文档 |

### 0.3 与业务配置类场景（计费/带宽）的差异

| 维度 | 业务配置类（计费/带宽） | 对接类（UPF 网元对接，本场景） |
|------|----------------------|------------------------------|
| CS 组织方式 | 按业务能力（基础/计费/带宽/限制） | **按对接面**（CS-ND-01 控制面 / CS-ND-02 用户面 / CS-ND-03 网管 / CS-ND-04 路由 / CS-ND-05 基础就绪） |
| 主体对象 | 业务规则、URR/PCC/RULE 配置块 | **对接方案闭包(CS) + 组网模式决策点(DP)** |
| 特性（Feature）角色 | 业务能力的载体（直接配置对象） | **引用支撑**（为对接方案提供能力，如 GWFD-010234 Single IP 支撑接口抽象） |
| 决策复杂度 | 单一业务路径 | **多维组网矩阵**（硬件 × SDN × IP 版本 × 路由协议 × 部署方式） |
| 第3层 Task 主线 | 业务开通流程 | **开局流程**（CS-5→CS-3→CS-1→CS-2→CS-4→FirstCall 调测） |

---

## 1. BusinessDomain + NetworkScenario

### 1.1 BusinessDomain

| 字段 | 值 |
|------|---|
| `domain_id` | `BD-ND` |
| `domain_name` | `网元对接` |
| `domain_summary` | 将 UDG 这一虚拟网元（扮演 UPF/PGW-U/SGW-U）接入运营商网络并打通端到端会话的开局基础设施对接域，覆盖控制面/用户面/网管/路由/基础就绪五大对接面 |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01` |

> **域边界说明**：BD-ND 与计费域 BD-CH-01、带宽域 BD-BW-01、访问限制域、APN 域独立。本域聚焦"开局对接闭包"，一旦 FirstCall 打通即转入业务配置（计费/带宽/限制）。

### 1.2 NetworkScenario

| 字段 | 值 |
|------|---|
| `scenario_id` | `NS-ND-UPF` |
| `scenario_name` | `UPF 网元对接` |
| `scenario_summary` | UDG 扮演 UPF/PGW-U/SGW-U，通过 N4（控制面 PFCP）、N3/N9（用户面 GTP-U）、N6/SGi（外联 DN）、网管（U2020/MAE）四大对接面接入运营商网络，打通 FirstCall 完成开局 |
| `judgment_basis` | 当部署目标为 UDG 扮演 UPF/PGW-U/SGW-U，需要完成 N4 偶联、用户面业务接口配置、路由对外可达、网管纳管，并验证 FirstCall 时，属于本场景 |
| `typical_outcome` | N4 偶联成功 + 用户面 Saif/Scif/Paif 接口就绪 + 路由负荷分担 + 网管 LST ME 成功 + FirstCall 拨测 `DSP SESSIONINFO` 4 参数正确（APN/RoleType/IPv4 PDP/Session 时间戳） |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-TK-01`, `EV-TK-02`, `EV-TK-03`, `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-TK-07`, `EV-CA-02` |

#### 场景边界

**覆盖范围**：
- 网元：UDG（扮演 UPF / PGW-U / SGW-U 融合角色）
- 对接面：控制面(N4↔SMF/SGW-C/PGW-C) / 用户面(N3/N9/N6↔AN/I-UPF/ULCL/DN) / 网管(U2020/MAE) / 路由(DC-GW/PE/EOR/Server Leaf) / 基础就绪(License/NTP/网元身份)
- 接口：N4(PFCP,3GPP TS 29.244) / Sa-N3-S1-U / Sc-N9c-S5-S-S8-S / Pa-N9a-S5-P-S8-P-S2b-Gn-U-Gp-U / S11-U / SGi/N6 / Nupf(HTTP/SBI)
- 决策矩阵：硬件(无NP卡/NP卡直连PE/网络加速卡直连DC-GW) × 组网(非SDN/SDN) × IP版本(IPv4/IPv6/双栈) × 路由(OSPF/静态/BGP over /MPLS VPN) × 部署(自动/手动)

**不覆盖范围**（相邻场景）：
- 计费场景：URR/PCC/RULE 业务配置（FirstCall 打通后）
- 带宽控制场景：BWM 限速配置
- 访问限制场景：URL 过滤/POLICYTYPE 动作
- APN 业务域：APN/DNN 业务路由与会话管理（本场景仅涉及 APN/DNN 的开局对接配置）

---

## 2. ConfigurationSolution（5 个方案闭包，★按对接面组织）

> **拆分依据**：cross-topic-analysis.md §6（5 个 CS 方案闭包素材）+ §1（5 对接面定位）。
> CS 组织方式：按对接面（区别计费场景按业务能力）。每个 CS 含方案要素 / uses_feature / uses_task / DP / BR / SO。

### 2.1 CS-ND-01 控制面对接方案（N4 ↔ SMF/SGW-C/PGW-C）

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-01` |
| `solution_name` | `控制面对接方案（N4↔SMF）` |
| `solution_summary` | 通过强制合一抽象接口 N4if（唯一，固定 `N4if1/0/0`）建立 UDG 与 SMF/SGW-C/PGW-C 的 N4/Sxa/Sxb 偶联，承载 PFCP 会话（PDR/FAR/QER 规则下发），是 UPF 对接的**唯一必备接口** |
| `design_intent` | 解决"控制面偶联"问题：N4 是 UPF 唯一不可省的接口，其余接口按 UPF 角色动态确认；N4 必备但单独配置不足以建立偶联，必须至少存在一个数据面逻辑接口 IP |
| `core_mechanism_combo` | `VPN_Signaling + N4if 强制合一抽象接口(N4/Sxa/Sxb) + UPF 标识(HostName 全网唯一) + PFCP 会话(PDR/FAR/QER)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-TK-03`, `EV-CA-02` |

**scopes**（§8.6）：
- `network_control`（控制面偶联范围，scope_type=`service_selection`）：N4 偶联范围按 SMF 实例

**participants**（§8.7）：
- UDG/UPF（N4if 端，user_plane，承载 PFCP 数据面）
- SMF/SGW-C/PGW-C（N4 对端，control_plane，PFCP 会话发起方）
- 多 SMF 场景额外 participant：GWFD-020161 CU Full Mesh 全互联拓扑

**uses_feature**：`GWFD-010234`(Single IP,接口抽象合一) / `GWFD-020161`(CU Full Mesh,多 SMF 对接) / `GWFD-010105`(用户面地址分配,N4 会话与地址分配联动)
**uses_task**：T-ND-07 配置 N4 控制面接口(含 N4 VPN 实例+N4if 合一逻辑接口 N4if1/0/0+SET UPINFO:HOSTNAME+N4 偶联验证 SRVPING/SRVTRACERT/DSP ROUTE)
**constrained_by**：`BR-ND-01`(N4 必备性) / `BR-ND-02`(接口强制合一) / `BR-ND-03`(VPN 四统一)
**uses_semantic_object**：`SO-ND-01`(N4if 接口) / `SO-ND-09`(VPN_Signaling) / `SO-ND-21`(UPF 标识) / `SO-ND-22`(PFCP 会话)

---

### 2.2 CS-ND-02 用户面对接方案（N3/N9/N6 + 会话接入）

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-02` |
| `solution_name` | `用户面对接方案（N3/N9/N6+会话接入）` |
| `solution_summary` | 按 UDG 部署位置（边缘 ULCL/BP/I-UPF / 锚点 PSA / 融合 / NB-IoT / NWDAF）配置接入侧(Saif)、中间侧(Scif)、锚点侧(Paif 强制合一)业务逻辑接口 + SGi/N6 外联口 + APN/DNN + 地址池三件套 + 地址分配规则，双层结构（接口层 + 会话接入层）打通用户面 |
| `design_intent` | 解决"用户面业务接口 + 会话接入闭环"问题：接口层保证 GTP-U 隧道可达，会话接入层保证 UE 能成功激活接入 PDN/DN 并分配 IP |
| `core_mechanism_combo` | `业务面 VPN(VPN_Access/Sc/Pa/Internet) + Saif/Scif/Paif 接口(Paif 强制合一) + APN/DNN + 地址池五件套(POOL→SECTION→POOLGROUP→POOLBINDGROUP→POOLGRPMAP) + IPALLOCRULE 三级` |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-TK-03`, `EV-CA-02` |

**scopes**：
- `access_side`（接入侧，scope_type=`access`）：Saif/N3if/S1-uif 按 UPF 角色组合
- `session_anchor`（会话锚点侧，scope_type=`subscription`）：Paif 强制合一 + SGi/N6
- `slice_binding`（切片绑定，scope_type=`slice`）：仅 Saif/N3if 支持 SLICEATTRSW + ADD SNSSAIUPINTF

**participants**：
- UDG/UPF（业务接口端 + 地址分配主体）
- (R)AN（接入侧对端，access_side）
- I-UPF/ULCL（中间侧对端，network_function）
- DN/PDN（外部数据网，external_system）
- SMF/SGW-C/PGW-C（APN/DNN 一致性对端，control_plane）
- UDM（EXTERNAL 地址池场景的 IP 分配主体，control_plane，按需）
- NWDAF（Nupf 服务化接口对端，external_system，按需）

**uses_feature**：`GWFD-010234`(Single IP) / `GWFD-010105`(用户面地址分配) / `GWFD-020421`(基于位置的地址分配) / `IPFD-010001`(接口管理)
**uses_task**：T-ND-08 配置业务用户面接口(业务面 VPN+接入侧 Saif/N3if/S1-uif 含切片+中间侧 Scif/N9cif/S5-Sif+锚点侧 Paif 强制合一+(按需)Nupf 服务化接口) / T-ND-09 配置会话接入(APN/DNN+地址池三件套 POOL→SECTION→POOLGROUP→POOLBINDGROUP→POOLGRPMAP+IPALLOCRULE)
**constrained_by**：`BR-ND-02`(接口强制合一) / `BR-ND-03`(VPN 四统一) / `BR-ND-04`(跨域协同)
**uses_semantic_object**：`SO-ND-02`(Saif) / `SO-ND-03`(Scif) / `SO-ND-04`(Paif) / `SO-ND-05`(外联口 SGi/N6) / `SO-ND-06`(Nupf) / `SO-ND-15`(APN/DNN) / `SO-ND-16~20`(地址池五件套+分配规则)

---

### 2.3 CS-ND-03 网管对接方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-03` |
| `solution_name` | `网管对接方案` |
| `solution_summary` | 通过 5 步闭包（重置北向密码 → 重置 SNMP 密钥 → 安装适配层 → 创建网元 14 参数 → EMS 归属检查 → LST ME 验证）完成 UDG 与 U2020/MAE 网管的对接，是开局对接调测的起点（CS-5 基础就绪之后） |
| `design_intent` | 解决"网管纳管"问题：UDG 必须被网管纳管才能进入可视化运维，密码三元组（北向必须重置 + SNMP 共享认证/加密密钥必须重置且不相同）是开局最常见对接失败原因 |
| `core_mechanism_combo` | `北向对接用户(重置密码) + SNMP 用户(重置共享认证/加密密钥且不相同) + 网管适配层 + 网元 14 参数(名称/IP/TLS/OSS 认证/emscomm/SNMPv3/端口 8000/SHA512+AES256) + EMS 归属` |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-TK-02`, `EV-CA-02` |

**scopes**：
- `mgmt_access`（网管纳管范围，scope_type=`service_selection`）：UDG 网元实例

**participants**：
- U2020/MAE（网管系统，external_system，网元创建者）
- UDG（被管网元，network_function）
- OM Portal（北向/SNMP 帐号管理入口，network_function）
- VNF LCM（独立部署时的 EMS 归属管理，external_system，按需）

**uses_feature**：`NPFD-010000`(操作维护功能) / `NPFD-010014`(支持 NTP 功能,间接关联基础)
**uses_task**：T-ND-06 配置网元和网管对接(5 步闭包:重置北向对接用户密码→重置 SNMP 用户共享认证/加密密钥→安装网管适配层→创建 UDG 网元 14 参数→(仅 VNF LCM 独立部署)检查 EMS 归属→验证 LST ME)
**constrained_by**：`BR-ND-06`(密码三元组) / `BR-ND-05`(CS-5→CS-3 回流)
**uses_semantic_object**：`SO-ND-23`(北向用户) / `SO-ND-24`(SNMP 用户) / `SO-ND-25`(网管适配层) / `SO-ND-26`(被管网元 14 参数) / `SO-ND-27`(EMS 归属)

---

### 2.4 CS-ND-04 路由对接方案（★最大最复杂，含组网模式决策树）

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-04` |
| `solution_name` | `路由对接方案（含组网模式决策树）` |
| `solution_summary` | 通过 5 层共性结构（VPN 实例 → 全局使能 → 路由协议 → 外联口 → 部署开关驱动）+ 组网模式 5 维决策矩阵（硬件 × SDN × 部署 × 路由协议 × IP 版本 + 隧道叠加），完成 UDG 与 DC-GW/PE/EOR/Server Leaf 的对外可达 + 负荷分担。CS-4 是图谱最大最复杂的方案闭包 |
| `design_intent` | 解决"对外可达 + 负荷分担"问题：用户下行路由发布(wlr)依赖路由协议承载；不同硬件/组网/部署方式组合决定命令路径（自动部署 AUTOSCALING 模板族 vs 手动部署逐条 MML）；MPLS VPN 是唯一独立成轨的进阶方案 |
| `core_mechanism_combo` | `VPN 实例 + 路由协议(OSPF/静态/BGP over IGP) + BFD 检测(双向/单臂) + 外联口(子接口/主接口/Eth-trunk) + 自动部署模板族(8 个 AUTOSCALING) / 手动部署逐条 MML + 隧道叠加(IPsec/GRE/MPLS VPN)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-TK-07`, `EV-CA-02` |

**scopes**：
- `external_routing`（对外路由范围，scope_type=`service_selection`）：UDG↔DC-GW/PE/EOR/Server Leaf
- `dual_stack`（双栈范围，scope_type=`other`）：IPv4/IPv6/IPv4v6 双栈分别配置
- `tunnel_overlay`（隧道叠加范围，scope_type=`other`）：IPsec/GRE/MPLS VPN 按业务需求

**participants**：
- UDG（VNF 侧路由端，user_plane）
- DC-GW（数据中心网关，network_function，非 SDN/SDN 通用对端）
- PE（运营商边缘路由器，network_function，NP 卡直连 PE 场景对端）
- EOR（Leaf-Spine 的 Server Leaf，network_function，SDN 场景对端）
- SDN 控制器（统一纳管 DC-GW/Spine/Leaf，external_system，SDN 场景）
- NFVO（直接部署 VNF，external_system，SDN 场景替代 VNFM）

**uses_feature**：`IPFD-014000`(路由功能,目录) / `IPFD-014001`(OSPF) / `IPFD-014002`(BGP) / `IPFD-014003`(静态路由) / `IPFD-012003`(BFD) / `GWFD-020411`(MPLS VPN) / `IPFD-015004`(IPsec) / `IPFD-010001`(接口管理,MTU/外联口基础)
**uses_task**（按路由协议/部署方式拆为可复用原子，自动轨 A*/手动轨 M* 的差异由 T-ND-11 外联口自动部署开关 + 04 层 CommandRule 表达）：
- T-ND-10 配置 VPN 实例与接口绑定（自动/手动均需，VPN 实例+地址族+IPBINDVPN）
- T-ND-11 外联口自动部署（自动轨: SET AUTOCONFIG 开关+AUTOSCALING 模板族 ETHTRUNK/SERVICE/BFD/SRROUTE/MPLS；手动轨由 T-ND-10/15 等承接）
- T-ND-12 配置 OSPF（OSPF/OSPFv3，自动轨 AUTOSCALING vs 手动逐条）
- T-ND-13 配置 BGP（BGP over OSPF/静态，含 Loopback+IMPORTROUTE=wlr）
- T-ND-14 配置静态路由（自动 AUTOSCALINGSRROUTE / 手动 ADD SRROUTE）
- T-ND-15 配置 BFD（双向 BFD / 单臂 BFD Echo；自动 AUTOSCALINGBFD / 手动 ADD BFDSESSION）
- T-ND-16 配置隧道（IPsec/GRE/MPLS VPN；MPLS 含手动 ADD MPLSIF）
- T-ND-17 配置 NP 卡级联口（仅 NP100 多框级联: ADD NPDIRECTCONNECTPORT）
- T-ND-18 整网调测 FirstCall（NGPING/DSP SESSIONINFO 等，承接全部 CS 对接完成后）
**constrained_by**：`BR-ND-07`(BGP 依赖 IGP) / `BR-ND-08`(MPLS VPN 公私分离) / `BR-ND-09`(自动部署开关规范) / `BR-ND-10`(MTU 层级)
**uses_semantic_object**：`SO-ND-09`(VPN 实例) / `SO-ND-10`(OSPF 进程/区域) / `SO-ND-11`(静态路由) / `SO-ND-12`(BFD 会话) / `SO-ND-13`(BGP 三件套) / `SO-ND-14`(MPLS 全局/接口) / `SO-ND-05`(外联口) / `SO-ND-28`(Loopback) / `SO-ND-29`(自动部署模板) / `SO-ND-30~32`(隧道 IPsec/GRE/MPLS) / `SO-ND-33`(NP 级联口) / `SO-ND-34`(组网模式)

---

### 2.5 CS-ND-05 基础就绪方案（License + 基础数据 + 架构认知，开局第 1 步）

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-ND-05` |
| `solution_name` | `基础就绪方案（License + 基础数据 + 架构认知）` |
| `solution_summary` | 开局第 1 步全局前置方案，包含架构认知（双模部署/UPF 角色/抽象接口映射）、License 加载（双路径 OM Portal/U2020-MAE）、NTP 时间同步（双路）、网元基本信息、高危命令二次授权（13 类清单）、公共参数（11 项）、MTU 三层调整 |
| `design_intent` | 解决"开局前置就绪"问题：所有后续对接面（CS-1~CS-4）都依赖基础就绪；CS-5 决策（架构模式/部署形态/UPF 角色/接口抽象策略）决定下游接口集与对接路径 |
| `core_mechanism_combo` | `架构认知(双模/UPF 角色/抽象接口) + License 双路径(OM Portal/U2020-MAE) + NTP 双路(OMC+FusionStage) + 网元身份(MOD ME/SET OMIP) + 二次授权(SET SECAUTH+13 类清单) + 公共参数 11 项 + MTU 三层(Fabric/Tunnel/外联口)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-TK-01`, `EV-TK-02`, `EV-CA-02` |

**scopes**：
- `global_bootstrap`（全局前置范围，scope_type=`other`）：开局第 1 步，全局生效

**participants**：
- UDG（被配置网元，network_function）
- OM Portal（License 加载 + 网元信息 + 二次授权入口，network_function）
- U2020/MAE（License 加载路径 2，external_system）
- OMC（NTP 时间源 1，external_system）
- FusionStage（NTP 时间源 2，external_system）

**uses_feature**：`NPFD-010014`(支持 NTP 功能) / `IPFD-010001`(接口管理,MTU 修改/外联口基础)
**uses_task**：T-ND-01 加载 License(DP-CS5-06 决策路径) / T-ND-02 NTP 双路时间同步 / T-ND-03 修改网元基本信息(MOD ME/SET OMIP,注意触发 CS-3 回流) / T-ND-04 配置公共参数含 MTU 三层(11 项公共参数+Fabric/外联口 MTU+自动部署模板同步) / T-ND-05 高危命令二次授权(SET SECAUTH+ADD USRSECAUTH)
> **注**：架构认知确认（原 T-CS5-07）属 DecisionPoint 范畴（DP-CS5-01~04），不单列 task；其影响通过 DP selects 关系边表达。
**constrained_by**：`BR-ND-01`(N4 必备性,架构认知约束) / `BR-ND-10`(MTU 层级) / `BR-ND-05`(CS-5→CS-3 回流)
**uses_semantic_object**：`SO-ND-35`(部署形态) / `SO-ND-36`(UPF 角色) / `SO-ND-37`(抽象接口映射) / `SO-ND-38`(License) / `SO-ND-39`(NTP 时间源) / `SO-ND-40`(网元身份) / `SO-ND-41`(二次授权) / `SO-ND-42`(公共参数 11 项) / `SO-ND-43`(MTU 三层)

---

## 3. DecisionPoint（27 个，组网模式决策树）

> **数据来源**：cross-topic-analysis.md §6.4（CS-4 组网模式 5 维决策树）+ §6.5（CS-5 架构认知）+ §6.1~6.3（CS-1/2/3 各自决策点）。
> **★Schema §8.8 必选字段统一声明（U-H-02 修复）**：本节 27 个 DecisionPoint 的 3 个公共必选字段统一取值，不在每行重复，特此声明：
> - `owner_layer` = `business`（全部 27 个 DP，业务层决策点）
> - `owner_ref_type` = `ConfigurationSolution`（全部 27 个 DP，归属对接方案闭包）
> - `status` = `active`（全部 27 个 DP）
> - `owner_ref` = 各 DP 对应的 CS-ND-XX（已在表中 `owner_ref` 列显式标注）

### 3.1 CS-5 基础就绪决策点（7 个，DP-CS5-01~07）

| `decision_id` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `source_evidence_ids` |
|---------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------------------|
| `DP-CS5-01` | `CS-ND-05` | 架构模式 | 当前网络是 5G SA 独立还是 2/3/4/5G 互操作融合？ | `["5G SA 独立","2/3/4/5G 互操作融合"]` | 开局架构认知第 1 步 | 决定 UDG 是否承担 PGW-U/SGW-U，影响 CS-1/CS-2 全部接口集 | `EV-TK-01`, `EV-CA-02` |
| `DP-CS5-02` | `CS-ND-05` | UDG 部署形态 | UDG 部署为独立 UPF / UPF+PGW-U / UPF+SGW-U+PGW-U 三种形态中的哪种？ | `["UPF 独立","UPF+PGW-U","UPF+SGW-U+PGW-U"]` | 架构模式确定后 | 决定 CS-2 可配置接口范围（独立 UPF 仅 N3/N9/N6；融合需 Paif+SGi 等） | `EV-TK-01`, `EV-CA-02` |
| `DP-CS5-03` | `CS-ND-05` | UPF 角色 | UPF 担任 PSA / ULCL / BP / I-UPF / 多角色共建中的哪种？ | `["PSA","ULCL","BP","I-UPF","多角色共建"]` | 部署形态确定后 | 决定 CS-2 N3/N9a/N9c/N6 接口组合（如 ULCL+本地 PSA 共建需 5 接口） | `EV-TK-01`, `EV-CA-02` |
| `DP-CS5-04` | `CS-ND-05` | 接口抽象策略 | 业务接口采用独立接口还是抽象接口合一？ | `["独立接口","抽象接口合一"]` | 角色确定后（4G/5G 隔离→独立；融合→抽象；Paif/N4if 强制抽象） | 决定 CS-1/CS-2 接口配置路径（Saif vs N3if/S1-uif；Paif/N4if 强制抽象） | `EV-TK-01`, `EV-CA-02` |
| `DP-CS5-05` | `CS-ND-05` | 路由方案 | CS-4 路由对接采用哪种基础组合（影响下游 CS-4 命令路径）？ | `["IPv4×OSPF","IPv6×OSPFv3","IPv4v6×OSPF 双栈","IPv4×静态","IPv6×静态","IPv4v6×BGP over 静态"]` | 进入 CS-4 前 | 影响 CS-4 全部命令路径与 BFD 模式选择 | `EV-TK-04`, `EV-TK-07`, `EV-CA-02` |
| `DP-CS5-06` | `CS-ND-05` | License 加载路径 | 通过 OM Portal 还是 U2020/MAE 加载 License？ | `["OM Portal(仅网元)","U2020/MAE(网元+Service Fabric)"]` | License 加载时 | OM Portal 仅加载网元 License；U2020/MAE 额外加载 Service Fabric License（上传即生效） | `EV-TK-01`, `EV-CA-02` |
| `DP-CS5-07` | `CS-ND-05` | License 文件格式 | License 文件采用 dat(2.0) 还是 xml(3.0)？ | `["dat(2.0)","xml(3.0)"]` | License 加载时 | 影响上传命令格式与激活流程 | `EV-TK-01`, `EV-CA-02` |

### 3.2 CS-4 路由对接组网模式决策点（7 个，DP-CS4-01~07，★核心决策树）

| `decision_id` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `source_evidence_ids` |
|---------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------------------|
| `DP-CS4-01` | `CS-ND-04` | 硬件类型 | UDG 采用哪种硬件形态接入？ | `["无 NP 卡标卡(Ethernet66/0/X)","NP 卡直连 PE(NP100 有级联 P3/P4 / NP121 自适应无级联)","网络加速卡直连 DC-GW(NP100/NP121)"]` | CS-4 第 1 维决策 | 无 NP 卡：全路由协议+自动/手动均可；NP 卡直连 PE：不支持自动部署+不支持 SDN；网络加速卡：强制 SR-IOV bonding+LACP+仅 BGP over 静态+BFD 单臂 Echo | `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-CA-02` |
| `DP-CS4-02` | `CS-ND-04` | 组网架构（SDN vs 非 SDN） | 采用 SDN（Leaf-Spine+NFVO+SDN 控制器）还是非 SDN 组网？ | `["非 SDN-三层/二层(DC-GW 作 L3GW)","非 SDN-二层/一层(DC-GW 作 L3GW+L2GW)","SDN(Leaf-Spine+NFVO+SDN 控制器)"]` | CS-4 第 2 维决策 | 非 SDN：全路由类型(OSPF/静态/BGP/MPLS)；二层/一层禁用 OSPF(环路)；SDN：不支持 OSPF+强制 DHCP+强制单臂 BFD Echo(DEST=Leaf IP)+仅 BGP over 静态/BGP MPLS VPN+VPN 命名 VRF_* | `EV-TK-04`, `EV-TK-06`, `EV-CA-02` |
| `DP-CS4-03` | `CS-ND-04` | 部署方式 | 采用自动部署（推荐）还是手动部署？ | `["自动部署(推荐,无 NP 卡/SDN/网络加速卡)","手动部署(NP 卡直连 PE 必选/自动失败补救/手动调测)"]` | CS-4 第 3 维决策 | 自动：AUTOSCALING 模板族+SET AUTOCONFIG 开关，部署完成后无法自动修改/删除，扩容零人工；手动：逐条 MOD/ADD INTERFACE+ADD MPLSIF(MPLS 关键差异)，MPLS 场景扩容需手工补 | `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-CA-02` |
| `DP-CS4-04` | `CS-ND-04` | 路由协议 × IP 版本 | 采用哪种路由协议 × IP 版本组合（6 种基础 + 3 种隧道）？ | `["OSPF×IPv4","OSPFv3×IPv6","OSPF/OSPFv3×双栈","静态×IPv4","静态×IPv6","静态×双栈","BGP over OSPF/静态×IPv4","BGP over OSPFv3/静态×IPv6","BGP over×双栈","IPsec 隧道","GRE 隧道","MPLS VPN"]` | CS-4 第 4 维决策 | 决定 VPN 地址族(ipv4uni/ipv6uni/双)、OSPF 进程类型(OSPF/OSPFv3)、Loopback 是否配(NSSA 自动选 FA)、地址段 SECTION 字段、BGP 对等体 ADDRESSTYPE、逻辑接口 IPVERSION | `EV-TK-04`, `EV-TK-05`, `EV-CA-02` |
| `DP-CS4-05` | `CS-ND-04` | BFD 模式 | 采用双向 BFD 还是单臂 BFD Echo？ | `["双向 BFD(ADD AUTOSCALINGSRBFD 或 ADD BFDSESSION 双臂)","单臂 BFD Echo(ADD AUTOSCALINGBFD ONEARMECHO=TRUE 或 ADD BFDSESSION ONEARMECHO=TRUE)"]` | CS-4 第 5 维决策 | 双向：非 SDN OSPF/静态场景；单臂：SDN 强制 / 网络加速卡强制 / DC-GW 双活网关·M-LAG 强制（DEST=Leaf IP） | `EV-TK-04`, `EV-TK-06`, `EV-CA-02` |
| `DP-CS4-06` | `CS-ND-04` | 外联口形态 | 外联口采用子接口、主接口还是 Eth-trunk？ | `["子接口(推荐,自动部署主路径)","主接口","Eth-trunk: 非 SR-IOV(VNIC)","Eth-trunk: SR-IOV bonding(ETHTRUNK,ADD AUTOSCALINGETHTRUNK)"]` | CS-4 第 6 维决策 | 影响外联口配置命令路径；网络加速卡场景强制 SR-IOV bonding+LACP(DC-GW 必须 active) | `EV-TK-04`, `EV-TK-05`, `EV-CA-02` |
| `DP-CS4-07` | `CS-ND-04` | 隧道叠加 | 是否叠加隧道（IPsec/GRE/MPLS VPN）？ | `["无(基础 6 种方案)","IPsec(跨安全域加密)","GRE(WAP 访问 PDN/DN)","MPLS VPN(UDG 作 PE 对接企业网,OptionB 跨域)"]` | CS-4 第 7 维决策（按业务需求） | IPsec 跨安全域信令/数据；GRE 基于 Loopback 对接 WAP 网关；MPLS VPN 外联口绑 _public_+VRFRD+perInstance/perNexthop 节省标签 | `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-CA-02` |

### 3.3 CS-1 / CS-2 / CS-3 决策点（7 个）

| `decision_id` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `source_evidence_ids` |
|---------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------------------|
| `DP-CS1-01` | `CS-ND-01` | N4 IP 版本 | N4 接口采用哪种 IP 版本？ | `["IPv4","IPv6","IPv4v6 双栈"]` | 配置 N4if 时 | 决定 LOGICINF 的 IPVERSION 取值(IPV4/IPV6/IPVER_ALL) | `EV-TK-03`, `EV-CA-02` |
| `DP-CS1-02` | `CS-ND-01` | 多 SMF 对接 | 是否需要 UDG 对接多个 SMF？ | `["单 SMF(默认)","多 SMF"]` | N4 组网规划时 | 多 SMF 需启用 GWFD-020161 CU Full Mesh+申请 License LKV3G5CUFM01 | `EV-TK-03`, `EV-CA-02` |
| `DP-CS2-01` | `CS-ND-02` | UPF 角色→接口组合 | UPF 角色决定哪些用户面接口组合？ | `["边缘 ULCL/BP/I-UPF(Saif+Scif)","锚点 PSA(Paif+SGi/N6)","融合(Saif+Scif+Paif+SGi/N6)","NB-IoT SGW-U(+S11-uif)","NWDAF 对接(+Nupf)"]` | 配置用户面前 | 决定 CS-2 接口配置范围（边缘 2 接口 / 锚点 2 接口 / 融合 4 接口 / NB-IoT 附加 / NWDAF 附加） | `EV-TK-03`, `EV-CA-02` |
| `DP-CS2-02` | `CS-ND-02` | 用户面 IP 版本 | 用户面接口采用哪种 IP 版本？ | `["IPv4","IPv6","IPv4v6 双栈"]` | 配置业务接口时 | 决定 VPN 地址族、逻辑接口 IPVERSION、地址段 SECTION 字段、APN HASVPN/HASVPNIPV6 | `EV-TK-03`, `EV-CA-02` |
| `DP-CS2-03` | `CS-ND-02` | Sa/Sc 合一 vs 独立 | 接入侧/中间侧采用 Saif/Scif 合一还是 N3if/S1-uif/N9cif/S5-Sif 独立？ | `["Saif/Scif 合一(推荐)","N3if/S1-uif/N9cif/S5-Sif 独立"]` | 配置接入/中间侧接口时 | 合一与独立互斥；推荐合一简化（Paif 强制合一不受此决策影响） | `EV-TK-03`, `EV-CA-02` |
| `DP-CS2-04` | `CS-ND-02` | 接入侧切片绑定 | 是否启用 Saif/N3if 切片绑定？ | `["启用(SLICEATTRSW=ENABLE+ADD SNSSAIUPINTF)","不启用"]` | 5G 切片场景 | 仅 Saif/N3if 支持切片绑定，决定是否附加 ADD SNSSAIUPINTF | `EV-TK-03`, `EV-CA-02` |
| `DP-CS2-05` | `CS-ND-02` | 地址分配主体 | IP 由 UDG 本地分配还是外部 NF 分配？ | `["LOCAL(UDG 主锚点分配,需完整三件套)","EXTERNAL(辅锚点/ULCL/外部 NF 如 UDM 分配,仅 POOL+SECTION,可选 CHECKIPVALID)"]` | 配置地址池时 | LOCAL 需完整 POOL→SECTION→POOLGROUP→POOLBINDGROUP→POOLGRPMAP；EXTERNAL 仅 POOL+SECTION | `EV-TK-03`, `EV-CA-02` |
| `DP-CS2-06` | `CS-ND-02` | 地址分配维度 | 地址分配按哪个维度？ | `["APN(默认)","SMF","位置(LAC/TAC)"]` | 配置 IPALLOCRULE 时 | 默认仅第一级 APN 维度使能；位置维度需启用 GWFD-020421+License LKV3G5LBAA01 | `EV-TK-03`, `EV-CA-02` |
| `DP-CS2-07` | `CS-ND-02` | 用户下行路由发布 | 用户下行路由(wlr)通过哪种协议发布？ | `["OSPF/OSPFv3 动态","BGP over 静态","纯静态(PROTOCOL=wlr)"]` | 配置用户下行路由时 | 影响路由引入 IMPORTPROTOCOL=wlr 的承载方式 | `EV-TK-03`, `EV-TK-04`, `EV-CA-02` |
| `DP-CS2-08` | `CS-ND-02` | DN-AAA 互通 | DN-AAA 互通采用方案 A 还是方案 B？ | `["方案 A:N6 直连","方案 B:N4 专用会话(不占 License)"]` | DN-AAA 互通场景 | 方案 A 走 N6 物理直连；方案 B 走 N4 专用会话（需 SSU+SBIM 服务） | `EV-TK-03`, `EV-CA-02` |
| `DP-CS3-01` | `CS-ND-03` | 认证模式×协议版本×加密协议 | 网管对接认证与加密组合？ | `["OSS 证书/匿名 × SNMPv3(推荐) × SHA512(推荐)+AES256(推荐)","SHA(不安全,告警 ALM-136750)"]` | 创建网元时 | 决定网元 14 参数中的 OSS 认证/SNMPv3/授权加密字段；SHA 不安全会告警 | `EV-TK-02`, `EV-CA-02` |
| `DP-CS3-02` | `CS-ND-03` | VNF LCM 部署形态×适配层时序 | VNF LCM 部署形态决定适配层时序？ | `["独立+已装+选 EMS=跳过","独立+未装+选 EMS=仅装适配层","合设=完整 5 步"]` | 创建网元时 | 决定 5 步闭包的执行范围（完整 5 步 / 仅装适配层 / 跳过） | `EV-TK-02`, `EV-CA-02` |
| `DP-CS3-03` | `CS-ND-03` | 证书更新路径 | 证书更新走 LiteCA 自动还是手动？ | `["LiteCA 自动(5 前置)","手动(4 类证书场景不支持自动更新)"]` | 证书场景 | LiteCA 自动需 5 前置；4 类证书场景必须手动更新 | `EV-TK-02`, `EV-CA-02` |

> **DP 计数**：CS-5(7) + CS-4(7) + CS-1(2) + CS-2(8) + CS-3(3) = **27 个**。其中 CS-2 含 8 个子决策（DP-CS2-01~08），是最细粒度的对接面；CS-4 组网模式 5 维决策树（DP-CS4-01~07）是图谱最复杂的决策结构。

---

## 4. BusinessRule（10 条）

> **数据来源**：cross-topic-analysis.md §5（10 条核心规则）。
> **rule_type 枚举**（Schema §8.9）：`selection_rule` / `scope_rule` / `design_rule` / `acceptance_rule` / `diagnosis_rule`。
> **rule_expression_mode**：`explicit` / `implicit`。
> **rule_source_kind**：`principle` / `config` / `design` / `ops` / `case` / `restriction`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` |
|-----------|-------------|-------------|------------------------|--------------------|--------------|---------------------|----------|----------------------|
| `BR-ND-01` | N4 必备性原则 | `selection_rule` | `explicit` | `principle` | UPF 对接时 N4 是**唯一必配接口**，其余接口按 UPF 角色(PSA/ULCL/BP/I-UPF)和位置动态确认；N4 单独配置不足以建立偶联，UDG 上**至少需存在一个数据面逻辑接口 IP**(Paif/Scif/Saif/N3if/S1-uif/S11-uif 任一)；多 SMF 对接需额外配置 GWFD-020161 CU Full Mesh 特性并申请 License。位置决定接口集：ULCL+本地 PSA 共建=N3+N4+N9c+N9a+N6 五接口；拆分 ULCL=N3+N4+N9c；拆分 PSA=N4+N9a+N6 | N4 缺失或仅配 N4 无数据面接口→偶联建立失败，开局卡死 | `active` | `EV-TK-01`, `EV-TK-03`, `EV-CA-02` |
| `BR-ND-02` | Paif/N4if 强制合一原则 | `design_rule` | `explicit` | `principle` | 因 4G/5G 互操作时移动锚点不变、协议相同，**Paif 和 N4if 不支持独立配置**，只能使用合一抽象接口：N4if(N4/Sxa/Sxb 强制合一,TS 29.244 协议相同) + Paif(N9a/S5-P/S8-P/S2b/Gn-U/Gp-U 强制合一,数据锚点不变地址必须相同)。对比：Saif(Sa/N3/S1-U)和 Scif(Sc/N9c/S5-S/S8-S)**可选合一**，与独立配置互斥 | 选错（Paif/N4if 配独立接口）→接口配置失败；Saif/Scif 同时配合一与独立→互斥冲突 | `active` | `EV-TK-01`, `EV-TK-03`, `EV-CA-02` |
| `BR-ND-03` | VPN 四统一原则 | `scope_rule` | `explicit` | `config` | 业务 APN 绑定 VPN、地址池绑定 VPN、Gi/SGi/N6 外联口绑定 VPN、各业务逻辑接口绑定 VPN —— **四者必须一致**（VPN_Access/VPN_Sc/VPN_Pa/VPN_Internet/VPN_Signaling 按业务面对齐）；逻辑接口 IP **不能**与外联口 IP 同网段，也**不能**与对端物理接口 IP 同网段 | VPN 不一致→业务流量跨 VPN 串扰或路由不通；网段冲突→接口配置失败 | `active` | `EV-TK-03`, `EV-CA-02` |
| `BR-ND-04` | 接口↔路由↔会话接入跨域协同 | `design_rule` | `implicit` | `design` | 逻辑接口绑定 VPN 必须与对应外联口 VPN 一致（路由侧规划）；用户下行路由发布(wlr 协议标识)依赖路由协议承载；N4 偶联成功需数据面逻辑接口存在；UDG 用 Saif 抽象接口(N3 与 S1-U IP 合一)时若无线侧 NG-U 与 S1-U IP 也合一，无线侧要求两者配在**同一用户面 EPGROUP**（跨设备协同约束） | 跨域不一致→偶联失败/下行路由不通/无线侧协同失败 | `active` | `EV-TK-03`, `EV-CA-02` |
| `BR-ND-05` | CS-5→CS-3 回流约束 | `runtime_check_rule` | `explicit` | `ops` | 修改浮动 IP(SET OMIP)会**中断网管和 VNFM 连接**，必须重对接网管(CS-3 完整 5 步重跑)。SET OMIP 本身是默认二次授权命令，需先完成二次授权配置。三者形成串行链：`二次授权配置(CS-5)→修改网元信息(CS-5)→重对接网管(CS-3)` | 未回流重对接→网管失联；未先二次授权→SET OMIP 弹窗阻塞 | `active` | `EV-TK-02`, `EV-CA-02` |
| `BR-ND-06` | 网管对接密码三元组 | `acceptance_rule` | `explicit` | `config` | CS-3 网管对接 3 类帐号中后两类有严格初次对接密码约束：**北向对接用户必须重置密码**；**SNMP 用户必须重置共享认证密钥和共享加密密钥，且两者不能相同**；任何一项不满足对接直接失败（开局最常见对接失败原因） | 密码未重置/共享认证与加密相同→对接直接失败 | `active` | `EV-TK-02`, `EV-CA-02` |
| `BR-ND-07` | BGP 依赖 IGP 原则 | `design_rule` | `explicit` | `design` | BGP 是"寄生"协议：**自身无自动部署**，依赖 OSPF/静态路由的 IGP 自动部署基础；**自身不能发现路由**，必须 ADD IMPORTROUTE:IMPORTPROTOCOL=wlr 引入；BGP 需专用 Loopback 接口(与 IGP 外联口同 VPN)，建立 eBGP 邻居(EBGPMAXHOP=10)；DC-GW 双活网关/M-LAG 场景**只支持 BGP over 静态路由+BFD 单臂 echo，不支持 OSPF** | 未配 IGP/Loopback→BGP 邻居无法建立；双活网关配 OSPF→不支持 | `active` | `EV-TK-04`, `EV-TK-06`, `EV-CA-02` |
| `BR-ND-08` | MPLS VPN 公私分离原则 | `scope_rule` | `explicit` | `design` | MPLS VPN 独特架构：外联口 VPN 固定 `_public_`(不绑业务 VPN)；**不配置 IPv6 外联口**(MP-EBGP 用 IPv4 eBGP 传 IPv6 私网路由)；Loopback 接口**不绑 VPN**(用公网 BGP 传私网路由)；**必须配 VRFRD**(路由标识)，不同 VPN 实例不能重复；MP-EBGP 开关=ADD BGPVRFAF:VRFNAME="_public_",AFTYPE=ipv4vpn；标签节省组合：VPN 侧 VRFLABELMODE=perInstance + BGP 侧 APPLYLABELMODE=perNexthop | 外联口绑业务 VPN/配 IPv6 外联口/Loopback 绑 VPN/VRFRD 重复→MPLS VPN 路由不通或标签浪费 | `active` | `EV-TK-04`, `EV-CA-02` |
| `BR-ND-09` | 自动部署开关操作规范 | `runtime_check_rule` | `explicit` | `ops` | 自动部署开关操作必须遵循顺序：`LST AUTOCONFIG → DSP OPSASSISTSTATE(确保 autoscaling_autoconfig.py 为 Ready) → SET AUTOCONFIG:SWITCHFLAG=FALSE(关) → 配置所有 AUTOSCALING* 模板 → SET AUTOCONFIG:SWITCHFLAG=TRUE(开) → DSP OPSASSISTSTATE(确认 Ready 后再做其他操作)`。部署完成后**无法自动修改/删除**已部署配置，需手动：关开关→删子接口→改模板→重开开关。仅修改接口 MTU 不同步 MOD AUTOSCALINGSERVICE 会触发告警 ALM-232398849 | 开关时序错误/助手非 Ready→自动部署失败或部分配置不生效；模板不可变→扩容隐患 | `active` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-CA-02` |
| `BR-ND-10` | MTU 层级约束 | `scope_rule` | `explicit` | `config` | MTU 层级：**网卡 MTU ≥ Fabric MTU > 主接口 MTU ≥ 子接口 MTU**(建议子接口与主接口一致)；外联口 MTU 必须与直连下一跳网关(DCGW/路由器)一致，默认 1500；IPv6 分片联动：SET IPV6FRAGPLCY:INNERIPV6FRAGPLCY 初始值 TOOBIG_PKTDROP 在 MTU 偏小时丢包，业务稳定需改 OUTERFRAG；Eth-trunk 不修改成员接口 MTU，成员接口加入 Eth-trunk 前修改 MTU 会导致添加失败 | MTU 不对齐→丢包/分片异常；Eth-trunk 成员 MTU 改后加入失败 | `active` | `EV-TK-02`, `EV-CA-02` |

> **rule_type 分布**：selection_rule(1) + design_rule(3) + scope_rule(3) + acceptance_rule(1) + runtime_check_rule(2) + diagnosis_rule(0)。
> **注（U-M-01 处理，选项 B）**：Schema §8.9 枚举为 5 类（selection_rule/scope_rule/design_rule/acceptance_rule/diagnosis_rule），BR-ND-05/09 沿用计费标杆 BR-CH-08/14 的 `runtime_check_rule` 类型作为**本场景扩展枚举**（运行时检查规则，与 ops 来源对齐），等 Schema 升级时合并入正式枚举。此项与计费标杆保持一致，非阻断。

---

## 5. SemanticObject（43 个，跨层共享语义桥接对象）

> **数据来源**：cross-topic-analysis.md §3（共性机制）+ §6（5 CS 方案闭包语义对象）。
> **Schema §8.10**：semantic_object_id / semantic_object_name / semantic_summary / semantic_layer_hint / status / source_evidence_ids。
> **跨层关系**：`NetworkScenario/ConfigurationSolution --uses_semantic_object--> SemanticObject`；`SemanticObject --realized_by--> ConfigObject`（ConfigObject 在第4层 04-command-graph 定义）。

### 5.1 抽象接口类（SO-ND-01~08，8 个）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|----------------------|----------------------|
| `SO-ND-01` | N4if 接口 | N4/Sxa/Sxb 强制合一抽象接口（固定 `N4if1/0/0` 唯一），承载 PFCP 会话，CS-1 控制面对接核心 | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-02` | Saif 接口 | Sa/N3/S1-U 可选合一抽象接口（`Saif1/1/0`），接入侧用户面；支持切片绑定 SLICEATTRSW | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-03` | Scif 接口 | Sc/N9c/S5-S/S8-S 可选合一抽象接口（`Scif1/1/0`），中间侧用户面 | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-04` | Paif 接口 | N9a/S5-P/S8-P/S2b/Gn-U/Gp-U **强制合一**抽象接口（`Paif1/1/N`），锚点侧用户面；4G/5G 数据锚点不变 | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-05` | 外联口（SGi/N6/物理外联口） | 对外数据网/路由器的物理接口（子接口/主接口/Eth-trunk），不抽象；CS-2 SGi/N6 + CS-4 外联口共用 | `cross_layer` | `EV-TK-03`, `EV-TK-04`, `EV-CA-02` |
| `SO-ND-06` | Nupf 接口 | 服务化接口（HTTP/SBI），NWDAF 对接场景；需 SSU+SBIM 服务（ADD LOGICIP+HTTPLEGRP+HTTPLE+SBIAPLE） | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-07` | S11-uif 接口 | NB-IoT SGW-U 附加接口（独立，无抽象），对接 MME | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-08` | 接口命名规范 | Saif/Scif/Paif/N4if 抽象接口命名规则（最后位 0~31），强制 vs 可选合一二元性 | `business` | `EV-TK-01`, `EV-CA-02` |

### 5.2 VPN 与路由协议类（SO-ND-09~14，6 个）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|----------------------|----------------------|
| `SO-ND-09` | VPN 实例 | L3VPN 实例 + 地址族（ipv4uni/ipv6uni），业务隔离；VPN_Signaling(CS-1)/VPN_Access·Sc·Pa·Internet(CS-2)/VRF_*(SDN)/`_public_`(MPLS VPN)；四统一约束 | `cross_layer` | `EV-TK-03`, `EV-TK-04`, `EV-CA-02` |
| `SO-ND-10` | OSPF 进程/区域 | OSPF v2/v3 进程 + 区域（含 NSSA 自动选 FA 需 Loopback）；非 SDN 三层/二层架构支持；SDN/二层/一层禁用 | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-11` | 静态路由 | 手工配置目标网段下一跳（PREFIX/NEXTHOP），可绑定 BFD；SDN/非 SDN/NP 卡三类部署均涉及 | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-12` | BFD 会话 | 快速检测链路故障；双向 BFD(非 SDN OSPF/静态) / 单臂 BFD Echo(SDN 强制/网络加速卡强制/DC-GW 双活强制,DEST=Leaf IP)；自动部署 AUTOSCALINGBFD/SRBFD vs 手动 BFDSESSION | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-13` | BGP 三件套 | BGP 实例 + 地址族(VPNv4/IPv4/IPv6) + 对等体(EBGPMAXHOP=10)；"寄生"协议依赖 IGP+IMPORTROUTE+Loopback；MPLS VPN 场景 MP-EBGP | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-14` | MPLS 全局/接口 | MPLS 全局(SET MPLSSITE) + 接口(ADD MPLSIF 手动 / ADD AUTOSCALINGMPLS 自动)；MPLS VPN 独立成轨，自动 vs 手动关键差异（扩容需手工补） | `cross_layer` | `EV-TK-04`, `EV-CA-02` |

### 5.3 会话接入类（SO-ND-15~20，6 个）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|----------------------|----------------------|
| `SO-ND-15` | APN/DNN | 接入点实例，UDG 本端与 C 面(SMF/SGW-C/PGW-C)一致；HASVPN/HASVPNIPV6 绑定业务 VPN | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-16` | 地址池（POOL） | LOCAL(UDG 主锚点分配) / EXTERNAL(辅锚点/ULCL/外部 NF 分配)；CHECKIPVALID 可选 | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-17` | 地址段（SECTION） | V4STARTIP/V4ENDIP 或 V6PREFIXSTART/END/LENGTH=64；双栈 SECTIONNUM=1(v4)+2(v6) | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-18` | 地址池组（POOLGROUP） | 地址池聚合，绑定 POOLBINDGROUP | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-19` | 地址池绑定组（POOLBINDGROUP） | 地址池组绑定关系 | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-20` | 地址分配规则（IPALLOCRULE） | 三级（APN/SMF/位置），默认仅第一级 APN 维度使能；位置维度需 GWFD-020421+License | `cross_layer` | `EV-TK-03`, `EV-CA-02` |

### 5.4 网管对接类（SO-ND-21~27，7 个）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|----------------------|----------------------|
| `SO-ND-21` | UPF 标识 | SET UPINFO:HOSTNAME 全网唯一，N4 偶联身份 | `business` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-22` | PFCP 会话 | 承载 PDR/FAR/QER 规则下发，3GPP TS 29.244 | `cross_layer` | `EV-TK-03`, `EV-CA-02` |
| `SO-ND-23` | 北向对接用户 | 网管北向帐号，初次对接**必须重置密码** | `business` | `EV-TK-02`, `EV-CA-02` |
| `SO-ND-24` | SNMP 用户 | SNMPv3 用户，**必须重置共享认证密钥和共享加密密钥且不相同** | `business` | `EV-TK-02`, `EV-CA-02` |
| `SO-ND-25` | 网管适配层 | 华为支持网站下载版本配套软件，网管侧安装 | `business` | `EV-TK-02`, `EV-CA-02` |
| `SO-ND-26` | 被管网元（14 参数） | 网管侧创建的 UDG 网元：名称/IP/TLS/OSS 认证/emscomm/SNMPv3/端口 8000/SHA512+AES256 | `business` | `EV-TK-02`, `EV-CA-02` |
| `SO-ND-27` | EMS 归属关系 | VNF LCM 独立部署时在 VNFM-EMS 管理检查 | `business` | `EV-TK-02`, `EV-CA-02` |

### 5.5 路由对接扩展类（SO-ND-28~34，7 个）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|----------------------|----------------------|
| `SO-ND-28` | Loopback 接口 | BGP/MPLS 必备（/32 或 /128），与 IGP 外联口同 VPN；MPLS VPN 场景不绑 VPN；BGP IPv4v6 双栈共用一个 ROUTERID | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-29` | 自动部署模板族 | 8 个 AUTOSCALING 模板（ETHTRUNK/SERVICE/BFD/SRBFD/SRROUTE/BGPLF/IPREACH/MPLS），构成自动部署配置对象族 | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-30` | IPsec 隧道 | 跨安全域加密（Sxa/Sxb/N4/S1-U/N3），基于安全联盟 SA | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-31` | GRE 隧道 | PGW-U/UPF↔WAP 网关（N6/SGi），基于 Loopback | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-32` | MPLS VPN 隧道 | UDG 作 PE 对接企业网（OptionB 跨域），外联口 `_public_`，VRFRD 必配 | `cross_layer` | `EV-TK-04`, `EV-CA-02` |
| `SO-ND-33` | NP 卡级联口 | NP100 多框级联（P3/P4 端口），NP121 无级联；ADD NPDIRECTCONNECTPORT | `cross_layer` | `EV-TK-05`, `EV-TK-06`, `EV-CA-02` |
| `SO-ND-34` | 组网模式 | 承载 DP-CS4 决策树结果（硬件×SDN×部署×路由×IP×隧道组合） | `business` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06`, `EV-CA-02` |

### 5.6 基础就绪类（SO-ND-35~43，9 个）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|----------------------|----------------------|
| `SO-ND-35` | 部署形态 | UPF 独立 / UPF+PGW-U / UPF+SGW-U+PGW-U 三态（DP-CS5-02） | `business` | `EV-TK-01`, `EV-CA-02` |
| `SO-ND-36` | UPF 角色 | PSA / ULCL / BP / I-UPF / 多角色共建（DP-CS5-03） | `business` | `EV-TK-01`, `EV-CA-02` |
| `SO-ND-37` | 抽象接口映射 | 3GPP→UDG 抽象接口映射表（Saif/Scif/Paif/N4if 5 组） | `business` | `EV-TK-01`, `EV-CA-02` |
| `SO-ND-38` | License | License 文件 + ESN + 控制项 + 状态机；双路径 OM Portal/U2020-MAE；颜色告警（红/黄/白）；紧急 License 3 次/7 天 | `cross_layer` | `EV-TK-01`, `EV-CA-02` |
| `SO-ND-39` | NTP 时间源 | 双路时间源（OMC + FusionStage），依赖 NPFD-010014 | `cross_layer` | `EV-TK-02`, `EV-CA-02` |
| `SO-ND-40` | 网元身份 | MEID/MENAME/OMIP（MOD ME 改名 + SET OMIP 改浮动/物理 IP） | `business` | `EV-TK-02`, `EV-CA-02` |
| `SO-ND-41` | 二次授权 | SET SECAUTH + ADD USRSECAUTH + ADD SECAUTHMEM；13 类 UDG 默认二次授权命令清单（SET OMIP/MOD VIRTUALIP/SET FWDPARA/IPsec 系列等） | `business` | `EV-TK-02`, `EV-CA-02` |
| `SO-ND-42` | 公共参数 11 项 | SIGDSCP / UDPCHECKSUM / SRVCOMMONPARA / QOSCAR / IPV6FRAGPLCY / CPTEIDUALLOC / TZ / ANTIFRAUD / FWDPARA(高危) / HEADENGLBPARA / MSFAULTALARM | `cross_layer` | `EV-TK-02`, `EV-CA-02` |
| `SO-ND-43` | MTU 三层配置 | Fabric/Tunnel/外联口 三层 MTU；网卡 MTU ≥ Fabric MTU > 主接口 MTU ≥ 子接口 MTU；默认 1500 | `cross_layer` | `EV-TK-02`, `EV-CA-02` |

> **SO 计数**：抽象接口(8) + VPN/路由协议(6) + 会话接入(6) + 网管(7) + 路由扩展(7) + 基础就绪(9) = **43 个**。

---

## 6. 业务图谱关系边

### 6.1 层级包含（BD→NS→CS）

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-ND` | `contains` | `NS-ND-UPF` |
| `NS-ND-UPF` | `instantiated_as` | `CS-ND-01`, `CS-ND-02`, `CS-ND-03`, `CS-ND-04`, `CS-ND-05` |

### 6.2 方案使用特性（uses_feature，共 18 条边）

| 起点 | 关系 | 终点（feature_code） |
|------|------|------|
| `CS-ND-01` | `uses_feature` | `GWFD-010234`, `GWFD-020161`, `GWFD-010105` |
| `CS-ND-02` | `uses_feature` | `GWFD-010234`, `GWFD-010105`, `GWFD-020421`, `IPFD-010001` |
| `CS-ND-03` | `uses_feature` | `NPFD-010000`, `NPFD-010014` |
| `CS-ND-04` | `uses_feature` | `IPFD-014000`, `IPFD-014001`, `IPFD-014002`, `IPFD-014003`, `IPFD-012003`, `GWFD-020411`, `IPFD-015004`, `IPFD-010001` |
| `CS-ND-05` | `uses_feature` | `NPFD-010014`, `IPFD-010001` |

> **去重后引用特性**：17 个（与 cross-feature-analysis.md §1.4 一致）。feature 详情见第2层 `02-feature-graph.md`。

### 6.3 方案使用任务（uses_task，task_id 权威形式 T-ND-NN，与 03/05 层一致）

> **Schema §13 禁止关系**：`ConfigurationSolution → ConfigTask` 的完整顺序链暂不进入主 schema（条件分支过强），仅保留 `uses_task`。
> **task_id 权威形式**：本表 uses_task 全部使用第3层定义的权威 task_id（`T-ND-NN`），与 03-task-layer §0.1 / 05-cross-layer-mapping §2.1 一致。01 层原中文流程描述（T-CS1-* / T-CS2-* / T-CS3-* / T-CS4-A*/M* / T-CS5-*）已合并为 03 层的 18 个原子 task，对应关系见 03 层 §0.1。
> **★顺序语义声明（U-M-08 强化）**：本表 uses_task 列表**无顺序语义**，CS→ConfigTask 的执行顺序由第3层 `FeatureTaskOrderEdge`（FE-ND-01~15）与 `TaskCommandOrderEdge`（TE-ND-*）承载。

| 起点 | uses_task（权威 task_id T-ND-NN + task_name） |
|------|------|
| `CS-ND-01` | T-ND-07 配置 N4 控制面接口（N4 VPN 实例+N4if 合一逻辑接口+SET UPINFO+N4 偶联验证） |
| `CS-ND-02` | T-ND-08 配置业务用户面接口（业务面 VPN+Saif/Scif/Paif+切片+Nupf 按需）/ T-ND-09 配置会话接入（APN/DNN+地址池三件套+IPALLOCRULE） |
| `CS-ND-03` | T-ND-06 配置网元和网管对接（5 步闭包：北向密码→SNMP 密钥→适配层→创建网元 14 参数→EMS 归属→LST ME 验证） |
| `CS-ND-04` | T-ND-10 VPN 实例与接口绑定 / T-ND-11 外联口自动部署（AUTOSCALING 模板族+SET AUTOCONFIG 开关） / T-ND-12 OSPF / T-ND-13 BGP / T-ND-14 静态路由 / T-ND-15 BFD / T-ND-16 隧道（IPsec/GRE/MPLS VPN） / T-ND-17 NP 卡级联口 |
| `CS-ND-05` | T-ND-01 加载 License（DP-CS5-06） / T-ND-02 NTP 双路时间同步 / T-ND-03 修改网元基本信息（触发 CS-3 回流） / T-ND-04 配置公共参数含 MTU 三层 / T-ND-05 高危命令二次授权 |
| （调测，跨 CS） | T-ND-18 整网调测 FirstCall（承接全部 CS 对接完成后） |

### 6.4 决策点归属（has_decision）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-ND-01` | `has_decision` | `DP-CS1-01`, `DP-CS1-02` |
| `CS-ND-02` | `has_decision` | `DP-CS2-01`, `DP-CS2-02`, `DP-CS2-03`, `DP-CS2-04`, `DP-CS2-05`, `DP-CS2-06`, `DP-CS2-07`, `DP-CS2-08` |
| `CS-ND-03` | `has_decision` | `DP-CS3-01`, `DP-CS3-02`, `DP-CS3-03` |
| `CS-ND-04` | `has_decision` | `DP-CS4-01`, `DP-CS4-02`, `DP-CS4-03`, `DP-CS4-04`, `DP-CS4-05`, `DP-CS4-06`, `DP-CS4-07` |
| `CS-ND-05` | `has_decision` | `DP-CS5-01`, `DP-CS5-02`, `DP-CS5-03`, `DP-CS5-04`, `DP-CS5-05`, `DP-CS5-06`, `DP-CS5-07` |

### 6.5 业务规则约束（constrained_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-ND-01` | `constrained_by` | `BR-ND-01`(N4 必备性), `BR-ND-02`(接口强制合一), `BR-ND-03`(VPN 四统一) |
| `CS-ND-02` | `constrained_by` | `BR-ND-02`(接口强制合一), `BR-ND-03`(VPN 四统一), `BR-ND-04`(跨域协同) |
| `CS-ND-03` | `constrained_by` | `BR-ND-06`(密码三元组), `BR-ND-05`(CS-5→CS-3 回流) |
| `CS-ND-04` | `constrained_by` | `BR-ND-07`(BGP 依赖 IGP), `BR-ND-08`(MPLS VPN 公私分离), `BR-ND-09`(自动部署开关规范), `BR-ND-10`(MTU 层级) |
| `CS-ND-05` | `constrained_by` | `BR-ND-01`(N4 必备性,架构认知约束), `BR-ND-10`(MTU 层级), `BR-ND-05`(CS-5→CS-3 回流) |

### 6.6 语义对象使用（uses_semantic_object）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-ND-01` | `uses_semantic_object` | `SO-ND-01`(N4if), `SO-ND-09`(VPN_Signaling), `SO-ND-21`(UPF 标识), `SO-ND-22`(PFCP 会话) |
| `CS-ND-02` | `uses_semantic_object` | `SO-ND-02`(Saif), `SO-ND-03`(Scif), `SO-ND-04`(Paif), `SO-ND-05`(外联口 SGi/N6), `SO-ND-06`(Nupf), `SO-ND-15`(APN/DNN), `SO-ND-16`(POOL), `SO-ND-17`(SECTION), `SO-ND-18`(POOLGROUP), `SO-ND-19`(POOLBINDGROUP), `SO-ND-20`(IPALLOCRULE) |
| `CS-ND-03` | `uses_semantic_object` | `SO-ND-23`(北向用户), `SO-ND-24`(SNMP 用户), `SO-ND-25`(网管适配层), `SO-ND-26`(被管网元 14 参数), `SO-ND-27`(EMS 归属) |
| `CS-ND-04` | `uses_semantic_object` | `SO-ND-09`(VPN 实例), `SO-ND-05`(外联口), `SO-ND-10`(OSPF), `SO-ND-11`(静态路由), `SO-ND-12`(BFD), `SO-ND-13`(BGP), `SO-ND-14`(MPLS), `SO-ND-28`(Loopback), `SO-ND-29`(自动部署模板), `SO-ND-30`(IPsec), `SO-ND-31`(GRE), `SO-ND-32`(MPLS VPN), `SO-ND-33`(NP 级联口), `SO-ND-34`(组网模式) |
| `CS-ND-05` | `uses_semantic_object` | `SO-ND-35`(部署形态), `SO-ND-36`(UPF 角色), `SO-ND-37`(抽象接口映射), `SO-ND-38`(License), `SO-ND-39`(NTP), `SO-ND-40`(网元身份), `SO-ND-41`(二次授权), `SO-ND-42`(公共参数 11 项), `SO-ND-43`(MTU 三层) |

### 6.7 决策点影响（selects / sets_value_pattern，跨层映射依据）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| `DP-CS5-01` | `selects` | `CS-ND-01`/`CS-ND-02` 接口集 | 架构模式决定下游接口集（5G SA vs 融合） |
| `DP-CS5-02` | `selects` | `CS-ND-02` 接口范围 | 部署形态决定可配置接口（独立/融合） |
| `DP-CS5-03` | `selects` | `CS-ND-02` 接口组合 | UPF 角色决定 N3/N9a/N9c/N6 组合 |
| `DP-CS4-01` | `selects` | `CS-ND-04` 自动 vs 手动轨 | 硬件类型决定部署轨（NP 卡必须手动） |
| `DP-CS4-02` | `selects` | `CS-ND-04` 路由协议范围 | SDN 禁用 OSPF，强制 BGP over 静态 |
| `DP-CS4-03` | `selects` | `CS-ND-04` 命令路径 | 自动(AUTOSCALING) vs 手动(逐条 MML) |
| `DP-CS4-04` | `sets_value_pattern` | VPN 地址族/OSPF 进程类型/SECTION 字段/逻辑接口 IPVERSION | IPv4/IPv6/双栈决定多个 ConfigParameter 值模式 |
| `DP-CS4-05` | `sets_value_pattern` | BFD 会话 ONEARMECHO/DEST | 双向 vs 单臂决定 BFD 模式参数 |
| `DP-CS2-03` | `selects` | `CS-ND-02` 接口配置路径 | Saif/Scif 合一 vs N3if/S1-uif 独立 |
| `DP-CS2-05` | `selects` | `CS-ND-02` 地址池配置范围 | LOCAL(完整三件套) vs EXTERNAL(仅 POOL+SECTION) |
| `DP-CS3-02` | `selects` | `CS-ND-03` 5 步闭包执行范围 | 完整 5 步 / 仅装适配层 / 跳过 |

### 6.8 证据支撑（supported_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-ND`, `NS-ND-UPF`, `CS-ND-01`~`CS-ND-05` | `supported_by` | `EV-BS-01`（设计文档 + doc-list） |
| 各 CS/DP/BR/SO | `supported_by` | 对应 `EV-TK-01~07` / `EV-CA-02`（见各对象 source_evidence_ids 字段） |

---

## 7. 端到端开局链路（→ 第3层 Task 编排 + Stage 4 端到端验证）

> **数据来源**：cross-topic-analysis.md §9。

### 7.1 完整开局流程（按对接面 CS × 流程顺序）

```
CS-5 基础就绪（开局第 1 步，全局前置）
  ├─ License 加载（DP-CS5-06 决策路径）
  ├─ NTP 双路时间同步（OMC + FusionStage）
  ├─ 网元基本信息（MOD ME + SET OMIP，注意触发 CS-3 回流，BR-ND-05）
  ├─ 高危命令二次授权（SET SECAUTH + 13 类清单）
  ├─ 公共参数 11 项
  ├─ MTU 三层调整 + 自动部署模板同步（BR-ND-10）
  └─ 架构认知确认（DP-CS5-01~04，决定下游接口集）
       ↓
CS-3 网管对接（开局对接调测起点）
  └─ 5 步闭包：北向密码(BR-ND-06) → SNMP 密钥(BR-ND-06) → 适配层 → 创建网元 14 参数 → EMS 检查
       ↓
CS-1 控制面 N4（UPF 唯一必备接口，BR-ND-01）
  └─ 配置 N4if（强制合一，BR-ND-02）+ SET UPINFO + SRVPING 验证偶联
       ↓
CS-2 用户面（接口 + 会话接入双层）
  ├─ 接口层：Saif/Scif/Paif + (S11-uif/Nupf 按需)
  └─ 会话接入层：APN → 地址池三件套 → IPALLOCRULE（BR-ND-03 VPN 四统一）
       ↓
CS-4 路由对接（★最大，按组网模式决策树 DP-CS4 分支）
  ├─ 自动部署（非 SDN 无 NP 卡 / SDN / 网络加速卡）：AUTOSCALING 模板族（BR-ND-09 开关规范）
  └─ 手动部署（NP 卡直连 PE / 失败补救）：逐条 MML
       ↓
调测 FirstCall（端到端验证）
  └─ 4 阶段 29 步：RU 状态 → UDG→对端路由 → 直连路由器→UDG → FirstCall 拨测
```

### 7.2 FirstCall 验证关键诊断分支（丢包率三分支）

```
NGPING 丢包率
├─ 0%   → 路由 OK → 进入 FirstCall 拨测
├─ 100% → 路由异常
│        ├─ 静态路由 → DSP SRROUTE（多条等开销 + 不同 ISU = 负荷分担正常）
│        ├─ OSPF     → DSP OSPFROUTING + LST OSPFAREA(NSSA) + Loopback 检查
│        └─ BGP      → LST BGPPEER + DSP BGPPEERINFO(=Established) + PING Loopback↔Peer
└─ 非 0 非 100% → 网络拥塞 → 联系华为技术支持
```

### 7.3 FirstCall 成功标志

`DSP SESSIONINFO` 4 参数正确：
- APN（接入点名）
- RoleType（UPF 角色）
- IPv4 PDP（IPv4 会话）
- Session 时间戳（会话建立时间）

---

## 8. 与其他场景业务图谱的差异

| 维度 | 网元对接（本场景） | 计费场景（标杆） | 带宽控制场景 |
|------|------------------|-----------------|--------------|
| BusinessDomain | `BD-ND 网元对接`（独立） | `BD-CH-01 业务感知`（共享） | `BD-BW-01 业务感知`（共享） |
| NetworkScenario | `NS-ND-UPF`（独立） | `NS-CH-01`（独立） | `NS-BW-01`（独立） |
| ConfigurationSolution | **5 个（按对接面组织）** | 7 个（按业务能力） | 7 个（按控制机制） |
| 核心机制 | N4if+业务接口+VPN+路由协议+BFD+自动部署模板 | SA→Rule→PCC/URR→Ga/Gy/N40→配额闭环 | SA→BWM→CAR/Shaping/FUP/GBR |
| 独有对象族 | N4if/Saif/Scif/Paif 抽象接口、AUTOSCALING 模板族（8 个）、VPN 实例、路由协议族、BFD 会话 | 计费三件套(URR/URRGROUP/PCCPOLICYGRP)、CCT/CHFINIT | BWM(BWMSERVICE/BWMCONTROLLER/BWMRULE) |
| DecisionPoint | **27 个**（含组网模式 5 维矩阵） | 8 个 | 8 个 |
| BusinessRule | 10 条 | 16 条 | 6 条 |
| SemanticObject | 43 个 | 12 个 | 8 个 |
| 特性角色 | **引用支撑**（非主体） | 主体（特性驱动配置） | 主体 |
| 端到端主线 | 开局流程（CS-5→CS-3→CS-1→CS-2→CS-4→FirstCall） | 业务开通流程 | 业务开通流程 |

> **场景特殊性总结**：对接类场景图谱主体是 CS 方案闭包 + DP 决策树（而非特性），CS 按对接面组织（而非业务能力），DP 数量是业务配置类的 3 倍（组网模式多维矩阵），SO 数量最多（43 个，含抽象接口/路由协议/会话接入/网管/基础就绪五大类）。

---

## 9. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| BusinessDomain | 1 | `BD-ND` |
| NetworkScenario | 1 | `NS-ND-UPF` |
| ConfigurationSolution | **5** | `CS-ND-01`~`CS-ND-05` |
| DecisionPoint | **27** | DP-CS1-01~02(2) + DP-CS2-01~08(8) + DP-CS3-01~03(3) + DP-CS4-01~07(7) + DP-CS5-01~07(7) |
| BusinessRule | **10** | `BR-ND-01`~`BR-ND-10` |
| SemanticObject | **43** | `SO-ND-01`~`SO-ND-43`（抽象接口 8 + VPN/路由 6 + 会话接入 6 + 网管 7 + 路由扩展 7 + 基础就绪 9） |
| Scope（子对象） | 9 | network_control / access_side / session_anchor / slice_binding / mgmt_access / external_routing / dual_stack / tunnel_overlay / global_bootstrap |
| Participant（子对象） | 22（U-M-03 修正） | UDG/UPF/SMF/SGW-C/PGW-C/(R)AN/I-UPF/ULCL/DN/PDN/UDM/NWDAF/U2020-MAE/OM Portal/VNF LCM/DC-GW/PE/EOR/SDN 控制器/NFVO/OMC/FusionStage（注：UDG/UPF 视为同一实体按角色拆分计 2） |
| **业务层对象总计** | **~118**（原 ~115，Participant 口径修正 +3） | — |

### 关系边计数

| 关系类型 | 数量 |
|---------|------|
| `contains` (BD→NS) | 1 |
| `instantiated_as` (NS→CS) | 5 |
| `uses_feature` (CS→Feature) | 18（去重后引用 17 特性） |
| `uses_task` (CS→Task，task_id 由 03 层定义) | ~40（5 CS 的 Task 描述） |
| `has_decision` (CS→DP) | 27 |
| `constrained_by` (CS→BR) | 15（5 CS × 平均 3 BR） |
| `uses_semantic_object` (CS→SO) | 43（全 SO 被 5 CS 引用） |
| `selects` / `sets_value_pattern` (DP→CS/参数) | 11（关键跨层映射） |
| `supported_by` (对象→EvidenceSource) | 全对象 |

---

## 10. §13 禁止关系遵循声明

本业务图谱严格遵循 Schema §13 禁止关系：

| 禁止关系 | 本文件遵循方式 |
|---------|--------------|
| `ConfigurationSolution → ConfigObject` | **未直接绑** ConfigObject；通过 `uses_feature` / `uses_task` / `uses_semantic_object` 间接关联 |
| `ConfigurationSolution → MMLCommand` | **未直接拥有** MMLCommand 实例；通过 `uses_task → invokes → MMLCommand`（第3/4层） |
| `BusinessRule → CommandParameter` 直接写死 | **未写死**参数值；通过 DecisionPoint（DP-CS4-04 等）+ TaskRule（第3层）+ CommandRule（第4层）表达 |
| 业务图谱内建 `ConfigObject` 实体 | **未内建**；ConfigObject 在第4层 04-command-graph 定义 |
| `ConfigurationSolution → ConfigTask` 完整顺序链 | **未建**完整顺序链；仅保留 `uses_task`（顺序待实例层承接，由 03-task-layer 的 TaskCommandOrderEdge 承载） |

> **`core_mechanism_combo` 业务语义化**：所有 CS 的 core_mechanism_combo 保持业务语义（如"VPN+OSPF+BFD+外联口"），**不写命令清单**。命令清单在第4层。

---

> 本文件为网元对接三层图谱第1层（业务图谱，主体层）。第2层特性图谱（`02-feature-graph.md`，已建）、第3层任务原子层（`03-task-layer.md`）、第4层命令图谱（`04-command-graph.md`）、第5层跨层映射、第6层证据索引见同目录其他文件。
