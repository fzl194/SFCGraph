# 网元对接三层图谱 · 第3层：任务原子层

> **文件定位**：`three-layer-graph/03-task-layer.md`
> **Schema 参考**：`三层图谱Schema-最终版-v0.1.md` §10 任务原子层（字段标准）、§9.7 FeatureTaskOrderEdge、§13 禁止关系
> **作用**：实例化 UPF 网元对接（UDG 扮演 UPF/PGW-U/SGW-U）开局对接所需的 ConfigTask + TaskRule + TaskCommandOrderEdge + 端到端开局链路
> **数据来源**：`cross-topic-analysis.md`（EV-CA-02，§9 端到端开局链路 / §6 各 CS 的 Task 要素 / 附录D）、`04-command-graph.md`（103 命令，task 的 `command_refs` 引用其 `command_name`）、`topic-knowledge/Batch-01~07`（命令顺序与流程细节，EV-TK-NN）
> **task_id 规范**：`T-ND-NN`（ND=网元对接，按端到端流程顺序编号）；与 01-business-graph.md 的中文 Task 描述一一对应
> **`command_refs` 引用规范**：引用 `04-command-graph.md` 的 `command_name`（如 `ADD VPNINST`），命名一致
> **编制日期**：2026-06-29

---

## 0. 任务层总览

### 0.1 ConfigTask 分类

| 类型 | 数量 | 编号范围 | 说明 |
|------|------|---------|------|
| feature_specific（特性专属） | 4 | T-ND-07/08/09/17 | 关联特定 UPF 接口/NP 卡能力的 task |
| cross_feature（跨多特性） | 4 | T-ND-06/10/16/18 | 跨多个特性/方案组合的 task |
| generic（通用，跨特性复用） | 10 | T-ND-01~05/11~15 | 跨特性复用的基础配置步骤 |
| **合计** | **18** | T-ND-01~T-ND-18 | — |

> **Task 编号段说明（按端到端开局流程顺序）**：
> - **CS-5 基础就绪**：T-ND-01 License / T-ND-02 NTP / T-ND-03 网元信息 / T-ND-04 公共参数(含MTU) / T-ND-05 二次授权
> - **CS-3 网管对接**：T-ND-06 网管对接(5步闭包)
> - **CS-1 控制面**：T-ND-07 配置N4控制面接口
> - **CS-2 用户面**：T-ND-08 配置业务用户面接口 / T-ND-09 配置会话接入
> - **CS-4 路由对接**：T-ND-10 VPN实例与接口绑定 / T-ND-11 外联口自动部署模板 / T-ND-12 OSPF / T-ND-13 BGP / T-ND-14 静态路由 / T-ND-15 BFD / T-ND-16 隧道(IPsec/GRE/MPLS VPN) / T-ND-17 级联口(NP卡)
> - **调测**：T-ND-18 整网调测与FirstCall验证

> **与 01-business-graph.md 的对应关系**（01 层 uses_task 引用中文描述，本层定义权威 task_id）：
> - T-CS5-01~07 → T-ND-01~05（合并：公共参数+MTU→T-ND-04；架构认知属 DecisionPoint 不单列 task）
> - T-CS3-01~06 → T-ND-06（5步闭包合并为单 task，步骤由 TaskCommandOrderEdge 表达）
> - T-CS1-01~04 → T-ND-07（N4 VPN+N4if+UPINFO 合并，验证由 T-ND-18 承接）
> - T-CS2-01~08 → T-ND-08（接口层）+ T-ND-09（会话接入层）
> - T-CS4-A1~A7 / M1~M7 → T-ND-10~17（按路由协议/部署方式拆为可复用原子）

### 0.2 任务原子化原则（对接场景特殊性）

1. **对接场景 task 多为 generic**：路由协议(OSPF/BGP/静态)、VPN 实例、BFD 等跨多种组网模式复用，优先提升为 generic
2. **接口配置按对接面归属**：N4 接口(CS-1)、用户面接口(CS-2)与特定 UPF 接口能力绑定，保留 feature_specific
3. **会话接入独立成 task**：APN+地址池+分配规则是用户面双层结构的下层，跨多个用户面接口复用
4. **命令顺序通过 TaskCommandOrderEdge 表达**：task 间端到端顺序通过 §5 端到端开局链路表达
5. **CS-4 组网模式分支由 DecisionPoint 承接**：同一 task（如 T-ND-12 OSPF）在不同 DP 分支下命令参数不同，差异由 04 层 CommandRule + variant_dimensions 表达，task 层只管"做什么"

---

## 1. ConfigTask 实例化（18 个）

> 字段顺序遵循 Schema §10.3：`task_id / task_name / task_summary / task_scope_type / task_goal / input_contract / output_contract / command_refs / source_evidence_ids`。`status` 默认 `active`。

### 1.1 CS-5 基础就绪（5 个，开局第 1 步全局前置）

#### T-ND-01 加载 License

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-01` |
| `task_name` | `加载 License` |
| `task_summary` | 加载网元 License 文件（含 Service Fabric License），确认 ESN 一致性与控制项生效 |
| `task_scope_type` | `generic` |
| `task_goal` | 完成 UDG 网元 License 加载与激活，为下游特性（多 SMF 对接 GWFD-020161、MPLS VPN GWFD-020411 等）提供能力前置 |
| `input_contract` | ESN、License 文件（dat 2.0 / xml 3.0）、加载路径决策（DP-CS5-06: OM Portal 仅网元 / U2020+MAE 含 Service Fabric） |
| `output_contract` | License 实例（含控制项 + 状态机），无红色告警，DSP RVKLICINFO 无失效码 |
| `command_refs` | `DSP RVKLICINFO`（查询失效码；加载动作在 OM Portal / U2020 网管侧 GUI 完成，非 MML） |
| `source_evidence_ids` | EV-CA-02 §6.5, EV-TK-01 KP-09~11 |

#### T-ND-02 配置 NTP 时间同步

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-02` |
| `task_name` | `配置 NTP 时间同步` |
| `task_summary` | 配置双路 NTP 时间源（OMC + FusionStage），保障网元时间与网络一致 |
| `task_scope_type` | `generic` |
| `task_goal` | 建立 UDG 双路时间同步，避免证书/日志时间偏移导致对接异常 |
| `input_contract` | OMC 时间源 IP、FusionStage 时间源 IP、SRVLEVEL |
| `output_contract` | NTPSource 实例（双路） |
| `command_refs` | `SET NTP` |
| `source_evidence_ids` | EV-CA-02 §6.5, EV-TK-02 KP-01 |

#### T-ND-03 修改网元基本信息

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-03` |
| `task_name` | `修改网元基本信息` |
| `task_summary` | 修改网元名称（MOD ME）与浮动/物理 IP（SET OMIP），注意触发 CS-3 网管回流 |
| `task_scope_type` | `generic` |
| `task_goal` | 设置全网唯一的网元身份与 OM IP，为网管对接（CS-3）提供可达地址 |
| `input_contract` | MEID/MENAME、浮动 IP、物理 IP；**前置**：T-ND-05 二次授权已完成（SET OMIP 是高危二次授权命令） |
| `output_contract` | NetworkElement + OMIP 实例；**副作用**：修改浮动 IP 会中断网管 + VNFM 连接，触发 T-ND-06 网管重对接 |
| `command_refs` | `MOD ME`, `SET OMIP`, `LST ME`, `LST OMIP` |
| `source_evidence_ids` | EV-CA-02 §5.6/§6.5, EV-TK-02 KP-02/03 |

#### T-ND-04 配置公共参数（含 MTU 三层）

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-04` |
| `task_name` | `配置公共参数（含 MTU）` |
| `task_summary` | 配置 11 项公共参数 + Fabric/外联口 MTU 三层（网卡≥Fabric>主接口≥子接口，外联口与下一跳网关一致默认 1500） |
| `task_scope_type` | `generic` |
| `task_goal` | 完成 UDG 全局公共参数与 MTU 层级基线，避免 IPv6 分片丢包（IPV6FRAGPLCY）与外联口 MTU 不一致告警（ALM-232398849） |
| `input_contract` | 11 项公共参数规划值、Fabric MTU、外联口 MTU（与直连 DCGW/PE 一致）、IPv6 分片策略（TOOBIG_PKTDROP→OUTERFRAG） |
| `output_contract` | GlobalParameter（11 项）+ MTUConfig（Fabric/外联口）；自动部署场景需同步 MOD AUTOSCALINGSERVICE |
| `command_refs` | `SET SIGDSCP`, `SET UDPCHECKSUM`, `SET SRVCOMMONPARA`, `SET QOSCAR`, `SET IPV6FRAGPLCY`, `SET CPTEIDUALLOC`, `SET TZ`, `SET ANTIFRAUD`, `SET FWDPARA`, `SET HEADENGLBPARA`, `SET MSFAULTALARM`, `SET FABRICMTU`, `MOD INTERFACE`, `SET IFIPV6ENABLE` |
| `source_evidence_ids` | EV-CA-02 §5.5/§6.5, EV-TK-02 KP-04/05 |

#### T-ND-05 配置高危命令二次授权

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-05` |
| `task_name` | `配置高危命令二次授权` |
| `task_summary` | 开启二次授权总开关 + 增加授权用户 + 13 类高危命令清单，避免开局自动化脚本弹窗阻塞 |
| `task_scope_type` | `generic` |
| `task_goal` | 解除 13 类 UDG 默认二次授权命令（SET OMIP / MOD VIRTUALIP / SET FWDPARA / IPsec 系列等）的弹窗阻塞，保障自动化开局连续执行 |
| `input_contract` | 授权用户名/密码、13 类命令清单 |
| `output_contract` | SecurityAuth 实例（总开关 STATUS=ON + 用户 + 命令清单成员） |
| `command_refs` | `SET SECAUTH`, `ADD USRSECAUTH`, `ADD SECAUTHMEM` |
| `source_evidence_ids` | EV-CA-02 §3.5, EV-TK-02 KP-03 |

---

### 1.2 CS-3 网管对接（1 个，5 步闭包）

#### T-ND-06 配置网元和网管对接

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-06` |
| `task_name` | `配置网元和网管对接` |
| `task_summary` | 网管对接 5 步闭包：重置北向密码 + 重置 SNMP 密钥 + 安装适配层 + 创建网元 14 参数 + EMS 检查 + LST ME 验证 |
| `task_scope_type` | `cross_feature` |
| `task_goal` | 完成 UDG 与 U2020/MAE 网管的端到端对接，LST ME 执行成功 |
| `input_contract` | **前置**：T-ND-03 已完成（网元 IP 可达）；北向用户密码、SNMP 认证/加密密钥（**两者不能相同**）、网管适配层版本、网元 14 项参数（名称/IP/TLS/OSS 认证/emscomm 账号/SNMPV3/端口 8000/SHA512+AES256） |
| `output_contract` | ManagedNE 实例（14 参数）+ NorthboundUser + SNMPUser + NetworkMgmtAdapter + EMSAssociation；LST ME 成功 |
| `command_refs` | `SET NEWCERTSWITCH`（证书自动更新前置）, `LST ME`（验证标志）；密码重置/适配层安装/网元创建在网管侧 GUI 完成 |
| `source_evidence_ids` | EV-CA-02 §5.7/§6.3, EV-TK-02 KP-06 |
| `note` | BR-CS3-PASSWORD-TRIPLE：北向密码必须重置 + SNMP 认证/加密密钥必须重置且不相同（开局最常见失败原因）；回流约束：T-ND-03 改浮动 IP 后必须重跑本 task |

---

### 1.3 CS-1 控制面（1 个，N4 唯一必备接口）

#### T-ND-07 配置 N4 控制面接口

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-07` |
| `task_name` | `配置 N4（N4if）控制面接口` |
| `task_summary` | 配置 N4 强制合一抽象接口（N4/Sxa/Sxb）+ VPN_Signaling + UPF 标识（HOSTNAME 全网唯一） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 UPF 与 SMF/SGW-C/PGW-C 的 PFCP 控制面偶联基础（N4 是 UPF 唯一必配接口） |
| `input_contract` | N4 IP（与外联口/对端物理口不同网段）、VPN_Signaling、HOSTNAME（全网唯一）、IP 版本（DP-CS1-01: IPv4/IPv6/双栈）；**关联特性**：GWFD-010234 Single IP（接口抽象合一）；多 SMF 场景需 GWFD-020161 CU Full Mesh + License |
| `output_contract` | N4Interface（N4if1/0/0 强制合一）+ VPNInstance(VPN_Signaling) + UPFIdentity(HOSTNAME)；**附加约束**：UDG 上至少存在一个数据面逻辑接口 IP（Paif/Scif/Saif 任一），否则 N4 偶联失败 |
| `command_refs` | `ADD VPNINST`, `ADD LOGICINF`, `SET UPINFO` |
| `source_evidence_ids` | EV-CA-02 §5.1/§5.2/§6.1, EV-TK-03 KP-01/02 |

---

### 1.4 CS-2 用户面（2 个，接口层 + 会话接入层）

#### T-ND-08 配置业务用户面接口

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-08` |
| `task_name` | `配置业务用户面接口（Saif/Scif/Paif/N3if/N6）` |
| `task_summary` | 按 UPF 角色配置接入侧(Saif/N3if/S1-uif)+中间侧(Scif/N9cif)+锚点侧(Paif 强制合一)逻辑接口，含切片绑定与 Nupf 服务化接口 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 UPF 与 (R)AN/I-UPF/ULCL/DN 的用户面数据通道（接口层） |
| `input_contract` | UPF 角色（DP-CS2-01: 边缘/锚点/融合/NB-IoT/NWDAF）→ 接口组合；IP 版本（DP-CS2-02）；Sa/Sc 合一 vs 独立（DP-CS2-03，互斥）；切片绑定开关（DP-CS2-04，仅 Saif/N3if）；各接口 IP（掩码固定 /32，与外联口/对端不同网段）；**关联特性**：GWFD-010234 Single IP |
| `output_contract` | LogicInterface 集合（SaInterface/CoreInterface/AnchorInterface 强制合一/SNSSAIBinding）+ 业务面 VPN（VPN_Access/VPN_Sc/VPN_Pa/VPN_Internet）；Nupf 场景额外 LogicIP+HTTPLEGRP |
| `command_refs` | `ADD VPNINST`, `ADD LOGICINF`, `ADD SNSSAIUPINTF`, `ADD LOGICIP`, `ADD HTTPLEGRP`, `ADD HTTPLE`, `ADD SBIAPLE`, `SET HTTPCONF` |
| `source_evidence_ids` | EV-CA-02 §3.1/§5.2/§6.2, EV-TK-03 KP-01~08 |

#### T-ND-09 配置会话接入

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-09` |
| `task_name` | `配置会话接入（APN/地址池三件套/分配规则）` |
| `task_summary` | 配置 APN/DNN + 地址池五件套（POOL→SECTION→POOLGROUP→POOLBINDGROUP→POOLGRPMAP）+ 三级地址分配规则 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成用户激活接入 PDN/DN 的完整闭环（会话接入层），使 UDG 可为 UE 分配 IP 并建立会话 |
| `input_contract` | APN/DNN 名（与 C 面 SMF/SGW-C 一致）、VPN 绑定（与 T-ND-08 业务面 VPN 一致，BR-VPN-4UNIFY）、地址池类型（DP-CS2-05: LOCAL UDG 分配 / EXTERNAL 外部 NF 分配）、地址段（IPv4 起止 IP / IPv6 前缀 LENGTH=64）、分配维度（DP-CS2-06: APN/SMF/位置，默认 APN）；**关联特性**：GWFD-010105 用户面地址分配、GWFD-020421 基于位置的地址分配 |
| `output_contract` | APN + AddressPool + AddressSection + PoolGroup + PoolBinding + PoolGroupMap + IPAllocRule（FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0） |
| `command_refs` | `ADD APN`, `SET APNSGLPASS`, `ADD POOL`, `ADD SECTION`, `ADD POOLGROUP`, `ADD POOLBINDGROUP`, `ADD POOLGRPMAP`, `SET IPALLOCRULE` |
| `source_evidence_ids` | EV-CA-02 §3.4/§6.2, EV-TK-03 KP-09~11 |

---

### 1.5 CS-4 路由对接（8 个，按部署方式 + 协议类型拆分）

#### T-ND-10 配置 VPN 实例与接口绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-10` |
| `task_name` | `配置 VPN 实例与接口绑定` |
| `task_summary` | 配置路由侧 L3VPN 实例 + 地址族（ipv4uni/ipv6uni）+ VPN Target + 接口绑定 VPN（外联口基础设施层） |
| `task_scope_type` | `cross_feature` |
| `task_goal` | 建立业务隔离的 VPN 路由容器，承载下游 OSPF/BGP/静态路由协议 |
| `input_contract` | VPN 名（VPN_Access/VRF_Internet/VRF_PDNx；MPLS 用 `_public_`）、地址族（DP: IPv4/IPv6/双栈 → ipv4uni+ipv6uni 都配）、RT 导入导出标记、VRFRD（MPLS 必配不重复）；**前置**：T-ND-08 业务面 VPN 已定 |
| `output_contract` | L3VPNInstance + VPNAddressFamily + VPNTarget + IPBINDVPN；MPLS VPN 场景外联口绑 `_public_`（公私分离） |
| `command_refs` | `ADD L3VPNINST`, `ADD VPNINSTAF`, `MOD VPNINSTAF`, `ADD VPNTARGET`, `ADD IPBINDVPN` |
| `source_evidence_ids` | EV-CA-02 §3.2层1/§5.9, EV-TK-04 KP-10 |

#### T-ND-11 配置外联口自动部署模板

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-11` |
| `task_name` | `配置外联口自动部署模板` |
| `task_summary` | 自动部署轨专用：关开关 → 配 AUTOSCALING 模板族（SERVICE/ETHTRUNK/BFD/SRROUTE/MPLS 等）→ 开开关，DSP OPSASSISTSTATE 确认 Ready |
| `task_scope_type` | `generic` |
| `task_goal` | 通过模板族实现外联口/BFD/静态路由/MPLS 接口的零人工扩容自动部署 |
| `input_contract` | **部署方式决策**（DP-CS4-03: 自动 vs 手动，本 task 仅自动轨）；组网架构（DP-CS4-02: 非SDN/SDN → IPALLOCTYPE4/6、NEXTHOPALLOCTYPE4/6 取值）；硬件类型（DP-CS4-01: AUTOCFGIFTYPE=VNIC/ETHTRUNK，网络加速卡强制 ETHTRUNK）；VPN 名（引用 T-ND-10）；OSPF 使能开关（OSPFENABLE，仅非SDN OSPF 方案） |
| `output_contract` | AutoConfigSwitch（FALSE→TRUE 时序）+ AutoScalingService + EthTrunk/BFD/SRRoute/MPLS 模板；部署完成后无法自动修改/删除（模板不可变约束） |
| `command_refs` | `LST AUTOCONFIG`, `DSP OPSASSISTSTATE`, `SET AUTOCONFIG`, `ADD AUTOSCALINGETHTRUNK`, `ADD AUTOSCALINGSERVICE`, `MOD AUTOSCALINGSERVICE`, `ADD AUTOSCALINGBFD`, `ADD AUTOSCALINGSRBFD`, `ADD AUTOSCALINGSRROUTE`, `ADD AUTOSCALINGBGPLF`, `ADD AUTOSCALINGIPREACH`, `ADD AUTOSCALINGMPLS` |
| `source_evidence_ids` | EV-CA-02 §3.2层5/§3.3/§5.10, EV-TK-04 KP-01 |
| `note` | TR-ND-03 自动部署开关时序；SDN 四强制（DHCP+单臂BFD+BGP over静态+DHCPv6 DUID）通过模板参数落值 |

#### T-ND-12 配置 OSPF 动态路由

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-12` |
| `task_name` | `配置 OSPF 动态路由` |
| `task_summary` | 配置 OSPF IPv4 进程+区域+接口+引入路由（IMPORTPROTOCOL=wlr 用户下行路由）；IPv6 用 OSPFv3 分别配 |
| `task_scope_type` | `generic` |
| `task_goal` | 通过 OSPF/OSPFv3 动态发布用户下行路由，建立 UDG 与 DC-GW/PE 的动态路由邻接 |
| `input_contract` | OSPF 进程 ID、Router ID（SCHEMAROUID/ROUTERID，IPv4 与 IPv6 共用）、区域 ID（NSSA 区域需配 Loopback 自动选 FA）、IP 版本（DP-CS4-04: IPv4=OSPF / IPv6=OSPFv3 / 双栈分别配）；**前置**：T-ND-10 VPN 实例+接口绑定完成；**不适用**：SDN 场景（SDN 不支持 OSPF）、DC-GW 双活/M-LAG（强制 BGP over 静态） |
| `output_contract` | OSPFProcess + OSPFArea + OSPFInterface + OSPFIMPORTROUTE（wlr 协议标识）；IPv6 场景额外 OSPFV3 系列 |
| `command_refs` | `ADD OSPF`, `ADD OSPFAREA`, `ADD OSPFNETWORK`, `ADD OSPFINTERFACE`, `ADD OSPFIMPORTROUTE`, `ADD OSPFV3`, `ADD OSPFV3AREA`, `ADD OSPFV3INTERFACE`, `ADD OSPFV3IMPORTROUTE` |
| `source_evidence_ids` | EV-CA-02 §4.4, EV-TK-04 KP-02/05 |

#### T-ND-13 配置 BGP 路由

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-13` |
| `task_name` | `配置 BGP 路由` |
| `task_summary` | 配置 BGP 全局+VPN 实例+地址族+对等体（eBGP Loopback EBGPMAXHOP=10）+ 引入路由（wlr）；MPLS VPN 用 MP-EBGP（ipv4vpn）传 IPv6 私网路由 |
| `task_scope_type` | `generic` |
| `task_goal` | 通过 BGP 发布用户路由（BGP 自身不能发现路由，必须 IMPORTROUTE），建立 UDG 与 PE/DC-GW 的 eBGP 邻居 |
| `input_contract` | BGP Router ID、对等体地址（用 Loopback 建 eBGP）、EBGPMAXHOP=10、VPN 名（引用 T-ND-10）、地址族类型（ipv4/ipv6/ipv4vpn=MPLS MP-EBGP 开关）；**前置**：T-ND-10 VPN 实例 + T-ND-15 BFD（动态检测） + 专用 Loopback 接口（与 IGP 外联口同 VPN，MPLS 不绑 VPN）；**依赖**：IGP 自动部署基础（OSPF/静态） |
| `output_contract` | BGPInstance + BGPVRF + BGPAddressFamily + BGPPeer + IMPORTROUTE（wlr）+ NetworkRoute（Loopback 路由引入）；MPLS 场景 perInstance+perNexthop 节省标签 |
| `command_refs` | `SET BGP`, `ADD BGPVRF`, `ADD BGPVRFAF`, `ADD BGPPEER`, `ADD BGPPEERAF`, `ADD IMPORTROUTE`, `ADD NETWORKROUTE` |
| `source_evidence_ids` | EV-CA-02 §5.8/§5.9, EV-TK-04 KP-04/10 |

#### T-ND-14 配置静态路由

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-14` |
| `task_name` | `配置静态路由` |
| `task_summary` | 配置手动 IPv4/IPv6 静态路由（SESSIONNAME 绑定 BFD），SDN 场景 DHCPENABLE=TRUE |
| `task_scope_type` | `generic` |
| `task_goal` | 通过静态路由发布用户下行路由，适用于 OSPF 环路禁用场景（二层/一层架构）与 SDN 场景 |
| `input_contract` | 前缀+下一跳（PREFIX4/NEXTHOP4 或 PREFIX6/NEXTHOP6）、SESSIONNAME（绑定 T-ND-15 BFD 会话）、SDN 场景 DHCPENABLE=TRUE；**前置**：T-ND-10 VPN 实例 + T-ND-15 BFD |
| `output_contract` | StaticRoute 实例（v4/v6）；自动部署场景由 ADD AUTOSCALINGSRROUTE 模板承载 |
| `command_refs` | `ADD SRROUTE`, `ADD SRROUTE6`（手动轨） / `ADD AUTOSCALINGSRROUTE`（自动轨，引用 T-ND-11） |
| `source_evidence_ids` | EV-CA-02 §4.1/§4.2/§4.4, EV-TK-04 KP-03/06 |

#### T-ND-15 配置 BFD 检测

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-15` |
| `task_name` | `配置 BFD 检测` |
| `task_summary` | 全局激活 BFD + 配置 BFD 会话（双向 LOCALDISCR/REMOTEDISCR 或单臂 Echo ONEARMECHO=TRUE），SDN/网络加速卡/DC-GW 双活强制单臂 |
| `task_scope_type` | `generic` |
| `task_goal` | 为静态路由/OSPF 提供快速故障检测，触发路由切换 |
| `input_contract` | BFD 模式（DP-CS4-05: 双向 vs 单臂 Echo）、本地/远端标识符（双向必配）、目的 IP（非SDN=网关 IP；SDN=Leaf 节点 IP）；**强制单臂场景**：SDN / 网络加速卡 / DC-GW 双活网关 M-LAG |
| `output_contract` | BFDSession 实例（双向或单臂 Echo）；自动部署场景由 ADD AUTOSCALINGBFD / ADD AUTOSCALINGSRBFD 模板承载 |
| `command_refs` | `SET BFD`, `ADD BFDSESSION`（手动轨） / `ADD AUTOSCALINGBFD`, `ADD AUTOSCALINGSRBFD`（自动轨，引用 T-ND-11） |
| `source_evidence_ids` | EV-CA-02 §3.2层2/§4.1, EV-TK-04/05 |

#### T-ND-16 配置隧道（IPsec/GRE/MPLS VPN）

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-16` |
| `task_name` | `配置隧道（IPsec/GRE/MPLS VPN）` |
| `task_summary` | 按业务需求叠加隧道：IPsec 跨安全域加密 / GRE 隧道（PGW-U↔WAP） / MPLS VPN（UDG 作 PE 对接企业网 OptionB 跨域） |
| `task_scope_type` | `cross_feature` |
| `task_goal` | 在基础路由之上叠加安全加密（IPsec）、WAP 访问（GRE）、企业网对接（MPLS VPN）能力 |
| `input_contract` | 隧道类型（DP-CS4-07: 无/IPsec/GRE/MPLS VPN）、源/目的 IP（基于 Loopback）、IPsec SA/SPI（**高危二次授权**）、MPLS 全局使能 + VRFRD；**关联特性**：IPFD-015004 IPsec、GWFD-020411 MPLS VPN；**前置**：T-ND-10 VPN 实例、Loopback 接口 |
| `output_contract` | IPsecSA / GRETunnel / MPLSGlobal+MPLSInterface 实例；MPLS 场景 ADD MPLSIF 手动逐个或 ADD AUTOSCALINGMPLS 自动 |
| `command_refs` | `ADD IPSEC*`（IPsec 系列）, `ADD GRETUNNEL`, `MOD GRETUNNEL`, `SET MPLSSITE`, `ADD MPLSIF`, `ADD AUTOSCALINGMPLS`（自动轨） |
| `source_evidence_ids` | EV-CA-02 §4.3/§5.9, EV-TK-04/05 |

#### T-ND-17 修改级联口（NP 卡场景）

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-17` |
| `task_name` | `修改级联口（NP 卡场景）` |
| `task_summary` | NP100 多框级联场景配置 NP 卡级联口（P3/P4），NP121 无级联 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 NP 卡多框级联链路，支撑 NP100 硬件的多框数据面互通 |
| `input_contract` | 硬件类型（DP-CS4-01: B=NP卡直连PE / C=网络加速卡直连DC-GW，仅 NP100 有级联口）、PORTID、型号（P3/P4）；**不适用**：无 NP 卡标卡、NP121 |
| `output_contract` | NPCascadePort 实例 |
| `command_refs` | `ADD NPDIRECTCONNECTPORT`, `LST NPDIRECTCONNECTPORT`, `RMV NPDIRECTCONNECTPORT` |
| `source_evidence_ids` | EV-CA-02 §4.3/附录B.4, EV-TK-06 KP-03/04 |

---

### 1.6 调测（1 个）

#### T-ND-18 整网调测与 FirstCall 验证

| 字段 | 值 |
|------|---|
| `task_id` | `T-ND-18` |
| `task_name` | `整网调测与 FirstCall 验证` |
| `task_summary` | 端到端 4 阶段验证：RU 就绪 → UDG→对端路由可达 → 直连路由器→UDG 回程 → FirstCall 拨测 + DSP SESSIONINFO 4 参数 |
| `task_scope_type` | `cross_feature` |
| `task_goal` | 验证端到端开局链路打通，FirstCall 成功（DSP SESSIONINFO 显示 APN/RoleType/IPv4 PDP/Session 时间戳） |
| `input_contract` | **前置**：T-ND-01~17 全部完成；测试终端（apn-test）、4G/5G 终端（融合场景需同时拨测） |
| `output_contract` | 验证通过：DSP SERVICERUSTATE 全正常 + NGPING 丢包率 0% + 路由负荷分担正常 + FirstCall 拨测成功 + DSP SESSIONINFO 4 参数正确 |
| `command_refs` | `DSP SERVICERUSTATE`, `NGPING`, `DSP SRROUTE`, `DSP OSPFROUTING`, `LST BGPPEER`, `DSP BGPPEERINFO`, `DSP ROUTE`, `DSP ROUTE6`, `PING`, `SRVPING`, `SRVTRACERT`, `DSP SESSIONINFO`, `LST OSPFIMPORTROUTE`, `LST LOGICINF`, `EXP MML` |
| `source_evidence_ids` | EV-CA-02 §9.2/§9.3, EV-TK-07 KP-08 |
| `note` | 丢包率三分支诊断：0%→路由 OK / 100%→路由异常（按协议类型分支定位）/ 非0非100%→网络拥塞 |

---

## 2. TaskRule（任务级规则）

> 字段顺序遵循 Schema §10.4：`rule_id / task_ref / rule_name / rule_type / rule_expression_mode / rule_logic / source_evidence_ids`。`status` 默认 `active`。

| `rule_id` | `task_ref` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_logic` | `source_evidence_ids` |
|-----------|------------|-------------|-------------|------------------------|--------------|----------------------|
| `TR-ND-01` | T-ND-07, T-ND-08 | N4 必备性 + 数据面接口附加 | `validation_rule` | `explicit` | N4 是 UPF 唯一必配接口；N4 单独配不足以建立偶联，UDG 上至少需存在一个数据面逻辑接口 IP（Paif/Scif/Saif/N3if/S1-uif/S11-uif 任一） | EV-CA-02 §5.1/§7.2 |
| `TR-ND-02` | T-ND-07, T-ND-08 | 接口掩码统一 | `naming_rule` | `explicit` | 所有业务逻辑接口 IPV4MASK1 固定 255.255.255.255（/32 主机路由）；IP 不能与外联口/对端物理口同网段 | EV-CA-02 §3.1, EV-TK-03 KP-01 |
| `TR-ND-03` | T-ND-08, T-ND-09, T-ND-10 | VPN 四统一 | `dependency_rule` | `explicit` | 业务 APN 绑定 VPN、地址池绑定 VPN、Gi/SGi/N6 外联口绑定 VPN、各业务逻辑接口绑定 VPN 四者必须一致 | EV-CA-02 §3.1/§5.3 |
| `TR-ND-04` | T-ND-07, T-ND-08 | 强制合一 vs 可选合一互斥 | `selection_rule` | `explicit` | N4if/Paif 强制合一（不支持独立 Sxa/Sxb/N9a 等）；Saif/Scif 可选合一，与独立配置互斥，已配独立再配抽象会失败 | EV-CA-02 §5.2/§7.1 |
| `TR-ND-05` | T-ND-05, T-ND-03 | 二次授权 → 网元信息 → 网管回流串行链 | `dependency_rule` | `explicit` | T-ND-05 二次授权 → T-ND-03 改网元信息（SET OMIP 是高危二次授权命令）→ T-ND-06 重对接网管（5 步重跑）；三者形成串行链 | EV-CA-02 §5.6/§7.3 |
| `TR-ND-06` | T-ND-06 | 网管密码三元组 | `validation_rule` | `explicit` | 北向对接用户必须重置密码；SNMP 用户必须重置共享认证密钥和共享加密密钥且两者不能相同；任一不满足对接直接失败（开局最常见原因） | EV-CA-02 §5.7 |
| `TR-ND-07` | T-ND-10, T-ND-12, T-ND-13 | 路由协议依赖 VPN 实例 + 接口绑定 | `input_output_rule` | `explicit` | 配置 OSPF/BGP/静态路由前必须先完成 T-ND-10（VPN 实例+地址族+接口绑定 IPBINDVPN），否则协议无承载容器 | EV-CA-02 §3.2层1 |
| `TR-ND-08` | T-ND-13 | BGP 是寄生协议 | `dependency_rule` | `implicit` | BGP 自身无自动部署（依赖 OSPF/静态 IGP 基础）；BGP 自身不能发现路由，必须 ADD IMPORTROUTE:IMPORTPROTOCOL=wlr；需专用 Loopback 建 eBGP（EBGPMAXHOP=10） | EV-CA-02 §5.8/§7.4 |
| `TR-ND-09` | T-ND-11 | 自动部署开关时序 | `dependency_rule` | `explicit` | 操作顺序：LST AUTOCONFIG → DSP OPSASSISTSTATE(autoscaling_autoconfig.py Ready) → SET AUTOCONFIG:SWITCHFLAG=FALSE → 配所有 AUTOSCALING 模板 → SET AUTOCONFIG:SWITCHFLAG=TRUE → DSP OPSASSISTSTATE(确认 Ready) | EV-CA-02 §3.2层5/§5.10 |
| `TR-ND-10` | T-ND-11 | 自动部署模板不可变 | `reuse_rule` | `explicit` | 自动部署完成后无法自动修改/删除已部署配置，需手动：关开关→删子接口→改模板→重开开关 | EV-CA-02 §7.7 |
| `TR-ND-11` | T-ND-12, T-ND-13, T-ND-15 | SDN 四强制 | `selection_rule` | `explicit` | SDN 场景：外联口 IP+下一跳强制 DHCP、强制单臂 BFD Echo(DEST=Leaf IP)、强制 BGP over 静态(不支持 OSPF)、强制 SET DHCP6CLIENTDUID | EV-CA-02 §4.1/§7.6 |
| `TR-ND-12` | T-ND-10, T-ND-13, T-ND-16 | MPLS VPN 公私分离 | `scope_rule` | `explicit` | MPLS VPN 外联口 VPN 固定 `_public_`（不绑业务 VPN）；Loopback 不绑 VPN；MP-EBGP 用 IPv4 eBGP 传 IPv6 私网路由（不配 IPv6 外联口）；VRFRD 必配且不重复；perInstance+perNexthop 节省标签 | EV-CA-02 §5.9/§7.5 |
| `TR-ND-13` | T-ND-04 | MTU 层级与同步 | `validation_rule` | `explicit` | 网卡 MTU ≥ Fabric MTU > 主接口 MTU ≥ 子接口 MTU；外联口 MTU 必须与直连下一跳网关一致（默认 1500）；仅改接口 MTU 不同步 MOD AUTOSCALINGSERVICE 触发 ALM-232398849；Eth-trunk 不改成员口 MTU，加入前改会失败 | EV-CA-02 §5.5 |
| `TR-ND-14` | T-ND-09 | IPv6 双栈地址族双配 | `input_output_rule` | `explicit` | IPv4v6 双栈：VPN 两个地址族(ipv4uni+ipv6uni)都要配；OSPF 与 OSPFv3 分别配；逻辑接口 IPVERSION=IPVER_ALL；APN 的 HASVPN 与 HASVPNIPV6 都 ENABLE；SDN 场景 SET DHCP6CLIENTDUID 必配 | EV-CA-02 §4.4 |
| `TR-ND-15` | T-ND-07 | UPINFO 全网唯一 | `validation_rule` | `explicit` | SET UPINFO:HOSTNAME 全网唯一，不配则 N4 偶联失败 | EV-CA-02 §6.1 |
| `TR-ND-16` | T-ND-09 | 地址池 LOCAL/EXTERNAL 范围 | `selection_rule` | `explicit` | LOCAL（UDG 主锚点分配 IP）需完整三件套（POOL+SECTION+POOLGROUP+POOLBINDGROUP+POOLGRPMAP）；EXTERNAL（辅锚点/ULCL/外部 NF 分配）仅 POOL+SECTION，可选 CHECKIPVALID | EV-CA-02 §3.4 |

---

## 3. TaskCommandOrderEdge（Task 内部命令顺序）

> 字段顺序遵循 Schema §10.5：`edge_id / task_ref / from_command_ref / to_command_ref / relation_type / condition_ref / requiredness / propagated_context / source_evidence_ids`。`from_command_ref`/`to_command_ref` 引用 04 层 `command_name`。

### 3.1 T-ND-07 配置 N4 控制面接口

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|------------------|-----------------|-----------------|----------------|----------------------|----------------------|
| `TE-ND-07-1` | T-ND-07 | `ADD VPNINST` | `ADD LOGICINF` | `precedes` | — | required | VPNINSTANCE=VPN_Signaling → LOGICINF.VPNINSTANCE | EV-CA-02 §3.1, EV-TK-03 KP-01/02 |
| `TE-ND-07-2` | T-ND-07 | `ADD LOGICINF` | `SET UPINFO` | `precedes` | — | required | NAME=N4if1/0/0；IPV4MASK1=255.255.255.255（固定） | EV-CA-02 §6.1, EV-TK-03 KP-02 |
| `TE-ND-07-3` | T-ND-07 | `SET UPINFO` | `SRVPING` | `depends_on` | — | optional | HOSTNAME → N4 偶联验证 | EV-CA-02 §6.1, EV-TK-07 |

### 3.2 T-ND-08 配置业务用户面接口（接入侧示例）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|------------------|-----------------|-----------------|----------------|----------------------|----------------------|
| `TE-ND-08-1` | T-ND-08 | `ADD VPNINST` | `ADD LOGICINF` | `precedes` | — | required | VPNINSTANCE=VPN_Access → LOGICINF.VPNINSTANCE | EV-CA-02 §3.1, EV-TK-03 KP-01 |
| `TE-ND-08-2` | T-ND-08 | `ADD LOGICINF` | `ADD SNSSAIUPINTF` | `precedes` | DP-CS2-04（切片绑定） | optional | NAME=Saif1/1/N → SNSSAIUPINTF.LOGICINFNAME（仅 Saif/N3if） | EV-CA-02 §6.2, EV-TK-03 KP-03 |

### 3.3 T-ND-09 配置会话接入（地址池五件套链）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|------------------|-----------------|-----------------|----------------|----------------------|----------------------|
| `TE-ND-09-1` | T-ND-09 | `ADD APN` | `ADD POOL` | `precedes` | — | required | APN, HASVPN=ENABLE, VPNINSTANCE → POOL（VPN 四统一） | EV-CA-02 §3.4, EV-TK-03 KP-09/10 |
| `TE-ND-09-2` | T-ND-09 | `ADD POOL` | `ADD SECTION` | `precedes` | — | required | POOLNAME → SECTION.POOLNAME；IPv6 LENGTH=64 | EV-CA-02 §3.4/§4.4, EV-TK-03 KP-10 |
| `TE-ND-09-3` | T-ND-09 | `ADD SECTION` | `ADD POOLGROUP` | `precedes` | — | required | POOLNAME | EV-CA-02 §3.4, EV-TK-03 KP-10 |
| `TE-ND-09-4` | T-ND-09 | `ADD POOLGROUP` | `ADD POOLBINDGROUP` | `precedes` | — | required | POOLGROUPNAME, POOLNAME → POOLBINDGROUP | EV-CA-02 §3.4, EV-TK-03 KP-10 |
| `TE-ND-09-5` | T-ND-09 | `ADD POOLBINDGROUP` | `ADD POOLGRPMAP` | `precedes` | — | required | POOLGROUPNAME → POOLGRPMAP；APN↔POOLGROUP 映射 | EV-CA-02 §3.4, EV-TK-03 KP-10 |
| `TE-ND-09-6` | T-ND-09 | `ADD POOLGRPMAP` | `SET IPALLOCRULE` | `precedes` | — | required | APN；FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0 | EV-CA-02 §3.4, EV-TK-03 KP-11 |
| `TE-ND-09-7` | T-ND-09 | `SET IPALLOCRULE` | `SET APNSGLPASS` | `precedes` | — | optional | APN（单通检测可选） | EV-CA-02 附录B.3, EV-TK-03 KP-09 |

### 3.4 T-ND-12 配置 OSPF 动态路由

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|------------------|-----------------|-----------------|----------------|----------------------|----------------------|
| `TE-ND-12-1` | T-ND-12 | `ADD VPNINST`（T-ND-10） | `ADD OSPF` | `depends_on` | — | required | VPNINSTANCE；OSPF 进程需 VPN 容器（TR-ND-07） | EV-CA-02 §3.2层1/§4.4, EV-TK-04 KP-02 |
| `TE-ND-12-2` | T-ND-12 | `ADD OSPF` | `ADD OSPFAREA` | `precedes` | — | required | OSPFPROCID, SCHEMAROUID → OSPFAREA；NSSA 区域需配 Loopback | EV-CA-02 §4.4, EV-TK-04 KP-02 |
| `TE-ND-12-3` | T-ND-12 | `ADD OSPFAREA` | `ADD OSPFINTERFACE` | `precedes` | — | required | OSPFPROCID, AREAID → OSPFINTERFACE | EV-CA-02 附录B.4, EV-TK-04 KP-02 |
| `TE-ND-12-4` | T-ND-12 | `ADD OSPFINTERFACE` | `ADD OSPFIMPORTROUTE` | `precedes` | — | required | IMPORTPROTOCOL=wlr（用户下行路由） | EV-CA-02 §5.8/§9.2, EV-TK-04 KP-02 |
| `TE-ND-12-5` | T-ND-12 | `ADD OSPF` | `ADD OSPFV3` | `precedes` | DP-CS4-04=IPv4v6 双栈 | optional | ROUTERID 共用；IPv6 分别配 OSPFv3（TR-ND-14） | EV-CA-02 §4.4, EV-TK-04 KP-05 |

### 3.5 T-ND-13 配置 BGP 路由

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|------------------|-----------------|-----------------|----------------|----------------------|----------------------|
| `TE-ND-13-1` | T-ND-13 | `SET BGP` | `ADD BGPVRF` | `precedes` | — | required | 全局使能；VRFNAME（MPLS: `_public_`）, ROUTERID | EV-CA-02 §3.2层2/§5.9, EV-TK-04 KP-04/10 |
| `TE-ND-13-2` | T-ND-13 | `ADD BGPVRF` | `ADD BGPVRFAF` | `precedes` | — | required | VRFNAME → BGPVRFAF；AFTYPE=ipv4/ipv6/ipv4vpn（MPLS MP-EBGP 开关） | EV-CA-02 §5.9, EV-TK-04 KP-04/10 |
| `TE-ND-13-3` | T-ND-13 | `ADD BGPVRFAF` | `ADD BGPPEER` | `precedes` | — | required | VRFNAME, AFTYPE → BGPPEER；EBGPMAXHOP=10（Loopback 邻居） | EV-CA-02 §5.8, EV-TK-04 KP-04 |
| `TE-ND-13-4` | T-ND-13 | `ADD BGPPEER` | `ADD BGPPEERAF` | `precedes` | — | required | PEERADDR → BGPPEERAF；APPLYLABELMODE=perNexthop 节省标签 | EV-CA-02 §5.9, EV-TK-04 KP-04/10 |
| `TE-ND-13-5` | T-ND-13 | `ADD BGPPEERAF` | `ADD IMPORTROUTE` | `precedes` | — | required | IMPORTPROTOCOL=wlr（BGP 不能发现路由，TR-ND-08） | EV-CA-02 §5.8, EV-TK-04 KP-04 |
| `TE-ND-13-6` | T-ND-13 | `ADD BGPPEERAF` | `ADD NETWORKROUTE` | `precedes` | — | optional | VRFNAME；Loopback 路由引入 BGP | EV-CA-02 附录B.4, EV-TK-04 KP-04 |

### 3.6 T-ND-11 配置外联口自动部署模板（开关时序链）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|------------------|-----------------|-----------------|----------------|----------------------|----------------------|
| `TE-ND-11-1` | T-ND-11 | `LST AUTOCONFIG` | `DSP OPSASSISTSTATE` | `precedes` | — | required | 确认 autoscaling_autoconfig.py 为 Ready（TR-ND-09） | EV-CA-02 §5.10, EV-TK-04 KP-01 |
| `TE-ND-11-2` | T-ND-11 | `DSP OPSASSISTSTATE` | `SET AUTOCONFIG` | `precedes` | — | required | SWITCHFLAG=FALSE（关开关） | EV-CA-02 §3.2层5, EV-TK-04 KP-01 |
| `TE-ND-11-3` | T-ND-11 | `SET AUTOCONFIG` | `ADD AUTOSCALINGETHTRUNK` | `precedes` | DP-CS4-06=SR-IOV bonding | optional | ETHTRUNKTMPID, VNICLIST（两 MAC 相同且 ID 连续） | EV-CA-02 §3.3, EV-TK-04/05 KP-08 |
| `TE-ND-11-4` | T-ND-11 | `ADD AUTOSCALINGETHTRUNK` / `SET AUTOCONFIG` | `ADD AUTOSCALINGSERVICE` | `precedes` | — | required | SERVICENAME, VPNNAME, AFTYPE, IPALLOCTYPE4/6, AUTOCFGIFTYPE（三态差异核心） | EV-CA-02 §3.3, EV-TK-04 KP-01 |
| `TE-ND-11-5` | T-ND-11 | `ADD AUTOSCALINGSERVICE` | `ADD AUTOSCALINGBFD` | `precedes` | DP-CS4-05=单臂 Echo | optional | SESSIONNAME, ONEARMECHO=TRUE（SDN/加速卡/双活强制） | EV-CA-02 §3.3/§4.1, EV-TK-04/06 |
| `TE-ND-11-6` | T-ND-11 | `ADD AUTOSCALINGSERVICE` | `ADD AUTOSCALINGSRROUTE` | `precedes` | DP-CS4-04=静态/BGP over 静态 | optional | PREFIX, NEXTHOP；SDN: DHCPENABLE=TRUE | EV-CA-02 §3.3/§4.2, EV-TK-04 KP-03 |
| `TE-ND-11-7` | T-ND-11 | `ADD AUTOSCALINGSERVICE` | `ADD AUTOSCALINGMPLS` | `precedes` | DP-CS4-07=MPLS VPN | optional | IFNAME（VM 扩容自动适配，替代手动 ADD MPLSIF） | EV-CA-02 §3.3/§4.2, EV-TK-04 KP-10 |
| `TE-ND-11-8` | T-ND-11 | `ADD AUTOSCALING*`（所有模板） | `SET AUTOCONFIG` | `must_be_last` | — | required | SWITCHFLAG=TRUE（开开关，激活下发） | EV-CA-02 §3.2层5/§5.10, EV-TK-04 KP-01 |
| `TE-ND-11-9` | T-ND-11 | `SET AUTOCONFIG`(TRUE) | `DSP OPSASSISTSTATE` | `depends_on` | — | required | 确认 Ready 后再做其他操作 | EV-CA-02 §5.10, EV-TK-04 KP-01 |

### 3.7 T-ND-18 整网调测与 FirstCall 验证（4 阶段顺序）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|------------------|-----------------|-----------------|----------------|----------------------|----------------------|
| `TE-ND-18-1` | T-ND-18 | `DSP SERVICERUSTATE` | `NGPING` | `precedes` | — | required | RU 全部正常 → 进入路由验证 | EV-CA-02 §9.2, EV-TK-07 KP-08 |
| `TE-ND-18-2` | T-ND-18 | `NGPING` | `DSP SRROUTE` / `DSP OSPFROUTING` / `LST BGPPEER` | `depends_on` | NGPING 丢包率=100% | optional | 路由异常分支定位（按协议类型） | EV-CA-02 §9.3, EV-TK-07 KP-08 |
| `TE-ND-18-3` | T-ND-18 | `DSP BGPPEERINFO` | `PING` | `precedes` | — | required | BGP=Established → 直连路由器→UDG 回程 | EV-CA-02 §9.2, EV-TK-07 KP-08 |
| `TE-ND-18-4` | T-ND-18 | `PING` | `DSP SESSIONINFO` | `must_be_last` | — | required | FirstCall 拨测成功标志：APN/RoleType/IPv4 PDP/Session 时间戳 4 参数 | EV-CA-02 §9.2/附录B.6, EV-TK-07 KP-08 |

---

## 4. ConfigTask 适用矩阵（Task × UPF 特性）

| Task | GWFD-010234 (Single IP) | GWFD-020161 (CU Full Mesh) | GWFD-010105 (地址分配) | GWFD-020421 (位置地址分配) | IPFD-010001 (接口管理) | NPFD-010014 (NTP) | NPFD-010000 (操作维护) | IPFD-014001 (OSPF) | IPFD-014002 (BGP) | IPFD-014003 (静态) | IPFD-012003 (BFD) | GWFD-020411 (MPLS VPN) | IPFD-015004 (IPsec) | GWFD-111201 (加速卡) |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T-ND-01 License | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ |
| T-ND-02 NTP | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-ND-03 网元信息 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-ND-04 公共参数+MTU | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-ND-05 二次授权 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ |
| T-ND-06 网管对接 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-ND-07 N4 控制面 | ★ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-ND-08 用户面接口 | ★ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-ND-09 会话接入 | ☆ | ☆ | ★ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-ND-10 VPN 实例 | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ |
| T-ND-11 自动部署模板 | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ★ |
| T-ND-12 OSPF | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-ND-13 BGP | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ★ | ☆ | ☆ |
| T-ND-14 静态路由 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ |
| T-ND-15 BFD | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ |
| T-ND-16 隧道 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ★ | ☆ |
| T-ND-17 级联口 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ |
| T-ND-18 调测 FirstCall | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |

> ★ = primary（主属特性，Task 在此特性下定义）  ☆ = optional（可选复用，特性可选用此 Task）

---

## 5. 端到端开局链路（FeatureTaskOrderEdge / 端到端流程）

> **Schema §9.7 FeatureTaskOrderEdge**：表达 task 间的稳定顺序与依赖。对接场景的端到端链路按 CS-5→CS-3→CS-1→CS-2→CS-4→调测 组织（来源：cross-topic-analysis.md §9.1）。

### 5.1 端到端 Task 编排主链（按对接面 CS × 流程顺序）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `condition_ref` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------------|-------------|-----------------|----------------|-----------------|-----------------|----------------|----------------------|----------------------|
| `FE-ND-01` | subfeature | CS-ND-05 内部 | T-ND-01 | T-ND-02 | `precedes` | — | required | License 生效 | EV-CA-02 §9.1 |
| `FE-ND-02` | subfeature | CS-ND-05 内部 | T-ND-02 | T-ND-05 | `precedes` | — | required | NTP 时间同步（证书前提） | EV-CA-02 §9.1 |
| `FE-ND-03` | subfeature | CS-ND-05 内部 | T-ND-05 | T-ND-03 | `precedes` | — | required | 二次授权完成（SET OMIP 是高危命令，TR-ND-05） | EV-CA-02 §5.6/§7.3 |
| `FE-ND-04` | subfeature | CS-ND-05 内部 | T-ND-03 | T-ND-04 | `precedes` | — | required | 网元身份+OM IP | EV-CA-02 §9.1 |
| `FE-ND-05` | subfeature | CS-5→CS-3 回流 | T-ND-03 | T-ND-06 | `depends_on` | — | required | 修改浮动 IP → 网管回流重对接（TR-ND-05 串行链） | EV-CA-02 §5.6/§7.3 |
| `FE-ND-06` | subfeature | CS-3→CS-1 | T-ND-06 | T-ND-07 | `precedes` | — | required | 网管对接完成（LST ME 成功）→ 进入控制面 | EV-CA-02 §9.1 |
| `FE-ND-07` | subfeature | CS-1→CS-2 | T-ND-07 | T-ND-08 | `precedes` | — | required | N4 控制面就绪（N4 偶联需数据面接口存在，TR-ND-01） | EV-CA-02 §5.1/§7.2 |
| `FE-ND-08` | subfeature | CS-ND-02 内部 | T-ND-08 | T-ND-09 | `precedes` | — | required | 业务面接口就绪 → 会话接入层（VPN 四统一 TR-ND-03） | EV-CA-02 §3.4/§6.2 |
| `FE-ND-09` | subfeature | CS-2→CS-4 | T-ND-09 | T-ND-10 | `precedes` | — | required | 会话接入完成 → 路由对接（用户下行路由 wlr 发布） | EV-CA-02 §9.1 |
| `FE-ND-10` | subfeature | CS-ND-04 内部 | T-ND-10 | T-ND-12 / T-ND-13 / T-ND-14 | `precedes` | DP-CS4-04（路由协议） | required | VPN 实例+接口绑定 → 路由协议（TR-ND-07） | EV-CA-02 §3.2层1/§9.1 |
| `FE-ND-11` | subfeature | CS-ND-04 内部 | T-ND-15 | T-ND-12 / T-ND-13 / T-ND-14 | `depends_on` | DP-CS4-05（BFD 模式） | optional | BFD 会话优先（静态路由 SESSIONNAME 绑定 BFD） | EV-CA-02 §3.2层2 |
| `FE-ND-12` | subfeature | CS-ND-04 内部 | T-ND-10 | T-ND-11 | `precedes` | DP-CS4-03=自动部署 | optional | 自动轨：VPN 实例 → AUTOSCALING 模板 | EV-CA-02 §3.2层5 |
| `FE-ND-13` | subfeature | CS-ND-04 内部 | T-ND-10 | T-ND-16 | `precedes` | DP-CS4-07（隧道叠加） | optional | VPN 实例 → 隧道（IPsec/GRE/MPLS VPN） | EV-CA-02 §4.3 |
| `FE-ND-14` | subfeature | CS-ND-04 内部 | T-ND-11 | T-ND-17 | `precedes` | DP-CS4-01=NP100 | optional | NP100 多框级联口（仅 NP 卡场景） | EV-CA-02 §4.3 |
| `FE-ND-15` | subfeature | CS-4→调测 | T-ND-12/T-ND-13/T-ND-14/T-ND-11/T-ND-16 | T-ND-18 | `depends_on` | — | required | 路由对接全部完成 → 整网调测 FirstCall | EV-CA-02 §9.1 |

### 5.2 7 个典型实例对应的 Task 组合（cross-topic-analysis 附录A）

| 实例 | UDG角色 / 路由 / IP / 部署 / SDN | 端到端 Task 组合 |
|------|----------------------------------|------------------|
| 1 | 融合 / OSPF / IPv4 / 自动 / 非SDN | T-ND-01~05 → T-ND-06 → T-ND-07 → T-ND-08~09 → T-ND-10 → T-ND-12(OSPFv4) → T-ND-11(AUTOSCALING, OSPFENABLE=TRUE) → T-ND-18 |
| 2 | 锚点 / OSPFv3 / IPv6 / 自动 / 非SDN | T-ND-01~05 → T-ND-06 → T-ND-07 → T-ND-08~09 → T-ND-10 → T-ND-12(OSPFv3) → T-ND-11(AUTOSCALING) → T-ND-18 |
| 3 | 边缘 / 静态 / IPv4 / 手动 / 非SDN | T-ND-01~05 → T-ND-06 → T-ND-07 → T-ND-08~09 → T-ND-10 → T-ND-15 → T-ND-14(静态v4) → T-ND-18 |
| 4 | 边缘 / BGP over OSPFv3 / IPv6 / 手动 / 非SDN | T-ND-01~05 → T-ND-06 → T-ND-07 → T-ND-08~09 → T-ND-10 → T-ND-12(OSPFv3) → T-ND-15 → T-ND-13(BGP) → T-ND-18 |
| 5 | PGW-U/UPF / BGP over 静态 / IPv4 / 自动 / **SDN** | T-ND-01~05 → T-ND-06 → T-ND-07 → T-ND-08~09 → T-ND-10 → T-ND-15(单臂BFD) → T-ND-14(静态,DHCPENABLE) → T-ND-11(AUTOSCALING,DHCP) → T-ND-13(BGP) → T-ND-18 |
| 6 | PGW-U/UPF / BGP over 静态 / IPv6 / 自动 / **SDN** | T-ND-01~05 → T-ND-06 → T-ND-07 → T-ND-08~09 → T-ND-10 → T-ND-15 → T-ND-14(静态v6) → T-ND-11(DHCP+DHCP6CLIENTDUID) → T-ND-13(BGP) → T-ND-18 |
| 7 | PGW-U/UPF / BGP over 静态 / IPv4v6 / 自动 / **SDN**（最完整） | T-ND-01~05 → T-ND-06 → T-ND-07 → T-ND-08~09 → T-ND-10(双栈地址族) → T-ND-15(单臂BFD) → T-ND-14(v4+v6) → T-ND-11(DHCP+DHCPv6 DUID) → T-ND-13(BGP双栈) → T-ND-18 |

---

## 6. 端到端链路样例（3 条完整 BD→NS→CS→Feature→Task→Command→Object）

> **SOP §5.5 要求**：至少给出 3 条完整端到端链路样例。引用 04-command-graph.md 的 command_name 与 ConfigObject。

### 样例 1：N4 控制面偶联（CS-1，UPF 唯一必备接口链路）

```
BD-ND 网元对接
  └─ NS-ND-UPF（UPF 网元对接子场景）
      └─ CS-ND-01 控制面对接方案（N4 ↔ SMF/SGW-C/PGW-C）
          ├─ Feature: GWFD-010234 Single IP（接口抽象合一能力）
          ├─ Feature: GWFD-020161 CU Full Mesh（多 SMF 场景，需 License）
          ├─ DecisionPoint: DP-CS1-01 IP 版本（IPv4/IPv6/双栈）, DP-CS1-02 多 SMF 对接
          ├─ BusinessRule: BR-N4-MANDATORY, BR-INTERFACE-FORCE-MERGE, BR-VPN-4UNIFY
          ├─ SemanticObject: SO_N4Interface, SO_VPN_Signaling, SO_UPFIdentity, SO_PFCPSession
          └─ ConfigTask:
              ├─ T-ND-07 配置 N4 控制面接口
              │   ├─ command_refs: ADD VPNINST → ADD LOGICINF → SET UPINFO
              │   ├─ ConfigObject: VPNInstance(VPN_Signaling) → N4Interface(N4if1/0/0) → UPFIdentity(HOSTNAME)
              │   ├─ TaskRule: TR-ND-01(N4 必备+数据面附加), TR-ND-02(掩码/32), TR-ND-04(强制合一), TR-ND-15(HOSTNAME 全网唯一)
              │   └─ TaskCommandOrderEdge: TE-ND-07-1/2/3（VPNINST→LOGICINF→UPINFO→SRVPING）
              └─ T-ND-18 调测（验证 N4 偶联）
                  └─ command_refs: SRVPING, DSP SESSIONINFO
```

### 样例 2：OSPF 自动部署路由（CS-4 实例 1，融合 OSPF IPv4 自动非SDN）

```
BD-ND 网元对接
  └─ NS-ND-UPF
      └─ CS-ND-04 路由对接方案（自动部署轨，非 SDN）
          ├─ Feature: IPFD-014001 OSPF, IPFD-010001 接口管理
          ├─ DecisionPoint: DP-CS4-01.A 无NP卡 / DP-CS4-02.A1 非SDN三层 / DP-CS4-03.A 自动 / DP-CS4-04 OSPFv4 / DP-CS4-06 子接口
          ├─ BusinessRule: BR-VPN-4UNIFY, BR-AUTOCONFIG-SWITCH, BR-MTU-HIERARCHY
          ├─ SemanticObject: SO_VPNInstance, SO_OSPFProcess, SO_OSPFArea, SO_AutoScalingTemplate, SO_ExternalInterface
          └─ ConfigTask 链:
              ├─ T-ND-10 配置 VPN 实例与接口绑定
              │   ├─ command_refs: ADD L3VPNINST → ADD VPNINSTAF → ADD VPNTARGET → ADD IPBINDVPN
              │   └─ ConfigObject: L3VPNInstance(VPN_Access) → VPNAddressFamily(ipv4uni) → VPNTarget → IPBINDVPN
              ├─ T-ND-12 配置 OSPF 动态路由
              │   ├─ command_refs: ADD OSPF → ADD OSPFAREA → ADD OSPFINTERFACE → ADD OSPFIMPORTROUTE
              │   ├─ ConfigObject: OSPFProcess → OSPFArea → OSPFInterface; IMPORTPROTOCOL=wlr
              │   ├─ TaskRule: TR-ND-07(依赖 VPN 实例), TR-ND-14(双栈双配)
              │   └─ TaskCommandOrderEdge: TE-ND-12-1/2/3/4
              ├─ T-ND-11 配置外联口自动部署模板（OSPFENABLE=TRUE）
              │   ├─ command_refs: LST AUTOCONFIG → DSP OPSASSISTSTATE → SET AUTOCONFIG(FALSE) → ADD AUTOSCALINGSERVICE(OSPFENABLE=TRUE) → SET AUTOCONFIG(TRUE) → DSP OPSASSISTSTATE
              │   ├─ ConfigObject: AutoConfigSwitch → AutoScalingService（activates OSPFProcess）
              │   ├─ TaskRule: TR-ND-09(开关时序), TR-ND-10(模板不可变)
              │   └─ TaskCommandOrderEdge: TE-ND-11-1/2/4/8/9（must_be_last）
              └─ T-ND-18 调测（NGPING 丢包 0% + DSP OSPFROUTING 路由负荷分担）
```

### 样例 3：SDN BGP over 静态双栈链路（CS-4 实例 7，最完整 SDN 场景）

```
BD-ND 网元对接
  └─ NS-ND-UPF
      └─ CS-ND-04 路由对接方案（SDN 自动部署轨）
          ├─ Feature: IPFD-014002 BGP, IPFD-014003 静态路由, IPFD-012003 BFD, IPFD-010001 接口管理
          ├─ DecisionPoint: DP-CS4-02.B SDN / DP-CS4-03.A 自动 / DP-CS4-04 BGP over 静态双栈 / DP-CS4-05.B 单臂 Echo
          ├─ BusinessRule: BR-BGP-DEPENDENCY, BR-AUTOCONFIG-SWITCH（SDN 四强制）
          ├─ SemanticObject: SO_VPNInstance(VRF_*), SO_StaticRoute, SO_BGPInstance, SO_BGPPeer, SO_BFDSession, SO_LoopbackInterface, SO_NetworkMode
          └─ ConfigTask 链:
              ├─ T-ND-10 配置 VPN 实例与接口绑定（双栈 ipv4uni+ipv6uni，TR-ND-14）
              │   └─ ConfigObject: L3VPNInstance(VRF_Internet) → VPNAddressFamily(ipv4uni + ipv6uni)
              ├─ T-ND-15 配置 BFD 检测（强制单臂 Echo，DEST=Leaf IP）
              │   ├─ command_refs: SET BFD → ADD AUTOSCALINGBFD(ONEARMECHO=TRUE)
              │   └─ TaskRule: TR-ND-11(SDN 四强制)
              ├─ T-ND-14 配置静态路由（DHCPENABLE=TRUE，v4+v6 分别配）
              │   ├─ command_refs: ADD AUTOSCALINGSRROUTE(v4) → ADD AUTOSCALINGSRROUTE(v6)
              │   └─ ConfigObject: AutoScalingSRRoute; SESSIONNAME 绑定 BFD
              ├─ T-ND-11 配置外联口自动部署模板（IPALLOCTYPE4/6=DHCP, NEXTHOPALLOCTYPE4/6=DHCP, AUTOCFGIFTYPE=VNIC/ETHTRUNK）
              │   ├─ 前置: SET DHCP6CLIENTDUID:DUIDTYPE=MAC_PLUS_VLAN（SDN 强制）
              │   ├─ command_refs: SET AUTOCONFIG(FALSE) → ADD AUTOSCALINGETHTRUNK → ADD AUTOSCALINGSERVICE(DHCP) → ADD AUTOSCALINGBFD → ADD AUTOSCALINGSRROUTE → SET AUTOCONFIG(TRUE)
              │   └─ ConfigObject: AutoConfigSwitch → AutoScalingService(DHCP) → AutoScalingEthTrunk
              ├─ T-ND-13 配置 BGP 路由（依赖 IGP 自动部署基础，专用 Loopback eBGP）
              │   ├─ command_refs: SET BGP → ADD BGPVRF → ADD BGPVRFAF → ADD BGPPEER(EBGPMAXHOP=10) → ADD BGPPEERAF → ADD IMPORTROUTE(wlr)
              │   ├─ ConfigObject: BGPInstance → BGPVRF → BGPAddressFamily → BGPPeer; Loopback 不绑 VPN
              │   ├─ TaskRule: TR-ND-08(BGP 寄生), TR-ND-11(SDN 四强制), TR-ND-14(双栈双配)
              │   └─ TaskCommandOrderEdge: TE-ND-13-1/2/3/4/5
              └─ T-ND-18 调测（NGPING 丢包 0% + LST BGPPEER + DSP BGPPEERINFO=Established + DSP SESSIONINFO 双栈 FirstCall）
```

---

## 7. 与计费场景任务层的对比

| 维度 | 计费场景 | 网元对接场景（本文件） |
|------|---------|----------------------|
| 场景性质 | 业务配置类（计费能力配置） | 对接类（开局组网对接） |
| ConfigTask 数量 | 27（generic 8 + feature_specific 19） | 18（generic 10 + feature_specific 4 + cross_feature 4） |
| TaskRule 数量 | 6 | 16 |
| TaskCommandOrderEdge 数量 | 20 | 36 task 内部边 + 15 端到端 FeatureTaskOrderEdge |
| task 主线 | 业务开通流程（三件套 URR→URRGROUP→PCCPOLICYGRP） | 开局流程（CS-5→CS-3→CS-1→CS-2→CS-4→FirstCall） |
| 独有 task 族 | 计费三件套、在线计费(DCC/OCS)、融合计费(CHF/CCT)、CG 接口 | 基础就绪(License/NTP/二次授权)、网管对接(5步闭包)、N4 控制面、用户面接口+会话接入、路由对接(OSPF/BGP/静态/BFD/隧道/级联口)、自动部署模板族、FirstCall 调测 |
| task 复用度 | 偏 feature_specific（19/27） | 偏 generic/cross_feature（14/18，对接步骤多跨特性复用） |
| 共享对象 | — | VPNInstance、LogicInterface、APN、AddressPool（与未来会话类场景潜在共享） |

---

## 8. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| ConfigTask | 18 | T-ND-01~T-ND-18（generic 10: 01~05/11~15 + feature_specific 4: 07/08/09/17 + cross_feature 4: 06/10/16/18） |
| TaskRule | 16 | TR-ND-01~TR-ND-16 |
| TaskCommandOrderEdge（task 内部） | 36 | TE-ND-07(3) / 08(2) / 09(7) / 11(9) / 12(5) / 13(6) / 18(4) 系列 |
| FeatureTaskOrderEdge（端到端） | 15 | FE-ND-01~FE-ND-15 |
| **任务层对象总计** | **85** | — |

---

## 9. §13 禁止关系合规声明

本文件严格遵守 Schema §13 禁止关系：

- **ConfigTask `invokes` MMLCommand**（§10.6 正向），命令引用 04-command-graph.md 的 `command_name`（如 `ADD VPNINST`），不跳层到 CommandParameter 写死参数值
- **ConfigTask `targets` SemanticObject / ConfigObject**（§10.6），不直接持有 ConfigObject 实例（实例由 04 层定义）
- **ConfigTask `constrained_by` TaskRule**（§10.6），TaskRule `refined_by` 04 层 CommandRule（如 TR-ND-11 SDN 四强制 → CR-ND-05），规则不跳层
- **ConfigurationSolution `uses_task` ConfigTask**（§12.2），01 层 CS 不直接持命令实例；本层定义权威 task_id，01 层 uses_task 引用
- **Feature `decomposes_to` ConfigTask**（§12.3），特性不跳层直接落命令；本层 ConfigTask 适用矩阵（§4）表达 Feature↔Task 的 primary/optional 关系
- **端到端顺序由 FeatureTaskOrderEdge 承接**（§9.7），不进入 ConfigurationSolution→ConfigTask 主 schema（条件分支过强，由实例层承接）

---

> 本文件为网元对接三层图谱第3层。第4层命令图谱（04-command-graph.md，103 命令）、第5层跨层映射、第6层证据索引见同目录其他文件。task 的 `command_refs` 引用 04 层 `command_name`，01 层 `uses_task` 引用本层 `task_id`/`task_name`。
