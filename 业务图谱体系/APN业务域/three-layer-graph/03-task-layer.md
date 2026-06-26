# APN 业务域三层图谱 · 第 3 层：任务原子层

> **文件定位**：`three-layer-graph/03-task-layer.md`
> **Schema 参考**：`三层图谱Schema-最终版-v0.1.md` §10 任务原子层（ConfigTask / TaskRule / TaskCommandOrderEdge + §10.6 关系）
> **作用**：实例化 APN 业务域 ConfigTask + TaskRule + TaskCommandOrderEdge，作为特性（§9）与命令（§11）之间的解耦原子层
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（附录 D 9 端到端流程 73 步、附录 B 命令交叉参考、附录 C 配置对象复用矩阵）、37 篇 feature-knowledge（§配置/§配置对象）
> **上游一致性**：Task ID 严格对齐 `02-feature-graph.md` §6 FeatureTaskOrderEdge 中预定义的 `T-xxx` 占位（6 个核心 Feature 已锁定编号，纯数字对齐访问限制 graph_parser）；本文件补充其余 Feature 的 ConfigTask 实例化

---

## §0 任务层总览

### 0.1 ConfigTask 分类

| 类型 | 数量 | 编号范围 | 说明 |
|------|------|---------|------|
| generic（通用，跨特性复用） | 3 | T-001, T-006, T-007 | VPN 实例准备 / 策略刷新 / License 开启（跨地址分配+隧道+鉴权共用） |
| feature_specific（特性专属） | 58 | T-002~005, T-101~310, T-401~511, T-601~708 | 按 feature_group 分族：地址分配 / 双栈 / 隧道 / 鉴权 / 网元选择 / 接入控制 / 别名 / 底座 |
| **合计** | **61** | — | — |

> **Task 编号段说明**：
> - `T-001~007`：GWFD-010105 用户面地址分配（附录 D.1 6 步 + REFRESHSRV），其中 001/006/007 为 generic
> - `T-101~109`：GWFD-020403 IPv4v6 双栈（附录 D.2 9 步）
> - `T-201~208`：GWFD-020412 L2TP VPN U 面 LAC 执行（附录 D.3 U 侧）
> - `T-301~307`：WSFD-011306/011305 Radius 鉴权级联（附录 D.6 R1~A2 + REFRESHSRV）
> - `T-401~406`：WSFD-107010 UPF 选择三轮筛选（附录 D.7）
> - `T-501~504`：WSFD-106003 接入控制 C 面（附录 D.8 C 侧）
> - `T-601~608`：IPFD-015002 GRE + IPFD-015004/016000 IPSec（附录 D.4/D.5）
> - `T-701~708`：别名 APN / DHCP / MPLS / 对等网元选择 / 底座运维 / L2TP-C 决策 / UNC 地址分配 / 静态路由冗余（补全 9 端到端流程之外的剩余特性）

### 0.2 任务原子化原则

1. **每 Task 一个明确 goal**：附录 D 一个步骤或一组语义内聚的命令成一个 Task，不细到单条 MML
2. **generic 严格收敛**：跨 3+ feature_group 复用的步骤才提升为 generic（本域仅 VPN 准备/REFRESHSRV/LICENSE 三类）
3. **feature_specific 保留特性语义**：UDG/UNC 命令前缀不对称（POOL vs ADDRPOOL、L2TPN4KEY vs L2TPKEY、APNL2TPATTR vs APNL2TPCTRL）在 task 层分离建模，避免混淆
4. **命令内部顺序由 TaskCommandOrderEdge 表达**；Task 间顺序由 `05-cross-layer-mapping.md` 的 FeatureTaskOrderEdge 表达（已由 F02 §6 FTOE-APN-001~036 定义）
5. **最小可复用原子粒度**：不大到变方案（如"整个 L2TP 流程"），不小到单命令（如"ADD POOL"独立成 task）

### 0.3 与带宽/计费场景编号段隔离

> APN 业务域 Task 使用纯数字编号 `T-xxx`（批次5 去除 APN 前缀，对齐访问限制场景 graph_parser 解析要求），各场景图谱文件独立解析故不冲突。generic Task 本域自定义，不复用带宽场景的 `T-001~T-008`（因 APN 域无 PCC/SA 体系）。

---

## §1 通用 Task（generic，3 个）

### T-001 VPN 实例与地址族准备

| 字段 | 值 |
|------|---|
| `task_id` | `T-001` |
| `task_name` | `VPN 实例与地址族准备` |
| `task_summary` | 建立 VPN 实例与 IPv4/IPv6 地址族，为地址分配与隧道类提供 VPN 基础设施 |
| `task_scope_type` | `generic` |
| `task_goal` | 输出 L3VPNINST + VPNINSTAF（AFTYPE=ipv4uni/ipv6uni）实例，承载 APN/POOL/隧道接口的 VPN 绑定 |
| `input_contract` | VPN 命名规划、IPv4/IPv6 地址族需求 |
| `output_contract` | L3VPNINST + VPNINSTAF 实例集（含双栈双实例） |
| `command_refs` | ADD L3VPNINST, ADD VPNINSTAF, ADD VPNINST |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-06`, `EV-FK-16`, `EV-FK-18`, `EV-FK-29`, `EV-FK-30`, `EV-CA-01` |
| `reused_by` | GWFD-010105, GWFD-020401, GWFD-020403, GWFD-020406, GWFD-020411, GWFD-020412, IPFD-015002, IPFD-015004, IPFD-016000, WSFD-011306, WSFD-108007 |
| `targets` | ConfigObject: `L3VPNINST`, `VPNINSTAF` |

### T-006 策略刷新生效

| 字段 | 值 |
|------|---|
| `task_id` | `T-006` |
| `task_name` | `策略刷新生效` |
| `task_summary` | 执行 SET REFRESHSRV 使 UDG 侧配置变更生效 |
| `task_scope_type` | `generic` |
| `task_goal` | 使地址分配/隧道/接入控制类 UDG 配置生效（REFRESHSRV 是 UDG 配置链的统一终点） |
| `input_contract` | 所有相关策略/地址池/隧道配置完成 |
| `output_contract` | 配置下发生效 |
| `command_refs` | SET REFRESHSRV |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-06`, `EV-FK-11`, `EV-FK-37`, `EV-CA-01` |
| `reused_by` | GWFD-010105, GWFD-020403, GWFD-020412, GWFD-010151（U 侧带宽流控生效） |
| `must_be_last` | `true` |
| `note` | 仅 UDG 侧需要；UNC 侧 PCC/Radius 类配置即时生效或经 PFCP 信令触发，不走 REFRESHSRV |

### T-007 License 开启

| 字段 | 值 |
|------|---|
| `task_id` | `T-007` |
| `task_name` | `License 开启` |
| `task_summary` | 通过 SET LICENSESWITCH 开启特性 License，是 13 个需 License 特性的前置门控 |
| `task_scope_type` | `generic` |
| `task_goal` | 满足 License 前置门控，使需 License 特性功能可用 |
| `input_contract` | 特性清单、对应 License 项（LKV 编号） |
| `output_contract` | License 使能 |
| `command_refs` | SET LICENSESWITCH |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-07`, `EV-FK-08`, `EV-FK-11`, `EV-FK-18`, `EV-FK-20`, `EV-FK-21`, `EV-FK-27`, `EV-FK-31`, `EV-FK-32`, `EV-FK-33`, `EV-FK-34`, `EV-FK-05`, `EV-FK-36`, `EV-CA-01` |
| `reused_by` | 全部 13 个需 License 特性（IPv6 三件套 + 基于位置 + MPLS + L2TP-U + 二次鉴权 + ARD-B + UPF 选择双 + 别名 APN 双） |
| `note` | IPv6 承载 License 串联链是地址分配域最长依赖路径：LKV3G5V6PB01 → LKV3G5VDSA01 → LKV3G5P6PD01（UDG）+ LKV3W9V6PD11（UNC） |

---

## §2 地址分配族（feature_specific，GWFD-010105 + GWFD-010107 + GWFD-020421 + GWFD-010108）

### T-002 APN 实例与地址属性配置

| 字段 | 值 |
|------|---|
| `task_id` | `T-002` |
| `task_name` | `APN 实例与地址属性配置` |
| `task_summary` | ADD APN 定义 APN/DNN 实例（含 HASVPN/HASVPNIPV6 双栈绑定），SET APNADDRESSATTR 定义地址支持属性 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 APN/DNN 实例并声明其支持的 IPv4/IPv6 地址类型与 VPN 绑定 |
| `input_contract` | T-001 输出的 VPN 实例、APN 命名规划 |
| `output_contract` | APN 实例 + APNADDRESSATTR 配置 |
| `command_refs` | ADD APN, SET APNADDRESSATTR |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-06`, `EV-FK-07`, `EV-FK-08`, `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-010104, GWFD-010105, GWFD-010107, GWFD-020421, GWFD-020403, GWFD-020406 |
| `targets` | ConfigObject: `APN`, `APNADDRESSATTR`; SemanticObject: `SO-APN-ADDRESS-POOL` |
| `note` | ADD APN 是跨域共用挂载点（地址分配 + 接入控制 + 鉴权 + 别名 APN 均依赖） |

### T-003 地址池配置（UDG 侧 POOLTYPE=LOCAL）

| 字段 | 值 |
|------|---|
| `task_id` | `T-003` |
| `task_name` | `地址池配置（UDG 侧 POOLTYPE=LOCAL）` |
| `task_summary` | UDG 侧 ADD POOL(POOLTYPE=LOCAL), ADD SECTION, ADD POOLGROUP, ADD POOLBINDGROUP 四件套 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 UDG 本地地址池、地址段、池组及绑定关系（与 UNC 侧 ADDRPOOL 前缀不对称） |
| `input_contract` | T-001 VPN 实例、T-002 APN 实例、地址段规划 |
| `output_contract` | POOL + SECTION + POOLGROUP + POOLBINDGROUP 实例集 |
| `command_refs` | ADD POOL, ADD SECTION, ADD POOLGROUP, ADD POOLBINDGROUP |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-06`, `EV-FK-07`, `EV-FK-10`, `EV-FK-08`, `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-010104, GWFD-010105, GWFD-010107, GWFD-020421, GWFD-020403, GWFD-020406 |
| `targets` | ConfigObject: `POOL`, `SECTION`, `POOLGROUP`, `POOLBINDGROUP`; SemanticObject: `SO-APN-ADDRESS-POOL` |
| `note` | TR-APN-03 校验：UDG 侧 POOLTYPE 必须为 LOCAL（非 EXTERNAL）；APN 的 VPN 与 POOL 的 VPN 必须一致 |

### T-004 池组映射（基于 APN/LOCATION/SMF）

| 字段 | 值 |
|------|---|
| `task_id` | `T-004` |
| `task_name` | `池组映射（基于 APN/LOCATION/SMF）` |
| `task_summary` | ADD POOLGRPMAP 定义映射条件（APN / LOCATION / SMF 任意组合） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 将池组按 APN/DNN、位置区、SMF 三维度映射，决定地址分配选池规则 |
| `input_contract` | T-003 输出的 POOLGROUP 实例 |
| `output_contract` | POOLGRPMAP 实例 |
| `command_refs` | ADD POOLGRPMAP |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-06`, `EV-FK-07`, `EV-FK-10`, `EV-FK-08`, `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-010104, GWFD-010105, GWFD-010107, GWFD-020421, GWFD-020403, GWFD-020406 |
| `targets` | ConfigObject: `POOLGRPMAP`; SemanticObject: `SO-APN-ADDRESS-POOL` |
| `note` | UNC 侧同样使用 ADD POOLGRPMAP（命令同名），但前置 POOLGROUP 换为 ADDRPOOLGRP |

### T-005 地址分配规则与下行路由发布

| 字段 | 值 |
|------|---|
| `task_id` | `T-005` |
| `task_name` | `地址分配规则与下行路由发布` |
| `task_summary` | SET IPALLOCRULE, SET APNIPALLOCRULE 定义三级分配规则，ADD OSPF, ADD OSPFIMPORTROUTE(PROTOCOL=wlr) 发布下行路由 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 配置全局/APN 级地址分配优先级，并通过 OSPF/OSPFv3 将用户面地址段引入 WLR 路由 |
| `input_contract` | T-003 POOL 实例、T-004 POOLGRPMAP、IPv4/IPv6 地址族决策 |
| `output_contract` | IPALLOCRULE/APNIPALLOCRULE + OSPF/OSPFv3 进程配置 |
| `command_refs` | SET IPALLOCRULE, SET APNIPALLOCRULE, ADD OSPF, ADD OSPFAREA, ADD OSPFNETWORK, ADD OSPFIMPORTROUTE, ADD OSPFV3, ADD OSPFV3AREA, ADD OSPFV3IMPORTROUTE |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-06`, `EV-FK-08`, `EV-FK-18`, `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-010105, GWFD-020421, GWFD-020406, GWFD-010107, GWFD-020403, GWFD-020401 |
| `targets` | ConfigObject: `IPALLOCRULE`, `APNIPALLOCRULE`, `OSPF`, `OSPFV3`; SemanticObject: `SO-APN-ADDRESS-POOL` |
| `note` | IPv6 承载需额外 OSPFV3 进程（由 GWFD-020401 提供）；GWFD-020421 位置分配需先 SET IPALLOCBYLOCGLBSW |

---

## §3 双栈族（feature_specific，GWFD-020403 IPv4v6 双栈 9 步）

> 附录 D.2 全流程。T-101~109 已在 F02 §6.2 FTOE-APN-007~015 锁定顺序。

### T-101 双 License 使能（V6PB01 + VDSA01）

| 字段 | 值 |
|------|---|
| `task_id` | `T-101` |
| `task_name` | `双 License 使能（V6PB01 + VDSA01）` |
| `task_summary` | 串联使能 IPv6 承载底座 License（LKV3G5V6PB01）+ 双栈能力使能 License（LKV3G5VDSA01） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 满足 IPv6 承载 + 双栈能力的线性 License 依赖链（地址分配域最长依赖路径起点） |
| `input_contract` | IPv6 承载需求、双栈能力需求 |
| `output_contract` | 两项 License 使能 |
| `command_refs` | SET LICENSESWITCH |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-FK-18`, `EV-CA-01` |
| `feature_ref` | GWFD-020403, GWFD-020401 |
| `targets` | License: `LKV3G5V6PB01`, `LKV3G5VDSA01` |
| `note` | 串联链：V6PB01（承载底座）→ VDSA01（双栈能力使能层）；GWFD-020403 是能力使能层，不替代 GWFD-010105 的分配机制 |

### T-102 VPN 双实例（IPv4 + IPv6 地址族激活）

| 字段 | 值 |
|------|---|
| `task_id` | `T-102` |
| `task_name` | `VPN 双实例（IPv4 + IPv6 地址族激活）` |
| `task_summary` | 建立 IPv4 VPN + IPv6 VPN 双实例，IPv6 需 ADD VPNINSTAF AFTYPE=ipv6uni 激活地址族 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 为双栈地址分配准备 IPv4/IPv6 双 VPN 基础设施 |
| `input_contract` | T-101 License 使能 |
| `output_contract` | IPv4 VPN + IPv6 VPN 双实例 |
| `command_refs` | ADD VPNINST, ADD L3VPNINST, ADD VPNINSTAF |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-FK-18`, `EV-CA-01` |
| `feature_ref` | GWFD-020403, GWFD-020401, GWFD-020406 |
| `targets` | ConfigObject: `VPNINSTAF`; SemanticObject: `SO-APN-ADDRESS-POOL` |
| `note` | TR-APN-04 校验：IPv6 地址族必须 AFTYPE=ipv6uni；双栈为 IPv4 VPN + IPv6 VPN 双实例 |

### T-103 双栈 APN（HASVPN + HASVPNIPV6 双绑定）

| 字段 | 值 |
|------|---|
| `task_id` | `T-103` |
| `task_name` | `双栈 APN（HASVPN + HASVPNIPV6 双绑定）` |
| `task_summary` | ADD APN 同时绑定 IPv4 VPN（HASVPN+VPNINSTANCE）与 IPv6 VPN（HASVPNIPV6+VPNINSTANCEIPV6） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 APN/DNN 级双栈 VPN 绑定 |
| `input_contract` | T-102 双 VPN 实例 |
| `output_contract` | 双栈 APN 实例 |
| `command_refs` | ADD APN |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-020403 |
| `targets` | ConfigObject: `APN`; SemanticObject: `SO-APN-ADDRESS-POOL` |

### T-104 双池双段（IPv4 POOL + IPv6 POOL 并存）

| 字段 | 值 |
|------|---|
| `task_id` | `T-104` |
| `task_name` | `双池双段（IPv4 POOL + IPv6 POOL 并存）` |
| `task_summary` | 建立 IPv4 POOL+SECTION 与 IPv6 POOL+SECTION 双地址池（V6PREFIXLENGTH=64 普通 / <64 切换 PD） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 为双栈 APN 提供 IPv4/IPv6 双地址段资源 |
| `input_contract` | T-103 双栈 APN、IPv4/IPv6 地址段规划 |
| `output_contract` | IPv4 POOL+SECTION + IPv6 POOL+SECTION |
| `command_refs` | ADD POOL, ADD SECTION |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-FK-20`, `EV-CA-01` |
| `feature_ref` | GWFD-020403, GWFD-020406 |
| `targets` | ConfigObject: `POOL`, `SECTION`; SemanticObject: `SO-APN-ADDRESS-POOL` |
| `note` | TR-APN-04：V6PREFIXLENGTH=64 为普通 IPv6 单栈；<64 切换为 IPv6 Prefix Delegation 模式（GWFD-020406） |

### T-105 双池绑定同组（双优先级算法使能）

| 字段 | 值 |
|------|---|
| `task_id` | `T-105` |
| `task_name` | `双池绑定同组（双优先级算法使能）` |
| `task_summary` | ADD POOLGROUP 同时使能 IPV4ALLOCPRIALG/IPV6ALLOCPRIALG，ADD POOLBINDGROUP 将双池绑入同组 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 将 IPv4/IPv6 双池组织为同一池组，启用双栈优先级分配算法 |
| `input_contract` | T-104 双池双段 |
| `output_contract` | 双优先级算法 POOLGROUP + POOLBINDGROUP |
| `command_refs` | ADD POOLGROUP, ADD POOLBINDGROUP |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-020403 |
| `targets` | ConfigObject: `POOLGROUP`, `POOLBINDGROUP` |

### T-106 APN 级双栈属性

| 字段 | 值 |
|------|---|
| `task_id` | `T-106` |
| `task_name` | `APN 级双栈属性` |
| `task_summary` | SET APNADDRESSATTR 声明 APN 同时 SUPPORTIPV4=ENABLE + SUPPORTIPV6=ENABLE |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 APN 级别显式声明双栈支持 |
| `input_contract` | T-103 双栈 APN |
| `output_contract` | APNADDRESSATTR 双栈配置 |
| `command_refs` | SET APNADDRESSATTR |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-020403, GWFD-020406 |
| `targets` | ConfigObject: `APNADDRESSATTR` |

### T-107 双栈池组映射

| 字段 | 值 |
|------|---|
| `task_id` | `T-107` |
| `task_name` | `双栈池组映射` |
| `task_summary` | ADD POOLGRPMAP 将双栈池组映射到 APN |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成双栈池组到 APN 的映射 |
| `input_contract` | T-105 双优先级池组、T-103 双栈 APN |
| `output_contract` | 双栈 POOLGRPMAP 实例 |
| `command_refs` | ADD POOLGRPMAP |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-020403 |
| `targets` | ConfigObject: `POOLGRPMAP` |

### T-108 下行路由发布（OSPF + OSPFv3 双进程）

| 字段 | 值 |
|------|---|
| `task_id` | `T-108` |
| `task_name` | `下行路由发布（OSPF + OSPFv3 双进程）` |
| `task_summary` | IPv4 侧 ADD OSPF, ADD OSPFIMPORTROUTE(PROTOCOL=wlr)，IPv6 侧 ADD OSPFV3, ADD OSPFV3IMPORTROUTE(PROTOCOL=wlr) 双进程 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 将 IPv4/IPv6 用户面地址段分别通过 OSPF/OSPFv3 引入 WLR 路由 |
| `input_contract` | T-104 双池双段、T-102 双 VPN |
| `output_contract` | OSPF + OSPFv3 双进程配置 |
| `command_refs` | ADD OSPF, ADD OSPFAREA, ADD OSPFNETWORK, ADD OSPFIMPORTROUTE, ADD OSPFV3, ADD OSPFV3AREA, ADD OSPFV3IMPORTROUTE |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-FK-18`, `EV-CA-01` |
| `feature_ref` | GWFD-020403, GWFD-020401 |
| `note` | OSPFv3 进程由 GWFD-020401 IPv6 承载上下文提供（跨 Feature 协同） |

### T-109 RA 通告（GWFD-020403 独有）

| 字段 | 值 |
|------|---|
| `task_id` | `T-109` |
| `task_name` | `RA 通告（GWFD-020403 独有）` |
| `task_summary` | UDG 主动下发 Router Advertisement（由 License LKV3G5VDSA01 使能，GWFD-010105 未涉及） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成 IPv6 双栈的 RA 通告（双栈能力使能层独有能力） |
| `input_contract` | T-101 VDSA01 License 使能、T-104 IPv6 POOL |
| `output_contract` | RA 通告使能 |
| `command_refs` | （由 License 使能后自动生效，无独立 MML） |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-16`, `EV-CA-01` |
| `feature_ref` | GWFD-020403 |
| `note` | 双栈能力使能层独有，区别于 GWFD-010105 机制层 |

---

## §4 L2TP-VPN 族（feature_specific，GWFD-020412 U 面 LAC 执行 8 步）

> 附录 D.3 U 侧。T-201~208 已在 F02 §6.3 FTOE-APN-016~022 锁定顺序。C 侧决策见 T-706。

### T-201 L2TP License 使能（LKV3G5L2TP01）

| 字段 | 值 |
|------|---|
| `task_id` | `T-201` |
| `task_name` | `L2TP License 使能（LKV3G5L2TP01）` |
| `task_summary` | SET LICENSESWITCH 使能 UDG 侧 L2TP 必需 License（82200BVC LKV3G5L2TP01，C 侧无 License） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 满足 U 侧 LAC 执行的 License 前置（C-U License 不对称） |
| `input_contract` | L2TP VPN 业务需求 |
| `output_contract` | U 侧 L2TP License 使能 |
| `command_refs` | SET LICENSESWITCH |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `feature_ref` | GWFD-020412 |
| `targets` | License: `LKV3G5L2TP01` |
| `note` | TR-APN-05：C-U License 不对称，UNC 侧 WSFD-104410 无 License 要求 |

### T-202 L2TP VPN 实例与 Giif 接口

| 字段 | 值 |
|------|---|
| `task_id` | `T-202` |
| `task_name` | `L2TP VPN 实例与 Giif 接口` |
| `task_summary` | ADD VPNINST, ADD LOGICINF(giif), ADD APN 建立 L2TP 承载基础 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 L2TP VPN 实例与 Gi 逻辑接口，挂载 APN |
| `input_contract` | T-201 License、VPN 命名 |
| `output_contract` | VPNINST + LOGICINF + APN 实例 |
| `command_refs` | ADD VPNINST, ADD LOGICINF, ADD APN |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `feature_ref` | GWFD-020412 |
| `targets` | ConfigObject: `VPNINST`, `LOGICINF`, `APN` |

### T-203 SET APNL2TPATTR（U 面核心 10+ 参数）

| 字段 | 值 |
|------|---|
| `task_id` | `T-203` |
| `task_name` | `SET APNL2TPATTR（U 面核心 10+ 参数）` |
| `task_summary` | SET APNL2TPATTR 定义 APN 级 L2TP 属性（L2TPSWITCH/SUPPORTIPV6 等 10+ 参数，★U 面核心对象） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 APN 级别使能 L2TP 并定义 U 面 LAC 执行参数 |
| `input_contract` | T-202 APN 实例 |
| `output_contract` | APNL2TPATTR 配置 |
| `command_refs` | SET APNL2TPATTR |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `feature_ref` | GWFD-020412 |
| `targets` | ConfigObject: `APNL2TPATTR`; SemanticObject: `SO-APN-TUNNEL` |
| `note` | TR-APN-06：APNL2TPATTR（U，10+ 参数）≠ APNL2TPCTRL（C，仅 2 参数），C 决策 U 执行模式典型不对称 |

### T-204 L2TP 组与 LNS 容器（本地配置或 AAA 下发）

| 字段 | 值 |
|------|---|
| `task_id` | `T-204` |
| `task_name` | `L2TP 组与 LNS 容器（本地配置或 AAA 下发）` |
| `task_summary` | 二选一：本地配置 ADD L2TPGROUP, ADD L2TPLNSINFO, ADD L2TPCLIENTIP；AAA 下发 ADD L2TPRDSCLIENT |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义 LNS 容器与源端 Giif 绑定，支持本地配置或 Radius 动态下发两种方式 |
| `input_contract` | T-203 APNL2TPATTR、LNS IP/域名规划 |
| `output_contract` | L2TPGROUP/L2TPLNSINFO/L2TPCLIENTIP 或 L2TPRDSCLIENT 实例 |
| `command_refs` | ADD L2TPGROUP, ADD L2TPLNSINFO, ADD L2TPCLIENTIP, ADD L2TPRDSCLIENT |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `feature_ref` | GWFD-020412 |
| `targets` | ConfigObject: `L2TPGROUP`, `L2TPCLIENTIP`, `L2TPRDSCLIENT` |

### T-205 L2TP 缺省属性与 PPP 协商

| 字段 | 值 |
|------|---|
| `task_id` | `T-205` |
| `task_name` | `L2TP 缺省属性与 PPP 协商` |
| `task_summary` | SET GLOBALL2TP 定义缺省属性，SET PPPCFG, SET APNPPPACCESS 定义 PPP 协商与鉴权 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成 L2TP 全局缺省属性与 PPP 链路协商参数 |
| `input_contract` | T-204 L2TP 组 |
| `output_contract` | GLOBALL2TP + PPPCFG + APNPPPACCESS 配置 |
| `command_refs` | SET GLOBALL2TP, SET PPPCFG, SET APNPPPACCESS |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `feature_ref` | GWFD-020412 |
| `targets` | ConfigObject: `GLOBALL2TP`, `PPPCFG` |

### T-206 N4 接口 L2TP 加密（SET L2TPN4KEY）

| 字段 | 值 |
|------|---|
| `task_id` | `T-206` |
| `task_name` | `N4 接口 L2TP 加密（SET L2TPN4KEY）` |
| `task_summary` | SET L2TPN4KEY 配置 N4 接口加密密钥（U 侧），与 UNC 侧 SET L2TPKEY 密钥须相同 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成 C-U 协同的 N4 接口 L2TP 加密（可选） |
| `input_contract` | T-205 PPP 协商、加密密钥规划 |
| `output_contract` | L2TPN4KEY 配置 |
| `command_refs` | SET L2TPN4KEY |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `feature_ref` | GWFD-020412 |
| `targets` | ConfigObject: `L2TPN4KEY` |
| `note` | TR-APN-06：U 侧 L2TPN4KEY 与 C 侧 L2TPKEY 密钥必须相同 |

### T-207 L2TP 静态路由（引导流量进 Tunnel）

| 字段 | 值 |
|------|---|
| `task_id` | `T-207` |
| `task_name` | `L2TP 静态路由（引导流量进 Tunnel）` |
| `task_summary` | ADD SRROUTE 引导用户面流量进入 L2TP Tunnel |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 将目标网段流量路由到 L2TP 隧道接口 |
| `input_contract` | T-204 L2TP 组、目标网段规划 |
| `output_contract` | SRROUTE 实例 |
| `command_refs` | ADD SRROUTE |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `feature_ref` | GWFD-020412 |
| `targets` | ConfigObject: `SRROUTE` |

### T-208 L2TP 策略刷新生效

| 字段 | 值 |
|------|---|
| `task_id` | `T-208` |
| `task_name` | `L2TP 策略刷新生效` |
| `task_summary` | SET REFRESHSRV 使 U 侧 L2TP 配置生效（L2TP 配置链终点） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | UDG 侧 L2TP 配置下发 |
| `input_contract` | T-207 静态路由及之前全部 L2TP 配置 |
| `output_contract` | 配置生效 |
| `command_refs` | SET REFRESHSRV |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `feature_ref` | GWFD-020412 |
| `must_be_last` | `true` |

---

## §5 Radius 鉴权族（feature_specific，WSFD-011306 + WSFD-011305 + WSFD-108007 + WSFD-011307）

> 附录 D.6。T-301~307 已在 F02 §6.4 FTOE-APN-023~028 锁定主干顺序；二次鉴权与抄送扩展见 T-308~310。

### T-301 Radius VPN 与 Gi 接口（AAA VPN）

| 字段 | 值 |
|------|---|
| `task_id` | `T-301` |
| `task_name` | `Radius VPN 与 Gi 接口（AAA VPN）` |
| `task_summary` | ADD L3VPNINST, ADD VPNINSTAF, ADD LOGICIP, ADD LOGICINF（鉴权/计费双 Gi 接口），ADD APN 建立 AAA 承载 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 Radius 鉴权/计费的 AAA VPN 与双 Gi 逻辑接口（giif1/0/0 鉴权、giif1/0/1 计费） |
| `input_contract` | AAA VPN 命名、Gi 接口规划 |
| `output_contract` | L3VPNINST + LOGICIP + LOGICINF + APN 实例 |
| `command_refs` | ADD L3VPNINST, ADD VPNINSTAF, ADD VPNINST, ADD LOGICIP, ADD APN |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-25`, `EV-CA-01` |
| `feature_ref` | WSFD-011306, WSFD-011307, WSFD-108007 |
| `targets` | ConfigObject: `LOGICIP`, `LOGICINF`; SemanticObject: `SO-APN-AUTH-AAA` |

### T-302 Radius 服务器组与服务器

| 字段 | 值 |
|------|---|
| `task_id` | `T-302` |
| `task_name` | `Radius 服务器组与服务器` |
| `task_summary` | ADD RDSSVRGRP, ADD RDSSVR 定义 Radius 服务器组与服务器（鉴权/计费、主备） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 Radius 服务器组实例，承接鉴权/计费请求 |
| `input_contract` | T-301 AAA VPN、Radius 服务器 IP/端口规划 |
| `output_contract` | RDSSVRGRP + RDSSVR 实例 |
| `command_refs` | ADD RDSSVRGRP, ADD RDSSVR |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-25`, `EV-FK-28`, `EV-CA-01` |
| `feature_ref` | WSFD-011306, WSFD-011305, WSFD-011307 |
| `targets` | ConfigObject: `RDSSVRGRP`, `RDSSVR`; SemanticObject: `SO-APN-AUTH-AAA` |
| `note` | RDSSVRGRP 是 Radius 三件套（011306/011305/011307）共享配置对象 |

### T-303 APN 级 Radius 绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-303` |
| `task_name` | `APN 级 Radius 绑定` |
| `task_summary` | ADD APNRDSSVRGRP 绑定 APN↔服务器组，ADD APNRDSCLIENTIP 定义鉴权/计费客户端 IP |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 将 APN 与 Radius 服务器组绑定，并定义双 Gi 客户端 IP |
| `input_contract` | T-302 RDSSVRGRP、T-301 Gi 接口 |
| `output_contract` | APNRDSSVRGRP + APNRDSCLIENTIP 实例 |
| `command_refs` | ADD APNRDSSVRGRP, ADD APNRDSCLIENTIP |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-25`, `EV-CA-01` |
| `feature_ref` | WSFD-011306 |
| `targets` | ConfigObject: `APNRDSSVRGRP`, `APNRDSCLIENTIP` |

### T-304 Radius 计费控制与域名

| 字段 | 值 |
|------|---|
| `task_id` | `T-304` |
| `task_name` | `Radius 计费控制与域名` |
| `task_summary` | SET APNRDSACCTCTRL 定义计费控制（SRVTRIGGER/SUPPORTACCTRSP），SET APNRADIUSATTR 域名增加/剥离 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成 Radius 计费触发策略与域名属性处理 |
| `input_contract` | T-303 APN 级 Radius 绑定 |
| `output_contract` | APNRDSACCTCTRL + APNRADIUSATTR 配置 |
| `command_refs` | SET APNRDSACCTCTRL, SET APNRADIUSATTR, SET RDSRSPADDRCHK |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-25`, `EV-CA-01` |
| `feature_ref` | WSFD-011306 |
| `targets` | ConfigObject: `APNRDSACCTCTRL`, `APNRADIUSATTR` |

### T-305 APN 鉴权属性（ACCESSMODE 4 种取值）

| 字段 | 值 |
|------|---|
| `task_id` | `T-305` |
| `task_name` | `APN 鉴权属性（ACCESSMODE 4 种取值）` |
| `task_summary` | SET APNAUTHATTR 定义鉴权方式：TRANS_NON_AUTH 透明接入 / TRANS_AUTH 透明鉴权 / NON_TRANS 非透明接入 / LOC_AUTH 本地鉴权 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 APN 级别声明鉴权方式（ACCESSMODE 决策点决定 Radius 调用分支） |
| `input_contract` | T-304 Radius 计费控制、ACCESSMODE 决策 |
| `output_contract` | APNAUTHATTR 配置 |
| `command_refs` | SET APNAUTHATTR |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-24`, `EV-CA-01` |
| `feature_ref` | WSFD-011305 |
| `targets` | ConfigObject: `APNAUTHATTR`; SemanticObject: `SO-APN-AUTH-AAA` |
| `note` | TR-APN-02：仅 TRANS_AUTH/NON_TRANS 强依赖 Radius 功能；TRANS_NON_AUTH/LOC_AUTH 不调用 Radius |

### T-306 鉴权属性验证

| 字段 | 值 |
|------|---|
| `task_id` | `T-306` |
| `task_name` | `鉴权属性验证` |
| `task_summary` | LST APNAUTHATTR 验证配置正确性 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 运维验证 APN 鉴权属性 |
| `input_contract` | T-305 APNAUTHATTR |
| `output_contract` | 验证通过 |
| `command_refs` | LST APNAUTHATTR |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-24`, `EV-CA-01` |
| `feature_ref` | WSFD-011305 |

### T-307 Radius 策略刷新生效

| 字段 | 值 |
|------|---|
| `task_id` | `T-307` |
| `task_name` | `Radius 策略刷新生效` |
| `task_summary` | SET REFRESHSRV 使 UNC 侧 Radius 配置生效（鉴权级联链终点） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | UNC 侧 Radius 配置下发 |
| `input_contract` | T-306 验证及之前全部 Radius 配置 |
| `output_contract` | 配置生效 |
| `command_refs` | SET REFRESHSRV |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-24`, `EV-FK-25`, `EV-CA-01` |
| `feature_ref` | WSFD-011305, WSFD-011306 |
| `must_be_last` | `true` |

### T-308 终端二次鉴权扩展（WSFD-108007，DN-AAA 场景）

| 字段 | 值 |
|------|---|
| `task_id` | `T-308` |
| `task_name` | `终端二次鉴权扩展（WSFD-108007，DN-AAA 场景）` |
| `task_summary` | SET LICENSESWITCH(LKV2SECAA01), ADD NETWORKINSTVPNMAP, ADD CPGTPUADDR, ADD UPLIST4RDS, ADD RDSUPFCTRL, ADD UPFRDSSVR, ADD UPFRDSCLIENTIP（必须最后） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 使能 DN-AAA 经 UPF N4 GTP-U 隧道转接的终端二次鉴权（企业 DN 场景） |
| `input_contract` | T-302 RDSSVRGRP（主流程前置）、UPF VPN 规划 |
| `output_contract` | UPF 侧 Radius 控制链（UPFRDSSVR → UPFRDSCLIENTIP） |
| `command_refs` | SET LICENSESWITCH, ADD NETWORKINSTVPNMAP, ADD CPGTPUADDR, ADD UPLIST4RDS, ADD RDSUPFCTRL, ADD UPFRDSSVR, ADD UPFRDSCLIENTIP |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-27`, `EV-CA-01` |
| `feature_ref` | WSFD-108007 |
| `targets` | ConfigObject: `CPGTPUADDR`, `RDSUPFCTRL`, `UPFRDSSVR`, `UPFRDSCLIENTIP`, `NETWORKINSTVPNMAP`; SemanticObject: `SO-APN-AUTH-AAA` |
| `note` | TR-APN-07：UPFRDSSVR 必须先于 UPFRDSCLIENTIP；UPFRDSCLIENTIP 执行后 SMF 立即触发建链；直连 AAA 与经 UPF 中转 AAA 的 Radius Server IP 不可相同 |

### T-309 Radius 抄送扩展（WSFD-011307，并行扩展）

| 字段 | 值 |
|------|---|
| `task_id` | `T-309` |
| `task_name` | `Radius 抄送扩展（WSFD-011307，并行扩展）` |
| `task_summary` | 复用 RDSSVRGRP，ADD APNRDSSVRGRP(PRIFLAG=CARBON_COPY) 定义抄送服务器组 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 将鉴权/计费消息并行抄送给第三方（共享配置对象） |
| `input_contract` | T-302 RDSSVRGRP（复用）、抄送目标服务器 |
| `output_contract` | 抄送服务器组绑定 |
| `command_refs` | ADD APNRDSSVRGRP |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-28`, `EV-CA-01` |
| `feature_ref` | WSFD-011307 |
| `targets` | ConfigObject: `APNRDSSVRGRP`; SemanticObject: `SO-APN-AUTH-AAA` |
| `note` | parallel_extends 关系：与 WSFD-011305/011306 共享 RDSSVRGRP 配置对象，PRIFLAG=CARBON_COPY 区分 |

### T-310 底层 AKA 鉴权配置（WSFD-010301）

| 字段 | 值 |
|------|---|
| `task_id` | `T-310` |
| `task_name` | `底层 AKA 鉴权配置（WSFD-010301）` |
| `task_summary` | ADD GBAUTHCIPH, ADD IUAUTHCIPH, ADD S1USRSECPARA, ADD NGUSRSECPARA 定义 2G/3G/4G/5G AKA 鉴权加密参数 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 SGSN/MME/AMF 侧底层 AKA 鉴权（三元组/五元组向量） |
| `input_contract` | 鉴权向量规划 |
| `output_contract` | GBAUTHCIPH/IUAUTHCIPH/S1USRSECPARA/NGUSRSECPARA 实例 |
| `command_refs` | ADD GBAUTHCIPH, ADD IUAUTHCIPH, ADD S1USRSECPARA, ADD NGUSRSECPARA, MOD AMDATA |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-26`, `EV-CA-01` |
| `feature_ref` | WSFD-010301 |
| `targets` | ConfigObject: `GBAUTHCIPH`, `IUAUTHCIPH`, `S1USRSECPARA`, `NGUSRSECPARA`; SemanticObject: `SO-APN-AUTH-AAA` |
| `note` | 与 WSFD-106003 子特性 B 卡类型控制强依赖（FR-卡类型依赖鉴权） |

---

## §6 UPF 选择族（feature_specific，WSFD-107010 三轮筛选 6 步）

> 附录 D.7。T-401~406 已在 F02 §6.5 FTOE-APN-029~033 锁定顺序。

### T-401 UPF 选择双 License 使能

| 字段 | 值 |
|------|---|
| `task_id` | `T-401` |
| `task_name` | `UPF 选择双 License 使能` |
| `task_summary` | SET LICENSESWITCH 串联使能 LKV2USBL01 + LKV2GWUS01（双 License） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 满足 UPF 选择特性双 License 前置 |
| `input_contract` | UPF 选择业务需求 |
| `output_contract` | 双 License 使能 |
| `command_refs` | SET LICENSESWITCH |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-34`, `EV-CA-01` |
| `feature_ref` | WSFD-107010 |
| `targets` | License: `LKV2USBL01`, `LKV2GWUS01` |

### T-402 第一轮必选 7 条件（PNFPROFILE 系列）

| 字段 | 值 |
|------|---|
| `task_id` | `T-402` |
| `task_name` | `第一轮必选 7 条件（PNFPROFILE 系列）` |
| `task_summary` | ADD PNFPROFILE + PNFDNN/PNFNS/PNFDNAI/PNFUPFINFO/UPNODE/UPAREA/UPBINDS11+GNGP 定义 UPF 全部必选属性 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成 UPF 第一轮筛选的 7 个必选条件（全满足无优先级） |
| `input_contract` | T-401 License、UPF NF 实例规划 |
| `output_contract` | PNFPROFILE + 7 属性实例集 |
| `command_refs` | ADD PNFPROFILE, ADD PNFDNN, ADD PNFNS, ADD PNFDNAI, ADD PNFUPFINFO, ADD UPNODE, ADD UPAREA, ADD PNFSMFSERAREA |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-34`, `EV-CA-01` |
| `feature_ref` | WSFD-107010 |
| `targets` | ConfigObject: `PNFPROFILE`, `PNFDNN`, `UPNODE`, `UPAREA`; SemanticObject: `SO-APN-PNFPROFILE` |
| `note` | TR-APN-08：4G 接入 PNFNSINDEX 保持默认 0（不用切片）；SMF 和 UPF 必须同厂商 |

### T-403 接口绑定（4G 互操作）

| 字段 | 值 |
|------|---|
| `task_id` | `T-403` |
| `task_name` | `接口绑定（4G 互操作）` |
| `task_summary` | ADD UPBINDS11（SGW-U 与 S11），ADD UPBINDGNGP（GGSN/PGW-U 与 Gn/Gp） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成 UPF 与 4G 互操作接口绑定 |
| `input_contract` | T-402 PNFPROFILE、4G 互操作需求 |
| `output_contract` | UPBINDS11 + UPBINDGNGP 实例 |
| `command_refs` | ADD UPBINDS11, ADD UPBINDGNGP |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-34`, `EV-CA-01` |
| `feature_ref` | WSFD-107010 |
| `targets` | ConfigObject: `UPBINDS11`, `UPBINDGNGP` |

### T-404 第二轮优选策略

| 字段 | 值 |
|------|---|
| `task_id` | `T-404` |
| `task_name` | `第二轮优选策略` |
| `task_summary` | SET UPSELECTPRI, SET UPSELECTFLAG, SET APNUPSELPLY 定义第二轮优选策略次序与开关 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义 UPF 第二轮优选的策略次序（COMBINED/LOCS11PRIORITY 等） |
| `input_contract` | T-403 接口绑定、优选策略规划 |
| `output_contract` | UPSELECTPRI + UPSELECTFLAG + APNUPSELPLY 配置 |
| `command_refs` | SET UPSELECTPRI, SET UPSELECTFLAG, SET APNUPSELPLY |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-34`, `EV-CA-01` |
| `feature_ref` | WSFD-107010 |
| `targets` | ConfigObject: `UPSELECTPRI`, `UPSELECTFLAG`, `APNUPSELPLY` |

### T-405 第三轮权重负载均衡

| 字段 | 值 |
|------|---|
| `task_id` | `T-405` |
| `task_name` | `第三轮权重负载均衡` |
| `task_summary` | SET UPLOADBALANCE 使能 UNC 处理 UPF 上报负载信息进行最终选择 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 启用第三轮基于权重与负载的最终 UPF 选择 |
| `input_contract` | T-404 优选策略 |
| `output_contract` | UPLOADBALANCE 配置 |
| `command_refs` | SET UPLOADBALANCE |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-34`, `EV-CA-01` |
| `feature_ref` | WSFD-107010 |
| `targets` | ConfigObject: `UPLOADBALANCE` |

### T-406 UPF 选择策略刷新生效

| 字段 | 值 |
|------|---|
| `task_id` | `T-406` |
| `task_name` | `UPF 选择策略刷新生效` |
| `task_summary` | SET REFRESHSRV 使 UNC 侧 UPF 选择配置生效 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | UNC 侧 UPF 选择配置下发 |
| `input_contract` | T-405 负载均衡及之前全部 UPF 选择配置 |
| `output_contract` | 配置生效 |
| `command_refs` | SET REFRESHSRV |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-34`, `EV-CA-01` |
| `feature_ref` | WSFD-107010 |
| `must_be_last` | `true` |

---

## §7 接入控制族（feature_specific，GWFD-010151 U 侧 + WSFD-106003 C 侧）

> 附录 D.8。U 侧带宽流控与 C 侧接入权限非对称（同名不同义，FR-APN-03）。C 侧 T-501~504 已在 F02 §6.6 FTOE-APN-034~036 锁定顺序。

### T-501 接入控制 License 与鉴权前置（WSFD-106003 子特性 B）

| 字段 | 值 |
|------|---|
| `task_id` | `T-501` |
| `task_name` | `接入控制 License 与鉴权前置（WSFD-106003 子特性 B）` |
| `task_summary` | SET LICENSESWITCH(LKV2ARD02) 使能 ARD License + 前置启用 WSFD-010301 AKA 鉴权（卡类型控制依赖） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 满足 ARD 接入控制的 License 与底层鉴权前置（卡类型区分 SIM/USIM） |
| `input_contract` | ARD 接入控制需求、WSFD-010301 鉴权就绪 |
| `output_contract` | ARD License 使能 + 鉴权前置完成 |
| `command_refs` | SET LICENSESWITCH |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-36`, `EV-FK-26`, `EV-CA-01` |
| `feature_ref` | WSFD-106003, WSFD-010301 |
| `targets` | License: `LKV2ARD02` |
| `note` | TR-APN-09：卡类型控制必须先启用 WSFD-010301；子特性 A（5GC NGMMSUBDATA）无 License |

### T-502 ARD 接入限制（GBARD/IUARD/S1ARD 按代际）

| 字段 | 值 |
|------|---|
| `task_id` | `T-502` |
| `task_name` | `ARD 接入限制（GBARD/IUARD/S1ARD 按代际）` |
| `task_summary` | ADD GBARD(2G), ADD IUARD(3G), ADD S1ARD(4G) 定义签约 ARD/APN/卡类型接入权限 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 SGSN/MME 侧按代际定义接入限制（ARD/CTRLTYPE=ALLOW|REJECT/CAUSE） |
| `input_contract` | T-501 License + 鉴权前置 |
| `output_contract` | GBARD + IUARD + S1ARD 实例 |
| `command_refs` | ADD GBARD, ADD IUARD, ADD S1ARD |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-36`, `EV-CA-01` |
| `feature_ref` | WSFD-106003 |
| `targets` | ConfigObject: `GBARD`, `IUARD`, `S1ARD`; SemanticObject: `SO-APN-ARD-RECORD` |
| `note` | C 侧本地配置优先于签约；紧急注册跳过 |

### T-503 5GC 移动性限制（NGMMSUBDATA，子特性 A）

| 字段 | 值 |
|------|---|
| `task_id` | `T-503` |
| `task_name` | `5GC 移动性限制（NGMMSUBDATA，子特性 A）` |
| `task_summary` | ADD NGMMSUBDATA, SET NGMMPROCTRL 定义 AMF 侧移动性限制（RATRESTRICT/CORERESTRICT） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 AMF 侧定义 5GC 接入限制（无 License，与子特性 B 独立） |
| `input_contract` | 5GC 移动性限制规划 |
| `output_contract` | NGMMSUBDATA + NGMMPROCTRL 配置 |
| `command_refs` | ADD NGMMSUBDATA, SET NGMMPROCTRL |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-36`, `EV-CA-01` |
| `feature_ref` | WSFD-106003 |
| `targets` | ConfigObject: `NGMMSUBDATA`, `NGMMPROCTRL`; SemanticObject: `SO-APN-ARD-RECORD` |

### T-504 接入控制策略刷新生效

| 字段 | 值 |
|------|---|
| `task_id` | `T-504` |
| `task_name` | `接入控制策略刷新生效` |
| `task_summary` | SET REFRESHSRV 使 UNC 侧接入控制配置生效 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | UNC 侧 ARD/NGMMSUBDATA 配置下发 |
| `input_contract` | T-502 ARD + T-503 NGMMSUBDATA |
| `output_contract` | 配置生效 |
| `command_refs` | SET REFRESHSRV |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-36`, `EV-CA-01` |
| `feature_ref` | WSFD-106003 |
| `must_be_last` | `true` |

### T-511 APN QoS 带宽流控配置（GWFD-010151 U 侧）

| 字段 | 值 |
|------|---|
| `task_id` | `T-511` |
| `task_name` | `APN QoS 带宽流控配置（GWFD-010151 U 侧）` |
| `task_summary` | ADD APN, SET APNQOSATTR 定义上下行 CAR/Shaping 开关与方式（CARSHAPESWUL/DL，CARSHAPEUL/DL） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 U 面按 APN 粒度配置带宽流控（CAR 直接丢弃 / SHAPE 缓存整形，上下行独立） |
| `input_contract` | APN 实例、上下行带宽流控目标 |
| `output_contract` | APNQOSATTR 配置 |
| `command_refs` | ADD APN, SET APNQOSATTR, LST APNQOSATTR |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-37`, `EV-CA-01` |
| `feature_ref` | GWFD-010151 |
| `targets` | ConfigObject: `APNQOSATTR`; SemanticObject: `SO-APN-APNQOSATTR` |
| `note` | TR-APN-10：U 侧配置粒度仅 APN（无法针对单用户）；与 C 侧 WSFD-106003 机制完全不同，非 C-U 对称 |

---

## §8 隧道族（feature_specific，IPFD-015002 GRE + IPFD-015004/016000 IPSec）

> 附录 D.4 IPSec + 附录 D.5 GRE。对称同构型（两侧配置对象与命令对称）。

### T-601 GRE 隧道配置（含 GRE over IPSec 场景）

| 字段 | 值 |
|------|---|
| `task_id` | `T-601` |
| `task_name` | `GRE 隧道配置（含 GRE over IPSec 场景）` |
| `task_summary` | LoopBack 接口，ADD GRETUNNEL(TNLTYPE=gre)，Tunnel 接口 IP，ADD SRROUTE，可选 MOD GRETUNNEL（Checksum/Key/Keepalive） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立三层 GRE 隧道，可选叠加 IPSec 加密（弥补 IPSec 不支持组播） |
| `input_contract` | 隧道源/目的 IP、LoopBack 规划 |
| `output_contract` | GRETUNNEL + LoopBack + Tunnel 接口 + SRROUTE 实例 |
| `command_refs` | ADD INTERFACE, ADD IFIPV4ADDRESS, ADD GRETUNNEL, MOD GRETUNNEL, ADD SRROUTE |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-29`, `EV-CA-01` |
| `feature_ref` | IPFD-015002, GWFD-010107 |
| `targets` | ConfigObject: `GRETUNNEL`; SemanticObject: `SO-APN-TUNNEL` |
| `note` | TR-APN-01：GRE 隧道源地址不能与 IPSec 隧道源地址相同（FR-GRE-IPSEC-SRC-EXCL）；无 License |

### T-602 IPSec VNRS 微服务 VPN 与隧道接口

| 字段 | 值 |
|------|---|
| `task_id` | `T-602` |
| `task_name` | `IPSec VNRS 微服务 VPN 与隧道接口` |
| `task_summary` | ADD L3VPNINST, ADD VPNINSTAF, ADD IPBINDVPN, ADD IFIPV4ADDRESS, ADD INTERFACE(Tunnel), ADD IPSECINTFCFG(TNLTYPE=IPSEC) |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 VNRS 微服务侧 VPN 实例与 IPSec 隧道接口 |
| `input_contract` | IPSec VPN 命名、物理接口与 Tunnel 接口规划 |
| `output_contract` | VNRS VPN + IPSec Tunnel 接口 |
| `command_refs` | ADD L3VPNINST, ADD VPNINSTAF, ADD IPBINDVPN, ADD IFIPV4ADDRESS, ADD INTERFACE, ADD IPSECINTFCFGIPSEC, ADD SRROUTE |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-30`, `EV-FK-31`, `EV-CA-01` |
| `feature_ref` | IPFD-015004, IPFD-016000 |
| `targets` | ConfigObject: `IPSECINTFCFG`; SemanticObject: `SO-APN-TUNNEL` |

### T-603 IPSec 微服务镜像配置

| 字段 | 值 |
|------|---|
| `task_id` | `T-603` |
| `task_name` | `IPSec 微服务镜像配置` |
| `task_summary` | ADD L3VPNINSTIPSEC, ADD VPNINSTAFIPSEC, ADD INTERFACEIPSEC, ADD IPBINDVPNIPSEC, ADD IFIPV4ADDRESSIPSEC 建立镜像 VPN |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 IPsec 微服务镜像 VPN 配置（与 VNRS 微服务对称） |
| `input_contract` | T-602 VNRS VPN |
| `output_contract` | IPsec 镜像 VPN 实例集 |
| `command_refs` | ADD L3VPNINSTIPSEC, ADD VPNINSTAFIPSEC, ADD INTERFACEIPSEC, ADD IPBINDVPNIPSEC, ADD IFIPV4ADDRESSIPSEC |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-30`, `EV-FK-31`, `EV-CA-01` |
| `feature_ref` | IPFD-015004, IPFD-016000 |
| `targets` | ConfigObject: `L3VPNINSTIPSEC`, `VPNINSTAFIPSEC` |

### T-604 IPSec ACL 规则（保护数据流）

| 字段 | 值 |
|------|---|
| `task_id` | `T-604` |
| `task_name` | `IPSec ACL 规则（保护数据流）` |
| `task_summary` | ADD ACLGROUPIPSEC, ADD ACLRULEADV4IPSEC 定义保护数据流（仅源/目的 IP，不支持端口） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义 IPSec 保护的数据流范围 |
| `input_contract` | 保护数据流源/目的 IP 规划 |
| `output_contract` | ACLGROUPIPSEC + ACLRULEADV4IPSEC 实例 |
| `command_refs` | ADD ACLGROUPIPSEC, ADD ACLRULEADV4IPSEC |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-30`, `EV-FK-31`, `EV-CA-01` |
| `feature_ref` | IPFD-015004, IPFD-016000 |
| `targets` | ConfigObject: `ACLGROUPIPSEC`, `ACLRULEADV4IPSEC` |

### T-605 IPSec 安全提议（封装+协议+算法）

| 字段 | 值 |
|------|---|
| `task_id` | `T-605` |
| `task_name` | `IPSec 安全提议（封装+协议+算法）` |
| `task_summary` | ADD IPSECPROPOSALIPSEC 定义封装模式（TUNNEL）、安全协议（ESP）、加密/认证算法 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义 IPSec 安全协议参数 |
| `input_contract` | 加密/认证算法选型 |
| `output_contract` | IPSECPROPOSALIPSEC 实例 |
| `command_refs` | ADD IPSECPROPOSALIPSEC |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-30`, `EV-FK-31`, `EV-CA-01` |
| `feature_ref` | IPFD-015004, IPFD-016000 |
| `targets` | ConfigObject: `IPSECPROPOSALIPSEC` |

### T-606 IPSec IKE 提议与对等体

| 字段 | 值 |
|------|---|
| `task_id` | `T-606` |
| `task_name` | `IPSec IKE 提议与对等体` |
| `task_summary` | ADD IKEPROPOSAL(AUTHMETHOD=PSK, DHGROUP), ADD IKEPEER(PRESHAREDKEY, REMOTEADDR, NATTRAVERSAL) |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义 IKE 协商提议与对等体（DH 组不能为 None） |
| `input_contract` | PSK 密钥、对端地址、DH 组选型 |
| `output_contract` | IKEPROPOSAL + IKEPEER 实例 |
| `command_refs` | ADD IKEPROPOSAL, ADD IKEPEER |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-30`, `EV-FK-31`, `EV-CA-01` |
| `feature_ref` | IPFD-015004, IPFD-016000 |
| `targets` | ConfigObject: `IKEPROPOSAL`, `IKEPEER` |
| `note` | TR-APN-11：DH 组不能为 None；NAT 穿越仅 ESP 隧道模式；默认 IKEv2 |

### T-607 IPSec 安全策略与应用

| 字段 | 值 |
|------|---|
| `task_id` | `T-607` |
| `task_name` | `IPSec 安全策略与应用` |
| `task_summary` | ADD IPSECPOLICY, ADD PROPATTACHIPSECPROPOSAL, ADD ATTACHIKEPEER, ADD IPSECINTFCFGIPSEC(应用到 Tunnel) |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 聚合 ACL+Proposal+IKE Peer 为策略并应用到 Tunnel 接口 |
| `input_contract` | T-604 ACL + T-605 Proposal + T-606 IKE Peer |
| `output_contract` | IPSECPOLICY + PROPATTACH + ATTACHIKEPEER + IPSECINTFCFGIPSEC |
| `command_refs` | ADD IPSECPOLICY, ADD PROPATTACHIPSECPROPOSAL, ADD ATTACHIKEPEER, ADD IPSECINTFCFGIPSEC |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-30`, `EV-FK-31`, `EV-CA-01` |
| `feature_ref` | IPFD-015004, IPFD-016000 |
| `targets` | ConfigObject: `IPSECPOLICY`, `IPSECINTFCFGIPSEC` |

### T-608 IPSec IKE 全局配置

| 字段 | 值 |
|------|---|
| `task_id` | `T-608` |
| `task_name` | `IPSec IKE 全局配置` |
| `task_summary` | SET IKEGLOBALCONFIG 定义 DPD（Dead Peer Detection）+ NAT 保活 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 配置 IKE 全局保活机制 |
| `input_contract` | DPD/NAT 保活参数 |
| `output_contract` | IKEGLOBALCONFIG 配置 |
| `command_refs` | SET IKEGLOBALCONFIG |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-30`, `EV-FK-31`, `EV-CA-01` |
| `feature_ref` | IPFD-015004, IPFD-016000 |
| `targets` | ConfigObject: `IKEGLOBALCONFIG` |

---

## §9 别名 APN / DHCP / MPLS / 对等网元选择 / 底座族（feature_specific）

### T-701 别名 APN 映射（双视角语义反转）

| 字段 | 值 |
|------|---|
| `task_id` | `T-701` |
| `task_name` | `别名 APN 映射（双视角语义反转）` |
| `task_summary` | SGSN/MME 侧 ADD ALIASAPN(IMSI_PREFIX+OLDAPN+NEWAPN, LKV2ALIASAPN02) / GGSN/PGW-C/SMF 侧 ADD APNALIAS(SUBRANGE+ALIASAPN+CONVERTAPN+SST/SD, LKV2AAPN01) |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立别名 APN ↔ 真实 APN 双向映射（两侧映射方向相反） |
| `input_contract` | 双 License 使能、APN 命名规划、IMSI 号段/切片规划 |
| `output_contract` | ALIASAPN（SGSN/MME 侧）或 APNALIAS（GGSN/PGW-C/SMF 侧）+ APNREPORTATTR |
| `command_refs` | SET LICENSESWITCH, ADD ALIASAPN, ADD APNALIAS, ADD APN, SET APNREPORTATTR |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-05`, `EV-CA-01` |
| `feature_ref` | WSFD-106203 |
| `targets` | ConfigObject: `ALIASAPN`, `APNALIAS`, `APNREPORTATTR`; SemanticObject: `SO-APN-ALIAS-APN-MAP` |
| `note` | TR-APN-12：双 License（LKV2ALIASAPN02 + LKV2AAPN01）分离；用户携带错误 APN 时先 APN 纠错（WSFD-106004）再别名转换 |

### T-702 DHCP / DHCPv6 地址分配（UNC 侧）

| 字段 | 值 |
|------|---|
| `task_id` | `T-702` |
| `task_name` | `DHCP / DHCPv6 地址分配（UNC 侧）` |
| `task_summary` | ADD ADDRPOOL, ADD ADDRPOOLGRP, ADD DHCPBINDPOOLGRP, ADD DHCPSERVER, ADD DHCPSERVERGRP, ADD AGENTIP, SET DHCPPARAREQ |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 UNC 侧 DHCP/DHCPv6 地址分配机制（与 ADD SECTION, ADD ADDRPOOL 体系协同） |
| `input_contract` | DHCP 服务器规划、地址段 |
| `output_contract` | DHCPBINDPOOLGRP + DHCPSERVER + AGENTIP 实例 |
| `command_refs` | ADD ADDRPOOL, ADD SECTION, ADD ADDRPOOLGRP, ADD DHCPBINDPOOLGRP, ADD DHCPSERVER, ADD AGENTIP, SET DHCPPARAREQ |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-22`, `EV-FK-23`, `EV-CA-01` |
| `feature_ref` | WSFD-104413, WSFD-104005 |
| `targets` | ConfigObject: `DHCPSERVER`, `DHCPBINDPOOLGRP`, `AGENTIP`; SemanticObject: `SO-APN-ADDRESS-POOL` |

### T-703 MPLS VPN 配置（对称同构，文档缺口补全）

| 字段 | 值 |
|------|---|
| `task_id` | `T-703` |
| `task_name` | `MPLS VPN 配置（对称同构，文档缺口补全）` |
| `task_summary` | ADD VPNINSTANCE(VRF) + RD + VPN Target + MP-BGP（文档缺口：9 篇无 MML 脚本，基于 MPLS L3VPN 标准推导） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 MPLS L3VPN 实例与 MP-BGP 路由发布 |
| `input_contract` | MPLS VPN RD/RT 规划 |
| `output_contract` | VPNINSTANCE + RD + VPN Target + MP-BGP 实例 |
| `command_refs` | ADD VPNINSTANCE, ADD BGPVPNV4ROUTETARGET, ADD BGPVPNV4PEER |
| `status` | `draft` |
| `source_evidence_ids` | `EV-FK-32`, `EV-FK-33`, `EV-CA-01` |
| `feature_ref` | GWFD-020411, WSFD-104411 |
| `targets` | ConfigObject: `VPNINSTANCE`, `BGPVPNV4ROUTETARGET`; SemanticObject: `SO-APN-TUNNEL` |
| `note` | TR-APN-13：★文档缺口（9 篇特性文档无 MML 脚本）→ ConfigTask `status=draft`（显式标注，区别于其他 active Task）；命令基于 MPLS L3VPN 标准实践**推导**（ADD VPNINSTANCE, ADD BGPVPNV4ROUTETARGET, ADD BGPVPNV4PEER），需命令字典补全验证；implicit_depends_on IGP/MPLS/BGP 基础；参见 04-command-graph.md §1.11（CMD-UDG-062/063/064 推导命令 status=active 但 command_summary 标"★推导"）；CR-APN-18 |

### T-704 位置区域 DNS 与对等网元选择（WSFD-010202）

| 字段 | 值 |
|------|---|
| `task_id` | `T-704` |
| `task_name` | `位置区域 DNS 与对等网元选择（WSFD-010202）` |
| `task_summary` | ADD AREADNS(LAC/RAC/TAC, ZONESW)，ADD DNSN, ADD IPV4DNSH, ADD SGSNDNS，SET MSCSELPLCY(SRVCC 基于 RAI/LAI FQDN) |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 SGSN/MME 侧将 LAI/RAI/TAI 聚合到单一 DNS 域名（非 SMF） |
| `input_contract` | 位置区规划、DNS 域名规划 |
| `output_contract` | AREADNS + DNS 系列 + MSCSELPLCY 配置 |
| `command_refs` | ADD AREADNS, ADD DNSN, SET MSCSELPLCY |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-35`, `EV-CA-01` |
| `feature_ref` | WSFD-010202 |
| `targets` | ConfigObject: `AREADNS`, `DNSN`, `MSCSELPLCY`; SemanticObject: `SO-APN-AREDNS` |
| `note` | 适用 NF 为 SGSN/MME（非 SMF）；Pre-5G 代际互补 |

### T-705 会话管理底座与并发限制（纯描述性 + WSFD-010503）

| 字段 | 值 |
|------|---|
| `task_id` | `T-705` |
| `task_name` | `会话管理底座与并发限制（纯描述性 + WSFD-010503）` |
| `task_summary` | WSFD-010503 ADD APNACTNUM(PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM/PDNCONNREJCAUSE)，底座运维 DSP POOLUSAGE, DSP SESSIONINFO，2/3G PDPAPN 维护 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义单 APN 并发限制 + 会话管理底座运维查询（无独立配置命令） |
| `input_contract` | APN 并发上限规划 |
| `output_contract` | APNACTNUM 实例 + 运维查询能力 |
| `command_refs` | ADD APNACTNUM, ADD PDPAPN, DSP POOLUSAGE, DSP SESSIONINFO |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-01`, `EV-FK-02`, `EV-FK-03`, `EV-CA-01` |
| `feature_ref` | GWFD-010101, WSFD-010501, WSFD-010503 |
| `targets` | ConfigObject: `APNACTNUM`, `PDPAPN`; SemanticObject: `SO-APN-SESSION-CONTEXT`, `SO-APN-APNACTNUM` |
| `note` | 纯描述性根底座（GWFD-010101/WSFD-010501）无独立 MML/License/配置对象；PDU/PDN/PDP 会话由 PFCP/GTP-C 被动触发 |

### T-706 L2TP-VPN C 侧决策（WSFD-104410）

| 字段 | 值 |
|------|---|
| `task_id` | `T-706` |
| `task_name` | `L2TP-VPN C 侧决策（WSFD-104410）` |
| `task_summary` | SET APNL2TPCTRL(仅 2 参数 APN/L2TPSWITCH)，SET L2TPKEY(N4 加密)，SET PFCPPVTEXT(私有扩展下发 LNS 参数) |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 UNC 侧决策 L2TP LNS 参数并经 N4 下发（C 决策 U 执行模式 C 侧） |
| `input_contract` | LNS 参数决策、N4 加密密钥（与 U 侧 L2TPN4KEY 相同） |
| `output_contract` | APNL2TPCTRL + L2TPKEY + PFCPPVTEXT 配置 |
| `command_refs` | SET APNL2TPCTRL, SET L2TPKEY, SET PFCPPVTEXT |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-14`, `EV-CA-01` |
| `feature_ref` | WSFD-104410 |
| `targets` | ConfigObject: `APNL2TPCTRL`, `L2TPKEY`; SemanticObject: `SO-APN-TUNNEL` |
| `note` | TR-APN-06：APNL2TPCTRL（C，2 参数）决策侧 vs APNL2TPATTR（U，10+ 参数）执行侧；无 License |

### T-707 UNC 侧控制面地址分配（WSFD-010502 + WSFD-010504 + WSFD-107021）

| 字段 | 值 |
|------|---|
| `task_id` | `T-707` |
| `task_name` | `UNC 侧控制面地址分配（WSFD-010502 + WSFD-010504 + WSFD-107021）` |
| `task_summary` | ADD SECTION, ADD ADDRPOOL, ADD ADDRPOOLGRP, ADD POOLBINDGRP, ADD POOLGRPMAP, ADD UPFBINDGRP, ADD UPNODE(ADDRALLOCMODE=INHERIT), SET STATICADDRPARA, SET IPALLOCRULE, SET APNIPALLOCRULE |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 UNC 侧控制面地址分配体系（命令前缀与 UDG 不对称：ADDRPOOL vs POOL） |
| `input_contract` | UPF 节点规划、地址段 |
| `output_contract` | ADDRPOOL, ADDRPOOLGRP, POOLBINDGRP, UPFBINDGRP, UPNODE 实例 |
| `command_refs` | ADD SECTION, ADD ADDRPOOL, ADD ADDRPOOLGRP, ADD POOLBINDGRP, ADD POOLBINDAPN, ADD POOLGRPMAP, ADD UPFBINDGRP, ADD UPNODE, ADD PNFPROFILE, SET STATICADDRPARA, SET IPALLOCRULE, ADD BLACKLIST |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-12`, `EV-FK-13`, `EV-FK-15`, `EV-CA-01` |
| `feature_ref` | WSFD-010502, WSFD-010504, WSFD-107021 |
| `targets` | ConfigObject: `ADDRPOOL`, `ADDRPOOLGRP`, `POOLBINDGRP`, `UPFBINDGRP`, `UPNODE`, `STATICADDRPARA`; SemanticObject: `SO-APN-ADDRESS-POOL` |
| `note` | TR-APN-03：UNC 侧命令前缀 ADDRPOOL/POOLBINDGRP（GRP 非 GROUP）与 UDG 不对称；UPNODE 是网元选择+地址分配共用对象 |

### T-708 静态路由冗余配置（GWFD-010107 + WSFD-107021 对称同构）

| 字段 | 值 |
|------|---|
| `task_id` | `T-708` |
| `task_name` | `静态路由冗余配置（GWFD-010107 + WSFD-107021 对称同构）` |
| `task_summary` | U 侧 ADD POOL(REDUNDFUNC), ADD REDUNDRDTIP, SET REDUNDUSER, ADD GRETUNNEL, SET APNREDUNDUPSW, ADD OSPFINTERFACE；C 侧 SET REDUNDUSER 对称 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立主备 UDG 间静态路由冗余（虚拟 IP 重定向业务流到 GRE Tunnel） |
| `input_contract` | 主备 UDG 规划、虚拟 IP |
| `output_contract` | REDUNDRDTIP + REDUNDUSER + GRETUNNEL + OSPFINTERFACE 配置 |
| `command_refs` | ADD POOL, ADD REDUNDRDTIP, SET REDUNDUSER, ADD GRETUNNEL, SET APNREDUNDUPSW, ADD OSPFINTERFACE, MOD OSPFIMPORTROUTE |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-10`, `EV-FK-15`, `EV-CA-01` |
| `feature_ref` | GWFD-010107, WSFD-107021 |
| `targets` | ConfigObject: `REDUNDRDTIP`, `REDUNDUSER`, `APNREDUNDUPSW` |
| `note` | SET REDUNDUSER 与 ADD POOL REDUNDFUNC 双使能；仅备用 UDG 启用 APNREDUNDUPSW |

---

## §10 TaskRule（任务级规则，13 条）

| `rule_id` | `rule_name` | `rule_type` | `applies_to` | `rule_logic` | `severity` |
|-----------|-------------|-------------|--------------|--------------|------------|
| `TR-APN-01` | GRE/IPSec 源地址互斥 | `validation_rule` | T-601, T-602 | GRE 隧道源地址不能与 IPSec 隧道源地址相同（FR-GRE-IPSEC-SRC-EXCL），GRE over IPSec 场景必须分离源地址 | critical |
| `TR-APN-02` | Radius ACCESSMODE 调用分支 | `selection_rule` | T-305 | 仅 ACCESSMODE=TRANS_AUTH/NON_TRANS 强依赖 Radius 功能；TRANS_NON_AUTH/LOC_AUTH 不调用 Radius；ACCESSMODE 决策点决定是否前置 T-301~304 | critical |
| `TR-APN-03` | UDG/UNC 地址池前缀不对称 | `naming_rule` | T-003, T-707 | UDG 侧 POOL/POOLGROUP/POOLBINDGROUP vs UNC 侧 ADDRPOOL/ADDRPOOLGRP/POOLBINDGRP（GRP 非 GROUP）；POOLTYPE 取值差异：UDG=LOCAL，UNC=UDM（仅静态签约）；不可混用 | critical |
| `TR-APN-04` | 双栈 V6PREFIXLENGTH 分水岭 | `validation_rule` | T-104 | V6PREFIXLENGTH=64 为普通 IPv6 单栈地址分配；<64 切换为 IPv6 Prefix Delegation 模式（GWFD-020406）；双栈 IPv4/IPv6 双池并存须双优先级算法使能 | warning |
| `TR-APN-05` | L2TP C-U License 不对称 | `restriction_rule` | T-201, T-706 | U 侧 LAC 执行必须 License 82200BVC LKV3G5L2TP01；C 侧决策（WSFD-104410）无 License；C-U 协同经 N4 接口（L2TPN4KEY/L2TPKEY 密钥须相同） | critical |
| `TR-APN-06` | APNL2TPATTR vs APNL2TPCTRL 不对称 | `validation_rule` | T-203, T-706 | U 侧 APNL2TPATTR（10+ 参数，LAC 执行）≠ C 侧 APNL2TPCTRL（2 参数，决策）；C 决策 U 执行模式典型不对称；与 GWFD-010108/020482 互斥 | critical |
| `TR-APN-07` | 二次鉴权 UPF Radius 链时序 | `dependency_rule` | T-308 | UPF 侧 VPN 前置（ADD NETWORKINSTVPNMAP）→ ADD UPFRDSSVR（必须先于 CLIENTIP）→ ADD UPFRDSCLIENTIP（必须最后，执行后 SMF 立即触发建链）；直连 AAA 与经 UPF 中转 AAA 的 Radius Server IP 不可相同 | critical |
| `TR-APN-08` | UPF 选择三轮筛选约束 | `selection_rule` | T-402, T-403, T-404, T-405 | 第一轮 7 必选条件全满足无优先级；4G 接入 PNFNSINDEX=0（不用切片）；SMF 和 UPF 必须同厂商；静态 IP 段绑定 UPF 与 SMF 主锚点 UPF 选择冲突时 SMF 优先 | critical |
| `TR-APN-09` | ARD 卡类型控制鉴权前置 | `dependency_rule` | T-501, T-502, T-310 | WSFD-106003 子特性 B 卡类型控制必须先启用 WSFD-010301 AKA 鉴权（通过三元组/五元组区分 SIM/USIM）；C 侧本地配置优先于签约；紧急注册跳过 | critical |
| `TR-APN-10` | 接入控制非 C-U 对称 | `restriction_rule` | T-511, T-502, T-503 | GWFD-010151（U 面带宽流控，APNQOSATTR，仅 APN 粒度）与 WSFD-106003（C 面接入权限，ARD/NGMMSUBDATA，可到单用户）机制完全不同，非同一控制目标的 C-U 分工；不建 c_u_symmetric 边 | critical |
| `TR-APN-11` | IPSec IKE DH 组与 NAT 约束 | `validation_rule` | T-606, T-608 | DH 组不能为 None；NAT 穿越仅 ESP 隧道模式；默认 IKEv2（IKEv1 需 MOD IKEPEER VERSION1=FALSE 关闭）；ACL 仅支持源/目的 IP 不支持端口 | critical |
| `TR-APN-12` | 别名 APN 双 License 与双视角 | `restriction_rule` | T-701 | SGSN/MME 侧（LKV2ALIASAPN02，协商 APN→别名 APN，DNS 屏蔽，ADD ALIASAPN）与 GGSN/PGW-C/SMF 侧（LKV2AAPN01，别名 APN→真实 APN，资源归一，ADD APNALIAS）License 分离、映射方向相反；转换后 APN 必须已 ADD APN | critical |
| `TR-APN-13` | MPLS VPN 文档缺口标记 | `validation_rule` | T-703 | 9 篇 MPLS 特性文档无完整 MML 脚本，ConfigTask status=draft；命令基于 MPLS L3VPN 标准推导（VPNINSTANCE/BGPVPNV4ROUTETARGET/BGPVPNV4PEER），需命令字典补全；implicit_depends_on IGP/MPLS/BGP 基础 | warning |

> **规则溯源**：
> - TR-APN-01 ← 互斥关系 §4.4 FR-GRE-IPSEC-SRC-EXCL（IPFD-015002 §1.10）
> - TR-APN-02 ← 附录 D.6 关键约束（Radius ACCESSMODE 调用分支）
> - TR-APN-03 ← 配置差异 §3.1（UDG/UNC 命令前缀不对称）
> - TR-APN-04 ← 发现二（IPv6 承载 License 串联链）+ 附录 D.2 关键约束
> - TR-APN-05 ← C-U 配对 §1.3 第 7 对（L2TP C 决策 U 执行）+ §3.2
> - TR-APN-06 ← 配置差异 §3.2（APNL2TPATTR vs APNL2TPCTRL 不对称）
> - TR-APN-07 ← 附录 D.6 扩展 1（二次鉴权 S2~S6 时序）
> - TR-APN-08 ← 附录 D.7 关键约束（三轮筛选 + 同厂商 + SMF 优先）
> - TR-APN-09 ← 附录 D.8 关键约束（卡类型控制鉴权前置）
> - TR-APN-10 ← 发现四（接入控制非 C-U 对称）+ 附录 D.8
> - TR-APN-11 ← 附录 D.4 关键约束（DH 组 + NAT + IKEv2）
> - TR-APN-12 ← 发现六（别名 APN 双视角语义反转）+ 附录 D.9
> - TR-APN-13 ← 配置差异 §3.3（MPLS 文档缺口）

---

## §11 TaskCommandOrderEdge（Task 内部命令顺序）

> 来源：`feature-knowledge/cross-feature-analysis.md` 附录 D 9 端到端配置流程（73 步）。
> Task 间顺序见 F02 §6 FeatureTaskOrderEdge（FTOE-APN-001~036，已定义）。
> 本节仅承载 **Task 内部** 命令时序（附录 D 单步骤内的命令依赖）与 **跨 Task 同流程** 关键 propagated_context。

### 11.1 T-003 UDG 地址池四件套链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-APN-003-1` | T-003 | `ADD POOL` | `ADD SECTION` | `precedes` | `required` | `POOLNAME → SECTION.POOLNAME` | `EV-FK-06, EV-CA-01` |
| `TE-APN-003-2` | T-003 | `ADD SECTION` | `ADD POOLGROUP` | `precedes` | `required` | `POOLGRPNAME` | `EV-FK-06, EV-CA-01` |
| `TE-APN-003-3` | T-003 | `ADD POOLGROUP` | `ADD POOLBINDGROUP` | `precedes` | `required` | `POOLGRPNAME + POOLNAME → POOLBINDGROUP` | `EV-FK-06, EV-CA-01` |

### 11.2 T-005 OSPF/OSPFv3 路由发布链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-APN-005-1` | T-005 | `ADD OSPF` | `ADD OSPFAREA` | `precedes` | `required` | `PROCID` | `EV-FK-06, EV-CA-01` |
| `TE-APN-005-2` | T-005 | `ADD OSPFAREA` | `ADD OSPFNETWORK` | `precedes` | `required` | `PROCID + AREAID` | `EV-FK-06, EV-CA-01` |
| `TE-APN-005-3` | T-005 | `ADD OSPFNETWORK` | `ADD OSPFIMPORTROUTE` | `precedes` | `required` | `PROCID; PROTOCOL=wlr` | `EV-FK-06, EV-CA-01` |
| `TE-APN-005-4` | T-005 | `ADD OSPFV3` | `ADD OSPFV3IMPORTROUTE` | `precedes` | `optional` | `PROCID; PROTOCOL=wlr（IPv6 侧，020401 提供）` | `EV-FK-18, EV-CA-01` |

### 11.3 T-204 L2TP 组与源端绑定链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-APN-204-1` | T-204 | `ADD L2TPGROUP` | `ADD L2TPLNSINFO` | `precedes` | `required` | `L2TPGROUPID + DOMAINNAME` | `EV-FK-11, EV-CA-01` |
| `TE-APN-204-2` | T-204 | `ADD L2TPLNSINFO` | `ADD L2TPCLIENTIP` | `precedes` | `required` | `L2TPGROUPID → INTFNAME` | `EV-FK-11, EV-CA-01` |

### 11.4 T-302 Radius 服务器组与服务器链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-APN-302-1` | T-302 | `ADD RDSSVRGRP` | `ADD RDSSVR` | `precedes` | `required` | `RDSSVRGRPNAME → RDSSVR` | `EV-FK-25, EV-CA-01` |

### 11.5 T-308 二次鉴权 UPF Radius 链（严格时序）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-APN-308-1` | T-308 | `ADD NETWORKINSTVPNMAP` | `ADD CPGTPUADDR` | `precedes` | `required` | `VPNINSTANCE（UPF 侧前置）` | `EV-FK-27, EV-CA-01` |
| `TE-APN-308-2` | T-308 | `ADD CPGTPUADDR` | `ADD UPLIST4RDS` | `precedes` | `required` | `IPV4ADDR; UPLISTNAME` | `EV-FK-27, EV-CA-01` |
| `TE-APN-308-3` | T-308 | `ADD UPLIST4RDS` | `ADD RDSUPFCTRL` | `precedes` | `required` | `UPLISTNAME + UPINSTANCEID` | `EV-FK-27, EV-CA-01` |
| `TE-APN-308-4` | T-308 | `ADD RDSUPFCTRL` | `ADD UPFRDSSVR` | `precedes` | `required` | `UPLISTNAME; SERVERTYPE=AUTHENTICATION` | `EV-FK-27, EV-CA-01` |
| `TE-APN-308-5` | T-308 | `ADD UPFRDSSVR` | `ADD UPFRDSCLIENTIP` | `must_be_last` | `required` | `UPLISTNAME; CLIENTIPV4（执行后 SMF 立即触发建链）` | `EV-FK-27, EV-CA-01` |

### 11.6 T-402 UPF 第一轮 7 必选条件链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-APN-402-1` | T-402 | `ADD PNFPROFILE` | `ADD PNFDNN` | `precedes` | `required` | `NFINSTANCENAME` | `EV-FK-34, EV-CA-01` |
| `TE-APN-402-2` | T-402 | `ADD PNFDNN` | `ADD PNFNS` | `precedes` | `required` | `NFINSTANCENAME; PNFNSINDEX=0（4G）` | `EV-FK-34, EV-CA-01` |
| `TE-APN-402-3` | T-402 | `ADD PNFNS` | `ADD PNFDNAI` | `precedes` | `optional` | `NFINSTANCENAME` | `EV-FK-34, EV-CA-01` |
| `TE-APN-402-4` | T-402 | `ADD PNFDNAI` | `ADD PNFUPFINFO` | `precedes` | `optional` | `NFINSTANCENAME; EPSFUPPORTED` | `EV-FK-34, EV-CA-01` |
| `TE-APN-402-5` | T-402 | `ADD PNFUPFINFO` | `ADD UPNODE` | `precedes` | `required` | `NFINSTANCENAME; 位置特征+分流能力` | `EV-FK-34, EV-CA-01` |
| `TE-APN-402-6` | T-402 | `ADD UPNODE` | `ADD UPAREA` | `precedes` | `required` | `NFINSTANCENAME; 位置区绑定` | `EV-FK-34, EV-CA-01` |

### 11.7 T-607 IPSec 策略聚合链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-APN-607-1` | T-607 | `ADD IPSECPOLICY` | `ADD PROPATTACHIPSECPROPOSAL` | `precedes` | `required` | `POLICYNAME + SEQ; PROPOSALNAME` | `EV-FK-30, EV-CA-01` |
| `TE-APN-607-2` | T-607 | `ADD PROPATTACHIPSECPROPOSAL` | `ADD ATTACHIKEPEER` | `precedes` | `required` | `POLICYNAME + SEQ; PEERNAME + PRIORITY` | `EV-FK-30, EV-CA-01` |
| `TE-APN-607-3` | T-607 | `ADD ATTACHIKEPEER` | `ADD IPSECINTFCFGIPSEC` | `must_be_last` | `required` | `POLICYNAME → IFNAME=Tunnel1` | `EV-FK-30, EV-CA-01` |

### 11.8 跨 Task 同流程关键 propagated_context（附录 D 端到端链）

> 此类边表达同一端到端流程中跨 Task 的命令上下文传播（如 POOLGRPMAP.POOLGROUPNAME 由 T-003 传播到 T-004）。Task 间顺序已由 FTOE 承载，本节仅记录关键上下文。

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-APN-X1` | T-003→T-004 | `ADD POOLBINDGROUP` | `ADD POOLGRPMAP` | `depends_on` | `required` | `POOLGROUPNAME → POOLGRPMAP` | `EV-FK-06, EV-CA-01` |
| `TE-APN-X2` | T-002→T-004 | `ADD APN` | `ADD POOLGRPMAP` | `depends_on` | `required` | `APN → POOLGRPMAP.MAPPINGNAME` | `EV-FK-06, EV-CA-01` |
| `TE-APN-X3` | T-101→T-104 | `SET LICENSESWITCH` | `ADD POOL`（IPv6） | `depends_on` | `required` | `LICITEM=LKV3G5V6PB01+LKV3G5VDSA01（License 串联链）` | `EV-FK-16, EV-CA-01` |
| `TE-APN-X4` | T-302→T-303 | `ADD RDSSVRGRP` | `ADD APNRDSSVRGRP` | `depends_on` | `required` | `RDSSVRGRPNAME → APNRDSSVRGRP` | `EV-FK-25, EV-CA-01` |
| `TE-APN-X5` | T-302→T-309 | `ADD RDSSVRGRP` | `ADD APNRDSSVRGRP`（抄送） | `depends_on` | `required` | `RDSSVRGRPNAME（共享）; PRIFLAG=CARBON_COPY` | `EV-FK-28, EV-CA-01` |
| `TE-APN-X6` | T-402→T-707 | `ADD UPNODE` | `ADD UPFBINDGRP` | `depends_on` | `required` | `NFINSTANCENAME; ADDRALLOCMODE=INHERIT（共用对象）` | `EV-FK-12, EV-FK-34, EV-CA-01` |

---

## §12 关系边汇总（§10.6 任务原子层关系）

| 关系类型 | 数量 | 说明 |
|---------|------|------|
| `constrained_by`（ConfigTask → TaskRule） | 61 → 13 | TR-APN-01~13，每个 ConfigTask 至少受 1 条规则约束（见 §10 applies_to） |
| `invokes`（ConfigTask → MMLCommand） | 183 | 每个 ConfigTask 的 command_refs 为纯文本命令名（对齐访问限制格式，graph_parser 通过 command_name 匹配 04 的 MMLCommand；60 Task 有命令引用；T-109 空设计；5 REFRESHSRV 边 T-006/208→CMD-UDG-088、T-307/406/504→CMD-UNC-087，见 §1 各 Task 表 + 05 §4.1） |
| `orchestrates`（ConfigTask → TaskCommandOrderEdge） | 30 | §11（TE-APN-003~607 共 24 条 Task 内部边 + 6 条跨 Task 上下文边，未含 FTOE） |
| `targets`（ConfigTask → SemanticObject / ConfigObject） | 61 | 每个 ConfigTask 操作目标（见各 Task 表 targets 字段） |
| `may_require_feature`（ConfigTask → Feature） | 58 | feature_specific Task 标注 feature_ref（generic Task 无） |
| `supported_by`（ConfigTask → EvidenceSource） | 61 | 每个 ConfigTask 由 EV-FK-xx + EV-CA-01 支撑 |

---

## §13 与带宽/计费场景任务层的对比

| 维度 | 计费场景 | 带宽控制场景 | APN 业务域 |
|------|---------|------------|-----------|
| 通用 Task 数 | 8（T-001~T-008） | 8（T-001~T-008） | 3（T-001/006/007） |
| 特性专属 Task 数 | 19 | 24 | 58 |
| **Task 合计** | 27 | 32 | **61** |
| TaskRule 数 | 6 | 6 | 13 |
| TaskCommandOrderEdge | 16 | 16 | 30（24 内部 + 6 跨 Task） |
| **任务层对象总计** | ~49 | ~54 | **104** |
| 独有 Task 族 | 计费三件套、在线计费、融合计费、CG 接口 | BWM 三级、FUP 三件套、QoS/GBR、ADC、UNC 控制面、无线优化 | 地址分配 4 步、双栈 9 步、L2TP U 面 8 步、Radius 级联 10 步、UPF 选择 6 步、接入控制 5 步、IPSec/GRE 8 步、别名/DHCP/MPLS/对等网元/底座/L2TP-C/UNC地址分配/静态冗余 11 步 |
| 核心差异 | URR 用于差异化计费 | URR 用于流量阈值监控 + BWM 限速整形 | 会话管理底座纯描述性 + 地址分配 6×3 正交矩阵 + 4 隧道 C-U 模式二分 + License 串联链 |
| generic 共享点 | T-001~008（SA/PCC 体系） | T-001~008（SA/PCC 体系） | T-001/006/007（VPN/REFRESHSRV/LICENSE，无 SA/PCC 依赖） |

> APN 业务域任务层对象最多（104），因其覆盖 37 个特性（最多）、6 大 feature_group、4 隧道 C-U 模式二分、纯描述性底座等独有维度。TaskRule 数（13）显著高于另两场景（均 6），反映了 APN 域的配置树修正项密集（双栈使能层、C 决策 U 执行、非 C-U 对称、双视角反转、MPLS 文档缺口等）。

---

## §14 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| ConfigTask（generic） | 3 | T-001, T-006, T-007 |
| ConfigTask（地址分配族） | 4 | T-002~005 |
| ConfigTask（双栈族） | 9 | T-101~109 |
| ConfigTask（L2TP-VPN U 族） | 8 | T-201~208 |
| ConfigTask（Radius 鉴权族） | 10 | T-301~310 |
| ConfigTask（UPF 选择族） | 6 | T-401~406 |
| ConfigTask（接入控制族） | 5 | T-501~504, T-511 |
| ConfigTask（隧道族 GRE+IPSec） | 8 | T-601~608 |
| ConfigTask（别名/DHCP/MPLS/对等网元/底座/L2TP-C/UNC地址分配/静态冗余） | 8 | T-701~708 |
| **ConfigTask 合计** | **61** | T-001~708（generic 3 + feature_specific 58） |
| TaskRule | 13 | TR-APN-01~13 |
| TaskCommandOrderEdge（Task 内部） | 24 | TE-APN-003(3) + 005(4) + 204(2) + 302(1) + 308(5) + 402(6) + 607(3) |
| TaskCommandOrderEdge（跨 Task 上下文） | 6 | TE-APN-X1~X6 |
| **TaskCommandOrderEdge 合计** | **30** | 24 内部 + 6 跨 Task |
| **任务层对象总计** | **104** | 61 ConfigTask + 13 TaskRule + 30 TaskCommandOrderEdge |

---

> 本文件为 APN 业务域三层图谱第 3 层。第 1 层业务图谱见 `01-business-graph.md`，第 2 层特性图谱见 `02-feature-graph.md`，第 4 层命令图谱、第 5 层跨层映射、第 6 层证据索引见同目录其他文件。
