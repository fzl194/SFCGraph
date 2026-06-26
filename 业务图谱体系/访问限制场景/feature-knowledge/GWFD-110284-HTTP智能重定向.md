# GWFD-110284 HTTP智能重定向 知识文档

> 访问限制场景 重定向族核心特性 | UDG | 来源：特性概述 + 实现原理 + 激活 + 调测 + 参考信息 | 2026-06-22

---

## 0. 元数据（三层图谱Schema §9.3 对齐）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110284 |
| feature_name | HTTP智能重定向 |
| feature_group | 重定向 |
| parent_feature_id | GWFD-110101 SA-Basic（HTTP 解析依赖父节点） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["重定向方式(HTTP响应改写/302 Location)", "目标类型(第三方服务器URL)", "触发条件(URL过滤 / user-agent / content-type / url-postfix / error-code范围)", "扩展过滤器组合(AND逻辑多条件)", "重定向携带信息(REQURLFLAG/IMSIFLAG/MSISDNFLAG/IMEIFLAG/IPFLAG)", "规则承载方式(预定义规则 / SMF动态下发)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-06, EV-FK-AC-07, EV-FK-AC-08, EV-FK-AC-09, EV-FK-AC-10] |
| license_required | 82209783 LKV3G5SHPR01 HTTP智能重定向（必须获得 License 许可） |

---

## 1. 概述

### 1.1 特性定义（是什么）

HTTP 智能重定向功能是指：**UDG 通过修改 HTTP 响应报文，将匹配到 HTTP 智能重定向规则的访问重定向到第三方服务器**。

工作机制：MS/UE 发起 HTTP 请求，HTTP 服务器返回失败响应（携带 error code、content type），UDG 解析响应报文，若错误码、content type、URL、user-agent、url-postfix 等与配置匹配，则 UDG 构造重定向报文（含第三方服务器 URL）发送给 MS/UE，重定向 URL 可携带初始请求 URL、MSISDN、IMEI、IMSI、用户 IP 等信息。

> 隐私声明：HTTP 智能重定向在 HTTP 报文头扩展字段插入特定用户标识（IMSI/MSISDN/IP 地址），存在将用户个人身份信息泄露的风险。请遵循当地法律允许的目的和范围内启用相应功能，以确保符合当地通信自由与个人隐私保护相关的法律要求。

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（定义）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 对 HTTP 报文进行识别和解析，根据解析结果匹配规则，修改 HTTP 响应报文，将匹配到 HTTP 智能重定向规则的访问重定向到第三方服务器 |

> 说明：本特性仅在用户面（UDG）执行，不涉及 UNC 与 PCF 的策略下发；规则可由 SMF 通过 PFCP 下发，也可 UDG 本地预定义。
> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（可获得性）

### 1.3 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 将用户吸引到门户网站，使用运营商提供的定制化服务；对用户错误输入的 URL 进行纠错，提高网站访问准确率，提升用户满意度；通过对错误码、URL、content type、user agent、URL 后缀名等条件组合过滤，实现 HTTP 智能重定向 |
| 用户 | 对用户错误输入的 URL 进行纠错，提高网站访问的准确率，提升用户的上网体验 |

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（客户价值）

### 1.4 应用场景（6类触发条件）

| # | 场景 | 触发条件 |
|---|------|---------|
| 1 | URL 错误重定向 | 用户请求的初始 URL 不正确或不存在时，UDG 将用户重定向到正确的 URL 或第三方服务器 |
| 2 | URL 过滤重定向 | 配置 URL 过滤条件，匹配后 UDG 将用户重定向到第三方服务器 |
| 3 | 内容类型过滤重定向 | 配置特定 HTTP 访问内容的类型（content-type）过滤条件，匹配后重定向 |
| 4 | URL 后缀过滤重定向 | 配置 URL 后缀名（扩展名）的页面类型（url-postfix）过滤条件，匹配后重定向 |
| 5 | 终端类型过滤重定向 | 配置终端使用的浏览器类型（user agent）过滤条件，匹配后重定向 |
| 6 | 错误码自动重定向 | **当 UDG 本地未配置上述过滤条件时**，如果 HTTP 业务响应码在 400-1000 范围内，系统也会执行 HTTP 智能重定向动作 |

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（应用场景）

### 1.5 License

- **License 控制项**：`82209783 LKV3G5SHPR01 HTTP智能重定向`
- **必须获得 License 许可后才能使用**该特性服务
- 软参 BIT1481 可控制"在没有 HTTP 或 DNS 错码重定向 License 的场景下，是否可以做重定向的基本功能"

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（License 支持）、`GWFD-110284 HTTP智能重定向参考信息_93168884.md`（软参 BIT1481）

### 1.6 前置条件与依赖

| 依赖类型 | 相关特性 / 控制项 | 说明 |
|---------|-----------------|------|
| 依赖 | GWFD-110101 SA-Basic（82209749 SA-Basic） | UDG 需要对 HTTP 报文进行解析和规则匹配，使用本特性前需启用 SA-Basic |
| 依赖 | GWFD-110103 SA-Web Browsing（82209765 SA-Network Administration） | HTTP 解析依赖 SA-Web Browsing |
| 互斥 | GWFD-110201 HTTP2.0 Host 识别（82209773） | HTTP2.0 为加密报文，不支持 HTTP 重定向处理 |
| 互斥 | GWFD-110203 HTTPS 业务地址识别（82209775） | HTTPS 为加密报文，UDG 无法准确获取特征信息，不支持 HTTP 重定向 |
| 数据前置 | 重定向的第三方服务器与 UDG 的互通配置已完成；重定向设备已安装第三方抓包工具 | 调测前置 |

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（与其他特性的交互）、`调测HTTP智能重定向_67075036.md`（必备事项）

### 1.7 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | 20.0.0 | 首次发布 |

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（发布历史）

### 1.8 特性规格

产品文档声明"本特性无应用限制"（指无独立规格限制），但实际受以下应用限制约束（见 1.10）。

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（特性规格）

### 1.9 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| IETF | 2616 | Hypertext Transfer Protocol -- HTTP/1.1 |

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（遵循标准）

### 1.10 应用限制（关键）

1. **协议限制**：本特性**只支持 HTTP 1.x 协议，不支持 HTTP 2.0 协议**
2. **HTTPS 不支持**：由于 UDG 无法准确获取 HTTPS 协议报文的特征信息，本特性**不支持对 HTTPS 协议报文的处理**
3. **加密场景限制**：不支持加密场景基于 host 的计费和控制

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（应用限制）

### 1.11 对系统的影响

当在 UDG 上开启 HTTP 智能重定向特性后，由于需要对 URL 进行缓存、对匹配到规则的 HTTP 报文进行业务感知，因此：
- 系统处理负荷将增加
- 报文转发性能和吞吐量将下降

具体下降程度需根据话务模型和实施的业务特性来评估。

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（对系统的影响）

### 1.12 计费与话单

**本特性不涉及计费与话单**。

> 来源：`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（计费与话单）

---

## 2. 原理（深度：HTTP 302 报文构造 + 扩展过滤器组合 + PCC 轨道关系）

### 2.1 重定向报文构造机制（HTTP 302 改写）

HTTP 智能重定向不依赖 302 状态码的 HTTP 服务器响应，而是 **UDG 主动构造重定向响应报文**。机制如下：

```
┌──────────────────────────────────────────────────────────────┐
│ HTTP 智能重定向报文构造流程                                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  [阶段1：请求到达与规则匹配]                                     │
│   MS/UE → UDG：HTTP Get Request                              │
│     携带：初始访问 URL                                          │
│   UDG 七层解析与规则匹配：                                       │
│     条件1：业务流为 HTTP 协议                                    │
│     条件2：方法为 GET                                           │
│     条件3：匹配 EXTENDEDFILTER（URL/user-agent/content-type/   │
│             url-postfix/error-code 组合）                       │
│   全部满足 → UDG 缓存 MS/UE 的初始请求 URL                       │
│                                                              │
│  [阶段2：向真实服务器转发请求]                                    │
│   UDG → HTTP Server：HTTP Get Request（原样转发）              │
│   HTTP Server → UDG：HTTP 失败响应                              │
│     携带：error code（如 404）、content type                    │
│                                                              │
│  [阶段3：UDG 响应解析与重定向决策]                                │
│   UDG 解析 HTTP 响应报文：                                       │
│     - 错误码（对照 ADD ERRORCODE 范围，如 ERRORCODEOP=GT,        │
│              ERRORCODESTART=400 表示 > 400 触发）                │
│     - content type、URL、user-agent、url-postfix                │
│   全部匹配 → 构造重定向报文                                       │
│                                                              │
│  [阶段4：重定向报文发送]                                          │
│   UDG → MS/UE：HTTP Response（重定向报文）                      │
│     必含：第三方服务器 URL（SERVERURL，如 www.example.com）       │
│     可选携带（由 ADD REDIRAPPENDINFO 控制）：                    │
│       - 初始请求 URL（REQURLFLAG=ENABLE）                       │
│       - MSISDN（MSISDNFLAG=ENABLE）                            │
│       - IMEI（IMEIFLAG=ENABLE）                                │
│       - IMSI（IMSIFLAG=ENABLE）                                │
│       - 用户 IP（IPFLAG=ENABLE）                                │
│   重定向 URL 最大长度由 SET SRVCOMMONPARA.URLREDLEN 控制         │
│   （取值 255~1400，默认 511）                                    │
│                                                              │
│  [阶段5：终端跳转]                                               │
│   MS/UE → 第三方服务器：HTTP Get Request                        │
│     携带：第三方服务器 URL + 初始请求 URL + MSISDN/IMEI/IMSI/IP  │
│   第三方服务器 → MS/UE：成功响应                                  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

> 说明：当存在某些服务器无法解析重定向 URL 总长度超过一定规格的重定向报文的情况下，可通过 `SET SRVCOMMONPARA` 命令的 `URLREDLEN` 参数配置重定向 URL 的最大长度，取值范围 255~1400，默认值 511。
> 来源：`实现原理_73611724.md`（业务流程第 1~7 步）

### 2.2 扩展过滤器组合机制（AND 逻辑）

UDG 通过 `ADD EXTENDEDFILTER` 配置独立的扩展过滤器，每个扩展过滤器承载一种触发条件。`ADD SMARTHTTPREDIR` 通过 `EXTFLTTYPE1/2/...` + `EXTFLTNAME1/2/...` 将多个扩展过滤器以 AND 逻辑组合：

| 扩展过滤器承载的条件类型 | EXTENDEDFILTER 参数 | 说明 |
|-------------------------|--------------------|------|
| URL 匹配 | URL | 如 `www.huawei.com/*` |
| 客户端浏览器类型 | USERAGENT | 如 `Mozilla/*` |
| HTTP 内容类型 | CONTENTTYPE | content-type 过滤 |
| URL 后缀/扩展名 | URLPOSTFIX | 页面类型过滤 |
| 错误码 | ERRORCODE（由 ADD ERRORCODE 定义） | 错误码范围，操作码 GT/LT/EQ |

**组合规则**：`ADD SMARTHTTPREDIR` 中 `EXTFLTTYPE=AND` 表示该扩展过滤器与其他以 AND 组合的过滤器同时满足才触发重定向。最多可绑定多个扩展过滤器。

> 来源：`激活HTTP智能重定向_67075035.md`（数据表 ADD EXTENDEDFILTER / ADD SMARTHTTPREDIR 参数说明）

### 2.3 SMARTREDIRECT 策略类型与 PCC 体系的关系（澄清）

**重要说明**：HTTP 智能重定向虽然属于访问限制场景的"轨道 A（PCC 体系）"特性大类，但其**规则承载方式与典型 PCC 特性（如 ADC、头增强）不同**：

| 维度 | 典型 PCC 特性（ADC/头增强） | HTTP 智能重定向 |
|------|---------------------------|----------------|
| RULE.POLICYTYPE | ADC / PCC / HEADEN | **SMARTREDIRECT**（与 DNS 纠错共用） |
| 动作承载对象 | PCCPOLICYGRP（→ PCCACTIONPROP） | **SMARTHTTPREDIR**（直接定义 SERVERURL、扩展过滤器、携带信息） |
| 动作触发位置 | PCRF/PCF 下发携带动作的 PCC 规则 | UDG 本地预定义或 SMF 下发规则名 |
| POLICYNAME 指向 | PCCPOLICYGRP（URRGROUP/动作组） | SMARTHTTPREDIR 对象（含 SERVERURL） |

**结论**：HTTP 智能重定向**不走 PCCPOLICYGRP/PCCACTIONPROP/REDIRECT 的典型 PCC 轨道 A 路径**，而是采用独立的 `POLICYTYPE=SMARTREDIRECT` 路径，通过 `ADD SMARTHTTPREDIR` 直接定义重定向动作。这与本特性任务描述中"PCCACTIONPROP 引用 REDIRECT"的说法不同——本特性是 SMARTREDIRECT 独立体系，POLICYNAME 引用 SMARTHTTPREDIR 对象。

> 来源：`激活HTTP智能重定向_67075035.md`（数据表 ADD RULE: POLICYTYPE=SMARTREDIRECT, POLICYNAME=http-redirect_test）；与 cross-feature-analysis.md §3.1 "POLICYTYPE 分类表"印证

### 2.4 触发条件矩阵

| 触发场景 | URL | user-agent | content-type | url-postfix | error-code | 触发结果 |
|---------|-----|-----------|--------------|-------------|-----------|---------|
| 场景1：URL 错误（未配置扩展过滤器） | — | — | — | — | 在 400-1000 范围 | 自动重定向（UDG 兜底） |
| 场景2：URL 过滤 | 配置 | — | — | — | 可选配置 | 匹配 URL 触发 |
| 场景3：URL+UA 组合（典型示例） | www.huawei.com/* | Mozilla/* | — | — | > 400 | AND 全满足触发 |
| 场景4：内容类型过滤 | — | — | 配置 | — | 可选配置 | 匹配 content-type 触发 |
| 场景5：URL 后缀过滤 | — | — | — | 配置 | 可选配置 | 匹配 url-postfix 触发 |
| 场景6：终端类型过滤 | — | 配置 | — | — | 可选配置 | 匹配 user-agent 触发 |

### 2.5 协议交互

| 接口 | 交互网元 | 关键信元 | 用途 |
|------|---------|---------|------|
| N4（5G）/ Sxa（4G） | SMF → PGW-U/UPF | PFCP Session Modification Request（携带 HTTP 智能重定向规则名） | SMF 下发动态规则（可选） |
| Gi/SGi/N6 | PGW-U/UPF ↔ HTTP Server | HTTP Get Request / HTTP Response | 业务报文转发与响应解析 |
| Gi/SGi/N6 | PGW-U/UPF ↔ 第三方服务器 | HTTP Get Request（含 SERVERURL + 初始URL + MSISDN/IMSI 等） | 终端跳转到第三方服务器 |
| Gi/SGi/N6（接入侧） | PGW-U/UPF ↔ MS/UE | HTTP Response（重定向报文） | UDG 构造并发送重定向响应 |

> 来源：综合 `实现原理_73611724.md`、`GWFD-110284 HTTP智能重定向特性概述_67329006.md`（原理概述）

---

## 3. 配置对象体系

### 3.1 配置对象层级

```
┌──────────────────────────────────────────────────────────────┐
│ HTTP 智能重定向配置对象体系                                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  [三四层过滤层]                                                │
│   FILTER ──→ FLTBINDFLOWF ──→ FLOWFILTER                    │
│                                    │                         │
│  [扩展过滤层]                       │                         │
│   EXTENDEDFILTER (URL/UA/         │                         │
│    content-type/url-postfix) ─────┤                         │
│        ↑                          │                         │
│        │ (EXTFLTTYPE=AND 引用)     │                         │
│  [错误码层]                       │                         │
│   ERRORCODE (范围+操作码) ─────────┤                         │
│                                    ▼                         │
│  [携带信息层]              [动作策略层]                        │
│   REDIRAPPENDINFO  ────→  SMARTHTTPREDIR                     │
│   (REQURLFLAG/             (SMTHTTPREDINAME,                  │
│    IMSIFLAG/                SERVERURL,                        │
│    MSISDNFLAG/              EXTFLTTYPE1/2 + EXTFLTNAME1/2,   │
│    IMEIFLAG/                APPENDINFONAME,                   │
│    IPFLAG)                  BINDERRCODENAME)                 │
│                                    │                         │
│                                    ▼                         │
│  [规则层]                                                    │
│   RULE (RULENAME,                                             │
│         POLICYTYPE=SMARTREDIRECT,                             │
│         FILTERINGMODE=FLOWFILTER,                             │
│         FLOWFILTERNAME=flow-filter1,                          │
│         PRIORITY,                                             │
│         POLICYNAME=http-redirect_test)                        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 关键配置对象

| 对象类型 | 对象名称（示例） | 用途 |
|----------|-----------------|------|
| FILTER | f-any | 三四层过滤条件 |
| FLOWFILTER | flow-filter1 | 流过滤器 |
| EXTENDEDFILTER | filter_http-redirect1 / filter_http-redirect2 | 扩展过滤器（URL、user agent、content-type、url-postfix 各自独立配置） |
| ERRORCODE | httperrorcode | 错误码范围（操作码 + 起始值） |
| REDIRAPPENDINFO | testredirappendinfo | 重定向携带信息（REQURLFLAG/IMSIFLAG/MSISDNFLAG/IMEIFLAG/IPFLAG） |
| SMARTHTTPREDIR | http-redirect_test | HTTP 智能重定向动作策略（绑定 SERVERURL + 扩展过滤器 + 携带信息 + 错误码） |
| RULE | rule_test | 业务规则（POLICYTYPE=SMARTREDIRECT，POLICYNAME 指向 SMARTHTTPREDIR） |

### 3.3 关键参数说明

#### 3.3.1 ADD EXTENDEDFILTER 参数

| 参数 | 取值 | 说明 |
|------|------|------|
| EXTFLTNAME | filter_http-redirect1 | 扩展过滤器名称，本端规划 |
| URL | www.huawei.com/* | 匹配的 URL |
| USERAGENT | Mozilla/* | 客户端浏览器类型 |
| CONTENTTYPE | （具体 content-type） | HTTP 内容类型 |
| URLPOSTFIX | （具体后缀） | URL 后缀/扩展名 |

> 说明：每个 EXTENDEDFILTER 承载一种条件，重复执行 ADD EXTENDEDFILTER 可增加多个不同过滤条件的扩展过滤器。

#### 3.3.2 ADD ERRORCODE 参数

| 参数 | 取值 | 说明 |
|------|------|------|
| ERRORCODENAME | httperrorcode | 错误码名称，全网规划 |
| ERRORCODEOP | GT / LT / EQ | 错误码范围操作码 |
| ERRORCODESTART | 400 | 错误码范围起始值 |

#### 3.3.3 ADD REDIRAPPENDINFO 参数

| 参数 | 取值 | 说明 |
|------|------|------|
| APPENDINFONAME | testredirappendinfo | 重定向携带信息名称 |
| REQURLFLAG | ENABLE / DISABLE | 请求 URL 标识，ENABLE 时携带用户原始请求 URL |
| IMSIFLAG | ENABLE / DISABLE | IMSI 携带标识 |
| MSISDNFLAG | ENABLE / DISABLE | MSISDN 携带标识（Stage 4 补充具体取值，参见命令参考） |
| IMEIFLAG | ENABLE / DISABLE | IMEI 携带标识 |
| IPFLAG | ENABLE / DISABLE | 用户 IP 携带标识 |

#### 3.3.4 ADD SMARTHTTPREDIR 参数

| 参数 | 取值 | 说明 |
|------|------|------|
| SMTHTTPREDINAME | http-redirect_test | HTTP 智能重定向名称 |
| SERVERURL | www.example.com | 服务器 URL（重定向目标） |
| EXTFLTTYPE1 / EXTFLTTYPE2 | AND | 扩展过滤器类型，AND 表示与下一过滤器同时满足 |
| EXTFLTNAME1 / EXTFLTNAME2 | filter_http-redirect1/2 | 扩展过滤器名称，已通过 ADD EXTENDEDFILTER 配置 |
| APPENDINFONAME | testredirappendinfo | 重定向携带信息名称，已通过 ADD REDIRAPPENDINFO 配置 |
| BINDERRCODENAME | httperrorcode | 绑定错误码名称，已通过 ADD ERRORCODE 配置 |

#### 3.3.5 ADD RULE 参数

| 参数 | 取值 | 说明 |
|------|------|------|
| RULENAME | rule_test | 规则名称 |
| POLICYTYPE | SMARTREDIRECT | **策略类型固定为 SMARTREDIRECT**（与 DNS 纠错共用） |
| FILTERINGMODE | FLOWFILTER / FLOWFILTERGRP | 流过滤器或流过滤器组选择；基于流过滤器组时需 ADD FLOWFILTERGRP |
| FLOWFILTERNAME | flow-filter1 | 流过滤器名称 |
| PRIORITY | 1（示例） | 全局优先级 |
| POLICYNAME | http-redirect_test | 业务策略绑定的 HTTP 智能重定向名称（指向 SMARTHTTPREDIR 对象） |

### 3.4 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| 协议限制 | 只支持 HTTP 1.x；不支持 HTTP 2.0；不支持 HTTPS |
| 加密场景限制 | 不支持加密场景基于 host 的计费和控制 |
| 互斥特性 | 与 GWFD-110201 HTTP2.0 Host 识别、GWFD-110203 HTTPS 业务地址识别互斥 |
| SMARTREDIRECT 共用 | POLICYTYPE=SMARTREDIRECT 同时被 HTTP 智能重定向（110284）和 DNS 纠错（110283）共用，区分点在 POLICYNAME 指向的对象类型 |
| URL 长度限制 | 重定向 URL 最大长度由 SET SRVCOMMONPARA.URLREDLEN 控制（255~1400，默认 511） |
| 隐私合规 | 在 HTTP 报文头插入 IMSI/MSISDN/IP 等用户标识，需遵循当地隐私保护法律 |

> 来源：综合 `GWFD-110284 HTTP智能重定向特性概述_67329006.md`、`激活HTTP智能重定向_67075035.md`、cross-feature-analysis.md §3.1

---

## 4. 配置流程

### 4.1 通用激活步骤骨架

```
步骤1：打开 License 配置开关
   SET LICENSESWITCH:LICITEM="LKV3G5SHPR01",SWITCH=ENABLE;

步骤2：配置三四层过滤条件
   ADD FILTER → ADD FLOWFILTER → ADD FLTBINDFLOWF → SET REFRESHSRV

步骤3：配置扩展过滤器（可重复执行，增加多个不同过滤条件）
   ADD EXTENDEDFILTER:EXTFLTNAME=...,URL=...;
   ADD EXTENDEDFILTER:EXTFLTNAME=...,USERAGENT=...;
   （可继续添加 CONTENTTYPE / URLPOSTFIX 等条件）

步骤4：配置错误码
   ADD ERRORCODE:ERRORCODENAME=...,ERRORCODEOP=GT,ERRORCODESTART=400;

步骤5：配置重定向动作策略
   ADD REDIRAPPENDINFO:APPENDINFONAME=...,REQURLFLAG=ENABLE,IMSIFLAG=ENABLE;
   ADD SMARTHTTPREDIR:SMTHTTPREDINAME=...,SERVERURL=...,
      EXTFLTTYPE1=AND,EXTFLTNAME1=...,
      EXTFLTTYPE2=AND,EXTFLTNAME2=...,
      APPENDINFONAME=...,BINDERRCODENAME=...;

步骤6：配置业务规则
   ADD RULE:RULENAME=...,POLICYTYPE=SMARTREDIRECT,
      FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME=...,
      PRIORITY=1,POLICYNAME=...;
   （注：基于流过滤器组时 FILTERINGMODE=FLOWFILTERGRP，
        需 ADD FLOWFILTERGRP 配置流过滤器组）
```

> 来源：`激活HTTP智能重定向_67075035.md`（操作步骤）

### 4.2 MML 命令清单（参考信息）

| 命令 | 用途 |
|------|------|
| ADD FILTER | 增加过滤器（三四层） |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FLTBINDFLOWF | 增加流过滤器与过滤器的绑定关系 |
| SET REFRESHSRV | 业务刷新 |
| ADD EXTENDEDFILTER | 增加扩展过滤器（URL/user-agent/content-type/url-postfix） |
| ADD SMARTHTTPREDIR | 新增 HTTP 智能重定向 |
| ADD ERRORCODE | 增加错误码 |
| ADD REDIRAPPENDINFO | 增加重定向携带信息 |
| ADD RULE | 增加规则（POLICYTYPE=SMARTREDIRECT） |

> 来源：`GWFD-110284 HTTP智能重定向参考信息_93168884.md`（命令）

---

## 5. 配置案例（多场景变体）

### 5.1 场景一：URL + user-agent 组合重定向（产品文档典型示例）

**场景描述**：采用 SMF 下发预定义规则方式。对于用户发起的 URL 为 `www.huawei.com/*`、user agent 为 `Mozilla/*` 的 HTTP 请求，当 HTTP 服务器返回的错误码值大于 400 时，UDG 进行 HTTP 智能重定向，重定向后 URL 为 `www.example.com`，并在重定向动作中携带 request-url-name 和 imsi-name。

**MML 命令序列（原样保留产品文档脚本）**：

```
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5SHPR01",SWITCH=ENABLE;

// 配置 HTTP 智能重定向使用的三四层过滤条件。
ADD FILTER:FILTERNAME="f-any",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flow-filter1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-filter1",FILTERNAME="f_any";
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;

// 配置 HTTP 智能重定向使用的扩展过滤器。
ADD EXTENDEDFILTER:EXTFLTNAME="filter_http-redirect1",URL="www.huawei.com/*";
ADD EXTENDEDFILTER:EXTFLTNAME="filter_http-redirect2",USERAGENT="Mozilla/*";

// 配置 HTTP 智能重定向错误码。
ADD ERRORCODE: ERRORCODENAME="httperrorcode", ERRORCODEOP=GT, ERRORCODESTART=400;

// 配置 HTTP 智能重定向动作策略。
ADD REDIRAPPENDINFO:APPENDINFONAME="testredirappendinfo",REQURLFLAG=ENABLE,IMSIFLAG=ENABLE;

ADD SMARTHTTPREDIR:SMTHTTPREDINAME="http-redirect_test", SERVERURL="www.example.com",
  EXTFLTTYPE1=AND, EXTFLTNAME1="filter_http-redirect1",
  EXTFLTTYPE2=AND, EXTFLTNAME2="filter_http-redirect2",
  APPENDINFONAME="testredirappendinfo", BINDERRCODENAME="httperrorcode";

// 配置 HTTP 智能重定向使用的业务规则。
ADD RULE:RULENAME="rule_test",POLICYTYPE=SMARTREDIRECT,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-filter1",
  PRIORITY=1,POLICYNAME="http-redirect_test";
```

> 注意：产品文档原文 `ADD FLTBINDFLOWF` 中 `FILTERNAME="f_any"`（下划线）与 `ADD FILTER` 中 `FILTERNAME="f-any"`（连字符）不一致，疑为笔误。实际部署时应统一为 `f-any` 或 `f_any`，本文档保留产品文档原文，已在 §8 标注。
> 来源：`激活HTTP智能重定向_67075035.md`（任务示例脚本）

### 5.2 场景二：仅 URL 过滤重定向（单条件触发）

**场景描述**：用户访问特定 URL（如未签约业务 `*unauthorized-site*`）时，无论 user-agent 和错误码如何，直接重定向到运营商 Portal 页面 `portal.operator.com`。本场景的 EXTENDEDFILTER 仅配置 URL，不绑定 ERRORCODE。

**MML 命令序列（核心差异部分）**：

```
SET LICENSESWITCH:LICITEM="LKV3G5SHPR01",SWITCH=ENABLE;

// 三四层过滤条件（与场景一相同，省略 FLTBINDFLOWF 等）

// 配置单个 URL 扩展过滤器（不配置 user-agent）。
ADD EXTENDEDFILTER:EXTFLTNAME="filter_url_only",URL="*unauthorized-site*";

// 配置重定向携带信息（仅携带 MSISDN）。
ADD REDIRAPPENDINFO:APPENDINFONAME="redir_msisdn_only",MSISDNFLAG=ENABLE;

// 配置 HTTP 智能重定向（只绑定一个扩展过滤器，不绑定错误码）。
ADD SMARTHTTPREDIR:SMTHTTPREDINAME="http-redir_url",
  SERVERURL="portal.operator.com",
  EXTFLTTYPE1=AND, EXTFLTNAME1="filter_url_only",
  APPENDINFONAME="redir_msisdn_only";

// 配置规则（同场景一）。
ADD RULE:RULENAME="rule_url_redir",POLICYTYPE=SMARTREDIRECT,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-filter1",
  PRIORITY=5,POLICYNAME="http-redir_url";
```

> 说明：本场景为基于产品文档机制的归纳示例，展示单扩展过滤器（仅 URL）+ 无错误码绑定的配置变体。
> 来源：基于 `激活HTTP智能重定向_67075035.md` 机制归纳

### 5.3 场景三：错误码自动重定向（UDG 兜底，无扩展过滤器）

**场景描述**：当 UDG 本地未配置任何扩展过滤器时，若 HTTP 业务响应码在 400-1000 范围内，系统自动执行 HTTP 智能重定向。本场景只需配置 ERRORCODE 和 SMARTHTTPREDIR（不绑定 EXTFLTNAME）。

**MML 命令序列（核心差异部分）**：

```
SET LICENSESWITCH:LICITEM="LKV3G5SHPR01",SWITCH=ENABLE;

// 三四层过滤条件（同场景一）

// 不配置 EXTENDEDFILTER（依赖 UDG 兜底机制）

// 配置错误码范围（400-1000）。
// ERRORCODEOP=GT, ERRORCODESTART=400 表示 > 400 触发；
// 产品文档明确未配置过滤条件时 400-1000 自动触发。
ADD ERRORCODE:ERRORCODENAME="http_err_400_1000",ERRORCODEOP=GT,ERRORCODESTART=400;

ADD REDIRAPPENDINFO:APPENDINFONAME="redir_default",REQURLFLAG=ENABLE;

// 配置 HTTP 智能重定向（不绑定扩展过滤器，仅绑定错误码）。
ADD SMARTHTTPREDIR:SMTHTTPREDINAME="http-redir_autofallback",
  SERVERURL="error.operator.com",
  APPENDINFONAME="redir_default",
  BINDERRCODENAME="http_err_400_1000";

ADD RULE:RULENAME="rule_autofallback",POLICYTYPE=SMARTREDIRECT,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-filter1",
  PRIORITY=10,POLICYNAME="http-redir_autofallback";
```

> 说明：本场景基于产品文档应用场景说明"当 UDG 本地没有配置上述过滤条件时，如果 HTTP 业务响应码在 400-1000 范围内，系统也会执行 HTTP 智能重定向动作"归纳。
> 来源：基于 `GWFD-110284 HTTP智能重定向特性概述_67329006.md`（应用场景说明）归纳

### 5.4 场景四：基于流过滤器组的重定向（多 FLOWFILTER 组合）

**场景描述**：运营商希望基于流过滤器组设置过滤条件（而非单个 FLOWFILTER），例如同时匹配 HTTP 和 WAP 流量。此时 RULE.FILTERINGMODE=FLOWFILTERGRP，需使用 ADD FLOWFILTERGRP 配置流过滤器组。

**MML 命令序列（核心差异部分）**：

```
// 配置两个流过滤器（HTTP 与 WAP）。
ADD FLOWFILTER:FLOWFILTERNAME="flow-http";
ADD FLOWFILTER:FLOWFILTERNAME="flow-wap";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-http",FILTERNAME="f-http";  // 假设 f-http 已配
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-wap",FILTERNAME="f-wap";    // 假设 f-wap 已配

// 配置流过滤器组（聚合 HTTP 与 WAP）。
ADD FLOWFILTERGRP:FLOWFILTERGRPNAME="ffg-http-wap",
  FLOWFILTERNAME1="flow-http",
  FLOWFILTERNAME2="flow-wap";

// 配置规则（FILTERINGMODE=FLOWFILTERGRP）。
ADD RULE:RULENAME="rule_grp",POLICYTYPE=SMARTREDIRECT,
  FILTERINGMODE=FLOWFILTERGRP,FLOWFILTERGRPNAME="ffg-http-wap",
  PRIORITY=1,POLICYNAME="http-redirect_test";
```

> 说明：产品文档明确"如果运营商希望基于流过滤器组设置过滤条件时，配置 FILTERINGMODE 为 FLOWFILTERGRP，并且使用 ADD FLOWFILTERGRP 命令配置流过滤器组"。
> 来源：`激活HTTP智能重定向_67075035.md`（操作步骤6 注释）

### 5.5 场景变体对照表

| 变体 | EXTENDEDFILTER 数量 | 绑定 ERRORCODE | FILTERINGMODE | 携带信息 | 关键差异 |
|------|---------------------|----------------|---------------|---------|---------|
| URL+UA 组合（典型） | 2 个（URL + USERAGENT），AND 组合 | 是（GT 400） | FLOWFILTER | REQURL + IMSI | 多条件 AND 触发；产品文档示例 |
| 仅 URL 过滤 | 1 个（URL） | 否（可选） | FLOWFILTER | MSISDN（示例） | 单条件触发，不依赖错误码 |
| 错误码自动兜底 | 0 个 | 是（GT 400） | FLOWFILTER | REQURL | UDG 兜底机制，无需配置扩展过滤器 |
| 基于流过滤器组 | 视场景 | 视场景 | FLOWFILTERGRP | 视场景 | 多 FLOWFILTER 聚合匹配 |
| content-type 过滤 | 1 个（CONTENTTYPE） | 可选 | FLOWFILTER | 视场景 | 按 HTTP 内容类型触发 |
| url-postfix 过滤 | 1 个（URLPOSTFIX） | 可选 | FLOWFILTER | 视场景 | 按 URL 后缀/扩展名触发 |
| 终端类型过滤 | 1 个（USERAGENT） | 可选 | FLOWFILTER | 视场景 | 按浏览器类型触发 |

---

## 6. 验证与调测

### 6.1 调测前提与目的

运营商部署 HTTP 智能重定向功能后，需要进行调测以保证本功能正常使用。

> 适用：PGW-U、UPF

### 6.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
|------|---------|---------|---------|------|
| 扩展过滤器查询 | 扩展过滤器名字（EXTFLTNAME） | filter_http-redirect1 / filter_http-redirect2 | 已配置数据中获取 | HTTP 智能重定向使用的扩展过滤器 |
| 规则查询 | 规则名称（RULENAME） | rule_test | 已配置数据中获取 | HTTP 智能重定向使用的业务规则 |

工具：测试终端、OM Portal 跟踪工具、第三方抓包工具

> 来源：`调测HTTP智能重定向_67075036.md`（数据 + 工具）

### 6.3 调测执行步骤（含预期报文样例）

**步骤 1**：执行 `LST LICENSESWITCH` 命令，查询 UDG 上 HTTP 重定向对应的 License 配置开关是否打开。

```
LST LICENSESWITCH: LICITEM="LKV3G5SHPR01";
```

预期输出（关键字段）：
```
-------------------------
   License Item  =  LKV3G5SHPR01
   Switch        =  ENABLE
-------------------------
```

判断：
- `SWITCH=ENABLE` → 执行步骤 2
- `SWITCH=DISABLE` → 执行 `SET LICENSESWITCH:LICITEM="LKV3G5SHPR01",SWITCH=ENABLE;` 打开开关

**步骤 2**：打开接入侧/PDN 侧镜像接口上的抓包工具，准备抓取测试终端的出入报文。

**步骤 3**：测试终端访问 `www.example.com` 网页。
- 可正常访问页面 → 执行步骤 4
- 无法正常访问页面 → 调测 UDG 的 Web 浏览功能（SA-Web Browsing）

**步骤 4**：测试终端访问 `www.huawei.com` 网页，查看镜像接口的抓包信息。

**预期报文样例**：

报文 1：MS/UE 发起 HTTP Get Request
```
Source IP       =  <测试终端 IP>
Destination IP =  <www.huawei.com 解析 IP>
Protocol        =  HTTP
Method          =  GET
Host            =  www.huawei.com
User-Agent      =  Mozilla/5.0 ...
```

报文 2：UDG 缓存初始请求 URL 并向 HTTP 服务器转发；HTTP 服务器返回失败响应（error code 404）

报文 3：UDG 发送 HTTP Response 消息给 MS/UE（重定向报文）
```
Source IP       =  <UDG 用户面 IP>
Destination IP =  <测试终端 IP>
Protocol        =  HTTP
Status Code     =  302 Found   （UDG 构造的重定向响应）
Location        =  www.example.com?request-url=www.huawei.com/...&imsi=460000...
                  （第三方服务器 URL + 初始请求 URL + IMSI）
```

> 说明：对于使用 HTTP 协议访问 URL 为以 www.huawei.com 开头的网页，且浏览器类型为 Mozilla 的网页访问，当 HTTP 服务器返回的错误码大于 400 时，触发 HTTP 智能重定向。

判断：
- 测试终端跳转到 `www.example.com` 页面，接入侧/PDN 侧抓包结果与预期一致 → **重定向成功，调测结束**
- 测试终端仍显示 `www.huawei.com` 网页，接入侧/PDN 侧抓包的目的 IP 与源 IP 一样 → 执行步骤 5

**步骤 5**：执行 `LST RULE`、`LST SMARTHTTPREDIR`、`LST EXTENDEDFILTER` 命令，查询 HTTP 智能重定向规则是否与规划一致。

```
LST RULE:RULENAME="rule_test";
```

预期输出（关键字段）：
```
-------------------------
   Rule Name         =  rule_test
   Policy Type       =  SMARTREDIRECT
   Filtering Mode    =  FLOWFILTER
   Flow Filter Name  =  flow-filter1
   Priority          =  1
   Policy Name       =  http-redirect_test
-------------------------
```

```
LST SMARTHTTPREDIR:;
```

预期输出（关键字段）：
```
-------------------------
   SMTHTTPREDINAME     =  http-redirect_test
   Server URL          =  www.example.com
   Ext Flt Type 1      =  AND
   Ext Flt Name 1      =  filter_http-redirect1
   Ext Flt Type 2      =  AND
   Ext Flt Name 2      =  filter_http-redirect2
   Append Info Name    =  testredirappendinfo
   Bind ErrCode Name   =  httperrorcode
-------------------------
```

```
LST EXTENDEDFILTER: EXTFLTNAME="filter_http-redirect1";
LST EXTENDEDFILTER: EXTFLTNAME="filter_http-redirect2";
```

判断：
- 与规划一致 → 执行步骤 6
- 不一致 → 参考 `激活HTTP智能重定向` 重新配置，并再次执行步骤 3

**步骤 6**：查看 UDG 用户跟踪中的 **PFCP Session Modification Request 消息**，检查 SMF 是否下发正确的 HTTP 智能重定向规则名称。

判断：
- SMF 下发正确业务规则 → 执行步骤 7
- SMF 下发的规则不正确 → 联系 SMF 工程师修改 SMF 上的规则配置，并再次执行步骤 3

**步骤 7**：执行 `PING` 命令，查看 UDG 到第三方服务器的链路是否正常连通。

```
PING: IPVERSION=IPv4, DESTIPV4ADDRESS="192.168.200.20";
```

预期输出：
```
PING 192.168.200.20 : 56 data bytes
Reply from 192.168.200.20 : bytes=56 time=...   （收到对端响应）
```

判断：
- 收到对端网元的响应 → UDG 到第三方服务器连接正常，执行步骤 8
- 连接出现 timeout → 链路不通；检查本端或第三方服务器是否存在物理接口故障或路由配置错误，重新执行步骤 4

**步骤 8**：收集信息并寻求技术支持。
- a. 在镜像接口或服务器上开启抓包工具，执行步骤 4 并保存报文
- b. 执行 `EXP MML` 命令将当前配置数据导出为 MML 脚本文件并保存
- c. 收集并保存上述所有查询信息
- d. 查看并收集对端设备配置及接口状态信息
- e. 收集归纳所有信息并联系华为技术支持解决

> 来源：`调测HTTP智能重定向_67075036.md`（操作步骤完整 8 步）

### 6.4 调测查询命令

| 命令 | 用途 |
|------|------|
| LST LICENSESWITCH | 查询 License 配置项开关 |
| LST RULE | 查询规则配置 |
| LST SMARTHTTPREDIR | 查询 HTTP 重定向配置 |
| LST EXTENDEDFILTER | 查询扩展过滤器配置 |
| LST ERRORCODE | 查询错误码配置 |
| PING | 检查 UDG 到第三方服务器的链路连通性 |
| EXP MML | 导出 MML 配置文件（故障收集） |

### 6.5 告警参考

**本特性无相关告警**。

> 来源：`GWFD-110284 HTTP智能重定向参考信息_93168884.md`（告警）

### 6.6 软参

| 软参 | 说明 |
|------|------|
| BIT1006 | 控制 AES CBC 算法加密前明文的填充方式 |
| BIT1481 | **控制在没有 HTTP 或 DNS 错误码重定向 License 的场景下，是否可以做重定向的基本功能** |
| BIT2517 | 控制 AES CBC 算法加密前明文的填充方式 |
| BIT2519 | 控制重定向 RELATIVE 类型时间戳和 token 校验的相对时间取值 |

此外，`SET SRVCOMMONPARA` 命令的 `URLREDLEN` 参数（255~1400，默认 511）控制重定向 URL 的最大长度（非软参，为业务公共参数）。

> 来源：`GWFD-110284 HTTP智能重定向参考信息_93168884.md`（软参）、`实现原理_73611724.md`（URLREDLEN 说明）

### 6.7 测量指标

**本特性无相关测量指标**。

> 来源：`GWFD-110284 HTTP智能重定向参考信息_93168884.md`（测量指标）

### 6.8 故障排查表

| # | 问题现象 | 可能原因 | 排查方法 |
|---|---------|---------|---------|
| 1 | 重定向不生效 | License 开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5SHPR01";` 确认 SWITCH=ENABLE；若无 License 可查软参 BIT1481 是否允许基本功能 |
| 2 | 重定向不生效 | 规则配置与规划不一致 | `LST RULE`、`LST SMARTHTTPREDIR`、`LST EXTENDEDFILTER` 逐项核对 |
| 3 | 重定向不生效 | SMF 未下发正确的 HTTP 智能重定向规则名称 | 查看用户跟踪中的 PFCP Session Modification Request 消息；联系 SMF 工程师 |
| 4 | 重定向不生效 | 扩展过滤器 AND 组合条件不满足 | 检查报文是否同时满足所有 EXTENDEDFILTER；如仅匹配部分条件不触发 |
| 5 | 重定向不生效 | HTTP 服务器返回的错误码不在 ERRORCODE 范围 | 抓包检查 HTTP 响应码；对照 `ADD ERRORCODE` 的 ERRORCODEOP + ERRORCODESTART |
| 6 | 重定向不生效 | 协议限制（HTTP 2.0 或 HTTPS） | 检查报文协议；本特性只支持 HTTP 1.x；不支持 HTTPS |
| 7 | 终端未跳转 | UDG 到第三方服务器链路不通 | `PING:IPVERSION=IPv4,DESTIPV4ADDRESS="...";`；检查物理接口或路由配置 |
| 8 | 终端跳转但第三方服务器无法解析 URL | 重定向 URL 总长度超过服务器处理规格 | `SET SRVCOMMONPARA` 的 URLREDLEN 参数（默认 511），可调整至最大 1400 |
| 9 | 第三方页面报"参数缺失" | REDIRAPPENDINFO 配置的携带信息与第三方服务器预期不符 | 核对 REQURLFLAG/IMSIFLAG/MSISDNFLAG/IMEIFLAG/IPFLAG 与第三方服务器接口约定 |
| 10 | 加密场景异常 | 互斥特性未关闭（HTTP2.0 Host 识别 / HTTPS 业务地址识别） | 检查 GWFD-110201 / GWFD-110203 是否启用；本特性与之互斥 |
| 11 | 业务感知负荷高 | SA 解析对所有 HTTP 报文缓存 URL | 预期影响；评估话务模型，必要时收敛 EXTENDEDFILTER 匹配范围 |

---

## 7. 特性关系网

### 7.1 访问限制场景中的角色

在访问限制场景（NS-03）中，GWFD-110284 作为**重定向族核心特性**之一，与 GWFD-110281（用户Portal）、GWFD-110282（WebProxy）、GWFD-110283（DNS纠错）共同构成"重定向族"：

- **重定向动作（REDIRECT）**：基于错误码、URL、user agent、content-type、url-postfix 等多维条件，通过修改 HTTP 响应报文将用户访问重定向到第三方服务器
- **HTTP 层重定向**：与 DNS 纠错（DNS 层重定向）、用户 Portal（IP Farm 重定向）、Web Proxy（Web 代理重定向）构成重定向族四种协议层实现
- **POLICYTYPE=SMARTREDIRECT 共用**：与 GWFD-110283 DNS 纠错共用 POLICYTYPE=SMARTREDIRECT，区分点在 POLICYNAME 指向的对象类型（SMARTHTTPREDIR vs DNSOVERWRITING）
- **配合 ADC**：ADC（GWFD-020357）检测特定应用后，可由 SMF 下发 HTTP 智能重定向规则实现"检测到特定应用即重定向"

### 7.2 重定向族四种协议层实现差异

| 维度 | HTTP 智能重定向（110284） | DNS 纠错（110283） | 用户 Portal（110281） | Web Proxy（110282） |
|------|-------------------------|-------------------|---------------------|---------------------|
| 协议层 | L7 HTTP 响应改写 | L7 DNS 响应改写 | L3 IPFarm | L7 Web 代理 |
| POLICYTYPE | SMARTREDIRECT | SMARTREDIRECT | PCC（USERPROFILE captive） | WEBPROXY |
| 动作对象 | SMARTHTTPREDIR | DNSOVERWRITING | IPFarm | Web Proxy 配置 |
| 触发条件 | 错误码/URL/UA/content-type/url-postfix | DNS 错误码 | 未签约/配额耗尽 | Web Proxy SA 解析 |
| 适用协议 | HTTP 1.x | DNS | IP 层（任意） | HTTP |

> 来源：访问限制场景 cross-feature-analysis.md §3.2

### 7.3 与其他特性的关系

| 关联特性 | 特性ID | 关系 | 说明 |
|---------|--------|------|------|
| SA-Basic | GWFD-110101 | 依赖 | HTTP 报文解析和规则匹配基础 |
| SA-Web Browsing | GWFD-110103 | 依赖 | HTTP 解析依赖 |
| HTTP2.0 Host 识别 | GWFD-110201 | 互斥 | HTTP2.0 加密报文不支持重定向 |
| HTTPS 业务地址识别 | GWFD-110203 | 互斥 | HTTPS 加密报文不支持重定向 |
| 增强的 ADC 基本功能 | GWFD-020357 | 协同 | ADC 检测特定应用后可触发 HTTP 智能重定向 |
| HTTP/RTSP/HTTPS 头增强 | GWFD-110261/262/263 | 协同 | 重定向携带信息（MSISDN/IMSI）机制与头增强类似 |
| 用户 Portal | GWFD-110281 | 协同（重定向族） | Portal 是常见的重定向目标 |
| DNS 纠错 | GWFD-110283 | 共用 POLICYTYPE | 共用 SMARTREDIRECT，区分点在 POLICYNAME 指向 |
| URL 过滤基本功能 | GWFD-110471 | 协同 | URL 过滤的 REDIRECT 动作可触发 HTTP 智能重定向 |

### 7.4 SMARTREDIRECT 共用机制（与 DNS 纠错）

**重要**：HTTP 智能重定向和 DNS 纠错**共用 POLICYTYPE=SMARTREDIRECT**，区分点在 POLICYNAME 指向的对象类型：
- HTTP 智能重定向：POLICYNAME 指向 SMARTHTTPREDIR 对象
- DNS 纠错：POLICYNAME 指向 DNSOVERWRITING 对象

这意味着同一 RULE 不能同时承载 HTTP 重定向和 DNS 纠错，需通过不同的 RULE 实现。

> 来源：访问限制场景 cross-feature-analysis.md §3.1

---

## 8. 文档一致性自检（feature-doc-list 描述 vs 产品文档实际）

| # | 维度 | feature-doc-list / 任务描述 | 产品文档实际内容 | 差异类型 / 处理 |
|---|------|----------------------------|-----------------|---------------|
| 1 | 规则承载方式 | "PCCACTIONPROP 引用 REDIRECT；与 PCCPOLICYGRP 包装" | 产品文档明确使用 **POLICYTYPE=SMARTREDIRECT + POLICYNAME 指向 SMARTHTTPREDIR 对象**，**不经过 PCCPOLICYGRP/PCCACTIONPROP**。RULE 直接引用 SMARTHTTPREDIR 对象 | **关键差异**：HTTP 智能重定向**不走 PCCPOLICYGRP/PCCACTIONPROP 路径**，而是 SMARTREDIRECT 独立体系。本任务描述的"轨道A：RULE.POLICYTYPE→PCCPOLICYGRP→PCCACTIONPROP"实际是 ADC/头增强等典型 PCC 特性的路径，不适用于本特性。本文档已按产品文档实际机制描述 |
| 2 | 适用 NF | UDG | 产品文档明确仅 PGW-U、UPF（用户面执行），不涉及 UNC/PCF | 一致 |
| 3 | 版本支持 | UDG 20.0.0 | 产品文档明确 UDG 20.0.0 及后续版本首发 | 一致（UDG 初始版本即支持） |
| 4 | 依赖特性 | 笼统"SA 相关" | 产品文档明确依赖 **GWFD-110101 SA-Basic + GWFD-110103 SA-Web Browsing** 两个具体特性；License 控制项为 82209749 + 82209765 | 补全：依赖具体到 SA-Basic 与 SA-Web Browsing |
| 5 | 互斥特性 | 未提及 | 产品文档明确与 **GWFD-110201 HTTP2.0 Host 识别 + GWFD-110203 HTTPS 业务地址识别** 互斥（加密报文不支持） | 补全：互斥关系需明确标注 |
| 6 | 触发条件数量 | 5 类（URL/UA/content-type/url-postfix/error-code） | 产品文档应用场景章节明确 **6 类**：URL 错误、URL 过滤、content-type 过滤、url-postfix 过滤、user-agent 过滤、**错误码自动重定向（UDG 兜底，400-1000）** | 补全：错误码自动兜底为第 6 类独立场景 |
| 7 | 错误码范围 | "400-1000" | 产品文档明确"当 UDG 本地没有配置上述过滤条件时，如果 HTTP 业务响应码在如下范围内（400-1000），系统也会执行 HTTP 智能重定向动作"。注意：**仅当未配置扩展过滤器时**才走兜底 | 补全：错误码兜底的触发前提是"未配置扩展过滤器" |
| 8 | 配置示例笔误 | — | 产品文档任务示例中 `ADD FILTER:FILTERNAME="f-any"` 与 `ADD FLTBINDFLOWF:...,FILTERNAME="f_any"` 不一致（连字符 vs 下划线），**疑为笔误**。实际部署应统一 | 已在 §5.1 标注；本文档保留产品文档原文，部署时统一 |
| 9 | URL 长度限制 | 未提及 | 产品文档实现原理明确：可通过 `SET SRVCOMMONPARA` 的 `URLREDLEN` 参数配置重定向 URL 最大长度（255~1400，默认 511） | 补全：URL 长度软参 |
| 10 | 软参完整清单 | 未提及 | 产品文档参考信息明确 4 个软参：BIT1006、**BIT1481**（无 License 时基本功能开关）、BIT2517、BIT2519 | 补全：BIT1481 对无 License 场景的降级能力 |
| 11 | 计费与话单 | 未提及 | 产品文档明确**本特性不涉及计费与话单** | 一致（无计费影响） |
| 12 | 告警/测量指标 | 未提及 | 产品文档明确**本特性无相关告警、无相关测量指标** | 补全：避免误认为有告警/测量 |
| 13 | SMARTREDIRECT 共用 | 未提及 | cross-feature-analysis.md §3.1 明确：POLICYTYPE=SMARTREDIRECT 同时被 HTTP 智能重定向（110284）和 DNS 纠错（110283）共用 | 补全：共用机制需区分 POLICYNAME 指向对象 |

---

## 9. 来源文件清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/GWFD-110284 HTTP智能重定向特性概述_67329006.md` | 适用NF（PGW-U/UPF）、定义（含隐私声明）、客户价值、6类应用场景（含错误码自动兜底）、可获得性（License LKV3G5SHPR01、UDG 20.0.0+）、与其他特性交互（依赖SA-Basic+SA-Web Browsing、互斥HTTP2.0Host/HTTPS）、对系统影响（性能下降）、应用限制（仅HTTP1.x/不支持HTTPS/不支持加密host计费）、原理概述、不涉及计费与话单、特性规格（无独立限制）、遵循标准（IETF 2616）、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/实现原理_73611724.md` | 7步业务流程（请求→七层解析匹配→缓存初始URL→转发服务器→失败响应→响应解析与重定向决策→构造重定向报文→终端跳转）、ADD EXTENDEDFILTER 触发条件、URLREDLEN 参数（255~1400，默认511）、错误码/content-type/URL/user-agent/url-postfix 组合判断 |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/激活HTTP智能重定向_67075035.md` | 操作场景、必备事项、20+参数数据规划表（FILTER/FLOWFILTER/EXTENDEDFILTER/REDIRAPPENDINFO/ERRORCODE/SMARTHTTPREDIR/RULE全参数）、6步操作步骤、**任务示例（URL+UA组合+错误码>400+携带REQURL/IMSI完整MML脚本）**、基于流过滤器组的扩展（FLOWFILTERGRP） |
| 4 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/调测HTTP智能重定向_67075036.md` | 8步调测流程（License查询→镜像抓包→访问example.com基线→访问huawei.com触发→抓包核对（HTTP Get Request/HTTP Response重定向报文）→LST RULE/SMARTHTTPREDIR/EXTENDEDFILTER检查→PFCP Session Modification Request检查SMF下发→PING第三方服务器→EXP MML收集） |
| 5 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/GWFD-110284 HTTP智能重定向参考信息_93168884.md` | 7条MML命令清单（ADD FILTER/FLOWFILTER/FLTBINDFLOWF/SET REFRESHSRV/ADD EXTENDEDFILTER/ADD SMARTHTTPREDIR/ADD RULE）、**无告警**、4个软参（BIT1006/BIT1481/BIT2517/BIT2519）、**无测量指标** |

### 9.1 关键术语

| 术语 | 全称 / 说明 |
|------|------------|
| SMARTREDIRECT | HTTP 智能重定向和 DNS 纠错共用的 RULE.POLICYTYPE 取值 |
| SMARTHTTPREDIR | HTTP 智能重定向动作策略对象（POLICYNAME 指向） |
| EXTENDEDFILTER | 扩展过滤器，承载 URL/user-agent/content-type/url-postfix 单一条件 |
| ERRORCODE | 错误码范围对象，操作码（GT/LT/EQ）+ 起始值 |
| REDIRAPPENDINFO | 重定向携带信息对象（REQURLFLAG/IMSIFLAG/MSISDNFLAG/IMEIFLAG/IPFLAG） |
| URLREDLEN | SET SRVCOMMONPARA 的参数，控制重定向 URL 最大长度（255~1400，默认 511） |
| BIT1481 | 软参，控制无 License 时是否允许重定向基本功能 |
| 重定向族 | GWFD-110281/282/283/284 四特性的统称，四种协议层实现"把用户引导到指定服务器" |
