# 11-VPN 实例与路由发布

> 数据源：`04-command-graph.md` §1.2/1.6/1.7 + `feature/GWFD-010105-用户面地址分配.md` §4.2.5
> 作用：Phase 3 VPN/接口/路由参数 / Phase 5 VPN 与下行路由生成

---

## 1. VPN 实例族（UDG）

| 命令 | command_id | 关键参数 | 用途 |
|------|-----------|---------|------|
| ADD VPNINST | CMD-UDG-003 | VPNINSTANCE | VPN 实例（IPv4 地址分配/隧道承载基础） |
| ADD L3VPNINST | CMD-UDG-004 | VRFNAME | L3VPN 实例（VRF） |
| ADD VPNINSTAF | CMD-UDG-005 | VRFNAME, AFTYPE(ipv4uni/ipv6uni) | VPN 地址族（★IPv6/双栈必须 ipv6uni，CR-APN-06） |
| ADD IPBINDVPN | CMD-UDG-007 | IFNAME, VPNINSTNAME | 接口绑定 VPN |
| ADD LOGICINF | CMD-UDG-008 | IFNAME | Giif 逻辑接口（L2TP 源端绑定） |

---

## 2. 接口 IP

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD INTERFACE | CMD-UDG-006 | IFNAME（物理/逻辑接口，Tunnel/LoopBack） |
| ADD IFIPV4ADDRESS | CMD-UDG-040 | IFNAME, IFIPADDR, SUBNETMASK |
| ADD IFIPV6ADDRESS | CMD-UDG-041 | IFNAME, IFIPV6ADDR, PREFIXLENGTH |
| SET IFIPV6ENABLE | CMD-UDG-042 | IFNAME, SWITCH（IPv6 接口使能） |

---

## 3. 静态路由

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD SRROUTE | CMD-UDG-043-1 | AFTYPE, PREFIX, MASKLENGTH, IFNAME（IPv4） |
| ADD SRROUTE6 | CMD-UDG-043-2 | AFTYPE, PREFIX, MASKLENGTH, IFNAME（IPv6） |

---

## 4. OSPF / OSPFv3（下行路由发布）

### 4.1 IPv4 OSPF

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD OSPF | CMD-UDG-032 | PROCID, ROUTERID, VRFNAME |
| ADD OSPFAREA | CMD-UDG-033 | PROCID, AREAID |
| ADD OSPFNETWORK | CMD-UDG-034 | PROCID, AREAID, NETWORK |
| **ADD OSPFIMPORTROUTE** | CMD-UDG-035 | PROCID, PROTOCOL(**wlr**) — ★引入 WLR 用户路由 |
| ADD ROUTEPOLICY / ROUTEPOLICYNODE / MATCHROUTETYPE | CMD-UDG-039 | 路由策略（IPv6 场景） |

### 4.2 IPv6 OSPFv3（IPv6 承载链必需）

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD OSPFV3 | CMD-UDG-036 | PROCID, ROUTERID |
| ADD OSPFV3AREA | CMD-UDG-037 | PROCID, AREAID |
| **ADD OSPFV3IMPORTROUTE** | CMD-UDG-038 | PROCID, PROTOCOL(wlr) — ★引入 WLR 到 OSPFv3 |

---

## 5. 配置实例（IPv4 OSPF 引入 WLR）

```mml
ADD OSPF:PROCID=100,VRFNAME="vpn1",SCHEMAROUID="10.10.10.1",LSAARRMAXINTV=1000,LSAARRSTARINTV=500,LSAARRHLDINTV=500;
ADD OSPFAREA:PROCID=100,AREAID="0.0.0.0";
ADD OSPFNETWORK:PROCID=100,AREAID="0.0.0.0",IPADDRESS="10.13.21.0",WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE:PROCID=100,TOPOID=0,PROTOCOL=wlr;
```

> 来源：`feature/GWFD-010105-用户面地址分配.md` §5.1

---

## 6. 约束

- **VPN 三者一致**：POOL VPN = APN VPN = Gi/SGi/N6 外联口 VPN（CR-APN-07 / GWFD-010105 §4.5）
- **OSPF Router ID 全网唯一**（SCHEMAROUID）
- **引入 WLR 路由**：PROTOCOL=wlr 是用户路由引入的关键参数（下行发布 UE 主机路由）
- **IPv6 承载链必需 OSPFv3**（与 IPv4 OSPF 独立进程）
- **VPNINSTAF AFTYPE=ipv6uni**：IPv6/双栈必须额外激活（CR-APN-06）
