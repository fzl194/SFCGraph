# Batch-04: CS-4路由对接 — 总览 + 非SDN无NP卡(自动部署)
> 批次04 | 对接面CS-4 | 文件数14 | 核心度★★★★★
> Stage4命令层核心输入 | 6种路由方案 + IPsec + GRE + MPLS VPN
> 关联特性: IPFD-014000路由功能 / IPFD-014001 OSPF / IPFD-014002 BGP / IPFD-014003 静态路由 / IPFD-012003 BFD / GWFD-020411 MPLS VPN / IPFD-015004 IPsec

---

## 1. 概述

CS-4路由对接是UPF网元对接**最大、最核心**的对接面，负责打通VNF（UDG扮演UPF/PGW-U/SGW-U）与运营商网络（IP骨干网）的网络层互通路径。

### 1.1 路由对接总览（来源：组网路由配置_75096802.md）

VNF与运营商网络互通组网中，**一条对外网络路径上每个节点的IP类型必须一致**，且**绑定的VPN实例要一致**。不同逻辑接口的对外通信路径独立。

| 项目 | IPv4 | IPv6 | IPv4v6双栈 | VPN实例 | VLAN ID |
|------|------|------|-----------|---------|---------|
| 业务逻辑接口 | IPv4 | IPv6 | 双栈 | 一致 | - |
| 外联口（子接口，推荐） | IPv4 | IPv6 | 双栈 | 一致 | - |
| 外联口（主接口） | IPv4 | IPv6 | 双栈 | 一致 | 一致 |
| 网关侧业务端口 | IPv4 | IPv6 | 双栈 | 一致 | 一致 |

**特殊接口说明：**
- **OM操作维护接口**：支持IPv4/IPv6/双栈（独立规划，不绑定业务VPN）
- **Gi/SGi/N6接口（外部DN连接）**：使用CSLB上vNIC外联口，组网IP类型与**接入的用户IP类型相关**（双栈用户→双栈组网，单栈用户→单栈组网）

### 1.2 网关侧路由要求（来源：配置网关侧IP路由数据_75096770.md）

VNF对端网关推荐采用：**运营商PE交换机 / DC-GW网关 / EOR交换机**（三种型号配置要求相同）。

| 配置项 | 要求 |
|--------|------|
| IP路由格式（IPv4/IPv6/双栈） | 与VNF一致 |
| IP路由类型（OSPFv3/OSPF/静态/BGP） | 与VNF一致 |
| 探测机制（BFD） | 与VNF一致 |
| VLAN | 与VNF外联口VLAN一致 |
| VPN实例 | 与VNF逻辑接口、外联口绑定VPN一致 |
| VLANIF端口及IP | 为VNF外联口配置下一跳VLANIF端口 |
| 路由信息 | 目的=VNF逻辑接口地址，下一跳=VNF外联口地址 |

### 1.3 非SDN组网架构与路由原则（来源：非SDN组网介绍_58930406.md）

**非SDN**：相对于SDN，业务网络互通需手动配置。业务网元通过VNFM部署。包含三种架构：

| 架构 | 组网（业务） | DC-GW角色 | pod间流量 |
|------|------------|-----------|-----------|
| 三层架构 | TOR+EOR+DC-GW | L3GW | 不经DC-GW |
| 二层架构 | TOR+DC-GW | L3GW | 不经DC-GW |
| 一层/二层架构 | DC-GW（或TOR+DC-GW） | L3GW+L2GW | 经DC-GW绕转 |

**三层/二层架构（DC-GW作L3GW）路由原则：**
- 路由类型：支持OSPF/OSPFv3、静态路由、BGP over OSPF/OSPFv3、BGP over静态路由
- BFD：支持双向BFD探测 + BFD Echo（单臂探测）
- 外联口IP分配：采用 **USER_CONFIG** 方式（本端配置地址取值范围，动态分配）

**二层/一层架构（DC-GW作L3GW+L2GW）路由原则：**
- 路由类型：**只支持静态路由、BGP over静态路由**（OSPF会产生环路，禁用）
- BFD：使用 **BFD echo（单臂BFD）** 与静态路由联动

**BGP over静态路由标准4步模式（Loopback IP互通建立eBGP邻居）：**
1. 静态路由实现VNF Loopback IP 与 DC-GW Loopback IP 互通
2. DC-GW配置到VNF Loopback IP静态路由，下一跳为各IPU/ISU虚拟机vNIC IP（多VM时配置等价路由）
3. VNF配置到DC-GW Loopback IP静态路由，下一跳为DC-GW接口IP
4. Loopback三层互通后，基于Loopback IP建立eBGP邻居，学习和发布业务路由

### 1.4 自动部署 vs 手动部署（来源：配置VNF侧IP路由数据（无NP卡_非SDN）_16653295.md + 自动部署（推荐）_16653305.md）

**推荐自动部署**：系统根据预先设置的模板（IP地址段、目的IP、路由下一跳等），在新增RU/扩容时**自动生成**外联口IP地址、静态路由、绑定OSPF实例等配置，无需人工干预。新增外联口与已存在外联口共同承载流量形成负载分担。

| 对比项 | 手动部署 | 自动部署 |
|--------|---------|---------|
| 配置外联口物理IP | 3个vNIC需执行3×5=15次命令 | 创建1个模板=1次命令 |
| 配置BFD会话 | 3个vNIC需3次 | 1次模板 |
| 配置静态路由绑定BFD | 3条路由=3次 | 1次模板 |
| 系统扩容 | 需人工重复手动配置 | 自动完成，零人工 |

**自动部署适用与约束：**
- 适用场景：规划采用**子接口**对接的场景；只提供新建业务接口部署功能
- 部署完成后**无法自动修改/删除**已部署配置（需手动：关闭开关→删子接口→改模板→重开开关）
- **无NP卡或NP卡直连TOR场景**：支持自动+手动部署
- **NP卡直连PE场景**：不支持自动部署，必须手动
- 自动部署与手动部署冲突：手动配置IP后再自动部署，模板不生效；时延问题，须 `DSP OPSASSISTSTATE` 查询助手状态为 Ready 才可执行其他配置
- 地址池扩容：直接扩地址池可能IP冲突，需改造现有网段

### 1.5 6种路由方案 + 3种隧道概览

本批次涵盖**9种路由对接子方案**（非SDN无NP卡 + 自动部署）：

| # | 方案 | 适用 | 核心命令 |
|---|------|------|---------|
| 1 | OSPF+BFD（IPv4） | 复杂网络动态路由 | ADD OSPF / ADD OSPFAREA / ADD AUTOSCALINGSERVICE(OSPFENABLE=TRUE) |
| 2 | 静态路由+BFD（IPv4） | 简单网络 | ADD AUTOSCALINGSRROUTE + ADD AUTOSCALINGSRBFD/BFD |
| 3 | BGP over OSPF/静态+BFD（IPv4） | 跨AS复杂网络 | OSPF/静态 + SET BGP + ADD BGPVRF/BGPPEER/IMPORTROUTE |
| 4 | OSPFv3+BFD（IPv6） | IPv6动态路由 | ADD OSPFV3 / ADD OSPFV3AREA |
| 5 | 静态路由+BFD（IPv6） | IPv6简单网络 | 同方案2替换IPVERSION=IPv6 |
| 6 | BGP over OSPFv3/静态+BFD（IPv6） | IPv6跨AS | 同方案3替换IPVERSION=IPv6 |
| 7 | IPsec | 跨安全域加密 | 详见IPFD-015004 |
| 8 | GRE隧道（PGW-U/UPF与PDN/DN） | WAP接入VPN | ADD GRETUNNEL / ADD SRROUTE(IFNAME=Tunnel) |
| 9 | BGP/MPLS VPN（OptionB跨域） | UDG作PE对接企业网 | SET MPLSSITE + MP-EBGP + ADD VPNTARGET |

---

## 2. 核心知识点

### KP-01: 自动部署模板体系与开关机制
- **内容**：自动部署核心是"模板化+开关驱动"。配置流程：①关闭自动配置开关（`SET AUTOCONFIG:SWITCHFLAG=FALSE`）②配置各类自动部署模板（外联口/ETHTRUNK/BFD/静态路由/MPLS）③打开开关（`SWITCHFLAG=TRUE`）触发系统按模板自动生成实例配置。
  - **模板族（按路由方案组合）**：
    - `ADD AUTOSCALINGETHTRUNK`：SR-IOV bonding场景的Eth-trunk模板（VNICLIST两个MAC相同且ID连续）
    - `ADD AUTOSCALINGSERVICE`：★外联口自动部署主模板（服务名/VPN/地址族/地址池/VLAN/接口类型/路由使能）
    - `ADD AUTOSCALINGSRBFD`：静态路由的动态BFD模板（双向检测）
    - `ADD AUTOSCALINGBFD`：BFD会话模板（单臂echo检测）
    - `ADD AUTOSCALINGSRROUTE`：静态路由模板（前缀/掩码/下一跳/BFD绑定）
    - `ADD AUTOSCALINGBGPLF`：BGP入不转板策略模板（路由增强）
    - `ADD AUTOSCALINGIPREACH`：RU可达性检测模板
    - `ADD AUTOSCALINGMPLS`：MPLS接口自动化模板
  - **`ADD AUTOSCALINGSERVICE`关键参数**（OSPF方案）：
    - SERVICENAME（双平面示例：ServName_Access_100/200）、VPNNAME、AFTYPE（IPv4/IPv6）
    - IPALLOCTYPE4/6=USER_CONFIG（固定）、AUTOCFGIFTYPE=VNIC（非bonding）/ETHTRUNK（bonding）
    - VNICID、ETHTRUNKTMPID、VLANID、BEGINADDR4/6、ENDADDR4/6、MASKLEN（IPv4典型25，IPv6典型121）
    - OSPFENABLE=TRUE、OSPFPROCID、OSPFAREAID（OSPF方案必配）
    - TPINENABLE/TPOUTENABLE（流量策略使能，典型FALSE）
  - **IPv4v6双栈**：对同一外联口分别执行命令配置IPv4和IPv6地址
- **来源**：自动部署（推荐）_16653305.md
- **核心度**：★★★★★
- **关联特性**：IPFD-014000（路由功能总称）
- **关联命令**：SET AUTOCONFIG / LST AUTOCONFIG / DSP OPSASSISTSTATE / ADD/RMV/LST/MOD AUTOSCALINGSERVICE / AUTOSCALINGETHTRUNK / AUTOSCALINGBFD / AUTOSCALINGSRBFD / AUTOSCALINGSRROUTE / AUTOSCALINGBGPLF / AUTOSCALINGIPREACH / AUTOSCALINGMPLS
- **配置对象**：自动部署主模板（服务）+ 各专项模板（外联口/BFD/路由/MPLS）+ 自动配置全局开关

---

### KP-02: OSPF+BFD组网（IPv4）— 完整MML序列
- **内容**：动态路由OSPF+BFD是复杂网络推荐方案。完整命令序列：
  ```mml
  // 1. 配置外联口VPN实例（一条通信路径所有节点VPN必须一致）
  ADD L3VPNINST:VRFNAME="VPN_Access";
  ADD VPNINSTAF:VRFNAME="VPN_Access",AFTYPE=ipv4uni;

  // 2. 全局激活BFD
  SET BFD:BFDENABLE=TRUE;

  // 3. 配置OSPF路由
  // 3a. 创建OSPF进程（含BFD参数）
  ADD OSPF:PROCID=6,VRFNAME="VPN_Access",SCHEMAROUID="192.168.35.210",
       BFDALLINTFFLG=TRUE, BFDRXCFGFLAG=TRUE,BFDMINRXINTV=500,
       BFDTXCFGFLAG=TRUE, BFDMINTXINTV=500, SCHEMABFDDETMUL=4,
       LSAARRINTVFLAG=FALSE, LSAARRMAXINTV=1000, LSAARRSTARINTV=500,
       LSAARRHLDINTV=500, VPNINSCAPSIMFLG=TRUE, VIRTUALSYSFLAG=TRUE;
  // 关键说明：
  //   - VPNINSCAPSIMFLG=TRUE：VPN多实例需取消环路检查，否则OSPF引入失败
  //   - VIRTUALSYSFLAG=TRUE：OSPF共网段时必须配置
  //   - BFDALLINTFFLG=TRUE：使能BFD会话

  // 3b. 增加OSPF区域
  ADD OSPFAREA:PROCID=6, AREAID="0.0.0.5", AREATYPE=NSSA, MAXCOSTFLAG=FALSE;

  // 3c. 设置OSPF引入路由类型
  ADD OSPFIMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr,
       IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;

  // 4. NSSA区域需配置Loopback接口（用于自动选FA，负载分担）
  ADD INTERFACE:IFNAME="LoopBack605";
  ADD IPBINDVPN:IFNAME="LoopBack605",VRFNAME="VPN_Access";
  ADD IFIPV4ADDRESS:IFNAME="LoopBack605",IFIPADDR="192.168.235.130",
       SUBNETMASK="255.255.255.255",ADDRTYPE=main;
  // 使能Loopback到OSPF区域（推荐ADD OSPFINTERFACE，或ADD OSPFNETWORK反掩码0.0.0.0）
  ADD OSPFINTERFACE:PROCID=6, AREAID="0.0.0.5", IFNAME="LoopBack605";

  // 5. 关闭自动配置开关
  LST AUTOCONFIG:;
  // （可选）DSP OPSASSISTSTATE:; 确认autoscaling_autoconfig.py为Ready
  SET AUTOCONFIG:SWITCHFLAG=FALSE;

  // 6. SR-IOV bonding组网时（可选）：ADD AUTOSCALINGETHTRUNK:ETHTRUNKTMPID=1,VNICLIST="4 5";

  // 7. 配置外联口自动部署模板（双平面示例）
  // 非SR-IOV bonding:
  ADD AUTOSCALINGSERVICE:SERVICENAME="ServName_Access_100",VPNNAME="VPN_Access",
       AFTYPE=IPv4,IPALLOCTYPE4=USER_CONFIG,AUTOCFGIFTYPE=VNIC,VNICID=4,
       VLANID=100, BEGINADDR4="192.168.89.2", ENDADDR4="192.168.89.126", MASKLEN=25,
       OSPFENABLE=TRUE, OSPFPROCID=6, OSPFAREAID="0.0.0.5",
       TPINENABLE=FALSE, TPOUTENABLE=FALSE;
  ADD AUTOSCALINGSERVICE:SERVICENAME="ServName_Access_200",VPNNAME="VPN_Access",
       AFTYPE=IPv4,IPALLOCTYPE4=USER_CONFIG,AUTOCFGIFTYPE=VNIC,VNICID=5,
       VLANID=200, BEGINADDR4="192.168.89.130", ENDADDR4="192.168.89.254", MASKLEN=25,
       OSPFENABLE=TRUE, OSPFPROCID=6, OSPFAREAID="0.0.0.5",
       TPINENABLE=FALSE, TPOUTENABLE=FALSE;
  // SR-IOV bonding: AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=1（去掉VNICID）

  // 8. 打开自动配置开关
  SET AUTOCONFIG:SWITCHFLAG=TRUE;
  // 务必 DSP OPSASSISTSTATE:; 确认Ready才执行其他操作
  ```
  **验证命令**：LST INTERFACE / LST IFIPV4ADDRESS / LST IPBINDVPN / DSP OSPFINTERFACE / DSP OSPFPEER / DSP BFDSESSION / PING
- **来源**：配置动态路由OSPF+BFD组网（IPv4）_16653306.md
- **核心度**：★★★★★
- **关联特性**：IPFD-014001 OSPF / IPFD-012003 BFD / IPFD-014000 路由
- **关联命令**：ADD L3VPNINST / ADD VPNINSTAF / SET BFD / ADD OSPF / ADD OSPFAREA / ADD OSPFIMPORTROUTE / ADD INTERFACE / ADD IPBINDVPN / ADD IFIPV4ADDRESS / ADD OSPFINTERFACE / ADD OSPFNETWORK / ADD AUTOSCALINGETHTRUNK / ADD AUTOSCALINGSERVICE / SET AUTOCONFIG
- **配置对象**：VPN实例 / OSPF进程 / OSPF区域（NSSA） / Loopback接口 / 外联口自动部署模板
- **必配参数**：VRFNAME / AFTYPE=ipv4uni / PROCID / SCHEMAROUID / AREAID / AREATYPE / PROTOCOL=wlr / SERVICENAME / VNICID / VLANID / 地址池起止+掩码 / OSPFPROCID / OSPFAREAID

---

### KP-03: 静态路由+BFD组网（IPv4）— 双向 vs 单臂echo
- **内容**：简单网络推荐。命令序列：
  ```mml
  // 1-2. VPN实例 + 全局BFD（同OSPF方案）
  ADD L3VPNINST:VRFNAME="VPN_Access";
  ADD VPNINSTAF:VRFNAME="VPN_Access",AFTYPE=ipv4uni;
  SET BFD:BFDENABLE=TRUE;

  // 3. 关闭自动配置开关
  LST AUTOCONFIG:; SET AUTOCONFIG:SWITCHFLAG=FALSE;

  // 4. （可选）SR-IOV bonding: ADD AUTOSCALINGETHTRUNK:ETHTRUNKTMPID=1,VNICLIST="4 5";

  // 5. 外联口自动部署模板（注意：静态路由方案无OSPFENABLE/OSPFPROCID/OSPFAREAID参数）
  ADD AUTOSCALINGSERVICE:SERVICENAME="ServName_Access_100",VPNNAME="VPN_Access",
       AFTYPE=IPv4,IPALLOCTYPE4=USER_CONFIG,AUTOCFGIFTYPE=VNIC,VNICID=4,
       VLANID=100, BEGINADDR4="192.168.89.2", ENDADDR4="192.168.89.126", MASKLEN=25;

  // 6. BFD双向检测：静态路由动态BFD模板
  ADD AUTOSCALINGSRBFD:SERVICENAME="ServName_Access_100", IPVERSION=IPv4,
       MINRXINTERVAL=500, MINTXINTERVAL=500, MULTIPLIER=4;

  // 7. BFD单臂echo检测：BFD会话模板（DESTADDR4是网关接口IP）
  ADD AUTOSCALINGBFD:TEMPLATENAME="BFD_1", BFDTYPE=Static,
       SERVICENAME="ServName_Access_100", IPVERSION=IPv4,
       DESTADDR4="192.168.89.1", MINECHORXINT=500, DETECTMULTI=4, ONEARMECHO=TRUE;

  // 8. 静态路由模板（BFD双向检测时）
  ADD AUTOSCALINGSRROUTE:SERVICENAME="ServName_Access_100", VRFNAME="VPN_Access",
       IPVERSION=IPv4, PREFIX4="192.168.53.4", MASKLENGTH=32,
       NEXTHOPALLOCTYPE4=CONFIG, NEXTHOP4="192.168.89.1",
       BFDENABLE=TRUE, DESCRIPTION="VPN_Access_ROUTE1";
  // BFD单臂echo时增加 BFDTEMPLATENAME="BFD_1"

  // 9. 打开开关 + 网关侧配置回程路由（目的=VNF逻辑接口IP，下一跳=外联口IP）
  SET AUTOCONFIG:SWITCHFLAG=TRUE;
  ```
  **关键差异（双向 vs 单臂echo）**：
  - 双向：用 `ADD AUTOSCALINGSRBFD`，SRROUTE不绑BFDTEMPLATENAME
  - 单臂echo：用 `ADD AUTOSCALINGBFD`（ONEARMECHO=TRUE），SRROUTE绑定BFDTEMPLATENAME
  - **下一跳规划**：SR-IOV bonding单平面双主网关需2个同网段下一跳；M-LAG组网1个；双平面2个不同网段下一跳
- **来源**：配置静态路由+BFD组网（IPv4）_16653303.md
- **核心度**：★★★★★
- **关联特性**：IPFD-014003 静态路由 / IPFD-012003 BFD
- **关联命令**：ADD L3VPNINST / ADD VPNINSTAF / SET BFD / ADD AUTOSCALINGSERVICE / ADD AUTOSCALINGSRBFD（双向）/ ADD AUTOSCALINGBFD（单臂echo）/ ADD AUTOSCALINGSRROUTE
- **配置对象**：VPN实例 / 外联口模板 / BFD模板（双向/单臂） / 静态路由模板
- **必配参数**：PREFIX4（目的IP，N3报文为基站IP）/ MASKLENGTH（典型32）/ NEXTHOP4（网关接口IP）/ BFDENABLE=TRUE

---

### KP-04: BGP over OSPF/静态+BFD（IPv4）— 入不转板扩展
- **内容**：BGP用于AS间路由控制，自身不能发现路由，需引入OSPF/静态路由。BGP本身无自动部署，依赖IGP自动部署基础。
  ```mml
  // 1. 先完成OSPF+BFD或静态路由+BFD（见KP-02/KP-03）
  //    BFD会话绑定的是路由不是BGPPEER；若有ADD BGPPEERBFD需删除
  //    静态路由方案需配两类路由：
  //      IP路由1: 目的=BGP对等体地址, 下一跳=网关接口IP, 绑BFD
  //      IP路由2: 目的=0.0.0.0/0, 其他同IP路由1（对端不发布默认路由时）

  // 2. 配置BGP专用Loopback接口（与IGP外联口同VPN）
  ADD INTERFACE:IFNAME="Loopback1";
  ADD IPBINDVPN:IFNAME="Loopback1",VRFNAME="VPN_Access";
  ADD IFIPV4ADDRESS:IFNAME="Loopback1",IFIPADDR="10.90.7.160",SUBNETMASK="255.255.255.255";

  // 3. 全局激活BGP
  SET BGP:BGPENABLE=TRUE, ASNUM="60001";

  // 4. 配置BGP
  // 4a. BGP VPN实例（ROUTERID是实例级，不同实例不能重复）
  ADD BGPVRF:VRFNAME="VPN_Access", DEFAULTAFTYPE=noaf, ROUTERID="10.90.7.160";
  // 4b. BGP VPN地址族（MAXIMUMLOADBALANCE=对接的负荷分担BGP PEER数）
  ADD BGPVRFAF:VRFNAME="VPN_Access", AFTYPE=ipv4uni, MAXIMUMLOADBALANCE=2;
  // 4c. BGP对等体（PEERADDR是DC-GW上建立BGP邻居的IP）
  ADD BGPPEER:VRFNAME="VPN_Access", ADDRESSTYPE=ipv4, PEERADDR="10.9.7.135",
       REMOTEAS="60002", LOCALIFADDR="10.90.7.160", LOCALIFNAME="Loopback1", EBGPMAXHOP=10;
  // 4d. BGP引入路由（BGP不能自己发现路由）
  ADD IMPORTROUTE:VRFNAME="VPN_Access", AFTYPE=ipv4uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;
  //   - N6口两UPF UE地址段重叠且需发网段路由时MEDENABLE=TRUE，备UPF的MED>主UPF

  // 5/6. 可选：入不转板（仅特定场景）
  ```
  **入不转板（路由增强）两种场景命令差异**：
  | 场景 | 开关命令 | 适用接口 |
  |------|---------|---------|
  | U面下沉（高密度框式+标卡+UPF分配IP+BGP over静态） | `SET DATAPLANEGIINFMODE:MODE=RU,ROUTEENHANCEDSW=ENABLE` | 仅N6/SGi |
  | 中心云（第三方底层+ISU POD+标卡+UPF分配IP+BGP over静态） | `SET DATAPLANEINFMODE:MODE=Instance,ROUTEENHANCEDSW=ENABLE` | s1-uif/n3if/saif/s5-sif/n9cif/scif/paif |

  入不转板配套命令（关闭自动开关后执行）：
  ```mml
  MOD AUTOSCALINGSERVICE:SERVICENAME="...", ISBACKUP=TRUE;  // 仅中心云场景
  MOD BGPPEERAF:VRFNAME=..., AFTYPE=ipv4uni, REMOTEADDRESS=..., ADVERTISECOMMUNITY=TRUE;
  ADD AUTOSCALINGBGPLF:POLICYNAME="bgppolicy1", IPVERSION=IPv4, SERVICENAME="...",
       PEERIP="10.9.7.135", PEERCOMMUNITY=1, UDADVCOMENABLE=TRUE, UDADVCOM="200";
  ADD AUTOSCALINGIPREACH:SERVICENAME="...", IPVERSION=IPv4,
       DESTADDR4="10.9.7.135", BFDTEMPLATENAME="BFD_1";
  ```
  **警告**：`SET DATAPLANEGIINFMODE`（下行入不转板）与 `SET DATAPLANEINFMODE`（入不转板总开关）易混淆，用错会触发 ALM-81210 告警。
- **来源**：配置BGP over OSPF_静态路由+BFD（IPv4）_16653311.md
- **核心度**：★★★★★
- **关联特性**：IPFD-014002 BGP / IPFD-014001 OSPF / IPFD-014003 静态路由
- **关联命令**：SET BGP / ADD BGPVRF / ADD BGPVRFAF / ADD BGPPEER / ADD IMPORTROUTE / SET DATAPLANEGIINFMODE / SET DATAPLANEINFMODE / MOD BGPPEERAF / ADD AUTOSCALINGBGPLF / ADD AUTOSCALINGIPREACH / MOD AUTOSCALINGSERVICE / LST BGPPEER / DSP BGPPEERINFO
- **配置对象**：BGP全局 / BGP VPN实例 / BGP地址族 / BGP对等体 / BGP引入路由 / 入不转板策略
- **对端设备**：DC-GW（双活网关/M-LAG只支持BGP over静态+BFD单臂echo，不支持OSPF）

---

### KP-05: OSPFv3+BFD组网（IPv6）
- **内容**：IPv6场景的OSPF动态路由。命令结构与IPv4 OSPF镜像，差异点：
  - VPN地址族：`ADD VPNINSTAF:AFTYPE=ipv6uni`
  - 进程命令：`ADD OSPFV3`（替代ADD OSPF），参数ROUTERID替代SCHEMAROUID，DETECTMULINTV替代SCHEMABFDDETMUL
  - 区域命令：`ADD OSPFV3AREA`（NSSA/Normal都不需配置Loopback，与IPv4 NSSA不同）
  - 引入路由：`ADD OSPFV3IMPORTROUTE`
  - 外联口模板：`AFTYPE=IPv6`、`BEGINADDR6/ENDADDR6`（FC00::1002等）、`MASKLEN=121`
  ```mml
  ADD L3VPNINST:VRFNAME="VPN_Access";
  ADD VPNINSTAF:VRFNAME="VPN_Access",AFTYPE=ipv6uni;
  SET BFD:BFDENABLE=TRUE;
  ADD OSPFV3:PROCID=6,VRFNAME="VPN_Access",ROUTERID="10.8.25.1",
       BFDALLINTFFLG=TRUE,BFDRXCFGFLAG=TRUE,BFDMINRXINTV=500,
       BFDTXCFGFLAG=TRUE, BFDMINTXINTV=500,DETECTMULINTV=4,
       VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
  ADD OSPFV3AREA:PROCID=6,AREAID="0.0.0.5", AREATYPE=NSSA, NSSADEFAULTROUTEADVERTISE=FALSE;
  ADD OSPFV3IMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr,
       IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;
  // 关开关 → 外联口模板(AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG, BEGINADDR6/ENDADDR6) → 开开关
  ```
- **来源**：配置动态路由OSPFv3+BFD组网（IPv6）_16653296.md
- **核心度**：★★★★
- **关联特性**：IPFD-014001 OSPF（IPv6版） / IPFD-012003 BFD
- **关联命令**：ADD OSPFV3 / ADD OSPFV3AREA / ADD OSPFV3IMPORTROUTE / ADD AUTOSCALINGSERVICE（AFTYPE=IPv6）
- **配置对象**：VPN实例（ipv6uni）/ OSPFv3进程 / OSPFv3区域 / 外联口IPv6模板

---

### KP-06: 静态路由+BFD组网（IPv6）
- **内容**：IPv6简单网络。与IPv4静态方案差异：IPVERSION=IPv6，地址用BEGINADDR6/ENDADDR6（FC00::），掩码MASKLEN=128，PREFIX6/NEXTHOP6，IPALLOCTYPE6。
  ```mml
  // 双向BFD：
  ADD AUTOSCALINGSRBFD:SERVICENAME="...", IPVERSION=IPv6,
       MINRXINTERVAL=500, MINTXINTERVAL=500, MULTIPLIER=4;
  // 单臂echo：
  ADD AUTOSCALINGBFD:TEMPLATENAME="BFD_1", BFDTYPE=Static, SERVICENAME="...",
       IPVERSION=IPv6, DESTADDR6="FC00::1001", MINECHORXINT=500, DETECTMULTI=4, ONEARMECHO=TRUE;
  // 静态路由：
  ADD AUTOSCALINGSRROUTE:SERVICENAME="...", VRFNAME="VPN_Access", IPVERSION=IPv6,
       PREFIX6="FC00::2001:4", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG,
       NEXTHOP6="FC00::1001", BFDENABLE=TRUE, DESCRIPTION="...";
  ```
- **来源**：配置静态路由+BFD组网（IPv6）_16653298.md
- **核心度**：★★★★
- **关联特性**：IPFD-014003 静态路由 / IPFD-012003 BFD
- **关联命令**：同KP-03替换IPVERSION=IPv6 + IPv6地址族参数
- **配置对象**：VPN实例（ipv6uni）/ IPv6外联口模板 / IPv6 BFD模板 / IPv6静态路由模板

---

### KP-07: BGP over OSPFv3/静态+BFD（IPv6）
- **内容**：IPv6跨AS方案。结构同IPv4 BGP，差异：
  - VPN地址族、BGP地址族、对等体地址类型、引入路由均用 ipv6uni / IPv6
  - Loopback接口需配置IPv6地址 `ADD IFIPV6ADDRESS`
  - MED用于N6口主备UPF网段路由发布（备>主）
- **来源**：配置BGP over OSPFv3_静态路由+BFD（IPv6）_16653308.md
- **核心度**：★★★★
- **关联特性**：IPFD-014002 BGP / IPFD-014001 OSPFv3 / IPFD-014003 静态路由
- **关联命令**：SET BGP / ADD BGPVRF / ADD BGPVRFAF(AFTYPE=ipv6uni) / ADD BGPPEER(ADDRESSTYPE=ipv6) / ADD IMPORTROUTE(AFTYPE=ipv6uni) / ADD IFIPV6ADDRESS
- **配置对象**：IPv6 BGP VPN实例 / IPv6 BGP地址族 / IPv6 BGP对等体

---

### KP-08: IPsec（跨安全域加密）
- **内容**：IPsec是IETF制定的IP层安全框架，提供数据加密、完整性保护、防重放攻击。建议场景：
  - **用户接入业务**：SGW-C/PGW-C/SmF 与 SGW-U/PGW-U/UPF 部署在不同区域时的 **Sxa/Sxb/N4接口信令报文**
  - **数据转发业务**：eNodeB/gNodeB 与 SGW-U/PGW-U/UPF 部署在不同区域时的 **S1-U/N3接口数据报文**
  - 详细配置参见 IPFD-015004 IPSec功能特性文档（本批次未展开MML）
- **来源**：配置IPsec_80591826.md
- **核心度**：★★★
- **关联特性**：IPFD-015004 IPsec
- **关联命令**：详见IPFD-015004特性文档
- **配置对象**：IPsec安全联盟 / 安全策略 / 加密认证参数

---

### KP-09: GRE隧道（PGW-U/UPF与PDN/DN之间）
- **内容**：用户通过WAP访问PDN/DN时，PGW-U/UPF与WAP网关建立GRE VPN。完整命令序列：
  ```mml
  // 前置：已完成BGP over OSPF/静态+BFD（IPv4）的外联口IP路由配置

  // 1. Loopback接口（与N6接口VPN一致）
  ADD INTERFACE:IFNAME="LoopBack1";
  ADD IPBINDVPN:IFNAME="LoopBack1",VRFNAME="VRF_Internet";
  ADD IFIPV4ADDRESS:IFNAME="LoopBack1", IFIPADDR="10.3.3.11",
       SUBNETMASK="255.255.255.255", ADDRTYPE=main;

  // 2. Loopback接口路由引入BGP（动态协议场景）
  ADD NETWORKROUTE:VRFNAME="VRF_Internet", AFTYPE=ipv4uni,
       NETWORKADDRESS="10.3.3.11", MASKLEN=32;

  // 3. 配置GRE Tunnel隧道
  ADD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, SRCTYPE=if_name,
       SRCIFNAME="LoopBack1", DSTIPADDR="10.4.4.11", DSTVPNNAME="VRF_Internet";
  ADD IPBINDVPN:IFNAME="Tunnel1", VRFNAME="VRF_Internet";
  ADD IFIPV4ADDRESS:IFNAME="Tunnel1", IFIPADDR="10.10.1.201",
       SUBNETMASK="255.255.255.0", ADDRTYPE=main;
  // MTU建议：MOD INTERFACE配置Tunnel MTU ≤ (出接口MTU - GRE头长度)

  // 4. 隧道间静态路由（出接口为Tunnel接口）
  ADD SRROUTE:AFTYPE=ipv4unicast, PREFIX="10.0.0.172", MASKLENGTH=32,
       VRFNAME="VRF_Internet", DESTVRFNAME="VRF_Internet",
       IFNAME="Tunnel1", PREFERENCE=60, BFDENABLE=FALSE, TAG=0, DHCPENABLE=FALSE;

  // 5. 可选：GRE校验（CHECKSUMEN=TRUE）
  MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, CHECKSUMEN=TRUE;
  // 6. 可选：识别关键字（GREKEYEN=TRUE, GREKEY两端必须相同）
  MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, GREKEYEN=TRUE, GREKEY="*****";
  // 7. Keepalive（默认周期5s，重试3次）
  MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre,
       KEEPALVEN=TRUE, KEEPALVPERIOD=5, KEEPALVRETRYCNT=3;
  ```
  **关键约束**：PGW-U/UPF与WAP网关必须支持Loopback接口建立GRE隧道；外联口用BGP/OSPF动态路由时，Loopback接口IP网段必须对外发布；用户上行数据用静态路由出接口为Tunnel接口。
- **来源**：配置PGW-U_UPF与PDN_DN之间的GRE隧道_84316409.md
- **核心度**：★★★
- **关联特性**：IPFD-014000（路由）/ GRE特性
- **关联命令**：ADD INTERFACE / ADD IPBINDVPN / ADD IFIPV4ADDRESS / ADD NETWORKROUTE / ADD GRETUNNEL / ADD SRROUTE / MOD GRETUNNEL / MOD INTERFACE / PING
- **配置对象**：Loopback接口 / Tunnel接口 / GRE隧道 / 静态路由（出接口Tunnel）
- **对端设备**：WAP网关

---

### KP-10: BGP/MPLS VPN（非SDN自动，OptionB跨域）
- **内容**：UDG作PE设备接入MPLS骨干网，通过MP-EBGP与其他PE传播VPN信息和VPN-IPv4路由，采用OptionB跨域VPN。UDG与DC-GW通过Loopback IP建eBGP邻居交换私网VPN路由，Loopback IP间通过静态路由/OSPF互通。
  **与非MPLS组网的关键差异**：
  - 外联口绑定VPN实例名固定为 `_public_`（不是业务VPN）
  - **不配置IPv6外联口数据**（MP-EBGP用IPv4 eBGP传递IPv6私网路由）
  - Loopback接口**不绑定VPN**（用公网BGP传私网路由）
  - 必须配置VRFRD（路由标识），不同VPN实例不能重复
  - 标签分配：VPN侧 `VRFLABELMODE=perInstance`，BGP侧 `APPLYLABELMODE=perNexthop`（配套节省标签）

  ```mml
  // 1-2. 全局激活BFD + BGP
  SET BFD:BFDENABLE=TRUE;
  SET BGP:BGPENABLE=TRUE, ASNUM="60001";

  // 3. MPLS全局（开启MPLS能力，不开启LDP）
  SET MPLSSITE:MPLSLSRID="10.10.10.78", MPLSENABLE=ENABLE, LDPENABLE=DISABLE;

  // 4. 关闭自动开关

  // 5. 外联口模板（VPNNAME=_public_，无IPv6）+ BFD单臂echo + 静态路由模板（含默认路由0.0.0.0/0 PREFERENCE=255）+ MPLS自动化模板

  // 6. 配置VPN实例及地址族（企业VPN，如VRF_PDN1~5）
  ADD L3VPNINST:VRFNAME="VRF_PDN1";
  ADD VPNINSTAF:VRFNAME="VRF_PDN1", AFTYPE=ipv4uni, VRFRD="100:100", VRFLABELMODE=perInstance;
  // IPv6/双栈增加 AFTYPE=ipv6uni

  // 7. VPN Target（Export/Import extcommunity）
  ADD VPNTARGET:VRFNAME="VRF_PDN1", AFTYPE=ipv4uni,
       VRFRTTYPE=export_extcommunity, VRFRTVALUE="1:1";
  ADD VPNTARGET:VRFNAME="VRF_PDN1", AFTYPE=ipv4uni,
       VRFRTTYPE=import_extcommunity, VRFRTVALUE="1:1";

  // 8. Loopback接口（不绑VPN，用于BGP邻居）
  ADD INTERFACE:IFNAME="Loopback1";
  ADD IFIPV4ADDRESS:IFNAME="Loopback1", IFIPADDR="10.10.10.78", SUBNETMASK="255.255.255.255";

  // 9. 公网BGP VPN实例ROUTERID
  MOD BGPVRF:VRFNAME="_public_", ROUTERID="10.1.1.1";

  // 10. 企业VPN的BGP VPN实例
  ADD BGPVRF:VRFNAME="VRF_PDN1", DEFAULTAFTYPE=noaf;

  // 11. ★MP-EBGP开关：公网BGP地址族 ipv4vpn/ipv6vpn
  ADD BGPVRFAF:VRFNAME="_public_", AFTYPE=ipv4vpn, APPLYLABELMODE=perNexthop;
  // 企业VPN的ipv4uni/ipv6uni地址族
  ADD BGPVRFAF:VRFNAME="VRF_PDN1", AFTYPE=ipv4uni, MAXIMUMLOADBALANCE=2;

  // 12. BGP对等体（VRFNAME=_public_，仅IPv4）
  ADD BGPPEER:VRFNAME="_public_", ADDRESSTYPE=ipv4, PEERADDR="10.10.20.78",
       REMOTEAS="60002", LOCALIFADDR="10.10.10.78", LOCALIFNAME="Loopback1", EBGPMAXHOP=10;
  ADD BGPPEERAF:VRFNAME="_public_", AFTYPE=ipv4vpn, REMOTEADDRESS="10.10.20.78";

  // 13. 引入wlr路由到企业VPN
  ADD IMPORTROUTE:VRFNAME="VRF_PDN1", AFTYPE=ipv4uni, IMPORTPROTOCOL=wlr;
  ```
  **VM扩容提示**：若用 `ADD AUTOSCALINGMPLS` 自动生成MPLS接口，扩容时自动添加新接口为MPLS接口；若用 `ADD MPLSIF` 手动添加，扩容时仍需手动添加新接口。
- **来源**：配置BGP_MPLS VPN（非SDN_自动）_20746526.md
- **核心度**：★★★★★
- **关联特性**：GWFD-020411 MPLS VPN / IPFD-014002 BGP / IPFD-012003 BFD
- **关联命令**：SET BFD / SET BGP / SET MPLSSITE / ADD AUTOSCALINGSERVICE(_public_) / ADD AUTOSCALINGBFD / ADD AUTOSCALINGSRROUTE / ADD AUTOSCALINGMPLS / ADD MPLSIF / ADD L3VPNINST / ADD VPNINSTAF(VRFRD/VRFLABELMODE) / ADD VPNTARGET / ADD INTERFACE / ADD IFIPV4ADDRESS / MOD BGPVRF / ADD BGPVRF / ADD BGPVRFAF(ipv4vpn=MP-EBGP开关) / ADD BGPPEER / ADD BGPPEERAF / ADD IMPORTROUTE
- **配置对象**：MPLS全局 / 公网BGP（MP-EBGP）/ 企业VPN实例 / VPN Target / Loopback（不绑VPN）/ MPLS接口

---

### KP-11: 网关侧IP路由数据（对端配置要求）
- **内容**：VNF对端网关（PE/DC-GW/EOR）配置要求（VNF侧配置的镜像）。详见§1.2概述表。
- **来源**：配置网关侧IP路由数据_75096770.md
- **核心度**：★★★
- **关联特性**：全部路由类特性
- **关联命令**：网关设备产品文档（非MML）
- **配置对象**：网关VLAN / VPN实例 / VLANIF端口 / BFD会话 / 路由信息（目的=VNF逻辑接口IP，下一跳=VNF外联口IP）

---

## 3. 关键发现

### 3.1 6种路由方案的共性结构（标准5层配置）
所有路由方案遵循统一的配置层次：
1. **VPN实例层**：`ADD L3VPNINST` + `ADD VPNINSTAF`（IPv4用ipv4uni，IPv6用ipv6uni）
2. **全局使能层**：`SET BFD:BFDENABLE=TRUE`；BGP方案加 `SET BGP`；MPLS方案加 `SET MPLSSITE`
3. **路由协议层**：
   - OSPF/OSPFv3：进程+区域+引入路由+（NSSA时）Loopback
   - 静态：静态路由模板+ BFD模板
   - BGP：VPN实例+地址族+对等体+引入路由（依赖IGP互通）
4. **外联口自动部署层**：`ADD AUTOSCALINGSERVICE`（OSPF方案带OSPFENABLE，静态方案不带）
5. **开关驱动层**：关→配模板→开，必须 `DSP OPSASSISTSTATE` 确认Ready

### 3.2 IPv4 vs IPv6 差异点
| 维度 | IPv4 | IPv6 |
|------|------|------|
| VPN地址族 | ipv4uni | ipv6uni |
| OSPF进程 | ADD OSPF (SCHEMAROUID) | ADD OSPFV3 (ROUTERID, DETECTMULINTV) |
| OSPF区域NSSA | 需配Loopback（自动选FA） | 不需配Loopback |
| 外联口模板 | AFTYPE=IPv4, BEGINADDR4/ENDADDR4, MASKLEN=25 | AFTYPE=IPv6, BEGINADDR6/ENDADDR6, MASKLEN=121 |
| 静态路由 | PREFIX4/NEXTHOP4, IPALLOCTYPE4 | PREFIX6/NEXTHOP6, IPALLOCTYPE6 |
| BGP对等体 | ADDRESSTYPE=ipv4 | ADDRESSTYPE=ipv6 |
| BGP地址族 | ipv4uni | ipv6uni |

### 3.3 OSPF vs 静态路由方案差异
| 维度 | OSPF+BFD | 静态路由+BFD |
|------|---------|------------|
| 适用网络 | 复杂网络、设备IP繁多 | 简单网络 |
| 外联口模板 | 带 OSPFENABLE/OSPFPROCID/OSPFAREAID | 不带OSPF参数 |
| BFD绑定 | OSPF进程级 BFDALLINTFFLG=TRUE | 路由级 BFDENABLE=TRUE + BFD模板 |
| NSSA区域 | 需配Loopback接口 | 无区域概念 |
| 二层/一层架构 | 禁用（产生环路） | 支持 |

### 3.4 BGP方案的依赖关系
- BGP**自身无自动部署**，依赖OSPF/静态路由的IGP自动部署基础
- BGP需要专用Loopback接口（与IGP外联口同VPN），用于建立eBGP邻居
- BGP引入路由IMPORTPROTOCOL典型为 `wlr`（无线路由）
- DC-GW双活网关/M-LAG场景**只支持BGP over静态+BFD单臂echo，不支持OSPF**

### 3.5 自动部署 vs 手动部署命令差异
| 操作 | 手动部署 | 自动部署 |
|------|---------|---------|
| 外联口IP | MOD INTERFACE + ADD INTERFACE + ADD IPBINDVPN + ADD ETHSUBIF + ADD IFIPV4ADDRESS (5命令×N次) | ADD AUTOSCALINGSERVICE (1次) |
| BFD会话 | ADD BFDSESSION (N次) | ADD AUTOSCALINGSRBFD / ADD AUTOSCALINGBFD (1次) |
| 静态路由 | ADD SRROUTE (N次) | ADD AUTOSCALINGSRROUTE (1次) |
| 扩容 | 重复全部手动步骤 | 自动完成 |

### 3.6 BGP/MPLS VPN独特性
- 外联口VPN固定 `_public_`，不配置IPv6外联口（用IPv4 eBGP传IPv6私网路由）
- Loopback接口**不绑VPN**
- 必须配置VRFRD，VPN Target（Export/Import extcommunity）
- MP-EBGP开关 = `ADD BGPVRFAF:VRFNAME="_public_", AFTYPE=ipv4vpn`
- 标签节省组合：VPN侧 perInstance + BGP侧 perNexthop

### 3.7 SR-IOV bonding场景共性
所有方案在SR-IOV bonding组网时需额外配置 `ADD AUTOSCALINGETHTRUNK`（VNICLIST两个MAC相同且ID连续的以太网接口），外联口模板的 `AUTOCFGIFTYPE=ETHTRUNK` + `ETHTRUNKTMPID`（去掉VNICID）。

---

## 4. 对接面与决策点归纳（★供第1层业务图谱）

### 4.1 CS-4路由对接方案要素
一个完整的CS-4路由对接闭包由以下要素组合决定：
- **VPN实例**：业务隔离（VPN_Access / VRF_Internet / VRF_PDNx / _public_）
- **路由协议**：OSPF / OSPFv3 / 静态 / BGP（依赖IGP）
- **BFD探测**：双向BFD / 单臂echo（BFD Echo）
- **外联口形态**：子接口（推荐）/ 主接口；SR-IOV bonding / 非bonding
- **IP版本**：IPv4 / IPv6 / IPv4v6双栈
- **隧道叠加**：无 / IPsec / GRE / MPLS VPN
- **部署方式**：自动部署（推荐）/ 手动部署

### 4.2 决策点DP矩阵

#### DP-1: 部署方式（自动 vs 手动）
- 自动部署：无NP卡或NP卡直连TOR（推荐）
- 手动部署：NP卡直连PE（必须）/ 自动部署失败补救

#### DP-2: 组网架构（DC-GW角色）
- 三层/二层（DC-GW作L3GW）：全路由类型支持
- 二层/一层（DC-GW作L3GW+L2GW）：仅静态/BGP over静态

#### DP-3: 路由协议 × IP版本（6种基础组合）
| | OSPF | 静态 | BGP over OSPF/静态 |
|---|------|------|---------------------|
| **IPv4** | ✓ KP-02 | ✓ KP-03 | ✓ KP-04 |
| **IPv6** | ✓ KP-05 (OSPFv3) | ✓ KP-06 | ✓ KP-07 |
| **双栈** | 分别配IPv4+IPv6 | 分别配IPv4+IPv6 | 分别配IPv4+IPv6 |

#### DP-4: 隧道叠加（按业务需求）
| 隧道 | 触发场景 | 关联接口 |
|------|---------|---------|
| IPsec | 跨安全域/跨区域信令或数据 | Sxa/Sxb/N4/S1-U/N3 |
| GRE | WAP访问PDN/DN | N6/SGi（PGW-U/UPF↔WAP网关） |
| MPLS VPN | UDG作PE对接企业网（OptionB跨域） | N6（外联口绑_public_） |

#### DP-5: 入不转板（BGP over静态的扩展）
- 下行入不转板（U面下沉）：`SET DATAPLANEGIINFMODE:MODE=RU`
- 入不转板总开关（中心云）：`SET DATAPLANEINFMODE:MODE=Instance`
- 仅特定接口 + 第三方底层转发性能低场景

### 4.3 路由方案→命令组合矩阵（★Stage4命令层核心输入）

| 方案 | 必备命令组合 | 配置对象数 |
|------|------------|-----------|
| OSPF+BFD(IPv4)自动 | L3VPNINST+VPNINSTAF / SET BFD / OSPF+OSPFAREA+OSPFIMPORTROUTE / (NSSA)INTERFACE+IPBINDVPN+IFIPV4ADDRESS+OSPFINTERFACE / AUTOSCALINGSERVICE | 6类 |
| 静态+BFD(IPv4)自动 | L3VPNINST+VPNINSTAF / SET BFD / AUTOSCALINGSERVICE / AUTOSCALINGSRBFD(双向)或AUTOSCALINGBFD(单臂) / AUTOSCALINGSRROUTE | 5类 |
| BGP over OSPF/静态(IPv4)自动 | 上游IGP全套 + INTERFACE+IPBINDVPN+IFIPV4ADDRESS(Loopback) / SET BGP / BGPVRF+BGPVRFAF+BGPPEER+IMPORTROUTE / (可选)DATAPLANExxxINFMODE+BGPPEERAF+AUTOSCALINGBGPLF+AUTOSCALINGIPREACH | 9~12类 |
| OSPFv3+BFD(IPv6)自动 | L3VPNINST+VPNINSTAF(ipv6uni) / SET BFD / OSPFV3+OSPFV3AREA+OSPFV3IMPORTROUTE / AUTOSCALINGSERVICE(IPv6) | 6类 |
| 静态+BFD(IPv6)自动 | L3VPNINST+VPNINSTAF(ipv6uni) / SET BFD / AUTOSCALINGSERVICE(IPv6) / AUTOSCALINGSRBFD或AUTOSCALINGBFD(IPv6) / AUTOSCALINGSRROUTE(IPv6) | 5类 |
| BGP over OSPFv3/静态(IPv6)自动 | 上游IPv6 IGP全套 + Loopback(IFIPV6ADDRESS) / SET BGP / BGPVRF+BGPVRFAF(ipv6uni)+BGPPEER(ipv6)+IMPORTROUTE(ipv6uni) | 9~12类 |
| IPsec | 详见IPFD-015004 | - |
| GRE隧道 | 前置BGP over路由 + Loopback+IPBINDVPN+IFIPV4ADDRESS / NETWORKROUTE / GRETUNNEL+IPBINDVPN+IFIPV4ADDRESS / SRROUTE(IFNAME=Tunnel) / MOD GRETUNNEL(CHECKSUM/KEY/Keepalive) | 5类 |
| BGP/MPLS VPN(OptionB)自动 | SET BFD+SET BGP+SET MPLSSITE / AUTOSCALINGSERVICE(_public_)+AUTOSCALINGBFD+AUTOSCALINGSRROUTE+AUTOSCALINGMPLS / L3VPNINST+VPNINSTAF(VRFRD/perInstance)+VPNTARGET / Loopback(不绑VPN) / MOD BGPVRF(_public_ ROUTERID)+BGPVRF(企业VPN)+BGPVRFAF(_public_ ipv4vpn=MP-EBGP开关 + 企业VPN ipv4uni)+BGPPEER(_public_)+BGPPEERAF+IMPORTROUTE | 10+类 |

### 4.4 公共配置块（跨方案复用）
1. **VPN实例块**：`ADD L3VPNINST` + `ADD VPNINSTAF`（每方案起始）
2. **全局使能块**：`SET BFD:BFDENABLE=TRUE`（除IPsec外所有方案）
3. **自动部署开关块**：`LST AUTOCONFIG` → `DSP OPSASSISTSTATE` → `SET AUTOCONFIG:SWITCHFLAG=FALSE` → 配模板 → `SWITCHFLAG=TRUE` → `DSP OPSASSISTSTATE`确认Ready
4. **外联口自动部署块**：`ADD AUTOSCALINGSERVICE`（含可选 `ADD AUTOSCALINGETHTRUNK` for SR-IOV bonding）
5. **验证块**：`LST INTERFACE` / `LST IFIPV4/V6ADDRESS` / `LST IPBINDVPN` / `PING` / 协议特定DSP命令

---

## 5. 文件清单与映射

| # | 文件 | 对应KP | 核心度 |
|---|------|--------|--------|
| 1 | 组网路由配置_75096802.md（总览） | §1.1 | ★★★★ |
| 2 | 配置网关侧IP路由数据_75096770.md | KP-11 / §1.2 | ★★★ |
| 3 | 配置VNF侧IP路由数据（无NP卡_非SDN）_16653295.md | §1.4 | ★★★ |
| 4 | 非SDN组网介绍_58930406.md | §1.3 | ★★★★ |
| 5 | 自动部署（推荐）_16653305.md | KP-01 / §1.4 | ★★★★★ |
| 6 | 配置动态路由OSPF+BFD组网（IPv4）_16653306.md | KP-02 | ★★★★★ |
| 7 | 配置静态路由+BFD组网（IPv4）_16653303.md | KP-03 | ★★★★★ |
| 8 | 配置BGP over OSPF_静态路由+BFD（IPv4）_16653311.md | KP-04 | ★★★★★ |
| 9 | 配置动态路由OSPFv3+BFD组网（IPv6）_16653296.md | KP-05 | ★★★★ |
| 10 | 配置静态路由+BFD组网（IPv6）_16653298.md | KP-06 | ★★★★ |
| 11 | 配置BGP over OSPFv3_静态路由+BFD（IPv6）_16653308.md | KP-07 | ★★★★ |
| 12 | 配置IPsec_80591826.md | KP-08 | ★★★ |
| 13 | 配置PGW-U_UPF与PDN_DN之间的GRE隧道_84316409.md | KP-09 | ★★★ |
| 14 | 配置BGP_MPLS VPN（非SDN_自动）_20746526.md | KP-10 | ★★★★★ |
