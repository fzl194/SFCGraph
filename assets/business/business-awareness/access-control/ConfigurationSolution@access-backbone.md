---
id: ConfigurationSolution@access-backbone
type: ConfigurationSolution
name: 策略匹配基础
domain: business-awareness
scenario: access-control
status: draft
---

# 策略匹配基础

> 访问限制所有动作（阻断/重定向/头增强/URL过滤/IP重定向）的公共底座：RULE+USERPROFILE+RULEBINDING+过滤链+SA-Basic 共享 backbone，RULE.POLICYTYPE 是动作总开关。属于[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)场景。

## 概览

策略匹配基础是访问限制场景的**基础范本**（类似计费场景的"内容计费基础"）：所有访问限制动作共用同一套 backbone——三四层/七层过滤链（FILTER/FLOWFILTER/FLTBINDFLOWF/PROTBINDFLOWF）+ 业务规则（ADD RULE）+ 用户模板（ADD USERPROFILE）+ 绑定（ADD RULEBINDING）+ SA-Basic 协议识别前提。**动作的选择由 RULE.POLICYTYPE 这一个参数决定**——它是访问限制的总开关。

**双轨道架构**（追溯 ADD RULE 命令 + 套餐3实例 + 头增强差异表）：
- **轨道 A（POLICYTYPE 隐式动作）**：RULE.POLICYTYPE 取值决定动作——PCC（策略/计费控制，多功能：阻塞 DISCARD/URL 重定向/计费触发）/ HEADEN（头增强）/ SMARTREDIRECT（智能重定向）/ WEBPROXY（Web 代理）/ ADC（应用检测）/ IPREDIR（IP 重定向）。**单条 RULE 内 POLICYTYPE 互斥**（一条 RULE 只能选一种动作）。
- **轨道 B（CF 显式动作）**：URL 过滤的 CFTEMPLATE.ACTION 决定动作（允许/阻断/重定向），APN 粒度开启；但**流匹配仍走 RULE.POLICYTYPE=PCC backbone**（非纯独立轨道）。

**★多 RULE 共存机制**（防"都得配"误解的核心，套餐3权威验证）：不同动作的 RULE 可**绑定同一 USERPROFILE 共存**——同一用户同时受多种访问限制动作控制。套餐3实例（[套餐3：访问限制场景](evidence/business/access-control/套餐3：访问限制场景_94838086.md)）演示 4 条 RULE 绑同一 USERPROFILE 共存：ruleA(PCC) + ruleB(HEADEN) + ruleC(IPREDIR) + ruleD(PCC)，4 个 RULEBINDING 指向同一 `up_policy`。**POLICYTYPE 互斥仅在"单条 RULE 内"——不是"整个用户只能配一种动作"**。

本 CS 是其他动作 CS（[URL 过滤](business/business-awareness/access-control/ConfigurationSolution@access-url-filter.md) / [HTTP/RTSP 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-http.md) / [HTTPS 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-https.md) / 用户 Portal / WebProxy / 智能重定向 / 位置策略）的基础——其他 CS 在此 backbone 上选 POLICYTYPE + 配对应动作对象。

## 配置与协同

本 CS 编排 **2 个特性 + 共享 backbone compound**：UDG [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md)（依赖前提）+ [PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md)（PCC 子轨 + PCCPOLICYGRP backbone 基准）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档 RULE 概念 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配（License 前置） | 业务识别前提，所有访问限制动作依赖其 L3/L4+L7 协议解析能力（识别后的业务流标签供 RULE 匹配引擎消费）。配置**不与动作特性重叠**——SA 配识别链（SIGNATUREDB/PARSERDB/WELLKNOWNPORT），动作特性配 RULE/动作对象 |
| [PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md) | 基础（依赖前提 + PCCPOLICYGRP backbone） | 必配 | 双重角色：①PCC 子轨（POLICYTYPE=PCC，承载阻塞/URL重定向/计费触发等多功能）的基准范例；②PCCPOLICYGRP backbone 的提供者——其他动作 CS（如计费叠加）经 PCCPOLICYGRP 绑 URRGROUP。配置**部分重叠**——PCC 配 RULE/USERPROFILE/RULEBINDING + PCCPOLICYGRP，是本 CS backbone 的标准范例 |
| 过滤链（[1-00009](task/UDG/20.15.2/1-00009.md)）+ 规则绑定（[1-00011](task/UDG/20.15.2/1-00011.md)） | 核心（backbone compound） | 必配 | 所有 POLICYTYPE 动作的公共底座；POLICYTYPE 在 ADD RULE 选——6 子轨互斥，多动作通过多 RULE 绑同一 USERPROFILE 共存（见概览多 RULE 机制） |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。
>
> **依赖前提特性必须进矩阵**：SA-Basic、PCC基本功能是 License 前置的依赖前提，必须作为矩阵行（角色=基础，必配列注明 License 前置），不只在约束段提。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 用户面：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task），**无特性级变种**。SA-Basic 提供 L3/L4+L7 协议识别能力（`LOD SIGNATUREDB` 特征字识别 + `LOD PARSERDB` 深度解析 + `ADD WELLKNOWNPORT` 知名端口加速 + `ADD L7FILTER`/`ADD PROTBINDFLOWF` 七层匹配），是访问限制所有动作的识别前提——RULE 匹配引擎消费 SA 识别后的业务流标签。

### UDG 用户面：PCC基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task），**无特性级变种**。PCC基本功能是本 CS 的 backbone 标准范例（POLICYTYPE=PCC + PCCPOLICYGRP + RULE + USERPROFILE + RULEBINDING）。本 CS 在此基础上**扩展 POLICYTYPE 选择维度**（见决策点 DP-1）——PCC 只是 6 子轨之一，其他动作 CS 选其他 POLICYTYPE。

### 跨特性协同：POLICYTYPE 6 子轨动作选择 + 多 RULE 共存

**POLICYTYPE 6 子轨**（RULE.POLICYTYPE 取值决定动作，单条 RULE 互斥）：

| POLICYTYPE | 动作 | POLICYNAME 指向 | 是否经 PCCPOLICYGRP | 承载 CS |
|---|---|---|---|---|
| PCC | 策略/计费控制（阻塞 DISCARD/URL重定向/计费触发）| PCCPOLICYGRPNM | 是（绑 URRGROUP）| 本 CS（PCC 子轨）+ [URL 过滤 CS](business/business-awareness/access-control/ConfigurationSolution@access-url-filter.md)（轨道B 触发）|
| HEADEN | 头增强（插入用户信息给 Web/Streaming Server）| HEADERENNAME（ADD HEADEN / ADD TLSHEADEN）| 否（直接引用）| [HTTP/RTSP 头增强 CS](business/business-awareness/access-control/ConfigurationSolution@access-headen-http.md) + [HTTPS 头增强 CS](business/business-awareness/access-control/ConfigurationSolution@access-headen-https.md) |
| SMARTREDIRECT | 智能重定向（Portal/HTTP重定向/DNS纠错）| 重定向动作对象名（随特性）| 否（直接引用）| 用户 Portal / 智能重定向 CS |
| WEBPROXY | Web 代理（L3 IP NAT 到代理池）| IPFARMNAME（IP Farm）| 否（直接引用）| WebProxy CS |
| ADC | 应用检测（不干预流量，仅检测记录）| PCCPOLICYGRPNM | 是（+ ADCMUTEFLAG=DISABLE）| 属带宽控制 ADC CS |
| IPREDIR | IP 重定向（L3 重定向到指定 IP）| 内嵌 RULE（REDIRIPVERFLAG+IPREDIRECTIP）| 否（直接引用）| 属访问限制 IP 重定向 |

> POLICYTYPE 证据：[规则](evidence/business/access-control/规则_92407887.md) RULE 概念 + [ADD RULE](evidence/business/access-control/ADD_RULE_82837266.md) 命令 + [1-00011](task/UDG/20.15.2/1-00011.md) 场景差异表。

**多 RULE 共存**（套餐3实例权威验证）：同一 USERPROFILE 可绑多条不同 POLICYTYPE 的 RULE——用户同时受多种动作控制。示例（[套餐3：访问限制场景](evidence/business/access-control/套餐3：访问限制场景_94838086.md)）：
```
ADD USERPROFILE:USERPROFILENAME="up_policy";
ADD RULEBINDING:USERPROFILENAME="up_policy",RULENAME="ruleA",POLICYTYPE=PCC;
ADD RULEBINDING:USERPROFILENAME="up_policy",RULENAME="ruleB",POLICYTYPE=HEADEN;
ADD RULEBINDING:USERPROFILENAME="up_policy",RULENAME="ruleC",POLICYTYPE=IPREDIR;
ADD RULEBINDING:USERPROFILENAME="up_policy",RULENAME="ruleD",POLICYTYPE=PCC;
```
> 关键：POLICYTYPE 互斥**仅在单条 RULE 内**（一条 RULE 只能一种动作）——不是"整个用户只能配一种动作"。多动作=多 RULE 共存，共享 backbone。

## 决策点

### DP-1：POLICYTYPE 动作选择（访问限制核心决策）

进入访问限制场景的首要决策，决定走哪个 ConfigurationSolution + 选哪种 POLICYTYPE。

| 选项/场景 | 影响（POLICYTYPE / POLICYNAME 指向 / 承载 CS） |
|---|---|
| PCC（策略/计费控制·阻塞/URL重定向/计费触发）| POLICYTYPE=PCC + POLICYNAME=PCCPOLICYGRPNM；经 PCCPOLICYGRP 绑 URRGROUP；本 CS + URL过滤 CS（轨道B 触发）|
| HEADEN（头增强）| POLICYTYPE=HEADEN + POLICYNAME=HEADERENNAME（ADD HEADEN / ADD TLSHEADEN）；不经 PCCPOLICYGRP；HTTP/RTSP CS + HTTPS CS |
| SMARTREDIRECT（智能重定向·Portal/HTTP重定向/DNS纠错）| POLICYTYPE=SMARTREDIRECT + POLICYNAME=重定向对象名；不经 PCCPOLICYGRP；用户Portal/智能重定向 CS |
| WEBPROXY（Web 代理·L3 IP NAT）| POLICYTYPE=WEBPROXY + POLICYNAME=IPFARMNAME；不经 PCCPOLICYGRP；WebProxy CS |
| ADC（应用检测·仅检测记录）| POLICYTYPE=ADC + POLICYNAME=PCCPOLICYGRPNM；经 PCCPOLICYGRP（ADCMUTEFLAG=DISABLE）；属带宽控制 ADC |
| IPREDIR（IP 重定向·L3）| POLICYTYPE=IPREDIR + 内嵌 RULE（REDIRIPVERFLAG+IPREDIRECTIP）；不经 PCCPOLICYGRP |

### DP-2：多动作共存策略

当用户需同时受多种访问限制动作控制时的 RULE 编排策略。

| 选项/场景 | 影响（RULE 编排 / USERPROFILE 绑定） |
|---|---|
| 单动作（仅一种 POLICYTYPE）| 单条 RULE + 单 RULEBINDING；最简配置 |
| 多动作共存（多种 POLICYTYPE 同用户）| 多条 RULE（各选不同 POLICYTYPE）+ 多条 RULEBINDING 指向**同一 USERPROFILE**（套餐3实例：4 业务 4 条 RULE 共存）|
| 动作+计费叠加（如 HEADEN+PCC 计费）| 双 RULE：一条 POLICYTYPE=HEADEN + 一条 POLICYTYPE=PCC，**共用同一 FLOWFILTER**（HTTP头增强 activation 演示双 RULE 模式）|

## 约束

- **SA-Basic License 前置**（critical）：SET LICENSESWITCH 开启 `LKV3G5SABS01` — 未开则协议识别失败、所有访问限制动作不生效（[2-00019](task/UDG/20.15.2/2-00019.md) License）。
- **PCC基本功能 License 前置**（critical）：SET LICENSESWITCH 开启 `LKV3G5PCCB01` — 未开则 PCC 子轨动作（阻塞/URL重定向/计费触发）+ PCCPOLICYGRP backbone 不生效（[2-00018](task/UDG/20.15.2/2-00018.md) License）。
- **POLICYTYPE 单 RULE 互斥**（critical）：一条 RULE 只能选一种 POLICYTYPE（PCC/HEADEN/SMARTREDIRECT/WEBPROXY/ADC/IPREDIR 六选一）— 配错则动作不触发。**但多 RULE 可绑同一 USERPROFILE 共存**（多动作共存机制，非互斥）。
- **POLICYTYPE 决定 POLICYNAME 指向**（critical）：PCC→PCCPOLICYGRPNM（经 PCCPOLICYGRP）；HEADEN→HEADERENNAME（直接引用 HEADEN/TLSHEADEN 对象）；SMARTREDIRECT/WEBPROXY→对应动作对象名；指错则规则链断开（[1-00011](task/UDG/20.15.2/1-00011.md) 场景差异）。
- **FLOWFILTER 至少绑一个 filter**（critical）：ADD FLOWFILTER 须至少绑一个 ADD FILTER 或 ADD L7FILTER — 否则所有报文都匹配不上（[1-00009](task/UDG/20.15.2/1-00009.md) 约束）。
- **REFRESHSRV 时序**（critical）：`SET REFRESHSRV:REFRESHTYPE=ALL`（或 USERPROFILE）必须在所有 ADD/SET 完成后最后执行；`PROTBINDFLOWF` 配置后需等待 60 秒再执行 REFRESHSRV — 不执行或时序错则 FILTER 配置变更不生效（[2-00019](task/UDG/20.15.2/2-00019.md) 约束）。
- **USERPROFILENAME 跨网元一致**（critical）：须 PCF/SMF/UPF 间一致（动态/预定义规则）— 不一致则会话匹配失败（[2-00018](task/UDG/20.15.2/2-00018.md) 约束）。
- **RULENAME+POLICYTYPE 唯一**（warning）：存在多条数据时，RULENAME+POLICYTYPE 不能完全相同 — 重复则新增失败（[1-00011](task/UDG/20.15.2/1-00011.md) 约束）。
- **CP-UP 配置一致性**（warning）：UDG 每 30 分钟扫描，RULE/UserProfile 不一致产生 ALM-81054 告警；控制面优先。

## 关联

- 上游场景：[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)
- 编排特性（feature task，优先）：[2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md) · [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md)
- 复用步骤/命令（compound/atom，按需）：[1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则与用户模板绑定 · [1-00016](task/UDG/20.15.2/1-00016.md) SA 协议识别链 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV
- 下游动作 CS：[URL 过滤](business/business-awareness/access-control/ConfigurationSolution@access-url-filter.md) · [HTTP/RTSP 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-http.md) · [HTTPS 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-https.md)
- 证据：[套餐3：访问限制场景](evidence/business/access-control/套餐3：访问限制场景_94838086.md)（4业务4RULE共存权威验证）· [规则](evidence/business/access-control/规则_92407887.md)（RULE/POLICYTYPE 概念）· [ADD RULE](evidence/business/access-control/ADD_RULE_82837266.md)（POLICYTYPE 参数）
