---
id: ConfigurationSolution@apn-tunnel
type: ConfigurationSolution
name: 隧道接入
domain: apn-domain
scenario: apn-access
status: draft
---

# 隧道接入

> 把 UE 流量通过隧道送到企业 DN 的完整配置链路，覆盖 5 种接入方式（VPN 直通 / GRE / IPSec / L2TP / MPLS VPN）。属于 [APN 接入与会话管理](business/apn-domain/NetworkScenario@apn-access.md) 场景。编排 UNC 4 + UDG 4 = 8 核心 feature。
>
> **方案角色**：可选（NS DP-3 实现，5 选 1；**VPN 直通 = 不启本 CS**——这是唯一"隐式不启"的设计）。与 [CS-1 地址分配](business/apn-domain/ConfigurationSolution@apn-addr-allocation.md) / [CS-2 鉴权](business/apn-domain/ConfigurationSolution@apn-auth.md) / [CS-4 IP 类型](business/apn-domain/ConfigurationSolution@apn-ip-typing.md) 是 **AND 关系**。

## 概览

隧道接入是 APN 业务域的"送到企业 DN"环节：当 UE 流量目标不是普通 Internet，而是企业内网 / 分支 / 运营商网络，需要通过隧道封装。

5 维度的接入方式决策：

| 接入方式 | 性能 | 安全 | 适用 |
|---|---|---|---|
| **VPN 直通**（隐式默认）| 最优 | 最低 | 普通 Internet 访问，无需隧道 |
| **GRE 隧道** | 中 | 低（仅封装）| 企业 DN + 公网可达 |
| **IPSec 隧道** | 中 | 最高（加密 + 认证）| 企业 DN + 公网 + 加密需求 |
| **L2TP 隧道** | 中 | 中 | 远程办公 / 分支接入 |
| **MPLS VPN** | 高（运营商级）| 中 | 跨域运营商 VPN |

> **关键洞察**："VPN 直通"是**默认隐式选项**——选 VPN 直通 = **不启本 CS**（不需要任何隧道配置）。其他 4 种才需要启用本 CS 编排对应的隧道命令。

跨网元协同：UDG（UPF 隧道封装）+ UNC（SMF 隧道参数管理）通过 N4 PFCP 消息 + 隧道配置同步。

## 配置与协同

### 特性关系矩阵

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UNC GRE 2-00029](task/UNC/20.15.2/2-00029.md) | 核心（方案主体·GRE）| 必选（选 GRE 时）| 企业 DN 接入 + 公网封装 |
| [UNC IPSec 2-00030](task/UNC/20.15.2/2-00030.md) | 核心（方案主体·IPSec）| 必选（选 IPSec 时）| 企业 DN + 公网 + 加密 |
| [UNC L2TP VPN 2-00020](task/UNC/20.15.2/2-00020.md) | 核心（方案主体·L2TP）| 必选（选 L2TP 时）| 远程办公 / 分支；含 LNS 模式（与 [CS-1 地址分配](business/apn-domain/ConfigurationSolution@apn-addr-allocation.md) 核心重叠）|
| [UNC MPLS VPN 2-00031](task/UNC/20.15.2/2-00031.md) | 核心（方案主体·MPLS VPN）| 必选（选 MPLS VPN 时）| 跨域运营商 VPN |
| [UDG IPSec 功能 2-00027](task/UDG/20.15.2/2-00027.md) | 跨网元对端（IPSec）| 必选（选 IPSec 时）| U 面对称 IPSec |
| [UDG IPSec 可靠性 2-00028](task/UDG/20.15.2/2-00028.md) | 跨网元对端（IPSec 可靠性）| 可选 | IPSec SA 备份 / DPD |
| [UDG IPSec 客户端 2-00029](task/UDG/20.15.2/2-00029.md) | 跨网元对端（IPSec Client）| 必选（选 IPSec 时）| U 面对称 |
| [UDG IPSec over GRE 2-00012](task/UDG/20.15.2/2-00012.md) | 跨网元对端（IPSec+GRE 组合）| 可选 | 加密 + 封装双层 |
| **[UNC 会话管理 2-00014](task/UNC/20.15.2/2-00014.md)** | **基础（依赖前提）** | **必配** | 隧道会话在 PDU/PDN/PDP 会话基础上建立——**配隧道时已隐含** |
| **[UNC UPF 选择 2-00033](task/UNC/20.15.2/2-00033.md)** | **基础（依赖前提）** | **必配** | 隧道端点选哪个 UPF——配隧道时已隐含 |

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**。

### UNC 控制面：4 种隧道（[2-00029](task/UNC/20.15.2/2-00029.md) / [2-00030](task/UNC/20.15.2/2-00030.md) / [2-00020](task/UNC/20.15.2/2-00020.md) / [2-00031](task/UNC/20.15.2/2-00031.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**：

- **GRE 隧道**（[2-00029](task/UNC/20.15.2/2-00029.md)）：
  - `ADD GRETUNNEL` + `ADD IFIPV4ADDRESS` + `ADD SRROUTE`（3 步）
  - 可选增强：`MOD GRETUNNEL: CHECKSUMEN=TRUE / GREKEYEN=TRUE / KEEPALVEN=TRUE`
  - 排除：IPSec over GRE 时用 [2-00012](task/UDG/20.15.2/2-00012.md)
- **IPSec 隧道**（[2-00030](task/UNC/20.15.2/2-00030.md)）：
  - `ADD IKEPEER` + `ADD IPSECPROPOSAL` + `ADD IPSECPOLICY` + `ADD IPSECTUNNEL`（4 步）
  - IKEv2 + ESP + PSK（默认）；或证书认证
- **L2TP 隧道**（[2-00020](task/UNC/20.15.2/2-00020.md)）：
  - `ADD APN` + `SET APNL2TPATTR`（含 LNS IP / NAME / PWD / 隧道密码）
  - 与 [CS-1 地址分配](business/apn-domain/ConfigurationSolution@apn-addr-allocation.md) LNS 模式核心重叠
- **MPLS VPN**（[2-00031](task/UNC/20.15.2/2-00031.md)）：
  - `ADD L3VPNINST` + `ADD VPNINSTAF` + `ADD VPNINST` + `ADD IPBINDVPN` + `ADD LOGICIP/INF`
  - 跨域 VPN 需 perNexthop 配套
- **排除** `MOD GTPU`（隧道不属 GTP-U 范畴）
- **排除** `MOD N4CHGMSGCTRL`（5G N4 不是隧道范畴）

### UDG 用户面：UDG 端隧道（[2-00027](task/UDG/20.15.2/2-00027.md) / [2-00028](task/UDG/20.15.2/2-00028.md) / [2-00029](task/UDG/20.15.2/2-00029.md) / [2-00012](task/UDG/20.15.2/2-00012.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**：

- **IPSec 对端**（[2-00027](task/UDG/20.15.2/2-00027.md)）：与 UNC 2-00030 对称
- **IPSec 可靠性**（[2-00028](task/UDG/20.15.2/2-00028.md)）：SA 备份 / DPD 探测
- **IPSec 客户端**（[2-00029](task/UDG/20.15.2/2-00029.md)）：U 面 IPSec 客户端模式
- **IPSec over GRE**（[2-00012](task/UDG/20.15.2/2-00012.md)）：双层封装
- **排除** `MOD UPNODE`（隧道不直接改 UPF 节点）

### 跨网元/跨特性协同

- **顺序**：
  1. UNC 侧隧道基础（LoopBack + Tunnel 接口 + 路由）就绪
  2. UNC 触发 UDG 侧隧道配置（N4 PFCP + 隧道配置同步）
  3. UE 流量经 UPF 封装通过隧道到企业 DN
- **与其他 CS 的协同**（AND 关系）：
  - 与 [CS-1 地址分配](business/apn-domain/ConfigurationSolution@apn-addr-allocation.md)：L2TP/LNS 模式时核心重叠
  - 与 [CS-2 鉴权](business/apn-domain/ConfigurationSolution@apn-auth.md)：企业 AAA 模式常配合 IPSec/L2TP
  - 与 [CS-4 IP 类型](business/apn-domain/ConfigurationSolution@apn-ip-typing.md)：双栈时隧道需 IPv4+IPv6 双协议栈支持
- **License 链**：无强制 License（GRE/IPSec 通用）
- **GRE 嵌套限制**（warning）：最多 2 层嵌套，超过 3 层状态变 Down

> **方案优先复用已有 compound**：[1-00027](task/UNC/20.15.2/1-00027.md) / [1-00029](task/UNC/20.15.2/1-00029.md)，**不新建 atom/compound**。

## 决策点

### DP-1：接入方式（5 选 1，可选——VPN 直通 = 不启本 CS）

| 选项 | 涉及命令 | 适用 |
|---|---|---|
| **VPN 直通** | **不启本 CS** | 普通 Internet 访问，UPF 直接 NAT 转发 |
| **GRE 隧道** | [2-00029](task/UNC/20.15.2/2-00029.md) | 企业 DN + 公网可达 + 无加密需求 |
| **IPSec 隧道** | [2-00030](task/UNC/20.15.2/2-00030.md) + UDG [2-00027/28/29](task/UDG/20.15.2/2-00027.md) | 企业 DN + 公网 + 加密 |
| **L2TP 隧道** | [2-00020](task/UNC/20.15.2/2-00020.md) | 远程办公 / 分支接入 |
| **MPLS VPN** | [2-00031](task/UNC/20.15.2/2-00031.md) | 跨域运营商 VPN |

## 约束

- **5 选 1 接入方式**（critical）：同一 APN 不可同时配 2 种隧道（VPN 直通除外）
- **VPN 直通 = 不启本 CS**（critical）：普通 Internet 访问不需要任何隧道配置
- **跨网元一致性**（critical）：UNC 端隧道参数与 UDG 端对称
- **GRE 嵌套限制**（warning）：最多 2 层嵌套
- **与其他 CS 协同**（critical）：与 [CS-1 地址分配](business/apn-domain/ConfigurationSolution@apn-addr-allocation.md) / [CS-2 鉴权](business/apn-domain/ConfigurationSolution@apn-auth.md) / [CS-4 IP 类型](business/apn-domain/ConfigurationSolution@apn-ip-typing.md) 严格顺序

## 关联

- **上游场景**：[NS APN 接入与会话管理](business/apn-domain/NetworkScenario@apn-access.md)
- **下游（同场景其他 CS，AND 关系）**：
  - [CS 地址分配](business/apn-domain/ConfigurationSolution@apn-addr-allocation.md) — L2TP/LNS 模式核心重叠
  - [CS 鉴权 AAA](business/apn-domain/ConfigurationSolution@apn-auth.md)
  - [CS IP 类型治理](business/apn-domain/ConfigurationSolution@apn-ip-typing.md) — 双栈时隧道需双协议栈
- **编排特性**：见上文"特性关系矩阵"段（8 核心 + 2 基础 = 10 feature）
- **共享骨架**：[1-00027 终端二次鉴权](task/UNC/20.15.2/1-00027.md)（含 GRE 隧道族）/ [1-00029 OSPF 路由发布](task/UNC/20.15.2/1-00029.md)
