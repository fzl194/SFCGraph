# Batch-06: CS-4路由对接 — NP卡直连PE + SDN

> 批次06 | 对接面CS-4 | 文件数16 | 核心度★★★★
> 业务域=网元对接，子场景=UPF网元对接。CS-4路由对接=最大对接面。
> 本批覆盖剩余两个硬件/组网分支：**NP卡直连PE（加速省交换）** 与 **SDN组网**。
> 与 Batch-04(非SDN无NP卡自动部署)/Batch-05(非SDN手动+加速卡直连DC-GW) 构成 CS-4 路由对接全集。

---

## 1. 概述

### 1.1 NP卡直连PE（加速省交换）分支定位
- **适用场景**：部署UDG的服务器所有刀片均带NP卡，且U面下沉或中心云场景。
- **核心特征**：NP卡接口直连PE，**不支持自动部署**，须通过手动部署（与 Batch-04 自动部署路径的根本差异）。
- **npworkmode 关键参数**：NP卡接口直连PE时 `npworkmode` 必须为 `1`（默认即1，需核验）。Batch-05 直连DC-GW场景同理。
- **不支持SDN组网**（NP卡分支明确限制）。
- **来源**：`配置VNF侧IP路由数据（NP卡直连PE）_52117668.md`

### 1.2 SDN组网分支定位
- **适用场景**：数据中心引入SDN控制器+NFVO的Leaf-Spine架构，VNF外联口IP由DHCP动态获取、NFVO集中管理。
- **核心特征**：仅支持 **BGP over 静态路由+BFD**（IPv4/IPv6/IPv4v6）+ **BGP MPLS VPN**；**不支持OSPF与DC-GW的路由交互**。
- **与Batch-04自动部署共享 AUTOSCALING 命令族**（ADD AUTOSCALINGSERVICE/BFD/SRROUTE），但下一条跳/外联口IP分配方式强制 `DHCP`、BFD强制单臂Echo。
- **来源**：`配置VNF侧IP路由（SDN）_80548319.md`、`SDN组网介绍_58930596.md`

---

## 2. 核心知识点

### KP-01: NP卡直连PE — 外联口与刀片出线规划（硬件分支核心）
- **来源**：`配置VNF侧IP路由数据（NP卡直连PE）_52117668.md`
- **核心度**：★★★★★（NP卡分支特有）
- **关联特性**：硬件加速卡系列（与Batch-05加速卡直连DC-GW同族）
- **对接面**：CS-4路由对接
- **配置对象**：NP卡物理口（无独立MML，由组网/VNF实例化决定）

**核心要点**：
1. **成对刀片出线原则**：UDG部署在带NP卡服务器上时，需成对刀片的NP卡接口出线与PE互连，用于传输业务报文。
   - 2块刀片出线→最上面2块；4块出线→最上面4块；2N块出线→最上面2N块（N≤4）。
2. **两种网络加速卡型号 × 外联口命名差异**（关键决策点）：

| 型号 | 接口位置1（业务主口） | 接口位置3（级联口） | 速率规格 | Eth-trunk成员口跨刀片规则 |
|------|---------------------|--------------------|----------|--------------------------|
| **NP100** | `100GE X/0/9` | `100GE X/0/7` | 100GE | 不同刀片 |
| **NP121** | `400GE X/0/9`（自适200/100GE） | `200GE X/0/7` | 400GE/200GE | 不同刀片+相同刀片的不同NP卡 |

   - `X = 63 + Y`（Y = 从下往上数第几块刀片，例如第3块刀片 Y=3 → X=66）。
3. **PE对接对象**：奇数槽位接口对接PE1，偶数槽位接口对接PE2；使用不同Ethernet/Eth-trunk子接口传输 N3/N4/N9/N6 接口报文。
4. **SR-IOV bonding 组网**：奇数槽位刀片同位置接口组成1个Eth-trunk（负荷分担），偶数槽位同理。
5. **NP121 不支持作为标卡使用**（仅用于PE直连场景）。

---

### KP-02: NP卡直连PE — 修改级联口数据（NP100）★NP卡特有命令
- **来源**：`修改级联口数据（NP100）_90163990.md`
- **核心度**：★★★★★（NP卡多框级联独有，Batch-05同名章节为加速卡直连DC-GW版）
- **关联特性**：硬件加速卡 → 多框级联
- **关联命令**（NP卡级联口专有，★完整保留）：
  - `ADD NPDIRECTCONNECTPORT` — 增加多框级联配置（使能级联口）
  - `LST NPDIRECTCONNECTPORT` — 查询多框级联配置
  - `RMV NPDIRECTCONNECTPORT` — 删除多框级联配置
- **对接面**：CS-4路由对接（硬件级联子分支）

**操作场景**：带NP卡专有硬件之间级联组网时，若VNF实例化后级联口数据与规划不一致，需修改级联口。

**核心要点**：
1. **两框对等板级联**：两框对等板（相同槽位的单板）上NP出级联线完成两框互联，**框间NP级联口必须全部直连**。
2. **典型配置（P3口级联，框0+框1各Slot1~Slot6）**：
   ```
   ADD NPDIRECTCONNECTPORT: SUBRACK=Subrack_0, SLOTID=Slot_1, PORTID=P3;
   ADD NPDIRECTCONNECTPORT: SUBRACK=Subrack_0, SLOTID=Slot_2, PORTID=P3;
   ... (Slot_3~Slot_6 同样)
   ADD NPDIRECTCONNECTPORT: SUBRACK=Subrack_1, SLOTID=Slot_1, PORTID=P3;
   ... (框1 Slot_2~Slot_6 同样)
   ```
3. **P1~P4 ↔ 位置1~4 对应**（位置3=P3级联口）。
4. **告警处理**：先连线再使能级联口会产生外联口DOWN告警（ALM-89005），不影响业务，确认后可手动清除。
5. **级联拓扑约束**（附加信息）：
   - 仅支持框0与PE连接，框1通过框0与PE连接。
   - **框0整体故障→整个网元故障**；框1故障→框0业务不受影响。
   - 框0外联口配置与单框无区别。

---

### KP-03: NP卡各路由配置（IPv4/IPv6）— 差异点为主
- **来源**（8份）：
  - `配置动态路由OSPF+BFD组网（IPv4）_54211732.md` / `（IPv6）_54211735.md`
  - `配置静态路由+BFD组网（IPv4）_54211731.md` / `（IPv6）_54211734.md`
  - `配置BGP over OSPF_静态路由+BFD（IPv4）_54211730.md` / `（IPv6）_54211733.md`
  - `配置IPsec_80588530.md` / `配置PGW-U_UPF与PDN_DN之间的GRE隧道_84978377.md`
- **核心度**：★★（命令同Batch-04/05，仅差异点）
- **关联特性**：IPFD-014001 OSPF、IPFD-014002 BGP、IPFD-014003 静态路由、IPFD-012003 BFD、IPFD-015004 IPsec
- **对接面**：CS-4

**差异点（NP卡分支 vs Batch-04/05）**：
1. **接口命名差异**：数据表样例接口名 = `100GE66/0/9`、`100GE67/0/9`（NP100）；NP121为 `400GE/200GE X/0/9`。
   - `MOD INTERFACE`、`ADD INTERFACE`、`ADD TRUNKMEMBER`、`ADD IFIPV4ADDRESS` 等接口名参数全部使用NP卡命名。
2. **Ethernet子接口双平面双PE对接模式**（NP卡直连PE特有）：
   - 一组外联口分别规划在不同刀片的NP卡上，每个NP卡各规划1个子接口负荷分担。
   - Ethernet子接口组网时**直连PE规划2个不同网段的IP**（每PE一段）；Eth-trunk子接口组网时**规划1个IP**。
3. **Eth-trunk LACP模式约束**（与其他分支共享但在此强调）：
   - 本端LACP的Eth-trunk仅支持 **passive模式**，要求对接DC-GW/PE的Eth-trunk必须为 **active模式**（对端主动发LACP报文）。
   - 加速省交换场景下，同一Trunk成员接口在不同刀片上。
4. **路由协议命令簇**（与Batch-04/05一致，简略引用）：
   - OSPF：`ADD OSPF` / `ADD OSPFAREA` / `ADD OSPFNETWORK` / `ADD OSPFIMPORTROUTE`
   - 静态路由：`ADD SRROUTE` / `ADD BFDSESSION`（含 ONEARMECHO 单臂Echo选项）
   - BGP：`SET BGP` / `ADD BGPVRF` / `ADD BGPVRFAF` / `ADD BGPPEER` / `ADD IMPORTROUTE`
   - VPN：`ADD L3VPNINST` / `ADD VPNINSTAF` / `ADD IPBINDVPN` / `ADD ETHSUBIF`
   - 子接口/Trunk：`MOD INTERFACE` / `ADD INTERFACE` / `MOD TRUNKIF` / `ADD TRUNKMEMBER`

---

### KP-04: NP卡 IPsec / GRE / MPLS VPN（非SDN手动）
- **来源**：
  - `配置IPsec_80588530.md`（IPsec，特性 IPFD-015004）
  - `配置PGW-U_UPF与PDN_DN之间的GRE隧道_84978377.md`（GRE）
  - `配置BGP_MPLS VPN（非SDN_手动）_33255612.md`（MPLS VPN）
- **核心度**：★★★（特性 **GWFD-020411 MPLS VPN**）
- **关联特性**：GWFD-020411、IPFD-014002、IPFD-012003
- **对接面**：CS-4

**核心要点（与Batch-05手动版MPLS VPN完全同构，差异点）**：
1. **MPLS VPN = UDG作PE接入MPLS骨干网**，通过 **MP-EBGP** 与其他PE传播VPN信息和VPN-IPv4路由，**OptionB跨域VPN**。
2. **UDG和DC-GW间通过Loopback IP建立eBGP邻居**，交换私网VPN路由。
3. **关键全局配置**：
   - `SET MPLSSITE: MPLSLSRID=..., MPLSENABLE=ENABLE, LDPENABLE=DISABLE`（开MPLS不开LDP）
   - `SET BGP: BGPENABLE=TRUE, ASNUM=...`
4. **N6外联口与非MPLS组网差异点**：
   - 绑定的VPN实例名固定为 `_public_`。
   - **不需要配置IPv6数据**（MP-EBGP组网使用IPv4 eBGP传递IPv6私网路由）。
   - Loopback接口**不绑定VPN**（用公网BGP传递私网路由），不需要规划IPv6地址。
5. **标签分配模式组合**：`VRFLABELMODE=perInstance`（VPN实例侧）+ `APPLYLABELMODE=perNexthop`（BGP VPN地址族侧），节省标签资源。
6. **MPLS OptionB 必须配置 VRFRD 值**。
7. **IPsec 触发场景**：信令/数据报文跨安全域传输时（如 Sxa/Sxb/N4 跨区信令、S1-U/N3 跨区数据）建议按需配置。
8. **GRE 隧道**：PGW-U/UPF与WAP网关间建立GRE VPN，必须基于Loopback接口；外联口BGP/OSPF动态路由时Loopback网段必须对外发布。

---

### KP-05: SDN组网介绍（★SDN特有机制）
- **来源**：`SDN组网介绍_58930596.md`
- **核心度**：★★★★★（SDN分支基础）
- **关联特性**：SDN/NFVO架构（非UDG特性，属组网架构）
- **对接面**：CS-4（SDN子分支）

**SDN vs 引入SDN前的本质差异**：
| 维度 | 引入SDN前 | 引入SDN后 |
|------|----------|----------|
| 业务网元部署 | 通过VNFM部署 | 通过NFVO直接部署 |
| 描述文件 | VNFD | VNFD + **NSD**（新增） |
| 新增功能组件 | — | **SDN控制器** + **NFVO** |
| 网络配置 | 手动配置 | 自动化（SDN控制器映射逻辑→物理网络） |

**SDN架构关键组件**（Leaf-Spine）：
| 组件 | 角色 |
|------|------|
| **NFVO** | 使用NSD文件定义VNF连接需求，构建VNF接入逻辑网络、VNF间连接，生命周期管理 |
| **VNFM** | 使用VNFD文件定义VNF内部网络需求，VNF生命周期管理 |
| **VIM** | 分配VNF-VM资源池，计算/存储/网络虚拟资源管理 |
| **SDN Controller** | 网络自动化控制中心，逻辑网络→物理网络映射，资源纳管 |
| **Server Leaf** | VXLAN隧道起点，VNF接入VXLAN |
| **Spine** | Fabric交换中枢（可独立或与Border Leaf合一） |
| **Border Leaf** | Fabric与外部网络边界，VXLAN隧道终点 |
| **DC-GW** | DC与WAN边界路由，南北流量转发 |
| **PE** | MPLS骨干网边界，**不在SDN网络范围内** |

**SDN组网四大原则（★关键约束）**：
1. **不支持DC-GW和VNF间使用OSPF路由交互**（与非SDN的本质差异）。
2. **VNF外联口IP通过DHCP动态获取**（非静态规划）。
3. **VNF和直连Server Leaf间配置BFD echo（单臂BFD）**用于链路检测，与静态路由联动。
4. **VNF和DC-GW间采用 BGP over 静态路由 组网**：
   - DC-GW配置到VNF Loopback IP的静态路由，下一跳为IPU/ISU虚拟机的vNIC IP（多IPU则多条等价路由）。
   - VNF配置到DC-GW Loopback IP的静态路由（可配默认路由，下一跳为Server Leaf网关IP）。
   - Loopback三层互通后基于Loopback IP建立eBGP邻居，学习发布业务路由。

---

### KP-06: SDN — BGP over静态路由+BFD(IPv4) ★SDN主路径
- **来源**：`BGP over静态路由+BFD(IPv4)_80466089.md`
- **核心度**：★★★★★（SDN推荐自动部署路径）
- **关联特性**：IPFD-014003 静态路由、IPFD-014002 BGP、IPFD-012003 BFD
- **对接面**：CS-4

> **★BFD特性ID勘误**：文档中引用特性为 `IPFD-104403 BFD特性概述`（别名/旧编号），**规范特性ID为 `IPFD-012003`**（特性指南实际路径）。下同 IPv6/IPv4v6/MPLS VPN文档。

**SDN特有的 AUTOSCALING 命令族（★完整保留，SDN自动部署核心）**：
| 命令 | 作用 | SDN关键参数 |
|------|------|------------|
| `ADD AUTOSCALINGETHTRUNK` | SR-IOV bonding多虚拟网卡模板 | `VNICLIST`（MAC相同且ID连续的两以太接口） |
| `ADD AUTOSCALINGSERVICE` | 外联口自动部署模板 | `IPALLOCTYPE4=DHCP`（强制）、`NETWORKINSTID`、`AUTOCFGIFTYPE=VNIC/ETHTRUNK` |
| `ADD AUTOSCALINGBFD` | BFD会话自动部署模板 | `BFDTYPE=Static`、**`ONEARMECHO=TRUE`（强制单臂）**、`DESTADDR4`=Leaf节点IP |
| `ADD AUTOSCALINGSRROUTE` | 静态路由自动部署模板 | `NEXTHOPALLOCTYPE4=DHCP`（强制）、`BFDENABLE=TRUE`、`BFDTEMPLATENAME` |
| `SET AUTOCONFIG` | 自动配置开关 | 关闭后才能修改模板（`SWITCHFLAG=FALSE`），改完打开 |
| `DSP OPSASSISTSTATE` | 查询自动部署维护助手状态 | 必须"Ready"才能关闭/打开开关 |
| `LST AUTOCONFIG` | 查询自动配置开关 | — |

**SDN自动部署典型流程**：
```
1. ADD L3VPNINST + ADD VPNINSTAF (配置VRF, e.g. VRF_Access)
2. SET BFD: BFDENABLE=TRUE;
3. LST AUTOCONFIG → SET AUTOCONFIG: SWITCHFLAG=FALSE (关开关)
4. [SR-IOV bonding] ADD AUTOSCALINGETHTRUNK
5. ADD AUTOSCALINGSERVICE (外联口模板, IPALLOCTYPE4=DHCP)
6. ADD AUTOSCALINGBFD (BFD模板, ONEARMECHO=TRUE, DEST=Leaf IP)
7. ADD AUTOSCALINGSRROUTE (两类: 到BGP Peer路由 + 业务默认路由, BFD联动)
8. SET AUTOCONFIG: SWITCHFLAG=TRUE (开开关)
9. SET BGP: BGPENABLE=TRUE, ASNUM=...
10. ADD INTERFACE Loopback1 + ADD IPBINDVPN + ADD IFIPV4ADDRESS
11. ADD BGPVRF + ADD BGPVRFAF (MAXIMUMLOADBALANCE) + ADD BGPPEER + ADD IMPORTROUTE(wlr)
```

**IPv4特有要点**：
- 两条静态路由：① 到BGP对等体地址（PREFIX4=Peer Loopback, MASK=32）；② 业务默认路由（0.0.0.0/0），均 `NEXTHOPALLOCTYPE4=DHCP` + BFD联动。
- `MAXIMUMLOADBALANCE=2`（对接2个负荷分担BGP邻居时）。
- BGP `IMPORTPROTOCOL=wlr`（引入WLR路由）。
- `NETWORKINSTID` 参数：仅当一个UPF对接的所有企业总共规划65~128 VPN专线时N6口需配置；一个网络分组标识最多绑64个VPN实例；UPF当前最多支持128个VPN专线。

---

### KP-07: SDN — BGP over静态路由+BFD(IPv6)
- **来源**：`BGP over静态路由+BFD(IPv6)_80466090.md`
- **核心度**：★★★★
- **关联特性**：同KP-06（IPv6版本）

**IPv6 vs IPv4 差异点**：
1. **DHCPv6 DUID必须配置**（SDN DHCP分配IPv6前提）：
   ```
   SET DHCP6CLIENTDUID: DUIDTYPE=MAC_PLUS_VLAN;
   ```
2. **外联口IPv6地址模式**：`ADDRMODE=NETWOKSEGMENT_MODE`（强制）。
3. 地址族/前缀参数变体：`AFTYPE=ipv6uni`、`PREFIX6`、`MASKLENGTH=128`、`PEERADDRV6`、`NEXTHOPALLOCTYPE6=DHCP`、`DESTADDR6`（Leaf IPv6）。
4. Loopback接口配置 IPv6 前必须 `SET IFIPV6ENABLE: IFNAME=..., ENABLEFLAG=TRUE`。
5. `ADD BGPVRFAF: AFTYPE=ipv6uni`。
6. IPv6默认路由前缀为 `0:0:0:0:0:0:0:0`（全0）。

---

### KP-08: SDN — BGP over静态路由+BFD(IPv4v6) 双栈
- **来源**：`BGP over静态路由+BFD(IPv4v6)_80466091.md`
- **核心度**：★★★★

**双栈要点**：
1. **VPN实例地址族两个都要配**：`ipv4uni` + `ipv6uni`。
2. **外联口模板四条**（IPv4×2 + IPv6×2，共享vNIC/VLAN）。
3. **BFD模板四条**：IPv4 Leaf IP ×2 + IPv6 Leaf IP ×2。
4. **静态路由模板**：v4对等体+v4默认+v6对等体+v6默认 共4×2=8条。
5. **Loopback双栈**：`ADD IFIPV4ADDRESS`（带 `ADDRTYPE=main`）+ `SET IFIPV6ENABLE` + `ADD IFIPV6ADDRESS`。
6. **BGP VPN实例ROUTERID共用**：IPv4和IPv6 BGP VPN实例地址族共用一个ROUTERID。
   - ★删除IPv4地址族前必须先查询记录ROUTERID，删除后若ROUTERID丢失需用 `MOD BGPVRF` 补回，否则IPv6 BGP重新协商会失败。
7. BGP对等体4个（v4×2 + v6×2），共享 `Loopback1` 本地接口名。

---

### KP-09: SDN — BGP MPLS VPN（SDN）★SDN+MPLS特有
- **来源**：`配置BGP_MPLS VPN（SDN）_20748722.md`
- **核心度**：★★★★★（特性 **GWFD-020411 MPLS VPN**，SDN场景）
- **关联特性**：GWFD-020411、IPFD-014002、IPFD-012003
- **对接面**：CS-4

**SDN MPLS VPN vs 非SDN手动 MPLS VPN 差异**：
| 维度 | 非SDN手动（Batch-05/KP-04） | SDN（本KP） |
|------|---------------------------|-------------|
| 部署方式 | 全手动 `ADD SRROUTE`/`ADD MPLSIF` | AUTOSCALING自动 + MPLS自动模板 |
| Loopback互通 | 静态路由/OSPF | **静态路由（DHCP下一跳）** |
| 接口MPLS使能 | `ADD MPLSIF` 手动 | **`ADD AUTOSCALINGMPLS` 自动** |
| VM扩容 | 手动ADD MPLSIF新接口 | 自动模板自动添加新接口 |

**SDN MPLS VPN关键命令（★SDN特有）**：
- `SET MPLSSITE: MPLSLSRID=..., MPLSENABLE=ENABLE, LDPENABLE=DISABLE`（开MPLS不开LDP）
- `ADD AUTOSCALINGMPLS: SERVICENAME=...`（★MPLS自动化模板，将外联口自动配为MPLS接口）
- `ADD MPLSIF`（手动补充，扩容前若手动添加则扩容时仍需手动）

**核心约束**：
1. **外联口VRFNAME固定 `_public_`**，仅IPv4（MP-EBGP用IPv4 eBGP传IPv6私网路由），不需要IPv6数据。
2. **Loopback接口不绑定VPN**，不规划IPv6地址。
3. **MPLS OptionB 必须配 VRFRD**，`VRFLABELMODE=perInstance` + BGP `APPLYLABELMODE=perNexthop`。
4. **业务默认路由 PREFERENCE=255**（与非SDN默认路由不同，SDN MPLS场景默认路由优先级设255）。
5. **MP-EBGP开关**：`ADD BGPVRFAF: VRFNAME="_public_", AFTYPE=ipv4vpn / ipv6vpn, APPLYLABELMODE=perNexthop`（vpn地址族是MP-EBGP使能开关）。
6. **BGP对等体仅IPv4**：`ADD BGPPEER: VRFNAME="_public_", ADDRESSTYPE=ipv4, PEERADDR=...`（自动生成ipv4uni对等体地址族，若不需要可用 `RMV BGPPEERAF` 删除）。
7. **BGP对等体地址族使能VPNv4/VPNv6**：`ADD BGPPEERAF: VRFNAME="_public_", AFTYPE=ipv4vpn/ipv6vpn, REMOTEADDRESS=...`。
8. **企业VPN实例按PDN数创建**（VRF_PDN1~5示例），每个VPN配 export_extcommunity + import_extcommunity RT值。
9. 自动部署开关打开后有时延，操作前必须 `DSP OPSASSISTSTATE` 确认"Ready"。

---

## 3. 关键发现

### F-1: SDN vs 非SDN 本质差异（★核心决策矩阵）
| 差异点 | 非SDN（Batch-04/05/NP卡） | SDN（Batch-06） |
|--------|--------------------------|-----------------|
| **路由协议** | OSPF / 静态 / BGP over OSPF·静态 / MPLS VPN | **仅 BGP over 静态路由 / BGP MPLS VPN** |
| **OSPF支持** | ✅ | ❌ 不支持DC-GW和VNF间OSPF |
| **外联口IP获取** | 静态规划 `ADD IFIPV4ADDRESS` | **DHCP动态获取** (`IPALLOCTYPE4/6=DHCP`) |
| **下一跳获取** | 静态IP | **DHCP** (`NEXTHOPALLOCTYPE4/6=DHCP`) |
| **BFD模式** | 双向BFD + 单臂Echo可选 | **强制单臂BFD Echo** (`ONEARMECHO=TRUE`) |
| **BFD目的地址** | 网关接口IP | **Leaf节点IP**（VNF↔Server Leaf直连检测） |
| **BGP对等体对象** | PE / DC-GW | **DC-GW**（经Leaf/Spine中转） |
| **部署方式** | 自动部署(无NP卡) / 手动(NP卡/加速卡) | **自动部署推荐** + 手动（手动复用非SDN手动章节+4点差异） |
| **控制器协同** | 无 | **SDN控制器统一纳管DC-GW/Spine/Server Leaf/TOR** |
| **外联口模板** | 无 | **AUTOSCALING 命令族**（模板化） |
| **`SET IFIPV6ENABLE` 参数** | 默认 | **`AUTOLINKLOCAL=TRUE` 必设**（SDN场景约束） |
| **`ADD SRROUTE/SRROUTE6` 参数** | 默认 | **`DHCPENABLE=TRUE` 必设**（SDN场景约束） |

### F-2: NP卡级联口（NP100）配置要点
1. 命令专有：`ADD/LST/RMV NPDIRECTCONNECTPORT`（仅NP卡多框级联场景）。
2. 框间级联口必须全部直连（两框对等板同槽位）。
3. 拓扑单点：框0是PE连接唯一节点，框0故障=网元故障。
4. 与Batch-05的"修改级联口数据（NP100）_81556318.md"为同命令不同上下文（Batch-05=加速卡直连DC-GW场景，Batch-06=NP卡直连PE场景，命令一致）。

### F-3: NP卡型号决策（NP100 vs NP121）
- **NP100**：100GE固定速率，成员口仅跨刀片，外联口名 `100GE X/0/9`。
- **NP121**：400GE/200GE/100GE自适应，成员口跨刀片+跨同刀片不同NP卡，外联口名 `400GE/200GE X/0/9`，**不可作标卡**，推荐SR-IOV bonding。

### F-4: AUTOSCALING 命令族为SDN/自动部署核心
- 共享于 Batch-04(无NP卡自动) 与 Batch-06(SDN自动)；
- 关键参数差异：SDN强制 DHCP下一跳 + 单臂Echo + Leaf目的IP；
- `NETWORKINSTID`：仅65~128 VPN专线N6口场景必配，其余可不配（默认0）。

### F-5: BFD特性ID勘误
- SDN BGP over静态路由3份文档 + SDN MPLS VPN 文档中引用 "IPFD-104403 BFD特性概述"；
- 实际特性指南路径规范ID为 **IPFD-012003**（IPFD-104403为旧/别名编号）；
- 路径：`特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-012000 IP可靠性/IPFD-012003 BFD/`。

### F-6: IPv6 DHCP前置（SDN特有）
- DHCPv6 分配IPv6前必须 `SET DHCP6CLIENTDUID: DUIDTYPE=MAC_PLUS_VLAN`（IPv6/IPv4v6 SDN场景必备）。
- 外联口IPv6地址 `ADDRMODE=NETWOKSEGMENT_MODE`（强制）。

---

## 4. 对接面与决策点归纳

### DP-1: 硬件 × 组网 决策矩阵（CS-4路由对接全集）
| 硬件\组网 | 非SDN自动部署 | 非SDN手动部署 | SDN |
|-----------|--------------|--------------|-----|
| **无NP卡** | ✅ Batch-04 | ✅ Batch-05 | ✅ Batch-06 |
| **NP卡直连PE** | ❌ 不支持自动 | ✅ Batch-06(KP-03/04) | ❌ 不支持SDN |
| **网络加速卡直连DC-GW** | — | ✅ Batch-05 | — |

### DP-2: NP卡分支命令差异要点
- 共享 Batch-05 路由协议命令簇（OSPF/静态/BGP/MPLS VPN/IPsec/GRE）。
- **分支独有命令**：`ADD/LST/RMV NPDIRECTCONNECTPORT`（级联口）。
- **分支独有约束**：npworkmode=1、Eth-trunk passive需对端active、Ethernet子接口双平面双PE（2个不同网段IP）。

### DP-3: SDN分支决策点
- **路由协议分支**：BGP over静态路由+BFD（IPv4单栈/IPv6单栈/IPv4v6双栈） vs BGP MPLS VPN（企业对接、跨域）。
- **子接口模式**：VNIC（非SR-IOV bonding） vs ETHTRUNK（SR-IOV bonding，需 AUTOSCALINGETHTRUNK 模板）。
- **VPN实例绑定**：普通业务 `VRF_Access`（自定义） vs MPLS VPN N6口 `_public_`（固定）。
- **MPLS VPN标签模式**：`perInstance` + `perNexthop`（推荐，省标签）。

### DP-4: SDN手动部署4点差异（若不用自动部署）
手动部署复用 `配置VNF侧IP路由数据（无NP卡_非SDN）/手动部署_16653307.md` 章节，差异点：
1. SDN场景VNF外联口IP采用DHCP动态获取。
2. SDN场景 `SET IFIPV6ENABLE` 的 `AUTOLINKLOCAL` 参数必须设 `TRUE`。
3. SDN场景采用单臂BFD echo探测。
4. SDN场景 `ADD SRROUTE/SRROUTE6` 的 `DHCPENABLE` 参数必须设 `TRUE`。

---

## 附录：批次文件清单（17份，含2父级）

### NP卡直连PE 分支（11份）
1. `配置VNF侧IP路由数据（NP卡直连PE）_52117668.md`（父级，硬件规划）
2. `修改级联口数据（NP100）_90163990.md`（★级联口专有）
3. `配置动态路由OSPF+BFD组网（IPv4）_54211732.md`
4. `配置静态路由+BFD组网（IPv4）_54211731.md`
5. `配置BGP over OSPF_静态路由+BFD（IPv4）_54211730.md`
6. `配置动态路由OSPFv3+BFD组网（IPv6）_54211735.md`
7. `配置静态路由+BFD组网（IPv6）_54211734.md`
8. `配置BGP over OSPFv3_静态路由+BFD（IPv6）_54211733.md`
9. `配置IPsec_80588530.md`
10. `配置PGW-U_UPF与PDN_DN之间的GRE隧道_84978377.md`
11. `配置BGP_MPLS VPN（非SDN_手动）_33255612.md`

### SDN 分支（6份）
12. `配置VNF侧IP路由（SDN）_80548319.md`（父级，含4点手动差异）
13. `SDN组网介绍_58930596.md`（★SDN架构基础）
14. `BGP over静态路由+BFD(IPv4)_80466089.md`
15. `BGP over静态路由+BFD(IPv6)_80466090.md`
16. `BGP over静态路由+BFD(IPv4v6)_80466091.md`
17. `配置BGP_MPLS VPN（SDN）_20748722.md`

---

## 附录：关键MML命令索引（本批特有/重点）

### NP卡级联口（NP100）专有
- `ADD NPDIRECTCONNECTPORT` / `LST NPDIRECTCONNECTPORT` / `RMV NPDIRECTCONNECTPORT`

### SDN AUTOSCALING 自动部署族（★SDN核心）
- `ADD AUTOSCALINGETHTRUNK` / `LST/RMV AUTOSCALINGETHTRUNK`
- `ADD AUTOSCALINGSERVICE` / `LST/RMV AUTOSCALINGSERVICE`
- `ADD AUTOSCALINGBFD` / `LST/RMV AUTOSCALINGBFD`
- `ADD AUTOSCALINGSRROUTE` / `LST/RMV AUTOSCALINGSRROUTE`
- `ADD AUTOSCALINGMPLS`（★SDN MPLS VPN特有）
- `SET AUTOCONFIG` / `LST AUTOCONFIG` / `DSP OPSASSISTSTATE`

### SDN DHCPv6 前置
- `SET DHCP6CLIENTDUID: DUIDTYPE=MAC_PLUS_VLAN`

### MPLS VPN 全局
- `SET MPLSSITE`（MPLSENABLE=ENABLE, LDPENABLE=DISABLE）
- `ADD MPLSIF`（手动MPLS接口，扩容补充）

### 共享路由协议命令（同Batch-04/05，简略）
- L3VPN: `ADD L3VPNINST` / `ADD VPNINSTAF` / `MOD VPNINSTAF` / `ADD VPNTARGET` / `ADD IPBINDVPN`
- BGP: `SET BGP` / `ADD BGPVRF` / `MOD BGPVRF` / `ADD BGPVRFAF` / `ADD BGPPEER` / `ADD BGPPEERAF` / `ADD IMPORTROUTE` / `RMV BGPPEERAF`
- 接口: `ADD INTERFACE` / `MOD INTERFACE` / `ADD ETHSUBIF` / `ADD IFIPV4ADDRESS` / `ADD IFIPV6ADDRESS` / `SET IFIPV6ENABLE`
- Trunk: `MOD TRUNKIF` / `ADD TRUNKMEMBER`
- BFD: `SET BFD` / `ADD BFDSESSION`
- OSPF: `ADD OSPF` / `ADD OSPFAREA` / `ADD OSPFNETWORK` / `ADD OSPFIMPORTROUTE`
- 静态路由: `ADD SRROUTE` / `ADD SRROUTE6`
- GRE: `ADD GRETUNNEL`
