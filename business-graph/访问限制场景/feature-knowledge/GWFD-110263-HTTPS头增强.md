# GWFD-110263 HTTPS头增强 知识文档

> 访问限制场景 | 头增强协议族（HTTP/HTTPS/RTSP/NSH）成员 | UDG | 来源：特性概述+实现原理+激活+参考信息+头增强功能专题 | 2026-06-22

---

## 0. 元数据（三层图谱Schema字段，对齐 §9.3）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110263 |
| feature_name | HTTPS头增强 |
| feature_group | 头增强 |
| parent_feature_id | -（本特性在配置树无独立父节点；业务上归属"智能策略控制功能 → 头增强控制"分支；头增强协议族父概念见 `UDG头增强功能专题`） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["协议类型(TLS1.0/1.1/1.2/1.3)", "插入字段(MSISDN/IMSI/IMEI/APN/MSIP/SGSNIP/GGSNIP/ULI/RAT/CHGCHAR/Roaming/USERDEF/User-Profile-alias/SESSIONID/TIMESTAMP/UPIPV4/UPIPV6/RANDNUM等24类，无MULTIPARA)", "插入位置(SSL报文头Extension字段内，TLV格式)", "加密算法(NONE/MD5/RC4/AES-128/AES-256/SHA-256，无RSA)", "编码方式(base64/ASCII/INHERIT + Byte837十六进制编码)", "触发方式(基于特定IP地址/基于特定SNI/基于HTTPS协议)", "过滤层级(三四层FILTER vs 七层L7FILTER+PROTBINDFLOWF PROTOCOLNAME=https)", "TLS Type值(TLSTYPEVAL + SUBTLSTYPEVAL，HTTPS独有)", "是否启用头防欺诈(支持，与HTTP头增强一致)", "灰名单模式(GRAYLIST=ENABLE只防欺诈不插入)", "POLICYTYPE=HEADEN（RULE直接引用TLSHEADEN对象，独立于PCC/SMARTREDIRECT）"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-110263-01, EV-FK-AC-110263-02, EV-FK-AC-110263-03, EV-FK-AC-110263-04, EV-FK-AC-110263-05]（P4建evidence-index时确定，先用占位） |
| license_required | `82209779 LKV3G5HTSE01 HTTPS头增强` |

---

## 1. 概述

### 1.1 特性定义（是什么）

随着互联网的快速发展，人们更注重数据传输的安全性，因此，基于安全的HTTPS协议逐渐成为互联网的主流协议。为适应主流的HTTPS协议，UDG支持HTTPS头增强功能。HTTPS头增强指对HTTPS报文头的内容做增强处理，将用户信息（如APN、IMEI、MSISDN、IMSI等）中的一个或多个信息添加到HTTPS报文头并传递给Web Server，运营商和服务提供商可基于这些信息灵活开展业务和实施控制。

**与HTTP头增强的本质差异**：HTTPS报文是加密的，HTTP头增强无法直接处理；HTTPS头增强将字段插入到**SSL报文头的Extension字段内**（在TLS握手阶段的Client Hello报文中），按照TLS协议的**TLV（Type-Length-Value）格式**组织，而非HTTP的`<字段前缀名称: 字段值>`文本格式。

> **法律声明（产品文档原文保留）**：HTTPS头增强在HTTPS报文头的扩展字段插入特定的用户标识信息，如IMSI/MSISDN/IP地址，存在将用户的个人身份信息泄露的风险。请遵循当地法律允许的目的和范围内启用相应的功能，以确保符合当地通信自由与个人隐私保护相关的法律要求。

> SourcePath: `UDG特性指南/智能策略控制功能/GWFD-110263 HTTPS头增强_67112727.md` §定义、§说明
> SourcePath: `HTTPS头增强原理_19738120.md` §组网架构（插入位置=SSL报文头Extension字段，TLV格式）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 对HTTPS报文头做内容增强处理，将用户信息中的一个或多个信息添加到HTTPS报文头并传递给Web Server |
| Web Server | 外部业务服务器 | 无特殊要求 | 支持对HTTPS报文头中增强内容的解析和处理；根据具体用户信息为用户返回定制化页面 |

**applicable_nf_map**（JSON）：
```json
{"UDG": ["PGW-U", "UPF"]}
```

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §可获得性

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 首次发布 |

> 说明：HTTPS头增强目前仅01版本（无02版本），未支持MULTIPARA多参数拼接字段（HTTP/RTSP头增强20.10.0支持）。

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §发布历史

### 1.4 License

- **License控制项**：`82209779 LKV3G5HTSE01 HTTPS头增强`
- 必须获得 License 许可后才能获得该特性的服务。

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §License支持

### 1.5 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 对用户加密业务进行认证，只允许签约用户访问专有业务；联合服务提供商进行广告宣传、业务推广等，从而获得相关收益；适应HTTPS主流协议趋势 |
| 用户 | 接收个性化加密业务内容，享受专有服务；使用实时便捷的账户管理与查询功能 |

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §客户价值

### 1.6 应用场景

| 场景 | 描述 |
|------|------|
| 加密业务访问认证 | Web Server部署在数据通信网络中，无法得知用户信息；HTTPS头增强将用户信息添加到HTTPS报文头传递给Web Server，满足运营商针对用户做加密业务访问认证的需求 |
| 个性化加密服务 | Web Server根据用户属性信息向用户返回个性化管理与查询页面以及计费结算 |
| 适应HTTPS主流化 | 随着HTTPS逐渐成为互联网主流协议，HTTPS头增强弥补HTTP头增强无法处理加密报文的不足 |

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §应用场景、§定义

### 1.7 前置条件与依赖（SA协议族依赖，含HTTP2.0 Host识别）

| 关系类型 | 相关特性 | License 控制项 | 说明 |
|----------|------|----------------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 LKV3G5SABS01 SA-Basic | **必选**：UDG解析HTTPS报文的基础 |
| 依赖 | GWFD-110103 SA-Web Browsing | 82209755 LKV3G5SAWB01 SA-Web Browsing | HTTPS解析依赖 |
| 依赖（条件性） | GWFD-110105 SA-Mobile | 82209757 LKV3G5SAMB01 SA-Mobile | HTTPS承载业务（如MMS）解析需要额外开启 |
| **依赖（HTTPS特有）** | **GWFD-110201 HTTP2.0 Host识别** | **82209773 LKV3G5HSHA01 HTTP2.0 Host识别** | **对HTTPS协议类型报文进行解析时必须开启**（HTTPS头增强独有的额外依赖） |

> 说明：HTTPS头增强的SA依赖比HTTP头增强**多一项 HTTP2.0 Host识别**（GWFD-110201），用于解析HTTPS的SNI（Server Name Indication）或证书。这是HTTPS头增强与其他头增强协议的关键差异。

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §与其他特性的交互

### 1.8 对系统的影响

当在UDG上开启HTTPS头增强特性后，由于匹配到头增强动作的用户**所有报文**，UDG都需要对其进行报文的解析和HTTPS头增强处理，因此：
- 系统处理负荷增加
- 报文转发性能和吞吐量将下降

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §对系统的影响

### 1.9 应用限制

| # | 限制项 | 说明 |
|---|--------|------|
| 1 | IPv6分片 | IPv6报文不支持中间路由器分片，对IPv6报文做HTTPS头增强需限制插入字段长度。建议 TCP MSS ≤ PMTU - IPv6首部(40B) - TCP首部(20B) - 头增强字段长度 |
| 2 | Client Hello分片 | HTTPS的**Client Hello报文分片场景下不支持头增强功能**（对应HTTP的"HTTP头域分片"限制） |
| 3 | 外置PCEF计费误差 | 网络中同时部署外置PCEF与内置PCEF时，若采用外置PCEF计费，内置PCEF上不建议部署HTTPS头增强。建议头增强与计费部署在同一网元 |
| 4 | 协议版本 | 本特性**只支持TLS1.0/1.1/1.2/1.3协议** |

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §应用限制

### 1.10 特性规格

| 规格名称 | 规格指标 |
|----------|----------|
| 支持配置的 Header Enrichment 动作个数（整机） | 100 |

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §特性规格

### 1.11 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| IETF | 5246 | The Transport Layer Security (TLS) Protocol Version 1.2 |

> 说明：HTTPS头增强遵循 TLS 1.2（RFC 5246），与HTTP头增强遵循的 HTTP/1.1（RFC 2616）不同；RTSP头增强无标准约束声明。

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §遵循标准

### 1.12 计费与话单

由于业务处理时都是**先做计费再进行头增强处理**（与规则优先级无关），所以HTTPS头增强特性对用户计费无影响，由UDG通过HTTPS头增强特性插入的信息不会作为用户上网使用的业务量进行计费统计。

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §计费与话单

---

## 2. 激活（License开启命令）

> 本特性**必须先打开 License 配置开关**才能获得服务。激活即"License开关 + ADD TLSHEADEN + ADD RULE(POLICYTYPE=HEADEN) + 绑定UserProfile"。

打开本特性的 License 配置开关：

```
SET LICENSESWITCH:LICITEM="LKV3G5HTSE01",SWITCH=ENABLE;
```

查询 License 开关状态：

```
LST LICENSESWITCH:LICITEM="LKV3G5HTSE01";
```

> SourcePath: `激活HTTPS头增强_60329629.md` §任务示例

---

## 3. 原理

### 3.1 动作机制：HEADEN —— 独立于PCC/SMARTREDIRECT的第4种POLICYTYPE

**核心结论**：HTTPS头增强与HTTP/RTSP头增强共享同一动作机制 —— RULE 中 `POLICYTYPE=HEADEN`，通过 POLICYNAME 参数**直接引用** HEADEN对象（HTTPS用 ADD TLSHEADEN 创建），**不经过** PCCPOLICYGRP。

**POLICYTYPE四轨道并列关系**（与GWFD-110261一致）：

| POLICYTYPE | 动作对象（POLICYNAME引用） | 业务含义 | 典型特性 |
|------------|--------------------------|---------|---------|
| PCC | PCCPOLICYGRP（含URRGROUP计费组） | 三四层匹配 + 计费/带宽策略 | GWFD-020351 PCC基本功能 |
| **HEADEN** | HEADEN（ADD HEADEN / **ADD TLSHEADEN**） | **报文头增强** | **GWFD-110261/262/263（本族）** |
| SMARTREDIRECT | 重定向对象 | URL/HTTP层重定向 | GWFD-110284 |
| （URL过滤） | CFTEMPLATE / CONTCATEGBIND | URL内容过滤独立动作 | GWFD-110471 |

> **HTTPS关键差异**：HTTPS头增强使用 **ADD TLSHEADEN** 命令创建头增强对象（HTTP/RTSP用 ADD HEADEN），但 RULE 的 POLICYTYPE 仍为 HEADEN，POLICYNAME 引用 TLSHEADEN 创建的对象名。

> SourcePath: `激活HTTPS头增强_60329629.md` §表8（RULE POLICYTYPE=HEADEN + POLICYNAME=header_test）

### 3.2 实现原理：SSL报文头Extension字段TLV格式插入

根据《RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2》文档对HTTPS协议的阐释，HTTPS报文头中的**扩展字段是灵活可扩展的**。HTTPS头增强特性的实现即在**HTTPS Client Hello请求报文头**（TLS握手阶段）中插入运营商规划的自定义字段内容。

**关键差异（与HTTP头增强）**：
- **插入位置**：SSL报文头的**Extension字段内**（HTTP头增强插入HTTP报文头扩展字段）
- **组织格式**：**TLS协议的TLV格式**（Type-类型，L-长度，V-数据值），而非HTTP的`<字段前缀名称: 字段值>`文本格式
- **插入时机**：TLS握手阶段的 **Client Hello 报文**（HTTP头增强在HTTP Get/Post等请求报文）

| 组成部分 | 数据来源 | 说明 |
|----------|----------|------|
| TLS Type值 | ADD TLSHEADEN 的 TLSTYPEVAL 参数 | **HTTPS头增强独有**；当插入多个字段时建议不同字段配置不同的TLSTYPEVAL |
| Sub TLS Type值 | ADD TLSHEADEN 的 SUBTLSTYPEVAL 参数 | **HTTPS头增强独有**；若多个字段插入在同一个头增强动作中且TLSTYPEVAL相同时，需配置SUBTLSTYPEVAL区分 |
| 字段值 | 业务访问用户的具体信息 | 用户相关信息实时插入 |

> SourcePath: `HTTPS头增强原理_19738120.md` §组网架构、§头增强插入字段介绍

### 3.3 支持插入的字段（24类，无MULTIPARA）

| 字段类型 | 字段值说明 | 加密 |
| --- | --- | --- |
| MSISDN | 用户激活时携带的MSISDN/GPSI | 支持 |
| IMSI | 用户激活时携带的IMSI/SUPI | 支持 |
| IMEI | 国际移动设备标识/永久设备标识（IMEI/PEI）；依赖SGSN/MME/S-GW/SMF是否携带 | 支持 |
| SGSN IP | SGSN/S-GW信令面IP地址（IPv4/IPv6） | 支持 |
| SUBPROFILE | 华为PCRF/PCF开户存储的用户信息 | 支持 |
| MS IP | 用户IP地址（IPv4/IPv6） | 支持 |
| APN | 用户激活时所属APN名称 | 支持 |
| Zone ID | HomeZone签约用户的当前HomeZone信息 | 不支持 |
| Billing Type | 用户相关计费属性信息 | 不支持 |
| CHGCHAR | 从SGSN/MME/SGW-C/SMF获取的用户计费属性 | 支持 |
| RAT | 用户接入网络类型 | 支持 |
| ULI | 用户接入位置信息（SAI/CGI（GPRS/UMTS）或ECGI/TAI（EPC）或EULF/NRLF（5GC）） | 支持 |
| CHGID | Charging ID | 不支持 |
| Roaming | 漫游属性（home/roaming/visiting） | 支持 |
| SGSN-MCC-MNC | 用户接入的SGSN/AMF所属的PLMN | 支持 |
| USERDEF | 运营商自定义字段（最多4个） | 不支持 |
| User-Profile-alias | user-profile别名 | 不支持 |
| MCC | 用户激活时携带的移动国家码 | 不支持 |
| MNC | 用户激活时携带的移动网络码 | 不支持 |
| SESSIONID | AAA服务器Access-Accept消息中Class字段 | 不支持 |
| GGSN IP | GGSN/P-GW/SMF信令面IP地址（IPv4/IPv6） | 支持 |
| TIMESTAMP | 时间戳 | 支持 |
| UPIPV4 | 用户面网关逻辑接口IPv4地址（优先级 Pa>Sa>N3>S1-U） | 支持 |
| UPIPV6 | 用户面网关逻辑接口IPv6地址（优先级 Pa>Sa>N3>S1-U） | 支持 |
| RANDNUM | 随机数，用于生成MD5/SHA256加密算法盐值 | 不支持 |

> **与HTTP/RTSP头增强字段差异**：HTTPS头增强**不支持 MULTIPARA**（多参数拼接字段），字段总数24类（HTTP/RTSP为25类含MULTIPARA）。

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §原理概述 表1；`HTTPS头增强原理_19738120.md` 表1

### 3.4 三种触发方式（基于IP / 基于SNI / 基于HTTPS协议）

| 触发方式 | 过滤条件配置 | FlowFilter配置 | 适用场景 |
|---------|------------|---------------|---------|
| **基于特定IP地址触发** | ADD FILTER（三四层）配置Web Server IP（如10.10.10.10/11）+ 端口443；**不配置协议类型** | 仅绑定FILTER，不绑定协议 | 用户通过IP访问特定Web Server；**会同时对HTTP/RTSP/HTTPS报文做头增强** |
| **基于特定SNI触发** | ADD L7FILTER 配置URL（此处URL实为SNI） | PROTBINDFLOWF绑定 **https** 协议 + L7Filter | 用户通过SNI访问特定Web Server；**SNI是HTTPS头增强独有的触发维度**（HTTP为URL，RTSP为URL） |
| **基于HTTPS协议触发** | 七层过滤，协议类型=https，**不配置L7Filter** | PROTBINDFLOWF绑定 **https** 协议，不绑L7Filter | 用户HTTPS报文触发 |

> **关键差异**：HTTPS头增强的 PROTBINDFLOWF 的 PROTOCOLNAME=**https**（HTTP=http，RTSP=rtsp）；WELLKNOWNPORT 配置端口443（HTTPS默认端口）；七层过滤的"URL"实际对应SNI。

### 3.5 业务流程（HTTPS Client Hello报文，端到端）

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. TCP三次握手                                                  │
│    MS/UE以HTTPS协议访问Web Server（如 www.huawei.com）           │
│    PGW-U/UPF 允许TCP连接的上下行报文通过                         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. MS/UE 发送 HTTPS Client Hello 报文给服务端                   │
│    （TLS握手第一阶段）                                           │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. PGW-U/UPF 三步处理（关键，与HTTP头增强不同）                 │
│    a. SA：解析报文                                              │
│       - 识别服务器IP、SNI、协议类型等关键特征                    │
│    b. Match：匹配规则                                           │
│       - 将解析到的报文特征与本地规则匹配                          │
│    c. Action：执行规则                                          │
│       - 若命中头增强动作，提取 ADD TLSHEADEN 配置的插入字段      │
│         及本地保存的用户信息                                     │
│       - 以 **TLV格式** 插入HTTPS Client Hello报文头的            │
│         Extension字段中（非HTTP的<字段名:字段值>文本格式）        │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. PGW-U/UPF 将添加头增强信息的HTTPS Client Hello 发送给Web Server │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. Web Server 处理                                              │
│    - 获取当前用户信息                                           │
│    - 构造 HTTPS Server Hello 报文返回 PGW-U/UPF                  │
│    （服务器端需支持对HTTPS Client Hello插入字段后导致的完整性校验，│
│      以确保整个TLS协商流程正常进行）                              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. PGW-U/UPF 将 HTTPS Server Hello 报文转发给 MS/UE              │
│    MS/UE 不感知 HTTPS头增强处理过程                              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 7. TLS协商完成后，数据报文在客户端和服务端间加密传输              │
└─────────────────────────────────────────────────────────────────┘
```

> SourcePath: `HTTPS头增强原理_19738120.md` §业务流程

### 3.6 安全机制（加密 + 编码）

#### 3.6.1 加密算法（无RSA）

HTTPS头增强功能支持以下加密算法：

| 加密算法 | 说明 | 安全风险 |
|---------|------|---------|
| MD5 | 支持盐值加密 | **有风险，不建议使用** |
| RC4 | — | **有风险，不建议使用** |
| AES-128 | SET AES128 配置IV值 | 安全 |
| AES-256 | SET AES256 配置IV值 | 安全 |
| SHA-256 | 支持盐值加密 | 安全 |

> **与HTTP/RTSP头增强差异**：HTTPS头增强**不支持RSA-1024和RSA-2048**（HTTP/RTSP支持），仅5种加密算法（HTTP/RTSP为7种）。MD5/RC4有安全风险不建议使用。

#### 3.6.2 编码方式（含Byte837十六进制编码）

- **base64 / ASCII编码**：与HTTP头增强一致（CIPHERTXTENCODE=BASE64/ASCII 或 INHERIT+SET BASE64+BIT475）
- **十六进制编码（HTTPS独有）**：当 ADD TLSHEADEN 的 ENCRYALGORI=**NONE**（未配置加密）时，通过软参 **Byte837** 控制是否对 MSISDN/IMSI/SGSN-IP/IMEI/MS-IP/GGSN-IP/TIMESTAMP 字段的值进行十六进制编码

#### 3.6.3 加密范围说明

当 ADD TLSHEADEN 的 ENCRYALGORI 不为 NONE 时，**UDG仅加密字段取值，不加密字段名称**。例如需插入的头增强字段为 `apn: head-en`，则UDG只会对 `head-en` 进行加密。

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §原理概述；`HTTPS头增强原理_19738120.md` §安全机制

### 3.7 与GWFD-110401 HTTP头防欺诈的关系（HTTPS也支持）

**HTTPS头增强支持头防欺诈**（与RTSP头增强的关键差异）。根据头增强功能差异表：

| 头防欺诈支持 | HTTP头增强 | **HTTPS头增强** | RTSP头增强 |
|------------|-----------|-----------------|---------------|
| 支持 | ✅ | **✅** | ❌ 不支持 |

> 说明：HTTPS头增强的防欺诈开关内嵌于 ADD TLSHEADEN 的 ANTIFRAUD 参数（与HTTP头增强的 ADD HEADEN.ANTIFRAUD 对应）。HTTPS Client Hello报文插入字段前，同样检测/纠正已存在的错误字段。

> SourcePath: `头增强功能之间的差异_10706790.md` §头防欺诈行；`激活HTTPS头增强_60329629.md` §表5（ADD TLSHEADEN 含 GRAYLIST 说明）

---

## 4. 配置

### 4.1 配置对象总览

HTTPS头增强的配置对象与HTTP头增强基本一致，关键差异：
- 头增强对象命令为 **ADD TLSHEADEN**（而非 ADD HEADEN）
- 协议绑定 PROTOCOLNAME=**https**
- WELLKNOWNPORT 端口=**443**
- ADD TLSHEADEN 含独有参数 **TLSTYPEVAL** 和 **SUBTLSTYPEVAL**

| 对象类型 | 命令 | HTTPS场景差异 |
|----------|------|------|
| FILTER | ADD FILTER | Web Server IP（如 10.10.10.10/11），端口443 |
| FLOWFILTER | ADD FLOWFILTER | — |
| FLTBINDFLOWF | ADD FLTBINDFLOWF | — |
| L7FILTER | ADD L7FILTER | URL（实际为SNI） |
| **PROTBINDFLOWF** | ADD PROTBINDFLOWF | **PROTOCOLNAME=https**（关键差异） |
| WELLKNOWNPORT | ADD WELLKNOWNPORT | **端口443**（HTTPS默认端口） |
| SIGNATUREDB | LOD SIGNATUREDB | — |
| PARSERDB | LOD PARSERDB | — |
| **TLSHEADEN** | **ADD TLSHEADEN** | **HTTPS头增强独有命令**（含TLSTYPEVAL/SUBTLSTYPEVAL/GRAYLIST等参数） |
| URR / URRGROUP | ADD URR / ADD URRGROUP | — |
| PCCPOLICYGRP | ADD PCCPOLICYGRP | — |
| RULE | ADD RULE | **POLICYTYPE=HEADEN**（与HTTP/RTSP一致，POLICYNAME引用TLSHEADEN对象） |
| USERPROFILE | ADD USERPROFILE | — |
| RULEBINDING | ADD RULEBINDING | — |

### 4.2 配置流程

```
1. 打开License开关
   SET LICENSESWITCH（LKV3G5HTSE01）

2. 配置流过滤器
   ADD FLOWFILTER

3. 配置过滤条件（三选一或组合）
   ├─ 基于IP：ADD FILTER + ADD FLTBINDFLOWF + SET REFRESHSRV
   ├─ 基于SNI：ADD L7FILTER + ADD PROTBINDFLOWF(PROTOCOLNAME=https) + SET REFRESHSRV
   └─ 基于HTTPS协议：ADD PROTBINDFLOWF(PROTOCOLNAME=https，无L7FILTER) + SET REFRESHSRV

4. 配置协议识别
   ADD WELLKNOWNPORT（端口443，PROTOCOLNAME=https）+ LOD SIGNATUREDB + LOD PARSERDB

5. 配置HTTPS头增强动作对象（ADD TLSHEADEN，含TLS Type值）
   ADD TLSHEADEN（HEADERENNAME + DATATYPE + TLSTYPEVAL + SUBTLSTYPEVAL + ENCRYALGORI）
   【多个字段多次执行该命令】

6. 配置计费属性和策略
   ADD URR + ADD URRGROUP + ADD PCCPOLICYGRP

7. 配置头增强规则（POLICYTYPE=HEADEN）
   ADD RULE（POLICYTYPE=HEADEN + FLOWFILTERNAME + POLICYNAME=header_test）

8. 配置计费规则（POLICYTYPE=PCC，可选）
   ADD RULE（POLICYTYPE=PCC + PRIORITY + POLICYNAME=pg_test）

9. 配置业务策略组合
   ADD USERPROFILE + ADD RULEBINDING
```

> SourcePath: `激活HTTPS头增强_60329629.md` §操作流程

### 4.3 关键 MML 命令列表

| 命令 | 用途 |
|------|------|
| SET LICENSESWITCH | 打开License开关（LKV3G5HTSE01） |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FILTER | 增加三四层过滤器（Web Server IP + 端口443） |
| ADD FLTBINDFLOWF | 增加流过滤器的过滤器绑定关系 |
| ADD L7FILTER | 增加七层过滤器（SNI） |
| **ADD PROTBINDFLOWF** | **增加流过滤器协议绑定关系（PROTOCOLNAME=https，HTTPS关键差异）** |
| ADD WELLKNOWNPORT | 增加知名端口（端口443，PROTOCOLNAME=https） |
| LOD SIGNATUREDB | 加载协议特征库 |
| LOD PARSERDB | 加载协议解析数据库 |
| SET REFRESHSRV | 业务刷新 |
| **ADD TLSHEADEN** | **增加HTTPS头增强（HTTPS头增强独有命令）** |
| ADD URR / ADD URRGROUP | 配置计费属性 |
| ADD PCCPOLICYGRP | 增加PCC策略组 |
| **ADD RULE** | **增加业务规则（POLICYTYPE=HEADEN）** |
| ADD USERPROFILE | 增加用户模板 |
| ADD RULEBINDING | 增加用户模板和规则的绑定关系 |

> 说明：参考信息命令列表中同时列出 ADD HEADEN 和 ADD TLSHEADEN，HTTPS头增强实际使用 ADD TLSHEADEN。

> SourcePath: `GWFD-110263 HTTPS头增强参考信息_79595498.md` §命令

### 4.4 关键参数说明

#### 4.4.1 ADD TLSHEADEN 关键参数（HTTPS头增强独有）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| HEADERENNAME | header_test | 头增强名称 |
| DATATYPE | APN / IMSI1 / MSIP1 / MSISDN1 等 | 数据类型（不支持MULTIPARA）；**多个字段需多次执行ADD TLSHEADEN** |
| **TLSTYPEVAL** | 1000 | **TLS报文头域的TLS Type值（HTTPS独有，必须配置）**；插入多个字段时建议不同字段配置不同值 |
| **SUBTLSTYPEVAL** | 10 / 20 / 30 / 40 | **TLS报文头域的Sub TLS Type值（HTTPS独有）**；若多个字段插入同一头增强动作且TLSTYPEVAL相同时需配置 |
| ENCRYALGORI | NONE / MD5 / RC4 / AES128 / AES256 / SHA256 | 加密算法标识（不支持RSA）；建议使用安全的加密算法 |
| CIPHERTXTENCODE | INHERIT / BASE64 / ASCII | 加密后编码方式 |
| GRAYLIST | ENABLE / DISABLE | 灰名单标识；ENABLE=只防欺诈不插入头增强字段 |

> SourcePath: `激活HTTPS头增强_60329629.md` §表5 头增强插入字段规划数据

#### 4.4.2 ADD WELLKNOWNPORT 关键参数（HTTPS协议识别）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| IDENPROTNAME | https_443 | 知名端口名称 |
| **PROTOCOLNAME** | **https** | **协议名称（HTTPS关键差异）** |
| PORTOP | EQUAL | 端口范围操作码 |
| STARTPORT | 443 | 起始端口号（HTTPS默认端口） |
| PRIORITY | 10 | 优先级（越小越高） |

### 4.5 软参

| 软参 | 说明 |
|------|------|
| BYTE896 | 控制头增强插入信息格式（4G/5G/4G接入5GC场景） |
| BIT475 | 控制头增强插入项加密后的值是否进行ASCII编码 |
| BIT735 | 控制系统头增强业务是否修改SACK |
| BYTE833 | 控制系统HTTP/TLS头增强报文分段不完整时的五元组老化时间 |
| **BYTE837** | **控制HTTPS头增强相关功能**（如ENCRYALGORI=NONE时是否对MSISDN/IMSI/SGSN-IP/IMEI/MS-IP/GGSN-IP/TIMESTAMP字段值十六进制编码） |
| BIT1006 | 控制AES CBC算法加密前明文的填充方式 |
| BIT1307 | 控制头增强特性是否支持启用TCP SACK功能 |
| BIT2517 | 控制AES CBC算法加密前明文的填充方式 |

> 说明：HTTPS头增强参考信息列出8个软参（少于HTTP头增强的13个，HTTPS独有 BYTE837）。

> SourcePath: `GWFD-110263 HTTPS头增强参考信息_79595498.md` §软参

---

## 5. 配置案例

### 5.1 场景一：基于SNI触发 + 多字段插入（标准部署，含TLS Type值）

**场景描述**：运营商Web Server需要通过获取用户的APN、IMSI、MSIP、MSISDN给某些用户提供特殊定制业务。UDG将用户上行HTTPS报文做头增强，采用基于特定IP地址、基于特定SNI或HTTPS协议的触发方式，将APN/IMSI/MSIP/MSISDN字段插入用户报文携带给Web Server。

**MML命令序列（原样保留产品文档）**：

```
// 打开本特性的License配置开关。
SET LICENSESWITCH: LICITEM="LKV3G5HTSE01",SWITCH=ENABLE;

// 配置流过滤器。
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";

// 配置基于特定IP地址触发HTTPS头增强，使用的三四层过滤条件。
ADD FILTER: FILTERNAME="filter_test1", L34PROTTYPE=STRING, L34PROTOCOL=TCP, SVRIPMODE=IP, SVRIP="10.10.10.10", SVRIPMASKTYPE=IPTYPE, SVRIPMASK="0.0.0.0", SVRSTARTPORT=443, SVRENDPORT=443;
ADD FILTER: FILTERNAME="filter_test2", L34PROTTYPE=STRING, L34PROTOCOL=TCP, SVRIPMODE=IP, SVRIP="10.10.10.11", SVRIPMASKTYPE=IPTYPE, SVRIPMASK="0.0.0.0", SVRSTARTPORT=443, SVRENDPORT=443;
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test2";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置基于特定SNI和HTTPS协议触发HTTPS头增强，使用七层过滤条件。
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_2",URL="www.example.com";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="https",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置知名端口识别HTTPS协议。
ADD WELLKNOWNPORT:IDENPROTNAME="https_443",PROTOCOLNAME="https",PORTOP=EQUAL,STARTPORT=443,PRIORITY=10;

// 配置报文特征库识别协议。
LOD SIGNATUREDB:LOADMODE=LATEST;
LOD PARSERDB:LOADMODE=LATEST;

// 配置HTTPS头增强动作属性（4个字段，多次执行ADD TLSHEADEN，每个字段不同SUBTLSTYPEVAL）。
ADD TLSHEADEN:HEADERENNAME="header_test",DATATYPE=APN,TLSTYPEVAL=1000, SUBTLSTYPEVAL=10, ENCRYALGORI=NONE;
ADD TLSHEADEN:HEADERENNAME="header_test",DATATYPE=IMSI1,TLSTYPEVAL=1000, SUBTLSTYPEVAL=20, ENCRYALGORI=NONE;
ADD TLSHEADEN:HEADERENNAME="header_test",DATATYPE=MSIP1,TLSTYPEVAL=1000, SUBTLSTYPEVAL=30, ENCRYALGORI=NONE;
ADD TLSHEADEN:HEADERENNAME="header_test",DATATYPE=MSISDN1,TLSTYPEVAL=1000, SUBTLSTYPEVAL=40, ENCRYALGORI=NONE;

// 配置HTTPS头增强使用的计费属性。
ADD URR:URRNAME="urr01",URRID=1000,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="cp_test",UPURRNAME1="urr01",DOWNURRNAME1="urr01";

// 配置HTTPS头增强使用的PCC动作策略组。
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="cp_test";

// 配置HTTPS头增强使用的规则（POLICYTYPE=HEADEN）。
ADD RULE:RULENAME="rule_test1",POLICYTYPE=HEADEN,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flowfilter_test",POLICYNAME="header_test";

// 配置计费规则（POLICYTYPE=PCC，与头增强规则共用同一FLOWFILTER）。
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flowfilter_test",PRIORITY=20, POLICYNAME="pg_test";

// 配置HTTPS头增强使用的业务策略组合（规则与用户模板的绑定关系）。
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test1";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

> 来源：`激活HTTPS头增强_60329629.md` §任务示例（脚本完整保留）

### 5.2 场景二：基于HTTPS协议触发变体（不配置SNI）

**场景描述**：仅配置协议绑定（PROTOCOLNAME=https），不配置L7Filter。所有HTTPS报文触发头增强。

**MML命令序列（相对场景一的差异部分）**：

```
// 配置基于HTTPS协议触发HTTPS头增强（不配置L7FILTER，仅绑https协议）。
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="https";
SET REFRESHSRV:REFRESHTYPE=ALL;
```

> 来源：`激活HTTPS头增强_60329629.md` §任务示例"七层过滤条件（HTTPS协议）"部分

### 5.3 场景变体对照表

| 变体 | 核心差异命令 | 关键参数 | 适用场景 |
|------|------------|---------|---------|
| 基于SNI触发（场景一） | ADD L7FILTER + ADD PROTBINDFLOWF | URL(SNI) + PROTOCOLNAME=https | 按SNI精确触发（主流） |
| 基于IP触发 | ADD FILTER + ADD FLTBINDFLOWF | Web Server IP + 端口443 | 按IP触发；同时影响HTTP/RTSP/HTTPS |
| 基于HTTPS协议（场景二） | ADD PROTBINDFLOWF | PROTOCOLNAME=https，无L7FILTER | 按协议触发，不区分SNI |
| 防欺诈+加密 | ADD TLSHEADEN ANTIFRAUD=ENABLE | ANTIFRAUD=ENABLE + ENCRYALGORI | 防欺诈+头增强（HTTPS支持） |
| 灰名单模式 | ADD TLSHEADEN GRAYLIST=ENABLE | GRAYLIST=ENABLE | 只防欺诈不插入 |
| 十六进制编码 | SET SOFTPARA Byte837 | ENCRYALGORI=NONE时启用 | HTTPS独有（HTTP/RTSP无） |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

当运营商需要部署HTTPS头增强功能时，需对HTTPS头增强功能进行调测，确保本功能可以正常使用。

> 适用：PGW-U、UPF。

#### 6.1.2 调测执行步骤（参照HTTP头增强调测流程）

HTTPS头增强的调测流程与HTTP头增强基本一致（产品文档调测文档未单独给出HTTPS预期输出样例，参照HTTP头增强调测结构）：

1. **查询License开关**：`LST LICENSESWITCH:LICITEM="LKV3G5HTSE01";` 确认开关=打开
2. **打开UDG接入侧/PDN侧镜像接口抓包工具**
3. **测试终端接入网络**：使用规划APN接入
4. **测试终端浏览HTTPS业务**：访问规划的HTTPS URL，查看镜像接口抓包信息
   - SGi/N6镜像接口抓包显示HTTPS Client Hello报文中插入了配置的头增强内容（TLV格式），且字段值正确 → HTTPS头增强功能正常
   - 未插入或字段值有误 → 步骤5
   - 无法访问 → 调测UDG的Web浏览功能（GWFD-110103 SA-Web Browsing）和HTTP2.0 Host识别（GWFD-110201）
5. **查询用户上下文**：`DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="...";`
6. **检查HTTPS头增强配置**（见6.1.3）
7. **收集信息并寻求技术支持**

> 说明：HTTPS头增强调测文档未提供独立的预期输出样例，参照HTTP头增强调测（`调测HTTP头增强_21598754.md`）的输出格式，关键差异是抓包观察的是HTTPS Client Hello报文（而非HTTP GET报文）。
> SourcePath: `调测HTTP头增强_21598754.md` §操作步骤（HTTPS场景参照）

#### 6.1.3 配置验证命令

| 命令 | 用途 | 验证点 |
|------|------|--------|
| LST LICENSESWITCH | 查询License开关 | LICITEM=LKV3G5HTSE01 是否 打开 |
| DSP SESSIONINFO | 显示用户上下文 | IMSI/MSISDN/APN 与规划值一致 |
| LST RULEBINDING | 查询规则绑定 | 规则名称=rule_test1，策略类型=Header Enrichment |
| LST RULE | 查询规则 | POLICYTYPE=HEADEN，策略名称=header_test，PCC策略组名称=NULL |
| LST PROTBINDFLOWF | 查询协议绑定 | **协议名称=https**（HTTPS关键差异），七层过滤器名字=l7filter_test |
| LST FILTER / LST FLTBINDFLOWF | 查询过滤器 | Web Server IP、端口443 |
| LST L7FILTER | 查询七层过滤器 | URL（实际为SNI） |
| LST TLSHEADEN | 查询HTTPS头增强 | 数据类型、TLSTYPEVAL、SUBTLSTYPEVAL、加密算法标识 |
| LST WELLKNOWNPORT | 查询知名端口 | **协议名称=https，端口443** |
| DSP SIGNATUREDB | 查询特征库加载状态 | Load Finish |
| EXP MML | 导出MML配置脚本 | 故障信息收集 |

### 6.2 告警参考

**本特性无相关告警**（产品文档明确声明）。

> SourcePath: `GWFD-110263 HTTPS头增强参考信息_79595498.md` §告警

### 6.3 测量指标

**本特性无相关测量指标**（产品文档明确声明）。

> SourcePath: `GWFD-110263 HTTPS头增强参考信息_79595498.md` §测量指标

### 6.4 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| HTTPS头增强字段未插入 | License开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5HTSE01";` 确认开关=打开 |
| HTTPS头增强字段未插入 | SA依赖未开启（SA-Basic/SA-Web Browsing/**HTTP2.0 Host识别** License未开） | 检查SA协议族依赖License（见 §1.7）；**特别确认 LKV3G5HSHA01 HTTP2.0 Host识别已开** |
| HTTPS头增强字段未插入 | 协议绑定错误（PROTOCOLNAME不是https） | `LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test";` 确认协议名称=https |
| HTTPS头增强字段未插入 | HTTPS协议未识别（未配置WELLKNOWNPORT 443或特征库未加载） | `LST WELLKNOWNPORT` 确认HTTPS端口443；`DSP SIGNATUREDB` 确认 Load Finish |
| HTTPS头增强字段未插入 | 规则策略类型不是HEADEN | `LST RULE:RULENAME="rule_test1";` 确认策略类型=Header Enrichment，策略名称=header_test |
| HTTPS头增强字段未插入 | 使用了ADD HEADEN而非ADD TLSHEADEN | HTTPS头增强必须用 **ADD TLSHEADEN**（含TLSTYPEVAL参数） |
| Client Hello分片场景未做头增强 | Client Hello报文分片不支持（应用限制#2） | 属预期行为 |
| 防欺诈未生效 | ANTIFRAUD未置ENABLE | `LST TLSHEADEN` 确认防欺诈标识=使能 |
| TLS协商失败 | 服务器端不支持Client Hello插入字段后的完整性校验 | 服务器端需支持对HTTPS Client Hello插入字段后的完整性校验（产品文档明确） |
| 加密后字段值与Web Server解析不一致 | UDG仅加密字段取值，不加密字段名称 | 属预期行为；Web Server侧需对应解析 |
| IPv6业务无法访问 | 头增强字段过长导致报文超PMTU | 限制头增强字段长度；调整TCP MSS |
| HTTP报文同时被头增强 | 基于IP触发时不区分协议 | 改用基于SNI触发；属预期行为（设计如此） |
| TLS1.3之外协议不支持 | 仅支持TLS1.0/1.1/1.2/1.3（应用限制#4） | 属预期行为 |

---

## 7. 参考信息

### 7.1 与其他特性的关系（头增强协议族 + 依赖）

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| SA-Basic | GWFD-110101（UDG） | **强依赖**：UDG解析HTTPS报文的基础 |
| SA-Web Browsing | GWFD-110103（UDG） | **协议依赖**：HTTPS解析必需 |
| SA-Mobile | GWFD-110105（UDG） | **条件依赖**：HTTPS承载业务（如MMS）解析需要 |
| **HTTP2.0 Host识别** | **GWFD-110201（UDG）** | **HTTPS特有强依赖**：对HTTPS协议类型报文进行解析时必须开启（解析SNI/证书） |
| HTTP头增强 | GWFD-110261（UDG） | **协议族兄弟**：HTTP协议的对应实现（共用ADD HEADEN命令；HTTPS用ADD TLSHEADEN） |
| RTSP头增强 | GWFD-110262（UDG） | **协议族兄弟**：RTSP协议的对应实现 |
| NSH头增强 | （业务专题） | **协议族兄弟**：NSH协议的对应实现 |
| PCC基本功能 | GWFD-020351（UDG） | **配合关系**：头增强规则与计费规则可绑定同一UserProfile |
| 增强的ADC基本功能 | GWFD-020357（UDG） | **配合关系**：ADC检测是HTTPS解析的前置能力 |
| URL过滤基本功能 | GWFD-110471（UDG） | **配合关系**：URL过滤对HTTPS仅能解析SNI；HTTPS头增强插入位置（Client Hello Extension）与SNI同源 |

> SourcePath: `GWFD-110263 HTTPS头增强_67112727.md` §与其他特性的交互

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110263 HTTPS头增强_67112727.md` | 适用NF、定义、法律声明、客户价值、应用场景、可获得性（UDG 20.0.0+、License LKV3G5HTSE01）、与其他特性交互（SA-Basic/SA-Web Browsing/SA-Mobile/**HTTP2.0 Host识别**）、对系统影响、应用限制（4条）、原理概述（24字段表、SSL Extension TLV格式、加密算法、编码方式、Byte837十六进制编码、加密范围说明）、特性规格（100动作）、遵循标准（IETF 5246 TLS 1.2）、计费与话单、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTPS头增强功能/GWFD-110263 HTTPS头增强参考信息_79595498.md` | MML命令清单（16条）、告警（无）、软参（8个：BYTE896/BIT475/BIT735/BYTE833/BYTE837/BIT1006/BIT1307/BIT2517）、测量指标（无） |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTPS头增强功能/HTTPS头增强原理描述/HTTPS头增强原理_19738120.md` | 组网架构（插入位置=SSL报文头Extension字段内，TLV格式）、头增强支持插入字段（24字段）、业务流程（7步TLS握手）、触发条件（基于IP/SNI/HTTPS协议3种）、安全机制（5加密算法+2编码方式+Byte837十六进制） |
| 4 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTPS头增强功能/HTTPS头增强原理描述/约束限制和系统影响_19898030.md` | 约束限制（4条：IPv6/Client Hello分片/外置PCEF/TLS版本）、系统影响 |
| 5 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTPS头增强功能/激活HTTPS头增强_60329629.md` | 10步操作流程、数据规划表（10张表，含TLSTYPEVAL/SUBTLSTYPEVAL规划）、完整MML脚本（License+FLOWFILTER+FILTER+L7FILTER+PROTBINDFLOWF+WELLKNOWNPORT+SIGNATUREDB+PARSERDB+TLSHEADEN+URR+URRGROUP+PCCPOLICYGRP+RULE+USERPROFILE+RULEBINDING）、BYTE896软参5G格式插入说明 |
| 6 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTPS头增强功能/调测HTTPS头增强_68438393.md` | HTTPS头增强调测文档（预期输出样例参照HTTP头增强调测） |
| 7 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/头增强功能之间的差异_10706790.md` | HTTP/HTTPS/RTSP头增强差异对照表（触发条件/支持协议/交互特性/业务/加密算法/编码/头防欺诈支持） |
| 8 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/特性映射_57402091.md` | 头增强协议族特性映射（GWFD-110263 → License LKV3G5HTSE01） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| TLS | Transport Layer Security | 传输层安全协议（HTTPS头增强插入位置） |
| TLSHEADEN | HTTPS头增强对象 | ADD TLSHEADEN 命令创建（区别于HTTP/RTSP的ADD HEADEN） |
| TLV | Type-Length-Value | TLS协议扩展字段组织格式（HTTPS头增强使用） |
| TLSTYPEVAL | TLS Type值 | ADD TLSHEADEN 独有参数，标识Extension字段类型 |
| SUBTLSTYPEVAL | Sub TLS Type值 | ADD TLSHEADEN 独有参数，同一TLSTYPEVAL下区分多字段 |
| SNI | Server Name Indication | TLS握手时携带的目标域名（HTTPS头增强触发维度之一） |
| Client Hello | TLS握手第一阶段报文 | HTTPS头增强字段插入的时机 |
| Extension字段 | TLS扩展字段 | HTTPS头增强插入的位置（SSL报文头内） |
| Byte837 | 软参 | HTTPS头增强独有，控制ENCRYALGORI=NONE时十六进制编码 |
| HTTP2.0 Host识别 | GWFD-110201 | HTTPS头增强独有依赖（解析SNI/证书） |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树/文档清单仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致与笔误，供 Stage 3 横向分析参考。

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | feature_group 归属 | feature-doc-list 归为"头增强"组 | 产品文档路径在"智能策略控制功能"下；业务专题归"UDG头增强功能专题/HTTPS头增强功能" | 一致 |
| 2 | POLICYTYPE | 文档清单未明确策略类型 | 产品文档明确 **POLICYTYPE=HEADEN**（RULE引用 TLSHEADEN 对象，不经过PCCPOLICYGRP） | 补全：HEADEN是第4种POLICYTYPE |
| 3 | 命令差异 | 文档清单未明确 | 产品文档明确 HTTPS头增强用 **ADD TLSHEADEN**（HTTP/RTSP用ADD HEADEN）；含独有参数 TLSTYPEVAL/SUBTLSTYPEVAL | 补全：HTTPS头增强命令差异 |
| 4 | 头防欺诈支持 | 文档清单未明确 | 头增强差异表明确 **HTTPS头增强支持头防欺诈**（与HTTP一致；RTSP不支持） | 补全：HTTPS防欺诈=支持 |
| 5 | 协议绑定参数 | 文档清单未明确 | 产品文档明确 PROTBINDFLOWF 的 PROTOCOLNAME=**https**；WELLKNOWNPORT 端口=**443** | 补全 |
| 6 | 插入位置 | 文档清单未明确 | 产品文档明确插入 **SSL报文头Extension字段内，TLV格式**（HTTP为HTTP报文头扩展字段，`<字段名:字段值>`文本格式） | 补全：HTTPS插入位置/格式与HTTP本质不同 |
| 7 | 触发维度 | 文档清单未明确 | 产品文档明确 HTTPS头增强触发维度含**基于特定SNI**（HTTP为URL，RTSP为URL） | 补全：SNI是HTTPS独有触发维度 |
| 8 | 加密算法 | 文档清单未列 | 产品文档明确 HTTPS头增强**仅支持5种加密算法**（MD5/RC4/AES-128/AES-256/SHA-256，**无RSA**）；HTTP/RTSP为7种 | 补全：HTTPS不支持RSA加密 |
| 9 | 字段数量 | 文档清单未明确 | 产品文档明确 HTTPS头增强**不支持MULTIPARA**，字段总数24类（HTTP/RTSP为25类含MULTIPARA） | 补全：HTTPS不支持多参数拼接 |
| 10 | HTTP2.0 Host识别依赖 | 文档清单未明确 | 产品文档明确 HTTPS头增强**额外依赖 GWFD-110201 HTTP2.0 Host识别**（HTTP/RTSP无此依赖） | 补全：HTTPS独有依赖 |
| 11 | 十六进制编码 | 文档清单未明确 | 产品文档明确 HTTPS独有 **Byte837** 软参，控制ENCRYALGORI=NONE时十六进制编码 | 补全：HTTPS独有编码 |
| 12 | 现有文档笔误 | （无） | 本次重读产品文档未发现明显笔误（4份文档MML脚本参数一致） | 无 |
| 13 | 参考信息命令列表 | — | 参考信息同时列出 ADD HEADEN 和 ADD TLSHEADEN；HTTPS头增强实际使用 ADD TLSHEADEN，ADD HEADEN 仅为兼容性列出 | 说明：实际使用 ADD TLSHEADEN |
| 14 | 软参数量差异 | — | HTTPS头增强参考信息列出8个软参（HTTP头增强13个），HTTPS独有 BYTE837 | 补全 |

---
