---
id: NetworkScenario@apn-access
type: NetworkScenario
name: APN 接入与会话管理
domain: apn-domain
scenario: apn-access
status: draft
---

# APN 接入与会话管理

> 解决"UE 如何接入移动核心网并获得 IP 服务"的业务问题。属于 [APN 业务域](business/apn-domain/BusinessDomain@apn-domain.md)。含 4 个方案（4 个独立决策维度，AND 关系），覆盖 24 个 UNC feature + 13 个 UDG feature。

## 概览

APN 接入与会话管理场景覆盖 UE 一次完整接入流程的所有配置决策：从 UE 发起附着请求 → SMF/PGW-C/SGSN 接收 → 鉴权（4 种 AUTHMODE）→ 地址分配（6 种方式 × 3 种 IP 类型）→ 隧道接入（5 种）→ 会话建立 → 用户面配置下发 → 业务流开始。

**核心洞察**：4 个方案（CS）在 APN 完整配置中是 **AND 关系**——一个完整 APN 方案通常同时包含 4 个 CS（地址分配 + 鉴权 + 隧道 + IP 类型），每个 CS 对应一个独立决策维度。**不存在"4 选 1"互斥设计**。

**判断依据**（什么业务诉求触发本场景）：需要为 UE 分配 IP（CS-1）+ 需要对 UE 鉴权（CS-2 4 选 1）+ 需要把 UE 流量送到企业 DN（CS-3 5 选 1，普通 Internet 访问可不启用）+ 需要支持 IPv4/IPv6/双栈（CS-4 3 选 1）。

**典型产出**：配置好的 APN 实例 + 地址池 + 鉴权链路 + 隧道 + 路由发布 + 跨网元一致性校验。

跨网元协同：UDG（UPF/PGW-U 执行）+ UNC（SMF/PGW-C/AMF/SGSN/MME 决策）通过 N4/PFCP（5G）/Gz-Gn（4G）消息解耦。

## 边界

- 覆盖：
  - 产品维度：UDG（用户面）+ UNC（控制面）双产品域
  - 网元维度：SMF/PGW-C/AMF/SGSN/MME（UNC）+ UPF/PGW-U（UDG）
  - 接口维度：N1/N2（NAS）/N4（PFCP）/Gz/Gn/Gy（4G）/Ga（话单）/N7/N40（5G 策略 + 融合计费）
  - 控制维度（4 个独立决策维度）：DP-1 地址分配方式（6 种 × 3 种 IP 类型 = 18 格矩阵）/ DP-2 鉴权方式（4 种）/ DP-3 接入方式（5 种，VPN 直通不启 CS-3）/ DP-4 IP 类型（3 种）
- 不覆盖（与相邻场景的边界）：
  - 业务识别 / 策略控制 / 计费 / 带宽控制 / 访问限制 — 属 [业务感知域](business/business-awareness/BusinessDomain@business-awareness.md)
  - 网元对接开局（N4 PFCP 偶联 / Diameter / SBI）— 属 [网元对接业务域](business/apn-domain/BusinessDomain@network-element-docking.md)（★待建，APN 域边界划定引用）
  - 运营级 KQI / 性能 / 告警 — 属运维域

> **边界划定原则**：本场景聚焦"UE 如何接入并获得服务"，不聚焦"如何识别业务 / 如何差异化策略/计费 / 如何差异化限速 / 如何差异化访问限制"。

## 决策点

> 决策点不编号（按 [业务层级构建SOP.md §5](business/业务层级构建SOP.md)）。4 个 DP 独立决策，**完整 APN 方案 = 4 DP 全部选 1 + 基础 feature 矩阵**。

### DP-1：地址分配方式（必选 1，6 选 1）

| 选项 | 涉及方案 | 走法 |
|---|---|---|
| **UPF 本地分配**（最常用）| [CS-1 地址分配](business/apn-domain/ConfigurationSolution@apn-addr-allocation.md) | UNC [2-00015](task/UNC/20.15.2/2-00015.md) POOLTYPE=LOCAL + UDG 4 子方式 [2-00034/35/36/38](task/UDG/20.15.2/2-00034.md) |
| **SMF 本地分配**（C 面独立）| CS-1 | UNC [2-00015](task/UNC/20.15.2/2-00015.md) + [2-00016](task/UNC/20.15.2/2-00016.md) ALLOCPRECEDENCE=SMF |
| **UDM 静态签约** | CS-1 | UNC [2-00015](task/UNC/20.15.2/2-00015.md) POOLTYPE=UDM + UDM 签约 Framed-IP |
| **Radius 下发** | CS-1 + CS-2 | UNC [2-00015](task/UNC/20.15.2/2-00015.md) + [CS-2 鉴权](business/apn-domain/ConfigurationSolution@apn-auth.md) Radius 完整 + UDG [2-00038](task/UDG/20.15.2/2-00038.md) 解析 Framed-Pool |
| **DHCP 代理** | CS-1 | UNC [2-00021/22](task/UNC/20.15.2/2-00021.md) DHCP 代理 + 外部 DHCP server |
| **L2TP/LNS 分配** | CS-1 + CS-3 | UNC [2-00020 L2TP](task/UNC/20.15.2/2-00020.md) LNS 模式 + LNS server |

### DP-2：鉴权方式（必选 1，4 选 1）

| 选项 | 涉及方案 | 走法 |
|---|---|---|
| **透明接入 TRANS_NON_AUTH** | [CS-2 鉴权](business/apn-domain/ConfigurationSolution@apn-auth.md) | HSS/UDM 已完成鉴权，无需 AAA 二次鉴权；UNC [2-00024](task/UNC/20.15.2/2-00024.md) ACCESSMODE=TRANS_NON_AUTH + 不启 Radius 功能 |
| **透明鉴权 TRANS_AUTH** | CS-2 | 网络侧配置的用户名密码；UNC [2-00024](task/UNC/20.15.2/2-00024.md) ACCESSMODE=TRANS_AUTH + [2-00025 Radius 功能](task/UNC/20.15.2/2-00025.md) |
| **不透明接入 NON_TRANS** | CS-2 | 用户 PCO 携带用户名密码，企业 AAA 二次鉴权；UNC [2-00024](task/UNC/20.15.2/2-00024.md) ACCESSMODE=NON_TRANS + [2-00025 Radius 功能](task/UNC/20.15.2/2-00025.md) |
| **本地鉴权 LOC_AUTH** | CS-2 | UNC 本地配置用户名密码，无 AAA server；UNC [2-00024](task/UNC/20.15.2/2-00024.md) ACCESSMODE=LOC_AUTH + 不启 Radius 功能 |

### DP-3：接入方式（可选 1，5 选 1；VPN 直通 = 不启 CS-3）

| 选项 | 涉及方案 | 走法 |
|---|---|---|
| **VPN 直通**（隐式默认）| **不启 CS-3** | 走标准 Internet 访问，无隧道；UPF 直接 NAT 转发 |
| **GRE 隧道** | [CS-3 隧道](business/apn-domain/ConfigurationSolution@apn-tunnel.md) | UNC [2-00029 GRE](task/UNC/20.15.2/2-00029.md) + UDG [2-00027/28/29](task/UDG/20.15.2/2-00027.md) |
| **IPSec 隧道** | CS-3 | UNC [2-00030 IPSec](task/UNC/20.15.2/2-00030.md) + UDG [2-00027/28/29](task/UDG/20.15.2/2-00027.md) |
| **L2TP 隧道** | CS-3 | UNC [2-00020 L2TP](task/UNC/20.15.2/2-00020.md) + LNS server + APNL2TPATTR |
| **MPLS VPN** | CS-3 | UNC [2-00031 MPLS VPN](task/UNC/20.15.2/2-00031.md) + L3VPN 实例 |

### DP-4：IP 类型（必选 1，3 选 1）

| 选项 | 涉及方案 | 走法 |
|---|---|---|
| **IPv4 单栈** | [CS-4 IP 类型](business/apn-domain/ConfigurationSolution@apn-ip-typing.md) | 不启 IPv6 承载 / 双栈 / Prefix Delegation |
| **IPv6 单栈** | CS-4 | UNC [2-00018 IPv6 承载](task/UNC/20.15.2/2-00018.md) + UDG [2-00041 IPv6 承载](task/UDG/20.15.2/2-00041.md) + License LKV3G5V6PB01 |
| **IPv4v6 双栈** | CS-4 | UNC [2-00017 双栈](task/UNC/20.15.2/2-00017.md) + UDG [2-00043 双栈](task/UDG/20.15.2/2-00043.md) + License LKV3G5VDSA01 |

> **完整 APN 方案示例**：
> - **基础家庭宽带 APN** = CS-1（UPF 本地 / IPv4）+ CS-2（透明接入 TRANS_NON_AUTH）+ **不启 CS-3**（VPN 直通）+ CS-4（IPv4 单栈）+ 基础 feature（会话管理 + UPF 选择 + 用户数据管理）
> - **企业工控 APN** = CS-1（UDM 静态 / IPv4）+ CS-2（不透明接入 NON_TRANS + Radius 完整）+ CS-3（IPSec 隧道）+ CS-4（IPv4 单栈）+ 基础 feature
> - **5G 智慧农业 APN** = CS-1（UPF 本地 / IPv4）+ CS-2（透明接入）+ **不启 CS-3**（VPN 直通）+ CS-4（IPv4 单栈）+ 基础 feature
> - **企业双栈 L2TP APN** = CS-1（L2TP/LNS 模式 / 双栈）+ CS-2（不透明接入 + Radius 完整）+ CS-3（L2TP 隧道）+ CS-4（双栈）+ 基础 feature
>
> **CS 间的依赖**（配置顺序）：CS-2 鉴权 → CS-1 地址分配 → CS-3 隧道 → CS-4 IP 类型。鉴权先于地址分配（鉴权失败时地址分配不发生）；地址分配先于隧道（隧道封装需要源 IP）；隧道在 IP 类型后激活（双栈时按需启动）。

## 关联

- 上游域：[APN 业务域](business/apn-domain/BusinessDomain@apn-domain.md)
- 下游方案（4 个，AND 关系，**全部** 必选/按需）：
  - [CS 地址分配](business/apn-domain/ConfigurationSolution@apn-addr-allocation.md) — 核心（必选）
  - [CS 鉴权 AAA](business/apn-domain/ConfigurationSolution@apn-auth.md) — 必选 1（4 选 1）
  - [CS 隧道接入](business/apn-domain/ConfigurationSolution@apn-tunnel.md) — 可选（VPN 直通时不启用）
  - [CS IP 类型治理](business/apn-domain/ConfigurationSolution@apn-ip-typing.md) — 必选 1（3 选 1）
