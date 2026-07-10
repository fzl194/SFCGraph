---
id: ConfigurationSolution@charging-metering
type: ConfigurationSolution
name: 计量形态增强
domain: business-awareness
scenario: charging
status: draft
---

# 计量形态增强
> 在内容计费三件套基础上，按业务特性选择流量（VOLUME）/时长（DURATION）/事件（EVENT）计量方式；时长支持 CTP/QCT 两种模式，事件计费仅限在线 SCUR。属于[计费](business/business-awareness/charging/NetworkScenario@charging.md)场景。编排 UDG 侧 4 个 feature task。

## 概览
计量形态增强（Metering Enhancement）是对[内容计费基础方案](task/UDG/20.15.2/2-00003.md)的**计量维度特化**：内容计费三件套结构（URR→URRGROUP→PCCPOLICYGRP→RULE→USERPROFILE）不变，差异仅在 `URR.METERINGTYPE`（`OFFMETERINGTYPE`/`ONLMETERINGTYPE`）按业务特性选 VOLUME / DURATION / EVENT。解决"按资源类型差异化计量"问题：视频按流量、语音按时长、短信按事件。

本方案编排 UDG 侧 4 个特性——[内容计费 2-00003](task/UDG/20.15.2/2-00003.md)（基础）+ [时长计费 2-00007](task/UDG/20.15.2/2-00007.md)（DURATION）+ [流量计费 2-00008](task/UDG/20.15.2/2-00008.md)（VOLUME）+ [事件计费 2-00009](task/UDG/20.15.2/2-00009.md)（EVENT）：
- **内容计费（基础）**：提供通用三件套 + 过滤链 + 规则绑定 + 计费收尾，是 3 个计量增强特性的共同基座。
- **时长计费**：URR 统计类型固定 `DURATION`；支持 CTP 连续时长（QCT=0）/ QCT 定时统计（QCT≠0），CTP/QCT 由控制面 UNC/OCS/CHF 决定。
- **流量计费**：URR 统计类型固定 `VOLUME`；按上下行字节数累计（默认计量方式）。
- **事件计费**：URR 统计类型固定 `EVENT`；按业务触发次数累计；**仅支持在线 SCUR**，不支持 Default Quota。

核心机制：3 个计量增强特性**复用同一费率标识链**（URR→URRGROUP→PCCPOLICYGRP→RULE），差异仅在 `URR.METERINGTYPE` 参数与对应 License。计量方式影响在线 GSU 携带的单位（CC-Time / CC-Total-Octets / serviceSpecificUnits）。

## 配置与协同

本方案编排 **4 个 UDG 特性**：[2-00003 内容计费](task/UDG/20.15.2/2-00003.md)（基础）+ [2-00007 时长计费](task/UDG/20.15.2/2-00007.md)（计量维度 DURATION）+ [2-00008 流量计费](task/UDG/20.15.2/2-00008.md)（计量维度 VOLUME）+ [2-00009 事件计费](task/UDG/20.15.2/2-00009.md)（计量维度 EVENT）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档「与其他特性的交互」段 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [内容计费 2-00003](task/UDG/20.15.2/2-00003.md) | 基础（费率三件套结构） | 必配 | 计量增强的基础结构（URR/URRGROUP/PCCPOLICYGRP）；本方案核心是选计量方式，内容计费提供承载骨架 |
| [时长计费 2-00007](task/UDG/20.15.2/2-00007.md) | 计量维度（DURATION） | 三选一/组合 | 计量方式正交维度，按业务选；本身是内容计费的 DURATION 特化（URR.METERINGTYPE=DURATION）；**与流量/事件不叠加于同一 URR**，每业务选其一 |
| [流量计费 2-00008](task/UDG/20.15.2/2-00008.md) | 计量维度（VOLUME） | 三选一/组合 | **≈内容计费 VOLUME 特化，配置脚本与内容计费高度雷同**（feature task 自述）；实质即内容计费的默认计量方式显式特化 |
| [事件计费 2-00009](task/UDG/20.15.2/2-00009.md) | 计量维度（EVENT） | 三选一/组合 | **仅在线 SCUR**；不支持 Default Quota；按业务触发次数累计 |
| UDG SA-Basic [2-00019](task/UDG/20.15.2/2-00019.md)（GWFD-110101） | 基础（依赖前提） | 必配（License 前置） | 业务识别前提，计量依赖业务识别；配置不重叠 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。注：本 CS 核心是**选计量方式**——内容计费是基础，时长/流量/事件是计量维度**三选一或多组合**（每业务选其一），不是 4 个都配。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### 内容计费特性（[2-00003](task/UDG/20.15.2/2-00003.md)）

走标准配置方法（见 feature task），**无特性级变种**。内容计费提供通用 backbone（计费三件套 + 过滤链 + 规则绑定 + 计费收尾），3 个计量增强特性在其上做 `URR.METERINGTYPE` 参数特化。

### 时长计费特性（[2-00007](task/UDG/20.15.2/2-00007.md)）

走标准配置方法（见 feature task），核心变种：

- **URR 统计类型 = DURATION**：`OFFMETERINGTYPE=DURATION`（离线）/ `ONLMETERINGTYPE=DURATION`（在线），按业务持续时间累计。话单/CCR 上报时长字段（离线话单时间信元 / 在线 `CC-Time`）。
- **CTP/QCT 由控制面决定**：UDG 只设 DURATION 统计类型；CTP（QCT=0，连续累计）vs QCT（QCT≠0，定时统计剔除空闲）由 UNC 侧 `ADD DCCTEMPLATE`（在线）/ `ADD OFCSRVTEMPLATE`（离线）或 OCS/CHF 下发决定。OCS/CHF 下发优先于 UNC 本地配置。
- **License**：`LKV3G5TBCS01`（独立于内容计费的 `LKV3G5BCBC01`）。

### 流量计费特性（[2-00008](task/UDG/20.15.2/2-00008.md)）

走标准配置方法（见 feature task），核心变种：

- **URR 统计类型 = VOLUME**：`OFFMETERINGTYPE=VOLUME`（离线）/ `ONLMETERINGTYPE=VOLUME`（在线），按上下行字节数累计。话单/CCR 上报 `datavolumeFBCUplink`/`Downlink`（离线）/ `CC-Input-Octets`/`CC-Output-Octets`（在线）。
- **License**：`LKV3G5VBCS01`。与内容计费配置结构零差异（activation 文档复用），仅 License 与依赖声明不同。
- **默认计量方式**：VOLUME 是内容计费 activation 演示的默认取值，流量计费是其显式特化。

### 事件计费特性（[2-00009](task/UDG/20.15.2/2-00009.md)）

走标准配置方法（见 feature task），核心变种：

- **URR 统计类型 = EVENT**：`OFFMETERINGTYPE=EVENT`（离线）/ `ONLMETERINGTYPE=EVENT`（在线），按业务触发次数累计。话单/CCR 上报 `numberOfEvents`+`eventTimeStamps`（离线）/ `serviceSpecificUnits`（在线/融合）。
- **PCCPOLICYGRP 使能事件计费**：`EVENTCHARGEFLAG=ENABLE` + `EVENTCHGPOINT=REQUEST/RESPONSE/FINISH`（DP 选事件计费点；REQUEST 直接占用，RESPONSE/FINISH 预占用+成功才正式占用）。
- **License**：`LKV3G5EBCS01`。
- **仅限在线 SCUR**（critical 约束）：事件计费仅支持 SCUR（Session Charging with Unit Reservation）；ECUR 仅在线计费额外支持（需 BIT1250）；**不支持 Default Quota**。

### 跨特性协同

- **费率标识链复用**：时长/流量/事件 3 特性复用同一套 URR→URRGROUP→PCCPOLICYGRP→RULE→RULEBINDING 结构，差异仅在 `URR.METERINGTYPE` 参数 + License。每业务按其计量方式选一个特性路径配三件套。
- **URRGROUP 同时绑在线+离线 URR**：3 个计量增强特性的 URRGROUP 均同时配在线+离线 URR（`UPURRNAME1`/`DOWNURRNAME1`=离线，`UPURRNAME2`/`DOWNURRNAME2`=在线），同一 RG 的在线/离线 URR 统计类型必须一致。
- **计量方式影响 GSU 单位**：在线计费时，OCS/CHF 下发的 GSU 携带单位由 METERINGTYPE 决定——VOLUME→CC-Total-Octets，DURATION→CC-Time，EVENT→serviceSpecificUnits。
- **全局缺省 URR 组**（可选）：3 特性均可选 `SET SPECTRAFURRGRP`（[0-00290](task/UDG/20.15.2/0-00290.md)）配全局兜底；但**事件计费场景此全局缺省对事件计量无效**（仅支持时长和流量，见 [0-00290](task/UDG/20.15.2/0-00290.md) 约束）。

> 本方案不新建 atom/compound——3 个计量增强特性全复用内容计费通用 backbone（UDG 1-00009~1-00012），差异仅在 URR 参数与 License。

## 决策点

### DP-1：计量方式选择（方案核心 DP）
按业务特性选 URR.METERINGTYPE，决定走哪个计量增强特性路径。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| VOLUME（流量） | `OFFMETERINGTYPE/ONLMETERINGTYPE=VOLUME`；走 [2-00008](task/UDG/20.15.2/2-00008.md)；License `LKV3G5VBCS01`；在线 GSU 携带 CC-Total-Octets |
| DURATION（时长） | `OFFMETERINGTYPE/ONLMETERINGTYPE=DURATION`；走 [2-00007](task/UDG/20.15.2/2-00007.md)；License `LKV3G5TBCS01`；在线 GSU 携带 CC-Time；CTP/QCT 由控制面决定 |
| EVENT（事件） | `OFFMETERINGTYPE/ONLMETERINGTYPE=EVENT`；走 [2-00009](task/UDG/20.15.2/2-00009.md)；License `LKV3G5EBCS01`；在线 GSU 携带 serviceSpecificUnits；**仅限在线 SCUR**；PCCPOLICYGRP 须 `EVENTCHARGEFLAG=ENABLE` |
| FREE（免费兜底） | `OFFMETERINGTYPE/ONLMETERINGTYPE=FREE`；异常场景兜底；**不支持事件计费使能** |

### DP-2：时长方式 CTP/QCT（DURATION 专属）
仅 DURATION 计量方式适用，由控制面 UNC/OCS/CHF 决定，UDG 不配。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| CTP 连续时长 | QCT=0；UNC `ADD DCCTEMPLATE`/`ADD OFCSRVTEMPLATE` 设 QCT=0；收到首包→业务终止连续累计；精度低 |
| QCT 定时统计 | QCT≠0；UNC 设 QCT≠0；空闲启动 QCT 定时器，空闲≤QCT 计入、>QCT 超时停止；精度高，剔除空闲 |

### DP-3：事件计费点（EVENT 专属）
仅 EVENT 计量方式适用，PCCPOLICYGRP 配置。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| REQUEST | 事件请求即占用配额；`EVENTCHGPOINT=REQUEST` |
| RESPONSE | 事件发生预占用+成功响应正式占用，未识别返还；`EVENTCHGPOINT=RESPONSE` |
| FINISH | 事件完成才占用；`EVENTCHGPOINT=FINISH` |

## 约束

- **SA+内容计费+计量特性 License 三前置**（critical）：UDG 侧 SA-Basic（GWFD-110101）+ 内容计费（GWFD-020301，`LKV3G5BCBC01`）+ 对应计量特性 License（时长 `LKV3G5TBCS01` / 流量 `LKV3G5VBCS01` / 事件 `LKV3G5EBCS01`）必须开启 — 否则配置命令成功但功能不生效。
- **事件计费仅限在线 SCUR**（critical）：事件计费仅支持 SCUR；不支持 Default Quota（与 `SET UPDEFAULTQUOTA` 不兼容）；ECUR 仅在线计费额外支持（需 BIT1250）— 违反则事件计费不生效或配额异常。
- **免费 RG 不支持事件计费**（critical）：`OFFMETERINGTYPE=FREE`/`ONLMETERINGTYPE=FREE` 的 RG 不能使能 `EVENTCHARGEFLAG` — 否则配置冲突。
- **CTP↔QCT 不可切换**（critical，DURATION）：计费会话过程中不支持 CTP 与 QCT 两种时长计费方式切换 — 会话建立后切换则统计异常。
- **URRGROUP 必须同时配在线+离线 URR**（critical）：3 个计量特性均要求；只配一种且与用户计费模式不匹配则无法计费。
- **融合计费特殊**（critical）：SMF `RGAPPLIED=DEFAULT` 时 URRGROUP 不能同时配离线+在线 URR — 否则计费冲突。
- **SMF/UPF 一致性**（critical）：`URRID`/`USAGERPTMODE`/`OFFMETERINGTYPE`/`ONLMETERINGTYPE`/`RULENAME`/`POLICYTYPE`/`POLICYNAME`/`USERPROFILENAME` 在 SMF 与 UPF（及 PCF）必须一致 — 不一致则计费异常/策略不生效（ALM-81026/81054）。
- **REFRESHSRV 时序**（critical，UDG 侧）：`SET REFRESHSRV:REFRESHTYPE=ALL` 必须在所有 ADD/SET 完成后最后执行 — 不执行或时序错则配置不生效。
- **每个 USERPROFILE 必绑缺省费率**（critical）：`SET URRGRPBINDING` 的 `DFTURRGRPNAME`+`DFTSIGURRGNAME` — 否则未匹配费率的报文无法计费。
- **全局缺省 URR 组不支持事件计费**（warning）：`SET SPECTRAFURRGRP`（[0-00290](task/UDG/20.15.2/0-00290.md)）仅支持时长和流量，事件计费场景此全局兜底对事件计量无效。
- **事件计费性能影响**（warning）：七层解析+事件统计对吞吐量有影响；仅支持 HTTP1.x，不支持 HTTP2.0；不支持加密场景基于 host 的计费；不支持 PCC 动态规则事件计费。
- **依赖链**（warning）：SA-Basic → 内容计费 → 计量增强特性（时长/流量/事件），依赖链上每环 License 须先开。

## 关联
- 上游场景：[计费](business/business-awareness/charging/NetworkScenario@charging.md)
- 编排特性（feature task，优先）：[2-00003 UDG 内容计费](task/UDG/20.15.2/2-00003.md) · [2-00007 UDG 时长计费](task/UDG/20.15.2/2-00007.md) · [2-00008 UDG 流量计费](task/UDG/20.15.2/2-00008.md) · [2-00009 UDG 事件计费](task/UDG/20.15.2/2-00009.md)
- 复用步骤/命令（compound/atom，按需）：UDG [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00290](task/UDG/20.15.2/0-00290.md) 全局缺省URR组（事件计费除外）
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（§2.5 CS-CH-05 计量形态增强 + §10 端到端流程）
