# 网元对接三层图谱 · 第4层：命令图谱

> **文件定位**：`three-layer-graph/04-command-graph.md`
> **Schema 参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（字段标准）、§13 禁止关系
> **作用**：实例化 UPF 网元对接（UDG 扮演 UPF/PGW-U/SGW-U）开局对接所需的 MMLCommand + CommandParameter + ConfigObject + CommandRule + ConfigObject 关系边
> **数据来源**：`cross-topic-analysis.md`（EV-CA-02，附录 B MML命令全集 / 附录 C ConfigObject矩阵 / §3共性机制 / §4差异对比 / §5依赖协同）、`topic-knowledge/Batch-01~07`（EV-TK-NN 命令参数细节）
> **命名规范**：`command_name` 为主要标识（如 `ADD VPNINST`），`command_id` = 去空格大写（如 `ADDVPNINST`）

---

## 0. 命令图谱总览

### 0.1 MMLCommand 按6类组织

| 类别 | 命令数 | 关键命令族 | 主要对接面 |
|------|-------|----------|----------|
| 1. 接口配置类 | 7 | ADD VPNINST / ADD LOGICINF / SET UPINFO / ADD SNSSAIUPINTF / ADD LOGICIP / ADD IPBINDVPN | CS-1/CS-2 |
| 2. 会话接入类 | 8 | ADD APN / SET APNSGLPASS / ADD POOL / ADD SECTION / ADD POOLGROUP / ADD POOLBINDGROUP / ADD POOLGRPMAP / SET IPALLOCRULE | CS-2 |
| 3. 网管与基础数据类 | 18 | MOD ME / SET OMIP / SET SECAUTH / SET NTP / SET NEWCERTSWITCH / 公共参数11项 / SET FABRICMTU / MOD INTERFACE / SET IFIPV6ENABLE | CS-5/CS-3 |
| 4. 路由-VPN与协议类 | 22 | ADD L3VPNINST / ADD VPNINSTAF / ADD VPNTARGET / ADD OSPF系列 / ADD OSPFV3系列 / SET BGP / ADD BGPVRF / ADD BGPVRFAF / ADD BGPPEER / ADD BGPPEERAF / ADD IMPORTROUTE / ADD NETWORKROUTE / ADD SRROUTE / ADD SRROUTE6 | CS-4 |
| 5. BFD/隧道/级联口/入不转板类 | 11 | SET BFD / ADD BFDSESSION / ADD GRETUNNEL / SET MPLSSITE / ADD MPLSIF / ADD NPDIRECTCONNECTPORT / SET DATAPLANEGIINFMODE / SET DATAPLANEINFMODE / SET DHCP6CLIENTDUID / IPsec 命令 | CS-4 |
| 6. 自动部署模板族 | 11 | SET/LST AUTOCONFIG / DSP OPSASSISTSTATE / ADD/RMV/MOD/LST AUTOSCALINGSERVICE / AUTOSCALINGETHTRUNK / AUTOSCALINGBFD / AUTOSCALINGSRBFD / AUTOSCALINGSRROUTE / AUTOSCALINGBGPLF / AUTOSCALINGIPREACH / AUTOSCALINGMPLS | CS-4 |
| + 验证查询类 | 26 | LST 系列 / DSP 系列 / SRVPING / SRVTRACERT / NGPING / PING / EXP MML | 全局 |
| **合计** | **103** | — | — |

### 0.2 ConfigObject 按功能域分布

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| 接口与VPN | 8 | VPNInstance, LogicInterface(N4if/Saif/Scif/Paif/S11-uif), ExternalInterface, LoopbackInterface, AbstractInterface, SNSSAIBinding, NupfInterface |
| 会话接入 | 7 | APN, AddressPool, AddressSection, PoolGroup, PoolBinding, PoolGroupMap, IPAllocRule |
| 路由协议 | 12 | L3VPNInstance, VPNAddressFamily, VPNTarget, OSPFProcess, OSPFArea, OSPFInterface, StaticRoute, BGPInstance, BGPAddressFamily, BGPPeer, LoopbackRoute, NetworkRoute |
| BFD/隧道/MPLS/NP | 9 | BFDSession, GRETunnel, MPLSGlobal, MPLSInterface, IPsecSA, NPCascadePort, DataPlaneGiInfMode, DataPlaneInfMode, DHCPv6ClientDUID |
| 自动部署模板 | 9 | AutoScalingService, AutoScalingEthTrunk, AutoScalingBFD, AutoScalingSRBFD, AutoScalingSRRoute, AutoScalingBGPLF, AutoScalingIPReach, AutoScalingMPLS, AutoConfigSwitch |
| 网管与基础 | 9 | NetworkElement, OMIP, NorthboundUser, SNMPUser, NetworkMgmtAdapter, ManagedNE, EMSAssociation, SecurityAuth, GlobalParameter |
| License/MTU/NTP | 4 | License, MTUConfig, NTPSource, UPFIdentity |
| **合计** | **58** | — |

---

## 1. MMLCommand 实例化

> 字段顺序遵循 Schema §11.3：`command_id / command_name / verb / object_keyword / command_summary / source_evidence_ids`。`status` 默认 `active`（除注明外）。

### 1.1 接口配置类（7个，CS-1/CS-2）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `ADDVPNINST` | ADD VPNINST | ADD | VPNINST | 增加业务/信令面 VPN 实例（VPN_Signaling/VPN_Access/VPN_Sc/VPN_Pa/VPN_Internet） | EV-CA-02 §3.1, EV-TK-03 KP-01~06 |
| `ADDLOGICINF` | ADD LOGICINF | ADD | LOGICINF | 增加业务逻辑接口（N4if/Saif/Scif/Paif/N3if/S1-uif/S11-uif），掩码固定 255.255.255.255 | EV-CA-02 §3.1, EV-TK-03 KP-01~06 |
| `ADDLOGICIP` | ADD LOGICIP | ADD | LOGICIP | 配置逻辑接口 IP（Nupf 服务化接口前置） | EV-CA-02 附录B.2, EV-TK-03 KP-08 |
| `ADDIPBINDVPN` | ADD IPBINDVPN | ADD | IPBINDVPN | 接口绑定 VPN（外联口基础设施层，手动部署） | EV-CA-02 §3.2层4, EV-TK-04/05 |
| `SETUPINFO` | SET UPINFO | SET | UPINFO | 设置 UPF 标识（HOSTNAME 全网唯一，不配则 N4 偶联失败） | EV-CA-02 §6.1, EV-TK-03 KP-02 |
| `ADDSNSSAIUPINTF` | ADD SNSSAIUPINTF | ADD | SNSSAIUPINTF | 网络切片与逻辑接口绑定（仅 Saif/N3if） | EV-CA-02 §6.2, EV-TK-03 KP-03 |
| `ADDHTTPLEGRP` / `ADDHTTPLE` / `ADDSBIAPLE` / `SETHTTPCONF` | Nupf 服务化接口族 | ADD/SET | HTTPLEGRP/HTTPLE/SBIAPLE/HTTPCONF | Nupf（接 NWDAF）HTTP/SBI 服务化接口配置（4命令聚合） | EV-CA-02 附录B.2, EV-TK-03 KP-08 |

### 1.2 会话接入类（8个，CS-2）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `ADDAPN` | ADD APN | ADD | APN | 增加 APN/DNN 实例（HASVPN/HASVPNIPV6 绑定 VPN） | EV-CA-02 §3.4, EV-TK-03 KP-09 |
| `SETAPNSGLPASS` | SET APNSGLPASS | SET | APNSGLPASS | APN 单通检测配置 | EV-CA-02 附录B.3, EV-TK-03 KP-09 |
| `ADDPOOL` | ADD POOL | ADD | POOL | 增加地址池（LOCAL/EXTERNAL） | EV-CA-02 §3.4, EV-TK-03 KP-10 |
| `ADDSECTION` | ADD SECTION | ADD | SECTION | 增加地址段（V4STARTIP/V4ENDIP 或 V6PREFIXSTART/END/LENGTH=64） | EV-CA-02 §4.4, EV-TK-03 KP-10 |
| `ADDPOOLGROUP` | ADD POOLGROUP | ADD | POOLGROUP | 增加地址池组 | EV-CA-02 §3.4, EV-TK-03 KP-10 |
| `ADDPOOLBINDGROUP` | ADD POOLBINDGROUP | ADD | POOLBINDGROUP | 地址池绑定到地址池组 | EV-CA-02 §3.4, EV-TK-03 KP-10 |
| `ADDPOOLGRPMAP` | ADD POOLGRPMAP | ADD | POOLGRPMAP | APN↔POOLGROUP 映射 | EV-CA-02 §3.4, EV-TK-03 KP-10 |
| `SETIPALLOCRULE` | SET IPALLOCRULE | SET | IPALLOCRULE | 三级地址分配规则（FIRSTRULESW + FIRSTRULE=APN-1&LOCATION-0&SMF-0） | EV-CA-02 §3.4, EV-TK-03 KP-11 |

### 1.3 网管与基础数据类（18个，CS-5/CS-3）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `MODME` | MOD ME | MOD | ME | 修改网元名称（MEID/MENAME） | EV-CA-02 附录B.1, EV-TK-02 KP-02 |
| `SETOMIP` | SET OMIP | SET | OMIP | 修改浮动IP/物理IP（**高危，二次授权**；改后中断网管+VNFM，触发CS-3回流） | EV-CA-02 §5.6, EV-TK-02 KP-02/03 |
| `LSTME` | LST ME | LST | ME | 查询网元信息（CS-3 验证标志） | EV-CA-02 附录B.1/B.6, EV-TK-02 KP-06 |
| `LSTOMIP` | LST OMIP | LST | OMIP | 查询 OMIP 配置 | EV-CA-02 附录B.1, EV-TK-02 KP-02 |
| `SETSECAUTH` | SET SECAUTH | SET | SECAUTH | 二次授权总开关（STATUS=ON） | EV-CA-02 §3.5, EV-TK-02 KP-03 |
| `ADDUSRSECAUTH` | ADD USRSECAUTH | ADD | USRSECAUTH | 增加二次授权用户 | EV-CA-02 §3.5, EV-TK-02 KP-03 |
| `ADDSECAUTHMEM` | ADD SECAUTHMEM | ADD | SECAUTHMEM | 二次授权命令清单成员（13类高危命令） | EV-CA-02 §3.5, EV-TK-02 KP-03 |
| `SETNTP` | SET NTP | SET | NTP | 配置 NTP 时间同步（双路：OMC + FusionStage） | EV-CA-02 §6.5, EV-TK-02 KP-01 |
| `SETNEWCERTSWITCH` | SET NEWCERTSWITCH | SET | NEWCERTSWITCH | 证书自动更新开关（LiteCA 5前置；4类证书场景不支持自动） | EV-CA-02 附录B.1, EV-TK-02 KP-06 |
| `SETSIGDSCP` | SET SIGDSCP | SET | SIGDSCP | 公共参数1：信令 DSCP | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETUDPCHECKSUM` | SET UDPCHECKSUM | SET | UDPCHECKSUM | 公共参数2：UDP 校验和 | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETSRVCOMMONPARA` | SET SRVCOMMONPARA | SET | SRVCOMMONPARA | 公共参数3：服务公共参数 | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETQOSCAR` | SET QOSCAR | SET | QOSCAR | 公共参数4：QoS CAR | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETIPV6FRAGPLCY` | SET IPV6FRAGPLCY | SET | IPV6FRAGPLCY | 公共参数5：IPv6 分片策略（INNERIPV6FRAGPLCY: TOOBIG_PKTDROP→OUTERFRAG） | EV-CA-02 §5.5, EV-TK-02 KP-04/05 |
| `SETCPTEIDUALLOC` | SET CPTEIDUALLOC | SET | CPTEIDUALLOC | 公共参数6：控制面 TEID 分配 | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETTZ` | SET TZ | SET | TZ | 公共参数7：时区 | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETANTIFRAUD` | SET ANTIFRAUD | SET | ANTIFRAUD | 公共参数8：反欺诈 | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETFWDPARA` | SET FWDPARA | SET | FWDPARA | 公共参数9：转发参数（**高危，二次授权**） | EV-CA-02 §6.5, EV-TK-02 KP-03/04 |
| `SETHEADENGLBPARA` | SET HEADENGLBPARA | SET | HEADENGLBPARA | 公共参数10：头部增强全局参数 | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETMSFAULTALARM` | SET MSFAULTALARM | SET | MSFAULTALARM | 公共参数11：多框故障告警 | EV-CA-02 §6.5, EV-TK-02 KP-04 |
| `SETFABRICMTU` | SET FABRICMTU | SET | FABRICMTU | 配置 Fabric MTU（MTU 三层之上层） | EV-CA-02 §5.5, EV-TK-02 KP-05 |
| `MODINTERFACE` | MOD INTERFACE | MOD | INTERFACE | 修改物理接口属性（MTU；外联口手动部署第1步） | EV-CA-02 §5.5/§4.2, EV-TK-02/05 |
| `SETIFIPV6ENABLE` | SET IFIPV6ENABLE | SET | IFIPV6ENABLE | IPv6 接口使能（SDN: AUTOLINKLOCAL=TRUE 必设） | EV-CA-02 §4.1/§4.4, EV-TK-06 |

> 公共参数共11项（SET SIGDSCP~SET MSFAULTALARM 含 FWDPARA），表内为18+3条目（含MOD ME/LST ME/SET NTP 等基础项）；编号 CMD-ND-018~035 占位。

### 1.4 路由-VPN与协议类（22个，CS-4）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `ADDL3VPNINST` | ADD L3VPNINST | ADD | L3VPNINST | 增加 L3VPN 实例（VPN实例层，路由侧；区别于 ADD VPNINST 业务面） | EV-CA-02 §3.2层1, EV-TK-04 |
| `ADDVPNINSTAF` | ADD VPNINSTAF | ADD | VPNINSTAF | VPN 实例地址族（ipv4uni/ipv6uni；双栈两个都要配） | EV-CA-02 §3.2层1/§4.4, EV-TK-04 |
| `MODVPNINSTAF` | MOD VPNINSTAF | MOD | VPNINSTAF | 修改 VPN 地址族（VRFRD/VRFLABELMODE=perInstance） | EV-CA-02 §5.9, EV-TK-04 KP-10 |
| `ADDVPNTARGET` | ADD VPNTARGET | ADD | VPNTARGET | VPN Target（RT，导入/导出路由标记） | EV-CA-02 附录B.4, EV-TK-04 |
| `ADDOSPF` | ADD OSPF | ADD | OSPF | OSPF IPv4 进程（SCHEMAROUID） | EV-CA-02 §4.4, EV-TK-04 KP-02 |
| `ADDOSPFAREA` | ADD OSPFAREA | ADD | OSPFAREA | OSPF 区域（NSSA 区域需配 Loopback 自动选 FA） | EV-CA-02 §4.4/§9.3, EV-TK-04 KP-02 |
| `ADDOSPFNETWORK` | ADD OSPFNETWORK | ADD | OSPFNETWORK | OSPF 网段使能 | EV-CA-02 附录B.4, EV-TK-04 KP-02 |
| `ADDOSPFINTERFACE` | ADD OSPFINTERFACE | ADD | OSPFINTERFACE | OSPF 接口使能 | EV-CA-02 附录B.4, EV-TK-04 KP-02 |
| `ADDOSPFIMPORTROUTE` | ADD OSPFIMPORTROUTE | ADD | OSPFIMPORTROUTE | OSPF 引入路由（IMPORTPROTOCOL=wlr 用户下行路由） | EV-CA-02 §5.8/§9.2, EV-TK-04 KP-02 |
| `ADDOSPFV3` | ADD OSPFV3 | ADD | OSPFV3 | OSPF IPv6 进程（ROUTERID, DETECTMULINTV） | EV-CA-02 §4.4, EV-TK-04 KP-05 |
| `ADDOSPFV3AREA` | ADD OSPFV3AREA | ADD | OSPFV3AREA | OSPFv3 区域 | EV-CA-02 附录B.4, EV-TK-04 KP-05 |
| `ADDOSPFV3INTERFACE` | ADD OSPFV3INTERFACE | ADD | OSPFV3INTERFACE | OSPFv3 接口使能 | EV-CA-02 附录B.4, EV-TK-04 KP-05 |
| `ADDOSPFV3IMPORTROUTE` | ADD OSPFV3IMPORTROUTE | ADD | OSPFV3IMPORTROUTE | OSPFv3 引入路由 | EV-CA-02 附录B.4, EV-TK-04 KP-05 |
| `SETBGP` | SET BGP | SET | BGP | BGP 全局使能 | EV-CA-02 §3.2层2, EV-TK-04 KP-04 |
| `ADDBGPVRF` | ADD BGPVRF | ADD | BGPVRF | BGP VPN 实例（含 ROUTERID；MPLS: VRFNAME="_public_"） | EV-CA-02 §5.9/§4.4, EV-TK-04 KP-04/10 |
| `ADDBGPVRFAF` | ADD BGPVRFAF | ADD | BGPVRFAF | BGP 地址族（AFTYPE=ipv4/ipv6；MPLS MP-EBGP: ipv4vpn 开关） | EV-CA-02 §5.9, EV-TK-04 KP-04/10 |
| `ADDBGPPEER` | ADD BGPPEER | ADD | BGPPEER | BGP 对等体（EBGPMAXHOP=10；用 Loopback 建 eBGP 邻居） | EV-CA-02 §5.8, EV-TK-04 KP-04 |
| `ADDBGPPEERAF` | ADD BGPPEERAF | ADD | BGPPEERAF | BGP 对等体地址族（APPLYLABELMODE=perNexthop 节省标签） | EV-CA-02 §5.9, EV-TK-04 KP-04/10 |
| `ADDIMPORTROUTE` | ADD IMPORTROUTE | ADD | IMPORTROUTE | BGP 引入路由（IMPORTPROTOCOL=wlr；BGP 自身不能发现路由） | EV-CA-02 §5.8, EV-TK-04 KP-04 |
| `ADDNETWORKROUTE` | ADD NETWORKROUTE | ADD | NETWORKROUTE | Loopback 路由引入 BGP | EV-CA-02 附录B.4, EV-TK-04 KP-04 |
| `ADDSRROUTE` | ADD SRROUTE | ADD | SRROUTE | 手动 IPv4 静态路由（SESSIONNAME 绑定 BFD；SDN: DHCPENABLE=TRUE） | EV-CA-02 §4.1/§4.2, EV-TK-04/05 |
| `ADDSRROUTE6` | ADD SRROUTE6 | ADD | SRROUTE6 | 手动 IPv6 静态路由 | EV-CA-02 §4.4, EV-TK-04 KP-06 |

### 1.5 BFD/隧道/级联口/入不转板类（11个，CS-4）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `SETBFD` | SET BFD | SET | BFD | 全局激活 BFD（BFDENABLE=TRUE） | EV-CA-02 §3.2层2, EV-TK-04 |
| `ADDBFDSESSION` | ADD BFDSESSION | ADD | BFDSESSION | 手动 BFD 会话（LOCALDISCR/REMOTEDISCR/ONEARMECHO；双向或单臂） | EV-CA-02 §4.1/§4.2, EV-TK-05 |
| `ADDGRETUNNEL` | ADD GRETUNNEL | ADD | GRETUNNEL | GRE 隧道（PGW-U/UPF↔WAP 网关，基于 Loopback） | EV-CA-02 §4.3/附录B.4, EV-TK-04/05 |
| `MODGRETUNNEL` | MOD GRETUNNEL | MOD | GRETUNNEL | 修改 GRE 隧道 | EV-CA-02 附录B.4, EV-TK-04/05 |
| `SETMPLSSITE` | SET MPLSSITE | SET | MPLSSITE | MPLS 全局使能 | EV-CA-02 §3.2层2, EV-TK-04 KP-10 |
| `ADD/MPLSIF` | ADD MPLSIF | ADD | MPLSIF | MPLS 接口（手动逐个；自动部署用 ADD AUTOSCALINGMPLS 替代） | EV-CA-02 §4.2, EV-TK-04/05 KP-11 |
| `ADDNPDIRECTCONNECTPORT` | ADD NPDIRECTCONNECTPORT | ADD | NPDIRECTCONNECTPORT | NP 卡级联口（NP100 多框级联，有 P3/P4） | EV-CA-02 §4.3/附录B.4, EV-TK-06 KP-03/04 |
| `SETDATAPLANEGIINFMODE` | SET DATAPLANEGIINFMODE | SET | DATAPLANEGIINFMODE | 入不转板：GI 接口模式（中心云下行入不转板） | EV-CA-02 §6.4/附录B.4, EV-TK-04 KP-04 |
| `SETDATAPLANEINFMODE` | SET DATAPLANEINFMODE | SET | DATAPLANEINFMODE | 入不转板：数据面接口模式（与上一条区分） | EV-CA-02 §6.4/附录B.4, EV-TK-04 KP-04 |
| `SETDHCP6CLIENTDUID` | SET DHCP6CLIENTDUID | SET | DHCP6CLIENTDUID | SDN IPv6 DHCPv6 前置（DUIDTYPE=MAC_PLUS_VLAN 必配） | EV-CA-02 §4.1, EV-TK-06 |
| `ADDIPSEC*` | ADD IPsec 系列命令 | ADD | IPSEC | IPsec 隧道（跨安全域加密 Sxa/Sxb/N4/S1-U/N3，**高危二次授权**） | EV-CA-02 §4.3/§3.5, EV-TK-04/05 |

### 1.6 自动部署模板族（11个，CS-4）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `SETAUTOCONFIG` | SET AUTOCONFIG | SET | AUTOCONFIG | 自动配置总开关（SWITCHFLAG=FALSE/TRUE；关→配模板→开） | EV-CA-02 §3.2层5/§5.10, EV-TK-04 KP-01 |
| `LSTAUTOCONFIG` | LST AUTOCONFIG | LST | AUTOCONFIG | 查询自动配置开关状态 | EV-CA-02 §5.10, EV-TK-04 KP-01 |
| `DSPOPSASSISTSTATE` | DSP OPSASSISTSTATE | DSP | OPSASSISTSTATE | 自动部署助手状态（必须 Ready；autoscaling_autoconfig.py） | EV-CA-02 §3.2层5/§5.10, EV-TK-04 KP-01 |
| `ADDAUTOSCALINGSERVICE` | ADD AUTOSCALINGSERVICE | ADD | AUTOSCALINGSERVICE | ★外联口自动部署主模板（VPN/地址族/地址池/VLAN/接口类型/路由使能） | EV-CA-02 §3.3, EV-TK-04 KP-01 |
| `MODAUTOSCALINGSERVICE` | MOD AUTOSCALINGSERVICE | MOD | AUTOSCALINGSERVICE | 修改外联口模板（ISBACKUP=TRUE 仅中心云；MTU 同步） | EV-CA-02 §4.2/§5.5, EV-TK-04 |
| `RMVAUTOSCALINGSERVICE` | RMV AUTOSCALINGSERVICE | RMV | AUTOSCALINGSERVICE | 删除外联口模板 | EV-CA-02 附录B.5, EV-TK-04 |
| `LSTAUTOSCALINGSERVICE` | LST AUTOSCALINGSERVICE | LST | AUTOSCALINGSERVICE | 查询外联口模板 | EV-CA-02 附录B.6, EV-TK-04 |
| `ADDAUTOSCALINGETHTRUNK` | ADD AUTOSCALINGETHTRUNK | ADD | AUTOSCALINGETHTRUNK | SR-IOV bonding Eth-trunk 模板（VNICLIST 两 MAC 相同且 ID 连续） | EV-CA-02 §3.3, EV-TK-04/05 KP-08 |
| `ADDAUTOSCALINGBFD` | ADD AUTOSCALINGBFD | ADD | AUTOSCALINGBFD | BFD 会话模板（ONEARMECHO=TRUE 单臂 echo） | EV-CA-02 §3.3/§4.1, EV-TK-04/06 |
| `ADDAUTOSCALINGSRBFD` | ADD AUTOSCALINGSRBFD | ADD | AUTOSCALINGSRBFD | 静态路由动态 BFD 模板（双向） | EV-CA-02 §3.3, EV-TK-04 KP-03 |
| `ADDAUTOSCALINGSRROUTE` | ADD AUTOSCALINGSRROUTE | ADD | AUTOSCALINGSRROUTE | 静态路由模板 | EV-CA-02 §3.3/§4.2, EV-TK-04 KP-03 |
| `ADDAUTOSCALINGBGPLF` | ADD AUTOSCALINGBGPLF | ADD | AUTOSCALINGBGPLF | BGP 入不转板策略模板 | EV-CA-02 §3.3, EV-TK-04 KP-04 |
| `ADDAUTOSCALINGIPREACH` | ADD AUTOSCALINGIPREACH | ADD | AUTOSCALINGIPREACH | RU 可达性检测模板（入不转板配套） | EV-CA-02 §3.3, EV-TK-04 KP-04 |
| `ADDAUTOSCALINGMPLS` | ADD AUTOSCALINGMPLS | ADD | AUTOSCALINGMPLS | MPLS 接口自动化模板（VM 扩容自动适配；替代手动 ADD MPLSIF） | EV-CA-02 §3.3/§4.2, EV-TK-04 KP-10 |

> 表内含 4 个 RMV/MOD/LST 变体，主 ADD 模板共 8 个（AUTOSCALINGSERVICE/ETHTRUNK/BFD/SRBFD/SRROUTE/BGPLF/IPREACH/MPLS），与 cross-topic §3.3 一致。

### 1.7 验证/查询类（26个，全局）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------|
| `LSTLOGICINF` | LST LOGICINF | LST | LOGICINF | 查询逻辑接口 | EV-CA-02 附录B.6, EV-TK-03 |
| `LSTVPNINST` | LST VPNINST | LST | VPNINST | 查询 VPN 实例 | EV-CA-02 附录B.6 |
| `LSTAPN` | LST APN | LST | APN | 查询 APN | EV-CA-02 附录B.6, EV-TK-03 |
| `LSTPOOL` / `LSTSECTION` / `LSTPOOLGROUP` / `LSTPOOLBINDGROUP` / `LSTPOOLGRPMAP` | 地址池五件套查询 | LST | POOL/SECTION/POOLGROUP/POOLBINDGROUP/POOLGRPMAP | 查询地址池族（5命令聚合） | EV-CA-02 附录B.6, EV-TK-03 |
| `LSTINTERFACE` | LST INTERFACE | LST | INTERFACE | 查询物理接口 | EV-CA-02 附录B.6 |
| `LSTIFIPV4ADDRESS` / `LSTIFIPV6ADDRESS` | 接口 IP 查询 | LST | IFIPV4ADDRESS/IFIPV6ADDRESS | 查询接口 IPv4/IPv6 地址（2命令聚合） | EV-CA-02 附录B.6 |
| `LSTIPBINDVPN` | LST IPBINDVPN | LST | IPBINDVPN | 查询接口绑定 VPN | EV-CA-02 附录B.6 |
| `LSTOSPF` / `LSTOSPFAREA` / `LSTOSPFINTERFACE` / `LSTOSPFNETWORK` / `LSTOSPFIMPORTROUTE` | OSPF 查询族 | LST | OSPF 系列 | 查询 OSPF 各对象（5命令聚合） | EV-CA-02 附录B.6, EV-TK-04 |
| `LSTBGPPEER` | LST BGPPEER | LST | BGPPEER | 查询 BGP 对等体 | EV-CA-02 附录B.6, EV-TK-04 |
| `LSTBGPVRFAF` | LST BGPVRFAF | LST | BGPVRFAF | 查询 BGP 地址族 | EV-CA-02 附录B.6 |
| `LSTFABRICMTU` | LST FABRICMTU | LST | FABRICMTU | 查询 Fabric MTU | EV-CA-02 附录B.6 |
| `DSPBGPPEERINFO` | DSP BGPPEERINFO | DSP | BGPPEERINFO | 查询 BGP 对等体详情（=Established 为成功） | EV-CA-02 §9.3/附录B.6, EV-TK-07 KP-08 |
| `DSPROUTE` / `DSPROUTE6` | 路由表查询 | DSP | ROUTE/ROUTE6 | 查询 IPv4/IPv6 路由表（2命令聚合） | EV-CA-02 §9.3, EV-TK-07 |
| `DSPSRROUTE` | DSP SRROUTE | DSP | SRROUTE | 查询静态路由（多条等开销 + 不同 ISU = 负荷分担正常） | EV-CA-02 §9.3, EV-TK-07 KP-08 |
| `DSPOSPFROUTING` | DSP OSPFROUTING | DSP | OSPFROUTING | 查询 OSPF 路由 | EV-CA-02 §9.3, EV-TK-07 |
| `DSPOSPFINTERFACE` | DSP OSPFINTERFACE | DSP | OSPFINTERFACE | 查询 OSPF 接口状态 | EV-CA-02 附录B.6, EV-TK-07 |
| `DSPOSPFPEER` | DSP OSPFPEER | DSP | OSPFPEER | 查询 OSPF 邻居 | EV-CA-02 附录B.6, EV-TK-07 |
| `DSPBFDSESSION` | DSP BFDSESSION | DSP | BFDSESSION | 查询 BFD 会话状态 | EV-CA-02 附录B.6 |
| `DSPIFSTATUS` | DSP IFSTATUS | DSP | IFSTATUS | 查询接口状态（UP/Down） | EV-CA-02 附录B.6 |
| `DSPSESSIONINFO` | DSP SESSIONINFO | DSP | SESSIONINFO | ★FirstCall 成功标志：APN/RoleType/IPv4 PDP/Session时间戳 | EV-CA-02 §9.2/附录B.6, EV-TK-07 KP-08 |
| `DSPSERVICERUSTATE` | DSP SERVICERUSTATE | DSP | SERVICERUSTATE | 查询所有 RU 状态（调测阶段须全部正常） | EV-CA-02 §9.2/附录B.6, EV-TK-07 KP-08 |
| `DSPRVKLICINFO` | DSP RVKLICINFO | DSP | RVKLICINFO | License 失效码查询 | EV-CA-02 附录B.1, EV-TK-01 KP-09~11 |
| `LSTNPDIRECTCONNECTPORT` / `RMVNPDIRECTCONNECTPORT` | NP 级联口查询/删除 | LST/RMV | NPDIRECTCONNECTPORT | NP 卡级联口查询与删除（2命令聚合） | EV-CA-02 附录B.4, EV-TK-06 |
| `SRVPING` | SRVPING | PING | SRVPING | 业务 Ping（SRCIPTYPE=LOGICINF/POOL；调测 UDG→对端） | EV-CA-02 §6.1/附录B.6, EV-TK-03/07 |
| `SRVTRACERT` | SRVTRACERT | TRACERT | SRVTRACERT | 业务 Tracert（故障定位） | EV-CA-02 §6.1/附录B.6, EV-TK-03/07 |
| `NGPING` | NGPING | PING | NGPING | 服务化/网络 Ping（Nupf；多 ISU 逐个） | EV-CA-02 附录B.6, EV-TK-07 KP-08 |
| `PING` | PING | PING | PING | 物理 Ping（直连路由器→UDG 回程验证） | EV-CA-02 §9.2, EV-TK-07 KP-08 |
| `EXPMML` | EXP MML | EXP | MML | 导出 MML 配置（兜底故障收集） | EV-CA-02 附录B.6, EV-TK-07 |

---

## 2. CommandParameter 实例化（关键命令必选参数）

> 字段顺序遵循 Schema §11.4：`parameter_id / command_ref / parameter_name / required_mode / enum_values / description`。

### 2.1 ADD LOGICINF（接口配置核心，掩码统一约束）

| `parameter_id` | `command_ref` | `parameter_name` | `required_mode` | `enum_values` | `description` |
|---------------|---------------|------------------|-----------------|---------------|---------------|
| P-LOGICINF-01 | ADD LOGICINF | NAME | required | — | 逻辑接口名（N4if1/0/0 / Saif1/1/N / Scif1/1/N / Paif1/1/N；N=0~31） |
| P-LOGICINF-02 | ADD LOGICINF | IPVERSION | required | IPV4 / IPV6 / IPVER_ALL | IP 版本；双栈用 IPVER_ALL |
| P-LOGICINF-03 | ADD LOGICINF | IPV4ADDRESS1 | conditional_required | — | IPv4 地址（IPVERSION=IPV4/IPVER_ALL 必填） |
| P-LOGICINF-04 | ADD LOGICINF | IPV4MASK1 | required | — | **固定 255.255.255.255（/32 主机路由，CR-ND-02）** |
| P-LOGICINF-05 | ADD LOGICINF | VPNINSTANCE | required | — | VPN 实例（VPN_Signaling/VPN_Access 等，CR-ND-03 四统一） |
| P-LOGICINF-06 | ADD LOGICINF | SLICEATTRSW | optional | ENABLE / DISABLE | 切片绑定开关（仅 Saif/N3if；ENABLE 后需 ADD SNSSAIUPINTF） |

### 2.2 ADD VPNINST / ADD L3VPNINST（VPN实例层）

| `parameter_id` | `command_ref` | `parameter_name` | `required_mode` | `enum_values` | `description` |
|---------------|---------------|------------------|-----------------|---------------|---------------|
| P-VPNINST-01 | ADD VPNINST | VPNINSTANCE | required | — | 业务/信令面 VPN 名（VPN_Signaling/VPN_Access） |
| P-L3VPNINST-01 | ADD L3VPNINST | VPNNAME | required | — | 路由侧 L3VPN 名（VPN_Access/VRF_Internet/VRF_PDNx；MPLS 用 _public_） |
| P-VPNINSTAF-01 | ADD VPNINSTAF | VPNNAME | required | — | 关联 L3VPN 实例 |
| P-VPNINSTAF-02 | ADD VPNINSTAF | AFTYPE | required | ipv4uni / ipv6uni | 地址族；双栈两个都要配 |
| P-VPNINSTAF-03 | MOD VPNINSTAF | VRFRD | conditional_required | — | 路由标识（MPLS VPN 必配，不同 VPN 实例不能重复 CR-ND-08） |
| P-VPNINSTAF-04 | MOD VPNINSTAF | VRFLABELMODE | optional | perInstance | 标签节省：与 BGP perNexthop 组合 |

### 2.3 ADD OSPF / ADD OSPFV3（OSPF 进程）

| `parameter_id` | `command_ref` | `parameter_name` | `required_mode` | `enum_values` | `description` |
|---------------|---------------|------------------|-----------------|---------------|---------------|
| P-OSPF-01 | ADD OSPF | OSPFPROCID | required | — | OSPF 进程 ID |
| P-OSPF-02 | ADD OSPF | SCHEMAROUID | required | — | OSPF Router ID（IPv4） |
| P-OSPFV3-01 | ADD OSPFV3 | OSPFPROCID | required | — | OSPFv3 进程 ID |
| P-OSPFV3-02 | ADD OSPFV3 | ROUTERID | required | — | OSPFv3 Router ID（与 IPv4 共用一个 ROUTERID） |
| P-OSPFV3-03 | ADD OSPFV3 | DETECTMULINTV | optional | — | OSPFv3 检测倍数间隔 |
| P-OSPFAREA-01 | ADD OSPFAREA | AREAID | required | — | 区域 ID；NSSA 区域需配 Loopback 自动选 FA |
| P-OSPFIMPORTROUTE-01 | ADD OSPFIMPORTROUTE | IMPORTPROTOCOL | required | wlr | 引入用户下行路由（wlr 协议标识） |

### 2.4 ADD BGPPEER / ADD BGPVRFAF（BGP 对等体与地址族）

| `parameter_id` | `command_ref` | `parameter_name` | `required_mode` | `enum_values` | `description` |
|---------------|---------------|------------------|-----------------|---------------|---------------|
| P-BGPVRF-01 | ADD BGPVRF | VRFNAME | required | — | BGP VPN 实例名（MPLS: _public_） |
| P-BGPVRF-02 | ADD BGPVRF | ROUTERID | required | — | BGP Router ID（双栈共用；删 IPv4 地址族前需查记录 ROUTERID 用 MOD BGPVRF 补回） |
| P-BGPVRFAF-01 | ADD BGPVRFAF | VRFNAME | required | — | 关联 BGP VPN 实例 |
| P-BGPVRFAF-02 | ADD BGPVRFAF | AFTYPE | required | ipv4 / ipv6 / ipv4vpn | 地址族；ipv4vpn=MPLS MP-EBGP 开关 |
| P-BGPPEER-01 | ADD BGPPEER | PEERADDR | required | — | 对等体地址（用 Loopback 建 eBGP） |
| P-BGPPEER-02 | ADD BGPPEER | EBGPMAXHOP | conditional_required | — | eBGP 最大跳数（=10，Loopback 邻居必配） |
| P-BGPPEERAF-01 | ADD BGPPEERAF | APPLYLABELMODE | optional | perNexthop | 标签节省：与 VPN perInstance 组合 |
| P-IMPORTROUTE-01 | ADD IMPORTROUTE | IMPORTPROTOCOL | required | wlr | BGP 引入用户下行路由（BGP 自身不能发现路由 CR-ND-06） |

### 2.5 ADD APN / SET IPALLOCRULE（会话接入）

| `parameter_id` | `command_ref` | `parameter_name` | `required_mode` | `enum_values` | `description` |
|---------------|---------------|------------------|-----------------|---------------|---------------|
| P-APN-01 | ADD APN | APN | required | — | APN/DNN 实例名（UDG 本端与 C 面一致） |
| P-APN-02 | ADD APN | HASVPN | conditional_required | ENABLE / DISABLE | IPv4 绑定 VPN（CR-ND-03 四统一） |
| P-APN-03 | ADD APN | HASVPNIPV6 | conditional_required | ENABLE / DISABLE | IPv6 绑定 VPN |
| P-APN-04 | ADD APN | VPNINSTANCE | conditional_required | — | 关联 VPN（HASVPN=ENABLE 时必填） |
| P-POOL-01 | ADD POOL | POOLTYPE | required | LOCAL / EXTERNAL | LOCAL=UDG 分配 IP；EXTERNAL=外部 NF 分配（仅 POOL+SECTION，可选 CHECKIPVALID） |
| P-IPALLOCRULE-01 | SET IPALLOCRULE | FIRSTRULESW | required | ENABLE / DISABLE | 第一级规则开关 |
| P-IPALLOCRULE-02 | SET IPALLOCRULE | FIRSTRULE | conditional_required | — | 规则串（默认 APN-1&LOCATION-0&SMF-0，仅 APN 维度使能） |

### 2.6 SET BFD / ADD BFDSESSION（BFD 模式）

| `parameter_id` | `command_ref` | `parameter_name` | `required_mode` | `enum_values` | `description` |
|---------------|---------------|------------------|-----------------|---------------|---------------|
| P-BFD-01 | SET BFD | BFDENABLE | required | TRUE / FALSE | 全局 BFD 使能 |
| P-BFDSESS-01 | ADD BFDSESSION | ONEARMECHO | conditional_required | TRUE / FALSE | 单臂 Echo 模式（SDN/网络加速卡/DC-GW双活强制 TRUE CR-ND-05） |
| P-BFDSESS-02 | ADD BFDSESSION | LOCALDISCR | required | — | 本地标识符（双向 BFD 必配） |
| P-BFDSESS-03 | ADD BFDSESSION | REMOTEDISCR | required | — | 远端标识符（双向 BFD 必配） |
| P-BFDSESS-04 | ADD BFDSESSION | DESTIP | required | — | 目的 IP（非SDN: 网关 IP；SDN: Leaf 节点 IP） |

### 2.7 ADD AUTOSCALINGSERVICE（★自动部署主模板，三态差异）

| `parameter_id` | `command_ref` | `parameter_name` | `required_mode` | `enum_values` | `description` |
|---------------|---------------|------------------|-----------------|---------------|---------------|
| P-ASS-01 | ADD AUTOSCALINGSERVICE | SERVICENAME | required | — | 服务名 |
| P-ASS-02 | ADD AUTOSCALINGSERVICE | VPNNAME | required | — | 关联 VPN（MPLS 用 _public_） |
| P-ASS-03 | ADD AUTOSCALINGSERVICE | AFTYPE | required | IPv4 / IPv6 | 地址族 |
| P-ASS-04 | ADD AUTOSCALINGSERVICE | IPALLOCTYPE4 / IPALLOCTYPE6 | required | USER_CONFIG / DHCP | 外联口 IP 获取（非SDN=USER_CONFIG；SDN=DHCP CR-ND-05） |
| P-ASS-05 | ADD AUTOSCALINGSERVICE | NEXTHOPALLOCTYPE4 / NEXTHOPALLOCTYPE6 | required | CONFIG / DHCP | 下一跳获取（非SDN=CONFIG；SDN=DHCP） |
| P-ASS-06 | ADD AUTOSCALINGSERVICE | AUTOCFGIFTYPE | required | VNIC / ETHTRUNK | 接口类型（非 bonding=VNIC；SR-IOV bonding=ETHTRUNK；网络加速卡强制 ETHTRUNK） |
| P-ASS-07 | ADD AUTOSCALINGSERVICE | VNICID | conditional_required | — | VNIC ID（AUTOCFGIFTYPE=VNIC 必填；ETHTRUNK 去掉） |
| P-ASS-08 | ADD AUTOSCALINGSERVICE | ETHTRUNKTMPID | conditional_required | — | Eth-trunk 模板 ID（AUTOCFGIFTYPE=ETHTRUNK 必填，引用 AUTOSCALINGETHTRUNK） |
| P-ASS-09 | ADD AUTOSCALINGSERVICE | OSPFENABLE | conditional_required | TRUE / FALSE | OSPF 使能（仅非SDN OSPF 方案；SDN/网络加速卡不支持） |
| P-ASS-10 | ADD AUTOSCALINGSERVICE | OSPFPROCID | conditional_required | — | OSPF 进程 ID（OSPFENABLE=TRUE 必填） |
| P-ASS-11 | ADD AUTOSCALINGSERVICE | OSPFAREAID | conditional_required | — | OSPF 区域 ID（OSPFENABLE=TRUE 必填） |
| P-ASS-12 | MOD AUTOSCALINGSERVICE | ISBACKUP | optional | TRUE | 备份标志（仅中心云场景） |

---

## 3. ConfigObject 实例化（58个）

> 字段顺序遵循 Schema §11.5：`object_id / object_name / identifier_parameters / object_kind / description / source_evidence_ids`。

### 3.1 接口与VPN（8个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
|-------------|---------------|-------------------------|---------------|---------------|----------------------|
| `OBJ-ND-VPNINST` | VPNInstance | VPNINSTANCE | entity | 业务/信令面 VPN 实例（CS-1/CS-2 接口侧；ADD VPNINST） | EV-CA-02 §3.1 |
| `OBJ-ND-LOGICINF` | LogicInterface | NAME, IPVERSION, IPV4ADDRESS1, VPNINSTANCE | entity | 业务逻辑接口（N4if/Saif/Scif/Paif/S11-uif；掩码固定 /32） | EV-CA-02 §3.1 |
| `OBJ-ND-N4IF` | N4Interface | NAME="N4if1/0/0" | entity | N4 强制合一抽象接口（N4/Sxa/Sxb，UPF 唯一必备接口） | EV-CA-02 §5.1/§5.2 |
| `OBJ-ND-PAIF` | PaInterface | NAME="Paif1/1/N" | entity | Pa 强制合一抽象接口（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U） | EV-CA-02 §5.2 |
| `OBJ-ND-SAIF` | SaInterface | NAME, SLICEATTRSW | entity | Sa 可选合一抽象接口（Sa/N3/S1-U；与独立配置互斥） | EV-CA-02 §5.2/§7.1 |
| `OBJ-ND-SCIF` | ScInterface | NAME | entity | Sc 可选合一抽象接口（Sc/N9c/S5-S/S8-S） | EV-CA-02 §5.2 |
| `OBJ-ND-EXTIF` | ExternalInterface | IFNAME, VLAN, MTU | entity | 外联口（SGi/N6 物理外联口、子接口、Eth-trunk；手动部署逐条配） | EV-CA-02 §3.2层4 |
| `OBJ-ND-LOOPBACK` | LoopbackInterface | NAME, IPADDR | entity | Loopback 接口（BGP/MPLS 必备；MPLS 不绑 VPN） | EV-CA-02 §5.8/§5.9 |
| `OBJ-ND-SNSSAI` | SNSSAIBinding | LOGICINFNAME, SNSSAI | binding | 切片与接口绑定（仅 Saif/N3if） | EV-CA-02 §6.2 |
| `OBJ-ND-NUPF` | NupfInterface | LOGICIP, HTTPLEGRP | composite | Nupf 服务化接口（接 NWDAF，HTTP/SBI） | EV-CA-02 附录B.2 |

### 3.2 会话接入（7个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
|-------------|---------------|-------------------------|---------------|---------------|----------------------|
| `OBJ-ND-APN` | APN | APN, HASVPN, VPNINSTANCE | entity | APN/DNN 实例（与 C 面一致） | EV-CA-02 §3.4 |
| `OBJ-ND-POOL` | AddressPool | POOLNAME, POOLTYPE(LOCAL/EXTERNAL) | entity | 地址池 | EV-CA-02 §3.4 |
| `OBJ-ND-SECTION` | AddressSection | POOLNAME, SECTIONNUM, V4STARTIP/V4ENDIP 或 V6PREFIXSTART/END/LENGTH | entity | 地址段（IPv6 LENGTH=64） | EV-CA-02 §4.4 |
| `OBJ-ND-POOLGROUP` | PoolGroup | POOLGROUPNAME | composite | 地址池组（contains POOL） | EV-CA-02 §3.4 |
| `OBJ-ND-POOLBIND` | PoolBinding | POOLGROUPNAME, POOLNAME | binding | 地址池绑定到组 | EV-CA-02 §3.4 |
| `OBJ-ND-POOLGRPMAP` | PoolGroupMap | APN, POOLGROUPNAME | binding | APN↔POOLGROUP 映射（refers_to POOLGROUP） | EV-CA-02 §3.4 |
| `OBJ-ND-IPALLOCRULE` | IPAllocRule | FIRSTRULESW, FIRSTRULE | entity | 三级地址分配规则（默认仅 APN 维度使能） | EV-CA-02 §3.4 |

### 3.3 路由协议（12个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
|-------------|---------------|-------------------------|---------------|---------------|----------------------|
| `OBJ-ND-L3VPN` | L3VPNInstance | VPNNAME | entity | 路由侧 L3VPN 实例（区别于业务面 VPNInstance） | EV-CA-02 §3.2层1 |
| `OBJ-ND-VPNAF` | VPNAddressFamily | VPNNAME, AFTYPE | entity | VPN 地址族（ipv4uni/ipv6uni；双栈两个） | EV-CA-02 §4.4 |
| `OBJ-ND-VPNTARGET` | VPNTarget | VPNNAME, EXPORTEXTCOMM/IMPORTEXTCOMM | entity | VPN RT（路由导入导出标记） | EV-CA-02 附录B.4 |
| `OBJ-ND-OSPFPROC` | OSPFProcess | OSPFPROCID, SCHEMAROUID | entity | OSPF IPv4 进程 | EV-CA-02 §4.4 |
| `OBJ-ND-OSPFAREA` | OSPFArea | OSPFPROCID, AREAID | entity | OSPF 区域（NSSA 需配 Loopback） | EV-CA-02 §4.4 |
| `OBJ-ND-OSPFIF` | OSPFInterface | OSPFPROCID, IFNAME | binding | OSPF 接口使能 | EV-CA-02 附录B.4 |
| `OBJ-ND-SRROUTE` | StaticRoute | PREFIX4/PREFIX6, NEXTHOP4/NEXTHOP6, SESSIONNAME | entity | 静态路由（SESSIONNAME 绑定 BFD） | EV-CA-02 §4.4 |
| `OBJ-ND-BGPINST` | BGPInstance | — | entity | BGP 全局使能对象 | EV-CA-02 §3.2层2 |
| `OBJ-ND-BGPVRF` | BGPVRF | VRFNAME, ROUTERID | entity | BGP VPN 实例 | EV-CA-02 §5.9 |
| `OBJ-ND-BGPAF` | BGPAddressFamily | VRFNAME, AFTYPE | entity | BGP 地址族（ipv4/ipv6/ipv4vpn） | EV-CA-02 §5.9 |
| `OBJ-ND-BGPPEER` | BGPPeer | PEERADDR, EBGPMAXHOP | entity | BGP 对等体（用 Loopback 建 eBGP） | EV-CA-02 §5.8 |
| `OBJ-ND-NETWORKROUTE` | NetworkRoute | PREFIX, VRFNAME | entity | Loopback 路由引入 BGP | EV-CA-02 附录B.4 |

### 3.4 BFD/隧道/MPLS/NP（9个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
|-------------|---------------|-------------------------|---------------|---------------|----------------------|
| `OBJ-ND-BFDSESS` | BFDSession | LOCALDISCR, REMOTEDISCR, ONEARMECHO, DESTIP | entity | BFD 会话（双向/单臂 Echo） | EV-CA-02 §4.1 |
| `OBJ-ND-GRETUNNEL` | GRETunnel | TUNNELNAME, SOURCEIP, DESTIP | entity | GRE 隧道（基于 Loopback） | EV-CA-02 §4.3 |
| `OBJ-ND-MPLSGLOBAL` | MPLSGlobal | MPLSSITE | entity | MPLS 全局使能 | EV-CA-02 §3.2层2 |
| `OBJ-ND-MPLSIF` | MPLSInterface | IFNAME | binding | MPLS 接口（手动逐个；自动用 AUTOSCALINGMPLS 替代） | EV-CA-02 §4.2 |
| `OBJ-ND-IPSEC` | IPsecSA | SA_NAME, SPI | entity | IPsec 安全联盟（跨安全域加密，高危二次授权） | EV-CA-02 §4.3/§3.5 |
| `OBJ-ND-NPCASCADE` | NPCascadePort | PORTID, MODEL(NP100 P3/P4) | entity | NP 卡级联口（NP100 多框级联） | EV-CA-02 §4.3 |
| `OBJ-ND-DPGIINFMODE` | DataPlaneGiInfMode | MODE | entity | 入不转板：GI 接口模式 | EV-CA-02 §6.4 |
| `OBJ-ND-DPINFMODE` | DataPlaneInfMode | MODE | entity | 入不转板：数据面接口模式（与上一条区分） | EV-CA-02 §6.4 |
| `OBJ-ND-DHCP6DUID` | DHCPv6ClientDUID | DUIDTYPE | entity | SDN IPv6 DHCPv6 DUID（MAC_PLUS_VLAN 必配） | EV-CA-02 §4.1 |

### 3.5 自动部署模板（9个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
|-------------|---------------|-------------------------|---------------|---------------|----------------------|
| `OBJ-ND-AUTOCONFIG` | AutoConfigSwitch | SWITCHFLAG | entity | 自动配置总开关（关→配模板→开，DSP OPSASSISTSTATE 确认 Ready） | EV-CA-02 §5.10 |
| `OBJ-ND-ASS` | AutoScalingService | SERVICENAME, VPNNAME, AFTYPE, IPALLOCTYPE4/6, AUTOCFGIFTYPE | composite | ★外联口自动部署主模板（三态差异核心） | EV-CA-02 §3.3 |
| `OBJ-ND-ASETHTRUNK` | AutoScalingEthTrunk | ETHTRUNKTMPID, VNICLIST | entity | SR-IOV bonding Eth-trunk 模板 | EV-CA-02 §3.3 |
| `OBJ-ND-ASBFD` | AutoScalingBFD | SESSIONNAME, ONEARMECHO | entity | BFD 会话模板（单臂 echo） | EV-CA-02 §3.3 |
| `OBJ-ND-ASSRBFD` | AutoScalingSRBFD | SESSIONNAME | entity | 静态路由动态 BFD 模板（双向） | EV-CA-02 §3.3 |
| `OBJ-ND-ASSRROUTE` | AutoScalingSRRoute | PREFIX, NEXTHOP | entity | 静态路由模板 | EV-CA-02 §3.3 |
| `OBJ-ND-ASBGPLF` | AutoScalingBGPLF | POLICYNAME | entity | BGP 入不转板策略模板 | EV-CA-02 §3.3 |
| `OBJ-ND-ASIPREACH` | AutoScalingIPReach | RU_ID | entity | RU 可达性检测模板 | EV-CA-02 §3.3 |
| `OBJ-ND-ASMPLS` | AutoScalingMPLS | IFNAME | entity | MPLS 接口自动化模板（VM 扩容自动适配） | EV-CA-02 §3.3 |

### 3.6 网管与基础（9个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
|-------------|---------------|-------------------------|---------------|---------------|----------------------|
| `OBJ-ND-NE` | NetworkElement | MEID, MENAME | entity | 网元身份 | EV-CA-02 §6.5 |
| `OBJ-ND-OMIP` | OMIP | FLOATIP, PHYSICALIP | entity | 浮动IP/物理IP（改后触发 CS-3 回流） | EV-CA-02 §5.6 |
| `OBJ-ND-NBUSER` | NorthboundUser | USERNAME, PASSWORD | entity | 北向对接用户（初次必须重置密码） | EV-CA-02 §5.7 |
| `OBJ-ND-SNMPUSER` | SNMPUser | USERNAME, AUTHKEY, ENCKEY | entity | SNMP 用户（认证/加密密钥必须重置且不相同） | EV-CA-02 §5.7 |
| `OBJ-ND-NMADAPTER` | NetworkMgmtAdapter | VERSION | entity | 网管适配层（华为支持网站下载） | EV-CA-02 §6.3 |
| `OBJ-ND-MANAGEDNE` | ManagedNE | NE_NAME, IP, TLS, OSS_AUTH, EMSACCOUNT, SNMPV3, PORT(8000), AUTH(AES256) | composite | 网管侧创建的网元（14 项参数） | EV-CA-02 §6.3 |
| `OBJ-ND-EMS` | EMSAssociation | VNF_ID, EMS_ID | binding | EMS 归属关系（VNF LCM 独立部署时检查） | EV-CA-02 §6.3 |
| `OBJ-ND-SECAUTH` | SecurityAuth | STATUS, USRSECAUTH, SECAUTHMEM | composite | 二次授权（总开关+用户+13类命令清单） | EV-CA-02 §3.5 |
| `OBJ-ND-GLOBALPARA` | GlobalParameter | PARANAME, PARAVALUE | entity | 11 项公共参数集 | EV-CA-02 §6.5 |

### 3.7 License/MTU/NTP/UPF标识（4个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
|-------------|---------------|-------------------------|---------------|---------------|----------------------|
| `OBJ-ND-LICENSE` | License | ESN, LICITEM, STATUS | entity | License 文件+控制项+状态机（OM Portal/U2020 双路径） | EV-CA-02 §6.5 |
| `OBJ-ND-MTU` | MTUConfig | FABRICMTU, IFMTU, SUBIFMTU | composite | MTU 三层（Fabric/Tunnel/外联口；网卡≥Fabric>主接口≥子接口） | EV-CA-02 §5.5 |
| `OBJ-ND-NTP` | NTPSource | SRVIP, SRVLEVEL | entity | 双路时间源（OMC + FusionStage） | EV-CA-02 §6.5 |
| `OBJ-ND-UPFID` | UPFIdentity | HOSTNAME | entity | UPF 标识（HOSTNAME 全网唯一，不配则 N4 偶联失败） | EV-CA-02 §6.1 |

---

## 4. ConfigObject 间关系边（contains/refers_to/depends_on/conflicts_with/composed_by/activates）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| VPNInstance | `contains` | LogicInterface | VPN 实例包含逻辑接口（N4if/Saif 等绑定 VPN） |
| L3VPNInstance | `contains` | VPNAddressFamily | L3VPN 实例包含地址族（ipv4uni/ipv6uni） |
| VPNAddressFamily | `refers_to` | VPNTarget | 地址族引用 RT 标记 |
| PoolGroup | `contains` | AddressPool | 地址池组包含地址池（via PoolBinding） |
| APN | `refers_to` | PoolGroup | APN 映射到地址池组（via PoolGroupMap） |
| AddressPool | `contains` | AddressSection | 地址池包含地址段 |
| LogicInterface(Saif) | `refers_to` | SNSSAIBinding | 接口绑定切片（仅 Saif/N3if） |
| OSPFProcess | `contains` | OSPFArea | OSPF 进程包含区域 |
| OSPFArea | `contains` | OSPFInterface | 区域包含接口使能 |
| BGPInstance | `contains` | BGPVRF | BGP 全局包含 VPN 实例 |
| BGPVRF | `contains` | BGPAddressFamily | BGP VPN 包含地址族 |
| BGPAddressFamily | `contains` | BGPPeer | 地址族包含对等体 |
| BGPAddressFamily | `refers_to` | NetworkRoute | 地址族引用 Loopback 路由 |
| StaticRoute | `depends_on` | BFDSession | 静态路由依赖 BFD 会话（SESSIONNAME 绑定） |
| BGPInstance | `depends_on` | OSPFProcess / StaticRoute | BGP 依赖 IGP 自动部署基础（BR-BGP-DEPENDENCY） |
| AutoScalingService | `refers_to` | AutoScalingEthTrunk | 外联口模板引用 Eth-trunk 模板（AUTOCFGIFTYPE=ETHTRUNK） |
| AutoScalingService | `activates` | OSPFProcess | 外联口模板 OSPFENABLE=TRUE 激活 OSPF（仅非SDN OSPF 方案） |
| AutoScalingSRRoute | `depends_on` | AutoScalingSRBFD / AutoScalingBFD | 静态路由模板依赖 BFD 模板 |
| MPLSGlobal | `contains` | MPLSInterface | MPLS 全局包含接口 |
| L3VPNInstance(MPLS _public_) | `conflicts_with` | VPNInstance(业务 VPN) | MPLS VPN 外联口绑 _public_，不绑业务 VPN（公私分离） |
| LoopbackInterface(MPLS) | `conflicts_with` | VPNInstance | MPLS Loopback 不绑 VPN（用公网 BGP 传私网路由） |
| LogicInterface | `conflicts_with` | ExternalInterface(同网段) | 逻辑接口 IP 不能与外联口/对端物理口同网段（IP网段隔离） |
| SaInterface | `conflicts_with` | N3if/S1-uif(独立) | Saif 合一与独立配置互斥（可选合一二元性） |
| ManagedNE | `composed_by` | NorthboundUser, SNMPUser, NetworkMgmtAdapter | 网管网元由北向用户+SNMP用户+适配层组合 |
| AutoConfigSwitch | `activates` | AutoScalingService(族) | 开关 TRUE 激活所有 AUTOSCALING 模板下发 |
| NupfInterface | `composed_by` | LogicIP, HTTPLEGRP, HTTPLE, SBIAPLE | Nupf 由 4 类对象组合 |

---

## 5. CommandRule（命令约束，governs MMLCommand）

> 字段顺序遵循 Schema §11.6：`rule_id / rule_name / rule_type / rule_expression_mode / rule_source_kind / scope_type / scope_ref / rule_logic / violation_effect / severity / source_evidence_ids`。反向关系：MMLCommand `governed_by` CommandRule。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|------------------------|--------------------|--------------|-------------|--------------|--------------|-------------------|------------|----------------------|
| `CR-ND-01` | N4 必备性 | semantic_rule | explicit | principle | command | ADD LOGICINF(NAME=N4if) | N4 是 UPF 唯一必配接口；N4 单独配不足以建立偶联，UDG 上至少需存在一个数据面逻辑接口 IP（Paif/Scif/Saif 任一） | N4 偶联异常，FirstCall 失败 | critical | EV-CA-02 §5.1/§7.2 |
| `CR-ND-02` | 接口掩码统一 | parameter_mutex | explicit | config | parameter | ADD LOGICINF:IPV4MASK1 | 所有业务逻辑接口 IPV4MASK1 固定 255.255.255.255（/32 主机路由） | 接口配置失败或路由异常 | critical | EV-CA-02 §3.1 |
| `CR-ND-03` | VPN 四统一 | object_reference_rule | explicit | principle | relation | ADD VPNINST/ADD APN/ADD LOGICINF:VPNINSTANCE | 业务 APN 绑定 VPN、地址池绑定 VPN、Gi/SGi/N6 外联口绑定 VPN、各业务逻辑接口绑定 VPN 四者必须一致 | 会话接入失败，路由不通 | critical | EV-CA-02 §3.1/§5.3 |
| `CR-ND-04` | 强制合一 vs 可选合一互斥 | restriction_rule | explicit | design | command | ADD LOGICINF(N4if/Paif/Saif/Scif) | N4if/Paif 强制合一（不支持独立 Sxa/Sxb/N9a 等）；Saif/Scif 可选合一，与独立配置互斥，已配独立再配抽象会失败 | 接口配置失败 | critical | EV-CA-02 §5.2/§7.1 |
| `CR-ND-05` | SDN 四强制 | restriction_rule | explicit | config | parameter | ADD AUTOSCALINGSERVICE(IPALLOCTYPE4/6,DHCP) + ADD AUTOSCALINGBFD(ONEARMECHO) + ADD SRROUTE(DHCPENABLE) | SDN 场景：外联口 IP+下一跳强制 DHCP、强制单臂 BFD Echo(DEST=Leaf IP)、强制 BGP over 静态(不支持 OSPF)、强制 SET DHCP6CLIENTDUID | SDN 路由不通，BFD 不生效 | critical | EV-CA-02 §4.1/§7.6 |
| `CR-ND-06` | BGP 依赖 IGP | precondition_rule | implicit | principle | command | ADD BGPPEER/ADD IMPORTROUTE | BGP 自身无自动部署（依赖 OSPF/静态 IGP 基础）；BGP 自身不能发现路由，必须 ADD IMPORTROUTE:IMPORTPROTOCOL=wlr；需专用 Loopback 建 eBGP(EBGPMAXHOP=10) | BGP 邻居建立失败，路由缺失 | critical | EV-CA-02 §5.8/§7.4 |
| `CR-ND-07` | 自动部署开关时序 | runtime_check_rule | explicit | ops | command | SET AUTOCONFIG + ADD AUTOSCALING* | 操作顺序：LST AUTOCONFIG → DSP OPSASSISTSTATE(Ready) → SET AUTOCONFIG:SWITCHFLAG=FALSE → 配所有 AUTOSCALING 模板 → SET AUTOCONFIG:SWITCHFLAG=TRUE → DSP OPSASSISTSTATE(确认 Ready) | 模板下发失败或部署不一致 | critical | EV-CA-02 §3.2层5/§5.10 |
| `CR-ND-08` | MPLS VPN 公私分离 | semantic_rule | explicit | design | object | ADD AUTOSCALINGSERVICE/ADD BGPVRF:VRFNAME | MPLS VPN 外联口 VPN 固定 _public_（不绑业务 VPN）；Loopback 不绑 VPN；MP-EBGP 用 IPv4 eBGP 传 IPv6 私网路由（不配 IPv6 外联口）；VRFRD 必配且不重复；perInstance+perNexthop 节省标签 | MPLS VPN 路由泄漏或标签浪费 | critical | EV-CA-02 §5.9/§7.5 |
| `CR-ND-09` | 入不转板命令区分 | syntax_rule | explicit | config | command | SET DATAPLANEGIINFMODE vs SET DATAPLANEINFMODE | 入不转板两条命令不同：DATAPLANEGIINFMODE（GI 接口模式）与 DATAPLANEINFMODE（数据面接口模式），不可混用 | 入不转板配置错误 | warning | EV-CA-02 §6.4/附录B.4 |
| `CR-ND-10` | MTU 层级与同步 | runtime_check_rule | explicit | ops | parameter | SET FABRICMTU/MOD INTERFACE:MTU/MOD AUTOSCALINGSERVICE | 层级：网卡 MTU ≥ Fabric MTU > 主接口 MTU ≥ 子接口 MTU；外联口 MTU 必须与直连下一跳网关一致(默认1500)；仅改接口 MTU 不同步 MOD AUTOSCALINGSERVICE 触发告警 ALM-232398849；Eth-trunk 不改成员口 MTU，加入前改会失败 | 告警或添加失败，分片丢包 | warning | EV-CA-02 §5.5 |
| `CR-ND-11` | 高危命令二次授权 | precondition_rule | explicit | ops | command | SET OMIP/SET FWDPARA/IPsec 系列 | 13类 UDG 默认二次授权命令（SET OMIP/MOD VIRTUALIP/SET FWDPARA/IPsec 等），开局脚本必须先 SET SECAUTH:STATUS=ON + ADD USRSECAUTH + ADD SECAUTHMEM 才能避免弹窗阻塞 | 自动化脚本阻塞 | warning | EV-CA-02 §3.5 |
| `CR-ND-12` | 网管密码三元组 | validation_rule | explicit | ops | object | NorthboundUser, SNMPUser | 北向对接用户初次必须重置密码；SNMP 用户必须重置共享认证密钥和共享加密密钥且两者不能相同；任一不满足对接直接失败 | 网管对接失败（开局最常见原因） | critical | EV-CA-02 §5.7 |
| `CR-ND-13` | CS-5→CS-3 回流 | runtime_check_rule | implicit | case | command | SET OMIP | 修改浮动 IP(SET OMIP) 会中断网管和 VNFM 连接，必须重对接网管（CS-3 完整5步重跑）；SET OMIP 本身是二次授权命令，形成串行链：二次授权→改网元信息→重对接网管 | 网管失联 | warning | EV-CA-02 §5.6/§7.3 |
| `CR-ND-14` | 自动部署模板不可变 | delete_constraint | explicit | ops | object | ADD/RMV AUTOSCALING* | 自动部署完成后无法自动修改/删除已部署配置，需手动：关开关→删子接口→改模板→重开开关 | 配置无法在线变更 | warning | EV-CA-02 §7.7 |
| `CR-ND-15` | IPv6 双栈地址族双配 | parameter_dependency | explicit | config | parameter | ADD VPNINSTAF:AFTYPE + ADD OSPF/ADD OSPFV3 | IPv4v6 双栈：VPN 两个地址族(ipv4uni+ipv6uni)都要配；OSPF 与 OSPFv3 分别配；逻辑接口 IPVERSION=IPVER_ALL；APN 的 HASVPN 与 HASVPNIPV6 都 ENABLE | 双栈路由不全 | warning | EV-CA-02 §4.4 |
| `CR-ND-16` | IP 网段隔离 | semantic_rule | explicit | principle | relation | ADD LOGICINF:IPV4ADDRESS1 vs ExternalInterface/对端物理口 | 逻辑接口 IP 不能与外联口 IP 同网段，也不能与对端物理接口 IP 同网段 | 路由冲突 | critical | EV-CA-02 §3.1/§7.1 |
| `CR-ND-17` | UPINFO 全网唯一 | validation_rule | explicit | config | parameter | SET UPINFO:HOSTNAME | HOSTNAME 全网唯一，不配则 N4 偶联失败 | N4 偶联失败 | critical | EV-CA-02 §6.1 |
| `CR-ND-18` | 地址池 LOCAL/EXTERNAL 范围 | restriction_rule | explicit | config | object | ADD POOL:POOLTYPE | LOCAL（UDG 主锚点分配 IP）需完整三件套；EXTERNAL（辅锚点/ULCL/外部 NF 分配）仅 POOL+SECTION，可选 CHECKIPVALID | 地址分配异常 | warning | EV-CA-02 §3.4 |

---

## 6. MMLCommand `operates_on` ConfigObject 边表（核心映射）

> **Schema 参考**：§11.7 `MMLCommand operates_on ConfigObject`。列出核心命令与配置对象的操作关系。

| MMLCommand | operates_on → ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD VPNINST (ADDVPNINST) | VPNInstance | 业务/信令面 VPN 实例 |
| ADD L3VPNINST (ADDL3VPNINST) | L3VPNInstance | 路由侧 L3VPN 实例 |
| ADD VPNINSTAF (ADDVPNINSTAF) | VPNAddressFamily | VPN 地址族 |
| ADD VPNTARGET (ADDVPNTARGET) | VPNTarget | VPN RT |
| ADD LOGICINF (ADDLOGICINF) | LogicInterface / N4Interface / PaInterface / SaInterface / ScInterface | 业务逻辑接口（含 4 类抽象） |
| SET UPINFO (SETUPINFO) | UPFIdentity | UPF 标识 |
| ADD SNSSAIUPINTF (ADDSNSSAIUPINTF) | SNSSAIBinding | 切片绑定 |
| ADD APN (ADDAPN) | APN | APN/DNN 实例 |
| ADD POOL (ADDPOOL) | AddressPool | 地址池 |
| ADD SECTION (ADDSECTION) | AddressSection | 地址段 |
| ADD POOLGROUP (ADDPOOLGROUP) | PoolGroup | 地址池组 |
| ADD POOLBINDGROUP (ADDPOOLBINDGROUP) | PoolBinding | 地址池绑定 |
| ADD POOLGRPMAP (ADDPOOLGRPMAP) | PoolGroupMap | APN↔POOLGROUP 映射 |
| SET IPALLOCRULE (SETIPALLOCRULE) | IPAllocRule | 地址分配规则 |
| ADD OSPF (ADDOSPF) | OSPFProcess | OSPF 进程 |
| ADD OSPFAREA (ADDOSPFAREA) | OSPFArea | OSPF 区域 |
| ADD OSPFINTERFACE (ADDOSPFINTERFACE) | OSPFInterface | OSPF 接口 |
| SET BGP (SETBGP) | BGPInstance | BGP 全局 |
| ADD BGPVRF (ADDBGPVRF) | BGPVRF | BGP VPN 实例 |
| ADD BGPVRFAF (ADDBGPVRFAF) | BGPAddressFamily | BGP 地址族 |
| ADD BGPPEER (ADDBGPPEER) | BGPPeer | BGP 对等体 |
| ADD SRROUTE (ADDSRROUTE) | StaticRoute | 静态路由 |
| SET BFD (SETBFD) | BFDSession(全局使能) | BFD 全局 |
| ADD BFDSESSION (ADDBFDSESSION) | BFDSession | BFD 会话 |
| ADD GRETUNNEL (ADDGRETUNNEL) | GRETunnel | GRE 隧道 |
| SET MPLSSITE (SETMPLSSITE) | MPLSGlobal | MPLS 全局 |
| ADD MPLSIF (ADD/MPLSIF) | MPLSInterface | MPLS 接口 |
| ADD NPDIRECTCONNECTPORT (ADDNPDIRECTCONNECTPORT) | NPCascadePort | NP 级联口 |
| SET DATAPLANEGIINFMODE | DataPlaneGiInfMode | 入不转板 GI 模式 |
| SET DATAPLANEINFMODE | DataPlaneInfMode | 入不转板数据面模式 |
| SET DHCP6CLIENTDUID | DHCPv6ClientDUID | SDN DHCPv6 DUID |
| SET AUTOCONFIG (SETAUTOCONFIG) | AutoConfigSwitch | 自动配置开关 |
| ADD AUTOSCALINGSERVICE (ADDAUTOSCALINGSERVICE) | AutoScalingService | 外联口主模板 |
| ADD AUTOSCALINGETHTRUNK | AutoScalingEthTrunk | bonding Eth-trunk 模板 |
| ADD AUTOSCALINGBFD | AutoScalingBFD | BFD 模板 |
| ADD AUTOSCALINGSRBFD | AutoScalingSRBFD | 静态路由 BFD 模板 |
| ADD AUTOSCALINGSRROUTE | AutoScalingSRRoute | 静态路由模板 |
| ADD AUTOSCALINGBGPLF | AutoScalingBGPLF | BGP 入不转板模板 |
| ADD AUTOSCALINGIPREACH | AutoScalingIPReach | RU 可达性模板 |
| ADD AUTOSCALINGMPLS | AutoScalingMPLS | MPLS 自动化模板 |
| MOD ME (MODME) | NetworkElement | 网元身份 |
| SET OMIP (SETOMIP) | OMIP | 浮动/物理 IP |
| SET SECAUTH + ADD USRSECAUTH + ADD SECAUTHMEM | SecurityAuth | 二次授权 |
| SET NTP (SETNTP) | NTPSource | NTP 时间源 |
| SET FABRICMTU + MOD INTERFACE | MTUConfig | MTU 三层 |
| SET NEWCERTSWITCH | (证书更新开关) | LiteCA 前置 |
| 公共参数 11 项 SET 命令 | GlobalParameter | 11 项公共参数 |

> 上表列出约 47 条核心映射。完整映射由命令语法隐含（ADD X 操作 ConfigObject X）。

---

## 7. 与计费场景命令图谱的差异

| 维度 | 计费场景 | 网元对接场景（本文件） |
|------|---------|----------------------|
| 场景性质 | 业务配置类（计费能力配置） | 对接类（开局组网对接） |
| MMLCommand 数量 | 87（UDG 41 + UNC 46） | 103（按6类组织，单产品 UDG） |
| ConfigObject 数量 | 55 | 58 |
| CommandRule 数量 | 14 | 18 |
| 独有命令族 | URR 三件套、在线计费(DIAMCONNGRP/DCCTEMPLATE)、融合计费18步链、CG 接口 | 接口配置(VPNINST/LOGICINF/UPINFO)、会话接入三件套(APN/POOL 五件套)、路由协议(OSPF/BGP/静态)、自动部署模板族(AUTOSCALING 8种)、网管对接(OMIP/SECAUTH/二次授权)、BFD/GRE/MPLS/IPsec 隧道 |
| 核心约束差异 | URRID 唯一、RG 跨侧一致、三件套绑定完整 | N4 必备性、VPN 四统一、强制合一抽象接口、SDN 四强制、自动部署开关时序、MPLS 公私分离、网管密码三元组 |
| 共享对象 | — | VPNInstance、LogicInterface、APN、AddressPool（与未来会话类场景潜在共享） |

---

## 8. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| MMLCommand | 103 | 接口7 + 会话接入8 + 网管基础18 + 路由22 + BFD/隧道11 + 自动部署11 + 验证26 |
| CommandParameter | ~50（关键命令） | P-LOGICINF/VPNINST/OSPF/BGPPEER/APN/IPALLOCRULE/BFD/ASS 系列 |
| ConfigObject | 58 | OBJ-ND-001~058（接口8 + 会话7 + 路由12 + BFD/隧道9 + 自动部署9 + 网管9 + License/MTU4） |
| CommandRule | 18 | CR-ND-01~CR-ND-18 |
| ConfigObject 关系边 | 25 | contains/refers_to/depends_on/conflicts_with/composed_by/activates |
| MMLCommand operates_on 边 | ~47 | 核心映射 |
| **命令层对象总计** | **~211** | — |

---

## 9. 禁止关系合规声明（Schema §13）

本文件严格遵守 §13 禁止关系：

- **未建立** `ConfigurationSolution -> ConfigObject` 直连（CS→对象由 Task 层承接，见 03-task-layer.md `invokes`）
- **未建立** `ConfigurationSolution -> MMLCommand` 直连（CS→命令由 ConfigTask `invokes` 承接）
- **未建立** `BusinessRule -> CommandParameter` 直接写死参数值（BR 影响通过 DecisionPoint + CommandRule 表达，如 CR-ND-05 SDN 四强制）
- **未建立** `Feature -> MMLCommand` 直接强绑定（Feature 经 ConfigTask 落命令，第2层特性图谱不直接持命令实例）
- **未建立** `Feature -> ConfigObject` 携带参数差异（差异由 SemanticObject + DecisionPoint variant_dimensions 表达）
- **CommandRule `governs` MMLCommand/CommandParameter/ConfigObject**（§11.7 正向；反向 MMLCommand `governed_by` CommandRule），命令不跳层

---

> 本文件为网元对接三层图谱第4层。第5层跨层映射、第6层证据索引见同目录其他文件。命令引用以 `command_name`（如 `ADD VPNINST`）为主要标识，03-task-layer.md 与 05-mapping-layer.md 据此引用。
