# 08-IPSec 隧道接入

> 数据源：`04-command-graph.md` §1.9/1.10 + §5.7 + `feature/IPFD-015004-IPSec功能.md` + `feature/IPFD-016000-IPSec功能.md`
> 作用：Phase 3 IPSec 参数 / Phase 5 IPSec 生成（DP-APN-ACCESS-MODE=IPSec）
> **UDG + UNC 对称部署**（CS-APN-01/09）；**互斥**：GRE 源地址不能与 IPSec 源地址相同（CR-APN-12）

---

## 1. IPSec 命令族（8 + 微服务镜像 5）

### 1.1 ACL（保护数据流容器）

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD ACLGROUPIPSEC | CMD-UDG-047 | ACLGROUPNAME |
| ADD ACLRULEADV4IPSEC | CMD-UDG-048 | ACLGROUPNAME, SRCIP, DSTIP（★CR-APN-11：仅源/目的 IP，不支持端口） |

### 1.2 安全提议

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD IPSECPROPOSALIPSEC | CMD-UDG-049 | PROPOSALNAME, ENCAPSULATIONMODE(TUNNEL/TRANSPORT), SECURITYPROTOCOL(AH/ESP) |

### 1.3 IKE 提议与对等体

| 命令 | command_id | 关键参数 | 约束 |
|------|-----------|---------|------|
| ADD IKEPROPOSAL | CMD-UDG-050 | PROPOSALNAME, AUTHMETHOD(PSK), **DHGROUP** | ★CR-APN-10：DH 组不能为 None |
| ADD IKEPEER | CMD-UDG-051 | PEERNAME, PRESHAREDKEY, EXCHANGEMODE(MAIN), REMOTEADDR, NATTRAVERSAL, VERSION1 | ★默认 IKEv2（IKEv1 需 VERSION1=FALSE 关闭） |

### 1.4 安全策略（聚合 ACL + Proposal + IKE Peer）

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD IPSECPOLICY | CMD-UDG-052 | POLICYNAME, SEQ, MODE(ISAKMP), ACLGROUPNAME |
| ADD PROPATTACHIPSECPROPOSAL | CMD-UDG-053 | POLICYNAME, SEQ, PROPOSALNAME |
| ADD ATTACHIKEPEER | CMD-UDG-054 | POLICYNAME, SEQ, PEERNAME, PRIORITY |

### 1.5 应用到接口

| 命令 | command_id | 关键参数 |
|------|-----------|---------|
| ADD IPSECINTFCFGIPSEC | CMD-UDG-055 | IFNAME, TNLTYPE(IPSEC), POLICYNAME |
| SET IKEGLOBALCONFIG | CMD-UDG-056 | DPDTYPE, DPDINTERVAL, NATKLI（DPD + NAT 保活） |

### 1.6 微服务镜像（IPSec 专用 L3VPN/接口镜像）

| 命令 | command_id |
|------|-----------|
| ADD L3VPNINSTIPSEC | CMD-UDG-057 |
| ADD VPNINSTAFIPSEC | CMD-UDG-058 |
| ADD INTERFACEIPSEC | CMD-UDG-059 |
| ADD IPBINDVPNIPSEC | CMD-UDG-060 |
| ADD IFIPV4ADDRESSIPSEC | CMD-UDG-061 |

---

## 2. ADD IPSECPOLICY 参数（CMD-UDG-052，§5.7）

| 参数 | 类型 | 取值 | required_mode | 说明 |
|------|------|------|--------------|------|
| POLICYNAME | string | — | required | 策略名 |
| SEQ | int | — | required | 策略序号 |
| MODE | enum | ISAKMP | required | 模式（ISAKMP = 经 IKE 协商） |
| ACLGROUPNAME | string | — | conditional_required | 引用 ACL（ISAKMP 模式必填） |

---

## 3. 配置实例

```mml
// IPSec ACL（仅源/目的 IP）
ADD ACLGROUPIPSEC:ACLGROUPNAME="acl_ipsec1";
ADD ACLRULEADV4IPSEC:ACLGROUPNAME="acl_ipsec1",SRCIP="10.10.1.0/24",DSTIP="192.168.1.0/24";

// IPSec 安全提议
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="prop1",ENCAPSULATIONMODE=TUNNEL,SECURITYPROTOCOL=ESP;

// IKE 提议与对等体（DH 组不能为 None）
ADD IKEPROPOSAL:PROPOSALNAME="ike_prop1",AUTHMETHOD=PSK,DHGROUP=14;
ADD IKEPEER:PEERNAME="ike_peer1",PRESHAREDKEY="{psk}",EXCHANGEMODE=MAIN,REMOTEADDR="10.2.2.2",VERSION1=FALSE;

// IPSec 安全策略（聚合）
ADD IPSECPOLICY:POLICYNAME="policy1",SEQ=10,MODE=ISAKMP,ACLGROUPNAME="acl_ipsec1";
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="policy1",SEQ=10,PROPOSALNAME="prop1";
ADD ATTACHIKEPEER:POLICYNAME="policy1",SEQ=10,PEERNAME="ike_peer1",PRIORITY=10;

// 应用到 Tunnel 接口
ADD IPSECINTFCFGIPSEC:IFNAME="Tunnel1",TNLTYPE=IPSEC,POLICYNAME="policy1";
```

---

## 4. 约束（CR-APN-10/11/12，TR-APN-11）

- **IKE DH 组不能为 None**（CR-APN-10），否则 IKE 协商无法完成密钥交换
- **ACL 仅源/目的 IP，不支持端口**（CR-APN-11）
- **NAT 穿越仅 ESP 隧道模式**（CR-APN-11）
- **默认 IKEv2**，IKEv1 需 MOD IKEPEER VERSION1=FALSE 关闭（TR-APN-11）
- **GRE 源地址 ≠ IPSec 源地址**（CR-APN-12 / TR-APN-01 / BR-APN-GRE-IPSEC-SRC-EXCL）
- **UDG + UNC 对称部署**（CS-APN-01/09），两侧 IPSec 配置需一致
- **IPv6 支持**：IPSec IPv6 支持 v02 20.8.0+（CS-APN-09 双栈加密场景）

---

## 5. IPSec 双栈加密（CS-APN-09）

企业双栈加密接入场景，IPv4 + IPv6 双栈叠加 IPSec 加密：
- IPv4 POOL + IPv6 POOL 双池双段（详见 §10）
- IPSec 隧道加密 IPv4 + IPv6 双协议
- IPv6 支持需 IPSec v02 20.8.0+
