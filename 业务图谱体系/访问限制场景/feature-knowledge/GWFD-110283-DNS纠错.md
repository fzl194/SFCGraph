# GWFD-110283 DNS纠错 知识文档

> 访问限制场景 | 重定向族-DNS重写变体 | UDG | 来源：特性概述+实现原理+激活+调测+参考信息 | 2026-06-22

---

## 0. 元数据（三层图谱Schema字段，对齐 §9.3）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110283 |
| feature_name | DNS纠错 |
| feature_group | 重定向 |
| parent_feature_id | -（本特性在配置树无显式独立父节点；业务上归属"智能策略控制功能 → 重定向控制 → DNS重写"分支，与 GWFD-110284 HTTP智能重定向同属重定向族） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["重定向动作类型(DNS重写/DNS Overwriting)", "触发条件(DNS错误码ERRORCODEOP=EQUAL/GT等)", "策略下发方式(PCRF预定义规则下发/本地配置)", "Platform类型(搜索引擎/运营商Portal)", "过滤模式(FLOWFILTER单流/FLOWFILTERGRP流组)", "扩展过滤器逻辑(EXTFLTTYPE AND/OR多域名)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-110283-01, EV-FK-AC-110283-02, EV-FK-AC-110283-03, EV-FK-AC-110283-04, EV-FK-AC-110283-05]（P4建06-evidence-index时确定，先用占位） |
| license_required | `82209782 LKV3G5DNSO01 DNS纠错` |

---

## 1. 概述

### 1.1 特性定义（是什么）

用户通过浏览器上网时，DNS（Domain Name Service）服务器解析用户访问的域名，并通过 DNS 应答消息将域名对应的 IP 地址返回给用户浏览器，用户浏览器根据 IP 地址通过发送 HTTP/HTTPS 等报文来访问网站服务器。

如果用户在上网浏览时**输入错误的域名**，使 DNS 服务器无法解析该域名获得对应的 IP 地址，DNS 服务器会向用户返回 DNS 域名查询失败的应答消息，用户浏览器根据应答消息显示出错页面，从而影响用户的业务体验。

为解决上述问题，UDG 引入 **DNS 纠错功能**：UDG 截获 DNS 服务器返回的失败应答消息，根据预先制定的策略**构造一个新的 DNS 应答报文**给用户，报文中域名对应的地址设置为**第三方 Platform（如搜索引擎）的 IP 地址**，引导用户访问第三方 Platform，由第三方 Platform 向用户提供指导和帮助，提升用户的上网体验。

**本质**：DNS 纠错是**重定向的 DNS 变体**（DNS Overwriting / DNS 重写）—— 通过 DNS 响应报文重写，将用户的错误访问引导到指定的 Platform 页面。这是访问限制场景"重定向到指定 Portal/页面"动作在 **DNS 解析层**的实现。

> SourcePath: `UDG特性指南/智能策略控制功能/GWFD-110283 DNS纠错/GWFD-110283 DNS纠错特性概述_67329005.md` §定义
> SourcePath: `实现原理_73457110.md` §表1

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 支持对 DNS 报文进行解析；根据预先制定的策略（PCRF 下发或本地配置）构造新的 DNS 应答报文给终端，报文中域名对应的地址设置为第三方 Platform 的 IP 地址 |
| Platform | 第三方系统 | 无特殊要求 | Platform 为第三方系统，一般为一个搜索引擎。当用户的错误访问请求被重定向至 Platform 时，由 Platform 为用户提供帮助 |

**applicable_nf_map**（JSON）：
```json
{"UDG": ["PGW-U", "UPF"]}
```

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §适用NF、§可获得性

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 首次发布 |

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §发布历史

### 1.4 License

- **License控制项**：`82209782 LKV3G5DNSO01 DNS纠错`
- 必须获得 License 许可后才能获得该特性的服务。

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §可获得性

### 1.5 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 在用户访问出错的情况下，引导用户访问第三方 Platform，降低用户上网出错的反感情绪，从而避免用户群的流失；通过第三方 Platform 可以吸引用户定制或签约个性化定制业务，增加运营商收入 |
| 用户 | 在网络出错情况下给用户提供一个提醒页面，降低用户上网出错的反感情绪，提升用户的上网体验 |

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §客户价值

### 1.6 应用场景

用户输入错误域名时进行 DNS 纠错。如终端用户访问 internet 时输入错误的域名，DNS 解析该域名并返回解析失败响应报文，UDG 检测到该响应报文为域名出错报文，则根据预先制定的策略构造新的 DNS 应答报文，将报文中域名对应的地址设置为第三方 Platform（如搜索引擎）的 IP 地址，引导用户访问第三方 Platform，从而协助用户继续访问业务。

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §应用场景

### 1.7 前置条件与依赖

| 关系类型 | 相关特性 | License 控制项 | 说明 |
|----------|------|----------------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 LKV3G5SABS01 SA-Basic | UDG 需要对用户数据报文进行解析获得 URL，需开启 SA-Basic 特性 |
| 依赖 | GWFD-110136 SA-Network Administration | 82209765 LKV3G5SANA01 SA-Network Administration | UDG 需要对 DNS 类型报文进行解析，需开启 SA-Network Administration 特性 |
| 依赖 | GWFD-020301 内容计费基本功能 | 82209822 LKV3G5CBBF01 内容计费基本功能 | DNS 纠错动作绑定在 Rule 中，且需要通过 Filter 匹配对应 Rule，因此该功能依赖于内容计费基本功能 |
| 依赖 | GWFD-020351 PCC 基本功能 | 82209825 LKV3G5PCCB01 PCC 基本功能 | 如果 DNS 纠错业务策略由 PCRF 下发，还需启用 PCC 基本功能特性 |

**前置条件**：
- 已完成激活 PCC 基本功能
- 已加载协议特征库文件（如需解析七层协议）

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §与其他特性的交互
> SourcePath: `激活DNS纠错_67964199.md` §必备事项

### 1.8 对系统的影响

**本特性对系统无影响**（产品文档明确声明）。

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §对系统的影响

### 1.9 应用限制

**仅支持对 UDP 承载的 DNS 消息进行纠错**（不支持 TCP 承载的 DNS，如 DoT/DoH）。

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §应用限制

### 1.10 特性规格

**本特性无特殊规格**。

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §特性规格

### 1.11 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| IETF RFC | 1034 | Domain names - concepts and facilities |
| IETF RFC | 1035 | Domain names - implementation and specification |
| IETF RFC | 1304 | Domain Names - internet engineering task force（**注：见 §8 一致性说明，疑为产品文档笔误**） |
| IETF RFC | 2181 | Clarifications to the DNS Specification |

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §遵循标准

### 1.12 计费与话单

本特性**不产生新的话单**，计费方式与现有计费保持一致：
- 对于 DNS 报文，如果有重定向费率，则使用重定向费率计费
- 如果没有重定向费率，则使用匹配的业务流对应的费率进行计费

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §计费与话单

---

## 2. 激活（License开启命令）

> 与 URL 过滤基本功能一样，本特性**必须先打开 License 配置开关**才能获得服务。激活即"License开关 + 过滤条件 + DNS重写动作 + 业务规则（POLICYTYPE=SMARTREDIRECT）"。

打开本特性的 License 配置开关：

```
SET LICENSESWITCH:LICITEM="LKV3G5DNSO01",SWITCH=ENABLE;
```

查询 License 开关状态：

```
LST LICENSESWITCH:LICITEM="LKV3G5DNSO01";
```

> SourcePath: `激活DNS纠错_67964199.md` §操作步骤、§任务示例
> SourcePath: `调测DNS纠错_67964200.md` §操作步骤

---

## 3. 原理

### 3.1 实现原理：DNS 响应报文重写（DNS Overwriting）

对于**使用本地策略的非 PCC 用户**，或**使用预定义策略的 PCC 用户**访问 internet 时，UDG 对 DNS 报文进行 Rule 匹配，判断是否对该 DNS 报文进行 DNS 纠错。

DNS 纠错的核心机制是 **DNS 响应报文重写**：
1. UDG 截获 DNS Server 返回给用户的**失败应答消息**（携带错误码，如 NXDOMAIN）
2. 根据预先制定的策略，**丢弃原失败应答**
3. **构造一个新的 DNS 查询成功响应消息**（Response Code = NOERROR，Answer Section 携带 A 记录）
4. 新响应中域名对应的 IP 地址设置为**第三方 Platform 的 IP 地址**（SERVERIP1）
5. 用户浏览器收到"成功"响应，向 Platform IP 发起 HTTP 请求（URL 仍是用户原输入的错误域名）

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §原理概述
> SourcePath: `实现原理_73457110.md`

### 3.2 DNS 纠错规则匹配过程（关键参数三要素）

DNS 纠错的触发判断基于以下**三类关键参数**（产品文档实现原理表1）：

| 类别 | 关键参数 | 获取方法（MML命令） | 应用说明 |
|------|----------|----------|----------|
| **域名信息** | URL（用户访问的域名） | `ADD EXTENDEDFILTER` 定义需匹配的域名；通过 `ADD DNSOVERWRITING` 的 `EXTFLTNAME1` 参数与 DNS 重写动作绑定 | 限定哪些域名出错时触发纠错（如 `www.example.com/*`） |
| **错误码** | ERRORCODEOP（操作码）/ ERRORCODESTART（起始值）/ ERRORCODEEND（终止值） | `ADD ERRORCODE` 配置 | UDG 上配置的错误码**必须与 DNS Server 返回的响应报文中携带的一致**，否则无法触发纠错 |
| **Platform IP 地址** | SERVERIP1 | `ADD DNSOVERWRITING` 配置 | UDG 上配置的 Server IP 即为第三方 Platform 的 IP 地址，通过 UDG 构造的新的 DNS 响应报文带给终端 |

**匹配逻辑**：当 DNS 报文同时满足"域名匹配（EXTFLTNAME）+ 错误码匹配（BINDERRCODENAME）"时，触发 DNSOVERWRITING 动作，构造新 DNS 响应（IP = SERVERIP1）。

> SourcePath: `实现原理_73457110.md` §表1 DNS纠错关键参数定义

### 3.3 关键信元与 DNS 协议级细节

#### 3.3.1 触发条件：DNS 响应错误码

UDG 截获的 DNS 失败应答消息中携带的 RCODE（Response Code）是触发关键。常见 DNS 错误码（RFC 1035 §4.1.1）：

| RCODE 值 | 含义 | 是否典型触发纠错 |
|----------|------|----------------|
| 0 | NoError（无错） | 否（成功响应，不纠错） |
| 1 | FormErr（格式错误） | 视配置 |
| 2 | ServFail（服务器失败） | 视配置 |
| 3 | **NXDOMAIN（域名不存在）** | **是（最常见，任务示例 ERRORCODESTART=3 即此场景）** |
| 5 | Refused（拒绝） | 视配置 |

**配置示例**：`ADD ERRORCODE:ERRORCODENAME="dnserrorcode",ERRORCODEOP=EQUAL,ERRORCODESTART=3;` 表示匹配 RCODE=3（NXDOMAIN）时触发。

> 说明：RCODE 语义来自 RFC 1035；产品文档未逐一列举错误码含义，本表为协议级补充。

#### 3.3.2 重写后的 DNS 响应报文结构

UDG 构造的新 DNS 响应（成功响应）：

| DNS 报文字段 | 原失败响应 | UDG 重写后的成功响应 |
|-------------|----------|-------------------|
| Header.Flags.QR | 1（Response） | 1（Response） |
| Header.Flags.Opcode | 0（Standard Query） | 0（Standard Query） |
| Header.RCODE | 3（NXDOMAIN）等 | **0（NoError）** |
| Question Section | 原域名（如 www.example.com, Type A） | 原域名（保持不变） |
| Answer Section | 空（失败响应无 Answer） | **新增 A 记录：域名 → SERVERIP1（Platform IP）** |
| Authority/Additional | 原 SOA/TTL | 重写（TTL 等） |

用户浏览器收到此响应后，认为域名解析成功，向 SERVERIP1（Platform）发起 HTTP 请求，URL 仍为原错误域名。

### 3.4 业务流程（端到端 DNS 纠错）

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. 终端浏览网页，发起 DNS 查询请求                                │
│    例：访问域名 www.example.com（用户输入的错误域名）            │
│    DNS Query: www.example.com, Type A                            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. DNS 服务器解析该域名                                          │
│    解析发现查询不到该域名（NXDOMAIN）                            │
│    返回 DNS 查询失败响应给 PGW-U/UPF                             │
│    DNS Response: RCODE=3 (NXDOMAIN), Answer Section 为空         │
└──────────────────────────────┬──────────────────────────────────┘
                               │ UDG 截获
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. UDG 判断 DNS 查询失败 + Rule 匹配                             │
│    a. UDG 解析 DNS 报文（依赖 SA-Network Administration）        │
│    b. 按 FILTER（UDP/53）+ FLOWFILTER 匹配业务流                 │
│    c. 命中 RULE（POLICYTYPE=SMARTREDIRECT）                      │
│    d. 进一步匹配 DNSOVERWRITING 的三要素：                       │
│       - 域名匹配：EXTFLTNAME1 (www.example.com/*) 命中           │
│       - 错误码匹配：BINDERRCODENAME (RCODE=3) 命中               │
└──────────────────────────────┬──────────────────────────────────┘
                               │ 三要素均命中
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. UDG 构造新的 DNS 查询成功响应消息                             │
│    - 丢弃原 NXDOMAIN 失败响应                                    │
│    - 构造新响应：RCODE=0 (NoError)                               │
│    - Answer Section 新增 A 记录：                                │
│      www.example.com → SERVERIP1 (192.168.1.1, Platform IP)      │
│    - 将新响应发给终端                                            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. 终端解析新 DNS 响应，获得 Platform IP                         │
│    终端认为 www.example.com 解析成功，IP=192.168.1.1             │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. 终端发起 HTTP 请求到第三方 Platform                           │
│    - HTTP 请求报文的目的 IP = 192.168.1.1（Platform）            │
│    - HTTP 请求报文的 URL = www.example.com（用户原输入域名）     │
│    - Host 头 = www.example.com                                  │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 7. Platform 返回 HTTP 响应给终端                                 │
│    Platform（如搜索引擎）根据 URL/Host 返回纠错页面              │
│    （如"您访问的页面不存在，为您推荐以下结果"）                  │
└─────────────────────────────────────────────────────────────────┘
```

> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §原理概述（4步流程细化）

### 3.5 与重定向族的关系（访问限制场景视角）

在访问限制场景（NS-03）中，GWFD-110283 作为**重定向族的 DNS 重写变体**，与其他重定向机制形成互补：

| 重定向机制 | 特性ID | 工作层级 | 介入时机 | 触发条件 |
|-----------|--------|---------|---------|---------|
| **DNS 纠错（DNS 重写）** | GWFD-110283 | **DNS 解析层** | **DNS 响应阶段**（用户尚未建立 TCP 连接） | DNS 返回错误码（如 NXDOMAIN） |
| HTTP 智能重定向 | GWFD-110284 | HTTP 响应层（L7） | HTTP 请求/响应阶段（用户已建立 TCP 连接） | HTTP 状态码匹配（如 404） |
| Web Proxy（L3 IP NAT） | GWFD-110282 | IP 层（L3） | 报文转发阶段 | 目的 IP 匹配 |
| URL 过滤 REDIRECT | GWFD-110471 | URL 内容层（L7） | URL 解析后（ICAP 返回 REDIRECT） | ICAP Server 返回 REDIRECT 动作 |

**关键差异**：DNS 纠错是**最早的介入时机**（DNS 解析阶段），用户尚未与目标服务器建立 TCP 连接即被引导到 Platform；HTTP 智能重定向介入较晚（已建立 TCP 连接）。DNS 纠错更早期、更轻量（无需维持 TCP 连接状态）。

### 3.6 POLICYTYPE=SMARTREDIRECT 的触发机制

DNS 纠错业务规则的关键参数是 `ADD RULE:POLICYTYPE=SMARTREDIRECT`：

- `SMARTREDIRECT` 是业务规则的策略类型，表示"智能重定向"族（含 DNS 重写、HTTP 重定向等变体）
- `POLICYNAME` 指向具体的重写动作策略（DNS 纠错场景为 `DNSOVERWRITING` 名称）
- 与 URL 过滤的 `POLICYTYPE=PCC` 不同，SMARTREDIRECT 是独立策略类型，不依赖 PCCPOLICYGRP
- 会话命中 RULE 后，按 POLICYNAME 执行 DNSOVERWRITING 动作

### 3.7 策略下发方式（PCRF 下发 vs 本地配置）

DNS 纠错支持两种策略下发方式：

| 下发方式 | 适用用户 | 配置位置 | 调测差异 |
|---------|---------|---------|---------|
| **PCRF 下发预定义规则** | PCC 用户 | PCRF/SMF 下发 PFCP Session Modification Request 携带规则名 | 需查 PFCP 跟踪消息确认 SMF 是否下发正确规则（调测步骤7） |
| **本地配置** | 非 PCC 用户 | UDG 本地 ADD RULE 配置 | 直接 LST RULE 核对（调测步骤6） |

> SourcePath: `实现原理_73457110.md`（"对于使用本地策略的非PCC用户或使用预定义策略的PCC用户"）
> SourcePath: `调测DNS纠错_67964200.md` §操作步骤（步骤5-7 区分两种下发方式）

---

## 4. 配置

### 4.1 配置对象总览

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| FILTER | filter1 | 三四层过滤条件（匹配 DNS UDP 53 端口） | ADD FILTER |
| FLOWFILTER | flow-filter1 | 流过滤器 | ADD FLOWFILTER |
| FLTBINDFLOWF | （绑定关系） | Filter 与 FlowFilter 绑定 | ADD FLTBINDFLOWF |
| EXTENDEDFILTER | l7-filter1 | 扩展过滤器（URL/域名匹配） | ADD EXTENDEDFILTER |
| ERRORCODE | dnserrorcode | DNS 错误码范围 | ADD ERRORCODE |
| DNSOVERWRITING | dec_1 | DNS 重写动作策略（含 Platform IP） | ADD DNSOVERWRITING |
| RULE（SMARTREDIRECT） | testrule | DNS 纠错业务规则（POLICYTYPE=SMARTREDIRECT） | ADD RULE |

> SourcePath: `激活DNS纠错_67964199.md` §数据

### 4.2 配置流程

```
1. 打开 License 开关
   SET LICENSESWITCH

2. 【可选】加载协议特征库文件（如需解析七层协议）
   LOD SIGNATUREDB

3. 配置三四层过滤条件（匹配 DNS UDP 53）
   a. ADD FILTER（L34PROTOCOL=UDP, SVRSTARTPORT=53, SVRENDPORT=53）
   b. ADD FLOWFILTER
   c. ADD FLTBINDFLOWF
   d. SET REFRESHSRV（将 Filter 置为生效）

4. 配置扩展过滤器（域名匹配）
   ADD EXTENDEDFILTER（可重复执行增加多个不同过滤条件）

5. 配置 DNS 错误码
   ADD ERRORCODE

6. 配置 DNS 纠错动作策略
   ADD DNSOVERWRITING（绑定扩展过滤器、错误码、Platform IP）

7. 配置业务规则
   ADD RULE（POLICYTYPE=SMARTREDIRECT）
```

> SourcePath: `激活DNS纠错_67964199.md` §操作步骤

### 4.3 关键 MML 命令列表

| 命令 | 用途 |
|------|------|
| SET LICENSESWITCH | 打开/关闭 License 开关 |
| LOD SIGNATUREDB | 加载协议特征库文件（七层协议解析） |
| ADD FILTER | 增加三四层过滤器（匹配 DNS UDP 53） |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FLTBINDFLOWF | 增加流过滤器的过滤器绑定关系 |
| ADD EXTENDEDFILTER | 增加扩展过滤器（域名匹配） |
| ADD DNSOVERWRITING | 新增 DNS 重写动作（DNS纠错动作策略） |
| ADD ERRORCODE | 增加错误码 |
| ADD RULE | 增加业务规则（POLICYTYPE=SMARTREDIRECT） |

> SourcePath: `GWFD-110283 DNS纠错参考信息_93168883.md` §命令

### 4.4 关键参数说明

#### 4.4.1 ADD FILTER 参数（DNS 匹配，三四层）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| FILTERNAME | filter1 | 过滤器名字 |
| L34PROTTYPE | STRING | 三四层 IPv4 协议输入类型 |
| L34PROTOCOL | UDP | 三四层协议类型（DNS 承载在 UDP 上，**仅支持 UDP**） |
| SVRSTARTPORT | 53 | 服务器起始端口号（DNS Server 端口） |
| SVRENDPORT | 53 | 服务器结束端口号（DNS Server 端口） |

#### 4.4.2 ADD EXTENDEDFILTER 参数（域名匹配，七层）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| EXTFLTNAME | l7-filter1 | 扩展过滤器名字 |
| URL | www.example.com/* | 需要匹配的域名信息（支持通配符） |

#### 4.4.3 ADD ERRORCODE 参数（错误码范围）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| ERRORCODENAME | dnserrorcode | 错误码名称 |
| ERRORCODEOP | EQUAL | 错误码范围操作码（EQUAL/GT/LT 等） |
| ERRORCODESTART | 3 | 错误码范围起始值（3 = NXDOMAIN） |
| ERRORCODEEND | （可选） | 错误码范围终止值（范围匹配时使用） |

#### 4.4.4 ADD DNSOVERWRITING 参数（核心 - DNS 重写动作）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| DNSOVERWRTNAME | dec_1 | DNS 重写动作名字 |
| EXTFLTTYPE1 | AND | 扩展过滤器类型1（AND/OR，多域名逻辑） |
| EXTFLTNAME1 | l7-filter1 | 扩展过滤器名称1（绑定域名匹配） |
| SERVERIP1 | 192.168.1.1 | 服务器 IPv4 地址1（**第三方 Platform 的 IP 地址**，重写后 DNS 响应的 A 记录值） |
| BINDERRCODENAME | dnserrorcode | 绑定错误码名称 |

#### 4.4.5 ADD RULE 参数（DNS 纠错关键参数）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| RULENAME | testrule | 规则名称 |
| POLICYTYPE | SMARTREDIRECT | **策略类型=SMARTREDIRECT 触发 DNS 重写（DNS纠错）动作** |
| FILTERINGMODE | FLOWFILTER | 流过滤器或流过滤器组选择（FLOWFILTER / FLOWFILTERGRP） |
| FLOWFILTERNAME | flow-filter1 | 流过滤器名称 |
| PRIORITY | 20 | 全局优先级 |
| POLICYNAME | dec_1 | 策略名称（DNSOVERWRITING 动作名） |

> SourcePath: `激活DNS纠错_67964199.md` §数据
> SourcePath: `实现原理_73457110.md` §表1

### 4.5 软参

| 软参 | 说明 |
|------|------|
| BIT1481 | 控制在没有 HTTP 或 DNS 错误码重定向 License 的场景下，是否可以做重定向的基本功能 |

> SourcePath: `GWFD-110283 DNS纠错参考信息_93168883.md` §软参

---

## 5. 配置案例

### 5.1 场景一：PCRF 下发预定义规则（标准场景，产品文档任务示例）

**场景描述**：采用 PCRF 下发预定义规则方式。当用户访问 internet 时输入错误域名（如 www.example.com），UDG 执行 DNS 纠错动作，将 DNS 响应报文中的 IP 地址设置为第三方 Platform 的 IP 地址 `192.168.1.1`，用户可访问第三方 Platform。

**触发条件**：DNS Server 返回 NXDOMAIN（RCODE=3）+ 域名匹配 www.example.com/*。

**MML命令序列（原样保留产品文档任务示例）**：

```
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5DNSO01",SWITCH=ENABLE;

// 加载协议特征库文件。
LOD SIGNATUREDB:LOADMODE=SPECIFIC,VERSION="01.0002.0358.01";

// 配置 DNS纠错 使用的三四层过滤条件（匹配 DNS UDP 53 端口）。
ADD FILTER:FILTERNAME="filter1",L34PROTTYPE=STRING,L34PROTOCOL=UDP,SVRSTARTPORT=53,SVRENDPORT=53;
ADD FLOWFILTER:FLOWFILTERNAME="flow-filter1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-filter1",FILTERNAME="filter1";
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;

// 配置 DNS纠错 使用的扩展过滤器。
ADD EXTENDEDFILTER:EXTFLTNAME="l7-filter1",URL="www.example.com/*";

// 配置 DNS 错误码（RCODE=3，即 NXDOMAIN）。
ADD ERRORCODE:ERRORCODENAME="dnserrorcode",ERRORCODEOP=EQUAL,ERRORCODESTART=3;

// 配置 DNS纠错 动作（DNS 重写动作，绑定 Platform IP 192.168.1.1）。
ADD DNSOVERWRITING:DNSOVERWRTNAME="dec_1",
  EXTFLTTYPE1=AND,EXTFLTNAME1="l7-filter1",
  SERVERIP1="192.168.1.1",
  BINDERRCODENAME="dnserrorcode";

// 配置 DNS纠错 规则（POLICYTYPE=SMARTREDIRECT 是关键）。
ADD RULE:RULENAME="testrule",POLICYTYPE=SMARTREDIRECT,
  FILTERINGMODE=FLOWFILTER,
  FLOWFILTERNAME="flow-filter1",
  PRIORITY=20,
  POLICYNAME="dec_1";
```

> 来源：`激活DNS纠错_67964199.md` §任务示例

### 5.2 场景二：本地配置规则变体（非 PCC 用户）

**场景描述**：与场景一采用 PCRF 下发预定义规则不同，本场景适用于非 PCC 用户，DNS 纠错规则在 UDG 本地配置并直接生效。无需 PCRF/SMF 介入，调测时直接 `LST RULE` 核对（跳过调测步骤7的 PFCP 消息检查）。

**MML命令序列（与场景一基本一致，差异在调测路径）**：

```
// 本地配置场景下，License/特征库/Filter/FlowFilter/EXTENDEDFILTER/ERRORCODE/DNSOVERWRITING/RULE 配置完全同场景一。
SET LICENSESWITCH:LICITEM="LKV3G5DNSO01",SWITCH=ENABLE;
LOD SIGNATUREDB:LOADMODE=SPECIFIC,VERSION="01.0002.0358.01";
ADD FILTER:FILTERNAME="filter1",L34PROTTYPE=STRING,L34PROTOCOL=UDP,SVRSTARTPORT=53,SVRENDPORT=53;
ADD FLOWFILTER:FLOWFILTERNAME="flow-filter1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-filter1",FILTERNAME="filter1";
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
ADD EXTENDEDFILTER:EXTFLTNAME="l7-filter1",URL="www.example.com/*";
ADD ERRORCODE:ERRORCODENAME="dnserrorcode",ERRORCODEOP=EQUAL,ERRORCODESTART=3;
ADD DNSOVERWRITING:DNSOVERWRTNAME="dec_1",EXTFLTTYPE1=AND,EXTFLTNAME1="l7-filter1",SERVERIP1="192.168.1.1",BINDERRCODENAME="dnserrorcode";
ADD RULE:RULENAME="testrule",POLICYTYPE=SMARTREDIRECT,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-filter1",PRIORITY=20,POLICYNAME="dec_1";

// 【差异】本场景下，规则直接对非 PCC 用户生效，无需 PCRF 下发。
// 调测时跳过 PFCP Session Modification Request 检查，直接 LST RULE 核对。
```

> 来源：基于 `实现原理_73457110.md`（"使用本地策略的非PCC用户"）+ 场景一配置。

### 5.3 场景三：多域名 + 错误码范围变体（EXTFLTTYPE=OR + ERRORCODEOP=GT）

**场景描述**：纠错多个域名（如 .com/.net 错误域名都触发），且匹配多种 DNS 错误码（NXDOMAIN=3 + ServFail=2 等）。通过多扩展过滤器 + OR 逻辑 + 错误码范围实现。

**MML命令序列（差异部分）**：

```
// 配置多个扩展过滤器（不同域名）。
ADD EXTENDEDFILTER:EXTFLTNAME="l7-filter-com",URL="*.com/*";
ADD EXTENDEDFILTER:EXTFLTNAME="l7-filter-net",URL="*.net/*";

// 配置错误码范围（RCODE >= 2，即涵盖 ServFail/NXDOMAIN 等）。
ADD ERRORCODE:ERRORCODENAME="dnserrorcode-range",ERRORCODEOP=GT,ERRORCODESTART=1;

// 配置 DNS纠错动作（多域名用 OR 逻辑）。
ADD DNSOVERWRITING:DNSOVERWRTNAME="dec_multi",
  EXTFLTTYPE1=OR,EXTFLTNAME1="l7-filter-com",
  EXTFLTTYPE2=OR,EXTFLTNAME2="l7-filter-net",
  SERVERIP1="192.168.1.1",
  BINDERRCODENAME="dnserrorcode-range";

ADD RULE:RULENAME="rule_multi",POLICYTYPE=SMARTREDIRECT,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-filter1",PRIORITY=20,POLICYNAME="dec_multi";
```

> 说明：多 EXTFLTTYPE 参数（EXTFLTTYPE1/2/3...）支持 AND/OR 逻辑组合，实现复杂域名匹配。错误码范围用 GT/LT/_EQUAL 组合匹配多个 RCODE。
> 来源：基于 `激活DNS纠错_67964199.md` §操作步骤4 说明（"重复执行可增加多个不同过滤条件的扩展过滤器"）+ EXTFLTTYPE 参数语义。

### 5.4 场景四：流过滤器组变体（FLOWFILTERGRP）

**场景描述**：运营商希望基于流过滤器组设置过滤条件（而非单个 FlowFilter），适用于复杂流量分类场景。

**MML命令序列（差异部分）**：

```
// 配置流过滤器组（替代单个 FLOWFILTER）。
ADD FLOWFILTERGRP:FLOWFILTERGRPNAME="flowfiltergrp-dns";

// RULE 中使用 FLOWFILTERGRP 模式。
ADD RULE:RULENAME="testrule-grp",POLICYTYPE=SMARTREDIRECT,
  FILTERINGMODE=FLOWFILTERGRP,
  FLOWFILTERGRPNAME="flowfiltergrp-dns",
  PRIORITY=20,
  POLICYNAME="dec_1";
```

> 来源：`激活DNS纠错_67964199.md` §操作步骤7 说明（FILTERINGMODE=FLOWFILTERGRP 选项）。

### 5.5 场景变体对照表

| 变体 | 核心差异命令 | 关键参数 | 适用场景 |
|------|------------|---------|---------|
| PCRF 下发（场景一） | ADD RULE（本地预定义，SMF 下发引用） | POLICYTYPE=SMARTREDIRECT | PCC 用户，规则由 PCRF/SMF 集中下发 |
| 本地配置（场景二） | ADD RULE（本地直接生效） | POLICYTYPE=SMARTREDIRECT | 非 PCC 用户，UDG 本地策略 |
| 多域名+错误码范围（场景三） | 多 ADD EXTENDEDFILTER + EXTFLTTYPE=OR + ERRORCODEOP=GT | 多域名逻辑组合 | 批量域名纠错，多种错误码 |
| 流过滤器组（场景四） | ADD FLOWFILTERGRP + FILTERINGMODE=FLOWFILTERGRP | 流组匹配 | 复杂流量分类场景 |
| Platform 变体 | SERVERIP1 取值不同 | 搜索引擎 IP / 运营商 Portal IP | 引导到不同 Platform |
| 错误码变体 | ERRORCODEOP + ERRORCODESTART/END | EQUAL=3（NXDOMAIN）/ GT=1（多码） | 不同 DNS 错误触发 |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

运营商部署 DNS 纠错功能，使终端用户在访问 internet 出错时能引导用户访问第三方 Platform，此时需要调测该功能，确保该功能生效。本处以 **SMF 下发预定义规则**的方式为例进行说明。

> 适用：PGW-U、UPF

#### 6.1.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 用户信息查询 | IMSI | 460000123456789 | 测试终端自带 |
| 测试终端使用的APN | APN名称（APN） | apn-test | 已配置数据中获取 |
| DNS纠错规则信息 | 规则名称（RULENAME） | testrule | 取自激活文档配置信息 |

工具：测试终端、OM Portal 跟踪工具

> SourcePath: `调测DNS纠错_67964200.md` §必备事项

#### 6.1.3 调测执行步骤

**步骤1**：执行 `LST LICENSESWITCH` 查询 License 开关。

```
LST LICENSESWITCH:LICITEM="LKV3G5DNSO01";
```

预期输出：
```
-------------------------------
  License Item  =  LKV3G5DNSO01
  Switch        =  ENABLE
-------------------------------
---    END
```

判断：
- SWITCH=ENABLE → 步骤2
- SWITCH=DISABLE → 执行 `SET LICENSESWITCH:LICITEM="LKV3G5DNSO01",SWITCH=ENABLE;` 打开开关

**步骤2**：在 OM Portal 上创建用户跟踪任务，"参数配置"栏输入用户 IMSI（460000123456789），"消息类型"栏选择 **PFCP_SESSION** 消息类型。

**步骤3**：测试终端使用 `apn-test` APN 接入网络。
- 成功接入 → 步骤4
- 无法接入 → 调测 UDG 的接入功能

**步骤4**：测试终端访问 `www.example.com`（错误域名），检查是否给测试终端提供第三方 Platform 的页面。
- 是（显示 Platform 页面，如搜索引擎纠错页） → 调测结束
- 否（显示 DNS 解析失败页面） → 步骤5

**步骤5**：执行 `DSP SESSIONINFO` 查询该测试终端当前使用的业务匹配的规则。

```
DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="460000123456789";
```

预期输出：
```
-------------------------------
  IMSI  =  460000123456789
  ......
  APN name  =  apn-test
  ......
  Matched Rule Name  =  testrule
  ......
(Number of results = 1)
---    END
```

判断：
- 业务匹配的规则名称为 `testrule` → 步骤6
- 业务匹配的规则名称不为 `testrule` → 步骤7

**步骤6**：执行 `LST RULE` + `LST DNSOVERWRITING` 检查 DNS 纠错规则是否与规划一致。

```
LST RULE:RULENAME="testrule";
LST DNSOVERWRITING:DNSOVERWRTNAME="dec_1";
```

预期输出：
```
-------------------------------
  Rule Name        =  testrule
  Policy Type      =  SMARTREDIRECT
  Filtering Mode   =  FLOWFILTER
  Flow Filter Name =  flow-filter1
  Priority         =  20
  Policy Name      =  dec_1
-------------------------------
---    END
```

判断：
- 与规划一致 → 步骤8
- 不一致 → 参考 `激活DNS纠错` 重新配置，再次执行步骤3

**步骤7**：查看 OM Portal 用户跟踪中的 **PFCP Session Modification Request** 消息，检查 SMF 是否下发正确的 DNS 纠错规则名称。
- SMF 下发正确业务规则（含 testrule） → 步骤8
- SMF 下发的规则不正确 → 联系 SMF 工程师修改 SMF 上的规则配置，再次执行步骤3

**步骤8**：收集信息并寻求技术支持。
- a. 执行 `EXP MML` 命令将当前配置数据导出为 MML 脚本文件并保存
- b. 收集并保存上述所有查询信息
- c. 查看并收集对端设备配置及接口状态信息
- d. 收集归纳所有信息并联系华为技术支持解决

> SourcePath: `调测DNS纠错_67964200.md` §操作步骤
> 说明：预期输出样例为参照标杆 §6.1.3 格式补充（产品文档未给出具体输出文本），字段名依据命令语义推断，实际以设备返回为准。

### 6.2 验证命令汇总

| 命令 | 用途 |
|------|------|
| LST LICENSESWITCH | 查询 License 开关状态 |
| DSP SESSIONINFO | 显示用户上下文，查询当前匹配的规则 |
| LST RULE | 查询 DNS 纠错规则配置 |
| LST DNSOVERWRITING | 查询 DNS 重写动作配置 |
| LST FILTER / LST FLOWFILTER | 查询过滤器/流过滤器配置 |
| LST EXTENDEDFILTER | 查询扩展过滤器（域名匹配）配置 |
| LST ERRORCODE | 查询错误码配置 |
| EXP MML | 导出 MML 配置脚本（用于故障信息收集） |

> SourcePath: `调测DNS纠错_67964200.md`

### 6.3 告警参考

**本特性无相关告警**（产品文档明确）。

> SourcePath: `GWFD-110283 DNS纠错参考信息_93168883.md` §告警

### 6.4 测量指标

**本特性无相关测量指标**（产品文档明确）。

> SourcePath: `GWFD-110283 DNS纠错参考信息_93168883.md` §测量指标

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| DNS 纠错不生效（仍显示原错误页面） | License 开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5DNSO01";` 确认 SWITCH=ENABLE |
| DNS 纠错不生效 | SA-Network Administration 未启用（DNS 报文无法解析） | 检查 GWFD-110136 License；UDG 必须能解析 DNS 报文才能触发纠错 |
| DNS 纠错不生效 | DNS 承载在 TCP（如 DoT/DoH），非 UDP | 应用限制：仅支持 UDP 承载的 DNS；检查用户 DNS 配置是否走 UDP/53 |
| 纠错规则未匹配（DSP SESSIONINFO 显示的规则名不是 testrule） | PCRF/SMF 未下发正确规则（PCRF下发场景） | 步骤7 查 PFCP Session Modification Request，联系 SMF 工程师核对规则配置 |
| 纠错规则未匹配（本地配置场景） | RULE 配置错误或优先级被覆盖 | `LST RULE` 确认 POLICYTYPE=SMARTREDIRECT、PRIORITY；检查是否有更高优先级规则抢占 |
| 错误码不匹配（DNS Server 返回的 RCODE 与配置不一致） | ERRORCODE 配置与实际 RCODE 不符 | 抓包确认 DNS Server 返回的 RCODE 值；`LST ERRORCODE` 核对 ERRORCODESTART/OP |
| 域名不匹配 | EXTENDEDFILTER 的 URL 通配符与实际访问域名不匹配 | `LST EXTENDEDFILTER` 核对 URL；注意通配符格式（`www.example.com/*` vs `*.example.com/*`） |
| 纠错后用户访问 Platform 失败 | SERVERIP1（Platform IP）不可达或 Platform 服务异常 | 核对 SERVERIP1；从 UDG ping Platform IP；检查 Platform 服务状态 |
| 纠错后用户访问到错误页面 | Platform 侧未按预期返回纠错页 | 联系 Platform 维护方；Platform 根据 URL/Host 返回页面，需 Platform 支持错误域名识别 |
| Filter 未生效 | SET REFRESHSRV 未执行 | 执行 `SET REFRESHSRV:REFRESHTYPE=USERPROFILE;` 将 Filter 置为生效 |
| 计费异常 | 重定向费率配置问题 | 产品文档：有重定向费率用重定向费率，无则用业务流费率；核对计费配置 |
| 协议特征库未加载（七层解析失败） | LOD SIGNATUREDB 未执行或版本过旧 | `LOD SIGNATUREDB:LOADMODE=SPECIFIC,VERSION=...;` 加载最新特征库 |
| 无 License 仍尝试重定向 | BIT1481 软参控制 | `LST SOFTPARA` 查 BIT1481；该软参控制无 License 时是否允许基本重定向功能 |

---

## 7. 参考信息

### 7.1 与其他特性的关系（特性关系网）

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| SA-Basic | GWFD-110101（UDG） | **强依赖**：UDG 解析报文基础，必须开启 |
| SA-Network Administration | GWFD-110136（UDG） | **强依赖**：UDG 解析 DNS 类型报文必需 |
| 内容计费基本功能 | GWFD-020301（UDG） | **依赖**：DNS 纠错动作绑定在 Rule 中，需通过 Filter 匹配 Rule |
| PCC 基本功能 | GWFD-020351（UDG） | **条件依赖**：若 DNS 纠错策略由 PCRF 下发则必需；本地配置非 PCC 用户可不需要 |
| HTTP 智能重定向 | GWFD-110284（UDG） | **同族关系**：同属重定向族（SMARTREDIRECT），HTTP 智能重定向在 HTTP 响应层改写，DNS 纠错在 DNS 解析层改写 |
| URL 过滤基本功能 | GWFD-110471（UDG） | **互补关系**：URL 过滤 REDIRECT 动作在 URL 内容层，DNS 纠错在 DNS 解析层，共同构成访问限制"重定向族" |
| Web Proxy | GWFD-110282（UDG） | **互补关系**：L3 IP NAT 重定向变体，同属重定向族 |
| 用户 Portal | GWFD-110281（UDG） | **互补关系**：DNS 纠错的 Platform 可为 Portal 页面 |

> 说明：GWFD-110284/110471/110282/110281 的同族/互补关系系基于访问限制场景重定向动作语义推断（feature-doc-list §D 重定向族分组），产品文档未直接交叉引用。
> SourcePath: `GWFD-110283 DNS纠错特性概述_67329005.md` §与其他特性的交互

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110283 DNS纠错/GWFD-110283 DNS纠错特性概述_67329005.md` | 适用NF（PGW-U/UPF + Platform）、定义（DNS重写本质）、客户价值、应用场景、可获得性（UDG 20.0.0+、License LKV3G5DNSO01）、与其他特性交互（SA-Basic+SA-Network Administration+内容计费+PCC 4项依赖）、对系统影响（无）、应用限制（仅UDP DNS）、原理概述（4步业务流程）、计费与话单（重定向费率）、特性规格（无特殊）、遵循标准（RFC 1034/1035/1304/2181）、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110283 DNS纠错/实现原理_73457110.md` | DNS纠错规则匹配过程、表1 三类关键参数定义（域名URL/错误码/Platform IP）、本地策略非PCC用户 vs 预定义策略PCC用户区分 |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110283 DNS纠错/激活DNS纠错_67964199.md` | 7步操作流程、数据规划表（含配置逻辑关系图）、完整MML脚本（License+SIGNATUREDB+FILTER+FLOWFILTER+FLTBINDFLOWF+REFRESHSRV+EXTENDEDFILTER+ERRORCODE+DNSOVERWRITING+RULE）、FLOWFILTERGRP 可选说明 |
| 4 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110283 DNS纠错/调测DNS纠错_67964200.md` | 8步调测流程（LST LICENSESWITCH→OM Portal跟踪→接入→访问www.example.com→DSP SESSIONINFO→LST RULE+LST DNSOVERWRITING→PFCP消息核对→EXP MML），区分PCRF下发 vs 本地配置 |
| 5 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110283 DNS纠错/GWFD-110283 DNS纠错参考信息_93168883.md` | MML命令清单（8条核心：LOD SIGNATUREDB+FILTER+FLOWFILTER+FLTBINDFLOWF+EXTENDEDFILTER+DNSOVERWRITING+RULE+ERRORCODE隐含）、告警（无）、软参（BIT1481）、测量指标（无） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| DNS | Domain Name Service | 域名解析服务 |
| DNS Overwriting | DNS 重写 | DNS 纠错的核心机制，重写 DNS 响应报文 |
| NXDOMAIN | Non-Existent Domain | DNS 响应错误码 RCODE=3，表示域名不存在（最常见触发场景） |
| RCODE | Response Code | DNS 响应码（RFC 1035 §4.1.1） |
| Platform | 第三方系统 | 一般为搜索引擎，DNS 纠错后引导用户访问的目标 |
| DNSOVERWRITING | DNS 重写动作 | UDG 构造新 DNS 响应的动作策略，含 Platform IP |
| SMARTREDIRECT | 智能重定向 | 业务规则的 POLICYTYPE，DNS 纠错属此族 |
| EXTENDEDFILTER | 扩展过滤器 | 定义需匹配的域名信息（URL） |
| ERRORCODE | 错误码 | DNS 响应错误码范围配置 |
| SA-Network Administration | 网络管理业务感知 | UDG 解析 DNS 类型报文的基础能力 |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树/文档清单仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致与笔误，供 Stage 3 横向分析参考。

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | feature_group 归属 | feature-doc-list 将 GWFD-110283 归为"重定向"组（作为 GWFD-110284 的变体） | 产品文档路径在"智能策略控制功能"下，配置对象涉及"重定向控制 → DNS重写控制"分支 | 一致（feature-doc-list 分组与产品路径的"重定向控制"分支语义一致） |
| 2 | 触发条件完整性 | 文档清单未细化触发条件 | 产品文档明确 **三类关键参数**（域名+错误码+Platform IP）必须同时匹配 | 补全：触发条件需三要素同时命中 |
| 3 | 策略下发方式 | 文档清单未区分 | 产品文档明确 **两种策略下发方式**：PCRF 下发预定义规则（PCC用户）vs 本地配置（非PCC用户） | 补全：影响调测路径（步骤7 PFCP 消息核对仅 PCRF 场景） |
| 4 | 协议限制 | 文档清单未强调 | 产品文档明确：**仅支持 UDP 承载的 DNS**（不支持 TCP DNS，如 DoT/DoH） | 补全：关键应用限制 |
| 5 | 规格与指标 | 文档清单未列 | 产品文档明确：**无特殊规格、无告警、无测量指标**（本特性较轻量） | 补全 |
| 6 | **遵循标准笔误（疑）** | 文档清单未涉及 | 产品文档遵循标准列出 "RFC 1304 Domain Names - internet engineering task force"，**但 RFC 1304 实际为 "Packet Switching in a Local Area Network"（FDDI 相关），与 DNS 无关**；真正的 DNS 标准应为 RFC 1034/1035（已正确列出）和 RFC 2181（已正确列出） | **疑产品文档笔误**：RFC 1304 应为其他 DNS 相关 RFC（如 RFC 1034 已列，可能为重复或编号错误），建议 Stage 3 向产品组核实 |
| 7 | 对系统影响 | 文档清单未涉及 | 产品文档明确声明"**本特性对系统无影响**"（与 URL 过滤增大 CPU/时延形成对比） | 补全：DNS 纠错是轻量特性 |
| 8 | 依赖特性完整性 | 文档清单列出 SA-Basic + 内容计费 + PCC | 产品文档还明确列出 **GWFD-110136 SA-Network Administration**（DNS 报文解析必需，是区别于 URL 过滤的特有依赖） | 补全：SA-Network Administration 是 DNS 纠错特有的 SA 子特性依赖 |
| 9 | POLICYTYPE 语义 | 文档清单未明确 | POLICYTYPE=SMARTREDIRECT 是"智能重定向"族策略类型（含 DNS 重写、HTTP 重定向变体），与 URL 过滤的 POLICYTYPE=PCC 不同 | 补全：DNS 纠错走 SMARTREDIRECT 独立策略类型，不走 PCC 体系 |
| 10 | 计费方式 | 文档清单未涉及 | 产品文档明确：不产生新话单，**有重定向费率用重定向费率，无则用业务流费率** | 补全：计费继承现有机制 |
| 11 | 现有文档笔误 | （无） | 本次重读 5 份产品文档，MML 脚本参数一致，未发现明显笔误（RFC 1304 见 #6） | 仅 #6 疑似笔误 |

---
