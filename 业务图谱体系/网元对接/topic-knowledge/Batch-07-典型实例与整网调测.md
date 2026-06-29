# Batch-07: 典型配置实例 + 整网调测

> 批次07 | 端到端证据+调测 | 文件数8 | 核心度★★★★
> 路径前缀：`output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/`
> 这是主题轨最后一批：7个典型配置实例是各组网模式组合的完整开局模板（Stage4端到端链路验证的关键证据），整网调测是FirstCall打通验证流程。

---

## 1. 概述

### 1.1 7个典型配置实例覆盖的组网模式组合

本批 7 个端到端配置实例系统覆盖了 **路由协议 × IP版本 × 自动/手动部署 × SDN/非SDN × UDG角色** 五维矩阵的全部主路径：

| # | 实例 | UDG角色 | 路由协议 | IP版本 | 部署方式 | 场景 | 接入用户 |
|---|------|---------|---------|--------|---------|------|---------|
| 1 | 基于OSPF路由自动部署融合UDG（IPv4） | **融合** | OSPF | IPv4 | 自动(非SDN) | 2/3/4/5G融合 | IPv4单栈 |
| 2 | 基于OSPFv3路由自动部署锚点UDG（IPv6） | **锚点** | OSPFv3 | IPv6 | 自动(非SDN) | 2/3/4/5G融合 | IPv4v6双栈 |
| 3 | 基于静态路由手动部署边缘UDG（IPv4） | **边缘** | 静态路由 | IPv4 | 手动(非SDN) | 2/3/4/5G融合 | IPv4单栈 |
| 4 | 基于BGP over OSPFv3路由手动部署边缘UDG（IPv6） | **边缘** | BGP over OSPFv3 | IPv6 | 手动(非SDN) | 2/3/4/5G融合 | IPv4v6双栈 |
| 5 | 基于BGP over 静态路由配置实例（SDN+IPv4） | **PGW-U/UPF** | BGP over 静态路由 | IPv4 | 自动(SDN) | SDN+融合 | IPv4单栈 |
| 6 | 基于BGP over 静态路由配置实例（SDN+IPv6） | **PGW-U/UPF** | BGP over 静态路由 | IPv6 | 自动(SDN) | SDN+融合 | IPv6单栈 |
| 7 | 基于BGP over 静态路由配置实例（SDN+IPv4v6） | **PGW-U/UPF** | BGP over 静态路由 | IPv4v6 | 自动(SDN) | SDN+融合 | IPv4v6双栈 |

**覆盖维度说明**：
- **UDG角色**：融合(1) / 锚点(1) / 边缘(2) / PGW-U-UPF(3=SDN场景统一形态)
- **路由协议**：OSPF/OSPFv3 动态路由(2) / 静态路由(1) / BGP over OSPFv3(1) / BGP over 静态路由(3)
- **IP版本**：IPv4(2) / IPv6(2) / IPv4v6双栈(3)
- **部署方式**：自动部署(4=非SDN 2 + SDN 2... 实为非SDN自动2+SDN自动3=5) / 手动部署(2)
- **场景**：非SDN(4) / SDN(3)

### 1.2 调测目标：FirstCall 打通验证

整网调测文档（KP-08）定义了初始配置完成后的端到端验证流程，核心目标：
1. **路由调测**：验证 UDG 经每个 ISU 到对端网元的 IP 路由可达 + 负荷分担
2. **接口连通性**：验证直连路由器到 UDG 逻辑接口 IP 的回程路由
3. **FirstCall 打通**：测试终端通过 APN 接入网络，建立用户上下文，访问 Internet 数据业务

---

## 2. 核心知识点

### KP-01: 实例1 — 基于OSPF路由自动部署融合UDG配置实例（IPv4）

- **来源**：`典型配置实例/基于OSPF路由自动部署融合UDG配置实例（IPv4）_70196672.md`
- **核心度**：★★★★（融合网元 + OSPF自动部署的标杆实例）
- **网络形态/角色**：2/3/4/5G融合网络 / **UDG融合网元**（融合 I-UPF 和 PSA UPF，对不同组网用户承担不同角色）
- **组网组合**：OSPF动态路由 × IPv4组网 × 自动部署(非SDN) × IPv4单栈用户
- **对接对象**：gNodeB/eNodeB、ULCL/BP/I-UPF/SGW-U/ePDG、SGSN、PSA UPF/PGW-U、SMF/PGW-C/SGW-C、DN/PDN
- **配置流程概要**（10步）：
  1. **关闭自动配置开关**：`LST AUTOCONFIG` → `DSP OPSASSISTSTATE`(确保Ready) → `SET AUTOCONFIG:SWITCHFLAG=FALSE`
  2. **全局激活BFD**：`SET BFD:BFDENABLE=TRUE`
  3. **(R)AN侧路由**：VPN实例 `VPN_Access` + OSPF进程6/区域0.0.0.5 + 外联口自动部署模板(ETHTRUNKTMPID=1, VNICLIST="4 5")
  4. **核心侧UPF路由**：VPN实例 `VPN_Sc` + OSPF进程7/区域0.0.0.6
  5. **接入侧UPF路由**：VPN实例 `VPN_Pa` + OSPF进程8/区域0.0.0.7 + ETHTRUNKTMPID=2(VNICLIST="6 7")
  6. **DN/PDN路由**：VPN实例 `VPN_Internet` + OSPF进程9/区域0.0.0.8
  7. **控制面路由**：VPN实例 `VPN_Signaling` + OSPF进程10/区域0.0.0.9 + ETHTRUNKTMPID=3(VNICLIST="8 9")
  8. **打开自动配置开关**：`SET AUTOCONFIG:SWITCHFLAG=TRUE`（⚠️打开后有时延，需 `DSP OPSASSISTSTATE` 查 Ready）
  9. **配置逻辑接口**：Sa/N3/S1-U(VPN_Access) + Sc/N9c(VPN_Sc) + Pa(VPN_Pa) + N4(VPN_Signaling) + `SET UPINFO:HOSTNAME`
  10. **配置会话接入**：APN/DNN实例 + 地址池(POOL/SECTION/POOLGROUP/POOLBINDGROUP/POOLGRPMAP) + `SET IPALLOCRULE`
- **关键配置块**：每对接面一个 VPN 实例 + 独立 OSPF 进程（进程6~10对应5个对接面）；外联口自动部署模板 `ADD AUTOSCALINGSERVICE`（USER_CONFIG地址段+OSPFENABLE=TRUE）；以太网隧道多虚拟网卡模板 `ADD AUTOSCALINGETHTRUNK`
- **涉及对接面**：CS-1(N4控制面) + CS-2(Sa/Sc/Pa用户面) + CS-4(OSPF路由对接) 全覆盖
- **关联特性**：IPFD-014000(IPv4路由), IPFD-014002(OSPF), GWFD-010105(N4接口)
- **关联命令**：SET AUTOCONFIG, DSP OPSASSISTSTATE, SET BFD, ADD L3VPNINST, ADD OSPF, ADD OSPFAREA, ADD OSPFIMPORTROUTE, ADD AUTOSCALINGETHTRUNK, ADD AUTOSCALINGSERVICE, ADD LOGICINF, ADD APN, ADD POOL/SECTION/GROUP, SET IPALLOCRULE, SET UPINFO

### KP-02: 实例2 — 基于OSPFv3路由自动部署锚点UDG配置实例（IPv6）

- **来源**：`典型配置实例/基于OSPFv3路由自动部署锚点UDG配置实例（IPv6）_70196674.md`
- **核心度**：★★★★（锚点网元 + IPv6 + 双栈用户的标杆实例）
- **网络形态/角色**：2/3/4/5G融合网络 / **锚点UDG**（仅做独立锚点网关，**不包含融合边缘网关形态，与(R)AN无连接**）
- **组网组合**：OSPFv3动态路由 × IPv6组网 × 自动部署(非SDN) × **IPv4v6双栈用户**
- **对接对象**：ULCL/BP/I-UPF/SGW-U/ePDG、SGSN、SMF/PGW-C/SGW-C、DN/PDN（**无gNodeB/eNodeB**，锚点不接无线侧）
- **配置流程概要**（9步）：
  1. 关闭自动配置开关
  2. 全局激活BFD
  3. **接入侧UPF路由**：VPN_Pa + OSPFv3进程8/区域0.0.0.7（IPv6）+ ETHTRUNKTMPID=2
  4. **DN/PDN的IPv4路由**：VPN_Internet_IPv4 + OSPF进程9/区域0.0.0.8（IPv4）
  5. **DN/PDN的IPv6路由**：VPN_Internet_IPv6 + OSPFv3进程90/区域0.0.0.2（IPv6）★双栈用户DN侧需拆双VPN实例
  6. **控制面路由**：VPN_Signaling + OSPFv3进程10/区域0.0.0.9 + ETHTRUNKTMPID=3
  7. 打开自动配置开关
  8. 配置逻辑接口：Pa(IPv6) + N4(IPv6) + SET UPINFO（**无Sa/Sc接口**，锚点不接无线/核心侧UPF的N3/N9c）
  9. 配置会话接入：APN/DNN(HASVPNIPV6=ENABLE) + IPv6前缀地址池(V6PREFIXSTART/END/LENGTH=64)
- **关键差异点（vs 实例1）**：
  - 锚点无(R)AN连接 → 无 VPN_Access/Sa接口；无核心侧UPF的 VPN_Sc/Sc接口
  - **双栈用户接入**：Gi/SGi/N6接口vNIC外联口需规划IPv4v6双栈地址 → DN侧拆分为 VPN_Internet_IPv4 (OSPF) + VPN_Internet_IPv6 (OSPFv3) **两个独立VPN实例**
  - IPv6用 `ADD OSPFV3` + `ROUTERID`（IPv4格式的router-id）+ `ADD IFIPV6ADDRESS` + `IPV6PREFIXLEN`
- **涉及对接面**：CS-1(N4) + CS-2(Pa用户面) + CS-4(OSPFv3路由)
- **关联特性**：IPFD-014001(IPv6路由), IPFD-014003(OSPFv3), GWFD-010105
- **关联命令**：ADD OSPFV3, ADD OSPFV3AREA, ADD OSPFV3IMPORTROUTE, ADD IFIPV6ADDRESS, ADD APN(HASVPNIPV6)

### KP-03: 实例3 — 基于静态路由手动部署边缘UDG配置实例（IPv4）

- **来源**：`典型配置实例/基于静态路由手动部署边缘UDG配置实例（IPv4）_70196678.md`
- **核心度**：★★★★（边缘网元 + 静态路由手动部署的标杆实例）
- **网络形态/角色**：2/3/4/5G融合网络 / **边缘UDG**
  - 本地分流场景：承担 ULCL/BP分流 + 本地PSA锚点网关（融合部署形态）
  - 普通场景：承担 I-UPF/S-GW，桥接用户到PSA锚点（独立网元形态）
- **组网组合**：静态路由 × IPv4组网 × **手动部署**(非SDN) × IPv4单栈用户
- **对接对象**：gNodeB/eNodeB、SGSN、PSA UPF/PGW-U、SMF/PGW-C/SGW-C、DN/PDN
- **配置流程概要**（7步，**无自动配置开关操作**）：
  1. **全局激活BFD**（手动部署无需关/开自动配置开关）
  2. **(R)AN侧路由**：VPN_Access + **手动配置外联口**(MOD INTERFACE→ADD INTERFACE Eth-trunk→MOD TRUNKIF Manual→ADD TRUNKMEMBER→ADD IPBINDVPN→ADD ETHSUBIF关联VLAN→ADD IFIPV4ADDRESS) + **新建BFD静态会话**(ADD BFDSESSION, SESS_STATIC, LOCALDISCR/REMOTEDISCR) + **静态路由绑定BFD**(ADD SRROUTE, SESSIONNAME)
  3. **核心侧UPF路由**：VPN_Sc + 同上手动外联口流程 + BFD会话 + 静态路由
  4. **控制面路由**：VPN_Signaling + 手动外联口 + BFD + 静态路由
  5. **DN/PDN路由**：VPN_Internet + 手动外联口 + BFD + 静态路由
  6. 配置逻辑接口：Sa/Sc/N4 + SET UPINFO
  7. 配置会话接入：APN/DNN + 地址池
- **关键差异点（vs 自动部署实例1）**：
  - **无自动配置开关操作**，无 AUTOSCALINGETHTRUNK/AUTOSCALINGSERVICE 模板
  - 外联口配置改为**完整手动链路**：主接口up → Eth-trunk(Manual模式) → 子接口 → 绑VPN → VLAN → IP
  - BFD改为 **ADD BFDSESSION 静态会话**（指定 LOCALDISCR/REMOTEDISCR/DESTADDR4/IFNAME）
  - 路由改为 **ADD SRROUTE**（显式 PREFIX/MASKLENGTH/NEXTHOP/IFNAME + SESSIONNAME 联动BFD）
  - 多路径负荷分担：到同一目的IP配置多条路由，下一跳分别是不同ISU的接口IP
- **涉及对接面**：CS-1(N4) + CS-2(Sa/Sc) + CS-4(静态路由+BFD)
- **关联特性**：IPFD-012003(静态路由), IPFD-014000(IPv4路由)
- **关联命令**：MOD INTERFACE, ADD INTERFACE, MOD TRUNKIF, ADD TRUNKMEMBER, ADD IPBINDVPN, ADD ETHSUBIF, ADD IFIPV4ADDRESS, ADD BFDSESSION, ADD SRROUTE

### KP-04: 实例4 — 基于BGP over OSPFv3路由手动部署边缘UDG配置实例（IPv6）

- **来源**：`典型配置实例/基于BGP over OSPFv3路由手动部署边缘UDG配置实例（IPv6）_70196679.md`
- **核心度**：★★★★（BGP over OSPFv3 + IPv6手动部署的标杆实例）
- **网络形态/角色**：2/3/4/5G融合网络 / **边缘UDG**（独立网元形态，承担I-UPF/S-GW桥接到PSA锚点）
- **组网组合**：**BGP over OSPFv3** × IPv6组网 × **手动部署**(非SDN) × IPv4v6双栈用户
- **对接对象**：gNodeB/eNodeB、SGSN、PSA UPF/PGW-U、SMF/PGW-C/SGW-C（不涉及外部DN网络连接，故IPv4v6双栈接入与其他IP类型无差异）
- **配置流程概要**（9步）：
  1. 全局激活BFD
  2. **(R)AN侧路由**：VPN_Access + 手动外联口(IPv6: SET IFIPV6ENABLE→ADD IFIPV6ADDRESS) + OSPFv3进程6/区域0.0.0.5 + OSPFv3接口属性(ADD OSPFV3INTERFACE)
  3. **核心侧UPF路由**：VPN_Sc + 手动外联口 + OSPFv3进程8/区域0.0.0.7
  4. **控制面路由**：VPN_Signaling + 手动外联口 + OSPFv3进程9/区域0.0.0.8
  5. **全局激活BGP**：`SET BGP:BGPENABLE=TRUE,ASNUM="60001"`
  6. **BGP Loopback接口**：3个Loopback接口分别绑 VPN_Access/VPN_Sc/VPN_Signaling + IPv6地址
  7. **配置BGP**：BGPVRF实例 + BGPVRFAF地址族(MAXIMUMLOADBALANCE=2对接2个负荷分担路由) + BGPPEER对等体(EBGPMAXHOP=10) + IMPORTROUTE引入wlr路由
  8. 配置逻辑接口：Sa/Pa/N4(IPv6) + SET UPINFO
  9. 配置会话接入：APN/DNN + IPv6地址池
- **关键差异点**：
  - **BGP over OSPFv3 双层路由**：底层OSPFv3打通Loopback到Peer的可达性，上层BGP在Loopback间建EBGP邻居(EBGPMAXHOP≥实际跳数)发布业务路由
  - BGP自身不能发现路由 → 必须 IMPORTROUTE 引入 wlr/OSPFv3 路由注入BGP
  - OSPFv3区域支持验证类型：ADD OSPFV3AREAAUTH(hmac-sha256等)
- **涉及对接面**：CS-1(N4) + CS-2(Sa/Pa) + CS-4(BGP over OSPFv3)
- **关联特性**：IPFD-014001(IPv6路由), IPFD-014003(OSPFv3), BGP相关
- **关联命令**：SET BGP, ADD OSPFV3/AREA/INTERFACE/IMPORTROUTE, ADD BGPVRF/VRFAF/PEER, ADD IMPORTROUTE, ADD IPBINDVPN(Loopback), ADD IFIPV6ADDRESS

### KP-05: 实例5 — 基于BGP over 静态路由配置实例（SDN+IPv4）

- **来源**：`典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv4）_80481423.md`
- **核心度**：★★★★（SDN场景 + BGP over 静态路由 IPv4 标杆实例）
- **网络形态/角色**：**SDN场景** + 2/3/4/5G融合网络 / **PGW-U/UPF**（SDN场景统一网元形态）
- **组网组合**：**BGP over 静态路由** + **BFD单臂echo** × IPv4组网 × **自动部署(SDN)** × IPv4单栈用户
- **对接对象**：gNodeB/eNodeB、ULCL/BP/I-UPF/SGW-U、SGSN、PSA UPF/PGW-U、SMF/PGW-C/SGW-C、DN/PDN
- **配置流程概要**（12步）：
  1. **配置基础数据**：修改网元名称、网元浮动IP（与组网无关）
  2. 激活全局BFD：`SET BFD:BFDENABLE=TRUE`
  3. 激活全局BGP：`SET BGP:BGPENABLE=TRUE,ASNUM="60001"`
  4. **关闭自动配置开关**：LST AUTOCONFIG→DSP OPSASSISTSTATE→SET AUTOCONFIG:SWITCHFLAG=FALSE
  5. **(R)AN侧路由**：VRF_Access + AUTOSCALINGETHTRUNK(VNICLIST="4 5") + AUTOSCALINGERVICE(**IPALLOCTYPE4=DHCP**) + **AUTOSCALINGBFD**(**ONEARMECHO=TRUE单臂**, DESTADDR4=Leaf节点IP) + **AUTOSCALINGSRROUTE**(NEXTHOPALLOCTYPE4=DHCP, 默认路由PREFERENCE=255低于对端发布路由) + Loopback1+BGPVRF+BGPVRFAF(MAXIMUMLOADBALANCE=2)+BGPPEER+IMPORTROUTE
  6~9. UPF/PGW-U(VRF_Sc)、ULCL UPF(VRF_Pa)、PDN/DN(VRF_Internet)、SMF(VRF_Signaling)路由 — 每个对接面重复步骤5的完整模板套件，仅VLANID(200/300/400/500)和Loopback IP递增
  10. **打开自动部署开关**：`SET AUTOCONFIG:SWITCHFLAG=TRUE`
  11. 配置逻辑接口：Sa/Sc/Pa/N4(IPv4)
  12. 配置会话接入：APN/DNN + 地址池
- **关键差异点（SDN场景 vs 非SDN）**：
  - **VPN命名前缀**：VRF_* （非SDN用 VPN_*）
  - **外联口IP分配方式**：`IPALLOCTYPE4=DHCP`（SDN由Leaf分配，非SDN用USER_CONFIG手工段）
  - **BFD模式**：**单臂echo**（ONEARMECHO=TRUE，DESTADDR=Leaf节点IP），非SDN用动态BFD(OSPF绑定)或静态双臂BFD
  - **静态路由用途**：仅打通 VNF BGP Loopback IP ↔ BGP PEER IP 的互通（不是发布业务路由）；含两条——32位主机路由(PREFERENCE=60) + 默认路由(PREFERENCE=255，默认路由优先级要低于对端发布路由)
  - **每对接面一套完整BGP模板**：Loopback + BGPVRF + BGPVRFAF + BGPPEER + IMPORTROUTE
- **涉及对接面**：CS-1(N4) + CS-2(Sa/Sc/Pa) + CS-4(BGP over 静态路由 SDN)
- **关联特性**：IPFD-012003(静态路由), BGP, SDN相关
- **关联命令**：SET BGP, ADD AUTOSCALINGETHTRUNK/SERVICE/**BFD**/**SRROUTE**(SDN专属), ADD BGPVRF/VRFAF/PEER, ADD IMPORTROUTE, ADD IFIPV4ADDRESS(Loopback)

### KP-06: 实例6 — 基于BGP over 静态路由配置实例（SDN+IPv6）

- **来源**：`典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv6）_80481424.md`
- **核心度**：★★★（SDN场景 IPv6 变体）
- **网络形态/角色**：SDN场景+融合 / PGW-U/UPF
- **组网组合**：BGP over 静态路由 + BFD单臂echo × **IPv6组网** × 自动部署(SDN) × **IPv6单栈用户**
- **关键差异点（vs 实例5 IPv4）**：
  - **新增步骤4**：DHCP分配IPv6地址时**必须**设置 `SET DHCP6CLIENTDUID:DUIDTYPE=MAC_PLUS_VLAN`
  - IPv6外联口自动部署模板新增 `ADDRMODE=NETWOKSEGMENT_MODE`
  - BFD/AUTOSCALINGSRROUTE 用 `DESTADDR6`/`PREFIX6`/`NEXTHOPALLOCTYPE6=DHCP`，默认路由 PREFIX6=`0:0:0:0:0:0:0:0`/MASKLENGTH=0
  - Loopback需 `SET IFIPV6ENABLE:ENABLEFLAG=TRUE` 后 `ADD IFIPV6ADDRESS`
  - BGPVRFAF AFTYPE=ipv6uni，BGPPEER ADDRESSTYPE=ipv6/PEERADDRV6
  - 地址池用 IPv6 前缀（V6PREFIXSTART/END/LENGTH=64）
- **涉及对接面**：同实例5（CS-1/CS-2/CS-4）
- **关联命令**：SET DHCP6CLIENTDUID(★SDN+IPv6必需), ADD IFIPV6ADDRESS, ADD AUTOSCALINGSERVICE(ADDRMODE=NETWOKSEGMENT_MODE)

### KP-07: 实例7 — 基于BGP over 静态路由配置实例（SDN+IPv4v6）

- **来源**：`典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv4v6）_80481422.md`
- **核心度**：★★★★（SDN场景双栈最完整实例，IPv4+IPv6并行配置）
- **网络形态/角色**：SDN场景+融合 / PGW-U/UPF
- **组网组合**：BGP over 静态路由 + BFD单臂echo × **IPv4v6双栈组网** × 自动部署(SDN) × **IPv4v6双栈用户**
- **关键差异点（vs 实例5/6）**：
  - 每个对接面的 VPN 实例 **同时启用 ipv4uni + ipv6uni 两个地址族**（ADD VPNINSTAF 两次）
  - 每个对接面配置 **IPv4 + IPv6 两套** AUTOSCALINGSERVICE/BFD/SRROUTE（VLANID相同，AFTYPE不同）
  - **每个 Loopback 同时配 IPv4 + IPv6 地址**（同一接口绑同一VRF，ADD IFIPV4ADDRESS + SET IFIPV6ENABLE + ADD IFIPV6ADDRESS）
  - BGPVRFAF/BGPPEER/IMPORTROUTE **每个VRF两套**（ipv4uni + ipv6uni）
  - 逻辑接口用 `IPVERSION=IPVER_ALL`（非IPV4/IPV6），同时填 IPV4ADDRESS1+IPV4MASK1 和 IPV6ADDRESS1+IPV6PREFIXLEN1
  - 会话接入 APN 同时 HASVPN=ENABLE + HASVPNIPV6=ENABLE，地址池 SECTION 配 IPv4段(SECTIONNUM=1) + IPv6段(SECTIONNUM=2)
  - SET DHCP6CLIENTDUID:DUIDTYPE=MAC_PLUS_VLAN（IPv6必需）
- **涉及对接面**：同实例5（CS-1/CS-2/CS-4）
- **关联命令**：IPVER_ALL(双栈逻辑接口), ADD VPNINSTAF×2, ADD BGPVRFAF×2

### KP-08: 整网调测与FirstCall验证

- **来源**：`整网调测_31373646.md`
- **核心度**：★★★★★（Stage4端到端链路验证的权威流程）
- **调测目标**：初始配置完成后，验证 (1) 能否打通 First Call (2) IP路由能否实现负荷分担
- **前提条件**：已完成初始配置 + 已加载License + 已完成gNodeB/AMF/SMF/PCF等所有网元配置
- **测试数据**：IMSI(460000123456789) + APN(apn-test，可通过 `LST APN` 查询)
- **调测流程**（4阶段29步）：

#### 阶段0：检查RU状态
- 步骤1：`DSP SERVICERUSTATE` 检查所有RU状态正常（异常→联系华为技术支持查软件安装）

#### 阶段1：调测 UDG 到对端的IP路由（UDG执行，验证每ISU可达+负荷分担）
- 步骤2：`NGPING` 检查UPF接口IP到周边网元可达
  - **必须配置源IP**(SOURCEIPV4/6) 或出接口(OBIFNAME)，目的IP是对端网元IP（非对接路由器接口IP）
  - 多ISU场景**逐个执行** NGPING 保证每ISU可用
  - 丢包率0%→路由OK；100%→按路由类型分支（静态→步骤3 / OSPF→步骤4 / BGP→步骤9）；非0非100%→网络拥塞联系华为
- 步骤3（静态路由异常）：`DSP SRROUTE` 检查IPv4静态路由 — 到同一目的IP多条路由开销相等 + 接口名不同 + 分布在不同ISU = 负荷分担正常
- 步骤4（OSPF异常）：`DSP OSPFROUTING` 检查OSPF路由 — 多ISU需存在多条到同一目的IP的OSPF路由
- 步骤5：`LST OSPF` 检查"OSPF共网段虚拟系统使能标志"=TRUE
- 步骤6：`LST OSPF` 检查"去使能VPN路由环路检测"=FALSE
- 步骤7：`LST OSPFAREA` 检查"区域类型"=NSSA
- 步骤8：NSSA场景检查Loopback接口配置（`LST INTERFACE`/`LST IPBINDVPN`/`LST OSPFINTERFACE`/`LST OSPFNETWORK`）— 设备自动选取Loopback地址作为FA，多路径等开销可负载分担
- 步骤9（BGP异常）：`LST BGPPEER` 查对等体配置 + `DSP BGPPEERINFO` 查状态=Established（条数与LST BGPPEER相等）
- 步骤11：PING 检查 UDG Loopback IP 与对等体IP可达

#### 阶段2：调测直连路由器到 UDG 的IP路由（路由器执行）
- 步骤12：PING 检查路由器到 UDG 逻辑接口IP可达（下一跳是UDG每个ISU的接口IP）
- 步骤13/14：路由器侧补静态路由 / 修正OSPF配置
- 步骤15：检查路由表 — 到UDG逻辑IP路由下一跳是每ISU接口IP，需多条路由

#### 阶段3：调测FirstCall
- 步骤16：`NGPING` 检查 UDG 逻辑接口IP与对端网元业务IP互通（源IP=UDG逻辑接口IP，目的IP=对端业务IP）
- 步骤17：`LST OSPFIMPORTROUTE` 检查OSPF引入wlr路由（协议分类=wlr）
- 步骤18：UNC产品上开启相关跟踪任务（联系UNC技术支持）
- 步骤19：PGW-U/UPF上创建 UDG N4接口跟踪任务/用户跟踪任务
- 步骤20：测试终端用 apn-test 接入网络（**基站同时支持4G/5G时需4G+5G终端同时拨测**）
  - 成功接入→步骤26；N4偶联建立失败→步骤21；PGW-U/UPF无资源→步骤23
  - 成功标志：`DSP SESSIONINFO` 查询用户上下文，**APN/Role Type/IPv4 PDP address/Session Activation Timestamp 参数值都正确**
  - Role Type取值：SGW-U / PGW-U / SPGW-U / UPF
- 步骤21-22：N4偶联失败 → `LST LOGICINF` 检查Pa接口 → 缺则补Pa逻辑接口配置
- 步骤23-25：UDG做主锚点时，确认是否需UDG给UE分配IP → 检查/补 UDG地址池配置(POOL/SECTION)
- 步骤26：用户访问Internet数据业务，观测业务正常 → 调测结束

#### 阶段4：联系华为技术支持（兜底）
- 步骤27-29：重新调测 + `EXP MML` 导出配置文件 + 联系华为技术支持

- **关键验证MML命令汇总**：
  | 命令 | 用途 | 阶段 |
  |------|------|------|
  | `DSP SERVICERUSTATE` | 检查所有RU状态正常 | 0 |
  | `NGPING` | UDG接口IP↔对端网元 / UDG逻辑接口IP↔对端业务IP | 1,3 |
  | `DSP SRROUTE` | 验证IPv4静态路由多条等开销负荷分担 | 1 |
  | `DSP OSPFROUTING` | 验证OSPF路由多ISU多路径 | 1 |
  | `LST OSPF` | 检查VPNINSCAPSIMFLG=TRUE / VPN路由环路检测=FALSE | 1 |
  | `LST OSPFAREA` | 检查区域类型=NSSA | 1 |
  | `LST OSPFINTERFACE`/`LST OSPFNETWORK` | 验证Loopback关联OSPF进程/区域 | 1 |
  | `LST BGPPEER` / `DSP BGPPEERINFO` | BGP对等体配置+状态=Established | 1 |
  | `LST OSPFIMPORTROUTE` | OSPF引入wlr路由（协议分类=wlr） | 3 |
  | `LST LOGICINF` | 检查Pa逻辑接口存在 | 3 |
  | `DSP SESSIONINFO` | ★FirstCall成功标志：APN/RoleType/IPv4 PDP/Session时间戳正确 | 3 |
  | `LST APN` | 查询已配置APN | 数据准备 |
  | `EXP MML` | 导出配置文件（兜底） | 4 |

- **关联对接面**：CS-1(N4偶联验证) + CS-2(逻辑接口连通) + CS-4(路由负荷分担验证)
- **关联特性**：全场景（端到端验证）

---

## 3. 关键发现

### 3.1 端到端开局流程共性（7实例共同的开局链路骨架）

所有7个典型实例都遵循同一个**5段式开局链路**，差异仅在每段内的具体配置命令：

```
[段1 全局预处理] → [段2 多对接面路由配置] → [段3 自动部署开关(自动部署类)] → [段4 业务逻辑接口] → [段5 会话接入]
```

- **段1 全局预处理**：BFD激活(`SET BFD:BFDENABLE=TRUE`)；SDN+BGP场景额外 `SET BGP:BGPENABLE=TRUE,ASNUM`；SDN+IPv6场景额外 `SET DHCP6CLIENTDUID:DUIDTYPE=MAC_PLUS_VLAN`
- **段2 多对接面路由**：按 (R)AN / 核心侧UPF / 接入侧UPF / DN-PDN / 控制面 5个对接面分别配置 VPN实例 + 路由协议 + 外联口（每个实例的5个VPN实例名固定：VPN_Access/VPN_Sc/VPN_Pa/VPN_Internet/VPN_Signaling，SDN用VRF_前缀）
- **段3 自动部署开关**：仅自动部署类（实例1/2/5/6/7）需 `SET AUTOCONFIG:SWITCHFLAG=FALSE`→配置→`TRUE`，开关切换前后必须 `DSP OPSASSISTSTATE` 确认 Ready 状态；手动部署类（实例3/4）无此段
- **段4 业务逻辑接口**：Sa/N3/S1-U + Sc/N9c + Pa + N4 四类逻辑接口绑对应VPN + `SET UPINFO:HOSTNAME`（锚点实例2无Sa/Sc）
- **段5 会话接入**：APN/DNN实例 + 地址池(POOL/SECTION/POOLGROUP/POOLBINDGROUP/POOLGRPMAP) + `SET IPALLOCRULE`

### 3.2 各实例关键差异矩阵

| 维度 | 实例1(融合/OSPF/v4) | 实例2(锚点/OSPFv3/v6) | 实例3(边缘/静态/v4) | 实例4(边缘/BGPoverOSPFv3/v6) | 实例5(SDN/BGPover静态/v4) | 实例6(SDN/v6) | 实例7(SDN/v4v6) |
|------|---------------------|----------------------|---------------------|------------------------------|---------------------------|---------------|-----------------|
| 自动配置开关 | ✓关→开 | ✓关→开 | ✗ | ✗ | ✓关→开 | ✓关→开 | ✓关→开 |
| 外联口部署 | AUTOSCALINGSERVICE(USER_CONFIG) | AUTOSCALINGSERVICE | 手动Eth-trunk链路 | 手动Eth-trunk链路 | AUTOSCALINGSERVICE(**DHCP**) | AUTOSCALINGSERVICE(DHCP) | AUTOSCALINGSERVICE(DHCP) |
| BFD模式 | 动态(OSPF绑定) | 动态(OSPFv3绑定) | **静态双臂**(LOCALDISCR/REMOTEDISCR) | 动态(OSPFv3绑定) | **单臂echo**(ONEARMECHO, Leaf IP) | 单臂echo | 单臂echo×2(v4+v6) |
| 路由协议命令 | ADD OSPF/AREA/IMPORTROUTE | ADD OSPFV3/AREA/IMPORTROUTE | ADD SRROUTE(SESSIONNAME绑定BFD) | ADD OSPFV3 + ADD BGPVRF/VRFAF/PEER/IMPORTROUTE | ADD AUTOSCALINGSRROUTE + ADD BGPVRF/VRFAF/PEER | 同5(IPv6变体) | 同5(v4+v6并行) |
| Loopback接口 | ✗ | ✗ | ✗ | ✓(3个,BGP邻居) | ✓(5个,每对接面1个) | ✓(5个) | ✓(5个,双栈) |
| 逻辑接口版本 | IPV4 | IPV6 | IPV4 | IPV6 | IPV4 | IPV6 | **IPVER_ALL** |
| 双栈特殊处理 | - | DN侧拆双VPN实例(IPv4+IPv6) | - | DN侧不涉及 | - | DHCP6CLIENTDUID | DHCP6CLIENTDUID+双AF×2套 |

### 3.3 FirstCall 验证要点

1. **多ISU逐个验证**：NGPING 必须逐ISU执行，保证每个 ISU 可达（负荷分担前提）
2. **丢包率三分支**：0%=路由OK / 100%=路由异常（按协议类型分支排查） / 非0非100%=网络拥塞（联系华为）
3. **NSSA区域需Loopback**：OSPF NSSA 区域必须配 Loopback 接口并引入OSPF进程，设备自动选 Loopback 作 FA 实现负载分担
4. **BGP必须引入外部路由**：BGP自身不能发现路由，必须 IMPORTROUTE 引入 wlr/OSPF/静态 路由注入BGP表
5. **默认路由优先级**：SDN场景静态路由默认路由 PREFERENCE=255，**必须低于**对端发布路由的优先级；对端发布默认路由时本侧不需配默认路由
6. **4G+5G同时拨测**：基站同时支持4G/5G时，需4G+5G终端同时拨测（在保持一制式业务前提下拨测另一制式）
7. **FirstCall成功标志**：`DSP SESSIONINFO` 查到 APN/RoleType/IPv4 PDP address/Session Activation Timestamp 4参数全部正确
8. **常见失败定位**：N4偶联失败→查Pa接口；PGW-U/UPF无资源→查UDG地址池配置

---

## 4. 端到端开局链路归纳（★供第3层Task编排和Stage4端到端链路验证）

### 4.1 完整开局流程（按对接面CS × 流程顺序）

```
CS-5 基础就绪
  └─ License加载 + NTP + 网元基本信息 + 高危命令二次授权 + 公共参数 + MTU
CS-3 网管对接
  └─ 配置网元和网管对接
CS-1 控制面(N4)
  └─ 配置N4(N4_Sxa_Sxb)接口数据 → VPN_Signaling 逻辑接口
CS-2 用户面
  ├─ 配置Sa/N3/S1-U接口 → VPN_Access
  ├─ 配置Sc/N9c/S5-S/S8-S接口 → VPN_Sc
  ├─ 配置Pa(N9a/S5-P/...)接口 → VPN_Pa
  ├─ 配置SGi/N6接口 → VPN_Internet
  ├─ 配置S11-U / Nupf 接口(按需)
  └─ 配置会话接入数据(APN/DNN/地址池)
CS-4 路由对接（★ 7实例的核心差异点）
  ├─ 自动部署(非SDN)：SET AUTOCONFIG:FALSE → 配置AUTOSCALING模板 → SET AUTOCONFIG:TRUE
  ├─ 手动部署(非SDN)：直接手动配置Eth-trunk/外联口/路由协议/BFD
  └─ SDN部署：SET AUTOCONFIG:FALSE → 配置AUTOSCALING+BGP模板 → SET AUTOCONFIG:TRUE
调测 FirstCall（KP-08）
  └─ DSP SERVICERUSTATE → NGPING(每ISU) → 路由验证 → 直连路由器PING → FirstCall拨测 → DSP SESSIONINFO
```

### 4.2 各典型实例对应的组网模式组合矩阵（路由×IP×部署×SDN × UDG角色）

| 实例 | 路由协议 | IP版本 | 部署 | SDN | UDG角色 | 典型适用场景 |
|------|---------|--------|------|-----|---------|------------|
| 1 | OSPF | IPv4 | 自动 | 非SDN | 融合 | 2/3/4/5G融合网络主流部署 |
| 2 | OSPFv3 | IPv6 | 自动 | 非SDN | 锚点 | IPv6网络独立锚点网关 |
| 3 | 静态路由 | IPv4 | 手动 | 非SDN | 边缘 | 本地分流/边缘桥接（无动态路由协议） |
| 4 | BGP over OSPFv3 | IPv6 | 手动 | 非SDN | 边缘 | 边缘网元需BGP路由发布场景 |
| 5 | BGP over 静态路由 | IPv4 | 自动 | **SDN** | PGW-U/UPF | SDN数据中心IPv4接入 |
| 6 | BGP over 静态路由 | IPv6 | 自动 | **SDN** | PGW-U/UPF | SDN数据中心IPv6接入 |
| 7 | BGP over 静态路由 | IPv4v6 | 自动 | **SDN** | PGW-U/UPF | SDN数据中心双栈接入（最完整） |

### 4.3 Stage4端到端链路验证清单（来自KP-08）

按以下顺序执行验证，任一阶段失败即按 KP-08 流程分支定位：

1. **RU就绪**：`DSP SERVICERUSTATE` 全部正常
2. **UDG→对端路由可达**：`NGPING`（每ISU逐个）丢包率0%
3. **路由负荷分担**：`DSP SRROUTE`/`DSP OSPFROUTING`/`LST BGPPEER`+`DSP BGPPEERINFO`(=Established) 验证多路径等开销
4. **直连路由器→UDG回程**：路由器PING UDG逻辑接口IP可达 + 路由表多条
5. **UDG逻辑接口→对端业务IP**：`NGPING`（源=逻辑接口IP）丢包率0%
6. **路由引入正确**：`LST OSPFIMPORTROUTE` 协议分类=wlr
7. **FirstCall拨测**：测试终端apn-test接入 → `DSP SESSIONINFO` APN/RoleType/IPv4 PDP/Session时间戳4参数正确
8. **数据业务验证**：用户访问Internet数据业务正常

---

## 附录：文件清单与核心度

| # | 文件 | 核心度 | KP |
|---|------|--------|-----|
| 1 | 典型配置实例/基于OSPF路由自动部署融合UDG配置实例（IPv4）_70196672.md | ★★★★ | KP-01 |
| 2 | 典型配置实例/基于OSPFv3路由自动部署锚点UDG配置实例（IPv6）_70196674.md | ★★★★ | KP-02 |
| 3 | 典型配置实例/基于静态路由手动部署边缘UDG配置实例（IPv4）_70196678.md | ★★★★ | KP-03 |
| 4 | 典型配置实例/基于BGP over OSPFv3路由手动部署边缘UDG配置实例（IPv6）_70196679.md | ★★★★ | KP-04 |
| 5 | 典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv4）_80481423.md | ★★★★ | KP-05 |
| 6 | 典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv6）_80481424.md | ★★★ | KP-06 |
| 7 | 典型配置实例/基于BGP over 静态路由配置实例（SDN+IPv4v6）_80481422.md | ★★★★ | KP-07 |
| 8 | 整网调测_31373646.md | ★★★★★ | KP-08 |
