---
id: ConfigurationSolution@bandwidth-bwm
type: ConfigurationSolution
name: BWM 基础限速/带宽控制
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# BWM 基础限速/带宽控制

> 基于业务感知的带宽控制主干方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。编排 UDG+UNC 跨网元 feature/compound task，覆盖 9 个子场景（3 作用范围 × 3 业务识别方式 × 时段/协议/切片维度）。本 CS 是带宽控制场景的**范本**——其他带宽方案（Shaping/FUP/QoS 触发等）在此基础上派生。

## 概览

BWM 基础限速解决"按业务/用户/用户组/切片/时段差异化限速"的核心诉求：P2P/VoIP/视频等占用大量带宽资源的业务可能导致网络拥塞，需按业务感知或 TOS 识别后对用户级/用户组级/整机级做层次化速率控制（CAR 承诺/超速限速、Shaping 平滑整形）。UDG 侧 UPF 执行实际限速；UNC 侧 SMF/PGW-C 承载本地规则 + 经 N4 接口透传带宽控制策略。

本方案编排 **5 个核心特性**跨网元协同——UDG 侧 [BWM 2-00001](task/UDG/20.15.2/2-00001.md) + [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md) + [PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md) + UNC 侧 [BWM 2-00010](task/UNC/20.15.2/2-00010.md)（即 WSFD-211005） + [PCC基本功能 2-00005](task/UNC/20.15.2/2-00005.md)（即 WSFD-109101）：

- **UDG 用户面（UPF/PGW-U）**：[BWM 2-00001](task/UDG/20.15.2/2-00001.md) 核心（方案主体）——`SET LICENSESWITCH` + `ADD BWMSERVICE`（业务识别 TOS/NONTOS）+ `ADD BWMCONTROLLER`（CAR/Shaping + CIR/CBS/PIR/PBS + 三色）+ `ADD BWMUSERGROUP`（用户集合）+ `ADD BWMRULE`（绑定 Service+Controller，分用户级/用户组级/缺省）→ 绑接入域（APN 或切片）。
- **UDG 业务识别**：复用 [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md)（基础/依赖前提）的特征库+解析库+L7 识别（HTTP/P2P/VoIP 七层识别能力）；[PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md)（策略通道，可选）的 PCCPOLICYGRP+RULE+USERPROFILE 承载 BWM 策略组（POLICYTYPE=BWM）。
- **UNC 控制面（SMF/PGW-C）**：[BWM 2-00010](task/UNC/20.15.2/2-00010.md) 控制面承载——License 前置 + PCC 基本功能 Gx/Npcf 通道 + `RULE(POLICYTYPE=BWM)` + UserProfile + RuleBinding + UsrProfGroup + 挂接 APN；[PCC基本功能 2-00005](task/UNC/20.15.2/2-00005.md) 提供 PCRF/PCF 对接链 + PCRF 选择 + PCC 开关模板。

核心架构：**PCRF/PCF ↔(N7/Gx)↔ UNC(SMF/PGW-C，本地规则或 PCRF 透传) ↔(N4/PFCP)↔ UDG(UPF/PGW-U，执行 BWM 限速)**。BWM 执行在 UDG，规则下发在 UNC，识别在 SA-Basic，策略在 PCC。

## 配置与协同

本方案跨网元编排 **5 个核心特性**：UDG 核心 [2-00001 BWM](task/UDG/20.15.2/2-00001.md) + UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）+ UDG 策略通道 [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md)（可选）+ UNC 跨网元对端 [2-00010 BWM](task/UNC/20.15.2/2-00010.md) + UNC 策略通道 [2-00005 PCC基本功能](task/UNC/20.15.2/2-00005.md)（可选）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档「与其他特性的交互」段 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UDG BWM 2-00001](task/UDG/20.15.2/2-00001.md) | 核心（方案主体） | 必配 | 本方案=带宽控制执行（CAR/Shaping/分级限速），BWM 对象族（BWMSERVICE→BWMCONTROLLER→BWMUSERGROUP→BWMRULE）由 UDG 承载 |
| [UDG SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | 业务识别前提——BWM 依赖 SA-Basic 的 L7 协议识别（HTTP/P2P/VoIP）；Protocol（`SRVTYPE=PROTOCOLNAME`）场景须先激活其特征库，否则 PROTOCOLNAME 引用无效；配置不重叠，License 必开 |
| [UDG PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md) | 策略通道 | 可选 | 提供 PCCPOLICYGRP+RULE+USERPROFILE 策略承载（`POLICYTYPE=BWM`）；**动态 PCC**（PCRF/PCF 下发 BWM 规则）时配；本地静态 BWM 规则可不配（`HOMEPCCSWITCH=DISABLE`） |
| [UNC BWM 2-00010](task/UNC/20.15.2/2-00010.md) | 跨网元对端 | 必配 | UNC 侧 BWM 规则承载（`RULE POLICYTYPE=BWM` + UserProfile + RuleBinding），与 UDG 对端组合；**UNC 仅承载不执行**——实际限速对象全在 UDG，UNC 配 CIR/PIR 无效 |
| [UNC PCC基本功能 2-00005](task/UNC/20.15.2/2-00005.md) | 跨网元对端（策略通道） | 可选 | UNC 侧 PCC 策略下发通道（Gx/Npcf）；动态 PCC 时配，与 UDG PCC 通道成对组合 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨网元协同**。

### UDG 核心：BWM 特性（[2-00001](task/UDG/20.15.2/2-00001.md)）

走标准配置方法（见 feature task，9 场景 DP 表已完整列出），**以下为本方案独占的特性级变种与约束**（BWM 范本独有）：

#### 变种点：9 场景 × 三维 DP（控制层级 × 业务识别方式 × 触发维度）

9 个子场景**共享同一套骨架**（前置 → 业务控制器 → 用户组规则绑定），差异完全由 9 场景 DP 表驱动，详见 [2-00001](task/UDG/20.15.2/2-00001.md) 决策点章节。本 CS 仅列维度（不重复 DP 表）：

- **3 作用范围**：用户级（`BWMRULETYPE=SUBSCRIBER_SPECIFIC`，`USERLEVSRVTYPE`）/ 用户组级（`GROUP_SPECIFIC`/`GROUP_DEFAULT`，`USERGLEVSRVTYPE`）/ 整机级（`GLOBAL`）。
- **3 业务识别方式**：TOS（DSCP/IP 优先级）/ NONTOS（不区分业务）/ Protocol（L7 协议名，如 HTTP）。
- **3 触发维度**：时段（`TIMERANGE`+`PERITIMERANGE`，绑控制器 1/2/3）/ 切片（`SNSSAI`+`SNSSAIUPINTF`+`SNSSAIBWMUSRG`，`BWMSUBSCRCTRL=PCC_RULE_IGNORE`）/ APN 用户组（`SET BANDWIDTHMNG` 必配）。

用户按业务选子集（典型组合：APN 用户组级 CAR / PCC 预定义规则 / 切片 GROUP / 时间段 / 用户 TOS / 用户组 TOS / 三级 / 分级带宽 / HTTP 用户限速）。

#### 约束：SHAPING 仅用户级（★ BWM 范本核心 critical）

**SHAPING 仅 `BWMRULETYPE=SUBSCRIBER_SPECIFIC`（用户级）支持；用户组级（`GROUP_SPECIFIC`/`GROUP_DEFAULT`）/ 整机级（`GLOBAL`）只能 CAR，不能 SHAPING**。这是 BWM 范本最易配错的核心约束——组级/整机级配 SHAPING 将被静默忽略或导致 BWM 不生效。

#### 工程经验：CAR 参数推荐公式（★）

`ADD BWMCONTROLLER` 配置 CAR 时推荐参数关系（防 burst 抖动+三色标记准确）：

- `CIR = 0.5 × PIR`（承诺速率取峰值一半，避免常态拥塞）
- `CBS ≥ CIR × 1.5 × 1000 / 8`（承诺突发容量，字节）
- `PBS ≥ PIR × 1.5 × 1000 / 8`（峰值突发容量，字节）

### UDG SA 识别：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。BWM 范本复用其 L7 协议识别能力（HTTP/P2P/VoIP 业务流分类）——HTTP 用户限速场景须配 SA-Basic 特征库 `LOD SIGNATUREDB`+`LOD PARSERDB`+`ADD WELLKNOWNPORT`，否则 PROTOCOLNAME 引用无效。

### UDG PCC 通道：PCC基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task）。BWM 范本复用其 PCCPOLICYGRP+RULE+USERPROFILE 骨架——`POLICYTYPE=BWM` 标识 BWM 策略组（区别于 `POLICYTYPE=PCC` 计费组）；`PCCPOLICYGRP` 不绑 `URRGROUPNAME`（BWM 不计费）；`RULENAME` 三网元（PCRF/PCF/SMF/UPF）一致。

### UNC BWM 承载：BWM 特性（[2-00010](task/UNC/20.15.2/2-00010.md)，即 WSFD-211005）

走标准配置方法（见 feature task）。BWM 范本复用其**控制面中转**——UNC **不执行实际限速**（仅做 License 开关 + PCC Gx/Npcf 通道 + `RULE(POLICYTYPE=BWM)` 本地承载 + N4 接口透传）；实际限速对象（`BWMSERVICE`/`BWMCONTROLLER`/`BWMUSERGROUP`/`BWMRULE`）全在 UDG 侧（[2-00001](task/UDG/20.15.2/2-00001.md)）配置。两侧 `RULENAME` 须一致。

### UNC PCC 通道：PCC基本功能（[2-00005](task/UNC/20.15.2/2-00005.md)，即 WSFD-109101）

走标准配置方法（见 feature task）。BWM 范本复用其 Gx/Npcf 通道——动态 PCC 经 PCRF/PCF 获取预定义 BWM 规则名，本地 PCC 配静态 BWM 规则（`SET PCCFUNC HOMEPCCSWITCH=DISABLE`）。代际选择按 NS 业务需求：2G/3G/4G 走 Gx+Diameter，5G 走 Npcf+NRF。

### 可选：ADC 应用检测触发（UNC [2-00006 ADC基本功能](task/UNC/20.15.2/2-00006.md)，即 WSFD-109102）

走标准配置方法（HTTP 应用触发 BWM 时启用，可选）。当 BWM 范本需要"PCRF/PCF 经 ADC 上报应用类型后再触发带宽策略"时启用本特性——典型场景：检测到 P2P 应用后由 PCRF 动态下发 BWM 限速规则。配置生成按需叠加，不强制。

### 跨网元/跨特性协同

- **顺序**：UDG SA-Basic 协议识别链（[2-00019](task/UDG/20.15.2/2-00019.md)）就绪 → UDG PCCPOLICYGRP(POLICYTYPE=BWM)+RULE+USERPROFILE 骨架就绪 → UDG BWM 业务识别/控制器/用户组/规则/绑 APN 就绪（[2-00001](task/UDG/20.15.2/2-00001.md)）→ UNC PCC License + Gx/Npcf 通道就绪（[2-00005](task/UNC/20.15.2/2-00005.md)）→ UNC BWM License + 本地 RULE(POLICYTYPE=BWM) 承载链就绪（[2-00010](task/UNC/20.15.2/2-00010.md)）→ UDG `SET REFRESHSRV`（`PROTBINDFLOWF` 后 60s，最后生效）。
- **一致性**：跨网元 `RULENAME`（PCRF/PCF/SMF/UPF 四方一致）；`PCCPOLICYGRPNM`（UNC 与 UDG 一致）；`USERPROFILENAME`（预定义规则组标识）；`BWMUSERGROUPNAME`（UDG 内一致）。两侧 `POLICYTYPE=BWM` 严格统一（区别 `POLICYTYPE=PCC` 计费组）。
- **协议链**：UDG ↔(N4/PFCP)↔ UNC(SMF) ↔(N7/Npcf 5G / Gx/Diameter 2G/3G/4G)↔ PCRF/PCF；N4 透传 BWM 策略（`BWMSERVICE`/`BWMCONTROLLER`/`BWMUSERGROUP`/`BWMRULE` 实际限速对象由 UPF 本地执行）。
- **触发维度协同**：切片场景 → UNC 侧切片选择 + UDG 侧 `SNSSAIUPINTF`+`SNSSAIBWMUSRG` 同步；时段场景 → UDG 单侧（UNC 无时段维度）；PCC 预定义规则 → 双方 PCCPOLICYGRP+RULE+USERPROFILE 三件套同步。

> 方案优先复用已有 UDG 1-00001~1-00006 与 UNC 1-00012~1-00018 等 backbone compound，不新建 atom/compound（9 场景差异已由 1-00001~1-00006 + 0-00108/0-00289 承载）。

## 决策点

### DP-1：场景级方案路由（方案级，选 NS→CS）

进入带宽控制场景时的首要决策，决定走哪个 ConfigurationSolution。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 按业务/用户/用户组/切片/时段差异化限速（CAR/Shaping/分级） | 选本 CS（BWM 范本）。UDG 8 场景 + UNC 211005 规则传递 + 9 场景 DP 驱动 |
| 仅按业务 Shaping（流量整形） | 选 CS Shaping 业务整形。SHAPING 限用户级（`SUBSCRIBER_SPECIFIC`），组/整机只能 CAR（见本 CS 约束） |
| 用户/业务级累计流量超量降速/重置（FUP） | 选 CS FUP 累计流量策略控制。UDG 110312 + 020353 + UNC 211009/109104，累计配额到阈值触发降速 |
| 业务触发 QoS 保证（GBR） | 选 CS QoS 触发保证。UDG 020358 + UNC 109107，VoNR/视频业务保带宽 |
| 应用检测触发（HTTP/P2P 应用） | 选 CS ADC 应用检测触发。UDG 020357 + UNC 109102，ADC 上报 PCRF/PCF 触发带宽 |

### DP-2：控制层级（用户级/用户组级/整机级，★ SHAPING 限制）

UDG `ADD BWMRULE` 的 `BWMRULETYPE` 参数决定控制层级，影响 SHAPING 支持范围。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 用户级（`SUBSCRIBER_SPECIFIC`） | 支持 SHAPING + CAR；`USERLEVSRVTYPE` 决定识别方式（TOS/NONTOS）；走用户模板 USERPROFILE 绑 RULE |
| 用户组级（`GROUP_SPECIFIC`/`GROUP_DEFAULT`） | 仅支持 CAR；`USERGLEVSRVTYPE` 决定识别方式；必配 `SET BANDWIDTHMNG`；走 BWMUSERGROUP+APNBINDBWMUSRG |
| 整机级（`GLOBAL`） | 仅支持 CAR；走 `ADD BWMRULEGLOBAL`（[0-00289](task/UDG/20.15.2/0-00289.md)）；整机 BWMSERVICE 必须 TOS 且 TOS 值全局唯一 |
| 三级控制（用户+组+整机） | 骨架 + [0-00289](task/UDG/20.15.2/0-00289.md)；[1-00002](task/UDG/20.15.2/1-00002.md) 配三级控制器（用户<组<整机）；[1-00003](task/UDG/20.15.2/1-00003.md) 用户级+组级 BWMRULE + 追加 BWMRULEGLOBAL |

### DP-3：业务识别方式（TOS/NONTOS/Protocol）

UDG `ADD BWMSERVICE` 的 `SRVTYPE` 参数决定识别方式。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| TOS（DSCP/IP 优先级） | `SRVTYPE=TOS`；配 TOS 值（`USERLEVSRVTYPE=TOS` 用户级 / `USERGLEVSRVTYPE=TOS` 组级）；典型场景：语音高优先级保带宽 |
| NONTOS（不区分业务） | `SRVTYPE=NONTOS`；不配 BWMSERVICE；APN 用户组级典型走法；`USERLEVSRVTYPE=NONTOS` |
| Protocol（L7 协议名） | `SRVTYPE=PROTOCOLNAME`；配 PROTOCOLNAME=http 等；依赖 SA-Basic 特征库（[2-00019](task/UDG/20.15.2/2-00019.md)）；HTTP 用户限速场景 |
| 分级带宽（多档 TOS） | 骨架 + [0-00108](task/UDG/20.15.2/0-00108.md) `ADD BCSRVLEVELPLY`；控制器加 `SRVLEVELSPEC` + 规则加 `SERVICELEVEL` + 用户组 `USERGLEVRULESW`；`CIRRATE` 和 ≤ 100% |

### DP-4：接入域（APN/DNN 或 切片）

BWM 绑定的接入域，影响 `ADD APNBINDBWMUSRG` 或 `ADD SNSSAIBWMUSRG` 走法。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| APN/DNN 用户组级 | `ADD APNBINDBWMUSRG` 绑 APN；典型主场景；用户组级必配 `SET BANDWIDTHMNG` |
| 切片 | 骨架 + [1-00005](task/UDG/20.15.2/1-00005.md) `ADD SNSSAI`+`ADD SNSSAIUPINTF`+`ADD SNSSAIBWMUSRG`；`BWMSUBSCRCTRL=PCC_RULE_IGNORE`；切片隔离 |
| 时间段 | 骨架 + [1-00006](task/UDG/20.15.2/1-00006.md) `ADD TIMERANGE`+`ADD PERITIMERANGE`；`TIMERANGENAME1/2/3` ↔ 控制器 1/2/3；夜间免打扰典型场景 |

### DP-5：PCC 模式（动态 vs 本地，决定规则来源）

UNC 侧 PCC 模式，影响 BWM 规则来源。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 动态 PCC（有 PCRF/PCF） | UNC 侧 [2-00005](task/UNC/20.15.2/2-00005.md) DP2=动态；PCRF/PCF 下发 BWM 预定义规则名，本地 `RULE(POLICYTYPE=BWM)` 匹配 |
| 本地 PCC（无 PCRF/PCF） | UNC 侧 `SET PCCFUNC HOMEPCCSWITCH=DISABLE`；UNC 配静态 BWM 规则（PRIORITY 全局优先级匹配） |
| 5G 动态 PCC（Npcf） | UNC 侧 [2-00005](task/UNC/20.15.2/2-00005.md) DP1=5G；PCF 经 NRF 服务化发现；无需 Diameter 对接 |
| 2G/3G/4G 动态 PCC（Gx） | UNC 侧 [2-00005](task/UNC/20.15.2/2-00005.md) DP1=2G/3G/4G；需 Diameter 对接链（[1-00012](task/UNC/20.15.2/1-00012.md)）+ PCRF 选择（[1-00013](task/UNC/20.15.2/1-00013.md)） |

## 约束

- **License 三前置**（critical）：UDG 侧 `SET LICENSESWITCH` 开启 `LKV3G5TCSA01`（BWM，[2-00001](task/UDG/20.15.2/2-00001.md)）+ `LKV3G5SABS01`（SA-Basic，[2-00019](task/UDG/20.15.2/2-00019.md)）+ `LKV3G5PCCB01`（PCC基本功能，[2-00018](task/UDG/20.15.2/2-00018.md)）；UNC 侧开启 `LKV3TCBSA01`（WSFD-211005，[2-00010](task/UNC/20.15.2/2-00010.md)）+ `LKV2PCCBF01`+`LKV3W9SPCC11`（WSFD-109101 PCC基本功能，[2-00005](task/UNC/20.15.2/2-00005.md)） — 全部开启后 BWM 才生效，未开部分静默不生效难排查。
- **SHAPING 仅用户级**（critical，★ BWM 范本核心）：`BWMRULETYPE=SUBSCRIBER_SPECIFIC`（用户级）支持 SHAPING；`GROUP_SPECIFIC`/`GROUP_DEFAULT`（用户组级）/ `GLOBAL`（整机级）只能 CAR，配 SHAPING 无效或被忽略。
- **跨网元 RULENAME/USERPROFILENAME/BWMUSERGROUPNAME 一致**（critical）：四网元（PCRF/PCF/SMF/UPF）的 RULENAME 一致；预定义规则组的 USERPROFILENAME 一致；UDG 内 BWMRULE.BWMSERVICENAME/BWMCONTROLLERNAME/BWMUSERGROUPNAME 一致 — 不一致则跨网元会话匹配失败、BWM 限速不生效（告警 ALM-81054）。
- **PCCPOLICYGRP 不绑 URRGROUP**（critical，BWM 范本与计费族的区别）：BWM 场景 `ADD PCCPOLICYGRP` 不配 `URRGROUPNAME`（BWM 不计费）；若误绑计费三件套 URRGROUP，将导致 URR 统计归零或规则冲突。
- **POLICYTYPE=BWM 三网元统一**（critical）：UNC `ADD RULE` 与 UDG `ADD PCCPOLICYGRP` 的策略类型必须 `POLICYTYPE=BWM`（区别 `POLICYTYPE=PCC` 计费组）；混用导致策略路由错位。
- **REFRESHSRV 时序**（critical，UDG 侧）：`SET REFRESHSRV:REFRESHTYPE=ALL` 必须在所有 ADD/SET 完成后最后执行；`PROTBINDFLOWF` 配置后需等待 60 秒再执行 REFRESHSRV（PCC/Protocol 场景必刷）— 不执行或时序错则 FILTER/RULE 配置变更不生效。
- **CAR 参数推荐公式**（warning，★ 工程经验）：`CIR = 0.5 × PIR`；`CBS ≥ CIR × 1.5 × 1000 / 8`（字节）；`PBS ≥ PIR × 1.5 × 1000 / 8`（字节）— 偏离推荐值易引发 burst 抖动或三色标记不准确。
- **Protocol 识别依赖 SA-Basic**（critical）：HTTP 用户限速等 Protocol 场景须先激活 SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）的 `LOD SIGNATUREDB`+`LOD PARSERDB`+`ADD WELLKNOWNPORT` — 否则 `PROTOCOLNAME` 引用无效，PROTBINDFLOWF 失败。
- **切片场景 BWMSUBSCRCTRL 必设**（critical）：`BWMSUBSCRCTRL=PCC_RULE_IGNORE` 必须配置（[2-00001](task/UDG/20.15.2/2-00001.md) 切片 DP）— 否则切片内 PCC 规则干扰 BWM 规则匹配。
- **三级控制整机 BWMSERVICE 必须 TOS**（warning）：整机级（`GLOBAL`）场景 BWMSERVICE 必须 `SRVTYPE=TOS` 且 TOS 值全局唯一 — 否则多级匹配冲突。
- **UNC 仅承载不执行**（critical，跨网元澄清）：UNC（SMF/PGW-C）仅做 License 开关 + PCC Gx/Npcf 通道 + `RULE(POLICYTYPE=BWM)` 本地承载 + N4 接口透传，**不执行实际限速**；实际限速对象（`BWMSERVICE`/`BWMCONTROLLER`/`BWMUSERGROUP`/`BWMRULE`）全在 UDG 侧 — 在 UNC 配 BWMCONTROLLER/CIR/PIR 等参数无效。
- **无 License 时配 BWM**（critical）：未开 BWM License 时配 BWM 参数，命令成功但功能不生效 — 配置生成须先检查 License 开关。
- **URL 长度截断影响识别**（warning）：SAURLLEN 超过 511/1023 字节截断，HTTP 用户限速场景策略匹配可能不准确（SA-Basic 约束联动）。
- **加密协议不可 BWM**（info）：SSL/FTPS 等加密协议报文不能按业务应用 BWM 策略（特性 wiki 应用限制）。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 编排特性（feature task，优先）：[2-00001 UDG BWM](task/UDG/20.15.2/2-00001.md)（主 backbone）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别 backbone）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（PCC 通道 backbone）· [2-00010 UNC BWM WSFD-211005](task/UNC/20.15.2/2-00010.md)（控制面承载）· [2-00005 UNC PCC基本功能 WSFD-109101](task/UNC/20.15.2/2-00005.md)（UNC PCC 通道 backbone）
- 可选特性：[2-00006 UNC ADC基本功能 WSFD-109102](task/UNC/20.15.2/2-00006.md)（HTTP 应用触发 BWM 时启用）
- 复用步骤/命令（compound/atom，按需）：UDG [1-00001](task/UDG/20.15.2/1-00001.md) 前置 · [1-00002](task/UDG/20.15.2/1-00002.md) 业务与控制器 · [1-00003](task/UDG/20.15.2/1-00003.md) 用户组规则绑定 · [1-00004](task/UDG/20.15.2/1-00004.md) PCC 链 · [1-00005](task/UDG/20.15.2/1-00005.md) 切片 · [1-00006](task/UDG/20.15.2/1-00006.md) 时间段 · [1-00016](task/UDG/20.15.2/1-00016.md) SA 协议识别链 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [0-00108](task/UDG/20.15.2/0-00108.md) 分级 BCSRVLEVELPLY · [0-00289](task/UDG/20.15.2/0-00289.md) 三级 BWMRULEGLOBAL · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV；UNC [1-00018](task/UNC/20.15.2/1-00018.md) BWM 本地规则承载链 · [1-00012](task/UNC/20.15.2/1-00012.md) PCRF 对接链 · [1-00013](task/UNC/20.15.2/1-00013.md) PCRF 选择 · [1-00014](task/UNC/20.15.2/1-00014.md) PCC 开关与模板
- 证据：[UDG BWM 特性概述](evidence/business/bandwidth-control/GWFD-110311 基于业务感知的带宽控制特性概述_77219469.md) · [实现原理](evidence/business/bandwidth-control/实现原理_77219470.md) · [9 激活子场景](evidence/business/bandwidth-control/)（BWM 主干） · [UNC BWM 概述](evidence/business/bandwidth-control/特性概述_79619204.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) · [UDG PCC基本功能](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md) · [UNC PCC基本功能 5G](evidence/business/bandwidth-control/UNC_PCC基本功能5G特性概述.md)