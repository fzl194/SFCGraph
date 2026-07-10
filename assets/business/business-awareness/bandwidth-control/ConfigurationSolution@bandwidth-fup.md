---
id: ConfigurationSolution@bandwidth-fup
type: ConfigurationSolution
name: FUP 累计流量策略控制
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# FUP 累计流量策略控制

> 用户/业务级累计流量超阈值降速/重置/改费率方案（Fair Usage Policy）。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。基于 PCC 框架的 URR MONITORINGKEY 机制，与 BWM（CAR/Shaping）正交独立。

## 概览

FUP（Fair Usage Policy）累计流量策略控制解决"超量用户/业务需降速或改策略"的诉求：对用户会话或特定业务做累计流量监控，达预设阈值后由 PCRF/PCF 下发降速/阻塞/改费率策略，达到网络公平使用。方案分两个维度——**会话级 FUP**（[020353](task/UDG/20.15.2/2-00026.md)，整个 PDU 会话粒度，不区分业务）与**业务级 FUP**（[110312](task/UDG/20.15.2/2-00027.md)，区分业务类型，双轨 URR：ONLINE 在线计费 + MONITORINGKEY 累计上报）二选一。两者均基于 PCC backbone（URR 上报累计流量→PCRF 决策→下发策略），降速执行可走 QoS（AMBR）或 BWM（可选叠加）。

协同骨架：UDG 用户面承载 URR 累计上报 + 执行 PCRF 下发的降速策略；UNC 控制面做 Gx/N7 策略中继（会话级 109104 / 业务级 211009）；PCRF/PCF 侧做阈值判定与策略下发（不在 UDG/UNC 配置范围）。

## 配置与协同

本方案编排 **6 个特性**跨网元：UDG 核心 [2-00026 会话级FUP](task/UDG/20.15.2/2-00026.md) + UDG 核心 [2-00027 业务级FUP](task/UDG/20.15.2/2-00027.md) + UDG 基础 [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md) + UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md) + UNC 跨网元对端 [2-00011 业务级FUP WSFD-211009](task/UNC/20.15.2/2-00011.md) + UNC 跨网元对端 [2-00007 会话级FUP WSFD-109104](task/UNC/20.15.2/2-00007.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [020353 会话级FUP](task/UDG/20.15.2/2-00026.md) | 核心（会话维度） | 二选一 | URR 关联所有 PDR（SessionRule），累计达阈值触发；基于 PCC backbone 非 BWM；UDG 侧仅 License 门控 + 复用 PCC（无独立配置对象） |
| [110312 业务级FUP](task/UDG/20.15.2/2-00027.md) | 核心（业务维度） | 二选一 | URR 绑定特定业务 PDR（PccRule），双轨 URR（ONLINE+MONITORINGKEY）同组；额外依赖 SA 业务识别；基于 PCC backbone |
| [PCC基本功能](task/UDG/20.15.2/2-00018.md) | 基础（依赖前提） | 必配 | FUP 基于 PCC 框架的 URR MONITORINGKEY 机制——累计流量上报与策略下发经 PCC 触发链；配置重叠（复用 PCCPOLICYGRP/RULE/USERPROFILE 骨架） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配（110312 业务级时） | 业务级 FUP 需业务识别（区分业务类型）；会话级 020353 不需要（整个会话粒度）；配置不重叠（SA 配识别链） |
| [UNC 211009](task/UNC/20.15.2/2-00011.md) | 跨网元对端（业务级） | 条件必配（业务级时） | UNC 侧业务级 FUP——Gx 配 MKPARSEFORMAT+UMCH+FUPSESSIONEXC 增量；N7 由 PCF 动态下发；与 UDG 110312 组合 |
| [UNC 109104](task/UNC/20.15.2/2-00007.md) | 跨网元对端（会话级） | 条件必配（会话级时） | UNC 侧会话级 FUP——Gx 配 MKPARSEFORMAT+UMCH+FUPSESSIONEXC 三增量；N7 仅 License；与 UDG 020353 组合 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心（二选一）：会话级 FUP（[2-00026](task/UDG/20.15.2/2-00026.md)）

走标准配置方法（见 feature task）。**本方案独有特征**：UDG 侧仅 License 门控（`LKV3G5PCBT01`）+ 复用 PCC backbone（URR 上报累计流量→PCRF），**无独立配置对象**——FUP 阈值/周期/动作（降速/阻塞/改费率）全在 PCRF/PCF 侧决策，UDG 不配置阈值参数。整个 PDU 会话为粒度（不区分业务）。

### UDG 核心（二选一）：业务级 FUP（[2-00027](task/UDG/20.15.2/2-00027.md)）

走标准配置方法（见 feature task）。**核心变种——双轨 URR 同组**：URRGROUP 同时绑两条 URR——① `urr_online`（`USAGERPTMODE=ONLINE`，在线流量计费）② `urr_mk`（`USAGERPTMODE=MONITORINGKEY`，累计流量上报）。PCCPOLICYGRP 绑该 URRGROUP，RULE 以 POLICYTYPE=PCC 触发。License `LKV3G5FPBS01`。区别于会话级：本维度区分业务类型，需配业务过滤链 + 双轨 URR。

> **FUP URR 与计费 URR 的关系**：同对象族（URR/URRGROUP），不同用途——计费 URR 产生话单，FUP URR（MONITORINGKEY）触发降速策略；`USAGERPTMODE` 区分（ONLINE/OFFLINE vs MONITORINGKEY），可共存于不同 URRGROUP。

### UDG 基础：PCC 基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task）。FUP 复用其 PCCPOLICYGRP+RULE+USERPROFILE 骨架 + URR 上报链——配置重叠（PCCPOLICYGRP 绑 URRGROUP，业务级 FUP 演示绑 2 个 URRGROUP）。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。仅业务级 FUP（110312）需要——业务过滤链依赖 SA 识别（activation 演示 TCP/80 HTTP）。会话级 020353 不需要（不区分业务）。

### UNC 跨网元对端：业务级 FUP（[2-00011](task/UNC/20.15.2/2-00011.md) WSFD-211009）

走标准配置方法（见 feature task）。UNC 侧做 Gx/N7 策略中继——Gx 接口配 MKPARSEFORMAT + URR(MONITORINGKEY)+URRGROUP+PCCPOLICYGRP(FUPSESSIONEXC) 费率标识链 + UMCH；N7 接口 L3/L4 由 PCF 动态下发、L7 用预定义规则。与 UDG 110312 组合（业务级时必配）。

### UNC 跨网元对端：会话级 FUP（[2-00007](task/UNC/20.15.2/2-00007.md) WSFD-109104）

走标准配置方法（见 feature task）。UNC 侧做策略中继——Gx 接口配 MKPARSEFORMAT + UMCH + FUPSESSIONEXC 三增量；N7 接口仅 License（PCF 侧配阈值）。与 UDG 020353 组合（会话级时必配）。

### 跨网元/跨特性协同

- **顺序**：PCC backbone 就绪（PCCPOLICYGRP+RULE+USERPROFILE）→ URR 双轨/单轨配置（业务级双轨 / 会话级单轨）→ URRGROUP 绑定 → UNC 侧 Gx/N7 策略中继增量配置 → 运行时累计流量上报→PCRF/PCF 阈值判定→下发降速策略→UDG 执行。
- **一致性**：URRNAME/URRID 跨网元一致（UDG 与 UNC 两端标识取值一致）；MKPARSEFORMAT 与 PCRF 一致（Gx 接口）；FUPSESSIONEXC 排除的业务策略组名一致。
- **降速执行路径**：PCRF 下发的降速策略可走 QoS（AMBR 调整）或 BWM（限速对象）——BWM 为可选叠加（若走 BWM 降速，需另配 [BWM 范本](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md)）。

## 决策点

### DP-1：FUP 维度（会话级 vs 业务级，二选一）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 会话级 FUP（020353，整个 PDU 会话） | UDG 仅 License + PCC backbone（无独立配置）；不需 SA-Basic；UNC 对端=109104；阈值在 PCRF/PCF |
| 业务级 FUP（110312，区分业务类型） | UDG 配双轨 URR（ONLINE+MONITORINGKEY）+ 业务过滤链；需 SA-Basic；UNC 对端=211009；activation 有完整脚本 |

### DP-2：降速执行路径（PCRF 下发后）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| QoS AMBR 调整 | PCRF 下发新 AMBR，UDG 执行（不走 BWM）；与 BWM 正交 |
| BWM 限速叠加 | PCRF 下发 BWM 规则名，UDG 执行限速；需另配 [BWM 范本](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md)；与 QoS 正交 |
| 阻塞/改费率 | PCRF 直接下发阻塞或改费率策略；UDG 执行；不走 BWM |

## 约束

- **License 前置**（critical）：会话级 `LKV3G5PCBT01`（020353）/ 业务级 `LKV3G5FPBS01`（110312）——二选一，未开则 FUP 不生效。
- **依赖 PCC 基本功能**（critical）：FUP 基于 PCC 框架 URR MONITORINGKEY 机制——未开则无策略执行路径。
- **会话级与业务级二选一**（warning）：两维度不混配——会话级以整个 PDU 会话为粒度，业务级区分业务类型；选其一。
- **URRNAME/URRID 跨网元一致**（critical，业务级）：UDG 和 UNC 两端 URR 标识取值一致——不一致则跨网元会话匹配失败。
- **双轨 URR 同组**（warning，业务级）：URRGROUP 须同时绑 online URR + monitoring URR——缺一则功能不完整。
- **REFRESHSRV 必须执行**（critical，业务级）：三四层 Filter 变更后须 `SET REFRESHSRV`（REFRESHTYPE=USERPROFILE）才生效。
- **策略在 PCRF/PCF 侧**（info）：阈值判定与降速/阻塞/改费率动作由 PCRF/PCF 下发，UDG/UNC 仅承载上报与执行——配置生成不产出 FUP 阈值参数。
- **MKPARSEFORMAT 与 PCRF 一致**（critical，UNC Gx 接口）：Monitoring-Key 解析方式须与 PCRF 一致——不一致则累计流量上报解析失败。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 编排特性（feature task，优先）：[2-00026 UDG 会话级FUP](task/UDG/20.15.2/2-00026.md)（会话维度核心）· [2-00027 UDG 业务级FUP](task/UDG/20.15.2/2-00027.md)（业务维度核心）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（backbone 依赖）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务级时业务识别前提）· [2-00011 UNC 业务级FUP WSFD-211009](task/UNC/20.15.2/2-00011.md)（业务级跨网元对端）· [2-00007 UNC 会话级FUP WSFD-109104](task/UNC/20.15.2/2-00007.md)（会话级跨网元对端）
- 复用步骤/命令（compound/atom，按需）：UDG [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链（业务级）· [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套·双轨 URR 变体 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV；UNC [1-00009](task/UNC/20.15.2/1-00009.md) 费率标识链（MONITORINGKEY 变种）· [1-00014](task/UNC/20.15.2/1-00014.md) PCC 开关（MKPARSEFORMAT）
- 证据：[UDG 020353 会话级FUP 特性概述](evidence/business/bandwidth-control/UDG_020353_GWFD-020353 基于累计流量的策略控制特性概述_83974937.md) · [UDG 110312 业务级FUP 特性概述](evidence/business/bandwidth-control/UDG_110312_GWFD-110312 基于业务累计流量的策略控制特性概述_76651884.md) · [UNC 211009 业务级FUP 实现原理](evidence/business/bandwidth-control/UNC_211009_实现原理（N7）_27915155.md) · [UNC 109104 会话级FUP 实现原理](evidence/business/bandwidth-control/UNC_109104_实现原理（N7）_29961017.md) · [UDG PCC基本功能](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md)
