---
id: ConfigurationSolution@bandwidth-anomaly-detection
type: ConfigurationSolution
name: 异常流量检测
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# 异常流量检测

> 基于 APN 级开关检测终端异常下行流量（DDoS 攻击/端口扫描等）并可触发带宽控制/阻断的方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。

> **★ 边界标注**：本方案本质是**异常流量检测（安全/检测类）**，可触发带宽控制/阻断动作，归入带宽控制场景是因"检测→限速/阻断"联动链路。与访问限制场景相邻（访问限制做主动策略阻断，本方案做被动异常检测）。**不依赖 BWM/PCC backbone**——依赖内容计费基本功能的业务流检测能力。activation 极简（License + APN 级检测开关，2 步）。

## 概览

异常流量检测解决"终端异常下行流量（DDoS 攻击/端口扫描等）需检测并可联动控制"的诉求：UDG 在指定 APN 下开启异常下行流量检测开关（`ADD ABNTRAFFICDT`），识别终端异常下行流量；可选开启基于流行为的检测（`TRAFFICBEHAVIORSWITCH`）增强识别能力；可选调整检测报文阈值（`SET ABNTRADTTHR`）。检测到异常后可联动带宽控制/阻断动作。

**核心机制极简**：APN 级 `ADD ABNTRAFFICDT` 开关（`SWITCH`）+ 基于流行为的检测开关（`TRAFFICBEHAVIORSWITCH`）。activation 仅 2 步（License + APN 级检测开关）；方案二可选 `SET ABNTRADTTHR` 调整检测报文阈值。**依赖内容计费基本功能**（原文"基于业务流检测，需开启内容计费基本功能"）——非 BWM/PCC backbone。本方案与 BWM 正交（不配 BWM 对象族），与计费族通过"共享内容计费 SA 识别底座"间接关联。

## 配置与协同

本方案编排 **3 个特性**：UDG 核心 [2-00021 异常流量](task/UDG/20.15.2/2-00021.md) + UDG 基础 [2-00003 内容计费](task/UDG/20.15.2/2-00003.md)（业务流检测依赖）+ UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [020305 异常流量](task/UDG/20.15.2/2-00021.md) | 核心 | 必配 | APN 级异常下行流量检测开关（`ADD ABNTRAFFICDT`）；**本质安全/检测方案，可触发带宽控制/阻断**；不配 BWM/PCC 对象族——仅 APN 级开关 + 可选阈值；activation 极简（2 步） |
| [内容计费 020301](task/UDG/20.15.2/2-00003.md) | 基础（依赖前提） | 必配 | 原文"基于业务流检测，需开启内容计费基本功能"——内容计费的 SA 业务流检测能力为异常流量检测底座；**不依赖 BWM/PCC**；配置不重叠（内容计费配 URR 三件套+过滤链，异常流量仅配 APN 级开关） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | 业务识别前提——内容计费的 SA 识别链底座；配置不重叠（SA 配识别链，异常流量配 APN 级开关） |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：终端异常下行流量检测（[2-00021](task/UDG/20.15.2/2-00021.md)）

走标准配置方法（见 feature task，UDG 侧仅 2 步 + 可选方案二）。**本方案核心变种**：

- **APN 级检测开关**（核心变种）：`ADD ABNTRAFFICDT:APN={apn},SWITCH=ENABLE`——对指定 APN 开启异常下行流量检测。区别于 BWM 的 BWMSERVICE（非 APN 级限速对象）。
- **基于流行为的检测**（可选增强）：`ADD ABNTRAFFICDT:TRAFFICBEHAVIORSWITCH=ENABLE`——增强识别能力（基于流行为模式判断异常）。
- **可选检测报文阈值**（方案二）：`SET ABNTRADTTHR`——调整检测报文阈值（按网络安全需求调整，默认值见特性 wiki）。
- **License**：`LKV3G5ADTD01`（控制项 82200BAJ，按特性 wiki 核实）。

**排除项**：不走 BWM 对象族（无 BWMSERVICE/BWMCONTROLLER/BWMRULE，与 BWM 正交）；不配 PCCPOLICYGRP/RULE/USERPROFILE（不依赖 PCC backbone）；不配 ADCPARA/QOSPROP/SADEDICBEARER（不建专有承载）；不配 URR 计费三件套（虽依赖内容计费底座，但本身不做计费）。

### UDG 基础：内容计费基本功能（[2-00003](task/UDG/20.15.2/2-00003.md)）

走标准配置方法（见 feature task）。异常流量检测依赖内容计费的 SA 业务流检测能力——内容计费的 URR 三件套+过滤链为业务流识别底座。License `LKV3G5BCBC01`（控制项 82209822，按特性 wiki 核实）须开启。**注意**：异常流量检测本身不做计费——仅复用内容计费的识别底座。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。内容计费的业务识别前提——SA-Basic 的特征库+解析库为业务流识别底座。License `LKV3G5SABS01`（控制项 82209749）须开启。

### 跨网元/跨特性协同

- **顺序**：SA-Basic 识别链底座就绪 → 内容计费业务流检测底座就绪（URR 三件套+过滤链）→ `ADD ABNTRAFFICDT`（APN 级检测开关 + 可选 TRAFFICBEHAVIORSWITCH）→（可选）`SET ABNTRADTTHR`（检测阈值）→ `SET REFRESHSRV`。
- **APN 一致性**：`ADD ABNTRAFFICDT` 的 APN 须已配置（依赖 APN 已存在）——特性 wiki 明示"依赖 APN 已配置"。
- **检测→控制联动**（可选，跨 CS 协同）：检测到异常流量后，若需联动带宽控制/阻断，由上层策略（如 PCRF 下发 BWM 限速规则、或访问限制策略）执行——本方案仅做检测，控制动作由下游 CS 承载。
- **无跨网元对端**：本方案是 UDG 单侧特性（无 UNC 对端特性）——检测在 UDG 用户面本地完成。

## 决策点

### DP-1：检测模式（基础 vs 流行为增强）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 基础检测（仅 SWITCH） | `ADD ABNTRAFFICDT:SWITCH=ENABLE`；开启异常下行流量检测开关；识别 DDoS 攻击/端口扫描等基础异常 |
| 流行为增强检测 | `ADD ABNTRAFFICDT:SWITCH=ENABLE,TRAFFICBEHAVIORSWITCH=ENABLE`；基于流行为模式判断异常；识别更精准，消耗更多资源 |

### DP-2：检测报文阈值（方案二，可选）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 默认阈值 | 不执行 `SET ABNTRADTTHR`；按特性 wiki 默认值检测 |
| 自定义阈值 | `SET ABNTRADTTHR` 调整检测报文阈值；按网络安全需求调整（高阈值减少误报，低阈值提高敏感度） |

## 约束

- **License 前置**（critical）：UDG `LKV3G5ADTD01`（020305）+ `LKV3G5BCBC01`（内容计费 020301）+ `LKV3G5SABS01`（SA-Basic）—— 三个 License 须同时开启。
- **依赖内容计费基本功能**（critical，原文明示）：异常流量检测基于业务流检测，需开启内容计费基本功能——内容计费 backbone 未配则检测底座缺失。
- **依赖 SA-Basic**（critical）：内容计费的 SA 识别链底座——未激活则业务流识别失效。
- **依赖 APN 已配置**（critical）：`ADD ABNTRAFFICDT` 的 APN 须已存在——未配置 APN 则检测开关无法绑。
- **不依赖 BWM/PCC**（critical，★ 本方案核心边界）：本方案不配 BWM 对象族、不配 PCCPOLICYGRP/RULE——与 BWM/PCC backbone 正交。若需联动限速/阻断，由下游 CS（BWM/访问限制）承载。
- **检测→控制联动非自动**（warning）：本方案仅做检测——联动带宽控制/阻断需上层策略（PCRF/上层 CS）配合。检测到异常后是否触发控制动作取决于下游配置。
- **无跨网元对端**（info）：UDG 单侧特性——检测在用户面本地完成，无 UNC 对端。
- **与 BWM 正交**（info）：不共享 BWM 对象族，可与 BWM 共存——不会互相干扰。
- **与访问限制场景相邻**（info）：本方案归入带宽控制是因"检测→限速/阻断"联动链路；访问限制场景做主动策略阻断，本方案做被动异常检测——两者边界相邻。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 相邻方案：[BWM 基础限速](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md)（检测后可联动 BWM 限速）· 访问限制场景（检测后可联动主动阻断，跨场景）
- 编排特性（feature task，优先）：[2-00021 UDG 异常流量](task/UDG/20.15.2/2-00021.md)（核心）· [2-00003 UDG 内容计费](task/UDG/20.15.2/2-00003.md)（业务流检测依赖）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）
- 证据：[UDG 020305 异常流量 特性概述](evidence/business/bandwidth-control/UDG_020305_GWFD-020305 终端异常下行流量检测特性概述_02456812.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md)
