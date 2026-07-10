---
id: ConfigurationSolution@bandwidth-adc-trigger
type: ConfigurationSolution
name: ADC 应用检测触发
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# ADC 应用检测触发

> 基于 ADC（应用检测与控制）识别 L7 应用上报 PCRF/PCF 触发应用级带宽策略的方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。ADC 是 BWM/QoS 等带宽策略的**上游触发源**——检测到应用后由 PCRF 下发策略（可能含 BWM/QoS）；不共享 BWM 对象族。

## 概览

ADC 应用检测触发解决"按应用类型（HTTP/P2P/视频等）动态触发带宽策略"的诉求：UDG（UPF/PGW-U）基于 SA+ADC 协议特征库检测 L7 应用 → 经 UNC（SMF/PGW-C）上报 PCRF/PCF（APPLICATION_START/STOP Event-Trigger 或 appid）→ PCRF/PCF 据此下发应用级 PCC 策略（可能含 BWM 限速、QoS 保障、访问限制等）→ UDG 执行。

**核心定位**：ADC 是**应用级策略触发通道**——本身不执行限速/整形，而是"检测→上报→PCRF 决策→下发策略"链路的上游触发源。PCRF 下发的策略类型决定下游走哪个 CS（BWM 限速 / QoS 保证 / 访问限制阻断等）。因此本方案与 BWM/QoS 等是**触发源与执行体**的关系——ADC 提供"应用检测上报"维度，BWM/QoS 提供"速率控制执行"维度，两者正交可叠加。

**两种规则下发方式**（UDG 侧 activation 演示二选一）：① 预定义规则（PCRF/PCF 下发 APPLICATION_START/STOP Event-Trigger，UDG 本地配全量 9 步）；② 动态规则下发（PCRF/PCF 直接下发 appid，UDG 本地仅配 ADCPARA + 计费属性最小集）。跨网元协同：UDG 用户面检测 + UNC 控制面中继上报 + PCRF/PCF 决策。

## 配置与协同

本方案跨网元编排 **4 个特性**：UDG 核心 [2-00028 增强ADC](task/UDG/20.15.2/2-00028.md) + UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md) + UDG 基础 [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md) + UNC 跨网元对端 [2-00006 ADC基本功能 WSFD-109102](task/UNC/20.15.2/2-00006.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [020357 增强ADC](task/UDG/20.15.2/2-00028.md) | 核心 | 必配 | UDG 检测 L7 应用上报 PCRF/PCF——ADC 是 BWM/QoS 等带宽策略的**上游触发源**（ADC→PCRF→PCC 规则，可能含 BWM）；**不共享 BWM 对象族**（ADC 用 ADCPARA+PCCPOLICYGRP(ADCMUTEFLAG) + ADC/PCC 规则，BWM 用 BWMSERVICE 等）；与 PCC 正交（ADC=应用检测维度，PCC=策略通道维度） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | 应用识别基础——ADC 协议特征库依赖 SA-Basic 的特征库+解析库底座；配置不重叠（SA 配识别链底座，ADC 配 ADCPARA+规则） |
| [PCC基本功能](task/UDG/20.15.2/2-00018.md) | 基础（依赖前提） | 必配 | 原文"必须同时开启 PCC 基本功能"——PCCPOLICYGRP+RULE+USERPROFILE 骨架为 ADC 规则链载体；配置重叠（复用 PCCPOLICYGRP/RULE/USERPROFILE 骨架，但 PCCPOLICYGRP 的 ADCMUTEFLAG=DISABLE 是 ADC 专属变种） |
| [UNC 109102 ADC](task/UNC/20.15.2/2-00006.md) | 跨网元对端 | 必配 | UNC 控制面中继——转发 UDG 检测的应用信息 + 承载 PCRF 下发策略；与 UDG 020357 组合；两条路径（动态规则下发 appid / 预定义规则下发 Event-Trigger）二选一 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：增强的 ADC 基本功能（[2-00028](task/UDG/20.15.2/2-00028.md)）

走标准配置方法（见 feature task，9 步/最小集二选一）。**本方案核心变种**：

- **ADCPARA 流信息上报开关**（核心变种）：`ADD ADCPARA` 配流信息上报开关——ADC 检测到应用后是否上报 PCRF/PCF 的控制开关。区别于 BWM 的 BWMSERVICE。
- **PCCPOLICYGRP ADCMUTEFLAG=DISABLE**（ADC 专属变种）：`ADD PCCPOLICYGRP:ADCMUTEFLAG=DISABLE`——允许 ADC 检测结果触发 PCC 策略。区别于 BWM 的 `POLICYTYPE=BWM` 和计费的无 ADCMUTEFLAG。
- **两条规则下发路径**（DP-1，二选一）：① 预定义规则（PCRF 下发 APPLICATION_START/STOP Event-Trigger，UDG 本地配全量 9 步：三四层+七层 URL+ADCPARA+计费属性+PCC 策略组+ADC/PCC 规则+用户模板绑定）；② 动态规则下发（PCRF 直接下发 appid，UDG 本地仅配 ADCPARA+计费属性最小集）。
- **License**：`LKV3G5ADCF01`（控制项 82209755）。

**排除项**：不走 BWM 对象族（无 BWMSERVICE/BWMCONTROLLER/BWMRULE，与 BWM 正交——ADC 是触发源，BWM 是执行体）；不建专有承载（无 SADEDICBEARER/QOSPROP，与 QoS 触发正交）；ADC 本身不执行限速（执行由 PCRF 下发的下游策略决定）。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。ADC 协议特征库依赖 SA-Basic 的特征库+解析库底座——须激活（`LOD SIGNATUREDB`+`LOD PARSERDB`）+ `ADD WELLKNOWNPORT` 加速识别。七层 URL 检测场景须配 L7FILTER+PROTBINDFLOWF。License `LKV3G5SABS01`（控制项 82209749）须开启。

### UDG 基础：PCC 基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task）。ADC 复用其 PCCPOLICYGRP+RULE+USERPROFILE 骨架——配置重叠，但 PCCPOLICYGRP 的 `ADCMUTEFLAG=DISABLE` 是 ADC 专属变种。License `LKV3G5PCCB01`（控制项 82209737）须开启。

### UNC 跨网元对端：ADC 基本功能（[2-00006](task/UNC/20.15.2/2-00006.md) WSFD-109102）

走标准配置方法（见 feature task）。UNC 侧承担控制面中继角色——转发 UDG 检测的应用信息给 PCRF/PCF + 承载 PCRF/PCF 下发的策略经 N4 透传 UDG。两条配置路径（动态规则下发 appid / 预定义规则下发 Event-Trigger）二选一，与 UDG 侧路径一致。License `LKV2ADCBF01`+`LKV3W9SADC11`（控制项 82207979）须开启。

### 跨网元/跨特性协同

- **顺序**：SA-Basic 协议识别链就绪（含 ADC 特征库）→ UDG 侧 ADCPARA + PCCPOLICYGRP(ADCMUTEFLAG=DISABLE) + 过滤链 + ADC/PCC 规则 + USERPROFILE 就绪 → UNC 侧 PCC Gx/N7 通道就绪 + ADC 中继配置就绪 → `SET REFRESHSRV` → 运行时：UDG 检测应用 → 经 UNC 上报 PCRF/PCF → PCRF/PCF 下发策略（可能含 BWM/QoS）→ UDG 执行。
- **一致性**：跨网元 RULENAME/USERPROFILENAME 一致；appid（动态规则下发路径）跨网元一致；APPLICATION_START/STOP Event-Trigger（预定义规则路径）PCRF 侧须订阅。
- **PCRF 须配置应用响应策略**：PCRF/PCF 侧须订阅 APPLICATION_START/STOP（或支持 appid 下发）+ 配置应用级响应策略——否则 ADC 上报后无策略下发。
- **与 BWM/QoS 正交叠加**：ADC 是触发源，BWM/QoS 是执行体——ADC 检测到 P2P 应用后，PCRF 可下发 BWM 限速策略（叠加 BWM CS）；或检测到视频后下发 QoS 保证（叠加 QoS CS）。对象族不冲突。

## 决策点

### DP-1：规则下发方式（预定义规则 vs 动态规则下发）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 预定义规则（UDG 本地全量配） | PCRF/PCF 下发 APPLICATION_START/STOP Event-Trigger；UDG 本地配全量 9 步（三四层+七层 URL+ADCPARA+计费属性+PCC 策略组+ADC/PCC 规则+用户模板绑定）；控制粒度细 |
| 动态规则下发（UDG 本地最小集） | PCRF/PCF 直接下发 appid；UDG 本地仅配 ADCPARA+计费属性最小集；配置简洁，依赖 PCRF 规则库完整 |

### DP-2：应用检测范围

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| HTTP/URL 应用 | 七层 URL 检测——L7FILTER+PROTBINDFLOWF 绑定 URL 规则；依赖 SA URL 特征库 |
| P2P 应用 | 协议特征检测——PROTBINDFLOWF 绑定 P2P 协议名；依赖 SA P2P 特征库 |
| 全应用族 | 按 ADC+SA 支持的应用全集配；须确认特征库覆盖范围 |

## 约束

- **License 前置**（critical）：UDG `LKV3G5ADCF01`（020357，控制项 82209755）+ `LKV3G5SABS01`（SA-Basic）+ `LKV3G5PCCB01`（PCC基本功能）+ UNC `LKV2ADCBF01`+`LKV3W9SADC11`（109102，控制项 82207979）—— 未开则 ADC 检测/上报功能不生效。
- **依赖 SA-Basic**（critical）：ADC 协议特征库依赖 SA-Basic 的特征库+解析库底座——未激活则应用识别失效。
- **必须同时开启 PCC 基本功能**（critical，原文明示）：UDG+UNC 两侧 PCC 基本功能须开启——PCC backbone 未配则 ADC 规则链无载体、上报通道断裂。
- **PCCPOLICYGRP ADCMUTEFLAG=DISABLE**（critical）：须显式配 `ADCMUTEFLAG=DISABLE`——否则 ADC 检测结果被静默，不触发 PCC 策略。
- **PCRF 须配置应用响应策略**（critical）：PCRF/PCF 侧须订阅 APPLICATION_START/STOP（或支持 appid 下发）+ 配置应用级响应策略——否则 ADC 上报后无策略下发。
- **规则下发方式两侧一致**（warning）：UDG 与 UNC 侧的规则下发路径（预定义规则 / 动态规则下发）须一致——不一致则上报/下发链路错位。
- **ADC 是触发源非执行体**（critical，★ 定位澄清）：ADC 本身不执行限速/整形——执行由 PCRF 下发的下游策略决定（可能叠加 BWM/QoS CS）。在 UDG 配 BWM 对象族不会触发 ADC 链路。
- **加密协议不可检测**（info）：SSL/FTPS 等加密协议报文 ADC 无法基于 host 检测——不在本方案覆盖范围。
- **仅支持 HTTP1.x**（info）：不支持 HTTP2.0 基于 host 的检测。
- **与 BWM/QoS 正交**（info）：不共享 BWM/QoS 对象族，可作为 BWM/QoS 的上游触发源叠加——不会互相干扰。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 相邻方案：[BWM 基础限速](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md)（ADC 触发后 PCRF 可下发 BWM 限速策略）· [QoS 触发保证](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-qos-trigger.md)（ADC 触发后 PCRF 可下发 QoS 保证策略）
- 编排特性（feature task，优先）：[2-00028 UDG 增强ADC](task/UDG/20.15.2/2-00028.md)（核心）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（应用识别前提）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（PCC 通道依赖）· [2-00006 UNC ADC基本功能 WSFD-109102](task/UNC/20.15.2/2-00006.md)（跨网元对端）
- 证据：[UDG 020357 增强ADC 特性概述](evidence/business/bandwidth-control/UDG_020357_GWFD-020357 增强的ADC基本功能特性概述_84866818.md) · [UNC 109102 实现原理(N7)](evidence/business/bandwidth-control/UNC_109102_实现原理(N7)_92582135.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) · [UDG PCC基本功能](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md)
