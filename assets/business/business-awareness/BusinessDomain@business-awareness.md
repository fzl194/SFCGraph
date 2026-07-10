---
id: BusinessDomain@business-awareness
type: BusinessDomain
name: 业务感知
status: draft
source_evidence_ids: [EV-BIZ-charging-00]
---

# 业务感知

> 对用户会话报文解析、区分业务，实现策略控制与计费控制。含 3 个场景：计费、带宽控制、访问限制。本域是 UDG（用户面）+ UNC（控制面）协同的业务能力底座。

## 概览

业务感知域（Business Awareness）在用户会话过程中对用户数据报文进行解析，区分出用户使用的不同业务（如视频、游戏、IM、Web），从而实现差异化的策略控制与计费控制。

核心能力：业务识别（L3/L4 过滤 + L7 协议/URL 识别）→ 策略匹配（RULE + PCC / 头增强 / 重定向 / 带宽）→ 计费/带宽执行。三场景（计费、带宽控制、访问限制）均挂在本域下，共享 SA-Basic + PCC 基本功能 backbone——UDG 侧做报文解析与执行，UNC 侧做策略编排与下发。

## 范围与边界

- 含场景：
  - [计费](business/business-awareness/charging/NetworkScenario@charging.md) — 按业务差异化计费（离线/在线/融合）
  - [[带宽控制]]（NetworkScenario@bandwidth-control）·待建
  - [[访问限制]]（NetworkScenario@access-control）·待建
- 不属于本域：基础接入与会话连通性（APN/地址池/路由，属接入与会话管理域）、网元对接开局（属网元对接域）。业务感知聚焦"识别业务 → 策略/计费控制"，不聚焦"会话建立 / 路由连通"。

## 关联

- 下游场景：[计费](business/business-awareness/charging/NetworkScenario@charging.md)（已建）、[[带宽控制]]、[[访问限制]]（待建）
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（EV-BIZ-charging-00，含业务感知域定义 + 三场景边界 + 共享 backbone 说明）
