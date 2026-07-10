---
id: ConfigurationSolution@bandwidth-im-radio
type: ConfigurationSolution
name: IM 业务无线管控
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# IM 业务无线管控

> 基于 SA 识别 IM 类业务（QQ/MSN/微信等）经 DSCP REMARK_FPI 标记触发无线侧差异化调度的管控方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。不共享 BWM 对象族——用 RULE(POLICYTYPE=REMARK_FPI) 标记业务流，无线侧按 DSCP 调度。

## 概览

IM 业务无线管控解决"IM 类业务（QQ/MSN/微信等）在无线资源有限场景下需差异化调度"的诉求：UDG 基于 SA 识别 IM 业务（七层协议 `qq_im` 等）→ RULE 经 `POLICYTYPE=REMARK_FPI` 将 IM 业务映射为 DSCP 值（如 AF12）标记业务报文 → 含 DSCP 标记的报文透传到 BSC/RNC，无线侧按 DSCP 综合调度优先级对 IM 报文做无线资源优化。

**核心机制**：与 FPI 业务流标识无线优化（[bandwidth-fpi-optimization](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-fpi-optimization.md)）机制相近——都用 `POLICYTYPE=REMARK_FPI` 标记触发无线侧调度；但本方案**专聚焦 IM 类业务**（依赖 SA-IM 子特性的 IM 协议特征库），且 **DSCP 标记方式需 MOD USERPROFILE 禁用 Alias Marking**（华为私有，仅 UDG+BSC/RNC 均为华为设备时生效）。三四层过滤条件配置为 ANY（全匹配兜底），IM 业务识别主要靠七层协议（`ADD PROTBINDFLOWF` 绑定 IM 协议名）。

## 配置与协同

本方案编排 **3 个特性**：UDG 核心 [2-00022 IM无线](task/UDG/20.15.2/2-00022.md) + UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)（含 SA-IM 子特性）+ UDG 基础 [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [020359 IM无线](task/UDG/20.15.2/2-00022.md) | 核心 | 必配 | DSCP REMARK_FPI 传递无线侧调度（`POLICYTYPE=REMARK_FPI`）；**不共享 BWM 对象族**（无 BWMSERVICE/BWMCONTROLLER/BWMRULE）；用 RULE(POLICYTYPE=REMARK_FPI) + USERPROFILE + PROTBINDFLOWF(IM 协议名) 专属组装；依赖 SA-IM 子特性的 IM 协议特征 |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | IM 业务识别基础——SA-Basic 的特征库+解析库+ SA-IM 子特性（QQ/MSN/微信等 IM 协议特征）为 IM 无线管控前提；配置不重叠（SA 配识别链，IM 无线配 RULE/USERPROFILE/PROTBINDFLOWF） |
| [PCC基本功能](task/UDG/20.15.2/2-00018.md) | 基础（依赖前提） | 必配 | PCRF 下发 PCC 规则的通道——PCCPOLICYGRP+RULE+USERPROFILE 骨架为 IM 规则链载体；配置重叠（复用 PCCPOLICYGRP/RULE/USERPROFILE 骨架，但 RULE 的 POLICYTYPE=REMARK_FPI 是 IM 专属变种） |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：IM 类业务无线资源管控（[2-00022](task/UDG/20.15.2/2-00022.md)）

走标准配置方法（见 feature task）。**本方案核心变种**：

- **RULE POLICYTYPE=REMARK_FPI**（核心变种）：`ADD RULE:POLICYTYPE=REMARK_FPI` + REMARKFPISEL=FPI + FPIVALUE={DSCP 映射值}——将 IM 业务流标记 DSCP（如 AF12）传无线侧。区别于 BWM 的 `POLICYTYPE=BWM` 和计费的 `POLICYTYPE=PCC`。
- **三四层过滤 ANY + 七层 IM 协议**：三四层 FILTER 配 ANY（全匹配兜底），IM 识别靠 `ADD PROTBINDFLOWF` 绑定 IM 协议名（如 `qq_im`）——依赖 SA-IM 子特性的协议特征库。
- **MOD USERPROFILE 禁用 Alias Marking**（★ 华为私有核心变种）：DSCP 标记方式需 `MOD USERPROFILE:ALIASMARKFLAG=DISABLE`——否则系统不改写报文 ToS 域、DSCP 标记不生效。仅 UDG+BSC/RNC 均为华为设备时支持。
- **License**：`LKV3G5WIMR01`（控制项 82200DHE）。

**排除项**：不走 BWM 对象族（无 BWMSERVICE/BWMCONTROLLER，与 BWM 正交）；不建专有承载（无 SADEDICBEARER/QOSPROP，与 QoS 触发正交）；不配 URR 计费（与计费族正交）。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。IM 无线管控依赖 SA-Basic 的协议识别——须激活特征库（`LOD SIGNATUREDB`+`LOD PARSERDB`）+ SA-IM 子特性的 IM 协议特征（QQ/MSN/微信等）+ `ADD WELLKNOWNPORT` 加速识别。License `LKV3G5SABS01`（控制项 82209749）须开启。

### UDG 基础：PCC 基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task）。IM 无线管控复用其 PCCPOLICYGRP+RULE+USERPROFILE 骨架——配置重叠，但 RULE 的 `POLICYTYPE=REMARK_FPI` 是 IM 专属变种（区别 BWM 的 `POLICYTYPE=BWM`）。License `LKV3G5PCCB01`（控制项 82209737）须开启。

### 跨网元/跨特性协同

- **顺序**：SA-Basic 协议识别链就绪（含 SA-IM 子特性）→ PCCPOLICYGRP+RULE(POLICYTYPE=REMARK_FPI)+USERPROFILE 骨架就绪 → 过滤链就绪（三四层 ANY + 七层 `ADD PROTBINDFLOWF` 绑 IM 协议名）→ `MOD USERPROFILE:ALIASMARKFLAG=DISABLE`（禁用 Alias Marking）→ `SET REFRESHSRV`。
- **一致性**：RULE 引用的 FLOWFILTERNAME + USERPROFILENAME 跨规则一致；FPIVALUE（DSCP 映射值）全网规划（与 RAN 侧调度权重对应）。
- **无线侧必须支持**：要求无线侧网元（BSC/RNC）同时支持基于 DSCP 的无线资源优化——且 **UDG+BSC/RNC 均为华为设备**（华为私有方式）。非华为设备时 DSCP 标记不生效。

## 决策点

### DP-1：IM 协议范围

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 单 IM 协议（如仅 QQ） | `ADD PROTBINDFLOWF:PROTOCOLNAME=qq_im`；单协议标记 |
| 多 IM 协议（QQ+MSN+微信等） | 逐协议 `ADD PROTBINDFLOWF`（qq_im / msn_im / wechat_im 等）；多 RULE 或单 RULE 多 FILTER |
| 全 IM 协议族 | 按 SA-IM 子特性支持的协议全集配；须确认 SA-IM 特征库覆盖范围 |

### DP-2：DSCP 标记方式（Alias Marking 开关）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 禁用 Alias Marking（DSCP 标记生效，华为私有） | `MOD USERPROFILE:ALIASMARKFLAG=DISABLE`；UDG 改写报文 ToS 域；仅 UDG+BSC/RNC 均华为设备支持 |
| 启用 Alias Marking（默认，DSCP 标记不生效） | 不执行 MOD 或 `ALIASMARKFLAG=ENABLE`；系统不改写报文 ToS 域；IM 无线管控不生效 |

## 约束

- **License 前置**（critical）：UDG `LKV3G5WIMR01`（020359）+ `LKV3G5SABS01`（SA-Basic）+ `LKV3G5PCCB01`（PCC基本功能）—— 三个 License 须同时开启。
- **依赖 SA-Basic + SA-IM 子特性**（critical）：IM 协议识别依赖 SA-Basic 特征库 + SA-IM 子特性的 IM 协议特征——未激活则 `PROTOCOLNAME=qq_im` 等引用无效。
- **依赖 PCC 基本功能**（critical）：PCRF 下发 PCC 规则通道——PCC backbone 未配则 RULE 无 PCCPOLICYGRP 可绑。
- **MOD USERPROFILE 禁用 Alias Marking**（critical，★ 华为私有核心）：`ALIASMARKFLAG=DISABLE` 须配——否则 DSCP 标记不生效，IM 无线管控失效。仅 UDG+BSC/RNC 均为华为设备时支持。
- **无线侧必须支持 + 华为设备**（critical）：要求无线侧网元（BSC/RNC）支持基于 DSCP 的无线资源优化——且 UDG+BSC/RNC 均为华为设备。非华为设备时本方案不适用。
- **RULE POLICYTYPE=REMARK_FPI 专属**（warning）：IM 无线管控的 RULE 须 `POLICYTYPE=REMARK_FPI`（非 BWM/PCC）——混用导致标记错位。
- **加密协议不可识别**（info）：加密 IM 协议（如端到端加密）报文 SA 无法识别——不在本方案覆盖范围。
- **与 BWM 正交**（info）：不共享 BWM 对象族，可与 BWM 共存——不会互相干扰。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 相邻方案：[FPI 业务流标识无线优化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-fpi-optimization.md)（机制相近，均用 REMARK_FPI；本方案专聚焦 IM + DSCP 标记方式华为私有）
- 编排特性（feature task，优先）：[2-00022 UDG IM无线](task/UDG/20.15.2/2-00022.md)（核心）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提，含 SA-IM 子特性）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（PCC 通道依赖）
- 证据：[UDG 020359 IM无线 特性概述](evidence/business/bandwidth-control/UDG_020359_GWFD-020359 IM类业务无线资源管控特性概述_39436333.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) · [UDG PCC基本功能](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md)
