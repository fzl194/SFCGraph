# 07-GRE 隧道接入

> 数据源：`04-command-graph.md` §1.8 + §5.8 + `feature/IPFD-015002-GRE.md`
> 作用：Phase 3 GRE 参数 / Phase 5 GRE 生成（DP-APN-ACCESS-MODE=GRE 或 GRE-over-IPSec）
> **License**：无；**互斥**：GRE 源地址不能与 IPSec 源地址相同（CR-APN-12 / TR-APN-01）

---

## 1. ADD GRETUNNEL（CMD-UDG-044）

| 参数 | 类型 | 取值 | required_mode | 说明 |
|------|------|------|--------------|------|
| TNLNAME | string | — | required | 隧道名 |
| **TNLTYPE** | enum | **gre** | required | 隧道类型 |
| SRCTYPE | enum | if_name / ... | required | 源类型（推荐 LoopBack 接口） |
| SRCIFNAME | string | 如 LoopBack1 | conditional_required | 源接口名（SRCTYPE=if_name 时必填） |
| **DSTIPADDR** | IPv4 | — | required | 目的 IP（★CR-APN-12：不能与 IPSec 源地址相同） |

### MOD GRETUNNEL（CMD-UDG-045，可选特性）

| 参数 | 说明 |
|------|------|
| CHECKSUMEN | 校验和使能 |
| GREKEYEN / GREKEY | GRE Key 使能/值 |
| KEEPALVEN / KEEPALVPERIOD / KEEPALVRETRYCNT | Keepalive 使能/周期/重试 |

---

## 2. 源接口（LoopBack，推荐）

```mml
ADD INTERFACE:IFNAME="LoopBack1";
ADD IPBINDVPN:IFNAME="LoopBack1",VPNINSTNAME="{vpn}";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="{src_ip}",SUBNETMASK="255.255.255.255";
```

---

## 3. 静态路由引导流量进 Tunnel

```mml
ADD SRROUTE:AFTYPE=ipv4,PREFIX="{dst_prefix}",MASKLENGTH={masklen},IFNAME="{gre_tnl}";
```

IPv6 用 `ADD SRROUTE6`（CMD-UDG-043-2）。

---

## 4. GRE over IPSec 场景

- 先建 GRE 再叠加 IPSec
- **GRE 源地址 ≠ IPSec 源地址**（CR-APN-12 / TR-APN-01）
- 用不同 LoopBack 接口分离源地址（如 LoopBack1 给 GRE，LoopBack2 给 IPSec）

---

## 5. 静态路由冗余（GWFD-010107 + WSFD-107021，对称同构）

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD REDUNDRDTIP | CMD-UDG-075 | REDUNDRDTIP（虚拟 IP，重定向业务流到 GRE Tunnel） |
| SET REDUNDUSER | CMD-UDG-076 / CMD-UNC-084 | SWITCH（★U+C 共用对象，与 ADD POOL REDUNDFUNC 双使能） |
| SET APNREDUNDUPSW | CMD-UDG-077 | APN, SWITCH（仅备用 UDG） |
| ADD OSPFINTERFACE | CMD-UDG-078 | PROCID, IFNAME（主备 UDG 路由互通） |
| MOD OSPFIMPORTROUTE / MOD IMPORTROUTE | CMD-UDG-079 | PROCID, COST, MED（路由引入优先级） |

---

## 6. 配置实例

```mml
// GRE 源接口
ADD INTERFACE:IFNAME="LoopBack1";
ADD IPBINDVPN:IFNAME="LoopBack1",VPNINSTNAME="vpn1";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.1.1.1",SUBNETMASK="255.255.255.255";

// GRE 隧道
ADD GRETUNNEL:TNLNAME="gre1",TNLTYPE=gre,SRCTYPE=if_name,SRCIFNAME="LoopBack1",DSTIPADDR="10.2.2.2";

// 静态路由引导
ADD SRROUTE:AFTYPE=ipv4,PREFIX="192.168.0.0",MASKLENGTH=16,IFNAME="gre1";
```

---

## 7. 约束

- **GRE 与 IPSec 源地址互斥**（CR-APN-12 / TR-APN-01 / BR-APN-GRE-IPSEC-SRC-EXCL）
- **GRE 嵌套限制**：最多两层嵌套，超过两层隧道状态变 Down
- **规格**：最大 4k 个隧道
- **特性**：仅封装不加密，性能开销低
- **LoopBack 推荐**：GRE 源接口推荐 LoopBack（接口稳定）
