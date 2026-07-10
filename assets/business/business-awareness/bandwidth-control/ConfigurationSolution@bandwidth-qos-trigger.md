---
id: ConfigurationSolution@bandwidth-qos-trigger
type: ConfigurationSolution
name: QoS 触发保证（GBR）
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# QoS 触发保证（GBR）

> 为关键业务（语音/视频）建立专有承载/QoS Flow 提供 GBR 带宽保证方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。与 BWM（CAR/Shaping 上限控制）正交独立——本方案做 GBR 下限保证（专用资源）。

## 概览

业务触发的 QoS 保证解决"关键业务需保证带宽下限"的诉求：用户请求需要 QoS 保障的业务（VoNR/视频）时，UDG 基于匹配的预定义规则向 PGW-C/SMF 上报 QoS 事件，发起专有承载激活/专有 QoS Flow 建立，提供 GBR（保证比特率）/MBR（最大比特率）保证。核心对象链：`URR(QOS) + QOSPROP(GBR/MBR→QOSURRNAME) + PCCPOLICYGRP(URRGROUPNAME+QOSPROPNAME)` → 过滤链 → `SADEDICBEARER`（七层触发）/ 报文匹配（三四层触发）→ `RULE(PCC) + USERPROFILE + RULEBINDING`。

**与 BWM 的核心区别**：BWM 做 CAR/Shaping（速率上限控制，共享带宽池），QoS 触发做 GBR（速率下限保证，专用资源）——两者正交独立，可共存于同一会话不同业务流。协同骨架：UDG 用户面识别业务 + 执行 QoS 策略；UNC 控制面下发预定义 PCC 规则触发 UDG 建承载；PCRF/PCF 侧下发 QoS 规则。

## 配置与协同

本方案编排 **4 个特性**跨网元：UDG 核心 [2-00029 QoS触发](task/UDG/20.15.2/2-00029.md) + UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md) + UDG 基础 [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md) + UNC 跨网元对端 [2-00008 QoS触发 WSFD-109107](task/UNC/20.15.2/2-00008.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [020358 QoS触发](task/UDG/20.15.2/2-00029.md) | 核心 | 必配 | 用 PCRF 下发的 QoS 参数建专有承载/QoS Flow（GBR）；**与 BWM 正交，不共享 BWM 对象族**——QoS 用 URR(QOS)+QOSPROP，BWM 用 BWMSERVICE/BWMCONTROLLER |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | 业务识别——七层触发（SADEDICBEARER PROTOCOLLEVEL=PROTOCOL）必需 SA 协议识别；配置不重叠（SA 配识别链，QoS 配 QOSPROP/专有承载） |
| [PCC基本功能](task/UDG/20.15.2/2-00018.md) | 基础（依赖前提） | 必配 | 从 PCRF/PCF 获取 QoS 规则——PCCPOLICYGRP 绑 QOSPROPNAME；配置重叠（复用 PCCPOLICYGRP/RULE/USERPROFILE 骨架，但 PCCPOLICYGRP 绑 QOSPROPNAME 非 URRGROUPNAME 为主） |
| [UNC 109107](task/UNC/20.15.2/2-00008.md) | 跨网元对端 | 必配 | UNC 下发预定义 PCC 规则触发 UDG 建承载——QoS 属性与规则绑定链 + UserProfile 组 APN 绑定；与 UDG 020358 组合 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：业务触发 QoS 保证（[2-00029](task/UDG/20.15.2/2-00029.md)）

走标准配置方法（见 feature task）。**本方案核心变种**：

- **QoS URR 上报模式固定 QOS**：`ADD URR` 须 `USAGERPTMODE=QOS`（非计费的 ONLINE/OFFLINE，也非 FUP 的 MONITORINGKEY）——QoS 事件上报专属。
- **QOSPROP 绑 GBR/MBR**：`ADD QOSPROP` 配 `QOSURRNAME + GBRUPLKVALUE/GBRDNLKVALUE + MBRUPLKVALUE/MBRDNLKVALUE`，保证比特率须 ≤ 最大比特率。
- **PCCPOLICYGRP 绑 QOSPROPNAME**：须同时绑 URRGROUPNAME + QOSPROPNAME（漏绑则 QoS 保证不生效）——区别于 BWM 的 PCCPOLICYGRP（不绑 QOSPROPNAME）和计费的 PCCPOLICYGRP（绑 URRGROUPNAME 为主）。
- **两种触发方式**（DP-1）：七层触发（L7FILTER+PROTBINDFLOWF+WELLKNOWNPORT+SADEDICBEARER，依赖 SA）/ 三四层触发（仅 FILTER，按报文匹配，无 SADEDICBEARER）。

**排除项**：不走 BWM 对象族（无 BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE）；不走 FUP 双轨 URR（QoS URR 单轨 USAGERPTMODE=QOS）。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。七层触发场景必需——SADEDICBEARER.PROTOCOLLEVEL=PROTOCOL 时需 SA 识别协议（WELLKNOWNPORT 加速 + 过滤链 PROTBINDFLOWF）。三四层触发不需要 SA（按报文匹配）。

### UDG 基础：PCC 基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task）。QoS 复用其 PCCPOLICYGRP+RULE+USERPROFILE 骨架——配置重叠，但 PCCPOLICYGRP 绑 QOSPROPNAME 是 QoS 专属变种（区别 BWM 的 POLICYTYPE=BWM）。

### UNC 跨网元对端：业务触发 QoS 保证（[2-00008](task/UNC/20.15.2/2-00008.md) WSFD-109107）

走标准配置方法（见 feature task）。UNC 侧下发预定义 PCC 规则触发 UDG 建承载——QoS URR（USAGERPTMODE=QOS）+ QOSPROP（GBR/MBR/5QI/QCI/ARP）+ PCCPOLICYGRP + RULE + USERPROFILE + RULEBINDING +（本地 PCC 时）USRPROFGROUP + APN 挂接。

### 跨网元/跨特性协同

- **顺序**：SA-Basic 协议识别链就绪（七层触发时）→ 过滤链就绪（FILTER+FLOWFILTER+FLTBINDFLOWF，七层加 L7FILTER+PROTBINDFLOWF）→ QoS URR + QOSPROP + URRGROUP + PCCPOLICYGRP 就绪 →（七层）WELLKNOWNPORT + SADEDICBEARER 就绪 → RULE+USERPROFILE+RULEBINDING → UNC 侧预定义规则 + APN 挂接就绪 → `SET REFRESHSRV`。
- **一致性**：QOSPROP.QOSURRNAME 引用一致（须引已配 QoS URR）；跨网元 RULENAME/USERPROFILENAME 一致；QCI/ARP/5QI 跨网元一致（专有承载 QoS 属性）。
- **与 BWM 正交**：QoS 保证（GBR 下限）与 BWM（CAR/Shaping 上限）可共存——同一会话不同业务流各走各的，对象族不冲突。

## 决策点

### DP-1：触发方式（七层 vs 三四层）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 七层触发（SA 识别协议，如 HTTP 下行） | 过滤链含 L7FILTER+PROTBINDFLOWF（PROTOCOLNAME）；需 WELLKNOWNPORT 加速识别；需 SADEDICBEARER（TRIGGERMODE=DOWNLINK_ONLY/UPLINK_ONLY/BOTH）；依赖 SA-Basic；走 [1-00009](task/UDG/20.15.2/1-00009.md)（含 L7 段）+[1-00016](task/UDG/20.15.2/1-00016.md)+[1-00017](task/UDG/20.15.2/1-00017.md) |
| 三四层触发（按报文匹配） | 过滤链仅 FILTER+FLOWFILTER+FLTBINDFLOWF（无 L7）；无 WELLKNOWNPORT/SADEDICBEARER；可选 BIT1104 软参；不依赖 SA（但 License 前置仍需）；走 [1-00009](task/UDG/20.15.2/1-00009.md)（仅 L34 段）+[1-00017](task/UDG/20.15.2/1-00017.md)（仅 QOSPROP 段） |

### DP-2：SADEDICBEARER.TRIGGERMODE（七层触发子选项）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| DOWNLINK_ONLY（activation 演示） | 下行报文触发专有承载创建；UDG 创建 l7-downlink 模板，上行走原承载 |
| UPLINK_ONLY | 上行报文触发专有承载创建 |
| BOTH | 上下行均触发 |
| NOT_TRIGGER（默认） | 不触发（须显式配为上述三值才生效） |

## 约束

- **License 前置**（critical）：UDG `LKV3G5STQE01`（020358）—— 未开则 QoS 保证功能不生效。
- **依赖 SA-Basic + PCC**（critical）：七层触发必需 SA-Basic 识别协议；PCC 基本功能从 PCRF/PCF 获取规则——缺一则 QoS 保证不工作。
- **QoS URR 上报模式固定 QOS**（critical）：`USAGERPTMODE=QOS` 固定取值——非 QOS 则 QoS 事件上报失效。
- **QOSPROP.QOSURRNAME 引用一致**（critical）：须引用已配的 QoS URR——不一致则 QoS 属性引用断链。
- **PCCPOLICYGRP 绑 QOSPROPNAME**（critical）：须同时绑 URRGROUPNAME + QOSPROPNAME——漏绑则 QoS 保证不生效。
- **GBR ≤ MBR**（warning）：保证比特率须 ≤ 最大比特率——否则 QoS 无法保证。
- **七层触发依赖协议识别**（critical）：SADEDICBEARER.PROTOCOLLEVEL=PROTOCOL 时需 WELLKNOWNPORT + PROTBINDFLOWF——未识别则专有承载不触发。
- **并发链路流 ≤ 8**（info）：为避免信令风暴，并发链路流小于 8 个协议才适合流触发专有承载。
- **仅支持 HTTP1.x**（info）：不支持 HTTP2.0、不支持加密场景基于 host 的计费和控制。
- **互斥特性**（info）：与 ULCL 分流（GWFD-020501）、专网业务触发专载（GWFD-020531）不能同时开启。
- **双栈需 IPMASK**（warning）：双栈地址 + AnyToAny 规则触发专有承载时，`SET UPGLBPMPARA.FLOWDANYFMT` 须配 IPMASK。
- **与 BWM 正交**（info）：QoS 保证不共享 BWM 对象族，可与 BWM 共存——不会互相干扰。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 编排特性（feature task，优先）：[2-00029 UDG QoS触发](task/UDG/20.15.2/2-00029.md)（核心）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（PCC 通道依赖）· [2-00008 UNC QoS触发 WSFD-109107](task/UNC/20.15.2/2-00008.md)（跨网元对端）
- 复用步骤/命令（compound/atom，按需）：UDG [1-00017](task/UDG/20.15.2/1-00017.md) QoS专有承载链（QOSPROP+SADEDICBEARER）· [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套·QoS 变体 · [1-00016](task/UDG/20.15.2/1-00016.md) SA协议识别（七层触发）· [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV · [0-00297](task/UDG/20.15.2/0-00297.md) UPGLBPMPARA（双栈收尾）；UNC [1-00017](task/UNC/20.15.2/1-00017.md) QoS 属性与规则绑定链
- 证据：[UDG 020358 QoS触发 特性概述](evidence/business/bandwidth-control/UDG_020358_GWFD-020358 业务触发的QoS保证特性概述_80966039.md) · [UNC 109107 QoS触发 特性概述](evidence/business/bandwidth-control/UNC_109107_特性概述_85397056.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) · [UDG PCC基本功能](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md)
