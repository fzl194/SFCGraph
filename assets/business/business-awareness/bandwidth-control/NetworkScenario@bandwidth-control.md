---
id: NetworkScenario@bandwidth-control
type: NetworkScenario
name: 带宽控制
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# 带宽控制

> 按业务差异化限速/整形/FUP 降速/GBR 保证。属于[业务感知](business/business-awareness/BusinessDomain@business-awareness.md)域。含 12 个方案（BWM 主干 + Shaping/FUP/QoS 触发/无线资源等变种）。

## 概览

带宽控制场景对不同业务流采用差异化带宽管理：基础 BWM（CAR/Shaping/分级）解决 P2P/VoIP 等占用大量带宽资源的业务导致的拥塞；FUP（Fair Use Policy，累计流量策略控制）在用户/业务级超量后降速或重置；QoS 触发保障关键业务（语音/视频）带宽；终端/切片/小区负荷等无线资源优化结合上层带宽策略。

**判断依据**：用户需按业务/用户/用户组/切片/时段/负荷等多维度差异化限速，或需对超量用户/业务做 FUP 降速，或需保障关键业务（VoNR/视频）GBR 带宽。**典型产出**：P2P 业务限速、夜间免打扰时段、超量用户降速、视频业务保证带宽、切片隔离、热点小区负载均衡。

跨网元协同：UDG（PGW-U/UPF）做带宽执行（CAR/Shaping 实际限速）；UNC（PGW-C/SMF）做 PCC 策略传递（PCRF/PCF 规则→N4 透传 UPF），本地规则模式无 PCRF/PCF 时 UNC 直接配置本地规则并经 N4 下发。Backbone 共享 SA-Basic（业务识别）+ PCC基本功能（策略通道）。

## 边界

- 覆盖：UDG（用户面 BWM 限速/CAR/Shaping/FUP/QoS 触发/无线资源优化）+ UNC（控制面 PCC 策略传递/本地规则/QoS 触发/ADC 应用检测/接入点策略）；接口 N4/PFCP（SMF↔UPF）、Gx/N7（PCRF/PCF↔SMF）；控制维度：业务类型（RG/CATEPROP）、用户级/用户组级/整机级、时段、TOS、协议（HTTP/P2P/VoIP）、切片、APN/DNN、用户归属（ROAMING/RAT）。
- 不覆盖：业务识别基础（属 SA-Basic backbone，跨场景共享）、接入控制（属访问限制场景）、计费/扣费（属计费场景，BWM/FUP 触发流量但不直接出话单）。

## 决策点

场景级方案路由——什么业务诉求选哪个方案。

| 业务诉求 | 推荐方案 | 理由 |
|---|---|---|
| 按业务/用户/用户组/切片/时段限速（CAR/Shaping/分级） | → [BWM 基础限速](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md) | 主干方案，9 子场景（用户/组/整机×TOS/协议/时段/切片/APN） |
| 仅按业务 Shaping（流量整形） | → [Shaping 业务整形](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-shaping.md) | SHAPING 限用户级；110313 突破组级限制 |
| 用户/业务级累计流量超量降速/重置 | → [FUP 累计流量](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-fup.md) | 会话级/业务级二选一，URR MONITORINGKEY 累计达阈值触发 |
| 业务触发 QoS 保证（GBR） | → [QoS 触发保证](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-qos-trigger.md) | 专有承载/QoS Flow，与 BWM 正交 |
| 终端系统码率差异化 | → [终端码率差异化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-coderate-terminal.md) | 110301，BWMRULE 加终端平台维度（共享 BWM 对象族） |
| 上下行解耦视频承载信令 | → [视频承载信令控制](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-video-bearer.md) | 110302，专有承载 QoS |
| 业务流标识无线资源优化（FPI） | → [FPI 无线优化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-fpi-optimization.md) | 110331，FPI+GTP-U 扩展头触发 RAN 调度 |
| 小区负荷上报无线资源优化 | → [小区负荷无线优化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-cell-load-optimization.md) | 110332+UNC 211101，GTP-U 上报+PCC 触发 |
| IM 类业务无线资源管控 | → [IM 无线管控](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-im-radio.md) | 020359，DSCP REMARK_FPI 标记 |
| 应用检测触发（HTTP/P2P 应用） | → [ADC 应用检测触发](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-adc-trigger.md) | 020357+UNC 109102，ADC 上报 PCRF 触发带宽（上游触发源） |
| 终端异常下行流量检测 | → [异常流量检测](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-anomaly-detection.md) | 020305，**边界：安全/检测类**，依赖内容计费，可触发带宽/阻断 |
| 接入点策略控制 | → [接入点策略](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-apn-strategy.md) | UNC 109108，位置上报（Non-3GPP/WiFi），UNC 主导 |

## 关联

- 上游域：[业务感知](business/business-awareness/BusinessDomain@business-awareness.md)
- 下游方案（12 个）：[BWM 基础限速](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md) · [Shaping 业务整形](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-shaping.md) · [FUP 累计流量](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-fup.md) · [QoS 触发保证](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-qos-trigger.md) · [终端码率差异化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-coderate-terminal.md) · [视频承载信令控制](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-video-bearer.md) · [FPI 无线优化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-fpi-optimization.md) · [小区负荷无线优化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-cell-load-optimization.md) · [IM 无线管控](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-im-radio.md) · [ADC 应用检测触发](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-adc-trigger.md) · [异常流量检测](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-anomaly-detection.md) · [接入点策略](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-apn-strategy.md)
- 证据：[UDG BWM 特性概述](evidence/business/bandwidth-control/GWFD-110311 基于业务感知的带宽控制特性概述_77219469.md) + [实现原理](evidence/business/bandwidth-control/实现原理_77219470.md) + [9 激活子场景](evidence/business/bandwidth-control/)（BWM 主干） + [UNC BWM 概述](evidence/business/bandwidth-control/特性概述_79619204.md) + [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) + [PCC](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md) + [UNC PCC 5G](evidence/business/bandwidth-control/UNC_PCC基本功能5G特性概述.md)
