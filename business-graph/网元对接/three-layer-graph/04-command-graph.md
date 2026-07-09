# UPF网元对接三层图谱 · 第4层：命令图谱

> **文件定位**：`three-layer-graph/04-command-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱
> **作用**：实例化 103 个 MMLCommand + 34 个 ConfigObject + 14 个 CommandRule + ConfigObject间关系边
> **数据来源**：`UDG初始配置与调测` 原始目录、`03-task-layer.md`

---

## 0. 命令图谱总览

### 0.1 MMLCommand 按功能分布

| 功能域 | 命令数 | 说明 |
|-------|-------|------|
| 基础与网管 | 22 | License、NTP、网元信息、授权、公共参数、MTU、纳管 |
| 控制面与用户面接口 | 9 | N4、业务接口、Nupf、切片、服务化入口 |
| 会话接入 | 8 | APN、地址池、绑定和分配规则 |
| 路由协议 | 18 | VPN、OSPF/OSPFv3、BGP、静态路由 |
| BFD/隧道/自动部署/验收 | 46 | BFD、GRE/MPLS、自动部署、级联口、核查命令 |
| **合计** | **103条语法项** | 主图谱登记命令 103 个 |

### 0.2 ConfigObject 按功能分布

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| 基础与运维 | 11 | LicenseItem, NTPSource, NetworkElement, SecurityAuth, ManagedNE |
| 控制面与接口 | 8 | VPNInstance, LogicInterface, UPFIdentity, SNSSAIBinding, HttpLe |
| 会话接入 | 7 | APN, AddressPool, AddressSection, PoolGroup, IPAllocRule |
| 路由协议 | 5 | L3VPNInstance, VPNTarget, OSPFDomain, BGPDomain, StaticRoute |
| 增强与自动化 | 3 | BFDSession, TunnelOverlay, AutoDeployTemplate |
| **合计** | **34** | — |

---

## 1. MMLCommand 实例化

### 1.1 基础与网管（22个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-ND-001` | `DSP RVKLICINFO` | 查询 License 激活状态 | UDG | License项 | EV-TK-01 |
| `CMD-ND-002` | `SET NTP` | 配置 NTP 时间同步 | UDG | 时间源地址 | EV-TK-02 |
| `CMD-ND-003` | `MOD ME` | 修改网元名称 | UDG | 网元名 | EV-TK-02 |
| `CMD-ND-004` | `SET OMIP` | 修改 OM IP | UDG | OM IP | EV-TK-02 |
| `CMD-ND-005` | `LST ME` | 查询网元信息 | UDG | — | EV-TK-02 |
| `CMD-ND-006` | `SET SECAUTH` | 开启二次授权总开关 | UDG | 开关值 | EV-TK-02 |
| `CMD-ND-007` | `ADD USRSECAUTH` | 增加授权用户 | UDG | 用户名 | EV-TK-02 |
| `CMD-ND-008` | `ADD SECAUTHMEM` | 增加授权命令成员 | UDG | 命令成员 | EV-TK-02 |
| `CMD-ND-009` | `SET NEWCERTSWITCH` | 证书相关开关 | UDG | 开关值 | EV-TK-02 |
| `CMD-ND-010` | `SET SIGDSCP` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-011` | `SET UDPCHECKSUM` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-012` | `SET SRVCOMMONPARA` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-013` | `SET QOSCAR` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-014` | `SET IPV6FRAGPLCY` | IPv6 分片策略 | UDG | 策略值 | EV-TK-02 |
| `CMD-ND-015` | `SET CPTEIDUALLOC` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-016` | `SET TZ` | 时区参数 | UDG | 时区值 | EV-TK-02 |
| `CMD-ND-017` | `SET ANTIFRAUD` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-018` | `SET FWDPARA` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-019` | `SET HEADENGLBPARA` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-020` | `SET MSFAULTALARM` | 公共参数配置 | UDG | 参数值 | EV-TK-02 |
| `CMD-ND-021` | `SET FABRICMTU` | 设置 Fabric MTU | UDG | MTU值 | EV-TK-02 |
| `CMD-ND-022` | `MOD INTERFACE` | 修改接口参数和 MTU | UDG | 接口、MTU | EV-TK-02, EV-TK-05 |

### 1.2 控制面与用户面接口（9个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-ND-023` | `SET IFIPV6ENABLE` | 打开接口 IPv6 能力 | UDG | 开关值 | EV-TK-02, EV-TK-06 |
| `CMD-ND-024` | `ADD VPNINST` | 增加信令或业务 VPN 实例 | UDG | VPN名 | EV-TK-03 |
| `CMD-ND-025` | `ADD LOGICINF` | 增加逻辑接口 | UDG | 接口名/地址 | EV-TK-03 |
| `CMD-ND-026` | `SET UPINFO` | 设置 UPF 标识 | UDG | HOSTNAME等 | EV-TK-03 |
| `CMD-ND-027` | `ADD SNSSAIUPINTF` | 切片与接口绑定 | UDG | SNSSAI、接口 | EV-TK-03 |
| `CMD-ND-028` | `ADD LOGICIP` | 增加逻辑 IP | UDG | 逻辑IP | EV-TK-03 |
| `CMD-ND-029` | `ADD HTTPLEGRP` | Nupf 接口对象组 | UDG | 对象组名 | EV-TK-03 |
| `CMD-ND-030` | `ADD HTTPLE` | Nupf 接口对象 | UDG | 对象参数 | EV-TK-03 |
| `CMD-ND-031` | `ADD SBIAPLE` | SBI 入口对象 | UDG | 入口参数 | EV-TK-03 |

### 1.3 会话接入（8个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-ND-032` | `SET HTTPCONF` | 服务化接口配置 | UDG | 接口参数 | EV-TK-03 |
| `CMD-ND-033` | `ADD APN` | 增加 APN/DNN | UDG | APN名 | EV-TK-03 |
| `CMD-ND-034` | `SET APNSGLPASS` | APN 单通检测 | UDG | 检测参数 | EV-TK-03 |
| `CMD-ND-035` | `ADD POOL` | 增加地址池 | UDG | 地址池名 | EV-TK-03 |
| `CMD-ND-036` | `ADD SECTION` | 增加地址段 | UDG | 起止地址 | EV-TK-03 |
| `CMD-ND-037` | `ADD POOLGROUP` | 增加地址池组 | UDG | 池组名 | EV-TK-03 |
| `CMD-ND-038` | `ADD POOLBINDGROUP` | 绑定地址池组 | UDG | 绑定关系 | EV-TK-03 |
| `CMD-ND-039` | `ADD POOLGRPMAP` | APN 与地址池组映射 | UDG | 映射关系 | EV-TK-03 |

### 1.4 路由协议（18个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-ND-040` | `SET IPALLOCRULE` | IP 分配规则 | UDG | 模式参数 | EV-TK-03 |
| `CMD-ND-041` | `ADD L3VPNINST` | 增加路由侧 L3VPN 实例 | UDG | VPN名 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-042` | `ADD VPNINSTAF` | 增加 VPN 地址族 | UDG | 地址族 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-043` | `MOD VPNINSTAF` | 修改 VPN 地址族 | UDG | 地址族参数 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-044` | `ADD VPNTARGET` | 增加 RT 路由目标 | UDG | RT值 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-045` | `ADD IPBINDVPN` | 接口绑定 VPN | UDG | 接口、VPN | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-046` | `ADD OSPF` | 增加 OSPF 进程 | UDG | 进程号 | EV-TK-04, EV-TK-05 |
| `CMD-ND-047` | `ADD OSPFAREA` | 增加 OSPF 区域 | UDG | 区域号 | EV-TK-04, EV-TK-05 |
| `CMD-ND-048` | `ADD OSPFNETWORK` | OSPF 网段使能 | UDG | 网段 | EV-TK-04, EV-TK-05 |
| `CMD-ND-049` | `ADD OSPFINTERFACE` | OSPF 接口使能 | UDG | 接口 | EV-TK-04, EV-TK-05 |
| `CMD-ND-050` | `ADD OSPFIMPORTROUTE` | OSPF 引入路由 | UDG | 引入类型 | EV-TK-04, EV-TK-05 |
| `CMD-ND-051` | `ADD OSPFV3` | 增加 OSPFv3 进程 | UDG | 进程号 | EV-TK-04, EV-TK-05 |
| `CMD-ND-052` | `ADD OSPFV3AREA` | 增加 OSPFv3 区域 | UDG | 区域号 | EV-TK-04, EV-TK-05 |
| `CMD-ND-053` | `ADD OSPFV3INTERFACE` | OSPFv3 接口使能 | UDG | 接口 | EV-TK-04, EV-TK-05 |
| `CMD-ND-054` | `ADD OSPFV3IMPORTROUTE` | OSPFv3 引入路由 | UDG | 引入类型 | EV-TK-04, EV-TK-05 |
| `CMD-ND-055` | `SET BGP` | 启用 BGP | UDG | BGP参数 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-056` | `ADD BGPVRF` | 增加 BGP VRF | UDG | VRF名 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-057` | `ADD BGPVRFAF` | 增加 BGP 地址族 | UDG | 地址族 | EV-TK-04, EV-TK-05, EV-TK-06 |

### 1.5 BFD/隧道/自动部署/验收（46个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-ND-058` | `ADD BGPPEER` | 增加 BGP 对等体 | UDG | Peer地址 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-059` | `ADD BGPPEERAF` | 增加 BGP 对等体地址族 | UDG | 地址族 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-060` | `ADD IMPORTROUTE` | 引入路由 | UDG | 引入策略 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-061` | `ADD NETWORKROUTE` | 增加 Network Route | UDG | 网段 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-062` | `ADD SRROUTE` | 增加 IPv4 静态路由 | UDG | 目的/下一跳 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-063` | `ADD SRROUTE6` | 增加 IPv6 静态路由 | UDG | 目的/下一跳 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-064` | `SET BFD` | 启用 BFD | UDG | BFD参数 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-065` | `ADD BFDSESSION` | 增加 BFD 会话 | UDG | 会话参数 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-066` | `ADD GRETUNNEL` | 增加 GRE 隧道 | UDG | 隧道参数 | EV-TK-04, EV-TK-05 |
| `CMD-ND-067` | `MOD GRETUNNEL` | 修改 GRE 隧道 | UDG | 隧道参数 | EV-TK-04, EV-TK-05 |
| `CMD-ND-068` | `SET MPLSSITE` | 启用 MPLS 全局 | UDG | 全局参数 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-069` | `ADD MPLSIF` | 增加 MPLS 接口 | UDG | 接口参数 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-070` | `SET DHCP6CLIENTDUID` | DHCPv6相关参数 | UDG | DUID参数 | EV-TK-04, EV-TK-06 |
| `CMD-ND-071` | `SET AUTOCONFIG` | 自动部署开关 | UDG | 开关值 | EV-TK-04 |
| `CMD-ND-072` | `LST AUTOCONFIG` | 查询自动部署状态 | UDG | — | EV-TK-04 |
| `CMD-ND-073` | `DSP OPSASSISTSTATE` | 查询自动部署助手状态 | UDG | — | EV-TK-04 |
| `CMD-ND-074` | `ADD AUTOSCALINGETHTRUNK` | 增加自动部署 Eth-Trunk 模板 | UDG | 模板参数 | EV-TK-04, EV-TK-05 |
| `CMD-ND-075` | `ADD AUTOSCALINGSERVICE` | 增加自动部署服务模板 | UDG | 模板参数 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-076` | `ADD AUTOSCALINGBFD` | 增加自动部署 BFD 模板 | UDG | 模板参数 | EV-TK-04, EV-TK-06 |
| `CMD-ND-077` | `ADD NPDIRECTCONNECTPORT` | 增加 NP 级联口 | UDG | 端口参数 | EV-TK-05, EV-TK-06 |
| `CMD-ND-078` | `DSP SESSIONINFO` | 查看会话信息 | UDG | 会话条件 | EV-TK-07 |
| `CMD-ND-079` | `MOD AUTOSCALINGSERVICE` | 修改自动部署服务模板 | UDG | 模板参数 | EV-TK-04, EV-TK-05, EV-TK-06 |
| `CMD-ND-080` | `ADD AUTOSCALINGSRBFD` | 增加静态路由 BFD 模板 | UDG | 模板参数 | EV-TK-04 |
| `CMD-ND-081` | `ADD AUTOSCALINGSRROUTE` | 增加静态路由模板 | UDG | 模板参数 | EV-TK-04, EV-TK-06 |
| `CMD-ND-082` | `ADD AUTOSCALINGBGPLF` | 增加 BGP 入不转板模板 | UDG | 模板参数 | EV-TK-04 |
| `CMD-ND-083` | `ADD AUTOSCALINGIPREACH` | 增加 RU 可达性模板 | UDG | 模板参数 | EV-TK-04 |
| `CMD-ND-084` | `ADD AUTOSCALINGMPLS` | 增加 MPLS 自动化模板 | UDG | 模板参数 | EV-TK-04, EV-TK-06 |
| `CMD-ND-085` | `LST LOGICINF` | 查询逻辑接口 | UDG | 接口条件 | EV-TK-07 |
| `CMD-ND-086` | `LST VPNINST` | 查询 VPN 实例 | UDG | VPN条件 | EV-TK-07 |
| `CMD-ND-087` | `LST APN` | 查询 APN/DNN | UDG | APN条件 | EV-TK-07 |
| `CMD-ND-088` | `LST OSPF` | 查询 OSPF 进程 | UDG | 进程条件 | EV-TK-07 |
| `CMD-ND-089` | `LST BGPPEER` | 查询 BGP 对等体 | UDG | Peer条件 | EV-TK-07 |
| `CMD-ND-090` | `DSP BGPPEERINFO` | 查询 BGP 对等体状态 | UDG | Peer条件 | EV-TK-07 |
| `CMD-ND-091` | `DSP ROUTE` | 查询 IPv4 路由 | UDG | 路由条件 | EV-TK-07 |
| `CMD-ND-092` | `DSP ROUTE6` | 查询 IPv6 路由 | UDG | 路由条件 | EV-TK-07 |
| `CMD-ND-093` | `DSP SRROUTE` | 查询静态路由 | UDG | 路由条件 | EV-TK-07 |
| `CMD-ND-094` | `DSP OSPFROUTING` | 查询 OSPF 路由信息 | UDG | 路由条件 | EV-TK-07 |
| `CMD-ND-095` | `DSP OSPFPEER` | 查询 OSPF 邻居 | UDG | 邻居条件 | EV-TK-07 |
| `CMD-ND-096` | `DSP BFDSESSION` | 查询 BFD 会话 | UDG | 会话条件 | EV-TK-07 |
| `CMD-ND-097` | `DSP IFSTATUS` | 查询接口状态 | UDG | 接口条件 | EV-TK-07 |
| `CMD-ND-098` | `DSP SERVICERUSTATE` | 查询业务运行状态 | UDG | 服务条件 | EV-TK-07 |
| `CMD-ND-099` | `NGPING` | 网元间连通性探测 | UDG | 目的地址 | EV-TK-07 |
| `CMD-ND-100` | `PING` | 基础 IP 连通性探测 | UDG | 目的地址 | EV-TK-07 |
| `CMD-ND-101` | `SRVPING` | 业务路径探测 | UDG | 业务地址 | EV-TK-07 |
| `CMD-ND-102` | `SRVTRACERT` | 业务路径跟踪 | UDG | 业务地址 | EV-TK-07 |
| `CMD-ND-103` | `EXP MML` | 导出 MML 或执行诊断导出 | UDG | 导出条件 | EV-TK-07 |

---

## 2. ConfigObject 实例化（34个）

| `object_id` | `object_name` | 所属功能 | 关键属性 | 包含关系 |
|-------------|---------------|----------|----------|----------|
| `OBJ-ND-01` | `LicenseItem` | 基础与运维 | License项 | — |
| `OBJ-ND-02` | `NTPSource` | 基础与运维 | 时间源地址 | — |
| `OBJ-ND-03` | `NetworkElement` | 基础与运维 | 网元名 | — |
| `OBJ-ND-04` | `OMIP` | 基础与运维 | OM地址 | belongs_to NetworkElement |
| `OBJ-ND-05` | `SecurityAuth` | 基础与运维 | 授权用户/命令成员 | contains 授权成员 |
| `OBJ-ND-06` | `GlobalParameter` | 基础与运维 | 参数名/值 | — |
| `OBJ-ND-07` | `MTUConfig` | 基础与运维 | Fabric/接口MTU | — |
| `OBJ-ND-08` | `NorthboundUser` | 基础与运维 | 北向账号 | — |
| `OBJ-ND-09` | `SNMPUser` | 基础与运维 | SNMPv3用户 | — |
| `OBJ-ND-10` | `NetworkMgmtAdapter` | 基础与运维 | 适配层参数 | — |
| `OBJ-ND-11` | `ManagedNE` | 基础与运维 | 被管网元实例 | contains 账号/适配层 |
| `OBJ-ND-12` | `VPNInstance` | 控制面与接口 | VPN名 | — |
| `OBJ-ND-13` | `LogicInterface` | 控制面与接口 | 接口名/地址 | belongs_to VPNInstance |
| `OBJ-ND-14` | `UPFIdentity` | 控制面与接口 | HOSTNAME/标识 | — |
| `OBJ-ND-15` | `SNSSAIBinding` | 控制面与接口 | 切片绑定参数 | links 切片到接口 |
| `OBJ-ND-16` | `LogicIP` | 控制面与接口 | 逻辑IP | belongs_to LogicInterface |
| `OBJ-ND-17` | `HttpLeGroup` | 控制面与接口 | 组名 | contains HttpLe |
| `OBJ-ND-18` | `HttpLe` | 控制面与接口 | 接口参数 | belongs_to HttpLeGroup |
| `OBJ-ND-19` | `SbiApLe` | 控制面与接口 | SBI入口 | — |
| `OBJ-ND-20` | `APN` | 会话接入 | APN/DNN | — |
| `OBJ-ND-21` | `AddressPool` | 会话接入 | 地址池名 | contains AddressSection |
| `OBJ-ND-22` | `AddressSection` | 会话接入 | 地址段 | belongs_to AddressPool |
| `OBJ-ND-23` | `PoolGroup` | 会话接入 | 池组名 | contains AddressPool |
| `OBJ-ND-24` | `PoolBindGroup` | 会话接入 | 绑定组 | links PoolGroup |
| `OBJ-ND-25` | `PoolGroupMap` | 会话接入 | 映射关系 | links APN to PoolGroup |
| `OBJ-ND-26` | `IPAllocRule` | 会话接入 | 分配规则 | applies_to APN |
| `OBJ-ND-27` | `L3VPNInstance` | 路由协议 | L3VPN名 | contains VPNTarget |
| `OBJ-ND-28` | `VPNTarget` | 路由协议 | RT值 | belongs_to L3VPNInstance |
| `OBJ-ND-29` | `OSPFDomain` | 路由协议 | 进程/区域/接口 | contains OSPF子对象 |
| `OBJ-ND-30` | `BGPDomain` | 路由协议 | VRF/Peer/AF | contains BGP子对象 |
| `OBJ-ND-31` | `StaticRoute` | 路由协议 | 目的/下一跳 | — |
| `OBJ-ND-32` | `BFDSession` | 增强与自动化 | 会话参数 | — |
| `OBJ-ND-33` | `TunnelOverlay` | 增强与自动化 | GRE/MPLS对象 | contains 隧道子对象 |
| `OBJ-ND-34` | `AutoDeployTemplate` | 增强与自动化 | 自动部署模板 | contains 模板子对象 |

---

## 3. CommandRule（14条）

| `rule_id` | `scope_ref` | `rule_name` | `severity` | `rule_logic` |
|-----------|-------------|-------------|------------|--------------|
| `CR-ND-01` | `CMD-ND-004` | 改 OMIP 触发回流 | `warning` | 修改 OMIP 后必须重新执行纳管闭环 |
| `CR-ND-02` | `CMD-ND-025` | 逻辑接口掩码统一 | `critical` | 逻辑接口掩码采用目录给定的统一模式 |
| `CR-ND-03` | `CMD-ND-033~040` | 会话接入必须闭环 | `critical` | APN、地址池、映射和分配规则缺一不可 |
| `CR-ND-04` | `CMD-ND-058` | BGP依赖前置路由基础 | `critical` | BGP 不能脱离静态或 OSPF 基础单独构建 |
| `CR-ND-05` | `CMD-ND-071~075` | 自动部署有时序 | `critical` | 必须先关、后配、再开、最后核查助手状态 |
| `CR-ND-06` | `CMD-ND-075` | SDN参数强约束 | `critical` | SDN 场景外联参数必须服从 DHCP/静态+BFD 组合 |
| `CR-ND-07` | `CMD-ND-077` | 级联口仅限特定硬件 | `warning` | 级联口只出现在特定硬件分支 |
| `CR-ND-08` | `CMD-ND-006~008` | 高危命令前置授权 | `warning` | 高危命令必须在授权之后执行 |
| `CR-ND-09` | `CMD-ND-009` | 证书开关前置 | `info` | 证书相关能力启用前应先确认开关 |
| `CR-ND-10` | `CMD-ND-021~022` | MTU层级一致 | `warning` | MTU 必须按目录中的层级逻辑设置 |
| `CR-ND-11` | `CMD-ND-024/041` | VPN命名语义一致 | `info` | 信令 VPN、业务 VPN、路由 VPN 必须保持语义一致 |
| `CR-ND-12` | `CMD-ND-064~065` | BFD模式服从分支 | `warning` | 双向或单臂必须与目录分支一致 |
| `CR-ND-13` | `CMD-ND-068~069` | MPLS方式服从部署方式 | `warning` | 自动部署和手工部署不能混用 MPLS 接口路径 |
| `CR-ND-14` | `CMD-ND-078` | FirstCall为最终验收 | `critical` | 没有 SESSIONINFO 验证通过，不算完成场景闭环 |

---

## 4. ConfigObject 关系边

| 起点 | 关系 | 终点 |
|------|------|------|
| `VPNInstance` | `contains` | `LogicInterface` |
| `LogicInterface` | `contains` | `LogicIP` |
| `HttpLeGroup` | `contains` | `HttpLe` |
| `AddressPool` | `contains` | `AddressSection` |
| `PoolGroup` | `contains` | `AddressPool` |
| `PoolGroupMap` | `links` | `APN` / `PoolGroup` |
| `L3VPNInstance` | `contains` | `VPNTarget` |
| `OSPFDomain` | `contains` | `OSPFArea/Interface` |
| `BGPDomain` | `contains` | `BGPVRF/Peer/AF` |
| `TunnelOverlay` | `contains` | `GRE/MPLS对象` |

---

## 5. 合规声明

- 命令层只承接命令、对象和规则
- 业务层与特性层不直接落命令
- 本层服务前端链路 `任务 → 命令`
