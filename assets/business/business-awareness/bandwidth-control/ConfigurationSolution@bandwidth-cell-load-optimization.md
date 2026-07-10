---
id: ConfigurationSolution@bandwidth-cell-load-optimization
type: ConfigurationSolution
name: 小区负荷无线优化
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# 小区负荷无线优化

> 基于小区负荷（拥塞）状态上报触发 PCRF 动态策略调整的无线资源优化方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。不配 BWM 对象族/过滤链/规则——UDG+UNC 两侧均为"开关+透传"，策略由 PCRF 动态下发。

## 概览

小区负荷无线优化解决"热点小区拥塞时需动态调整用户/业务策略"的诉求：RAN 侧监测小区负荷状态（Cell Load Level）变化，经 GTP-U 扩展头实时上报给 PGW-U（UDG）；UDG 经 N4 接口上报 PGW-C（UNC），UNC 经 Gx/N7 接口触发 CELL_CONGESTION_CHANGE(1003) Event-Trigger 上报 PCRF；PCRF 据此下发差异化策略（如限速/降级），减缓小区拥塞。

**核心架构**：`RAN →(GTP-U 扩展头)→ UDG(PGW-U) →(N4/PFCP)→ UNC(PGW-C/SMF) →(Gx/N7)→ PCRF`。**UDG+UNC 两侧均为被动上报+透传**——不执行限速、不配过滤链/规则/策略组；两侧 activation 均极简（License + `SET APNREPORTATTR` 开启 APN 级拥塞上报开关）。策略决策在 PCRF，策略执行回到 PGW-U（由 PCRF 动态下发）。本方案共享 PCC backbone（Gx/N7 通道 + N4 透传），不共享 BWM 对象族。

## 配置与协同

本方案跨网元编排 **4 个特性**：UDG 核心 [2-00032 小区负荷](task/UDG/20.15.2/2-00032.md) + UDG 基础 [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md) + UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)（License 前置）+ UNC 跨网元对端 [2-00012 小区负荷 WSFD-211101](task/UNC/20.15.2/2-00012.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [110332 小区负荷](task/UDG/20.15.2/2-00032.md) | 核心 | 必配 | GTP-U 扩展头收 RAN 上报小区负荷 + N4 透传 PGW-C；UDG 侧 activation 仅 License + `SET APNREPORTATTR`；**共享 PCC backbone**（N4/Gx 通道），不配 BWM 对象族/过滤链/规则——策略由 PCRF 动态下发 |
| [PCC基本功能](task/UDG/20.15.2/2-00018.md) | 基础（依赖前提） | 必配 | 原文"需开启 PCC 基本功能"——UDG 从 PCRF 获取策略；配置不重叠（PCC 配 Gx 通道+PCCPOLICYGRP+RULE 骨架，小区负荷仅 License+APNREPORTATTR 开关） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配（License 前置） | 业务识别基础能力前置——小区负荷方案本身不直接用 SA 识别，但 UDG 侧 SA-Basic License 为业务感知体系底座；配置不重叠 |
| [UNC 211101](task/UNC/20.15.2/2-00012.md) | 跨网元对端 | 必配 | UNC 控制面中继——接收 PGW-U 经 N4 上报 + 经 Gx/N7 CCR-U 上报 PCRF（CELL-CONGESTION-CHANGE trigger）；与 UDG 110332 对端组合，两侧 activation 均极简（License + `SET APNREPORTATTR`），License 控制项不同 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：小区负荷上报（[2-00032](task/UDG/20.15.2/2-00032.md)）

走标准配置方法（见 feature task，UDG 侧仅 2 步）。**本方案核心变种**：

- **UDG 侧 activation 极简**：`SET LICENSESWITCH`（`LKV3G5WOCR01`，控制项 82200DHW）+ `SET APNREPORTATTR`（`CONGESTIONRPT=ENABLE`）——仅对指定 APN 开启拥塞上报开关。
- **不配任何过滤链/规则/PCC 策略组**（★ 本方案核心排除）：策略由 PCRF 动态下发（特性 wiki 明示"PCRF 下发 CELL_CONGESTION_CHANGE trigger + 下发策略"），UDG 仅作透传 + 上报。

**排除项**：不走 BWM 对象族（无 BWMSERVICE/BWMCONTROLLER/BWMRULE）；不配 FILTER/FLOWFILTER/RULE/USERPROFILE（策略非本地匹配）；不配 ADC/QOSPROP/SADEDICBEARER（不建专有承载）。

### UDG 基础：PCC 基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task）。小区负荷方案依赖 PCC 通道从 PCRF 获取动态策略——UDG 侧 PCCPOLICYGRP+RULE+USERPROFILE 骨架为 PCRF 下发策略的本地承载容器。License `LKV3G5PCCB01`（控制项 82209737）须开启。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。业务感知体系底座——License `LKV3G5SABS01`（控制项 82209749）前置。小区负荷方案本身不直接用 SA 协议识别（策略由 PCRF 下发），但 SA-Basic 是 UDG 业务感知能力基础。

### UNC 跨网元对端：小区负荷上报（[2-00012](task/UNC/20.15.2/2-00012.md) WSFD-211101）

走标准配置方法（见 feature task，UNC 侧仅 2 步）。**本方案核心变种**：

- **UNC 侧 activation 极简**：`SET LICENSESWITCH`（`LKV3W9WOCR11`，控制项 82209457）+ `SET APNREPORTATTR`（`CONGESTIONRPT=ENABLE`）——License 控制项与 UDG 侧不同（UNC=`LKV3W9WOCR11` / UDG=`LKV3G5WOCR01`）。
- **UNC 侧纯中继**（★ 跨网元澄清）：UNC（PGW-C/SMF）接收 PGW-U 经 N4 上报的小区负荷状态 → 经 Gx/N7 CCR-U 上报 PCRF（CELL-CONGESTION-CHANGE(1003) trigger）→ PCRF 决策后下发 PCC 策略经 N4 透传 PGW-U 执行。UNC **不执行限速、不配规则/策略组**。

### 跨网元/跨特性协同

- **顺序**：UDG+UNC 两侧 License 前置（`LKV3G5WOCR01` / `LKV3W9WOCR11`）→ 两侧 PCC 基本功能 Gx/N7 通道就绪 → 两侧 `SET APNREPORTATTR`（`CONGESTIONRPT=ENABLE`）开启指定 APN 拥塞上报 → 运行时：RAN 上报小区负荷 → UDG 经 N4 上报 UNC → UNC 经 Gx/N7 上报 PCRF → PCRF 下发策略 → UDG 执行。
- **APN 一致性**：两侧 `SET APNREPORTATTR` 的 APN 须一致（同一 APN 开启拥塞上报）。
- **RAN 必须支持**：无线侧网元须支持经 GTP-U 扩展头上报小区负荷状态——否则 UDG 收不到上报。
- **PCRF 必须配置 CELL-CONGESTION-CHANGE trigger**：PCRF 侧须订阅(1003) trigger + 配置拥塞响应策略——否则 UNC 上报后无策略下发。

## 决策点

### DP-1：APN 粒度（哪些 APN 开启拥塞上报）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 单 APN 开启 | `SET APNREPORTATTR:APN={apn},CONGESTIONRPT=ENABLE`；对指定 APN 生效 |
| 多 APN 开启 | 逐 APN 执行 `SET APNREPORTATTR`；两侧 APN 列表一致 |
| 全 APN 开启 | 不推荐——全量上报可能引发 PCRF 策略风暴；按热点小区所在 APN 选择性开启 |

## 约束

- **License 双前置**（critical）：UDG 侧 `LKV3G5WOCR01`（110332，控制项 82200DHW）+ UNC 侧 `LKV3W9WOCR11`（211101，控制项 82209457)——两侧 License 控制项不同，未开则小区负荷上报功能不生效。
- **依赖 PCC 基本功能**（critical）：UDG+UNC 两侧均依赖 PCC 基本功能 Gx/N7 通道承载 CELL-CONGESTION-CHANGE trigger——PCC backbone 未配则上报链断。
- **两侧 APNREPORTATTR 必配一致**（critical）：UDG 与 UNC 两侧 `SET APNREPORTATTR` 的 APN + `CONGESTIONRPT=ENABLE` 须一致——不一致则单侧上报、链路断裂。
- **RAN 必须支持**（critical）：无线侧网元须支持经 GTP-U 扩展头上报小区负荷状态——否则 UDG 收不到上报。
- **PCRF 须配置响应策略**（critical）：PCRF 侧须订阅 CELL-CONGESTION-CHANGE(1003) trigger + 配置拥塞响应策略——否则 UNC 上报后无策略下发，UDG 不执行任何动作。
- **UDG+UNC 两侧均不执行限速**（critical，跨网元澄清）：策略决策在 PCRF，执行回到 PGW-U（PCRF 动态下发）——两侧仅做开关+中继，配限速对象/过滤链无效。
- **REFRESHSRV 时序**（warning）：`SET APNREPORTATTR` 后两侧均需 `SET REFRESHSRV` 生效。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 编排特性（feature task，优先）：[2-00032 UDG 小区负荷](task/UDG/20.15.2/2-00032.md)（核心）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（PCC 通道依赖）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（License 前置底座）· [2-00012 UNC 小区负荷 WSFD-211101](task/UNC/20.15.2/2-00012.md)（跨网元对端）
- 证据：[UDG 110332 小区负荷 特性概述](evidence/business/bandwidth-control/UDG_110332_GWFD-110332 基于小区负荷上报的无线资源优化特性概述_31087646.md) · [UNC 211101 实现原理](evidence/business/bandwidth-control/UNC_211101_实现原理_89376139.md) · [UDG PCC基本功能](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md)
