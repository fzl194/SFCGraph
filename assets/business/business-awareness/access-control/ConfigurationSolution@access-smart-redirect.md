---
id: ConfigurationSolution@access-smart-redirect
type: ConfigurationSolution
name: 智能重定向
domain: business-awareness
scenario: access-control
status: draft
---

# 智能重定向

> 根据服务器返回错误码（HTTP 4xx/5xx 或 DNS NXDOMAIN）触发重定向/改写：HTTP 智能重定向到第三方 server，DNS 纠错改写响应 IP。属于[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)场景。

## 概览

智能重定向是 SMARTREDIRECT 子轨的另一类应用（区别于用户Portal 的 IPFarm 重定向）。两个核心特性**共享动作链 compound** [1-00015](task/UDG/20.15.2/1-00015.md)（扩展过滤器+错误码+动作命令），但改写层不同：

- **HTTP 智能重定向**（[110284](task/UDG/20.15.2/2-00017.md)）：HTTP 服务器返回错误码（>400）触发，`ADD SMARTHTTPREDIR` 绑扩展过滤器+错误码+携带信息→SERVERURL，**HTTP 层 URL 重定向**到第三方 server。依赖 SA-Basic + SA-Web Browsing。
- **DNS 纠错**（[110283](task/UDG/20.15.2/2-00016.md)）：DNS 响应错误码（=3 NXDOMAIN）触发，`ADD DNSOVERWRITING` 绑扩展过滤器+错误码→SERVERIP1，**DNS 层响应 IP 改写**为第三方 Platform IP。依赖 PCC 基本功能（DNS 层，无 SA 依赖）。

核心机制：RULE 经 `POLICYTYPE=SMARTREDIRECT` 直接引用动作对象（SMTHTTPREDINAME / DNSOVERWRTNAME），独立于 PCC/HEADEN 子轨，不经 PCCPOLICYGRP、**不经 IPFarm**（SERVERURL/SERVERIP1 在动作命令直配）。与 [用户Portal CS](business/business-awareness/access-control/ConfigurationSolution@access-portal.md) 都用 SMARTREDIRECT 但机制不同（**动作链 vs IPFarm**）。

## 配置与协同

本方案编排 **3 个特性**（二选一/组合核心）：[HTTP智能重定向 110284](task/UDG/20.15.2/2-00017.md) + [DNS纠错 110283](task/UDG/20.15.2/2-00016.md)（二选一或组合）+ 共享依赖前提。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯 feature task 依赖声明 + [1-00015](task/UDG/20.15.2/1-00015.md) 场景差异）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [HTTP智能重定向 110284](task/UDG/20.15.2/2-00017.md)（GWFD-110284） | 核心（HTTP 重定向） | 二选一/组合 | POLICYTYPE=SMARTREDIRECT + SMARTHTTPREDIR（错误码触发 HTTP 层 URL 重定向）；**共享动作链**与 DNS 纠错（同 compound [1-00015](task/UDG/20.15.2/1-00015.md)）。改写层=HTTP URL（对比 DNS 纠错=DNS IP） |
| [DNS纠错 110283](task/UDG/20.15.2/2-00016.md)（GWFD-110283） | 核心（DNS 重定向） | 二选一/组合 | POLICYTYPE=SMARTREDIRECT + DNSOVERWRITING（错误码触发 DNS 层响应 IP 改写）；**共享动作链**与 HTTP 智能重定向（同 compound [1-00015](task/UDG/20.15.2/1-00015.md)）。改写层=DNS IP（对比 HTTP 智能重定向=HTTP URL） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md)（GWFD-110101） | 基础（依赖前提） | 必配（HTTP智能重定向时） | HTTP 智能重定向需 SA-Basic + SA-Web Browsing（HTTP/WAP2.0 解析）；**DNS 纠错不需要 SA**（DNS 层）。配置**不与核心重叠** |
| [PCC基本功能](task/UDG/20.15.2/2-00018.md)（GWFD-020351） | 基础（依赖前提） | 必配（DNS纠错时） | DNS 纠错 activation 明示"完成激活 PCC 基本功能"——DNS 纠错建立在 PCC 之上。配置**不与核心重叠**（PCC 提供 backbone，DNS 纠错配动作对象） |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加；④**跨网元对端**=另一网元对应特性；⑤**二选一**=互斥路径选其一。
>
> **HTTP智能重定向与DNS纠错的关系**：两者**共享动作链 compound** [1-00015](task/UDG/20.15.2/1-00015.md)（扩展过滤器+错误码前置），同属 SMARTREDIRECT 体系，但**改写层不同**（HTTP URL vs DNS IP）+**错误码不同**（GT 400 vs EQUAL 3）+**携带信息不同**（HTTP 可携带 REQURL/IMSI，DNS 不携带）。两者可组合部署（同一用户同时配 HTTP 智能重定向 RULE + DNS 纠错 RULE）。
>
> **与用户Portal CS 的关系**：两者 POLICYTYPE 都=SMARTREDIRECT，但机制不同——本 CS 用**动作链**（SMARTHTTPREDIR/DNSOVERWRITING，**不用 IPFarm**），Portal 用**IPFarm**（POLICYNAME=IPFARMNAME）。RULE.POLICYNAME 指向不同对象。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 用户面：HTTP智能重定向（[2-00017](task/UDG/20.15.2/2-00017.md)）

走标准配置方法（见 feature task），**无特性级变种**（本 CS 即该特性的标准应用场景）。activation 演示 SMF 下发预定义规则 + URL(www.huawei.com/*)+USERAGENT(Mozilla/*) 组合 + 错误码 GT 400 + 携带 REQURL+IMSI + 重定向 www.example.com 的标准场景。

### UDG 用户面：DNS纠错（[2-00016](task/UDG/20.15.2/2-00016.md)）

走标准配置方法（见 feature task），**无特性级变种**（本 CS 即该特性的标准应用场景）。activation 演示 PCRF 下发预定义规则 + UDP 端口 53 + URL(www.example.com/*) + 错误码 EQUAL 3 + SERVERIP1(192.168.1.1) 的标准场景。

### 跨特性协同：共享动作链 + 改写层差异

- **共享动作链**：HTTP 智能重定向与 DNS 纠错共用 compound [1-00015](task/UDG/20.15.2/1-00015.md)——ADD EXTENDEDFILTER（扩展过滤器，[0-00022](task/UDG/20.15.2/0-00022.md)）+ ADD ERRORCODE（错误码，[0-00089](task/UDG/20.15.2/0-00089.md)）两前置命令共享。
- **关键差异**（[1-00015](task/UDG/20.15.2/1-00015.md) 场景差异 §1）：①动作命令（SMARTHTTPREDIR→SERVERURL vs DNSOVERWRITING→SERVERIP1）；②错误码（GT 400 vs EQUAL 3）；③携带信息（HTTP 用 REDIRAPPENDINFO，DNS 不配）；④触发匹配（HTTP 用 L34 ANY，DNS 用 L34 UDP 端口 53）；⑤前置依赖（HTTP 需 SA-Basic+SA-Web，DNS 需 PCC 基本功能）。
- **组合部署**：同一用户可同时配 HTTP 智能重定向 RULE + DNS 纠错 RULE（两条 SMARTREDIRECT RULE 绑同一 USERPROFILE，分别处理 HTTP/DNS 流量）。

## 决策点

### DP-1：重定向机制选择（选 CS）

| 选项/场景 | 影响（POLICYTYPE / 机制 / 承载 CS） |
|---|---|
| HTTP 错误码重定向（4xx/5xx→第三方 server）| POLICYTYPE=SMARTREDIRECT + SMARTHTTPREDIR（动作链，**不用 IPFarm**）；本 CS（HTTP 智能重定向） |
| DNS 纠错（NXDOMAIN→改写响应 IP）| POLICYTYPE=SMARTREDIRECT + DNSOVERWRITING（动作链，**不用 IPFarm**）；本 CS（DNS 纠错） |
| Captive Portal（IPFarm L7 URL 重定向）| POLICYTYPE=SMARTREDIRECT + IPFarm（**用 IPFarm**）；→ [用户Portal CS](business/business-awareness/access-control/ConfigurationSolution@access-portal.md) |
| Web 代理（IPFarm L3 IP NAT）| POLICYTYPE=WEBPROXY + IPFarm；→ [WebProxy CS](business/business-awareness/access-control/ConfigurationSolution@access-webproxy.md) |

### DP-2：改写层选择（HTTP 智能重定向 vs DNS 纠错）

| 选项/场景 | 影响（动作命令 / 错误码 / 携带信息 / 依赖） |
|---|---|
| HTTP 智能重定向 | ADD SMARTHTTPREDIR→SERVERURL；ERRORCODEOP=GT,START=400；ADD REDIRAPPENDINFO（REQURL+IMSI）；依赖 SA-Basic+SA-Web |
| DNS 纠错 | ADD DNSOVERWRITING→SERVERIP1；ERRORCODEOP=EQUAL,START=3；无 REDIRAPPENDINFO；依赖 PCC 基本功能 |
| 两者组合 | 两条 SMARTREDIRECT RULE（各自动作对象），绑同一 USERPROFILE |

### DP-3：智能重定向部署维度（特性级，详见 [2-00017](task/UDG/20.15.2/2-00017.md) / [2-00016](task/UDG/20.15.2/2-00016.md) 决策点）

| 维度 | 选项 | 影响 |
|---|---|---|
| 触发匹配 | URL / URL+USERAGENT（HTTP）/ URL（DNS）| 扩展过滤器组合（EXTFLTTYPE AND/OR/NOT，[1-00015](task/UDG/20.15.2/1-00015.md) 场景差异 §3） |
| 错误码操作 | GT/EQUAL（默认）/ GE/LE/LT | ADD ERRORCODE（[1-00015](task/UDG/20.15.2/1-00015.md) 场景差异 §2） |
| 携带信息（仅 HTTP） | REQURL+IMSI / +MSISDN+IMEI+MSIP（+加密）| ADD REDIRAPPENDINFO（[0-00023](task/UDG/20.15.2/0-00023.md)） |
| 规则下发 | PCRF/SMF 下发预定义（activation）/ 本地 USERPROFILE+RULEBINDING | [1-00011](task/UDG/20.15.2/1-00011.md) |

## 约束

- **HTTP智能重定向 License 前置**（critical）：开启 `LKV3G5SHPR01`（GWFD-110284）— 未开则 HTTP 智能重定向不生效（License 编号交叉验证自 [2-00017](task/UDG/20.15.2/2-00017.md) 约束段，非推断）。
- **DNS纠错 License 前置**（critical）：开启 `LKV3G5DNSO01`（GWFD-110283）— 未开则 DNS 纠错不生效（License 编号交叉验证自 [2-00016](task/UDG/20.15.2/2-00016.md) 约束段，非推断）。
- **SA-Basic License 前置**（critical，HTTP智能重定向时）：开启 `LKV3G5SABS01` + SA-Web Browsing `LKV3G5SAWB01` — HTTP 解析必需（交叉验证自 [2-00019](task/UDG/20.15.2/2-00019.md) + [2-00017](task/UDG/20.15.2/2-00017.md)）。
- **PCC基本功能 License 前置**（critical，DNS纠错时）：开启 `LKV3G5PCCB01`（GWFD-020351）— DNS 纠错 activation 明示依赖 PCC 基本功能（交叉验证自 [2-00018](task/UDG/20.15.2/2-00018.md) + [2-00016](task/UDG/20.15.2/2-00016.md)）。
- **POLICYTYPE=SMARTREDIRECT 触发条件**（critical）：RULE.POLICYTYPE=SMARTREDIRECT + POLICYNAME=动作对象名（SMTHTTPREDINAME / DNSOVERWRTNAME，非 PCCPOLICYGRPNM、非 IPFARMNAME）— 指错则智能重定向不触发。
- **动作对象须先于 RULE 配置**（critical）：SMTHTTPREDINAME / DNSOVERWRTNAME 须先于 `RULE(POLICYTYPE=SMARTREDIRECT)` 配置 — 否则 RULE 引用失败。
- **EXTFLTNAME/BINDERRCODENAME 引用须已配置**（critical）：动作命令的扩展过滤器+错误码须先配（[0-00022](task/UDG/20.15.2/0-00022.md) / [0-00089](task/UDG/20.15.2/0-00089.md)）。
- **仅 HTTP，不支持 HTTPS/HTTP2.0**（warning，HTTP智能重定向）：HTTPS 需其他特性；HTTP2.0 不支持。
- **L34 用 UDP 端口 53 匹配 DNS 流量**（warning，DNS纠错）：ADD FILTER 用 L34PROTOCOL=UDP + SVRSTARTPORT/SVRENDPORT=53 — 用错协议/端口则 DNS 流量匹配失效。
- **规格差异**（warning）：SMARTHTTPREDIR 整机 ≤50（明显小于 DNSOVERWRITING ≤2000 / REDIRAPPENDINFO ≤1000）。

## 关联

- 上游场景：[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)
- 编排特性（feature task，优先）：[2-00017 HTTP智能重定向](task/UDG/20.15.2/2-00017.md) · [2-00016 DNS纠错](task/UDG/20.15.2/2-00016.md) · [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)（HTTP 时）· [2-00018 PCC基本功能](task/UDG/20.15.2/2-00018.md)（DNS 时）
- 复用步骤/命令（compound/atom，按需）：[1-00015](task/UDG/20.15.2/1-00015.md) 智能重定向动作链（HTTP+DNS 共享）· [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [0-00023](task/UDG/20.15.2/0-00023.md) REDIRAPPENDINFO（仅 HTTP）· [0-00027](task/UDG/20.15.2/0-00027.md) SIGNATUREDB（DNS 可选）· [0-00294](task/UDG/20.15.2/0-00294.md) FLOWFILTERGRP（可选）
- 基础 CS：[策略匹配基础](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md)（backbone + POLICYTYPE 6 子轨）
- 同族 CS：[用户Portal](business/business-awareness/access-control/ConfigurationSolution@access-portal.md)（同 SMARTREDIRECT 但用 IPFarm）· [WebProxy](business/business-awareness/access-control/ConfigurationSolution@access-webproxy.md)（用 IPFarm，POLICYTYPE=WEBPROXY）
- 证据：[激活HTTP智能重定向](evidence/business/access-control/激活HTTP智能重定向_67075035.md)（HTTP 智能重定向主源）· [激活DNS纠错](evidence/business/access-control/激活DNS纠错_67964199.md)（DNS 纠错主源）
