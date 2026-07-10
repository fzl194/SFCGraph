---
id: ConfigurationSolution@charging-content
type: ConfigurationSolution
name: 内容计费基础
domain: business-awareness
scenario: charging
status: draft
---

# 内容计费基础
> SA 识别业务类型（L34/L7），每条业务一套独立的 URR→URRGROUP→PCCPOLICYGRP 三件套，按 RG 差异化费率（计费三件套 backbone 不变，按业务粒度实例化）。属于[计费](business/business-awareness/charging/NetworkScenario@charging.md)场景。编排 UDG+UNC 跨网元 feature task。

## 概览
内容计费基础（Content Charging Base）是计费场景的内容计费**基本方法**——三件套 backbone（URR→URRGROUP→PCCPOLICYGRP→RULE→USERPROFILE）结构本身不改变，差异在按业务粒度实例化：每条业务（视频 RG=100/语音 RG=200/兜底 RG=999 等）配独立一套三件套，SA 识别后的业务流匹配到对应 RULE 后按所属 URRGROUP 差异化费率计费。SA-Basic 提供 L3/L4 + L7（URL/协议）识别能力，PCC 提供规则绑定与执行骨架，内容计费基本功能提供三件套结构与收尾。

与离线/在线/融合计费的差异：**计费方式（OFFLINE/ONLINE/CONVERGED）由承载计费特性决定**，本方案聚焦"按业务差异化"这一层——是承载计费方式之上的业务粒度增强。典型场景：视频业务按 VOLUME 流量计费、语音按 DURATION 时长计费、彩信按 EVENT 事件计费、默认 any 业务兜底。

本方案编排 5 个特性跨网元协同——UDG [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md)（基础/依赖前提）+ [内容计费 2-00003](task/UDG/20.15.2/2-00003.md)（核心）+ [PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md)（策略通道，可选）；UNC [PCC基本功能 2-00005](task/UNC/20.15.2/2-00005.md)（跨网元对端/策略通道，可选）+ [内容计费 2-00004](task/UNC/20.15.2/2-00004.md)（跨网元对端）：
- **UDG 用户面（UPF）**：SA 识别业务（L34/L7）→ FILTER/FLOWFILTER 匹配 → RULE（POLICYTYPE=PCC，绑 FLOWFILTER+PCCPOLICYGRP）→ URRGROUP（含 online/offline URR）→ URR（RG 标识）→ 计费链执行。**每业务一套独立三件套**。
- **UNC 控制面（SMF）**：PCRF/PCF 经 Gx/Npcf 下发动态策略或本地预定义规则；费率标识链 URR→URRGROUP→PCCPOLICYGRP→RULE→RULEBINDING→USERPROFILE，与 UDG 侧同构。

核心架构：UDG ↔(N4/PFCP)↔ UNC/SMF ↔(Gx/Npcf)↔ PCRF/PCF。PCC 规则下发：PCF 经 N7 下发策略（含 URR 信息），UDG 按规则执行计费。

## 配置与协同

本方案跨网元编排 **5 个特性**：UDG [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md) + [2-00003 内容计费](task/UDG/20.15.2/2-00003.md) + [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md)；UNC [2-00005 PCC基本功能](task/UNC/20.15.2/2-00005.md) + [2-00004 内容计费](task/UNC/20.15.2/2-00004.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档「与其他特性的交互」段 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UDG 内容计费 2-00003](task/UDG/20.15.2/2-00003.md) | 核心（方案主体） | 必配 | 本方案=按业务粒度计费的基础能力；费率三件套（URR/URRGROUP/PCCPOLICYGRP）由此特性承载 |
| [UDG SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | 业务识别前提——内容计费依赖它识别业务（L34/L7）后才能按业务差异化费率；配置不与内容计费重叠（SA 配识别链，内容计费配三件套），但功能上必配 |
| [UDG PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md) | 策略通道 | 可选 | 动态 PCC（PCRF/PCF 下发规则）时配；本地静态规则可不配。提供 RULE/PCCPOLICYGRP 执行骨架 |
| [UNC 内容计费 2-00004](task/UNC/20.15.2/2-00004.md) | 跨网元对端 | 必配 | UNC 侧费率标识链，与 UDG 侧内容计费组合（UDG 用户面 + UNC 控制面同配费率标识） |
| [UNC PCC基本功能 2-00005](task/UNC/20.15.2/2-00005.md) | 跨网元对端（策略通道） | 可选 | UNC 侧 PCC 策略下发通道（Gx/Npcf），动态 PCC 时配；与 UDG PCC基本功能对端组合 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨网元协同**。

### UDG 用户面：SA-Basic 特性（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task），**无特性级变种**。SA-Basic 提供 L3/L4 + L7 协议/URL 识别能力（`LOD SIGNATUREDB` + `LOD PARSERDB` + `ADD WELLKNOWNPORT` + `ADD L7FILTER` + `ADD PROTBINDFLOWF`），是内容计费业务识别的前置能力。识别后的业务流标签供 RULE 匹配引擎消费。

### UDG 用户面：内容计费特性（[2-00003](task/UDG/20.15.2/2-00003.md)）

走标准配置方法（见 feature task），但有以下**业务粒度实例化**强调（内容计费基础独有）：

- **每业务一套独立三件套**：每条业务（视频/语音/any 等）配独立的 URR→URRGROUP→PCCPOLICYGRP；URRGROUP 同时绑在线+离线 URR（业务粒度贯穿各计费方式）。
- **RG 标识业务费率**：URR 的 `RG`（Rating Group）参数是该业务的费率标识；UNC 侧 `ADD URR.RG` 必须一致（跨网元一致性）。
- **4 场景实例化**：URL 业务（`L34`+`L7` URL 匹配）、IMS 语音（`L34 IPv6`）、any 兜底（`L34 any to any`）、异常（FREE 不计费）；各场景 URR 的 `OFFMETERINGTYPE`/`ONLMETERINGTYPE` 按业务特性选 VOLUME/DURATION/EVENT。
- **可选** `SET SPECTRAFURRGRP`（[0-00290](task/UDG/20.15.2/0-00290.md)）：整机级全局缺省 URR 组；**事件计费场景无效**（见事件计费约束）。

### UDG 用户面：PCC基本功能特性（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task），但有以下**内容计费协同**（与典型 PCC 骨架差异）：

- **PCCPOLICYGRP 必绑 URRGROUP**（计费时）：`ADD PCCPOLICYGRP` 的 `URRGROUPNAME` 指向内容计费的 URRGROUP（来自 [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套）；纯策略不计费时可省 `URRGROUPNAME`。
- **RULE 优先级**（warning）：数字越小越高；只绑三四层的 RULE 优先级低于绑七层的（与 SA-Basic 七层识别协同）；any 规则优先级最低（如 65000/65010）；内容计费典型：URL 七层场景 100，IMS 三四层 110，any 兜底 65000。
- **USERPROFILE 跨侧一致**：`ADD USERPROFILE` 的 `USERPROFILENAME` 与 SMF/PCF 一致；动态规则时 RULENAME 跨侧一致；本地预定义规则组时 USERPROFILENAME 跨侧一致。

### UNC 控制面：内容计费特性（[2-00004](task/UNC/20.15.2/2-00004.md)）

走标准配置方法（见 feature task），**无特性级变种**。UNC 侧内容计费 = License 前置（`LKV3W9BCC12`）+ 复用承载计费方式（在线/离线/融合）的费率标识链。**UNC 侧不配 FILTER/L7FILTER/FLOWFILTER**——业务识别在用户面 UDG，UNC 只做计费规则管理与上报。费率标识链复用 [1-00009](task/UNC/20.15.2/1-00009.md) 与 [1-00002](task/UNC/20.15.2/1-00002.md) UserProfile 绑定结构。

### UNC 控制面：PCC基本功能特性（[2-00005](task/UNC/20.15.2/2-00005.md)）

走标准配置方法（见 feature task），**无特性级变种**。UNC 侧 PCC 提供"从 PCRF/PCF 获取策略"的通道——2G/3G/4G Gx 接口对接 PCRF 或 5G Npcf 接口对接 PCF；PCRF 分组选择（号段/APN/全局缺省）；PCC 开关（全局+APN 级）+ PCC 模板。**本方案不直接依赖本特性的费率标识链**，仅复用其 PCC 策略下发通道与本地规则承载结构。

### 跨网元/跨特性协同

- **顺序**：UDG SA 协议识别链 + 特征库先就绪（`LOD SIGNATUREDB` + `LOD PARSERDB`）→ UDG 三件套按业务配（每业务一套）→ UDG PCCPOLICYGRP 绑 URRGROUP + RULE 绑 FLOWFILTER+PCCPOLICYGRP + USERPROFILE/RULEBINDING → UNC 侧 License + 费率标识链 + UserProfile 绑定 → UDG `SET REFRESHSRV`（`REFRESHTYPE=ALL`）最后生效。
- **业务粒度一致**：UDG 每业务的 URR.RG = UNC 的 URR.RG（跨侧一致）；URRID 全局唯一；CP/UP 的 `URRID`/`USAGERPTMODE`/`METERINGTYPE`/`RULENAME`/`POLICYNAME`/`USERPROFILENAME` 必须一致。
- **过滤链同构**：SA-Basic 提供识别能力 → FILTER/FLOWFILTER 组合匹配 → RULE.PRIORITY 优先级裁决（多规则同时命中时）；七层 RULE 优先级高于三四层。
- **协议链**：UDG ↔(N4/PFCP)↔ UNC/SMF ↔(Gx/Npcf)↔ PCRF/PCF。PCF 经 N7 下发动态规则或本地预定义规则激活。

> 方案优先复用已有 UDG [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 + [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 + [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 + [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾 + [1-00016](task/UDG/20.15.2/1-00016.md) SA 协议识别链；UNC [1-00009](task/UNC/20.15.2/1-00009.md) 费率标识链 + [1-00002](task/UNC/20.15.2/1-00002.md) UserProfile绑定 + [1-00012](task/UNC/20.15.2/1-00012.md) PCRF对接链 + [1-00013](task/UNC/20.15.2/1-00013.md) PCRF选择 + [1-00014](task/UNC/20.15.2/1-00014.md) PCC开关与模板。

## 决策点

### DP-1：计费方式选择（方案级，选 CS）
进入计费场景时的首要决策，决定走哪个 ConfigurationSolution——本方案定位为业务粒度基础，承载计费方式可叠加。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 内容计费基础 | 选本 CS。UDG 三件套按业务粒度实例化（每业务一套）；SA-Basic 识别 + PCC 骨架；UNC 侧 License + 费率标识链 |
| 离线计费 | 选离线 CS。UDG 仅 offline URR + UNC Ga/CG 接口；OFCTemplate 模板 |
| 在线计费 | 选在线 CS。UDG 仅 online URR + UNC Gy/DCC/OCS 接口；DCC 模板 + UPDEFAULTQUOTA |
| 融合计费 | 选融合 CS。UDG 双 URR（offline+online）+ UNC Nchf/CCT/CHF 全链；RGAPPLIED 约束 |
| 内容计费基础 + 计量形态增强 | 选本 CS + 计量形态 CS。叠加 VOLUME/DURATION/EVENT 计量方式选择（见 [ConfigurationSolution@charging-metering](business/business-awareness/charging/ConfigurationSolution@charging-metering.md)） |

### DP-2：匹配层次选择（业务识别深度）
按业务流通过哪层匹配，决定过滤链复杂度和 RULE 优先级。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| L34 匹配（IPv4/IPv6 + 端口） | `ADD FILTER`+`ADD FLOWFILTER`+`ADD FLTBINDFLOWF`；无需 L7 解析；性能高；适用 IMS 语音等 |
| L7-URL 匹配 | 加 `ADD L7FILTER`（URL/Host/Path）+ `ADD PROTBINDFLOWF`（PROTOCOLNAME 引用识别协议）；性能低；适用视频/Web |
| L7-协议匹配 | 仅 `ADD PROTBINDFLOWF`（PROTOCOLNAME=HTTP/HTTPS/RTSP 等）；不解析 URL；适用协议级差异化 |
| L34+L7 混合 | 全匹配；视频业务典型；RULE 优先级：L7 优先 |

### DP-3：PCC 规则下发方式（动态 vs 本地）
UNC 侧 PCC 规则由 PCRF/PCF 下发还是本地预定义，决定 RULE/USERPROFILE 跨网元一致性关键字段。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 动态 PCC（Gx/Npcf 通道） | PCRF/PCF 下发业务流特征+动作；**RULENAME** 须与 SMF/PCF 一致；可随时增删 |
| 本地 PCC（无 PCRF/PCF） | UPF/SMF/PCF 定义相同规则标识；**USERPROFILENAME** 须与 SMF 一致；SMF 下发 USERPROFILENAME 激活本地规则 |
| 预定义规则变体（PCF 下发 RULENAME 激活） | UPF/SMF/PCF 定义相同 RULENAME；PCF 下发规则标识激活本地静态规则 |

### DP-4：计费粒度选择
计费策略作用于哪个粒度，决定 URRGROUP 绑定方式和 Feature 选择。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 会话级（普通计费） | 单 URR 兜底；无业务识别；走 PCC 基本功能骨架 |
| 业务级（内容计费·本方案默认） | 每业务一套三件套 + RG 标识；SA-Basic 识别 + RULE 优先级裁决 |
| QoS flow 级（漫游计费） | 按 QoS flow 拆分 URR；跨网元会话一致性要求高 |

## 约束

- **SA+内容计费+PCC License 三前置**（critical）：UDG 侧 SA-Basic（GWFD-110101，`LKV3G5SABS01`）+ 内容计费基本功能（GWFD-020301，`LKV3G5BCBC01`）+ PCC 基本功能（GWFD-020351，`LKV3G5PCCB01`）+ UNC 侧 PCC（WSFD-109101，`LKV3W9SPCC11`/`LKV2PCCBF01`）+ 内容计费（WSFD-109002，`LKV3W9BCC12`）License 必须全部开启 — 否则配置命令成功但功能不生效。
- **特征库 + 解析库须加载**（critical）：`LOD SIGNATUREDB`（特征字识别）+ `LOD PARSERDB`（深度解析）— 未加载则协议识别失败、ALM-81030 告警。
- **URRID 全网唯一**（critical）：建议从 1000 开始分配 — 重复则 PFCP Session Report 无法关联。
- **CP/UP 一致性**（critical）：`URRID`/`USAGERPTMODE`/`METERINGTYPE`/`RULENAME`/`POLICYTYPE`/`POLICYNAME`/`USERPROFILENAME` 在 SMF/PCF/UPF 间必须一致 — 不一致则计费异常/策略不生效（ALM-81026/81054）。
- **URRGROUP 必须同时配在线+离线 URR**（critical）：除非融合 RGAPPLIED=DEFAULT 场景（二选一），否则 URRGROUP 须同时绑在线+离线 URR — 否则计费失败。
- **RG 跨侧一致**（critical）：UDG `ADD URR.RG` = UNC `ADD URR.RG` — 不一致则报表与实际计费不一致。
- **REFRESHSRV 时序**（critical，UDG 侧）：`SET REFRESHSRV:REFRESHTYPE=ALL` 必须在所有 ADD/SET 完成后最后执行 — 不执行或时序错则 FILTER 配置变更不生效。
- **每个 USERPROFILE 必绑缺省费率**（critical）：`SET URRGRPBINDING` 的 `DFTURRGRPNAME`+`DFTSIGURRGNAME` — 否则未匹配费率的报文无法计费。
- **RULE 优先级约束**（warning）：数字越小越高；七层 RULE 优先级低于三四层 RULE（与 SA-Basic 七层识别协同——七层规则优先）；any 兜底 RULE 优先级最低（如 65000）。
- **FLOWFILTER 必须至少绑一个过滤条件**（critical）：否则 Rule 无效。
- **PROTBINDFLOWF 协议匹配约束**（critical）：`PROTOCOLNAME` 必须与目标网站实际协议一致（https 网站必须配 https）；执行后 60s 才生效 — 否则 L7 匹配失败，流量不会被识别为指定业务。
- **PCCPOLICYGRP 计费时绑 URRGROUP**（warning）：需要计费时 `PCCPOLICYGRP.URRGROUPNAME` 须指向已配的 URRGROUP（来自 [1-00010](task/UDG/20.15.2/1-00010.md)）；漏配则计费不生效。
- **加密协议不可内容计费**（warning）：对 SSL/FTPS 等加密协议报文不能应用内容计费特性 — 特性 wiki 应用限制。
- **URL 长度截断**（warning）：`SAURLLEN=511/1023` 字节，超过将截断，可能导致业务策略匹配不准确。
- **规格限制**（warning）：整机内容计费 rule ≤ 5000，URR ≤ 10000（UNC 侧）。

## 关联
- 上游场景：[计费](business/business-awareness/charging/NetworkScenario@charging.md)
- 编排特性（feature task，优先）：[2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md) · [2-00003 UDG 内容计费](task/UDG/20.15.2/2-00003.md) · [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md) · [2-00005 UNC PCC基本功能](task/UNC/20.15.2/2-00005.md) · [2-00004 UNC 内容计费](task/UNC/20.15.2/2-00004.md)
- 复用步骤/命令（compound/atom，按需）：UDG [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾 · [1-00016](task/UDG/20.15.2/1-00016.md) SA 协议识别链 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) SET REFRESHSRV · [0-00065](task/UDG/20.15.2/0-00065.md) SRVCOMMONPARA · [0-00290](task/UDG/20.15.2/0-00290.md) 全局缺省URR组（事件计费除外）；UNC [1-00009](task/UNC/20.15.2/1-00009.md) 费率标识链 · [1-00002](task/UNC/20.15.2/1-00002.md) UserProfile绑定 · [1-00012](task/UNC/20.15.2/1-00012.md) PCRF对接链 · [1-00013](task/UNC/20.15.2/1-00013.md) PCRF选择 · [1-00014](task/UNC/20.15.2/1-00014.md) PCC开关与模板 · [0-00180](task/UNC/20.15.2/0-00180.md) SET LICENSESWITCH · [0-00052](task/UNC/20.15.2/0-00052.md) ADD PCCPOLICYGRP · [0-00071](task/UNC/20.15.2/0-00071.md) ADD RULE · [0-00094](task/UNC/20.15.2/0-00094.md) ADD USERPROFILE · [0-00073](task/UNC/20.15.2/0-00073.md) ADD RULEBINDING
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（§2.4 CS-CH-04 内容计费基础）