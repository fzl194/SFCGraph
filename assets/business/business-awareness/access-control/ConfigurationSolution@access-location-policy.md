---
id: ConfigurationSolution@access-location-policy
type: ConfigurationSolution
name: 位置策略
domain: business-awareness
scenario: access-control
status: draft
---

# 位置策略

> UNC（PCF）按用户初始接入位置（ULI：CGI/ECGI/NCGI）决策下发 PCC 策略，UDG（UPF）执行位置策略。★跨网元方案（控制面决策 + 用户面执行）。属于[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)场景。

## 概览

位置策略是访问限制场景的**跨网元方案**：UNC 侧 PCF 根据用户初始接入位置（User Location Information，ULI）做策略决策，UDG 侧 UPF 执行 PCF 下发的位置策略。本方案聚焦"位置感知的策略控制"端到端——从位置信息采集到策略决策再到用户面执行。

核心对象链（UNC 侧）：**用户位置**（`ADD USRLOCATION`，代际 CGI/ECGI/NCGI 分叉）→ **位置组**（`ADD USRLOCATIONGRP`）→ 绑 **用户模板组**（`MOD UPBINDUPG`）→ 绑 **APN**（`ADD APNUSRPROFG`）。策略动作（如带宽控制/访问限制）在规则中配置，引用 [BWM](task/UNC/20.15.2/2-00010.md) / [PCC](task/UNC/20.15.2/2-00005.md)。UDG 侧执行 PCF 下发的 PCC 策略（经 N7/N4 接口）。

> **★边界标注——与带宽控制场景的交集**：UNC WSFD-211001 依赖带宽控制（[WSFD-211005 BWM](task/UNC/20.15.2/2-00010.md)，activation 约束段声明）。位置策略可触发带宽控制/访问限制动作——本 CS 聚焦"位置感知的策略控制"端到端，带宽控制的具体限速配置见带宽控制场景。即：位置是**决策维度**（WHERE），带宽/访问限制是**动作维度**（WHAT），两者正交。

本方案编排 1 个核心跨网元特性 + 2 个 UDG 依赖前提——UNC 侧[位置策略 WSFD-211001](task/UNC/20.15.2/2-00013.md)（控制面位置决策）+ UDG 侧[PCC基本功能](task/UDG/20.15.2/2-00018.md)（用户面执行）+ [SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别，若策略含业务维度）。

## 配置与协同

本方案跨网元编排 **3 个特性**：UNC 核心 [位置策略 211001](task/UNC/20.15.2/2-00013.md) + UDG 跨网元对端 [PCC基本功能](task/UDG/20.15.2/2-00018.md) + UDG 依赖前提 [SA-Basic](task/UDG/20.15.2/2-00019.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯 feature task 依赖声明 + activation 约束）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UNC 位置策略 211001](task/UNC/20.15.2/2-00013.md)（WSFD-211001） | 核心（控制面决策） | 必配 | UNC/PCF 按用户初始接入位置(ULI)决策下发 PCC 策略；跨网元对端。三种部署场景（DP）：有 PCRF 动态（UNC 仅 License）/ 有 PCRF 预定义 或 无 PCRF 本地（UNC 配位置链）。**依赖带宽控制**（activation 声明，动作维度） |
| [UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（GWFD-020351） | 跨网元对端（用户面执行） | 必配 | UDG 执行 PCF 下发的位置策略（PCC 子轨，POLICYTYPE=PCC）。配置**不与 UNC 位置链重叠**——UNC 配位置链（USRLOCATION/USRLOCATIONGRP/UPBINDUPG），UDG 配 RULE/USERPROFILE/PCCPOLICYGRP 执行策略 |
| [UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（GWFD-110101） | 基础（依赖前提） | 必配（若策略含业务维度） | 业务识别前提——若位置策略的动作含业务维度（如限速特定业务流），需 SA-Basic 协议识别。配置**不与核心重叠** |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。
>
> **★与带宽控制场景的交集边界**（防混淆）：UNC WSFD-211001 依赖带宽控制（WSFD-211005）——activation 约束段明示"策略动作若为带宽控制，须先完成 BWM"。位置策略的**动作可以是带宽控制或访问限制**——位置是决策维度（WHERE，基于 ULI 触发），带宽/访问限制是动作维度（WHAT，PCC/BWM RULE 执行）。本 CS 聚焦位置决策链（UNC 侧），动作配置见对应场景 CS（[带宽控制 BWM CS](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md)）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UNC 控制面：位置策略（[2-00013](task/UNC/20.15.2/2-00013.md)）

走标准配置方法（见 feature task），**无特性级变种**（本 CS 即该特性的标准应用场景）。activation 演示 5 命令完整脚本：SET LICENSESWITCH + ADD USRLOCATION（CGI/ECGI/NCGI 三代际同脚本演示）+ ADD USRLOCATIONGRP + MOD UPBINDUPG + ADD APNUSRPROFG。

### UDG 用户面：PCC基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task），**无特性级变种**。UDG 执行 PCF 经 N7/N4 下发的位置策略（动态规则方式：PCRF/PCF 下发业务流特征+动作，RULENAME 跨网元一致）。

### 跨网元协同：UNC 决策 → UDG 执行

- **端到端链路**：UNC/PCF 采集用户位置（ULI）→ 按位置组（USRLOCATIONGRP）决策 → PCF 下发 PCC 策略（经 N7 接口给 SMF）→ SMF 经 N4/PFCP 下发 RULE/USERPROFILE 给 UDG/UPF → UDG 执行策略（POLICYTYPE=PCC）。
- **跨网元一致性关键**：动态规则方式下，PCF 下发的 RULENAME 须与 UDG/SMF 上规则名称相同（[2-00018](task/UDG/20.15.2/2-00018.md) 约束）；本地 PCC 方式下，USERPROFILENAME 须跨网元一致。
- **位置代际分叉**：ADD USRLOCATION 的 LOCATIONTYPE（CGI/ECGI/NCGI）决定位置码参数（2/3G LAC+CI / 4G ECI / 5G NCI），配置生成按部署代际选其一。

## 决策点

### DP-1：部署场景选择（UNC 侧，详见 [2-00013](task/UNC/20.15.2/2-00013.md) 决策点）

| 选项/场景 | 影响（UNC 配置 / UDG 配置 / 跨网元） |
|---|---|
| 有 PCRF/PCF 动态 | UNC 仅 License（PCRF 决策，UNC 无新增）；UDG 执行动态规则；RULENAME 跨网元一致 |
| 有 PCRF/PCF 预定义规则 | UNC License + 位置链 + 绑 APN；UDG 执行预定义规则（USERPROFILENAME 一致） |
| 无 PCRF/PCF 或本地 PCC | UNC License + 位置链 + 绑 APN + 本地规则（引用 BWM/PCC）；UDG 本地 RULE |

### DP-2：位置代际选择（UNC 侧，代际分叉）

| 选项/场景 | 影响（LOCATIONTYPE / 位置码参数） |
|---|---|
| 2/3G（CGI） | LOCATIONTYPE=CGI；位置码=LAC+CI |
| 4G（ECGI） | LOCATIONTYPE=ECGI；位置码=ECI |
| 5G（NCGI） | LOCATIONTYPE=NCGI；位置码=NCI |

### DP-3：位置策略动作维度（★与带宽控制交集）

| 选项/场景 | 影响（动作 RULE 引用 / 关联场景） |
|---|---|
| 位置触发带宽控制 | 动作 RULE 引用 [BWM](task/UNC/20.15.2/2-00010.md)；关联带宽控制场景 |
| 位置触发访问限制 | 动作 RULE 引用 PCC（POLICYTYPE=PCC，阻塞/重定向等）；属本访问限制场景 |
| 位置触发计费 | 动作 RULE 引用计费三件套（PCCPOLICYGRP 绑 URRGROUP）；关联计费场景 |

## 约束

- **位置策略 License 前置**（critical，UNC 侧）：SET LICENSESWITCH 开启 `LKV2PCIAL01`（WSFD-211001）— 未开则特性不生效（License 编号交叉验证自 [2-00013](task/UNC/20.15.2/2-00013.md) 约束段，非推断）。
- **PCC基本功能 License 前置**（critical，UDG 侧）：开启 `LKV3G5PCCB01`（GWFD-020351）— UDG 执行 PCC 策略必需（交叉验证自 [2-00018](task/UDG/20.15.2/2-00018.md) 约束段）。
- **SA-Basic License 前置**（critical，策略含业务维度时，UDG 侧）：开启 `LKV3G5SABS01`（GWFD-110101）— 业务识别必需（交叉验证自 [2-00019](task/UDG/20.15.2/2-00019.md) 约束段）。
- **依赖带宽控制**（info，UNC 侧）：策略动作若为带宽控制，须先完成 [2-00010 BWM](task/UNC/20.15.2/2-00010.md)（activation 声明）——这是动作维度依赖，非位置链依赖。
- **代际分叉**（warning，UNC 侧）：LOCATIONTYPE=CGI/ECGI/NCGI 决定位置码参数（2/3G LAC+CI / 4G ECI / 5G NCI）。
- **RULENAME/USERPROFILENAME 跨网元一致**（critical）：动态规则的 RULENAME 须 UNC/UDG/SMF/PCF 间一致；本地 PCC 的 USERPROFILENAME 须跨网元一致 — 不一致则会话匹配失败（[2-00018](task/UDG/20.15.2/2-00018.md) 约束）。
- **CP-UP 配置一致性**（warning）：UDG 每 30 分钟扫描，RULE/UserProfile 不一致产生 ALM-81054 告警；控制面优先。

## 关联

- 上游场景：[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)
- 编排特性（feature task，优先）：[2-00013 UNC 位置策略](task/UNC/20.15.2/2-00013.md) · [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md) · [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)
- 复用步骤/命令（compound/atom，按需）：UNC [1-00019](task/UNC/20.15.2/1-00019.md) 配置用户位置与模板绑定 · [0-00008](task/UNC/20.15.2/0-00008.md) ADD APNUSRPROFG · [0-00180](task/UNC/20.15.2/0-00180.md) SET LICENSESWITCH；UDG [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定
- 跨场景关联：[带宽控制 BWM CS](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md)（动作维度依赖）· [策略匹配基础 CS](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md)（backbone）
- 证据：[激活基于初始接入位置的策略控制](evidence/UNC/20.15.2/激活基于初始接入位置的策略控制_27915138.md)（UNC 侧主源，5 命令完整脚本，CGI/ECGI/NCGI 三代际）
