---
id: ConfigurationSolution@access-headen-http
type: ConfigurationSolution
name: HTTP/RTSP 头增强
domain: business-awareness
scenario: access-control
status: draft
---

# HTTP/RTSP 头增强

> 将用户信息（MSISDN/IMSI/APN/MSIP 等）插入 HTTP/RTSP 请求报文头扩展字段传 Web/Streaming Server，POLICYTYPE=HEADEN，HTTP 与 RTSP 共享 ADD HEADEN（协议变种），含防欺诈内嵌分支。属于[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)场景。

## 概览

HTTP/RTSP 头增强是头增强协议族的**基础 CS**（HTTP 基础 + RTSP 协议变种）。HTTP 头增强将用户信息以 `<字段前缀: 字段值>` 格式插入 HTTP 请求报文头扩展字段传给 Web Server；RTSP 头增强是协议变种——共享 ADD HEADEN 命令，差异仅在协议绑定（PROTOCOLNAME=rtsp）+ License + SA 依赖（SA-Streaming）+ 知名端口（554）。

**核心机制**（[2-00010](task/UDG/20.15.2/2-00010.md) 配置概览）：RULE 经 `POLICYTYPE=HEADEN` **直接引用 HEADEN 对象**（ADD HEADEN 定义），独立于 PCC/SMARTREDIRECT 的第 3 种 POLICYTYPE，**不经 PCCPOLICYGRP**（调测输出 PCC 策略组名称=NULL）。RTSP 与 HTTP 共用 ADD HEADEN 命令（实时流协议在语法和操作上与 HTTP/1.1 类似，扩展机制基本相同）。

**头增强与计费可绑定同一 UserProfile**：activation 演示双 RULE 模式——一条 POLICYTYPE=HEADEN（头增强）+ 一条 POLICYTYPE=PCC（计费），**共用同一 FLOWFILTER**，绑同一 USERPROFILE（见 [策略匹配基础 CS](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md) 多 RULE 共存机制）。

**内嵌分支：HTTP 头防欺诈**（[2-00013](task/UDG/20.15.2/2-00013.md)，GWFD-110401）——防欺诈开关内嵌于 `ADD HEADEN` 的 `ANTIFRAUD` 参数，**不独立配置策略对象**，共用 HTTP 头增强的 HEADEN/RULE/FILTER 全套配置载体。防欺诈 License `LKV3G5HHAS01` + 头增强 License `LKV3G5HTHE01` 双开。**RTSP 按官方差异表不支持防欺诈**（见约束）。

## 配置与协同

本方案编排 **4 个特性**：UDG [HTTP头增强 2-00010](task/UDG/20.15.2/2-00010.md)（核心·HTTP）+ [RTSP头增强 2-00011](task/UDG/20.15.2/2-00011.md)（维度增强·协议变种）+ [HTTP头防欺诈 2-00013](task/UDG/20.15.2/2-00013.md)（内嵌分支）+ [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md)（依赖前提）。PCC基本功能可选（计费叠加时配）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯 [头增强差异表](evidence/business/access-control/头增强功能之间的差异_10706790.md) + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [HTTP头增强 2-00010](task/UDG/20.15.2/2-00010.md) | 核心（HTTP·族范本） | 必配 | POLICYTYPE=HEADEN + ADD HEADEN 多字段插入；头增强族基础。License `LKV3G5HTHE01`。配置对象=HEADEN（与 RTSP 共享，与 HTTPS 的 TLSHEADEN 不同） |
| [RTSP头增强 2-00011](task/UDG/20.15.2/2-00011.md) | 维度增强（协议变种） | 可选（RTSP 业务时） | **共享 ADD HEADEN**（非独立对象）——配置重叠：同一 HEADEN 对象，协议参数变（PROTOCOLNAME=rtsp vs http）+ License（`LKV3G5RTHE01`）+ SA 依赖（SA-Streaming GWFD-110107 vs SA-Web Browsing）+ 知名端口（554 vs 80）。**按官方差异表不支持防欺诈**（见约束） |
| [HTTP头防欺诈 2-00013](task/UDG/20.15.2/2-00013.md) | 内嵌分支（参数级内嵌） | 可选（需防欺诈时） | **ANTIFRAUD=ENABLE 参数内嵌 ADD HEADEN**（无独立策略对象）；共用 HTTP 头增强的 HEADEN/RULE/FILTER 全套配置载体。License `LKV3G5HHAS01` + `LKV3G5HTHE01` 双开。配置零差异（仅参数 ANTIFRAUD=ENABLE + PREFIXNAME 非标准头域名） |
| [SA-Basic 2-00019](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提·识别） | 必配（License 前置） | HTTP/RTSP 报文解析基础。+ 协议对应 SA：HTTP→SA-Web Browsing（GWFD-110103，`LKV3G5SAWB01`）；RTSP→SA-Streaming（GWFD-110107，`LKV3G5SAST01`）。配置**不重叠**——SA 配识别链，头增强配 HEADEN 对象 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。
>
> **RTSP 共享 ADD HEADEN 关键**：RTSP 不是独立配置对象——它与 HTTP 共用 ADD HEADEN 命令，差异仅在协议绑定参数 + License + SA 依赖。配 RTSP 时**不需另建 HEADEN 对象**，复用 HTTP 的 HEADEN 对象 + 改协议参数即可。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 用户面：HTTP 头增强（[2-00010](task/UDG/20.15.2/2-00010.md)）

走标准配置方法（见 feature task），**无特性级变种**（本 CS 即 HTTP 头增强的族范本）。POLICYTYPE=HEADEN + ADD HEADEN 多字段插入（HEADERENNAME+DATATYPE+PREFIXNAME+ENCRYALGORI）。触发方式变种（基于 URL/IP/HTTP 协议三选一）、加密变种、编码变种、防欺诈变种、灰名单变种——均见 feature task DP。

### UDG 用户面：RTSP 头增强（[2-00011](task/UDG/20.15.2/2-00011.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**（RTSP 协议变种独有）：

- **协议绑定变种**：`ADD PROTBINDFLOWF` 的 PROTOCOLNAME=**rtsp**（HTTP=http）；`ADD WELLKNOWNPORT` 端口=**554**（HTTP=80）。
- **License 变种**：`LKV3G5RTHE01`（HTTP=`LKV3G5HTHE01`）。
- **SA 依赖变种**：SA-Basic + **SA-Streaming**（GWFD-110107，`LKV3G5SAST01`）；HTTP=SA-Basic + SA-Web Browsing（GWFD-110103，`LKV3G5SAWB01`）。
- **排除 防欺诈**（critical）：RTSP 按官方差异表**不支持头防欺诈**（证据：[头增强功能之间的差异](evidence/business/access-control/头增强功能之间的差异_10706790.md) §头防欺诈行；HTTP/HTTPS 标"支持"，RTSP 标"不支持"）——虽然 ADD HEADEN 命令含 ANTIFRAUD 参数（RTSP 与 HTTP 共用），但 RTSP 场景防欺诈不生效，配置生成不产出 ANTIFRAUD=ENABLE。
- **排除 HTTPS**（warning）：RTSP 不支持 HTTP2.0；HTTPS 需 GWFD-110263（ADD TLSHEADEN）— 见 [HTTPS 头增强 CS](business/business-awareness/access-control/ConfigurationSolution@access-headen-https.md)。
- **仅基于 TCP 的 RTSP**（critical）：UDG 仅支持 TCP（RFC 2326 允许 TCP/UDP，UDG 不支持 UDP）；不支持 RTSP over HTTP。

### UDG 用户面：HTTP 头防欺诈（内嵌分支，[2-00013](task/UDG/20.15.2/2-00013.md)）

走标准配置方法（见 feature task），防欺诈**不独立配置策略对象**——开关内嵌于 ADD HEADEN 的 ANTIFRAUD 参数。差异仅三点：

- **License 双开**（critical）：`LKV3G5HHAS01`（防欺诈）+ `LKV3G5HTHE01`（头增强，强耦合必开）——任一未开则防欺诈不生效。
- **ANTIFRAUD=ENABLE 必配**（critical）：ADD HEADEN 的 ANTIFRAUD=ENABLE 是本分支核心开关（默认 DISABLE）——不配则防欺诈不生效。
- **PREFIXNAME 不可为 HTTP 标准头域名**（critical）：如 host/accept/user-agent 会导致防欺诈失效——UDG 无法识别已有字段，防欺诈失败。
- **可选灰名单模式**：GRAYLIST=ENABLE（只防欺诈不插入头增强字段）——须配合 ANTIFRAUD=ENABLE，单独配无效。
- **执行顺序**：软参 BIT1030 控制防欺诈是否在头增强前执行（0=在头增强中执行/1=在头增强前执行，初始值 0；默认防欺诈→纠正→插入）。

### UDG 用户面：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task），**无特性级变种**。SA-Basic 提供 HTTP/RTSP 报文解析基础 + 协议对应 SA（HTTP→SA-Web Browsing；RTSP→SA-Streaming）。

### 跨特性协同：HTTP/RTSP 协议族共享 + 防欺诈内嵌

- **HTTP/RTSP 共享 ADD HEADEN**：两协议共用同一 HEADEN 对象（配置重叠）——配 HTTP 头增强时 HEADEN 对象已建，RTSP 业务复用同一 HEADEN + 改协议绑定参数（PROTOCOLNAME=rtsp）+ 知名端口（554）。不需为 RTSP 另建 HEADEN。
- **防欺诈内嵌**：防欺诈开关内嵌于 ADD HEADEN 的 ANTIFRAUD 参数（参数级内嵌，非独立对象）——启用防欺诈时**不另建策略对象**，仅 ADD HEADEN 加 ANTIFRAUD=ENABLE + License 双开。防欺诈检测在头增强插入动作**执行前**先执行（软参 BIT1030 控制顺序）。
- **头增强与计费叠加**（双 RULE 模式）：一条 RULE(POLICYTYPE=HEADEN) + 一条 RULE(POLICYTYPE=PCC)，**共用同一 FLOWFILTER**，绑同一 USERPROFILE——activation 演示双 RULE 模式（[2-00010](task/UDG/20.15.2/2-00010.md) activation §表8/§表9）。详见 [策略匹配基础 CS](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md) 多 RULE 共存机制。

## 决策点

### DP-1：协议选择（HTTP vs RTSP）

决定走 HTTP 头增强还是 RTSP 头增强——影响协议绑定 + License + SA 依赖 + 防欺诈支持。

| 选项/场景 | 影响（协议 / License / SA 依赖 / 防欺诈） |
|---|---|
| HTTP | PROTOCOLNAME=http + 端口 80 + `LKV3G5HTHE01` + SA-Web Browsing（`LKV3G5SAWB01`）；**支持防欺诈**（ANTIFRAUD=ENABLE） |
| RTSP | PROTOCOLNAME=rtsp + 端口 554 + `LKV3G5RTHE01` + SA-Streaming（`LKV3G5SAST01`）；**不支持防欺诈**（官方差异表） |
| HTTP+RTSP 共存 | 同一 HEADEN 对象 + 两条 PROTBINDFLOWF（http + rtsp）；两 License 双开；多协议共用（基于 IP 触发时同时影响 HTTP/RTSP/HTTPS） |

### DP-2：防欺诈启用（内嵌分支）

决定是否启用 HTTP 头防欺诈——影响 ADD HEADEN 参数 + License。

| 选项/场景 | 影响（ANTIFRAUD / License / PREFIXNAME） |
|---|---|
| 不启用防欺诈（默认） | ADD HEADEN 的 ANTIFRAUD=DISABLE（默认）；仅头增强 License `LKV3G5HTHE01` |
| 启用防欺诈（[2-00013](task/UDG/20.15.2/2-00013.md)） | ADD HEADEN 的 **ANTIFRAUD=ENABLE**；License 双开 `LKV3G5HHAS01` + `LKV3G5HTHE01`；PREFIXNAME 不可为 HTTP 标准头域名；插入前先检测纠正 |
| 灰名单模式（只防欺诈不插入） | ANTIFRAUD=ENABLE + GRAYLIST=ENABLE；只检测纠正不插入头增强字段；须配合 ANTIFRAUD=ENABLE |

### DP-3：触发方式（HTTP/RTSP 共用）

决定头增强按什么条件触发——影响过滤链走法。

| 选项/场景 | 影响（过滤链走法） |
|---|---|
| 基于 URL（HTTP 主流）| L7FILTER（URL）+ PROTBINDFLOWF（http/rtsp + L7FILTER） |
| 基于特定 IP | FILTER（SVRIP+端口）+ FLTBINDFLOWF（**不配协议**，同时影响 HTTP/RTSP/HTTPS） |
| 基于 HTTP/RTSP 协议 | PROTBINDFLOWF（http/rtsp，无 L7FILTER） |

### DP-4：加密算法（HTTP/RTSP 共用）

决定头增强字段值的加密方式——影响 ADD HEADEN 参数。

| 选项/场景 | 影响（ENCRYALGORI / 联动命令） |
|---|---|
| 不加密（默认） | ENCRYALGORI=NONE |
| AES 加密（安全推荐） | AES128_GCM/AES256_GCM（+PSWDKEY+SET AES） |
| 哈希加密 | SHA256（+PSWDKEY+SALTSW，RANDNUM 可作盐） |
| RSA 加密（仅 HTTP/RTSP，HTTPS 不支持） | RSA-1024/RSA-2048（+ADD RSA* 命令） |

## 约束

- **HTTP头增强 License 前置**（critical）：SET LICENSESWITCH 开启 `LKV3G5HTHE01` — 未开则 HTTP 头增强不生效（[2-00010](task/UDG/20.15.2/2-00010.md) License）。
- **RTSP头增强 License 前置**（critical，RTSP 时）：`LKV3G5RTHE01` — 未开则 RTSP 头增强不生效（[2-00011](task/UDG/20.15.2/2-00011.md) License）。
- **防欺诈 License 双开**（critical，防欺诈时）：`LKV3G5HHAS01`（防欺诈）**且** `LKV3G5HTHE01`（头增强）——任一未开则防欺诈不生效（[2-00013](task/UDG/20.15.2/2-00013.md) License）。
- **SA-Basic + 协议 SA License 前置**（critical）：SA-Basic（`LKV3G5SABS01`）+ HTTP→SA-Web Browsing（`LKV3G5SAWB01`）/ RTSP→SA-Streaming（`LKV3G5SAST01`）— 未开则报文解析失败。
- **POLICYTYPE=HEADEN 触发**（critical）：RULE.POLICYTYPE=HEADEN + POLICYNAME=HEADERENNAME（直接引用，PCC 策略组名称=NULL）— 指错则头增强不触发（[1-00011](task/UDG/20.15.2/1-00011.md) 场景差异）。
- **RTSP 不支持防欺诈**（critical）：官方差异表明确声明 RTSP 头防欺诈"不支持"（证据：[头增强功能之间的差异](evidence/business/access-control/头增强功能之间的差异_10706790.md) §头防欺诈行）——配 ANTIFRAUD=ENABLE 在 RTSP 场景不生效。
- **防欺诈 ANTIFRAUD=ENABLE 必配**（critical，防欺诈时）：ADD HEADEN 的 ANTIFRAUD=ENABLE 是防欺诈核心开关 — 不配则防欺诈不生效（默认 DISABLE）。
- **防欺诈 PREFIXNAME 不可为标准头域名**（critical，防欺诈时）：如 host/accept/user-agent 会导致防欺诈失效 — UDG 无法识别已有字段。
- **仅 HTTP1.x/RTSP1.x，不支持 HTTP2.0/HTTPS**（warning）：HTTPS 需 GWFD-110263（ADD TLSHEADEN）— 见 [HTTPS 头增强 CS](business/business-awareness/access-control/ConfigurationSolution@access-headen-https.md)。
- **基于 IP 触发同时影响 HTTP/RTSP/HTTPS**（warning）：不区分协议，对用户的 HTTP/RTSP/HTTPS 报文都做头增强（设计如此）— 后果：其他协议报文意外被头增强；改用基于 URL 触发可规避。
- **IPv6 分片风险**（warning）：头增强字段过长致报文超 PMTU 将导致 IPv6 业务无法访问；建议 TCP MSS ≤ PMTU - 60B - 头增强字段长度。
- **外置 PCEF 计费误差**（warning）：头增强改变报文长度，外置 PCEF 计费有误差；建议头增强与计费部署在同一网元。
- **规格**（info）：整机 ≤100 头增强动作；头增强仅针对上行报文（计费属性须含上行）。
- **先计费再头增强**（info）：与规则优先级无关，头增强插入信息不计入业务量计费统计。

## 关联

- 上游场景：[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)
- 基础 CS：[策略匹配基础](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md)（共享 backbone + POLICYTYPE=HEADEN 选择）
- 编排特性（feature task，优先）：[2-00010 HTTP头增强](task/UDG/20.15.2/2-00010.md) · [2-00011 RTSP头增强](task/UDG/20.15.2/2-00011.md) · [2-00013 HTTP头防欺诈](task/UDG/20.15.2/2-00013.md) · [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)
- 复用步骤/命令（compound/atom，按需）：[1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00013](task/UDG/20.15.2/1-00013.md) 头增强对象配置 · [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套（可选）· [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00016](task/UDG/20.15.2/1-00016.md) SA 协议识别链 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00291](task/UDG/20.15.2/0-00291.md) ADD HEADEN · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV
- 族内 CS：[HTTPS 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-https.md)（独立 ADD TLSHEADEN，非复用 HEADEN）
- 证据：[激活HTTP头增强](evidence/UDG/20.15.2/激活HTTP头增强_13649828.md) · [激活RTSP头增强](evidence/UDG/20.15.2/激活RTSP头增强_60009655.md) · [激活HTTP头防欺诈](evidence/UDG/20.15.2/激活HTTP头防欺诈_69815661.md) · [头增强功能之间的差异](evidence/business/access-control/头增强功能之间的差异_10706790.md)（HTTP/HTTPS/RTSP 差异权威表）
