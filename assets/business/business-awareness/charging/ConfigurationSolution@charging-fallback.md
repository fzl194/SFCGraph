---
id: ConfigurationSolution@charging-fallback
type: ConfigurationSolution
name: 兜底默认计费
domain: business-awareness
scenario: charging
status: draft
---

# 兜底默认计费
> 通过 DFTURRGRPNAME + DFTSIGURRGNAME 双重兜底，确保未命中任何 RULE 的流量仍按默认费率计费；全局特殊流量经 SET SPECTRAFURRGRP 兜底。属于[计费](business/business-awareness/charging/NetworkScenario@charging.md)场景。编排 UDG 侧 2 个 feature task。

## 概览
兜底默认计费（Fallback Default Charging）解决"未匹配流量漏计费"问题：默认所有流量都有 RG 标识，无遗漏。当业务流未命中任何 RULE 的精确匹配条件时，通过 USERPROFILE 级缺省费率组和整机级全局缺省 URR 组兜底计费，确保计费完整性。

本方案编排 UDG 侧 2 个特性——[内容计费 2-00003](task/UDG/20.15.2/2-00003.md)（核心，三件套基础）+ [PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md)（策略承载骨架，可选）：
- **内容计费**（核心）：提供计费三件套（URR→URRGROUP→PCCPOLICYGRP）+ 计费收尾（[1-00012](task/UDG/20.15.2/1-00012.md) `SET URRGRPBINDING`），是兜底费率组的配置基座。
- **PCC基本功能**（策略承载骨架，可选）：提供 RULE（POLICYTYPE=PCC）+ USERPROFILE + RULEBINDING 策略承载，兜底流量走未命中精确 RULE 后的默认路径。

核心机制——**双重兜底**：
1. **USERPROFILE 级缺省费率**（[1-00012](task/UDG/20.15.2/1-00012.md)）：`SET URRGRPBINDING` 每 USERPROFILE 配 `DFTURRGRPNAME`（缺省业务费率）+ `DFTSIGURRGNAME`（缺省信令费率）。未命中 RULE 的流量自动走默认 URR 组。
2. **整机级全局缺省 URR 组**（[0-00290](task/UDG/20.15.2/0-00290.md)）：`SET SPECTRAFURRGRP` 配整机级全局特殊流量兜底，承接 `GLBDFTURRGSW=ENABLE`/`GLBDFTSIGURRGSW=ENABLE` 全局继承开关。USERPROFILE 未单独配缺省费率时继承本全局缺省。

本方案是对计费收尾（[1-00012](task/UDG/20.15.2/1-00012.md)）的**兜底强化**：标准计费收尾只配 USERPROFILE 级缺省，本方案额外强调全局兜底层的配置与继承。

## 配置与协同

本方案编排 **2 个 UDG 特性**：[2-00003 内容计费](task/UDG/20.15.2/2-00003.md)（核心，三件套基础）+ [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md)（策略骨架，可选）。兜底是内容计费的收尾增强（DFTURRGRPNAME + SPECTRAFURRGRP），依赖费率三件套。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档「与其他特性的交互」段 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UDG 内容计费 2-00003](task/UDG/20.15.2/2-00003.md) | 核心（三件套基础） | 必配 | 兜底是内容计费的收尾增强（DFTURRGRPNAME + SPECTRAFURRGRP），依赖内容计费的费率三件套（URR/URRGROUP/PCCPOLICYGRP）+ 计费收尾（SET URRGRPBINDING） |
| [UDG PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md) | 策略骨架（可选） | 可选 | 提供 RULE（POLICYTYPE=PCC）+ USERPROFILE + RULEBINDING 策略承载骨架；动态 PCC 规则场景配；本地静态规则可不配 |
| UDG SA-Basic [2-00019](task/UDG/20.15.2/2-00019.md)（GWFD-110101） | 基础（依赖前提） | 必配（License 前置） | 业务识别前提；配置不重叠 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。
>
> 本方案（兜底默认计费）与计费模式（在线/离线/融合）**正交**——叠加于任何计费模式 CS 之上，为未命中规则的流量提供默认费率兜底，不改变模式本身的配置。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### 内容计费特性（[2-00003](task/UDG/20.15.2/2-00003.md)）

走标准配置方法（见 feature task），本方案的强化点在计费收尾步骤（[1-00012](task/UDG/20.15.2/1-00012.md)）：

- **USERPROFILE 级双重缺省**（标准配置，本方案强调必配）：`SET URRGRPBINDING` 每 USERPROFILE 必须同时配 `DFTURRGRPNAME`（缺省业务费率，通常指向 any 兜底组）+ `DFTSIGURRGNAME`（缺省信令费率，通常指向 abnormal 异常组）。两者缺一不可——只配业务费率则信令流量漏计费。
- **全局继承开关**（本方案强化）：`SET URRGRPBINDING` 可带 `GLBDFTURRGSW=ENABLE`/`GLBDFTSIGURRGGSW=ENABLE` 开启全局继承——USERPROFILE 未单独配缺省费率时继承整机级全局缺省（见下）。
- **典型兜底费率组规划**：any 组（`OFFMETERINGTYPE=VOLUME`，基础业务兜底）作 `DFTURRGRPNAME`；abnormal 组（`OFFMETERINGTYPE=FREE`，异常免费）作 `DFTSIGURRGNAME`。

### PCC基本功能特性（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task），**无特性级变种**。PCC 提供 RULE（POLICYTYPE=PCC）+ USERPROFILE + RULEBINDING 骨架，兜底流量走"未命中精确 RULE → USERPROFILE 缺省费率组"路径。PCCPOLICYGRP 绑 URRGROUPNAME（来自计费三件套的兜底组）。

### 整机级全局兜底（[0-00290](task/UDG/20.15.2/0-00290.md)）

本方案的核心强化——在 USERPROFILE 级缺省之上，额外配整机级全局兜底：

- **`SET SPECTRAFURRGRP`**：配置整机级全局缺省 URR 组（`URRGROUPNAME`，典型取 abnormal 兜底组），处理两类流量：
  - **特殊流量**：业务报文丢失未能完成七层精确匹配时已转发的流量（如在线用户下线时仅剩的信令报文，需 `BIT1232=1` 才走本组计费）。
  - **未配任何费率的业务流量**：USERPROFILE 未配缺省且全局继承开关 ENABLE 时继承本组。
- **步骤位置**：`SET URRGRPBINDING`（步骤 9）之后、`SET REFRESHSRV` 之前；与全局继承开关配套。
- **立即生效**：修改 URRGROUPNAME 立即生效（高危，会导致整机计费全局缺省费率变化）。

### 跨特性协同

- **兜底层次链**：精确 RULE 匹配（PCC RULE 优先级裁决）→ USERPROFILE 级 `DFTURRGRPNAME`/`DFTSIGURRGNAME`（第一层兜底）→ 整机级 `SET SPECTRAFURRGRP` + 全局继承开关（第二层兜底）。流量逐层降级匹配，确保无漏计费。
- **费率组规划一致**：`DFTURRGRPNAME` 指向的 URRGROUP 必须已通过计费三件套（[1-00010](task/UDG/20.15.2/1-00010.md)）配置；`SET SPECTRAFURRGRP` 的 URRGROUPNAME 必须已通过 `ADD URRGROUP` 配置 — 否则引用空对象。
- **REFRESHSRV 时序**：`SET SPECTRAFURRGRP` 位于 `SET URRGRPBINDING` 之后、`SET REFRESHSRV` 之前；`SET REFRESHSRV:REFRESHTYPE=ALL` 仍为最后一步。

> 本方案不新建 atom/compound——全局兜底复用 [0-00290](task/UDG/20.15.2/0-00290.md)（SET SPECTRAFURRGRP），USERPROFILE 级缺省复用 [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾标准步骤。

## 决策点

### DP-1：兜底策略选择
未命中 RULE 的流量如何计费，决定兜底层次配置。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 仅 USERPROFILE 级缺省 | `SET URRGRPBINDING` 配 `DFTURRGRPNAME`+`DFTSIGURRGNAME`；不走全局继承；每 USERPROFILE 必须单独配 |
| USERPROFILE + 全局继承 | `SET URRGRPBINDING` 带 `GLBDFTURRGSW=ENABLE`/`GLBDFTSIGURRGSW=ENABLE` + `SET SPECTRAFURRGRP` 配整机级全局缺省；USERPROFILE 未配则继承全局 |
| 全局兜底（无 USERPROFILE 级） | 仅 `SET SPECTRAFURRGRP`；所有未配 USERPROFILE 缺省的流量走整机级全局缺省；适合简单场景 |

### DP-2：兜底费率组规划
缺省费率组选什么 URRGROUP，影响兜底计费行为。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| any 组（VOLUME，基础业务兜底） | `DFTURRGRPNAME` 指向 any 组；未命中流量按 VOLUME 计费；最常见的业务兜底 |
| abnormal 组（FREE，异常免费） | `DFTSIGURRGNAME` 指向 abnormal 组；信令/异常流量免费不计费；防欺诈场景需配合 `ADD SPECURRGRPLIST` |
| abnormal 组（VOLUME，异常计费） | `DFTSIGURRGNAME` 指向 abnormal 组但 `OFFMETERINGTYPE=VOLUME`；异常流量也计费；需运营策略决定 |

## 约束

- **每个 USERPROFILE 必绑缺省费率**（critical）：`SET URRGRPBINDING` 的 `DFTURRGRPNAME`+`DFTSIGURRGNAME` 必须同时配置 — 只配一个则另一类流量漏计费。
- **缺省费率须已配置**（critical）：`DFTURRGRPNAME`/`DFTSIGURRGNAME` 须已通过 `ADD URRGROUP` 配置 — 否则绑定引用空对象。
- **全局兜底立即生效且高危**（critical）：`SET SPECTRAFURRGRP` 修改 URRGROUPNAME 立即生效，会导致整机计费全局缺省费率变化或业务不计费，造成运营商计费损失 — 修改前须确认 URRGROUPNAME 已正确配置。
- **全局兜底规格唯一**（warning）：`SET SPECTRAFURRGRP` 最大记录数 1（整机级唯一全局缺省），重复配置即覆盖。
- **全局兜底不支持事件计费**（warning）：`SET SPECTRAFURRGRP` 仅支持时长和流量计费方式，不支持基于事件的计费方式 — 事件计费场景此全局兜底对事件计量无效（见 [0-00290](task/UDG/20.15.2/0-00290.md) 约束）。
- **特殊流量触发需软参**（warning）：特殊流量走全局兜底组计费需 `BIT1232=1`（开启特殊流量使用量上报功能） — 未开则特殊流量不走本组。
- **全局兜底 URRGROUP 前置**（warning）：`SET SPECTRAFURRGRP` 的 URRGROUPNAME 必须已通过 `ADD URRGROUP` 配置；若绑定的 URR 出现欠费，会影响特殊流量使用量上报。
- **REFRESHSRV 时序**（critical，UDG 侧）：`SET REFRESHSRV:REFRESHTYPE=ALL` 必须在所有 ADD/SET（含 `SET SPECTRAFURRGRP`）完成后最后执行 — 不执行或时序错则配置不生效。
- **SA+内容计费+PCC License 三前置**（critical）：UDG 侧 SA-Basic（GWFD-110101）+ 内容计费（GWFD-020301，`LKV3G5BCBC01`）+ PCC（GWFD-020351，`LKV3G5PCCB01`）License 必须开启 — 否则配置命令成功但功能不生效。
- **PCCPOLICYGRP 计费时绑 URRGROUP**（warning）：PCC 特性的 PCCPOLICYGRP.URRGROUPNAME 须指向已配的兜底 URRGROUP — 漏配则计费不生效。

## 关联
- 上游场景：[计费](business/business-awareness/charging/NetworkScenario@charging.md)
- 编排特性（feature task，优先）：[2-00003 UDG 内容计费](task/UDG/20.15.2/2-00003.md) · [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)
- 复用步骤/命令（compound/atom，按需）：UDG [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾 · [0-00290](task/UDG/20.15.2/0-00290.md) 全局缺省URR组 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00003](task/UDG/20.15.2/0-00003.md) ADD PCCPOLICYGRP · [0-00015](task/UDG/20.15.2/0-00015.md) SET REFRESHSRV
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（§2.7 CS-CH-07 兜底默认 + §10 端到端流程）
