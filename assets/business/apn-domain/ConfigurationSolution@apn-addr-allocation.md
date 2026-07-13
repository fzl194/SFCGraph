---
id: ConfigurationSolution@apn-addr-allocation
type: ConfigurationSolution
name: 地址分配
domain: apn-domain
scenario: apn-access
status: draft
---

# 地址分配

> 为 UE 分配 IP 地址的完整配置链路，覆盖 6 种地址分配方式（UPF/SMF/UDM/Radius/DHCP/LNS）× 3 种地址类型（IPv4/IPv6/双栈）的全 18 格矩阵。属于 [APN 接入与会话管理](NetworkScenario@apn-access.md) 场景。编排 UNC 5 + UDG 6 = 11 核心 feature。
>
> **方案角色**：核心（必选）——任何 APN 方案都必须启用本方案。与 [CS-2 鉴权](ConfigurationSolution@apn-auth.md) / [CS-3 隧道](ConfigurationSolution@apn-tunnel.md) / [CS-4 IP 类型](ConfigurationSolution@apn-ip-typing.md) 是 **AND 关系**（4 CS 同时启用，非互斥）。

## 概览

地址分配是 APN 业务域的核心链路：在 UE 鉴权通过后，SMF/PGW-C/SGSN 根据配置决策"为该 UE 分配哪个 IP、用什么方式分配、什么类型"，并通过 N4/PFCP（5G）/Gz-Gn（4G）消息通知 UPF 执行实际分配。

4 维度的地址分配决策：

```
维度 1（地址分配方式）：6 种
├─ UPF 本地分配（4 子方式）：基于 APN/DNN / 基于 SMF / 基于位置区 / Radius 下发池名
├─ SMF 本地分配（控制面独立池）
├─ UDM 静态签约分配（Framed-IP）
├─ Radius 下发分配（Framed-Pool）
├─ DHCP 代理（DHCPv4 / DHCPv6）
└─ LNS 分配（L2TP 隧道 PPP 协商）

维度 2（地址类型）：3 种
├─ IPv4
├─ IPv6
└─ IPv4v6 双栈

→ 6 × 3 = 18 格矩阵（全可填，但受 License 与互斥约束限制）
```

跨网元协同骨架：

| 决策/执行 | UNC（C 面：SMF/PGW-C/AMF/SGSN/MME）| UDG（U 面：UPF/PGW-U）|
|---|---|---|
| **地址分配方式决策** | [2-00015](task/UNC/20.15.2/2-00015.md) 4 选 1 + [2-00016](task/UNC/20.15.2/2-00016.md) ALLOCPRECEDENCE | [2-00021](task/UDG/20.15.2/2-00021.md) 执行 C 面指示 |
| **能力协商** | 发起 N4 PFCP Association Setup | 响应 ADUP=1（恒定）|
| **地址类型指示** | PFCP Session Est Req 携带 CHV4/CHV6/V4/V6 | 按真值表执行 |
| **地址池名下发** | Radius→SMF→UPF（Framed-Pool）| [2-00038](task/UDG/20.15.2/2-00038.md) 解析池名 |
| **位置信息透传** | PFCP 携带 LAC/TAC | [2-00036](task/UDG/20.15.2/2-00036.md) 匹配位置池组 |

## 配置与协同

### 特性关系矩阵（★必填——回答"哪些必配 / 可选 / 包含 / 正交"）

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UNC 地址分配方式 2-00015](task/UNC/20.15.2/2-00015.md) | 核心（方案主体·主特性）| 必配 | 4 选 1 决策源（UDM/Radius/SMF 本地/DHCP）；与 [2-00016](task/UNC/20.15.2/2-00016.md) ALLOCPRECEDENCE 决定 SMF 还是 UPF 决策 |
| [UNC 控制面地址分配 2-00016](task/UNC/20.15.2/2-00016.md) | 核心（主特性配套）| 必配 | SMF 独立地址池；ALLOCPRECEDENCE 选 SMF 优先还是 UPF 优先——与 [2-00015](task/UNC/20.15.2/2-00015.md) 配合 |
| [UNC DHCPv4 2-00021](task/UNC/20.15.2/2-00021.md) | 维度增强（DHCP 模式）| 可选 | DHCPv4 分配方式时必配；UNC 仅做 DHCP 代理，server 在外部 |
| [UNC DHCPv6 2-00022](task/UNC/20.15.2/2-00022.md) | 维度增强（DHCPv6 模式）| 可选 | IPv6 / 双栈 DHCPv6 分配时必配；同上 |
| [UNC L2TP/LNS 2-00020](task/UNC/20.15.2/2-00020.md) | 维度增强（L2TP/LNS 模式）| 可选 | 企业 L2TP 场景；含地址分配 LNS 模式（与 [CS-3 隧道](ConfigurationSolution@apn-tunnel.md) 核心重叠，配隧道时已含 LNS 分配）|
| [UDG 用户面地址分配主特性 2-00021](task/UDG/20.15.2/2-00021.md) | 跨网元对端 | 必配（任何 UNC 侧方式都需 UDG 配合）| UNC 决策后 UDG 执行；含 UPF 地址池 + 路由发布 |
| [UDG 基于 APN_DNN 分配 2-00034](task/UDG/20.15.2/2-00034.md) | 跨网元对端（UPF 子方式 1）| 可选（按子方式）| 4 子方式中最常用；POOLTYPE=LOCAL |
| [UDG 基于 SMF 分配 2-00035](task/UDG/20.15.2/2-00035.md) | 跨网元对端（UPF 子方式 2）| 可选 | CU Full-Mesh 组网；SMF 选 UPF |
| [UDG 基于位置分配 2-00036](task/UDG/20.15.2/2-00036.md) | 跨网元对端（UPF 子方式 3）| 可选 | 按 LAC/TAC 匹配池组；区域化运营 |
| [UDG Radius 下发池名 2-00038](task/UDG/20.15.2/2-00038.md) | 跨网元对端（UPF 子方式 4）| 可选 | 解析 Framed-Pool 字符串 |
| [UDG 用户面地址自动检测 2-00021](task/UDG/20.15.2/2-00021.md)（运维）| 维度增强（可选）| 可选 | STR PDNROUTETST / STP / DSP PDNTSTRESULT 探测 |
| **[UNC 会话管理 2-00014](task/UNC/20.15.2/2-00014.md)** | **基础（依赖前提）** | **必配（能力底座）**| PDU/PDN/PDP 会话宿主；地址分配结果写入会话上下文——**配地址分配时已隐含**（配置不重叠）|
| **[UNC UPF 选择 2-00033](task/UNC/20.15.2/2-00033.md)** | **基础（依赖前提）** | **必配** | UPF 选哪个的决策；地址分配与 UPF 选择耦合（不同 UPF 实例有不同地址池）——配置不重叠（UPF 选实例，地址分配选池）|
| **[UNC 用户数据管理 2-00036](task/UNC/20.15.2/2-00036.md)** | **基础（依赖前提）** | **必配** | UDM/HLR/HSS 签约数据管理；UDM 静态分配时强依赖——配置与核心部分重叠（UDM 签约时已含 IP）|
| **[UNC 别名 APN 2-00032](task/UNC/20.15.2/2-00032.md)** | **基础（APN 实例化）** | **必配（用别名 APN 时）**| 原 APN 映射为另一名；地址分配按别名寻池 |
| **[UNC 多 PDN_PDU 2-00035](task/UNC/20.15.2/2-00035.md)** | **基础（APN 业务）** | **必配** | 一 APN 允许多 PDN/PDU 会话；地址分配需支持并发——配置与核心部分重叠（多 PDN 时核心多轮分配）|
| **[UNC 接入控制 2-00034](task/UNC/20.15.2/2-00034.md)** | **基础（依赖前提）** | **必配（License LKV2USRAC01）**| 接入控制决策；未通过不触发地址分配——配置不重叠 |
| **[UNC 位置区域网元选择 2-00037](task/UNC/20.15.2/2-00037.md)** | **基础（依赖前提）** | **可选（按 UPF 子方式）**| UPF 基于位置选择 2-00036 选型时必配 |

> **矩阵规则**（按 [业务层级构建SOP.md §4.1 特性关系矩阵规则](business/业务层级构建SOP.md)）：
> - ①**核心**=方案主体（必配）
> - ②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）
> - ③**维度增强**=正交维度可选叠加
> - ④**跨网元对端**=另一网元对应特性（组合关系）
> - **配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UNC 控制面：地址分配方式（[2-00015](task/UNC/20.15.2/2-00015.md) + [2-00016](task/UNC/20.15.2/2-00016.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**（地址分配独有）：

- **ALLOCPRECEDENCE 决策**（[2-00016](task/UNC/20.15.2/2-00016.md) §配置维度 1）：SMF 优先 vs UPF 优先
  - SMF 优先：SMF 选 UPF 并分配（CU Full-Mesh）
  - UPF 优先：UPF 自主分配（典型 4G）
- **UDM 静态分配特有**：[2-00015](task/UNC/20.15.2/2-00015.md) POOLTYPE=UDM + CHECKIPVALID=Enable + HASVPN=Enable；需 UDM 签约 Framed-IP
- **Radius 下发分配特有**：[2-00015](task/UNC/20.15.2/2-00015.md) 接收 Framed-Pool；需先配 [CS-2 鉴权](ConfigurationSolution@apn-auth.md) Radius 完整
- **DHCP 代理特有**：[2-00021/22](task/UNC/20.15.2/2-00021.md) 仅做 DHCP 代理，server 在外部
- **L2TP/LNS 分配特有**：[2-00020 L2TP](task/UNC/20.15.2/2-00020.md) APNL2TPATTR + IPV4ALLOCTYPE=LNS；与 [CS-3 隧道](ConfigurationSolution@apn-tunnel.md) 核心重叠
- **排除** `SET UPFGRPTYPE`（SMF 优先时无需 UPF 组配置）
- **排除** `ADD NGMMPROCTRL`（5G NGMM 不是地址分配范畴）

### UDG 用户面：地址分配 4 子方式 + 主特性（[2-00021 UDG 主特性](task/UDG/20.15.2/2-00021.md) + [2-00034/35/36/38](task/UDG/20.15.2/2-00034.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**（UDG 地址分配独有）：

- **基于 APN_DNN 分配**（[2-00034](task/UDG/20.15.2/2-00034.md)）：POOLTYPE=LOCAL，按 APN 业务类型分池——**最常用**
- **基于 SMF 分配**（[2-00035](task/UDG/20.15.2/2-00035.md)）：CU Full-Mesh，SMF 选 UPF
- **基于位置分配**（[2-00036](task/UDG/20.15.2/2-00036.md)）：LAC/TAC 匹配池组
- **Radius 下发池名**（[2-00038](task/UDG/20.15.2/2-00038.md)）：解析 Framed-Pool 字符串
- **地址自动检测**（[2-00021 运维](task/UDG/20.15.2/2-00021.md)）：STR PDNROUTETST / STP / DSP PDNTSTRESULT——可选
- **排除** `MOD RULENAME`（地址分配不涉及规则名）
- **排除** `MOD PCCPOLICYGRP`（属业务感知域）

### 跨网元/跨特性协同

- **C-U 决策执行分离**（[业务层级构建SOP.md §1.3 C-U 决策执行分离](business/业务层级构建SOP.md)）：
  - UNC 决策地址分配方式 → N4 PFCP → UDG 执行
  - 真值表：CHV4/CHV6/V4/V6 信元控制 U 面是否本地分配
- **顺序**：
  1. UNC 侧地址池体系（[1-00020](task/UNC/20.15.2/1-00020.md)）+ APN 基础信息（[1-00024](task/UNC/20.15.2/1-00024.md)）先就绪
  2. UNC 决策地址分配方式 + [CS-2 鉴权](ConfigurationSolution@apn-auth.md)
  3. UDG 侧地址池 + 路由发布（[1-00029](task/UNC/20.15.2/1-00029.md)）就绪
  4. UE 附着触发地址分配：N4 PFCP Session Establishment
  5. UDG 分配并通过 N4 响应返回地址给 SMF
- **一致性约束**：APN 名 / 地址池名 / UPF 实例名 / N4 PFCP Node ID 跨网元严格一致
- **License 依赖链**（[业务层级构建SOP.md §1.3 C-U 决策执行分离](business/业务层级构建SOP.md)）：IPv6 完整承载需线性 License 链——**不可按命名规律推断**
- **与其他 CS 的协同**（AND 关系）：
  - 与 [CS-2 鉴权](ConfigurationSolution@apn-auth.md)：Radius 下发模式时，Radius 链路必须先就绪
  - 与 [CS-3 隧道](ConfigurationSolution@apn-tunnel.md)：L2TP/LNS 模式时，隧道必须先就绪
  - 与 [CS-4 IP 类型](ConfigurationSolution@apn-ip-typing.md)：IPv6 / 双栈时，IP 类型 License 必须先就绪

> **方案优先复用已有 compound**：[1-00020](task/UNC/20.15.2/1-00020.md) / [1-00024](task/UNC/20.15.2/1-00024.md) / [1-00029](task/UNC/20.15.2/1-00029.md)，**不新建 atom/compound**。

## 决策点

### DP-1：地址分配方式（6 选 1，必选）

| 选项 | UNC | UDG | 适用场景 |
|---|---|---|---|
| **UPF 本地分配** | [2-00015](task/UNC/20.15.2/2-00015.md) POOLTYPE=LOCAL | [2-00034/35/36/38](task/UDG/20.15.2/2-00034.md) | 多数 4G/5G 场景 |
| **SMF 本地分配** | [2-00015](task/UNC/20.15.2/2-00015.md) + [2-00016](task/UNC/20.15.2/2-00016.md) ALLOCPRECEDENCE=SMF | UDG 接收外部地址 | CU 分离 C 面完全控制 |
| **UDM 静态签约** | [2-00015](task/UNC/20.15.2/2-00015.md) POOLTYPE=UDM + CHECKIPVALID=Enable | UDG 接收外部地址 | 工控/IoT 固定 IP |
| **Radius 下发** | [2-00015](task/UNC/20.15.2/2-00015.md) 接收 Framed-Pool | [2-00038](task/UDG/20.15.2/2-00038.md) 解析池名 | 企业 AAA 模式 |
| **DHCP 代理** | [2-00021/22](task/UNC/20.15.2/2-00021.md) DHCP 代理 | UDG 透传 | 传统企业网络迁移 |
| **L2TP/LNS 分配** | [2-00020](task/UNC/20.15.2/2-00020.md) LNS 模式 | LNS PPP 协商 | 企业 L2TP VPN |

### DP-2：UDG UPF 子方式（4 选 1，选 UPF 本地时再选）

| 选项 | 池组映射 | 适用 |
|---|---|---|
| **基于 APN/DNN**（[2-00034](task/UDG/20.15.2/2-00034.md)）| ADD POOLGRPMAP: APN | 多数场景（按业务类型分池）|
| **基于 SMF**（[2-00035](task/UDG/20.15.2/2-00035.md)）| SET IPALLOCRULE: SMF-1 | CU Full-Mesh |
| **基于位置**（[2-00036](task/UDG/20.15.2/2-00036.md)）| ADD POOLGRPMAP: LOCATION | 区域化运营 |
| **Radius 下发池名**（[2-00038](task/UDG/20.15.2/2-00038.md)）| 解析 Framed-Pool | 企业 AAA |

### DP-3：地址类型（3 选 1，与 [CS-4 IP 类型](ConfigurationSolution@apn-ip-typing.md) 协同）

| 选项 | UNC | UDG | License |
|---|---|---|---|
| **IPv4** | 不启 IPv6 承载 | 不启 IPv6 承载 | 无 |
| **IPv6** | [2-00018](task/UNC/20.15.2/2-00018.md) | [2-00041](task/UDG/20.15.2/2-00041.md) | LKV3G5V6PB01 |
| **双栈** | [2-00017](task/UNC/20.15.2/2-00017.md) | [2-00043](task/UDG/20.15.2/2-00043.md) | LKV3G5VDSA01 |

## 约束

- **6 选 1 地址分配方式**（critical）：同一 APN 不可同时配 2 种分配方式
- **跨网元一致性**（critical）：APN 名 / 地址池名 / UPF 实例名 / N4 PFCP Node ID 严格一致
- **决策与执行分离**（critical）：UNC 决策 → N4 PFCP → UDG 执行
- **License 完整性**（critical）：IPv6 / 双栈场景需完整 License 链
- **DHCP 外部依赖**（critical）：DHCP server 在外部
- **L2TP/LNS 外部依赖**（critical）：LNS server 在外部
- **地址池段数限制**（warning）：本地地址池最多 64 段
- **配置后必须配地址段**（critical）：配 ADDRPOOL 后必须 ADD SECTION
- **路由发布时序**（warning）：OSPF 需在用户面配置后 60s 生效
- **与 NS 4 DP 协同**（critical）：本方案是 NS DP-1 的实现，配置时必须确认 DP-2/3/4 也已就绪

## 关联

- **上游场景**：[NS APN 接入与会话管理](NetworkScenario@apn-access.md) — 本 CS 所属场景
- **下游（同场景其他 CS，AND 关系）**：
  - [CS 鉴权 AAA](ConfigurationSolution@apn-auth.md) — NS DP-2 实现（地址分配前需鉴权）
  - [CS 隧道接入](ConfigurationSolution@apn-tunnel.md) — NS DP-3 实现（L2TP/LNS 时核心重叠）
  - [CS IP 类型治理](ConfigurationSolution@apn-ip-typing.md) — NS DP-4 实现
- **编排特性**：见上文"特性关系矩阵"段（11 核心 + 7 基础 = 18 feature）
- **共享骨架**：[1-00020 SMF 地址池体系](task/UNC/20.15.2/1-00020.md) / [1-00024 APN 接入域基础设施](task/UNC/20.15.2/1-00024.md) / [1-00029 OSPF 路由发布](task/UNC/20.15.2/1-00029.md)
- **业务层 SOP**：[业务层级构建SOP.md](business/业务层级构建SOP.md) §4.2 CS 模板 + §4.1 特性关系矩阵规则
- **业务层审视**：[业务层级wiki审视流程.md](business/业务层级wiki审视流程.md) R1.1 覆盖 / R1.2 复用 / R1.3 跨网元协同 / R1.5 证据链
- **证据**（原始产品文档）：[WSFD-010502 地址分配方式 md](evidence/UNC/20.15.2/WSFD-010502/) / [WSFD-010504 控制面地址分配方式 md](evidence/UNC/20.15.2/WSFD-010504/) / [WSFD-104413 DHCPv4 md](evidence/UNC/20.15.2/WSFD-104413/) / [WSFD-104005 DHCPv6 md](evidence/UNC/20.15.2/WSFD-104005/) / [WSFD-104410 L2TP md](evidence/UNC/20.15.2/WSFD-104410/) + UDG 对应
- **范本**：[业务感知域融合计费 CS](business/business-awareness/charging/ConfigurationSolution@charging-converged.md) — 跨网元协同 + 特性关系矩阵范本
