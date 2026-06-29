# Batch-05: CS-4路由对接 — 非SDN无NP卡(手动) + 网络加速卡直连DC-GW

> 批次05 | 对接面 CS-4 路由对接 | 文件数 16 | 核心度 ★★★★
> 主题轨Agent产出 | 子场景: UPF网元对接 | 2026-06-29
> 路径前缀: `output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/组网路由配置/`

---

## 1. 概述

本批次覆盖 **CS-4 路由对接** 两个并列分支，与 Batch-04（非SDN无NP卡**自动部署**）形成完整对比：

### 1.1 手动部署定位（文件 1~9）
- **场景**：VNF侧IP路由数据的**手动部署**（非自动）。当局点不采用自动部署、或自动部署模板不适用时，操作员逐条MML命令手工下发外联口/VLAN/IP/VPN/路由配置。
- **硬件**：无NP卡的标卡硬件（Ethernet66/0/X 物理口 + 子接口）或 SR-IOV bonding（Eth-trunk）。
- **对接对象**：DC-GW / EOR / PE（VNF配置相同，对端配置参考对应产品文档）。
- **覆盖方案**：OSPF+BFD(IPv4/IPv6)、静态路由+BFD(IPv4/IPv6)、BGP over OSPF/静态路由+BFD(IPv4/IPv6)、IPsec、GRE隧道、BGP/MPLS VPN（非SDN手动）。
- **关键定位**：路由协议命令本身与自动部署一致（OSPF/静态/BGP/MPLS协议层无差异），**差异在"外联口/子接口/VLAN/IP/VPN绑定"的基础设施层必须手工MML下发**，且 **MPLS接口（ADD MPLSIF）需手动逐个配置**（自动部署用 ADD AUTOSCALINGMPLS 模板）。

### 1.2 网络加速卡直连DC-GW硬件分支定位（文件 10~16）
- **场景**：UDG专有硬件**所有槽位刀片均带网络加速卡**（NP100 或 NP121），U面下沉，加速卡接口**直连DC-GW**（加速省交换场景）。
- **触发条件**：UDG 20.12.2 及后续版本 + U面下沉 + 全槽位带网络加速卡 → 推荐本方案。
- **关键约束**：`npworkmode=1`（默认值，加速省交换场景必须为1）；**不支持SDN组网**。
- **核心协议**：**BGP over 静态路由+BFD**（基于Loopback IP建立eBGP邻居），网络加速卡场景**仅支持静态路由+BFD单臂Echo**，不支持OSPF动态路由协议。
- **部署方式**：**自动部署模板**（ADD AUTOSCALINGETHTRUNK / AUTOSCALINGSERVICE / AUTOSCALINGBFD / AUTOSCALINGSRROUTE），非逐条手工。
- **硬件类型**：NP100（100GE接口，级联口P3/P4）、NP121（400GE/200GE自适应，无级联概念）。

---

## 2. 核心知识点（KP）

### KP-01: 手动部署 vs 自动部署差异（★关键，本批次核心差异）

- **来源**：`手动部署/配置动态路由OSPF+BFD组网（IPv4）_16653312.md`、`配置静态路由+BFD组网（IPv4）_16653313.md`、`配置BGP_MPLS VPN（非SDN_手动）_70507877.md` 等9个手动部署文件
- **核心度**：★★★★★
- **关联特性**：IPFD-014000 路由功能 / IPFD-014001 OSPF / IPFD-014002 BGP / IPFD-014003 静态路由 / IPFD-012003 BFD / GWFD-020411 MPLS VPN
- **关联命令**（手动部署**特有或必须手工下发**）：
  - 外联口基础设施：`MOD INTERFACE`（主接口up）、`ADD INTERFACE`（子接口）、`ADD IPBINDVPN`（绑定VPN）、`ADD ETHSUBIF`（VLAN）、`ADD IFIPV4ADDRESS`/`ADD IFIPV6ADDRESS`（IP）、`MOD TRUNKIF`+`ADD TRUNKMEMBER`（SR-IOV bonding Eth-trunk）
  - 路由协议：`ADD OSPF`/`ADD OSPFV3`、`ADD OSPFAREA`/`ADD OSPFV3AREA`、`ADD OSPFNETWORK`、`ADD OSPFINTERFACE`/`ADD OSPFV3INTERFACE`、`ADD OSPFIMPORTROUTE`/`ADD OSPFV3IMPORTROUTE`、`ADD BFDSESSION`（静态BFD）、`ADD SRROUTE`/`ADD SRROUTE6`、`SET BGP`、`ADD BGPVRF`、`ADD BGPVRFAF`、`ADD BGPPEER`、`ADD IMPORTROUTE`
  - **MPLS接口（手动部署关键差异）**：`ADD MPLSIF`（逐个接口手动添加为MPLS接口）
  - GRE隧道：`ADD GRETUNNEL`、`ADD IPBINDVPN`、`ADD IFIPV4ADDRESS`、`ADD SRROUTE`、`MOD GRETUNNEL`（校验/keepalive）
- **配置对象**：VPN实例(VRF)、外联口子接口(Ethernet66/0/X.Y 或 Eth-trunkX.Y)、VLAN、BFD会话、OSPF进程/区域、静态路由、BGP VPN实例/对等体、Loopback接口、MPLS接口、GRE Tunnel
- **对接面**：CS-4 路由对接

**★ 手动部署 vs 自动部署命令差异矩阵**

| 配置层 | 自动部署（Batch-04） | 手动部署（本批次） |
|--------|---------------------|-------------------|
| 外联口/子接口/VLAN/IP/VPN | `ADD AUTOSCALINGSERVICE`（模板，自动生成子接口+IP+VLAN+VPN绑定） | **逐条手工**：MOD INTERFACE → ADD INTERFACE → ADD IPBINDVPN → ADD ETHSUBIF → ADD IFIPV4/V6ADDRESS |
| BFD会话（静态路由场景） | `ADD AUTOSCALINGBFD`（模板） | `ADD BFDSESSION`（逐条，含LOCALDISCR/REMOTEDISCR/ONEARMECHO） |
| 静态路由 | `ADD AUTOSCALINGSRROUTE`（模板） | `ADD SRROUTE`/`ADD SRROUTE6`（逐条，SESSIONNAME绑定BFD） |
| OSPF/BGP协议层 | 与手动**相同**（ADD OSPF / SET BGP / ADD BGPPEER等） | 与自动**相同** |
| **MPLS接口**（MPLS VPN场景） | `ADD AUTOSCALINGMPLS`（模板，VM扩容自动适配） | **`ADD MPLSIF` 逐个手动**；VM扩容时新接口也需手工 ADD MPLSIF |
| 自动化开关 | SET AUTOCONFIG:SWITCHFLAG=TRUE/FALSE 控制 | 不涉及（无模板） |

**关键发现**：协议层（OSPF/BGP/MPLS VPN 的 VPN实例/对等体/地址族/RT/LDP等）命令在手动与自动部署中**完全一致**；差异集中在**外联口基础设施层**（自动用模板，手动逐条）和 **MPLS接口层**（自动用 AUTOSCALINGMPLS 模板，手动逐个 ADD MPLSIF）。

---

### KP-02: 手动部署 OSPF+BFD（IPv4/IPv6）— 与自动部署的协议层无差异

- **来源**：`手动部署/配置动态路由OSPF+BFD组网（IPv4）_16653312.md`、`配置动态路由OSPFv3+BFD组网（IPv6）_16653304.md`
- **核心度**：★★★（协议命令同 Batch-04 KP，此处仅记录差异点）
- **关联特性**：IPFD-014001 OSPF、IPFD-012003 BFD
- **关联命令**：`ADD OSPF`（PROCID/VRFNAME/SCHEMAROUID/BFDALLINTFFLG=TRUE/BFDMINRXINTV/BFDMINTXINTV/SCHEMABFDDETMUL/**VPNINSCAPSIMFLG=TRUE**/**VIRTUALSYSFLAG=TRUE**）、`ADD OSPFAREA`（AREAID/AREATYPE=NSSA|Normal）、`ADD OSPFINTERFACE`、`ADD OSPFNETWORK`、`ADD OSPFIMPORTROUTE`(PROTOCOL=wlr)；IPv6 用 `ADD OSPFV3` 系列 + `SET IFIPV6ENABLE`
- **配置对象**：OSPF进程(PROCID=6)、OSPF区域(AREAID=0.0.0.5, AREATYPE=NSSA)、Loopback（NSSA区域需配Loopback作FA，掩码255.255.255.255）
- **对接面**：CS-4

**差异要点（vs 自动）**：仅外联口基础设施层手工（MOD INTERFACE/ADD INTERFACE/ADD IPBINDVPN/ADD ETHSUBIF/ADD IFIPV4ADDRESS），OSPF协议命令一致。NSSA区域需手工配Loopback接口并绑定VPN+IP+加入OSPF区域（ADD OSPFINTERFACE 或 ADD OSPFNETWORK WILDCARDMASK=0.0.0.0）。

---

### KP-03: 手动部署 静态路由+BFD（IPv4/IPv6）— BFD会话必须手工建

- **来源**：`手动部署/配置静态路由+BFD组网（IPv4）_16653313.md`、`配置静态路由+BFD组网（IPv6）_16653301.md`
- **核心度**：★★★
- **关联特性**：IPFD-014003 静态路由、IPFD-012003 BFD
- **关联命令**：`SET BFD`(BFDENABLE=TRUE)、`ADD BFDSESSION`（SESSNAME/ADDRTYPE/CREATETYPE4=SESS_STATIC/**LOCALDISCR**/**REMOTEDISCR**/**ONEARMECHO**=FALSE|TRUE/DESTADDR4/LINKTYPE=IP/VRFNAME/IFNAME）、`ADD SRROUTE`（VRFNAME/AFTYPE=ipv4unicast/PREFIX/MASKLENGTH/DESTVRFNAME/NEXTHOP/IFNAME/**SESSIONNAME**绑定BFD）
- **配置对象**：BFD会话(双向/单臂Echo两种)、IPv4/IPv6静态路由
- **对接面**：CS-4

**差异要点（vs 自动）**：
- BFD会话必须手工 `ADD BFDSESSION` 逐条建，需规划 **LOCALDISCR/REMOTEDISCR**（本端本地标识符=对端远端标识符），单臂Echo时删除REMOTEDISCR、ONEARMECHO=TRUE。
- 静态路由通过 `SESSIONNAME` 参数绑定BFD会话。
- 双平面：2个下一跳在不同网段；SR-IOV bonding单平面双主网关：2个下一跳同网段；M-LAG：1个下一跳。
- 回程路由：目的为UE网段地址，下一跳为VNF外联口IP。

---

### KP-04: 手动部署 BGP over OSPF/静态路由+BFD（IPv4/IPv6）

- **来源**：`手动部署/配置BGP over OSPF_静态路由+BFD（IPv4）_16653300.md`、`配置BGP over OSPFv3_静态路由+BFD（IPv6）_16653302.md`
- **核心度**：★★★★
- **关联特性**：IPFD-014002 BGP
- **关联命令**：`SET BGP`(BGPENABLE/ASNUM)、`ADD BGPVRF`(VRFNAME/DEFAULTAFTYPE=noaf/ROUTERID)、`ADD BGPVRFAF`(VRFNAME/AFTYPE=ipv4uni/MAXIMUMLOADBALANCE=2)、`ADD BGPPEER`(VRFNAME/ADDRESSTYPE/PEERADDR/REMOTEAS/LOCALIFADDR/LOCALIFNAME=Loopback1/EBGPMAXHOP=10)、`ADD IMPORTROUTE`(IMPORTPROTOCOL=wlr/MEDENABLE)
- **配置对象**：BGP VPN实例、BGP对等体(基于Loopback1)、Loopback接口
- **对接面**：CS-4

**关键约束（手动部署特有说明）**：
- BGP协议自身**没有自动部署功能**，本文是在OSPF/静态路由手动部署基础上引入BGP传播。
- BFD会话绑定的是**路由**，不是BGPPEER；如存在 ADD BGPPEERBFD 配置请删除。
- 静态路由场景需配两类路由：①目的IP=BGP对等体地址（绑定BFD）；②目的0.0.0.0/0默认路由（对端不发布默认路由时）。
- **双活网关/M-LAG场景约束**：VNF与DC-GW直连且双活网关或M-LAG时，**仅支持 BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议**。
- N6口主备容灾（两UPF的UE地址段重叠）需对外发布网段路由时，MEDENABLE=TRUE，主UPF的MED值<备UPF。
- **入不转板功能**调测：涉及 AUTOSCALINGBGPLF 模板、ROUTEPOLICY、COMMUNITYFILTER、APPLYCOMMUNITY 的查询/删除/重建流程（SET AUTOCONFIG开关控制）。

---

### KP-05: 手动部署 BGP/MPLS VPN（非SDN手动）— MPLS接口逐个手工配置（★关键差异）

- **来源**：`手动部署/配置BGP_MPLS VPN（非SDN_手动）_70507877.md`
- **核心度**：★★★★★
- **关联特性**：GWFD-020411 MPLS VPN、IPFD-014002 BGP、IPFD-012003 BFD
- **关联命令**：
  - MPLS全局：`SET MPLSSITE`(MPLSLSRID/MPLSENABLE=ENABLE/**LDPENABLE=DISABLE**)
  - **MPLS接口（手动部署核心差异）**：`ADD MPLSIF:IFNAME="Ethernet66/0/4.100"` 等（标卡非bonding）/ `ADD MPLSIF:IFNAME="Eth-trunk6604.100"`（标卡bonding）/ `ADD MPLSIF:IFNAME="100GE66/0/9.1"`（NP卡/网络加速卡非bonding）/ `ADD MPLSIF:IFNAME="Eth-trunk1.1"`（NP卡/网络加速卡bonding）
  - VPN实例：`ADD L3VPNINST`(VRFNAME=VRF_PDN1~5)、`ADD VPNINSTAF`(**VRFRD=100:100** 必配、**VRFLABELMODE=perInstance**)、`ADD VPNTARGET`(VRFRTTYPE=export_extcommunity|import_extcommunity/VRFRTVALUE=1:1~5:1)
  - Loopback（不绑VPN）：`ADD INTERFACE`/`ADD IFIPV4ADDRESS`（Loopback1, 10.10.10.78, /32）
  - BGP MP-EBGP：`MOD BGPVRF`(VRFNAME=_public_/ROUTERID)、`ADD BGPVRFAF`(VRFNAME=_public_/**AFTYPE=ipv4vpn**|ipv6vpn/APPLYLABELMODE=perNexthop)、`ADD BGPPEER`(VRFNAME=_public_/ADDRESSTYPE=ipv4/PEERADDR=10.10.20.78,10.10.30.78/EBGPMAXHOP=10)、`ADD BGPPEERAF`(AFTYPE=ipv4vpn|ipv6vpn)、`ADD IMPORTROUTE`(IMPORTPROTOCOL=wlr)
- **配置对象**：MPLS LSR、MPLS接口、L3VPN实例(VRF_PDN1~5)、VPN Target(RT)、公网BGP(_public_)、MP-EBGP对等体
- **对接面**：CS-4（OptionB跨域VPN）

**★ 手动部署 MPLS VPN 关键差异与要点**：
1. **N6外联口绑定 `_public_` VPN**（非MPLS组网绑定业务VPN）；**不需要配IPv6**（MP-EBGP用IPv4 eBGP传递IPv6私网路由）。
2. **Loopback接口不绑定VPN**（用公网BGP传递私网路由）；Loopback仅IPv4（10.10.10.78）。
3. **MPLS OptionB 必须配 VRFRD**；VRFLABELMODE=perInstance 配合 APPLYLABELMODE=perNexthop 节省标签。
4. **★ MPLS接口必须逐个 ADD MPLSIF 手工配置**；VM扩容时新增接口也需手工添加（自动部署则用 ADD AUTOSCALINGMPLS 模板自动适配）。
5. UD G 作为PE设备接入MPLS骨干网，通过MP-EBGP与其他PE传播VPN-IPv4路由，采用 **OptionB** 跨域VPN。

---

### KP-06: 网络加速卡直连DC-GW — 硬件架构与接口对应（NP100/NP121）

- **来源**：`配置VNF侧IP路由数据（网络加速卡直连DC-GW）_32651719.md`
- **核心度**：★★★★★
- **关联特性**：GWFD-111201 网络加速卡流量加速单元（推测关联）
- **关联命令**：无（本节为硬件接口规划）
- **配置对象**：网络加速卡物理接口（NP100/NP121）
- **对接面**：CS-4

**NP100 接口布局（8个位置）**：
| 位置 | 接口名 | 作用 |
|------|--------|------|
| 1, 2 | 100GE*X*/0/9, 100GE*X*/0/8 | **直连DC-GW**，SR-IOV bonding组网（同刀片2口组1个Eth-trunk负荷分担），传N3/N4/N9/N6 |
| 3, 4 | 100GE*X*/0/7, 100GE*X*/0/6 | **级联口**（多框级联） |
| 5~8 | 25GE*X*/0/11,10,13,12 | 预留 |

**NP121 接口布局（8个位置）**：
| 位置 | 接口名 | 作用 |
|------|--------|------|
| 1 | 400GE*X*/0/9 | 直连DC-GW（400GE自适应200GE/100GE） |
| 2~4 | 200GE*X*/0/8,7,6 | 直连DC-GW（200GE自适应100GE） |
| 5~8 | 400GE/200GE*X*/0/11,10,13,12 | 直连DC-GW（**无级联口概念**） |

**关键约束**：
- 接口名 *X* = **63 + Y**，Y=从下往上数第几块刀片（如第3块刀片 Y=3）。
- 1个Eth-trunk所有成员端口在同一刀片；同一DCGW的接口**不跨网络加速卡**（NP121：1-4连DCGW1，5-8连DCGW2）。
- **npworkmode=1**（加速省交换场景默认且必须为1）。
- **不支持SDN组网**。

---

### KP-07: 网络加速卡直连DC-GW — 修改级联口数据（NP100 特有，★关键）

- **来源**：`配置VNF侧IP路由数据（网络加速卡直连DC-GW）/修改级联口数据（NP100）_81556318.md`
- **核心度**：★★★★★（网络加速卡多框级联场景必配）
- **关联特性**：GWFD-111201 网络加速卡流量加速单元
- **关联命令**（★ 网络加速卡特有，无NP卡场景无此命令）：
  - `ADD NPDIRECTCONNECTPORT: SUBRACK=Subrack_0, SLOTID=Slot_1, PORTID=P3;`（框0 Slot1~8 的 P3/P4 口使能为级联口）
  - `ADD NPDIRECTCONNECTPORT: SUBRACK=Subrack_1, SLOTID=Slot_1, PORTID=P4;`（框1 对等板级联口）
  - 验证：`LST NPDIRECTCONNECTPORT`、`RMV NPDIRECTCONNECTPORT`
- **配置对象**：多框级联口（NP100 P3/P4 对应位置3/4）
- **对接面**：CS-4（多框级联基础设施）

**关键要点**：
- **适用场景**：带网络加速卡的专有硬件**多框级联组网**，VNF实例化后级联口数据与规划不一致时修改。
- **连线规则**：两框对等板（相同槽位单板）网络加速卡出级联线完成两框互联，**框间级联口必须全部直连**。
- **P1~P4 对应位置1~4**：P3=位置3（100GE*X*/0/7），P4=位置4（100GE*X*/0/6）。
- **告警提示**：先连线再使能级联口会产生 ALM-89005 NP端口状态为Down 告警（不影响业务，可手动清除）。
- 框0和框1**都需要与DC-GW连接**。
- **NP121 无此配置**（NP121无级联口概念）。

---

### KP-08: 网络加速卡 IPv4 路由配置 — 自动部署模板 + LACP bonding + 单臂BFD（★核心差异）

- **来源**：`配置VNF侧IP路由数据（网络加速卡, IPv4）_81401928.md`
- **核心度**：★★★★★
- **关联特性**：IPFD-014002 BGP、IPFD-014003 静态路由、IPFD-012003 BFD、GWFD-111201 网络加速卡
- **关联命令**（★ 网络加速卡 IPv4 路由核心命令集）：
  - VPN实例：`ADD L3VPNINST`(VRFNAME=VRF_Access)、`ADD VPNINSTAF`(AFTYPE=ipv4uni)、**`MOD VPNINSTAF`(VRFRD="10.10.10.78:100")** ← 网络加速卡场景配RD
  - 全局：`SET BFD`(BFDENABLE=TRUE)
  - 自动化开关：`SET AUTOCONFIG:SWITCHFLAG=FALSE`（配模板前关）→ `DSP OPSASSISTSTATE`（查Ready）→ 配模板 → `SET AUTOCONFIG:SWITCHFLAG=TRUE`
  - **★ Eth-trunk多虚拟网卡自动化模板**：`ADD AUTOSCALINGETHTRUNK`(ETHTRUNKTMPID=1, **VNICLIST="8 9"**[NP100] | **"6 7 12 13"**[NP121], **WORKMODE=Lacp**, **LEASTACTLINKNUM=1**[NP100] | **2**[NP121])
  - **★ 外联口自动部署模板**：`ADD AUTOSCALINGSERVICE`(SERVICENAME=ServName_Access_100_v4, VPNNAME=VRF_Access, AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=1, VLANID=100, BEGINADDR4, ENDADDR4, MASKLEN=27)
  - **★ BFD会话自动部署模板（单臂Echo）**：`ADD AUTOSCALINGBFD`(TEMPLATENAME=BFD_1, BFDTYPE=Static, SERVICENAME, IPVERSION=IPv4, DESTADDR4=网关IP, MINECHORXINT=500, DETECTMULTI=4, **ONEARMECHO=TRUE**)
  - **★ 静态路由自动部署模板**：`ADD AUTOSCALINGSRROUTE`(SERVICENAME, VRFNAME, IPVERSION=IPv4, PREFIX4=对端Loopback IP, MASKLENGTH=32, NEXTHOPALLOCTYPE4=CONFIG, NEXTHOP4=网关IP, BFDENABLE=TRUE, BFDTEMPLATENAME=BFD_1)
  - BGP（Loopback基于静态路由+BFD）：`SET BGP`、`ADD INTERFACE`(Loopback1)、`ADD IPBINDVPN`、`ADD IFIPV4ADDRESS`(10.10.10.78/32)、`ADD BGPVRF`、`ADD BGPVRFAF`(MAXIMUMLOADBALANCE=2)、`ADD BGPPEER`(PEERADDR=10.10.20.78,10.10.30.78 / REMOTEAS=60002 / EBGPMAXHOP=10)、`ADD IMPORTROUTE`(IMPORTPROTOCOL=wlr)
- **配置对象**：VPN实例(VRF_Access)、Eth-trunk模板(ETHTRUNKTMPID=1)、服务模板(ServName_Access_100_v4)、BFD模板(BFD_1)、Loopback1、BGP VPN实例/对等体
- **对接面**：CS-4（BGP over 静态路由+BFD）

**★ 网络加速卡 IPv4 与无NP卡（Batch-04自动部署）核心差异**：

| 维度 | 无NP卡自动部署（Batch-04） | 网络加速卡直连DC-GW（本批次） |
|------|---------------------------|------------------------------|
| 物理口 | Ethernet66/0/X（标卡） | 100GE*X*/0/8,9（NP100）/ 400GE/200GE*X*/0/6,7,12,13（NP121） |
| Eth-trunk工作模式 | Manual（可选bonding） | **Lacp（强制，passive模式）**，DC-GW必须active |
| bonding必要性 | 可选（非SR-IOV bonding可不用） | **强制 SR-IOV bonding**（无标卡选项） |
| 最小激活链路数 | 不涉及 | NP100=1，NP121=2（须与DC-GW一致） |
| BFD类型 | 双向或单臂Echo可选 | **强制单臂Echo（ONEARMECHO=TRUE）** |
| 路由协议 | OSPF/静态/BGP 均支持 | **仅 BGP over 静态路由+BFD**（不支持OSPF） |
| Eth-trunk模板 | 不涉及 | **ADD AUTOSCALINGETHTRUNK**（VNICLIST按NP类型固定） |
| VPN RD | 通常不配 | **MOD VPNINSTAF 配 VRFRD** |
| 路由下一跳分配 | CONFIG | **NEXTHOPALLOCTYPE4=CONFIG**（M-LAG单下一跳） |

---

### KP-09: 网络加速卡 IPv6 路由配置 — 双栈独立模板

- **来源**：`配置VNF侧IP路由数据（网络加速卡, IPv6）_32770255.md`
- **核心度**：★★★★
- **关联特性**：同 KP-08（IPv6变体）
- **关联命令**（与 IPv4 结构一致，IPv6 参数变体）：
  - `ADD VPNINSTAF`(AFTYPE=**ipv6uni**)、`MOD VPNINSTAF`(AFTYPE=ipv6uni, VRFRD)
  - `ADD AUTOSCALINGSERVICE`(AFTYPE=**IPv6**, **IPALLOCTYPE6=USER_CONFIG**, BEGINADDR6=FC00::10C2, ENDADDR6=FC00::10DE, MASKLEN=**123**)
  - `ADD AUTOSCALINGBFD`(IPVERSION=**IPv6**, **DESTADDR6**, ONEARMECHO=TRUE)
  - `ADD AUTOSCALINGSRROUTE`(IPVERSION=**IPv6**, **PREFIX6**, MASKLENGTH=**128**, **NEXTHOPALLOCTYPE6=CONFIG**, **NEXTHOP6**)
  - Loopback：`SET IFIPV6ENABLE`(ENABLEFLAG=TRUE)、`ADD IFIPV6ADDRESS`(IPV6ADDRESS=FC00::10:78, PREFIXLEN=**128**)
  - BGP：`ADD BGPVRFAF`(AFTYPE=**ipv6uni**)、`ADD BGPPEER`(ADDRESSTYPE=**ipv6**, **PEERADDRV6**=FC00::20:78,FC00::30:78, **LOCALIFADDR**=FC00::10:78)、`ADD IMPORTROUTE`(AFTYPE=**ipv6uni**)
- **配置对象**：IPv6变体的所有模板与BGP对象
- **对接面**：CS-4

**差异要点**：IPv6独立模板，掩码从27位→123位，Loopback从/32→/128，地址 FC00:: 前缀。Eth-trunk模板（VNICLIST/WORKMODE/LEASTACTLINKNUM）与IPv4**完全相同**（硬件层无IPv4/IPv6之分）。

---

### KP-10: 网络加速卡 IPv4v6 双栈路由配置 — 双模板并存

- **来源**：`配置VNF侧IP路由数据（网络加速卡, IPv4v6）_87775238.md`
- **核心度**：★★★★
- **关联特性**：同 KP-08
- **关联命令**：IPv4模板 + IPv6模板**并存**（SERVICENAME 分 `_v4`/`_v6` 后缀）
  - VPN实例：同时建 ipv4uni + ipv6uni 地址族，均配 VRFRD
  - Eth-trunk模板：**仅1个**（硬件层共享，VNICLIST/WORKMODE/LEASTACTLINKNUM 同IPv4）
  - `ADD AUTOSCALINGSERVICE` ×2（ServName_Access_100_v4 + ServName_Access_100_v6）
  - `ADD AUTOSCALINGBFD` ×2（BFD_1 模板名相同，但 DESTADDR4/DESTADDR6 分别配）
  - `ADD AUTOSCALINGSRROUTE` ×N（IPv4路由 + IPv6路由分别配）
  - Loopback：同时配 IPv4(10.10.10.78/32) + IPv6(FC00::10:78/128)，先 `SET IFIPV6ENABLE`
  - BGP：`ADD BGPVRFAF` ipv4uni+ipv6uni 各一；`ADD BGPPEER` ipv4+ipv6 各一；`ADD IMPORTROUTE` ipv4uni+ipv6uni 各一
- **配置对象**：双栈VPN实例、双服务模板、双BGP对等体
- **对接面**：CS-4

**差异要点**：双栈 = IPv4模板全套 + IPv6模板全套**叠加**；Eth-trunk硬件模板**只建1个**（共享）。调测时IPv4/IPv6独有检查**均需执行**。

---

### KP-11: 网络加速卡 BGP/MPLS VPN — AUTOSCALINGMPLS + _public_ + MP-EBGP

- **来源**：`配置VNF侧IP路由数据（网络加速卡直连DC-GW）/配置BGP_MPLS VPN（网络加速卡）_73574941.md`
- **核心度**：★★★★★
- **关联特性**：GWFD-020411 MPLS VPN、IPFD-014002 BGP、IPFD-012003 BFD、GWFD-111201 网络加速卡
- **关联命令**（★ 网络加速卡 MPLS VPN 特有/差异）：
  - MPLS全局：`SET MPLSSITE`(MPLSLSRID=10.10.10.78/MPLSENABLE=ENABLE/LDPENABLE=DISABLE)
  - **★ MPLS自动化模板（vs 手动的 ADD MPLSIF）**：`ADD AUTOSCALINGMPLS`(SERVICENAME=ServName_N6_100) ← 自动将外联口配置为MPLS接口
  - 外联口模板：`ADD AUTOSCALINGETHTRUNK`(同KP-08)、`ADD AUTOSCALINGSERVICE`(**VPNNAME=_public_** 固定值，AFTYPE=IPv4，IPALLOCTYPE4=USER_CONFIG)
  - BFD/静态路由模板：`ADD AUTOSCALINGBFD`(ONEARMECHO=TRUE)、`ADD AUTOSCALINGSRROUTE`（**两类路由**：①到BGP对等体地址 PREFIX4=10.10.20.78/10.10.30.78 /32；②默认路由 PREFIX4=0.0.0.0 MASKLENGTH=0 **PREFERENCE=255**）
  - L3VPN实例：`ADD L3VPNINST`(VRF_PDN1~5)、`ADD VPNINSTAF`(**VRFRD=100:100~500:500** 必配/VRFLABELMODE=perInstance)、`ADD VPNTARGET`(export_extcommunity+import_extcommunity/VRFRTVALUE=1:1~5:1)
  - MP-EBGP：`MOD BGPVRF`(VRFNAME=_public_/ROUTERID)、`ADD BGPVRFAF`(VRFNAME=_public_/**AFTYPE=ipv4vpn**|ipv6vpn/APPLYLABELMODE=perNexthop)、`ADD BGPPEER`(VRFNAME=_public_/ADDRESSTYPE=ipv4/PEERADDR/EBGPMAXHOP=10)、`ADD BGPPEERAF`(AFTYPE=ipv4vpn|ipv6vpn)、`ADD IMPORTROUTE`(IMPORTPROTOCOL=wlr)
  - Loopback（不绑VPN，仅IPv4）：`ADD INTERFACE`(Loopback1)/`ADD IFIPV4ADDRESS`(10.10.10.78/32)
- **配置对象**：MPLS LSR、MPLS自动化模板、L3VPN实例(VRF_PDN1~5)、VPN Target、公网BGP(_public_)、MP-EBGP对等体
- **对接面**：CS-4（OptionB跨域VPN）

**★ 网络加速卡 MPLS VPN vs 手动 MPLS VPN 核心差异**：

| 维度 | 手动 MPLS VPN（KP-05） | 网络加速卡 MPLS VPN（本KP） |
|------|----------------------|------------------------------|
| MPLS接口配置 | **`ADD MPLSIF` 逐个手动** | **`ADD AUTOSCALINGMPLS` 模板自动**（VM扩容自动适配） |
| 外联口VPN | _public_ | _public_（同） |
| Eth-trunk硬件 | ADD MPLSIF 逐个 | ADD AUTOSCALINGETHTRUNK 模板（LACP/NIC列表） |
| BGP/VPN实例/RT | 相同（MOD BGPVRF/ADD BGPVRFAF/ADD VPNTARGET） | 相同 |
| 默认路由 | 不涉及 | **ADD AUTOSCALINGSRROUTE 配 0.0.0.0/0 PREFERENCE=255** |
| 部署开关 | 不涉及 | SET AUTOCONFIG FALSE→配模板→TRUE |

---

### KP-12: IPsec 与 GRE 隧道（手动部署，与 Batch-04 命令一致）

- **来源**：`手动部署/配置IPsec_80591827.md`、`配置PGW-U_UPF与PDN_DN之间的GRE隧道_84974108.md`
- **核心度**：★★（差异极小，引用 Batch-04）
- **关联特性**：IPFD-015004 IPsec、GRE
- **关联命令**：
  - IPsec：详见特性文档 IPFD-015004（无独立MML清单，跨安全域时按需配置，如Sxa/Sxb/N4信令、S1-U/N3数据跨区域传输）
  - GRE：`ADD INTERFACE`(LoopBack1)、`ADD IPBINDVPN`(VRF_Internet)、`ADD IFIPV4ADDRESS`、`ADD NETWORKROUTE`(BGP引入Loopback路由)、`ADD GRETUNNEL`(TNLNAME=gre/gre6/SRCTYPE=if_name/SRCIFNAME=LoopBack1/DSTIPADDR)、`ADD SRROUTE`(IFNAME=Tunnel1)、`MOD GRETUNNEL`(CHECKSUMEN/KEEPALVEN/GREKEYEN)
- **配置对象**：Loopback接口、GRE Tunnel接口、隧道间静态路由
- **对接面**：CS-4（PGW-U/UPF与PDN/DN GRE VPN）

**差异要点**：与 Batch-04 自动部署的 IPsec/GRE **命令完全一致**；手动部署仅外联口基础设施层手工。GRE隧道用Loopback作源地址，MTU需≤(出接口MTU-GRE头长度)。BGP场景需 ADD NETWORKROUTE 将Loopback路由引入BGP。

---

## 3. 关键发现

### 3.1 手动部署与自动部署的本质差异
1. **协议层（OSPF/BGP/MPLS VPN）命令完全一致** —— 差异不在路由协议本身。
2. **差异集中在基础设施层**：自动部署用 `ADD AUTOSCALING*` 模板批量生成外联口/子接口/VLAN/IP/VPN绑定/BFD/静态路由；手动部署逐条MML下发。
3. **MPLS接口是关键差异点**：自动用 `ADD AUTOSCALINGMPLS`（VM扩容自动适配），手动用 `ADD MPLSIF`（逐个，扩容需手工补）。
4. **入不转板功能**（BGP场景）涉及 AUTOSCALINGBGPLF/ROUTEPOLICY/COMMUNITYFILTER 模板的增删改，是手动BGP调测的复杂点。

### 3.2 网络加速卡场景的独有特征
1. **硬件类型分叉**：NP100（100GE，有级联口P3/P4）vs NP121（400GE/200GE自适应，无级联口）—— 影响接口命名、VNICLIST、LEASTACTLINKNUM。
2. **强制 SR-IOV bonding + LACP**：无标卡选项，Eth-trunk工作模式固定 Lacp（passive），DC-GW必须active。
3. **强制单臂BFD Echo**（ONEARMECHO=TRUE），不支持双向BFD。
4. **仅支持静态路由+BFD**：不支持OSPF动态路由协议（网络加速卡直连DC-GW场景）。
5. **级联口配置（NP100多框级联必配）**：`ADD NPDIRECTCONNECTPORT` 是网络加速卡特有命令，无NP卡场景无此配置。
6. **npworkmode=1**：加速省交换场景必须为1（默认值）。
7. **不支持SDN组网**。

### 3.3 路由方案适用性矩阵
| 硬件/部署 | OSPF+BFD | 静态路由+BFD | BGP over OSPF/静态 | BGP/MPLS VPN | IPsec/GRE |
|-----------|----------|-------------|-------------------|-------------|-----------|
| 无NP卡自动（Batch-04） | ✓ | ✓ | ✓ | ✓(AUTOSCALINGMPLS) | ✓ |
| 无NP卡手动（本批次） | ✓ | ✓ | ✓ | ✓(**ADD MPLSIF**逐个) | ✓ |
| 网络加速卡（本批次） | **✗不支持** | ✓(单臂Echo) | ✓(仅静态基础) | ✓(AUTOSCALINGMPLS) | 引用Batch-04 |
| NP卡直连PE（Batch-06） | - | - | - | - | - |

### 3.4 GWFD-020161 CU Full Mesh
- 本批次16个文档**未明确提及** GWFD-020161。该特性更可能在 NP卡直连PE/MPLS 跨域场景（Batch-06）或 CU 分离组网中出现。手动部署的 BGP over OSPF/静态路由+BFD 场景中，Loopback基于eBGP邻居的建立理论上可支持Full Mesh，但文档未展开。

---

## 4. 对接面与决策点归纳

### 4.1 决策点 DP：部署方式 × 硬件类型 的命令差异矩阵

```
部署方式 (自动推荐 / 手动)
   ×
硬件类型 (无NP卡标卡 / 网络加速卡NP100 / 网络加速卡NP121)
   ×
路由协议 (OSPF+BFD / 静态路由+BFD / BGP over / BGP MPLS VPN / GRE)
   ×
IP版本 (IPv4 / IPv6 / IPv4v6双栈)
```

**关键决策分支**：

| 决策 | 选项A | 选项B | 影响命令 |
|------|-------|-------|---------|
| DP-1 部署方式 | 自动部署（推荐） | 手动部署 | AUTOSCALING*模板 vs 逐条MOD/ADD INTERFACE+ADD MPLSIF |
| DP-2 硬件类型 | 无NP卡标卡 | 网络加速卡 | Ethernet66/0/X vs 100GE*X*/0/X(NP100)/400GE*X*/0/X(NP121) |
| DP-3 网络加速卡型号 | NP100 | NP121 | VNICLIST="8 9" vs "6 7 12 13"；LEASTACTLINKNUM=1 vs 2；级联口有/无 |
| DP-4 组网bonding | 非SR-IOV bonding | SR-IOV bonding | 子接口直接 vs Eth-trunk；无NP卡Manual vs 加速卡强制Lacp |
| DP-5 路由协议 | OSPF动态 | 静态路由 | 加速卡场景仅静态；BFD双向 vs 单臂Echo(加速卡强制) |
| DP-6 IP版本 | IPv4/IPv6单栈 | IPv4v6双栈 | 单模板 vs 双模板叠加；Eth-trunk模板始终1个 |
| DP-7 MPLS VPN | 是 | 否 | ADD MPLSIF(手动)/AUTOSCALINGMPLS(自动)；VPN=_public_；VRFRD必配 |

### 4.2 网络加速卡级联口（NP100）配置要点
1. **触发条件**：多框级联组网（框0+框1）+ 实例化后级联口与规划不一致。
2. **命令**：`ADD NPDIRECTCONNECTPORT: SUBRACK=Subrack_{0|1}, SLOTID=Slot_{1~8}, PORTID=P{3|4}`
3. **连线规则**：两框对等板级联口全部直连；P3=位置3(100GE*X*/0/7)，P4=位置4(100GE*X*/0/6)。
4. **验证**：`LST NPDIRECTCONNECTPORT`；错误用 `RMV NPDIRECTCONNECTPORT` 删除重建。
5. **告警**：先连线再使能会产生 ALM-89005（不影响业务，手动清除）。
6. **NP121 不适用**（无级联口）。
7. 框0和框1都需要与DC-GW连接。

### 4.3 自动化开关操作规范（网络加速卡场景）
1. 配模板前：`SET AUTOCONFIG:SWITCHFLAG=FALSE`（关闭）
2. 查状态：`DSP OPSASSISTSTATE`（确保 autoscaling_autoconfig.py 为 Ready）
3. 配所有 AUTOSCALING* 模板
4. 开生效：`SET AUTOCONFIG:SWITCHFLAG=TRUE`
5. 再查状态：`DSP OPSASSISTSTATE`（确保 Ready 后再做其他操作）

---

## 附录：文件清单与对应KP

| # | 文件 | 对应KP |
|---|------|--------|
| 1 | 手动部署/配置动态路由OSPF+BFD组网（IPv4）_16653312.md | KP-01,02 |
| 2 | 手动部署/配置静态路由+BFD组网（IPv4）_16653313.md | KP-01,03 |
| 3 | 手动部署/配置BGP over OSPF_静态路由+BFD（IPv4）_16653300.md | KP-01,04 |
| 4 | 手动部署/配置动态路由OSPFv3+BFD组网（IPv6）_16653304.md | KP-02(IPv6) |
| 5 | 手动部署/配置静态路由+BFD组网（IPv6）_16653301.md | KP-03(IPv6) |
| 6 | 手动部署/配置BGP over OSPFv3_静态路由+BFD（IPv6）_16653302.md | KP-04(IPv6) |
| 7 | 手动部署/配置IPsec_80591827.md | KP-12 |
| 8 | 手动部署/配置PGW-U_UPF与PDN_DN之间的GRE隧道_84974108.md | KP-12 |
| 9 | 手动部署/配置BGP_MPLS VPN（非SDN_手动）_70507877.md | KP-05 |
| 10 | 配置VNF侧IP路由数据（网络加速卡直连DC-GW）_32651719.md | KP-06 |
| 11 | .../修改级联口数据（NP100）_81556318.md | KP-07 |
| 12 | .../配置VNF侧IP路由数据（网络加速卡, IPv4）_81401928.md | KP-08 |
| 13 | .../配置VNF侧IP路由数据（网络加速卡, IPv6）_32770255.md | KP-09 |
| 14 | .../配置VNF侧IP路由数据（网络加速卡, IPv4v6）_87775238.md | KP-10 |
| 15 | .../配置BGP_MPLS VPN（网络加速卡）_73574941.md | KP-11 |
| 16 | （手动部署总览并入KP-01） | - |
