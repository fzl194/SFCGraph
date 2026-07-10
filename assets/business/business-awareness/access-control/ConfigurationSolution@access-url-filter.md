---
id: ConfigurationSolution@access-url-filter
type: ConfigurationSolution
name: URL 过滤
domain: business-awareness
scenario: access-control
status: draft
---

# URL 过滤

> 按外部 ICAP Server 分析的 URL 分类做黑白名单过滤（允许/阻断/重定向），CF.ACTION 显式决定动作，流匹配走 PCC RULE backbone。属于[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)场景。

## 概览

URL 过滤对用户访问的 URL 按分类施加控制：UDG 经 ICAP 把 URL 发外部 ICAP Server 分析分类，按 CF 策略-模板-分类体系执行动作（PERMIT/BLOCK/REDIRECT）。它是访问限制场景**双轨道架构的轨道 B**（CF 显式动作）——但**非纯独立轨道**：流匹配仍走 RULE.POLICYTYPE=PCC backbone（轨道 A 的 PCC 子轨触发）。

**双轨道协同**（[2-00002](task/UDG/20.15.2/2-00002.md) 配置概览）：
- **轨道 A（PCC 触发）**：三四层匹配 + PCC 费率策略组 + RULE(POLICYTYPE=PCC) 触发 URL 过滤业务流。PCCPOLICYGRP 是 URL 过滤流的匹配骨架（可绑 URRGROUP 计费，也可纯策略不计费）。
- **轨道 B（CF 内容匹配）**：CF 策略-模板-分类体系——CFTEMPLATE.ACTION 决定缺省动作（允许/阻断/重定向），CONTCATEGBIND.ACTION（分类绑定）**优先**于缺省动作。APN 粒度开启（`SET APNCFFUNC`）或全局粒度（`SET GLBCFFUNC`）。

本方案编排 3 个特性：UDG [URL过滤 2-00002](task/UDG/20.15.2/2-00002.md)（核心）+ [PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md)（backbone）+ [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md)（识别前提）。ICAP 外置分析可选（轨道 B 的外置增强）。

## 配置与协同

本方案编排 **3 个特性**：UDG [2-00002 URL过滤](task/UDG/20.15.2/2-00002.md) + [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md) + [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯 [2-00002](task/UDG/20.15.2/2-00002.md) 依赖声明 + feature task）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [URL过滤 2-00002](task/UDG/20.15.2/2-00002.md) | 核心（轨道 B CF.ACTION + 轨道 A 触发） | 必配 | 本方案主体：CFTEMPLATE.ACTION（BLOCK/REDIRECT/PERMIT）+ CF 策略-模板-分类体系（CFPROFILE/CFTEMPLATE/CONTCATEGROUP/CONTCATEGBIND）+ APN 粒度开关（APNCFFUNC）；非纯独立轨道，流匹配依赖 PCC backbone |
| [PCC基本功能 2-00018](task/UDG/20.15.2/2-00018.md) | 基础（依赖前提·backbone） | 必配 | URL 过滤流匹配走 RULE.POLICYTYPE=PCC backbone（过滤链 + RULE + PCCPOLICYGRP + USERPROFILE + RULEBINDING）；PCCPOLICYGRP 可绑 URRGROUP 计费或纯策略不计费。配置**部分重叠**——PCC 的 RULE/USERPROFILE 骨架即 URL 过滤的流匹配骨架 |
| [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提·识别） | 必配（License 前置） | URL 分类需 SA 解析——HTTP/WAP→SA-Web Browsing（GWFD-110103）；HTTPS 仅 SNI 需 HTTP2.0 Host 识别（GWFD-110201）。配置**不重叠**——SA 配识别链，URL 过滤配 CF 体系 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。
>
> **依赖前提特性必须进矩阵**：PCC基本功能、SA-Basic 是 License 前置的依赖前提，必须作为矩阵行。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 用户面：URL过滤（[2-00002](task/UDG/20.15.2/2-00002.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**（URL 过滤 CS 独有）：

- **动作匹配模式变种**（CF.ACTION 决策，DP-1）：分类匹配（主流）= CFTEMPLATE.ACTION 兜底 + CONTCATEGBIND.ACTION（分类绑定，**优先**）；直接动作 = 仅 CFTEMPLATE.ACTION 兜底，省 CONTCATEGBIND。
- **粒度变种**（DP-2）：APN 粒度（`SET APNCFFUNC`，主流）vs 全局粒度（`SET GLBCFFUNC`）。
- **协议变种**（DP-3）：HTTP/WAP→SA-Web Browsing；HTTPS 仅 SNI→HTTP2.0 Host 识别（GWFD-110201）；各协议 SA 依赖不同。
- **ICAP 外置分析**（[1-00007](task/UDG/20.15.2/1-00007.md)）：可选——轨道 B 的外置增强（ADD ICAPSERVER + ICAPSVRGRP + ICAPSVRBINDISG）；CFTEMPLATE 引用 ICAPSRVGMNAME。不配 ICAP 则用本地分类。
- **本地 cache**（[0-00258](task/UDG/20.15.2/0-00258.md)）：可选——`SET CFCACHEPARA` 缓解每会话 ICAP 交互的性能开销。
- **白名单豁免**：CFWHITEURLLST（URL 白名单）/ CFIPWHITELIST（IP 白名单）——免过滤。

### UDG 用户面：PCC基本功能（[2-00018](task/UDG/20.15.2/2-00018.md)）

走标准配置方法（见 feature task），**无特性级变种**。PCC 提供 URL 过滤的流匹配 backbone（RULE.POLICYTYPE=PCC + PCCPOLICYGRP）。PCCPOLICYGRP.URRGROUPNAME：计费时绑 URRGROUP（走计费三件套 [1-00010](task/UDG/20.15.2/1-00010.md)）；纯策略阻断时 URRGROUPNAME 可省（直引 atom [0-00003](task/UDG/20.15.2/0-00003.md)）。

### UDG 用户面：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task），**无特性级变种**。SA-Basic 提供 URL 解析基础（HTTP/WAP 解析需 SA-Web Browsing；HTTPS SNI 解析需 HTTP2.0 Host 识别）。

### 跨特性协同：双轨道协同顺序

- **顺序**：ICAP 互通（[1-00007](task/UDG/20.15.2/1-00007.md)，可选）→ SA 识别链（[1-00016](task/UDG/20.15.2/1-00016.md)）→ CF 体系（[1-00008](task/UDG/20.15.2/1-00008.md)，轨道 B 核心）→ 过滤链（[1-00009](task/UDG/20.15.2/1-00009.md)，轨道 A 三四层）→ 计费三件套（[1-00010](task/UDG/20.15.2/1-00010.md)，轨道 A 费率组，可选）→ 规则绑定（[1-00011](task/UDG/20.15.2/1-00011.md)，POLICYTYPE=PCC 触发）→ `SET REFRESHSRV` 最后。
- **双轨道一致性**：CFTEMPLATE.ACTION（轨道 B 缺省）+ CONTCATEGBIND.ACTION（轨道 B 分类绑定，**优先**）决定动作；RULE.POLICYTYPE=PCC（轨道 A）决定流匹配。两轨道协同——PCC 触发流，CF 决定动作。
- **与轨道 A 重定向正交可叠加**：URL 过滤的 CF.ACTION=REDIRECT（轨道 B）与 SMARTREDIRECT/WEBPROXY（轨道 A 重定向）是不同机制——URL 过滤重定向按分类触发，SMARTREDIRECT/WEBPROXY 按 RULE.POLICYTYPE 触发；两者可叠加（多 RULE 共存，见 [策略匹配基础 CS](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md) 多 RULE 机制）。

## 决策点

### DP-1：动作匹配模式（CF.ACTION）

决定 CF 动作如何决定——分类绑定（精细）vs 直接动作（粗放）。

| 选项/场景 | 影响（CFTEMPLATE.ACTION / CONTCATEGBIND） |
|---|---|
| 分类匹配（主流） | CFTEMPLATE.ACTION=兜底（如 PERMIT）+ CONTCATEGBIND.ACTION=BLOCK/REDIRECT（分类绑定，**优先**于缺省）；配 CONTCATEGROUP + CONTCATEGBIND |
| 直接动作 | 仅 CFTEMPLATE.ACTION（如 BLOCK）兜底；省 CONTCATEGBIND/CONTCATEGROUP |

### DP-2：CF 粒度

决定 CF 功能在哪个层级开启。

| 选项/场景 | 影响（命令 / 粒度） |
|---|---|
| APN 粒度（主流） | `SET APNCFFUNC`（APN 级开关）+ `SET APNCFTEMPLATE`（APN 绑 CFTEMPLATE）；先 `ADD APN` |
| 全局粒度 | `SET GLBCFFUNC`（全局开关）；无 APN 绑定 |

### DP-3：协议与 SA 依赖

决定 URL 过滤覆盖哪些协议 + 各协议 SA 依赖。

| 选项/场景 | 影响（协议 / SA 依赖） |
|---|---|
| HTTP/WAP | SA-Web Browsing（GWFD-110103，License LKV3G5SAWB01）；Get/Post URL 解析 |
| WAP1.X | SA-Mobile（GWFD-110105）；WAP1.X 协议解析 |
| HTTPS（仅 SNI） | HTTP2.0 Host 识别（GWFD-110201，License LKV3G5HSHA01）；仅 SNI/证书，不解析加密内容 |
| 非加密 QUIC（仅 SNI/证书） | 同 HTTPS，仅 SNI |

### DP-4：ICAP 外置分析

决定是否用外置 ICAP Server 分析 URL 分类。

| 选项/场景 | 影响（ICAP 通道 / 性能） |
|---|---|
| 本地分类（无 ICAP） | 仅用本地分类规则；无 ICAP 交互开销 |
| ICAP 外置分析（可选增强） | 走 [1-00007](task/UDG/20.15.2/1-00007.md)（ADD ICAPSERVER + ICAPSVRGRP + ICAPSVRBINDISG）；CFTEMPLATE 引用 ICAPSRVGMNAME；每会话 ICAP 交互增 CPU + Get 首包时延，建议开 cache（[0-00258](task/UDG/20.15.2/0-00258.md)） |

## 约束

- **URL过滤 License 前置**（critical）：SET LICENSESWITCH 开启 `LKV3G5UFBF01` — 未开则 URL 过滤不生效（[2-00002](task/UDG/20.15.2/2-00002.md) License）。
- **SA-Basic + 协议 SA License 前置**（critical）：SA-Basic（`LKV3G5SABS01`）+ 协议对应 SA（HTTP/WAP→SA-Web Browsing `LKV3G5SAWB01`；HTTPS→HTTP2.0 Host 识别 `LKV3G5HSHA01`）— 未开则 URL 解析失败。
- **PCC基本功能 License 前置**（critical）：`LKV3G5PCCB01` — 未开则 PCC backbone 不生效，URL 过滤流不触发。
- **CONTCATEGBIND.ACTION 优先于 CFTEMPLATE.ACTION**（critical，分类匹配模式核心）：分类绑定的动作优先于模板缺省动作 — 配错则动作不符合预期（[2-00002](task/UDG/20.15.2/2-00002.md) 约束）。
- **ICAP 前置**（critical，ICAP 部署时）：必须先配 [1-00007](task/UDG/20.15.2/1-00007.md)，CFTEMPLATE 引用 ICAPSRVGMNAME — 漏配则 ICAP 分析不触发。
- **APN 粒度需先建 APN**（warning）：`SET APNCFFUNC` 前须 `ADD APN` — 否则 APN 粒度开关找不到 APN。
- **规格限制**（warning）：≤500 套餐 / ≤30 ICAP Server / 每组 ≤10 / ≤150 万 URL（[2-00002](task/UDG/20.15.2/2-00002.md) 约束）。
- **性能影响**（warning）：每会话与 ICAP 交互增 CPU + Get 首包时延；建议开 cache（[0-00258](task/UDG/20.15.2/0-00258.md)）缓解。
- **仅解析特定协议 URL**（info）：HTTP/WAP1.X/WAP2.0（Get/Post URL）/HTTPS/非加密 QUIC（仅 SNI/证书）— 其他协议不解析。

## 关联

- 上游场景：[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)
- 基础 CS：[策略匹配基础](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md)（共享 backbone + POLICYTYPE 选择）
- 编排特性（feature task，优先）：[2-00002 URL过滤](task/UDG/20.15.2/2-00002.md) · [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md) · [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)
- 复用步骤/命令（compound/atom，按需）：[1-00007](task/UDG/20.15.2/1-00007.md) ICAP互通 · [1-00008](task/UDG/20.15.2/1-00008.md) CF业务 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套（可选）· [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00016](task/UDG/20.15.2/1-00016.md) SA 协议识别链 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00020](task/UDG/20.15.2/0-00020.md) APN · [0-00251](task/UDG/20.15.2/0-00251.md) APNCFFUNC · [0-00258](task/UDG/20.15.2/0-00258.md) CFCACHEPARA · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV
- 证据：[配置URL过滤](evidence/UDG/20.15.2/配置URL过滤_47348205.md) · [GWFD-110471 URL过滤基本功能特性概述](evidence/UDG/20.15.2/GWFD-110471-URL过滤基本功能特性概述_56369529.md) · [配置到ICAP Server的互通数据](evidence/UDG/20.15.2/配置到ICAP Server的互通数据_75400117.md)
