---
id: ConfigurationSolution@bandwidth-apn-strategy
type: ConfigurationSolution
name: 接入点策略控制
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# 接入点策略控制

> 基于 Non-3GPP（WiFi）用户 IP/Port 位置变化触发 PCRF 差异化策略的接入点级控制方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。UNC 主导（位置上报），UDG 侧无独立特性——仅执行 PGW-C 下发的策略动作。

## 概览

接入点策略控制解决"Non-3GPP（WiFi）接入用户位置变化时需差异化策略控制"的诉求：UNC（PGW-C）侧当 Non-3GPP（WiFi）用户 IP/Port 变化时，经 Gx 接口向 PCRF 上报 Event-Trigger(43)（位置变化），由 PCRF 下发差异化策略（如位置增强、差异化带宽/访问控制）。

**核心定位**：本方案是 **UNC 主导的纯被动响应型特性**——参考信息原文明示「本特性无相关 MML 命令 / 无相关告警 / 无相关软参 / 无相关测量指标」。功能实现完全依赖：① License 加载后自动生效；② PCC 基本功能的 Gx 接口通道承载 Event-Trigger 上报。配置生成仅编 1 步 License 开关 + 引用 PCC 基本功能前置；位置上报与策略下发为运行时自动行为，无 PGW-C 侧专属 MML 配置命令。本方案**共享 PCC backbone**（Gx 通道），不配 BWM 对象族。

**与 UDG 侧无对应特性**：本特性是 UNC/PGW-C 侧 Non-3GPP 接入专属——UDG/UPF 侧仅执行 PGW-C 下发的策略动作（如带宽限制、访问控制），无独立 UDG 特性。可选 SA-Basic（若需业务识别增强）。

## 配置与协同

本方案编排 **3 个特性**（UNC 主导）：UNC 核心 [2-00009 接入点策略 WSFD-109108](task/UNC/20.15.2/2-00009.md) + UNC 基础 [2-00005 PCC基本功能 WSFD-109101](task/UNC/20.15.2/2-00005.md) + UDG 可选 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UNC 109108 接入点策略](task/UNC/20.15.2/2-00009.md) | 核心 | 必配 | WiFi 用户 IP/Port 位置变化上报 PCRF（Event-Trigger 43），位置增强；纯被动响应型——License 加载后自动生效，无专属 MML 配置命令；**共享 PCC backbone**（Gx 通道），不配 BWM 对象族 |
| [UNC PCC基本功能 109101](task/UNC/20.15.2/2-00005.md) | 基础（依赖前提） | 必配 | 原文"需开启 PCC 基本功能上报位置"——Gx 接口通道为 Event-Trigger(43) 上报载体；配置重叠（PCC 配 Gx 通道+PCCPOLICYGRP+RULE 骨架，接入点策略仅 License） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（可选增强） | 可选 | 若需业务识别增强（如按业务叠加策略）则配；UDG 侧无独立特性——SA-Basic 为 UDG 业务识别底座；配置不重叠 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UNC 核心：基于接入点策略控制（[2-00009](task/UNC/20.15.2/2-00009.md) WSFD-109108）

走标准配置方法（见 feature task，UNC 侧仅 1 步 License）。**本方案核心变种**：

- **UNC 侧 activation 极简**（纯被动响应型）：仅 `SET LICENSESWITCH`（`LKV3WPWULI11`，控制项 82209749）——License 加载后自动生效，**无专属 MML 配置命令**。位置变化上报（Event-Trigger 43）+ 策略下发为运行时自动行为。
- **不配任何 PCCPOLICYGRP/RULE/USERPROFILE**（★ 本方案核心排除）：接入点策略本身不下发本地规则——位置变化经 Gx 上报 PCRF，策略由 PCRF 动态下发（经 N4 透传 UDG 执行）。

**排除项**：不走 BWM 对象族（无 BWMSERVICE/BWMCONTROLLER）；不配本地 RULE/策略组（策略由 PCRF 下发）；不配 ADCPARA/QOSPROP（不建专有承载/应用检测）。

### UNC 基础：PCC 基本功能（[2-00005](task/UNC/20.15.2/2-00005.md) WSFD-109101）

走标准配置方法（见 feature task）。接入点策略依赖 PCC 基本功能的 Gx 接口通道承载 Event-Trigger(43) 上报——PCCPOLICYGRP+RULE+USERPROFILE 骨架为 PCRF 下发策略的本地承载容器。License `LKV2PCCBF01`+`LKV3W9SPCC11`（控制项 82207979）须开启。代际选择按网络：2G/3G/4G 走 Gx+Diameter，5G 走 Npcf+NRF。

### UDG 可选：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。若需业务识别增强（如按业务叠加策略），UDG 侧可选配 SA-Basic——License `LKV3G5SABS01`（控制项 82209749）。UDG 侧无独立特性对应本方案——仅执行 PGW-C 下发的策略动作。

### 跨网元/跨特性协同

- **顺序**：UNC 侧 PCC 基本功能 Gx 通道就绪 → UNC 侧 License 加载（接入点策略自动生效）→ 运行时：WiFi 用户 IP/Port 变化 → UNC 经 Gx 上报 PCRF（Event-Trigger 43）→ PCRF 下发差异化策略 → UNC 经 N4 透传 UDG → UDG 执行。
- **PCRF 须配置位置响应策略**：PCRF 侧须订阅 Event-Trigger(43) + 配置位置变化响应策略——否则 UNC 上报后无策略下发。
- **Non-3GPP（WiFi）接入专属**：本方案仅适用于 Non-3GPP（WiFi）接入场景——3GPP 接入不触发位置变化上报。
- **UDG 侧无独立特性**：UDG/UPF 侧仅执行 PGW-C 下发的策略动作（如带宽限制、访问控制），无独立 UDG 特性 activation。

## 决策点

### DP-1：网络代际（Gx vs Npcf）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 2G/3G/4G（Gx + Diameter） | UNC 侧 [2-00005](task/UNC/20.15.2/2-00005.md) DP1=2G/3G/4G；需 Diameter 对接链 + PCRF 选择；Event-Trigger(43) 经 Gx 上报 |
| 5G（Npcf + NRF） | UNC 侧 [2-00005](task/UNC/20.15.2/2-00005.md) DP1=5G；PCF 经 NRF 服务化发现；位置变化经 Npcf 上报 |

### DP-2：业务识别增强（SA-Basic 可选）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 不配 SA-Basic（纯位置策略） | 仅按位置变化触发策略；UDG 侧无业务识别增强；最小配置 |
| 配 SA-Basic（业务+位置叠加） | UDG 侧配 SA-Basic 识别链；支持按业务+位置叠加策略；配置增加 |

## 约束

- **License 前置**（critical）：UNC 侧 `LKV3WPWULI11`（109108，控制项 82209749）+ `LKV2PCCBF01`+`LKV3W9SPCC11`（PCC基本功能 109101，控制项 82207979）—— 未开则位置上报功能不生效。
- **依赖 PCC 基本功能**（critical，原文明示）：UNC 侧 PCC 基本功能的 Gx 接口通道为 Event-Trigger(43) 上报载体——PCC backbone 未配则上报链断。
- **无专属 MML 配置命令**（critical，★ 本特性核心）：License 加载后自动生效——原文明示「无相关 MML 命令 / 无相关告警 / 无相关软参 / 无相关测量指标」。配置生成仅编 License 步骤 + 引用 PCC 前置。
- **PCRF 须配置位置响应策略**（critical）：PCRF 侧须订阅 Event-Trigger(43) + 配置位置变化响应策略——否则 UNC 上报后无策略下发。
- **Non-3GPP（WiFi）接入专属**（warning）：本方案仅适用于 Non-3GPP（WiFi）接入场景——3GPP 接入不触发位置变化上报。
- **UDG 侧无独立特性**（info，跨网元澄清）：UDG/UPF 侧仅执行 PGW-C 下发的策略动作——无独立 UDG 特性 activation。UDG 侧配置由 PCRF 下发的下游策略决定。
- **与 BWM 正交**（info）：不共享 BWM 对象族，可与 BWM 共存——不会互相干扰。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 编排特性（feature task，优先）：[2-00009 UNC 接入点策略 WSFD-109108](task/UNC/20.15.2/2-00009.md)（核心，UNC 主导）· [2-00005 UNC PCC基本功能 WSFD-109101](task/UNC/20.15.2/2-00005.md)（Gx 通道依赖）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（可选业务识别增强）
- 证据：[UNC 109108 接入点策略 特性概述](evidence/business/bandwidth-control/UNC_109108_特性概述_79067211.md) · [UNC PCC基本功能 5G](evidence/business/bandwidth-control/UNC_PCC基本功能5G特性概述.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md)
