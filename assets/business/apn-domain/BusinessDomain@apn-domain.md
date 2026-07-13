---
id: BusinessDomain@apn-domain
type: BusinessDomain
name: APN 业务域
domain: apn-domain
status: draft
---

# APN 业务域

> APN（Access Point Name）业务域是 5G/4G/3G/2G 移动网络中 UE 从附着到 PDU 会话建立的完整链路所涉及的所有业务能力集合——覆盖用户身份验证 → 接入权限判定 → 地址分配 → 网元选择 → 隧道接入 → 会话治理 6 个环节。UDG（用户面）+ UNC（控制面）协同的基础底座。含 1 个场景 + 4 个方案。

## 概览

APN 业务域按 3GPP 标准的 4 维度决策（地址分配 / 鉴权 / 接入方式 / 地址类型）将 24 个 UNC feature + 13 个 UDG feature = 37 个 feature 编排为 4 个方案 + 1 个场景。4 个方案在 APN 完整配置中是 **AND 关系**——一个完整 APN 实例同时需要 CS-1 地址分配（必选核心）+ CS-2 鉴权（必选维度增强）+ CS-3 隧道（按需维度增强，VPN 直通时**不启**）+ CS-4 IP 类型治理（必选维度增强）。

外加 7 个基础 feature（散到各 CS 矩阵行：会话管理/UPF 选择/用户数据管理/接入控制/别名 APN/多 PDN_PDU/位置区域），是任何 APN 方案的依赖前提。

4 大配置组：APN 基础信息（标识属性）+ 地址分配信息（OR 节点 6 种方式）+ 鉴权计费信息（AND 节点 鉴权方式 + Radius 功能）+ 接入方式信息（OR 节点 5 种方式）。3 底座支撑：会话管理 / 网元选择 / 接入控制。

跨网元协同骨架：UDG（UPF 执行地址分配 + 隧道封装）↔ UNC（SMF 决策 + 签约管理）通过 N4/PFCP（5G）/Gz-Gn（4G）消息解耦决策与执行。

## 范围与边界

- 含场景（1 个）：[APN 接入与会话管理](NetworkScenario@apn-access.md)
- 含方案（4 个，AND 关系）：
  - [地址分配](ConfigurationSolution@apn-addr-allocation.md) — 核心（必选）
  - [鉴权 AAA](ConfigurationSolution@apn-auth.md) — 维度增强（4 选 1）
  - [隧道接入](ConfigurationSolution@apn-tunnel.md) — 维度增强（5 选 1，VPN 直通时可不启用）
  - [IP 类型治理](ConfigurationSolution@apn-ip-typing.md) — 维度增强（3 选 1）
- 不属于本域（与相邻域的边界）：
  - 业务识别与策略控制（SA-Basic / PCC基本功能）— 属 [业务感知域](business/business-awareness/BusinessDomain@business-awareness.md)
  - 计费与配额管理（融合/在线/离线计费）— 属业务感知域计费场景
  - 带宽控制与限速（BWM / FUP / QoS）— 属业务感知域带宽控制场景
  - 访问限制与重定向（URL 过滤 / 头增强 / 位置策略）— 属业务感知域访问限制场景
  - 网元对接开局（N4 PFCP 偶联 / Diameter 对接 / SBI 基础）— 属 [网元对接业务域](BusinessDomain@network-element-docking.md)（待建）
  - 运营级 KQI / 性能 / 告警 — 属运维域

> **边界划定原则**：本域聚焦"接入连通性 + 会话生命周期"，不聚焦"业务识别 + 策略/计费控制 + 带宽/接入限制"。本域是业务感知域的**前置底座**——任何业务感知域方案都依赖本域的地址分配和会话建立。

## 约束

- **本域是基础底座**（critical）：业务感知域所有方案均依赖本域先建
- **跨网元一致性**（critical）：UDG 与 UNC 两侧的 IP 池名 / APN 名 / UPF 实例名 / N4 PFCP Node ID 全网唯一，必须严格一致
- **决策与执行分离**（critical）：地址分配决策在 C 面（SMF/PGW-C），执行在 U 面（UPF），通过 N4/PFCP / Gz-Gn 消息解耦
- **License 依赖链**（critical）：IPv6 完整承载需线性 License 链（[GWFD-020401 LKV3G5V6PB01] → [GWFD-020403 LKV3G5VDSA01] → [GWFD-020406 LKV3G5P6PD01]），构建方案时必须交叉验证（**不可按命名规律推断**）
- **CS 之间是 AND 关系**（critical）：一个完整 APN 方案 = CS-1 必选 + CS-2/3/4 按需；4 个 CS 在配置时**全部生效**（除 CS-3 VPN 直通场景），不是 NS 决策点"4 选 1"

## 关联

- **下游场景**：[APN 接入与会话管理](NetworkScenario@apn-access.md)
- **下游方案**（4 个，AND 关系）：[地址分配](ConfigurationSolution@apn-addr-allocation.md) / [鉴权 AAA](ConfigurationSolution@apn-auth.md) / [隧道接入](ConfigurationSolution@apn-tunnel.md) / [IP 类型治理](ConfigurationSolution@apn-ip-typing.md)
- **下游业务域**（[业务感知域](business/business-awareness/BusinessDomain@business-awareness.md)）— 下游消费方
- **业务层 SOP**：[业务层级构建SOP.md](business/业务层级构建SOP.md) §4.2 BD 模板
- **业务层审视**：[业务层级wiki审视流程.md](business/业务层级wiki审视流程.md) R1.4 前置门 / R2.4 模板合规
- **范本**：[业务感知域 BD](business/business-awareness/BusinessDomain@business-awareness.md) — 3 场景 27 CS 的成熟范本
- **证据**（原始产品文档，从 `assets/evidence/{UDG,UNC}/20.15.2/{WSFD,GWFD,IPFD}-xxxxx/` 拷入）：按需在各 CS 关联段用 markdown 链接引用
