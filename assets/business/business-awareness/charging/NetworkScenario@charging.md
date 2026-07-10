---
id: NetworkScenario@charging
type: NetworkScenario
name: 计费
domain: business-awareness
status: draft
---

# 计费

> 按业务差异化计费，结合默认计费、免费业务和配额动作完成计费闭环。属于[业务感知](business/business-awareness/BusinessDomain@business-awareness.md)域。含 7 个方案。

## 概览

计费场景对不同业务流采用不同计费方式，结合默认计费、免费业务和配额动作完成计费闭环。

**判断依据**：用户需按业务粒度差异化计费（离线/在线/融合），或需按流量/时长/事件统计特定业务使用量。**典型产出**：专项业务单独计费、免费业务不计费、普通业务默认计费，配额耗尽后切换到阻断或重定向。

跨网元协同：UDG（用户面）做业务识别 + URR 累计 + 配额执行；UNC（控制面）做话单格式化 / 配额管理 / CHF-OCS 对接。三计费方式（离线 Ga / 在线 Gy-DCC / 融合 N40-Nchf）共享费率标识链（URR→URRGROUP→PCCPOLICYGRP→RULE→RULEBINDING）。

## 边界

- 覆盖：UDG（用户面 URR 执行）+ UNC（控制面 SMF/CHF/CG）；接口 Ga（离线）/Gy-DCC（在线）/N40-Nchf（融合）/N4-PFCP（SMF↔UPF）/Gx-N7（PCF↔PCEF）；控制维度：业务类型 RG、计量方式（流量/时长/事件）、计费方式（离线/在线/融合）、配额动作（BLOCK/REDIRECT/FORWARD）。
- 不覆盖：带宽控制（差异化限速/整形/FUP/GBR）、访问限制（URL 过滤/重定向阻断/接入控制）——属相邻场景，但共享业务感知 backbone（SA-Basic + PCC 基本功能）。

## 决策点

场景级方案路由——什么业务诉求选哪个方案。

| 选项/场景 | 影响（选哪个 CS） |
|---|---|
| 后付费、话单结算 | → [CS 离线计费](business/business-awareness/charging/ConfigurationSolution@charging-offline.md)（Ga 接口，URR=OFFLINE） |
| 预付费、实时余额控制 | → [CS 在线计费](business/business-awareness/charging/ConfigurationSolution@charging-online.md)（Gy/DCC，URR=ONLINE） |
| 在线+离线统一（5G SA） | → [CS 融合计费](business/business-awareness/charging/ConfigurationSolution@charging-converged.md)（N40/Nchf，双 URR） |
| 按业务差异化费率 | → [CS 内容计费基础](business/business-awareness/charging/ConfigurationSolution@charging-content.md)（SA 识别 + RG） |
| 按流量/时长/事件计量 | → [CS 计量形态增强](business/business-awareness/charging/ConfigurationSolution@charging-metering.md)（METERINGTYPE） |
| 配额耗尽体验切换 | → [CS 配额降速](business/business-awareness/charging/ConfigurationSolution@charging-quota-exhaust.md)（Final-Unit-Action） |
| 未匹配流量兜底 | → [CS 兜底默认](business/business-awareness/charging/ConfigurationSolution@charging-fallback.md)（DFTURRGRPNAME） |

## 关联

- 上游域：[业务感知](business/business-awareness/BusinessDomain@business-awareness.md)
- 下游方案：[融合计费](business/business-awareness/charging/ConfigurationSolution@charging-converged.md)（已建范本）、[[charging-online]]、[[charging-offline]]、[[charging-content]]、[[charging-metering]]、[[charging-quota-exhaust]]、[[charging-fallback]]（待建）
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（EV-BIZ-charging-00，含 NS-CH-01 计费场景定义 + 边界 + 8 决策点）
