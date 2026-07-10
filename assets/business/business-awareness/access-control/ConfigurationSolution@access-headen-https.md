---
id: ConfigurationSolution@access-headen-https
type: ConfigurationSolution
name: HTTPS 头增强
domain: business-awareness
scenario: access-control
status: draft
---

# HTTPS 头增强

> 将用户信息以 TLS Extension TLV 格式插入 HTTPS Client Hello 报文头传 Web Server，POLICYTYPE=HEADEN，独立 ADD TLSHEADEN（非复用 HTTP 的 ADD HEADEN）。属于[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)场景。

## 概览

HTTPS 头增强是头增强协议族的 **HTTPS 协议变种**——因 HTTPS 报文是 TLS 加密的，HTTP 头增强（ADD HEADEN）无法直接处理，需先 SA 解密识别（依赖 HTTP2.0 Host 识别解析 SNI），再用 **ADD TLSHEADEN** 在 TLS Client Hello Extension 字段按 **TLV（Type-Length-Value）格式**插入字段。

**与 HTTP/RTSP 头增强的本质差异**（[头增强差异表](evidence/business/access-control/头增强功能之间的差异_10706790.md) + [2-00012](task/UDG/20.15.2/2-00012.md) 配置概览）：
- **配置对象不同**：HTTPS 用 **ADD TLSHEADEN**（TLSTYPEVAL+SUBTLSTYPEVAL 编码，**无 PREFIXNAME 参数**——字段名不进报文，靠 TLV 编码）；HTTP/RTSP 用 ADD HEADEN（`<前缀: 值>` 文本格式，有 PREFIXNAME）。**配置不与 HTTP 头增强重叠**（不同对象）——这是本 CS 独立于 [HTTP/RTSP 头增强 CS](business/business-awareness/access-control/ConfigurationSolution@access-headen-http.md) 的根本原因。
- **核心机制一致**：RULE 经 `POLICYTYPE=HEADEN` 直接引用 HEADEN 对象，独立于 PCC/SMARTREDIRECT，**不经 PCCPOLICYGRP**（PCC 策略组名称=NULL）。
- **HTTPS 独有强依赖**：HTTP2.0 Host 识别（GWFD-110201，解析 HTTPS 的 SNI/证书必须开启）——HTTP/RTSP 头增强无此依赖。
- **加密算法收敛**：HTTPS **不支持 RSA**（仅 10 种；HTTP/RTSP 支持 RSA）；**不支持 MULTIPARA 拼接**。
- **HTTPS 独有十六进制编码**：软参 Byte837 Bit5 控未加密场景字段值十六进制编码。
- **防欺诈支持**：HTTPS 支持（与 HTTP 一致，ANTIFRAUD=ENABLE 内嵌 ADD TLSHEADEN）。

**仅 HTTP2.0 回落场景**：HTTPS 头增强只支持 TLS1.0/1.1/1.2/1.3（遵循 IETF 5246 TLS 1.2）；Client Hello 报文分片不支持。

## 配置与协同

本方案编排 **2 个特性**：UDG [HTTPS头增强 2-00012](task/UDG/20.15.2/2-00012.md)（核心）+ [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md)（依赖前提，含 HTTP2.0 Host 识别强依赖）。PCC基本功能可选（计费叠加时配）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯 [头增强差异表](evidence/business/access-control/头增强功能之间的差异_10706790.md) + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [HTTPS头增强 2-00012](task/UDG/20.15.2/2-00012.md) | 核心（方案主体） | 必配 | POLICYTYPE=HEADEN + **独立 ADD TLSHEADEN**（TLS Extension TLV，TLSTYPEVAL+SUBTLSTYPEVAL，**无 PREFIXNAME**）；配置**不与 HTTP 头增强重叠**（不同对象 TLSHEADEN vs HEADEN）。License `LKV3G5HTSE01`（与 HTTP `LKV3G5HTHE01` 不同）。支持防欺诈（ANTIFRAUD=ENABLE 内嵌 ADD TLSHEADEN） |
| [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提·识别） | 必配（License 前置） | HTTPS 报文解析基础。+ SA-Web Browsing（GWFD-110103，`LKV3G5SAWB01`）+ **HTTP2.0 Host 识别**（GWFD-110201，`LKV3G5HSHA01`，HTTPS 独有强依赖——解析 SNI/证书必须开启）。配置**不重叠**——SA 配识别链，HTTPS 头增强配 TLSHEADEN 对象 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。
>
> **HTTPS 独立 CS 根因**：配置对象不同（TLSHEADEN vs HEADEN）——非协议参数变种（RTSP 那种共享 ADD HEADEN），而是独立命令对象。故 HTTPS 头增强不与 HTTP/RTSP 头增强共用 CS。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 用户面：HTTPS 头增强（[2-00012](task/UDG/20.15.2/2-00012.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**（HTTPS 独有，区别 HTTP/RTSP）：

- **配置对象变种**（critical）：**ADD TLSHEADEN**（[0-00292](task/UDG/20.15.2/0-00292.md)，TLV 格式：TLSTYPEVAL+SUBTLSTYPEVAL，**无 PREFIXNAME**）——非 ADD HEADEN（[0-00291](task/UDG/20.15.2/0-00291.md)，`<前缀: 值>` 文本）。字段名不进报文，靠 TLSTYPEVAL/SUBTLSTYPEVAL 在 Extension 内 TLV 编码。
- **协议绑定变种**：PROTOCOLNAME=**https** + 端口=**443**（HTTP=80，RTSP=554）；基于 **SNI** 触发（HTTPS 主流，activation 演示）——L7FILTER 的 URL 实为 SNI（如 www.huawei.com/*）。
- **License 变种**：`LKV3G5HTSE01`（HTTP=`LKV3G5HTHE01`，RTSP=`LKV3G5RTHE01`）。
- **SA 依赖变种**：SA-Basic + SA-Web Browsing + **HTTP2.0 Host 识别**（GWFD-110201，`LKV3G5HSHA01`，HTTPS 独有强依赖——解析 SNI/证书必须开启）。
- **排除 RSA 加密**（info）：HTTPS 头增强 ENCRYALGORI 不支持 RSA*（HTTP/RTSP 支持）——需 RSA 加密改用 HTTP 头增强。
- **排除 MULTIPARA 拼接**（info）：HTTPS 不支持 MULTIPARA1/2/3 多参数拼接（HTTP/RTSP 20.10.0+ 支持）——需拼接场景改用 HTTP 头增强。
- **HTTPS 独有十六进制编码变种**：软参 Byte837 Bit5 控未加密场景字段值十六进制编码（`SET SOFTPARA:DT=BYTE,BYTENUM=837,BYTEVALUE=16`；证据：[GWFD-110263](feature/UDG/20.15.2/GWFD-110263.md) §安全机制 + 软参文档）。
- **防欺诈支持**（与 HTTP 一致）：ANTIFRAUD=ENABLE 内嵌 ADD TLSHEADEN；License 双开 `LKV3G5HHAS01` + `LKV3G5HTSE01`。**RTSP 不支持防欺诈**（差异表）。

### UDG 用户面：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task），**无特性级变种**。SA-Basic 提供 HTTPS 报文解析基础 + SA-Web Browsing + **HTTP2.0 Host 识别**（HTTPS 独有强依赖）。

### 跨特性协同：HTTPS 头增强与 HTTP 头增强的正交性

- **配置对象正交**：HTTPS 用 ADD TLSHEADEN（TLV 格式），HTTP/RTSP 用 ADD HEADEN（文本格式）——**不同对象，不重叠**。配 HTTPS 头增强时**不另建 HEADEN**，反之亦然。
- **多协议共存**：基于 IP 触发时同时影响 HTTP/RTSP/HTTPS（不区分协议）——需多协议头增强时各协议分别配对应对象（HEADEN + TLSHEADEN），RULE 绑同一 USERPROFILE 共存（见 [策略匹配基础 CS](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md) 多 RULE 机制）。基于 SNI/URL 触发可规避跨协议影响。
- **头增强与计费叠加**（双 RULE 模式）：一条 RULE(POLICYTYPE=HEADEN) + 一条 RULE(POLICYTYPE=PCC)，**共用同一 FLOWFILTER**，绑同一 USERPROFILE——activation 演示双 RULE 模式（[2-00012](task/UDG/20.15.2/2-00012.md) activation §表8/§表9）。
- **防欺诈跨协议**：HTTP/HTTPS 支持防欺诈（ANTIFRAUD=ENABLE 内嵌 ADD HEADEN / ADD TLSHEADEN）；RTSP 不支持。需多协议防欺诈时 HTTP+HTTPS 分别启用，RTSP 不配。

## 决策点

### DP-1：触发方式（HTTPS 独有 SNI）

决定 HTTPS 头增强按什么条件触发——影响过滤链走法。

| 选项/场景 | 影响（过滤链走法 / SNI） |
|---|---|
| 基于 SNI（HTTPS 主流，activation 演示） | L7FILTER（URL=SNI，如 www.huawei.com/*）+ PROTBINDFLOWF（**https**+L7FILTER） |
| 基于特定 IP | FILTER（SVRIP+端口=**443**）+ FLTBINDFLOWF（**不配协议**，同时影响 HTTP/RTSP/HTTPS） |
| 基于 HTTPS 协议 | PROTBINDFLOWF（**https**，无 L7FILTER） |

### DP-2：防欺诈启用（HTTPS 支持，与 HTTP 一致）

决定是否启用 HTTPS 头防欺诈——影响 ADD TLSHEADEN 参数 + License。

| 选项/场景 | 影响（ANTIFRAUD / License） |
|---|---|
| 不启用防欺诈（默认） | ADD TLSHEADEN 的 ANTIFRAUD=DISABLE（默认）；仅 HTTPS 头增强 License `LKV3G5HTSE01` |
| 启用防欺诈 | ADD TLSHEADEN 的 **ANTIFRAUD=ENABLE**；License 双开 `LKV3G5HHAS01`（防欺诈）+ `LKV3G5HTSE01`（HTTPS 头增强）；插入前先检测纠正 |
| 灰名单模式 | ANTIFRAUD=ENABLE + GRAYLIST=ENABLE；只检测纠正不插入 |

### DP-3：加密算法（HTTPS 收敛，无 RSA）

决定头增强字段值的加密方式——HTTPS 不支持 RSA。

| 选项/场景 | 影响（ENCRYALGORI） |
|---|---|
| 不加密（默认） | ENCRYALGORI=NONE |
| AES 加密（安全推荐） | AES128_GCM/AES256_GCM（+PSWDKEY+SET AES，**无 RSA**） |
| 哈希加密 | SHA256（+PSWDKEY+SALTSW） |
| 十六进制编码（HTTPS 独有） | NONE + 软参 Byte837 Bit5（`SET SOFTPARA:DT=BYTE,BYTENUM=837,BYTEVALUE=16`） |

### DP-4：TLS Type 规划（HTTPS 独有 TLV）

决定 TLS Extension 内 TLV 的 Type 值规划——HTTPS 独有（HTTP/RTSP 用 PREFIXNAME 文本前缀）。

| 选项/场景 | 影响（TLSTYPEVAL / SUBTLSTYPEVAL） |
|---|---|
| 标准 TLV Type（activation 演示） | TLSTYPEVAL=1000 + SUBTLSTYPEVAL=10/20/30/40（对应不同字段 APN/IMSI/MSIP/MSISDN） |
| 自定义 TLV Type | 按业务规划 TLSTYPEVAL + SUBTLSTYPEVAL（须 Web Server 侧对齐解析） |

## 约束

- **HTTPS头增强 License 前置**（critical）：SET LICENSESWITCH 开启 `LKV3G5HTSE01`（HTTPS 头增强 License，与 HTTP `LKV3G5HTHE01` 不同）— 未开则 HTTPS 头增强不生效（[2-00012](task/UDG/20.15.2/2-00012.md) License）。
- **防欺诈 License 双开**（critical，防欺诈时）：`LKV3G5HHAS01`（防欺诈）**且** `LKV3G5HTSE01`（HTTPS 头增强）——任一未开则防欺诈不生效。
- **SA-Basic + SA-Web + HTTP2.0 Host 识别 License 前置**（critical）：SA-Basic（`LKV3G5SABS01`）+ SA-Web Browsing（`LKV3G5SAWB01`）+ **HTTP2.0 Host 识别**（`LKV3G5HSHA01`，HTTPS 独有强依赖——解析 SNI/证书必须开启）— 未开则无法解析 HTTPS。
- **POLICYTYPE=HEADEN 触发**（critical）：RULE.POLICYTYPE=HEADEN + POLICYNAME=HEADERENNAME（直接引用，PCC 策略组名称=NULL）— 指错则头增强不触发。
- **必须用 ADD TLSHEADEN（不可用 ADD HEADEN）**（critical）：HTTPS 头增强必须用 ADD TLSHEADEN（含 TLSTYPEVAL 参数，TLV 格式插入 TLS Extension）；ADD HEADEN 只处理 HTTP/RTSP — 混用则 HTTPS 报文不做头增强。
- **仅支持 TLS1.0/1.1/1.2/1.3**（warning）：遵循 IETF 5246 TLS 1.2 — 其他 TLS 版本报文不做头增强。
- **Client Hello 报文分片不支持**（warning）：HTTPS 的 Client Hello 报文分片场景不支持头增强 — 分片报文不做头增强。
- **基于 IP 触发同时影响 HTTP/RTSP/HTTPS**（warning）：不区分协议，对用户的 HTTP/RTSP/HTTPS 报文都做头增强（设计如此）— 后果：HTTP/RTSP 报文意外被头增强；改用基于 SNI 触发可规避。
- **不支持 RSA 加密**（info）：HTTPS ENCRYALGORI 不支持 RSA*（HTTP/RTSP 支持）— 需 RSA 改用 HTTP 头增强。
- **不支持 MULTIPARA 拼接**（info）：HTTPS 不支持 MULTIPARA1/2/3 — 需拼接改用 HTTP 头增强。
- **规格**（info）：≤100 HTTPS 头增强动作；≤500 TLSHeadEn 前缀字段；≤32 TLS Type 启防欺诈；单报文 ≤16 前缀开防欺诈；新增防欺诈项 30 秒内生效；头增强仅针对上行报文。
- **法律声明**（info）：HTTPS 头增强插入用户标识（IMSI/MSISDN/IP）有泄露个人身份信息风险，须遵循当地法律启用。
- **先计费再头增强**（info）：与规则优先级无关，头增强插入信息不计入业务量计费统计。

## 关联

- 上游场景：[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)
- 基础 CS：[策略匹配基础](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md)（共享 backbone + POLICYTYPE=HEADEN 选择）
- 编排特性（feature task，优先）：[2-00012 HTTPS头增强](task/UDG/20.15.2/2-00012.md) · [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)
- 复用步骤/命令（compound/atom，按需）：[1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00013](task/UDG/20.15.2/1-00013.md) 头增强对象配置（HTTPS 场景走 ADD TLSHEADEN）· [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套（可选）· [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00016](task/UDG/20.15.2/1-00016.md) SA 协议识别链 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00292](task/UDG/20.15.2/0-00292.md) ADD TLSHEADEN · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV
- 族内 CS：[HTTP/RTSP 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-http.md)（ADD HEADEN，配置对象不同）
- 证据：[激活HTTPS头增强](evidence/UDG/20.15.2/激活HTTPS头增强_60329629.md) · [增加HTTPS头增强](evidence/UDG/20.15.2/增加HTTPS头增强（ADD-TLSHEADEN）_82837521.md) · [头增强功能之间的差异](evidence/business/access-control/头增强功能之间的差异_10706790.md)（HTTP/HTTPS/RTSP 差异权威表）
