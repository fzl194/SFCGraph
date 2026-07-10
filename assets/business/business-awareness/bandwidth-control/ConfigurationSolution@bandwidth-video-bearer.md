---
id: ConfigurationSolution@bandwidth-video-bearer
type: ConfigurationSolution
name: 视频承载信令控制（上下行解耦）
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# 视频承载信令控制（上下行解耦）

> 视频业务上下行解耦的专有承载 QoS 保证方案——上行走缺省承载，下行走专有承载。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。与 [QoS 触发保证](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-qos-trigger.md) 同族（QoS 专有承载链），核心差异在 QOSPROP 打开 DECOUPLINGSW=ENABLE（上下行解耦开关）。

## 概览

基于上下行解耦的视频承载信令控制解决"视频业务下行需专有承载 QoS 保证、上行用缺省承载"的诉求：UDG 识别特定视频业务，对其**下行链路**建立专有承载/专有 QoS Flow（无线侧基于 QoS 参数提供差异化调度），上行报文使用缺省承载转发。核心对象链：`URR(QOS) + QOSPROP(QOSURRNAME + DECOUPLINGSW=ENABLE)` + `PCCPOLICYGRP(URRGROUPNAME+QOSPROPNAME)` → 过滤链（三四层 + PROTBINDFLOWF）→ `RULE(PCC) + USERPROFILE + RULEBINDING`。

**与 [QoS 触发保证](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-qos-trigger.md) 的核心区别**：① QOSPROP 打开 `DECOUPLINGSW=ENABLE`（上下行解耦开关，硬性要求）② QOSPROP **不含 GBR/MBR 四档比特率**（仅 QOSURRNAME + DECOUPLINGSW）③ **无 SADEDICBEARER**——专有承载触发由 DECOUPLINGSW + 规则匹配驱动，不经 SA 专有承载命令 ④ PROTBINDFLOWF **无 L7FILTERNAME**（仅 PROTOCOLNAME）。两者均与 BWM 正交（不共享 BWM 对象族）。

## 配置与协同

本方案编排 **3 个特性**：UDG 核心 [2-00030 视频承载](task/UDG/20.15.2/2-00030.md) + UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md) + UDG 基础 [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [110302 视频承载](task/UDG/20.15.2/2-00030.md) | 核心 | 必配 | 上下行解耦的专有承载 QoS；**与 BWM 正交**——用 URR(QOS)+QOSPROP(DECOUPLINGSW)，不走 BWM 对象族；与 QoS 触发（020358）同族但 QOSPROP 参数集不同 |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | 视频业务识别——PROTBINDFLOWF.PROTOCOLNAME 须为 SA 可识别视频协议；配置不重叠（SA 配识别链） |
| [PCC基本功能](task/UDG/20.15.2/2-00018.md) | 基础（依赖前提） | 必配 | PCRF/PCF 下发规则建专有承载——PCCPOLICYGRP 绑 QOSPROPNAME；配置重叠（复用 PCCPOLICYGRP/RULE/USERPROFILE 骨架） |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：视频承载信令控制（[2-00030](task/UDG/20.15.2/2-00030.md)）

走标准配置方法（见 feature task）。**本方案核心变种**（与 QoS 触发 020358 的关键差异）：

- **QOSPROP 打开 DECOUPLINGSW=ENABLE**（硬性要求）：`ADD QOSPROP` 仅 `QOSPROPNAME + QOSURRNAME + DECOUPLINGSW=ENABLE` 三参数——**不含 GBR/MBR 四档比特率**（activation §数据规划表明示"必须配置为 ENABLE"）。
- **无 SADEDICBEARER**：专有承载触发由 DECOUPLINGSW + 规则匹配驱动，不经 SA 专有承载命令——区别于 QoS 触发的七层 SADEDICBEARER。
- **PROTBINDFLOWF 无 L7FILTERNAME**：`ADD PROTBINDFLOWF` 仅 `FLOWFILTERNAME + PROTOCOLNAME`（如 example_video），不建 L7FILTER 对象——区别于 QoS 触发的七层绑定含 L7FILTERNAME。
- **无 WELLKNOWNPORT**：activation 无此命令——区别于 QoS 触发七层场景。
- **License**：`LKV3G5SCUD01`（与 QoS 触发 `LKV3G5STQE01` 不同）。

**排除项**：不走 BWM 对象族（与 BWM 正交）；不走 SADEDICBEARER（DECOUPLINGSW 驱动）；QOSPROP 不配 GBR/MBR（仅解耦开关）。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。PROTBINDFLOWF 绑定的 PROTOCOLNAME（activation 演示 example_video）须为 SA 可识别的视频协议——未识别则规则匹配失效。

### UDG 基础：PCC 基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task）。视频承载复用其 PCCPOLICYGRP+RULE+USERPROFILE 骨架——配置重叠，但 PCCPOLICYGRP 绑的 QOSPROPNAME 指向含 DECOUPLINGSW=ENABLE 的 QOSPROP（视频解耦专属变种）。

### 跨网元/跨特性协同

- **顺序**：SA-Basic 协议识别链就绪 → 过滤链就绪（FILTER+FLOWFILTER+FLTBINDFLOWF+PROTBINDFLOWF，无 L7FILTER）→ `SET REFRESHSRV` → QoS URR + QOSPROP（DECOUPLINGSW=ENABLE）+ PCCPOLICYGRP（绑 QOSPROPNAME）→ RULE+USERPROFILE+RULEBINDING。
- **一致性**：QOSPROP.QOSURRNAME 引用一致；跨网元 RULENAME/USERPROFILENAME 一致；PROTBINDFLOWF.PROTOCOLNAME 须为可识别视频协议。
- **与 BWM 正交**：视频承载 QoS 保证不共享 BWM 对象族，可与 BWM 共存。

## 决策点

### DP-1：是否启用计费（PCCPOLICYGROUP.URRGROUPNAME）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 纯 QoS 保证（不计费，activation 注释） | PCCPOLICYGRP 仅绑 QOSPROPNAME，URRGROUPNAME 可省 |
| 计费变体 | PCCPOLICYGRP 绑 QOSPROPNAME + URRGROUPNAME（引用已配 URRGROUP） |

> activation 演示绑定 URRGROUPNAME=urrgp_test（"已配置数据中获取"），脚本注释"当需要计费时配置"——实际演示为配 URRGROUPNAME，注释为通用说明。

## 约束

- **License 前置**（critical）：`LKV3G5SCUD01`（110302）—— 未开则视频承载信令控制功能不生效。
- **依赖 SA-Basic + PCC**（critical）：SA 识别视频业务；PCC 从 PCRF/PCF 获取规则——缺一则不工作。
- **DECOUPLINGSW 必须 ENABLE**（critical，★ 本特性核心）：`ADD QOSPROP` 须 `DECOUPLINGSW=ENABLE`（activation 明示"必须配置为 ENABLE"）——非 ENABLE 则上下行解耦不生效，特性功能失效。
- **QoS URR 上报模式固定 QOS**（critical）：`USAGERPTMODE=QOS` 固定取值——非 QOS 则 QoS 事件上报失效。
- **QOSPROP.QOSURRNAME 引用一致**（critical）：须引用已配的 QoS URR——不一致则 QoS 属性引用断链。
- **PCCPOLICYGRP 绑 QOSPROPNAME**（critical）：须绑指向含 DECOUPLINGSW=ENABLE 的 QOSPROP——漏绑则上下行解耦不生效。
- **PROTBINDFLOWF.PROTOCOLNAME 须为可识别视频协议**（warning）：须为 SA 可识别的视频协议——未识别则规则匹配失效。
- **并发链路流 ≤ 8**（info）：为避免信令风暴，并发链路流小于 8 个协议才适合配置。
- **仅支持 HTTP1.x**（info）：不支持 HTTP2.0/HTTP3.0。
- **互斥特性**（info）：与 HTTP2.0 Host 识别（GWFD-110201）、HTTPS 业务地址识别（GWFD-110203）、GWFD-110251、GWFD-110252 不能同时开启（HTTP2.0 加密报文不支持）。
- **与 BWM 正交**（info）：不共享 BWM 对象族，可与 BWM 共存。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 同族方案：[QoS 触发保证](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-qos-trigger.md)（本方案在其上派生，QOSPROP 视频解耦变体 DECOUPLINGSW=ENABLE）
- 编排特性（feature task，优先）：[2-00030 UDG 视频承载](task/UDG/20.15.2/2-00030.md)（核心）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（PCC 通道依赖）
- 复用步骤/命令（compound/atom，按需）：UDG [1-00017](task/UDG/20.15.2/1-00017.md) QoS专有承载链（QOSPROP 视频解耦变体：DECOUPLINGSW=ENABLE，无 GBR/MBR，无 SADEDICBEARER）· [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链（PROTBINDFLOWF 无 L7FILTERNAME 变体）· [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套·QoS 变体 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV
- 证据：[UDG 110302 视频承载 特性概述](evidence/business/bandwidth-control/UDG_110302_GWFD-110302 基于上下行解耦的视频承载信令控制特性概述_59558143.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) · [UDG PCC基本功能](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md)
