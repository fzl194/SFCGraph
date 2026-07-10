---
id: ConfigurationSolution@bandwidth-shaping
type: ConfigurationSolution
name: 业务整形（Shaping）
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# 业务整形（Shaping）

> 基于业务的流量整形方案——超速率报文缓存整形而非直接丢弃，实现稳定发送速率。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。在 [BWM 基础限速](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md) 范本上派生，核心变种为 BWMCONTROLLER 改 SHAPING 模式。

## 概览

业务整形（Shaping）解决"超速报文需缓存平滑转发而非直接丢弃"的诉求：对识别为指定业务类型的用户业务流，超速率报文进入队列缓存后平稳转发，避免 CAR 三色直接丢包造成的抖动。方案包含两个层次——**用户级 Shaping**（[020354](task/UDG/20.15.2/2-00023.md) 基础）+ **组级智能 Shaping**（[110313](task/UDG/20.15.2/2-00024.md) 组内用户公平调度增强），均复用 BWM 对象族（BWMSERVICE→BWMCONTROLLER→BWMUSERGROUP→BWMRULE），差异仅在 BWMCONTROLLER 走 SHAPING（RATE/QUEDEPTH/MAXFDNUM）而非 CAR（CIR/CBS/PIR/PBS/三色）。

协同骨架：UDG 用户面 UPF 执行实际整形；BWMCONTROLLER.SHAPING 是核心控制对象；SA-Basic 提供业务识别前提（Protocol 场景）；PCC 通道可选承载（动态 PCC 时）。

## 配置与协同

本方案编排 **5 个特性**：UDG 核心 [2-00023 业务Shaping](task/UDG/20.15.2/2-00023.md) + UDG 核心（组级增强）[2-00024 智能Shaping](task/UDG/20.15.2/2-00024.md) + UDG 基础 [2-00001 BWM](task/UDG/20.15.2/2-00001.md)（依赖前提）+ UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)（License 前置）+ UDG 策略通道 [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md)（可选）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [020354 业务Shaping](task/UDG/20.15.2/2-00023.md) | 核心（用户级 SHAPING） | 必配 | BWM CONTROLLER 的 SHAPING 模式用户级特化；仅用户级（SUBSCRIBER_SPECIFIC）生效；配置重叠（BWMCONTROLLER 的 CTRLTYPE=SHAPING，复用 BWM 对象族） |
| [110313 智能Shaping组级](task/UDG/20.15.2/2-00024.md) | 核心（组级 SHAPING 公平增强） | 按需（组级整形时） | 突破基础 BWM 组级不能 SHAPING 的专用增强；依赖 020354+110311；配置重叠（同一 BWMCONTROLLER 叠加 USERFAIREN/WORKMODE 智能参数）；不重建 BWM 对象族 |
| [BWM 110311](task/UDG/20.15.2/2-00001.md) | 基础（依赖前提） | 必配 | Shaping 是 BWM CONTROLLER 模式特化，共享 BWM 对象族骨架；配置重叠（BWMSERVICE/BWMUSERGROUP/BWMRULE/APNBINDBWMUSRG 全复用） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配（License 前置） | 业务识别前提——Protocol 场景须先激活特征库；配置不重叠（SA 配识别链，BWM 配限速对象，对象集不同） |
| [PCC基本功能](task/UDG/20.15.2/2-00018.md) | 策略通道 | 可选 | 动态 PCC（PCRF/PCF 下发 Shaping 规则）时配；本地静态规则可不配 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：业务 Shaping（[2-00023](task/UDG/20.15.2/2-00023.md)）

走标准配置方法（见 feature task）。**本方案的核心变种**：BWMCONTROLLER 走 SHAPING 模式——参数集为 `RATE/QUEDEPTH/MAXFDNUM`（非 CAR 的 CIR/CBS/PIR/PBS/三色），两套参数集**正交不可混配**（同一控制器不能同时带 SHAPING 的 RATE 和 CAR 的 CIR）。License 控制项为 `LKV3G5SBTS01`（与 BWM 主特性 `LKV3G5TCSA01` 不同——Shaping 是独立 License）。

**排除项**：本特性按 TOS 直接识别，不走 PCC 规则链，故配置流程不含 FILTER/PCCPOLICYGRP/RULE/USERPROFILE（若实际部署需 PCC 联动，参考 [1-00004](task/UDG/20.15.2/1-00004.md) PCC 链 + [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链）。

### UDG 核心增强：智能 Shaping 组级公平（[2-00024](task/UDG/20.15.2/2-00024.md)）

**本方案的关键扩展**——组级智能公平调度。走标准配置方法（见 feature task）。**变种**：在已有 SHAPING 控制器上叠加智能参数——`USERFAIREN=ENABLE`（组级公平总开关）+ `WORKMODE=MANUAL|AUTO`（二选一）+ `SRVLEVELSPEC`（业务等级数上限）+ `BCSRVLEVELPLY`（每 ServiceLevel 策略）。**AUTO 模式专属三参数**（MAXPKTLOSTRATE/PKTLOSTRATEDTL/ASSUREMODE）须同配。License 控制项 `LKV3G5FSHP01`。

**不重建 BWM 对象族**——假定上游 BWM 基础（BWMSERVICE/BWMUSERGROUP/BWMRULE/绑定）已配，仅增强控制器。"组级公平"是组内用户的**用户级**公平（SUBSCRIBER_SPECIFIC 规则），非 GROUP_SPECIFIC 规则——承继 020354 约束。

### UDG 基础：BWM（[2-00001](task/UDG/20.15.2/2-00001.md)）

走标准配置方法（见 feature task，BWM 范本）。Shaping 方案复用 BWM 全套对象族骨架（9 场景 DP 驱动控制层级/识别方式/触发维度），**仅 CTRLTYPE 由 CAR 改 SHAPING**——配置高度重叠，不需额外配一遍 BWM。

### UDG SA 识别：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。Protocol 场景（HTTP 用户整形）须先激活 SA 特征库 `LOD SIGNATUREDB`+`LOD PARSERDB`+`ADD WELLKNOWNPORT`，否则 PROTOCOLNAME 引用无效。

### 跨网元/跨特性协同

- **顺序**：SA-Basic 协议识别链就绪 → BWM 对象族骨架就绪（BWMSERVICE/BWMUSERGROUP/BWMRULE/APNBINDBWMUSRG）→ BWMCONTROLLER 改 SHAPING 模式（020354 基础）→ 智能参数叠加（110313 组级，按需）→ `SET REFRESHSRV`（PROTBINDFLOWF 后 60s，最后生效）。
- **一致性**：UDG 内 BWMRULE.BWMSERVICENAME/BWMCONTROLLERNAME/BWMUSERGROUPNAME 一致；SHAPING 控制器与 CAR 控制器不可混配（同一规则引用的控制器类型须统一）。

## 决策点

### DP-1：Shaping 控制层级（用户级 vs 组级公平）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 用户级 Shaping（基础，020354） | BWMRULETYPE=SUBSCRIBER_SPECIFIC；BWMCONTROLLER 仅 RATE/QUEDEPTH/MAXFDNUM；走 [1-00002](task/UDG/20.15.2/1-00002.md)+[1-00003](task/UDG/20.15.2/1-00003.md) |
| 组级智能 Shaping（公平增强，110313） | 在用户级基础上叠加 USERFAIREN=ENABLE + WORKMODE（MANUAL/AUTO 二选一）+ BCSRVLEVELPLY；走 [1-00002](task/UDG/20.15.2/1-00002.md)+[0-00108](task/UDG/20.15.2/0-00108.md) |

### DP-2：组级工作模式（MANUAL vs AUTO）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| MANUAL（手动公平） | WORKMODE=MANUAL；无 AUTO 三参数；每 ServiceLevel 手动配 BCSRVLEVELPLY.SHAPRATE；QUEDEPTH 样例 25 |
| AUTO（智能公平，推荐） | WORKMODE=AUTO + MAXPKTLOSTRATE + PKTLOSTRATEDTL + ASSUREMODE(EXPFIRST/BWDFIRST)；系统自动算丢包率；QUEDEPTH 建议加深（样例 40） |

## 约束

- **SHAPING 仅用户级**（critical，★ Shaping 方案核心）：CTRLTYPE=SHAPING 仅 `SUBSCRIBER_SPECIFIC` 支持；组级（GROUP_SPECIFIC/GROUP_DEFAULT）/整机级（GLOBAL）只能 CAR。110313"组级公平"是组内用户级公平，非 GROUP_SPECIFIC 规则——违反则配置失败或语义错位。
- **SHAPING 与 CAR 参数集正交不可混配**（critical）：同一 BWMCONTROLLER 不能同时带 RATE（SHAPING）和 CIR（CAR）——命令参数校验失败。
- **License 三前置**（critical）：`LKV3G5SBTS01`（020354 Shaping）+ `LKV3G5FSHP01`（110313 智能Shaping，组级时）+ `LKV3G5SABS01`（SA-Basic）—— 全部开启后 Shaping 才生效。
- **USERFAIREN 必 ENABLE**（critical，110313）：组级公平调度总开关——DISABLE 则退化为普通 Shaping，与 110313 语义冲突。
- **AUTO 三参数必同配**（warning，110313）：WORKMODE=AUTO 时 MAXPKTLOSTRATE/PKTLOSTRATEDTL/ASSUREMODE 须同时给——缺一则自动计算无依据。
- **SRVLEVELSPEC 上限**（warning，110313）：最大 15；BCSRVLEVELPLY 的 SERVICELEVEL 须 ≤ SRVLEVELSPEC。
- **REFRESHSRV 时序**（critical）：`SET REFRESHSRV` 必须最后执行，PROTBINDFLOWF 后等待 60 秒——不执行则配置变更不生效。
- **MAXFDNUM 规划**（info）：整形队列可追踪五元组流数上限，超限新流不被整形——按用户规模规划。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 范本派生：[BWM 基础限速](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md)（本方案在其上派生，复用 BWM 对象族）
- 编排特性（feature task，优先）：[2-00023 UDG 业务Shaping](task/UDG/20.15.2/2-00023.md)（用户级核心）· [2-00024 UDG 智能Shaping组级](task/UDG/20.15.2/2-00024.md)（组级公平增强）· [2-00001 UDG BWM](task/UDG/20.15.2/2-00001.md)（基础依赖）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（可选策略通道）
- 复用步骤/命令（compound/atom，按需）：UDG [1-00002](task/UDG/20.15.2/1-00002.md) 业务与控制器（SHAPING 变种）· [1-00003](task/UDG/20.15.2/1-00003.md) 用户组规则绑定 · [1-00001](task/UDG/20.15.2/1-00001.md) License+APN 前置 · [0-00108](task/UDG/20.15.2/0-00108.md) BCSRVLEVELPLY（110313 业务等级策略，Shaping 范式）· [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV
- 证据：[UDG 020354 Shaping 特性概述](evidence/business/bandwidth-control/UDG_020354_GWFD-020354 基于业务的Shaping特性概述_83823121.md) · [UDG 110313 智能Shaping 特性概述](evidence/business/bandwidth-control/UDG_110313_GWFD-110313 基于智能Shaping的组级带宽控制特性概述_76026865.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) · [BWM 主干](evidence/business/bandwidth-control/GWFD-110311 基于业务感知的带宽控制特性概述_77219469.md)
