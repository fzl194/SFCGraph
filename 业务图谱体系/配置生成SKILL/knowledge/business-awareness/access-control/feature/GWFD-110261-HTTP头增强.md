# GWFD-110261 HTTP头增强 知识文档

> 访问限制场景 | 头增强协议族（HTTP/HTTPS/RTSP/NSH）成员 | UDG | 来源：特性概述+实现原理+激活+调测+参考信息+头增强功能专题 | 2026-06-22

---

## 0. 元数据（三层图谱Schema字段，对齐 §9.3）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110261 |
| feature_name | HTTP头增强 |
| feature_group | 头增强 |
| parent_feature_id | -（本特性在配置树无独立父节点；业务上归属"智能策略控制功能 → 头增强控制"分支；头增强协议族父概念见 `UDG头增强功能专题`） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["协议类型(HTTP1.x)", "插入字段(MSISDN/IMSI/IMEI/APN/MSIP/SGSNIP/GGSNIP/ULI/RAT/CHGCHAR/Roaming/USERDEF/User-Profile-alias/SESSIONID/TIMESTAMP/UPIPV4/UPIPV6/MULTIPARA/RANDNUM等25类)", "加密算法(NONE/MD5/RC4/AES-128/AES-256/RSA-1024/RSA-2048/SHA-256)", "编码方式(base64/ASCII/INHERIT)", "触发方式(基于特定IP地址/基于特定URL/基于HTTP协议)", "过滤层级(三四层FILTER vs 七层L7FILTER+PROTBINDFLOWF)", "是否启用头防欺诈(ADD HEADEN ANTIFRAUD=ENABLE，强耦合GWFD-110401)", "灰名单模式(GRAYLIST=ENABLE只防欺诈不插入)", "POLICYTYPE=HEADEN（RULE直接引用HEADEN对象，独立于PCC/SMARTREDIRECT）"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-110261-01, EV-FK-AC-110261-02, EV-FK-AC-110261-03, EV-FK-AC-110261-04, EV-FK-AC-110261-05]（P4建evidence-index时确定，先用占位） |
| license_required | `82209777 LKV3G5HTHE01 HTTP头增强` |

---

## 1. 概述

### 1.1 特性定义（是什么）

HTTP头增强指对HTTP报文头的内容做增强处理，将用户信息（如APN、IMEI、MSISDN、IMSI、MSIP等）中的一个或多个信息添加到HTTP报文头，并传递给Web Server。运营商和服务提供商可基于这些信息灵活开展业务和实施控制，例如业务认证、广告宣传、业务推广和账户管理与查询。

**本质**：一种"带内（in-band）"用户信息传递机制 —— 业务服务器（Web Server）位于纯粹的数据通信网络中，无法直接获取承载网用户属性；HTTP头增强将MSISDN/IMSI/APN等承载网属性直接注入用户业务请求报文头中，业务服务器在处理业务请求的同时即可获得该信息，无需额外信令会话（区别于传统的带外RADIUS方式）。

> **法律声明（产品文档原文保留）**：HTTP头增强在HTTP报文头的扩展字段插入特定的用户标识信息，如IMSI/MSISDN/IP地址，存在将用户的个人身份信息泄露的风险。请遵循当地法律允许的目的和范围内启用相应的功能，以确保符合当地通信自由与个人隐私保护相关的法律要求。

> SourcePath: `UDG特性指南/智能策略控制功能/GWFD-110261 HTTP头增强_62736942.md` §定义、§说明
> SourcePath: `业务专题/UDG头增强功能专题/头增强功能概述_04211022.md` §背景（带内 vs 带外）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 对HTTP报文头做内容增强处理，将用户信息中的一个或多个信息添加到HTTP报文头并传递给Web Server |
| Web Server | 外部业务服务器 | 无特殊要求 | 支持对HTTP报文头中增强内容的解析和处理；根据具体用户信息为用户返回定制化页面，可用于广告宣传、账户查询、消费提醒、业务推广及业务认证等 |

**applicable_nf_map**（JSON）：
```json
{"UDG": ["PGW-U", "UPF"]}
```

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §可获得性

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 02 | 20.10.0 | 支持插入多参数拼接字段（MULTIPARA，最多3个拼接字段 × 每字段4参数） |
| 01 | 20.0.0 | 首次发布 |

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §发布历史

### 1.4 License

- **License控制项**：`82209777 LKV3G5HTHE01 HTTP头增强`
- 必须获得 License 许可后才能获得该特性的服务。

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §License支持

### 1.5 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 对用户业务进行认证，只允许签约用户访问专有业务；联合服务提供商进行广告宣传、业务推广等，从而获得相关收益；降低对业务服务器的复杂度要求；在UDG上集成WAP GW的部分功能，助力网络简化 |
| 用户 | 接收个性化业务内容，享受专有服务；使用实时便捷的账户管理与查询功能 |

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §客户价值；`头增强功能概述_04211022.md` §价值

### 1.6 应用场景

| 场景 | 描述 |
|------|------|
| 业务访问认证 | Web Server部署在数据通信网络中，无法得知用户信息；HTTP头增强将用户信息添加到HTTP报文头传递给Web Server，满足运营商针对用户做业务访问认证的需求 |
| 个性化服务 | 运营商/服务提供商的Web Server根据用户属性信息向用户返回个性化管理与查询页面以及计费结算 |
| 自营业务定制 | 运营商需要为用户提供自营数据业务（如指定用户访问某网站免流量费），Web Server通过头增强字段识别用户身份 |

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §应用场景

### 1.7 前置条件与依赖（SA协议族依赖）

| 关系类型 | 相关特性 | License 控制项 | 说明 |
|----------|------|----------------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 LKV3G5SABS01 SA-Basic | **必选**：UDG需对HTTP报文进行解析以执行头增强动作；SA-Basic是所有SA(Service Awareness)协议解析的基础 |
| 依赖 | GWFD-110103 SA-Web Browsing | 82209755 LKV3G5SAWB01 SA-Web Browsing | HTTP/WAP2.0协议解析必需 |
| 依赖（条件性） | GWFD-110105 SA-Mobile | 82209757 LKV3G5SAMB01 SA-Mobile | HTTP承载业务（如MMS）头增强时需要额外开启 |

> 说明：一些业务承载于HTTP协议之上（如MMS、流媒体等），对这些业务进行HTTP头增强时，还需在UDG上开启对应协议的SA特性。例如对HTTP承载的MMS业务进行HTTP头增强，需要增加开启SA-Mobile特性。

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §与其他特性的交互

### 1.8 对系统的影响

当在UDG上开启HTTP头增强特性后，由于匹配到头增强动作的用户**所有报文**，UDG都需要对其进行报文的解析和HTTP头增强处理，因此：
- 系统处理负荷增加
- 报文转发性能和吞吐量将下降

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §对系统的影响

### 1.9 应用限制

| # | 限制项 | 说明 |
|---|--------|------|
| 1 | METHODTYPE限制 | 若整机未通过 ADD L7FILTER 配置METHODTYPE，只支持对默认METHODTYPE（GET、POST、CONNECT）的业务做头增强；配置后由软参 BIT316 控制行为（=0仅默认+配置的METHODTYPE；=1支持默认+配置+其他特殊METHODTYPE） |
| 2 | IPv6分片 | IPv6报文不支持中间路由器分片，对IPv6报文做HTTP头增强需限制插入字段长度。建议 TCP MSS ≤ PMTU - IPv6首部(40B) - TCP首部(20B) - 头增强字段长度。插入字段过长导致报文超过PMTU将导致IPv6业务无法访问 |
| 3 | MTU过小分片 | 网络设备MTU过小，用户报文到达UDG前被分片，UDG**不对分片报文**进行头增强处理 |
| 4 | HTTP头域分片 | HTTP头域分片的请求报文不支持头增强功能 |
| 5 | 外置PCEF计费误差 | 网络中同时部署外置PCEF与内置PCEF时，若采用外置PCEF计费，内置PCEF上不建议部署HTTP头增强。头增强插入信息改变报文长度，导致外置PCEF计费有误差。建议头增强与计费部署在同一网元，或内置PCEF计费+外置PCEF部署头增强 |
| 6 | 协议版本 | 本特性**只支持HTTP1.x协议，不支持HTTP2.0协议** |
| 7 | 加密场景计费 | 本特性不支持加密场景基于host的计费和控制 |
| 8 | HTTPS协议 | 本特性**不支持对HTTPS协议报文的处理**（HTTPS场景需使用 GWFD-110263 HTTPS头增强） |
| 9 | 拼接字段数量 | HTTP头增强最多支持插入**3个拼接字段**，每个拼接字段最多支持**4个参数拼接**（MULTIPARA，仅支持MSISDN、SGSNIP、MSIP作为拼接参数） |

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §应用限制；`约束限制和系统影响_12764478.md` §约束限制

### 1.10 特性规格

| 规格名称 | 规格指标 |
|----------|----------|
| 支持配置的 Header Enrichment 动作个数（整机） | 100 |

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §特性规格

### 1.11 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF | 2616 | Hypertext Transfer Protocol -- HTTP/1.1 |

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §遵循标准

### 1.12 计费与话单

由于业务处理时都是**先做计费再进行头增强处理**（与规则优先级无关），所以HTTP头增强特性对用户计费无影响，由UDG通过HTTP头增强特性插入的信息不会作为用户上网使用的业务量进行计费统计。

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §计费与话单

---

## 2. 激活（License开启命令）

> 本特性**必须先打开 License 配置开关**才能获得服务。激活即"License开关 + ADD HEADEN + ADD RULE(POLICYTYPE=HEADEN) + 绑定UserProfile"。

打开本特性的 License 配置开关：

```
SET LICENSESWITCH:LICITEM="LKV3G5HTHE01",SWITCH=ENABLE;
```

查询 License 开关状态：

```
LST LICENSESWITCH:LICITEM="LKV3G5HTHE01";
```

> SourcePath: `激活HTTP头增强_13649828.md` §任务示例
> SourcePath: `调测HTTP头增强_21598754.md` §操作步骤

---

## 3. 原理

### 3.1 动作机制：HEADEN —— 独立于PCC/SMARTREDIRECT的第4种POLICYTYPE

**核心结论**：HTTP头增强是 RULE 中 `POLICYTYPE=HEADEN` 的动作机制 —— RULE 通过 POLICYNAME 参数**直接引用** HEADEN（ADD HEADEN）对象，**不经过** PCCPOLICYGRP。这是访问限制场景中独立于 PCC（POLICYTYPE=PCC，轨道A三四层匹配+计费）和 SMARTREDIRECT（POLICYTYPE=SMARTREDIRECT，重定向）的第3种 POLICYTYPE，与 URL过滤（CFTEMPLATE/CONTCATEGBIND 独立动作）共同构成第4种轨道。

**POLICYTYPE四轨道并列关系**：

| POLICYTYPE | 动作对象（POLICYNAME引用） | 业务含义 | 典型特性 |
|------------|--------------------------|---------|---------|
| **PCC** | PCCPOLICYGRP（含URRGROUP计费组） | 三四层匹配 + 计费/带宽策略 | GWFD-020351 PCC基本功能 |
| **HEADEN** | HEADEN（ADD HEADEN / ADD TLSHEADEN） | **报文头增强**（插入用户字段） | **GWFD-110261/262/263（本族）** |
| **SMARTREDIRECT** | 重定向对象（如 HTTP智能重定向） | URL/HTTP层重定向 | GWFD-110284 |
| （URL过滤） | CFTEMPLATE / CONTCATEGBIND | URL内容过滤独立动作 | GWFD-110471 |

> SourcePath: `激活HTTP头增强_13649828.md` §表8（RULE POLICYTYPE=HEADEN + POLICYNAME=header_test）
> SourcePath: `调测HTTP头增强_21598754.md` §步骤6.b（LST RULE 输出 策略类型=Header Enrichment，策略名称=header_test，PCC策略组名称=NULL）

**头防欺诈内嵌于 HEADEN**：GWFD-110401 HTTP头防欺诈不独立配置策略对象，其开关内嵌于 `ADD HEADEN` 命令的 `ANTIFRAUD` 参数（ANTIFRAUD=ENABLE）；灰名单开关内嵌于 `GRAYLIST` 参数。详见 §3.6。

### 3.2 实现原理：HTTP报文头扩展字段插入

根据《RFC 2616: Hypertext Transfer Protocol -- HTTP/1.1》文档对HTTP协议的阐释，HTTP报文头中的**扩展字段是灵活可扩展的**。HTTP头增强特性的实现即在HTTP请求报文头中插入运营商规划的自定义字段内容。每一组字段都是按照 **`<字段前缀名称: 字段值>`** 的协议标准格式进行组织插入。

| 组成部分 | 数据来源 | 说明 |
|----------|----------|------|
| 字段前缀名称 | UDG上预先设定的配置（ADD HEADEN 的 PREFIXNAME 参数） | 按运营商需求灵活配置；**不能配置为HTTP标准头域名**（如 host、accept），否则可能防欺诈失效 |
| 字段值 | 业务访问用户的具体信息（ADD HEADEN 的 DATATYPE 映射本地保存的用户信息） | 用户相关信息实时插入；灵活可变 |

> SourcePath: `HTTP头增强原理_10865468.md` §组网架构、§头增强插入字段介绍

### 3.3 支持插入的字段（25类）

| 字段类型 | 字段值说明 | 加密 |
| --- | --- | --- |
| MSISDN | 用户激活时携带的MSISDN/GPSI（4G=MSISDN，5G=GPSI） | 支持 |
| IMSI | 用户激活时携带的IMSI/SUPI（4G=IMSI，5G=SUPI） | 支持 |
| IMEI | 国际移动设备标识/永久设备标识（IMEI/PEI）；**依赖SGSN/MME/S-GW/SMF是否携带**，不携带则无法插入 | 支持 |
| SGSN IP | SGSN/S-GW信令面IP地址（IPv4/IPv6）；只有4G接入用户才插入 | 支持 |
| SUBPROFILE | 华为PCRF/PCF开户存储的用户信息（如性别、年龄），通过Gx/N4私有信元Subscriber Profile下发 | 支持 |
| MS IP | 用户IP地址（IPv4/IPv6） | 支持 |
| APN | 用户激活时所属APN名称（真实APN或请求APN） | 支持 |
| Zone ID | HomeZone签约用户的当前HomeZone信息 | 不支持 |
| Billing Type | 用户相关计费属性信息 | 不支持 |
| CHGCHAR | 从SGSN/MME/SGW-C/SMF获取的用户计费属性 | 支持 |
| RAT | 用户接入网络类型 | 支持 |
| ULI | 用户接入位置信息（SAI/CGI（GPRS/UMTS）或ECGI/TAI（EPC）或EULF/NRLF（5GC）） | 支持 |
| CHGID | Charging ID | 不支持 |
| Roaming | 漫游属性（home/roaming/visiting） | 支持 |
| SGSN-MCC-MNC | 用户接入的SGSN/AMF所属的PLMN | 支持 |
| USERDEF | 运营商自定义字段（最多4个） | 不支持 |
| User-Profile-alias | user-profile别名，用户业务匹配到相应user-profile时插入，便于运营商了解user-profile使用情况（值来源于UDG本地配置） | 不支持 |
| MCC | 用户激活时携带的移动国家码 | 不支持 |
| MNC | 用户激活时携带的移动网络码 | 不支持 |
| SESSIONID | AAA服务器Access-Accept消息中Class字段 | 不支持 |
| GGSN IP | GGSN/P-GW/SMF信令面IP地址（IPv4/IPv6） | 支持 |
| TIMESTAMP | 时间戳 | 支持 |
| UPIPV4 | 用户面网关逻辑接口IPv4地址（优先级 Pa>Sa>N3>S1-U） | 支持 |
| UPIPV6 | 用户面网关逻辑接口IPv6地址（优先级 Pa>Sa>N3>S1-U） | 支持 |
| RANDNUM | 随机数，用于生成MD5/SHA256加密算法盐值 | 不支持 |
| MULTIPARA | 多参数拼接字段（仅支持MSISDN、SGSNIP、MSIP作为拼接参数；最多3个拼接字段，每个最多4参数） | 支持 |

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §原理概述 表1；`HTTP头增强原理_10865468.md` 表1

### 3.4 三种触发方式（基于IP / 基于URL / 基于HTTP协议）

UDG支持按如下三种方式使能HTTP头增强，差异在过滤条件配置：

| 触发方式 | 过滤条件配置 | FlowFilter配置 | 适用场景 |
|---------|------------|---------------|---------|
| **基于特定IP地址触发** | ADD FILTER（三四层）配置SVRIP/UE IP/端口；**不配置协议类型** | 仅绑定FILTER，不绑定协议 | 用户通过IP访问特定Web Server；由于不区分协议，**会同时对HTTP/RTSP/HTTPS报文做头增强** |
| **基于特定URL触发** | ADD L7FILTER 配置URL | PROTBINDFLOWF绑定 http 协议 + L7Filter | 用户通过URL访问特定Web Server；UDG按 PROTOCOLNAME 决定HTTP/RTSP/HTTPS头增强 |
| **基于HTTP协议触发** | 七层过滤，协议类型=http，**不配置L7Filter** | PROTBINDFLOWF绑定 http 协议，不绑L7Filter | 用户访问Web Server的报文为指定方法的HTTP报文 |

> **重要说明**：基于特定IP地址触发时，UDG的报文头增强处理只针对用户的HTTP/RTSP/HTTPS报文进行，当非HTTP/RTSP/HTTPS协议的业务流匹配到包含Header Enrichment动作的三四层规则时，**不会**进行HTTP/RTSP/HTTPS头增强的报文处理。

> SourcePath: `HTTP头增强原理_10865468.md` §触发条件

### 3.5 业务流程（HTTP GET报文示例，端到端）

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. 建立TCP连接                                                  │
│    MS/UE → Web Server，目的IP=Web Server IP                     │
│    PGW-U/UPF 允许TCP连接建立报文通过                             │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. MS/UE 发起HTTP业务，HTTP Get Request报文到达 PGW-U/UPF        │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. PGW-U/UPF 三步处理（关键）                                   │
│    a. SA：解析报文                                              │
│       - 识别服务器IP、URL、协议类型等关键特征                    │
│    b. Match：匹配规则                                           │
│       - 将解析到的报文特征与本地规则匹配                          │
│       - 命中规则后执行对应策略动作                                │
│    c. Action：执行规则                                          │
│       - 若命中头增强动作，提取 ADD HEADEN 配置的插入字段          │
│         及本地保存的用户信息                                     │
│       - 以 <字段前缀名称: 字段值> 格式插入HTTP Get Request报文头 │
│    （若开启防欺诈 ANTIFRAUD=ENABLE：先检测/纠正，再插入）         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. PGW-U/UPF 将添加头增强信息的HTTP Get Request 发送给Web Server │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. Web Server 处理                                              │
│    - 获取插入的增强内容，进行计费等操作                           │
│    - 获取当前用户信息，构造个性化请求响应报文                     │
│    - 返回 HTTP Response 给 PGW-U/UPF                            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. PGW-U/UPF 将 HTTP Response 转发给 MS/UE                      │
│    MS/UE 不感知 PGW-U/UPF 的头增强处理过程                       │
└─────────────────────────────────────────────────────────────────┘
```

> SourcePath: `HTTP头增强原理_10865468.md` §业务流程

### 3.6 安全机制（加密 + 编码）

#### 3.6.1 加密算法

HTTP头增强功能支持以下加密算法：

| 加密算法 | 说明 | 安全风险 |
|---------|------|---------|
| MD5 | 支持盐值加密（RANDNUM作盐） | **有风险，不建议使用** |
| RC4 | — | **有风险，不建议使用** |
| AES-128 | SET AES128 配置IV值（HEADENRANDOMIV=ENABLE支持随机IV） | 安全 |
| AES-256 | SET AES256 配置IV值（HEADENRANDOMIV=ENABLE支持随机IV） | 安全 |
| RSA-1024 | ADD RSA1024 配置公钥文件 | **有风险，不建议使用** |
| RSA-2048 | ADD RSA2048 配置公钥文件 | 安全 |
| SHA-256 | 支持盐值加密 | 安全 |

> **注意**：MD5、RC4、RSA-1024 有安全风险，不建议使用。建议使用安全的加密算法。

#### 3.6.2 编码方式（base64 / ASCII）

对端服务器具备base64或ASCII解码能力时，建议在UDG上对通过加密的头增强报文进行编码。两种配置方式：

- **方式一（继承式）**：ADD HEADEN `CIPHERTXTENCODE=INHERIT` → 通过 `SET BASE64` 开启base64编码，通过软参 `BIT475` 开启ASCII编码
- **方式二（命令内显式）**：ADD HEADEN `CIPHERTXTENCODE=BASE64` 开启base64编码，`CIPHERTXTENCODE=ASCII` 开启ASCII编码

> SourcePath: `HTTP头增强原理_10865468.md` §安全机制、表2；`GWFD-110261 HTTP头增强_62736942.md` §原理概述

### 3.7 与GWFD-110401 HTTP头防欺诈的强耦合关系

HTTP头防欺诈（GWFD-110401）**不独立配置策略对象**，其开关内嵌于 `ADD HEADEN` 命令的两个参数：

| 参数 | 取值 | 含义 |
|------|------|------|
| **ANTIFRAUD** | **ENABLE**（防欺诈核心开关） | 使能HTTP头防欺诈：在头增强插入前，先检测HTTP头中是否已存在该字段，若存在且取值不正确则纠正为本地保存的正确值；若存在多个则删除冗余 |
| GRAYLIST | ENABLE / DISABLE（默认） | ENABLE=灰名单模式：**只处理防欺诈，不插入头增强字段**；适用于"只防欺诈不需要头增强"的场景 |

**执行顺序**（BIT1030 控制）：防欺诈检测 → 字段纠正/冗余清理 → 头增强插入（灰名单模式下跳过插入）。

> SourcePath: `激活HTTP头增强_13649828.md` §表5（ADD HEADEN 含 GRAYLIST 说明）；`调测HTTP头增强_21598754.md` §步骤6.d（LST HEADEN 输出含"防欺诈标识"）

---

## 4. 配置

### 4.1 配置对象总览

本特性配置分为四大块：**License开关 + 过滤条件（三四层/七层）+ 头增强动作对象 + 业务规则+用户模板**。

#### 4.1.1 过滤条件配置对象（三种触发方式选用）

| 对象类型 | 命令 | 用途 |
|----------|------|------|
| FILTER | ADD FILTER | 三四层过滤条件（基于IP触发时配置：SVRIP/端口/协议） |
| FLOWFILTER | ADD FLOWFILTER | 流过滤器 |
| FLTBINDFLOWF | ADD FLTBINDFLOWF | 流过滤器的过滤器绑定关系 |
| L7FILTER | ADD L7FILTER | 七层过滤条件（URL + METHODTYPE，基于URL触发时配置） |
| PROTBINDFLOWF | ADD PROTBINDFLOWF | 流过滤器的协议绑定（PROTOCOLNAME=http + L7FILTERNAME） |
| WELLKNOWNPORT | ADD WELLKNOWNPORT | 知名端口识别HTTP协议（端口80/8080） |
| SIGNATUREDB | LOD SIGNATUREDB | 加载协议特征库（识别HTTP协议） |
| PARSERDB | LOD PARSERDB | 加载协议解析数据库 |
| REFRESHSRV | SET REFRESHSRV | 业务刷新（将新配置的Filter/L7Filter置为生效；系统默认60s后生效，可立即刷新） |

#### 4.1.2 头增强动作对象

| 对象类型 | 命令 | 用途 |
|----------|------|------|
| **HEADEN** | **ADD HEADEN** | **头增强对象（HTTP/RTSP用；HTTPS用 ADD TLSHEADEN）**。含插入字段DATATYPE、前缀PREFIXNAME、加密ENCRYALGORI、防欺诈ANTIFRAUD、灰名单GRAYLIST等参数 |

#### 4.1.3 业务规则与计费策略对象

| 对象类型 | 命令 | 用途 |
|----------|------|------|
| URR | ADD URR | 使用量上报规则（因头增强仅针对上行报文，需包含上行报文的计费属性） |
| URRGROUP | ADD URRGROUP | URR组 |
| PCCPOLICYGRP | ADD PCCPOLICYGRP | PCC策略组（绑定URRGROUP，用于计费规则） |
| RULE | ADD RULE | 业务规则（**POLICYTYPE=HEADEN** 引用头增强；POLICYTYPE=PCC 引用计费策略组） |
| USERPROFILE | ADD USERPROFILE | 用户模板（与SMF上的user-profile名称保持一致） |
| RULEBINDING | ADD RULEBINDING | 用户模板与规则绑定关系 |

> SourcePath: `激活HTTP头增强_13649828.md` §数据 表1~表10

### 4.2 配置流程

```
1. 打开License开关
   SET LICENSESWITCH（LKV3G5HTHE01）

2. 配置流过滤器
   ADD FLOWFILTER

3. 配置过滤条件（三选一或组合）
   ├─ 基于IP：ADD FILTER + ADD FLTBINDFLOWF + SET REFRESHSRV
   ├─ 基于URL：ADD L7FILTER + ADD PROTBINDFLOWF(PROTOCOLNAME=http) + SET REFRESHSRV
   └─ 基于HTTP协议：ADD PROTBINDFLOWF(PROTOCOLNAME=http，无L7FILTER) + SET REFRESHSRV

4. 配置协议识别（HTTPS场景必要，可选）
   ADD WELLKNOWNPORT（端口80/8080）+ LOD SIGNATUREDB + LOD PARSERDB

5. 配置头增强动作对象
   ADD HEADEN（HEADERENNAME + DATATYPE + PREFIXNAME + ENCRYALGORI）
   【多个字段多次执行该命令；防欺诈时设 ANTIFRAUD=ENABLE】

6. 配置计费属性和策略（因头增强针对上行报文，需上行计费）
   ADD URR + ADD URRGROUP + ADD PCCPOLICYGRP

7. 配置头增强规则（POLICYTYPE=HEADEN）
   ADD RULE（RULENAME + POLICYTYPE=HEADEN + FLOWFILTERNAME + POLICYNAME=header_test）

8. 配置计费规则（POLICYTYPE=PCC，可选，与头增强规则共用同一FLOWFILTER）
   ADD RULE（POLICYTYPE=PCC + PRIORITY + POLICYNAME=pg_test）

9. 配置业务策略组合
   ADD USERPROFILE + ADD RULEBINDING（绑定头增强规则和计费规则）
```

> SourcePath: `激活HTTP头增强_13649828.md` §操作流程

### 4.3 关键 MML 命令列表

#### 4.3.1 核心命令

| 命令 | 用途 |
|------|------|
| SET LICENSESWITCH | 打开License开关 |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FILTER | 增加三四层过滤器 |
| ADD FLTBINDFLOWF | 增加流过滤器的过滤器绑定关系 |
| ADD L7FILTER | 增加七层过滤器（URL + METHODTYPE） |
| ADD PROTBINDFLOWF | 增加流过滤器协议绑定关系（PROTOCOLNAME=http） |
| ADD WELLKNOWNPORT | 增加知名端口（识别HTTP协议端口80/8080） |
| LOD SIGNATUREDB | 加载协议特征库 |
| LOD PARSERDB | 加载协议解析数据库 |
| SET REFRESHSRV | 业务刷新（Filter/L7Filter生效） |
| **ADD HEADEN** | **增加头增强（HTTP头增强核心命令）** |
| ADD URR / ADD URRGROUP | 配置计费属性 |
| ADD PCCPOLICYGRP | 增加PCC策略组 |
| **ADD RULE** | **增加业务规则（POLICYTYPE=HEADEN 触发头增强）** |
| ADD USERPROFILE | 增加用户模板 |
| ADD RULEBINDING | 增加用户模板和规则的绑定关系 |

#### 4.3.2 辅助配置命令（加密算法相关 + 全局参数）

| 命令 | 用途 |
|------|------|
| SET AES128 / SET AES256 | 设置AES加密算法IV值（HEADENRANDOMIV=ENABLE支持随机IV） |
| ADD RSA1024 / ADD RSA2048 | 配置RSA加密使用的公钥文件（不建议使用RSA1024） |
| SET BASE64 | 设置base64编码规则 |
| SET HEADENGLBPARA | 设置头增强全局参数（如RC4加密前MD5加密开关 RC4KEYMD5EN） |
| SET HEADENRATTYPE | 设置头增强RAT类型定义（灵活定义RAT参数） |
| SET FLOWAGETIME | 设置业务流五元组老化时间 |
| SET SOFTPARA | 配置软参（如 BYTE896 控制头增强插入信息格式） |

> SourcePath: `GWFD-110261 HTTP头增强参考信息_79595496.md` §命令

### 4.4 关键参数说明

#### 4.4.1 ADD HEADEN 关键参数（HTTP头增强核心）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| HEADERENNAME | header_test | 头增强名称；**不能配置为HTTP标准头域名**（如accept、host），否则可能导致防欺诈失败 |
| DATATYPE | APN / IMSI1 / MSIP1 / MSISDN1 / IMEI1 / SGSNIP / GGSNIP / ULI / RAT / CHGCHAR / Roaming / USERDEF / TIMESTAMP / UPIPV4 / UPIPV6 / RANDNUM / MULTIPARA 等 | 数据类型（要插入的用户信息字段类型）；**若需在HTTP头部插入多种信息，需多次执行ADD HEADEN命令** |
| PREFIXNAME | pre-msisdn / X-imsi | HTTP头扩展字段前缀（非标准头域名） |
| ENCRYALGORI | NONE / MD5 / RC4 / AES128 / AES256 / RSA1024 / RSA2048 / SHA256 | 加密算法标识；建议使用安全的加密算法（MD5/RC4/RSA1024有风险） |
| CIPHERTXTENCODE | INHERIT / BASE64 / ASCII | 加密后编码方式；INHERIT需配合SET BASE64和BIT475软参 |
| PSWDKEY / PSWDKEYCONFIRM | （密码字符串） | 加密密钥（加密算法不为NONE时配置） |
| **ANTIFRAUD** | **ENABLE / DISABLE** | **防欺诈标识（GWFD-110401强耦合开关）**；ENABLE=使能HTTP头防欺诈 |
| GRAYLIST | ENABLE / DISABLE | 灰名单标识；ENABLE=只防欺诈不插入头增强字段 |
| RC4KEYMD5EN | INHERIT / ENABLE | RC4加密前是否做一次MD5加密（INHERIT需配合SET HEADENGLBPARA） |

> SourcePath: `激活HTTP头增强_13649828.md` §表5 头增强插入字段规划数据；`调测HTTP头增强_21598754.md` §步骤6.d（LST HEADEN 完整输出）

#### 4.4.2 ADD RULE 关键参数（POLICYTYPE=HEADEN）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| RULENAME | rule_test1 | 规则名称；存在多条数据时，该参数+策略类型不能完全相同 |
| **POLICYTYPE** | **HEADEN** | **策略类型=HEADEN 触发头增强业务（独立于PCC的第4种POLICYTYPE）** |
| FILTERINGMODE | FLOWFILTER | 流过滤器或流过滤器组选择（FLOWFILTER / FLOWFILTERGRP） |
| FLOWFILTERNAME | flowfilter_test | 流过滤器名称 |
| **POLICYNAME** | **header_test** | **策略名称（HEADEN对象名，由ADD HEADEN定义；直接引用，不经过PCCPOLICYGRP）** |

> SourcePath: `激活HTTP头增强_13649828.md` §表8 头增强规则规划数据

### 4.5 软参

| 软参 | 说明 |
|------|------|
| BYTE896 | 控制头增强插入信息格式（4G=IMSI/MSISDN/IMEI；4/5G融合+5G=GPSI/SUPI/PEI，仅对RAT=5G用户生效；4G用户接入5GC时按3GPP TS29.061格式插ULI） |
| BIT316 | 控制对特殊method是否开启SA信息增强解析功能（=0仅默认+配置；=1支持默认+配置+特殊） |
| BIT413 | 控制系统是否支持在一片报文的多个Method中插入头增强信息 |
| BIT475 | 控制头增强插入项加密后的值是否进行ASCII编码 |
| BIT569 | 控制是否开启对头域以"\r\n\r"结束的HTTP关键分片报文进行头增强处理 |
| BIT688 | 控制HTTP头增强针对报文分段场景是否开启防欺诈功能 |
| BIT735 | 控制系统头增强业务是否修改SACK |
| BIT861 | 控制解析头域时是否兼容支持把\n当做头域结束符 |
| BIT1006 | 控制是否对AES算法加密后的密文的校验位进行截断处理 |
| BIT1030 | 控制HTTP头防欺诈功能是否在头增强业务前执行 |
| BIT1307 | 控制头增强特性是否支持启用TCP SACK功能 |
| BYTE833 | 控制系统HTTP/TLS头增强报文分段不完整时的五元组老化时间 |
| BIT2517 | 控制AES CBC算法加密前明文的填充方式 |

> SourcePath: `GWFD-110261 HTTP头增强参考信息_79595496.md` §软参

---

## 5. 配置案例

### 5.1 场景一：基于URL触发 + 多字段插入（标准部署）

**场景描述**：运营商Web Server需要通过获取用户的APN、IMSI、MSIP、MSISDN给某些用户提供特殊定制业务。UDG将用户上行HTTP报文做头增强，采用基于特定URL触发方式，将APN/IMSI/MSIP/MSISDN字段插入用户报文携带给Web Server。

**MML命令序列（原样保留产品文档）**：

```
// 打开本特性的License配置开关。
SET LICENSESWITCH: LICITEM="LKV3G5HTHE01",SWITCH=ENABLE;

// 配置流过滤器。
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";

// 配置基于特定URL触发HTTP头增强，使用的七层过滤条件。
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_2",URL="www.example.com";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置知名端口识别HTTP协议。
ADD WELLKNOWNPORT:IDENPROTNAME="http_80",PROTOCOLNAME="http",PORTOP=EQUAL,STARTPORT=80,PRIORITY=2;
ADD WELLKNOWNPORT:IDENPROTNAME="http_8080",PROTOCOLNAME="http",PORTOP=EQUAL,STARTPORT=8080,PRIORITY=3;

// 配置报文特征库识别协议。
LOD SIGNATUREDB:LOADMODE=LATEST;
LOD PARSERDB:LOADMODE=LATEST;

// 配置HTTP头增强动作属性（4个字段，多次执行ADD HEADEN）。
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=APN,PREFIXNAME="pre-apn", ENCRYALGORI=NONE;
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=IMSI1,PREFIXNAME="pre-imsi",ENCRYALGORI=NONE;
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=MSIP1,PREFIXNAME="pre-msip",ENCRYALGORI=NONE;
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=MSISDN1,PREFIXNAME="pre-msisdn",ENCRYALGORI=NONE;

// 配置HTTP头增强使用的计费属性和策略。
ADD URR:URRNAME="urr01",URRID=1000,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="cp_test",UPURRNAME1="urr01",DOWNURRNAME1="urr01";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="cp_test";

// 配置HTTP头增强使用的规则（POLICYTYPE=HEADEN）。
ADD RULE:RULENAME="rule_test1",POLICYTYPE=HEADEN,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flowfilter_test",POLICYNAME="header_test";

// 配置计费规则（POLICYTYPE=PCC，与头增强规则共用同一FLOWFILTER）。
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flowfilter_test",PRIORITY=20, POLICYNAME="pg_test";

// 配置HTTP头增强使用的业务策略组合（规则与用户模板的绑定关系）。
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test1";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

> 来源：`激活HTTP头增强_13649828.md` §任务示例（脚本完整保留）

### 5.2 场景二：基于特定IP地址触发变体（三四层）

**场景描述**：采用基于特定IP地址触发，配置三四层过滤条件（Web Server IP + 端口）。**注意：此触发方式不区分协议，会同时对HTTP/RTSP/HTTPS报文做头增强**（仅对用户的HTTP/RTSP/HTTPS报文进行）。

**MML命令序列（相对场景一的差异部分）**：

```
// 配置基于特定IP地址触发HTTP头增强，使用的三四层过滤条件。
ADD FILTER: FILTERNAME="filter_test_80", L34PROTTYPE=STRING, L34PROTOCOL=TCP, SVRIPMODE=IP, SVRIP="10.10.10.10", SVRIPMASKTYPE=IPTYPE, SVRIPMASK="0.0.0.0", SVRSTARTPORT=80, SVRENDPORT=80;
ADD FILTER: FILTERNAME="filter_test_8080", L34PROTTYPE=STRING, L34PROTOCOL=TCP, SVRIPMODE=IP, SVRIP="10.10.10.10", SVRIPMASKTYPE=IPTYPE, SVRIPMASK="0.0.0.0", SVRSTARTPORT=8080, SVRENDPORT=8080;
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test_80";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test_8080";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 【基于IP触发时不配置L7FILTER/PROTBINDFLOWF】
```

> 来源：`激活HTTP头增强_13649828.md` §任务示例"三四层过滤条件"部分

### 5.3 场景三：基于HTTP协议触发变体（不配置URL）

**场景描述**：用户访问Web Server的报文为指定方法的HTTP报文即可触发。仅配置协议绑定，不配置L7Filter。

**MML命令序列（相对场景一的差异部分）**：

```
// 配置基于HTTP协议触发HTTP头增强（不配置L7FILTER，仅绑http协议）。
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="http";
SET REFRESHSRV:REFRESHTYPE=ALL;
```

> 来源：`激活HTTP头增强_13649828.md` §任务示例"七层过滤条件（HTTP协议）"部分

### 5.4 场景四：防欺诈 + 加密变体（ANTIFRAUD=ENABLE）

**场景描述**：在HTTP头增强同时启用头防欺诈，防止用户使用欺诈的MSISDN/IMSI等头增强信息。加密算法使用AES128。

**MML命令序列（ADD HEADEN 差异部分）**：

```
// 配置头增强对象，使能防欺诈（ANTIFRAUD=ENABLE），加密AES128。
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=IMSI1,PREFIXNAME="X-imsi",ENCRYALGORI=AES128,PSWDKEY="XXXXXX",PSWDKEYCONFIRM="XXXXXX",ANTIFRAUD=ENABLE;
```

> 说明：ANTIFRAUD=ENABLE 会同时启用 GWFD-110401 HTTP头防欺诈（需配套加载 LKV3G5HHAS01 License）。详见 GWFD-110401 文档。
> 来源：`激活HTTP头防欺诈_69815661.md` §任务示例（参考防欺诈激活配置）

### 5.5 场景五：灰名单模式变体（GRAYLIST=ENABLE）

**场景描述**：只进行防欺诈而不需要插入头增强字段的场景。适用于运营商仅需检测纠正已有的错误增强字段。

**MML命令序列（ADD HEADEN 差异部分）**：

```
// 灰名单模式：只防欺诈不插入头增强字段。
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=MSISDN1,PREFIXNAME="pre-msisdn",ENCRYALGORI=NONE,ANTIFRAUD=ENABLE,GRAYLIST=ENABLE;
```

> 来源：`激活HTTP头增强_13649828.md` §表5 说明（UDG支持头增强灰名单功能）

### 5.6 场景变体对照表

| 变体 | 核心差异命令 | 关键参数 | 适用场景 |
|------|------------|---------|---------|
| 基于URL触发（场景一） | ADD L7FILTER + ADD PROTBINDFLOWF | URL + PROTOCOLNAME=http | 按URL精确触发（主流） |
| 基于IP触发（场景二） | ADD FILTER + ADD FLTBINDFLOWF | SVRIP + 端口，不配协议 | 按IP触发；同时影响HTTP/RTSP/HTTPS |
| 基于HTTP协议（场景三） | ADD PROTBINDFLOWF | PROTOCOLNAME=http，无L7FILTER | 按协议触发，不区分URL |
| 防欺诈（场景四） | ADD HEADEN ANTIFRAUD=ENABLE | ANTIFRAUD=ENABLE + 加密 | 防欺诈+头增强（强耦合GWFD-110401） |
| 灰名单（场景五） | ADD HEADEN GRAYLIST=ENABLE | GRAYLIST=ENABLE | 只防欺诈不插入 |
| 多参数拼接 | ADD HEADEN DATATYPE=MULTIPARA | MULTIPARA（最多3字段×4参数） | 多用户信息拼接（20.10.0+） |
| 5G格式插入 | SET SOFTPARA BYTE896=1 | 仅对RAT=5G用户生效 | 4/5G融合场景GPSI/SUPI/PEI |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

当运营商需要部署HTTP头增强功能在用户的上行报文中增加IMSI、MSISDN、MSIP、APN等字段以传递用户的相关信息到Web Server时，需对HTTP头增强功能进行调测，确保本功能可以正常使用。

> 适用：PGW-U、UPF。本任务以GPRS/UMTS网络中调测HTTP头增强为例。

#### 6.1.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 用户信息 | 用户IMSI号（IMSI） | 123324423123195 | 测试终端自带 |
| 用户信息 | MSIP | 10.3.2.1 | 测试终端自带 |
| 用户信息 | MSISDN | 8615001336713 | 测试终端自带 |
| 测试终端使用的APN | APN名称（APN） | test-head-en | 与对端协商（与SMF上的APN名称保持一致） |
| 触发HTTP头增强的URL | URL | www.huawei.com | 已配置数据中获取（取自激活HTTP头增强中配置的URL） |

工具：测试终端、第三方抓包工具（UDG接入侧/PDN侧镜像接口）

> SourcePath: `调测HTTP头增强_21598754.md` §必备事项

#### 6.1.3 调测执行步骤

**步骤1**：执行 `LST LICENSESWITCH` 命令，查询License中是否允许使用HTTP头增强业务。

```
LST LICENSESWITCH:LICITEM="LKV3G5HTHE01";
```

预期输出：
```
......
-------------------------
       License项  =  LKV3G5HTHE01
     License名称  =  HTTP header enrichment
            开关  =  打开
(结果个数 = 1)
---    END
```

判断：
- License"开关"="打开" → 步骤2
- "关闭" → 打开License开关

**步骤2**：打开UDG接入侧/PDN侧镜像接口上的抓包工具，准备抓取测试终端的出入报文。

**步骤3**：测试终端使用 `test-head-en` APN接入网络。
- 成功接入 → 步骤4
- 无法接入 → 调测UDG的接入功能

**步骤4**：测试终端浏览Web业务，访问 `www.huawei.com` 网页，查看镜像接口的抓包信息。

判断：
- 测试终端可以正常浏览网页，**SGi/N6镜像接口抓包显示HTTP请求报文中插入了配置的头增强内容，且插入字段值正确** → HTTP头增强功能正常，调测结束
- 可以正常浏览网页，但SGi/N6镜像接口抓包显示**没有插入**配置的头增强内容，或**插入了但字段值有误** → 步骤5
- 无法浏览网页 → 调测UDG的Web浏览功能

> **抓包关键点**：S1-U/N3接口报文中**不携带**MSISDN/IMSI等用户信息（用户原始报文）；经UDG处理后，SGi/N6接口报文中**增加了**MSISDN/IMSI/MS IP/APN用户信息。当 ADD HEADEN 的"加密算法标识"不为"NONE"时，仅字段取值加密，字段名称不加密（例如 `msisdn:` 不加密，仅取值是加密后的字符串）。

**步骤5**：执行 `DSP SESSIONINFO` 命令，通过测试终端IMSI查看测试终端激活时使用的APN和用户模板。

```
DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="123324423123195";
```

判断：
- 测试终端使用的"IPv4 PDP address"/"IPv6 PDP address"、"MSISDN"、"APN name"与规划值一致 → 步骤6
- 不一致 → 参考"激活HTTP头增强"重新配置

**步骤6**：检查HTTP头增强业务相关配置是否正确（按6.1.4命令逐项核查）。

**步骤7**：收集信息并寻求技术支持。
- a. 在镜像接口或服务器上开启抓包工具，执行步骤3并保存报文
- b. 执行 `EXP MML` 命令将当前配置数据导出为MML脚本文件并保存
- c. 收集并保存上述所有查询信息
- d. 收集归纳所有信息并联系华为技术支持解决

> SourcePath: `调测HTTP头增强_21598754.md` §操作步骤

#### 6.1.4 配置验证命令与预期输出

**a. 查询用户模板和规则的绑定关系**：

```
LST RULEBINDING:USERPROFILENAME="up_test";
```

预期输出：
```
-------------------------
用户模板名称       规则名称      优先级         策略类型
up_test          rule_test1       65535          Header Enrichment
up_test          rule_test2       20             PCC
(结果个数 = 2)
---    END
```

**b. 查询规则配置（验证 POLICYTYPE=Header Enrichment）**：

```
LST RULE:RULENAME="rule_test1";
```

预期输出：
```
-------------------------
                 规则名称  =  rule_test1
                 策略类型  =  Header Enrichment
                        ......
             流过滤器名称  =  flowfilter_test
                        ......
               全局优先级  =  65535
            PCC策略组名称  =  NULL       ← HEADEN 不经过 PCCPOLICYGRP
             分类属性名称  =  NULL
                 策略名称  =  header_test    ← 直接引用 HEADEN 对象
                        ......
(结果个数 = 1)
---    END
```

**c. 查询协议绑定、过滤器、七层过滤器**：

```
LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test";
```
预期输出：协议名称=http，七层过滤器名字=l7filter_test。

```
LST L7FILTER:L7FILTERNAME="l7filter_test";
```
预期输出：方法类型=GET & POST & CONNECT。

**d. 查询头增强对象（验证防欺诈标识、加密算法）**：

```
LST HEADEN:HEADERENNAME="header_test";
```

预期输出：
```
---------------------------
               头增强名称  =  header_test
                 数据类型  =  IMSI1
                 前缀名称  =  pre-imsi
             用户自定义值  =  NULL
                 IMEI类型  =  IMEI
             加密算法标识  =  AES256
                     密码  =  *****
               防欺诈标识  =  不使能        ← 默认不使能；ANTIFRAUD=ENABLE时显示"使能"
                 头域长度  =  31
Charge Characteristic格式  =  十进制
            RSA2048公钥名称  =  NULL
                    ......
(结果个数 = 1)
--- END
```

**e. 查询知名端口与特征库加载状态**：

```
LST WELLKNOWNPORT:IDENPROTNAME="http_80";
```
预期输出：协议名称=http，起始端口号=80，优先级=2。

```
DSP SIGNATUREDB:;
```
预期输出：Signature Database Load Status = Load Finish，Engine Version = SA V300R009C10。

> SourcePath: `调测HTTP头增强_21598754.md` §步骤6、步骤7

### 6.2 验证命令汇总

| 命令 | 用途 |
|------|------|
| LST LICENSESWITCH | 查询License开关 |
| DSP SESSIONINFO | 显示用户上下文（IMSI/MSISDN/APN） |
| LST RULEBINDING | 查询用户模板和规则的绑定关系 |
| LST RULE | 查询规则（POLICYTYPE=Header Enrichment） |
| LST PROTBINDFLOWF | 查询协议绑定 |
| LST FILTER / LST FLTBINDFLOWF | 查询三四层过滤器及绑定 |
| LST L7FILTER | 查询七层过滤器（URL/METHODTYPE） |
| LST HEADEN | 查询头增强（数据类型/前缀/加密/防欺诈标识） |
| LST WELLKNOWNPORT | 查询知名端口（HTTP协议识别端口） |
| DSP SIGNATUREDB | 查询特征库加载状态 |
| EXP MML | 导出MML配置脚本（故障信息收集） |

> SourcePath: `调测HTTP头增强_21598754.md`

### 6.3 告警参考

**本特性无相关告警**（产品文档明确声明）。

> SourcePath: `GWFD-110261 HTTP头增强参考信息_79595496.md` §告警

### 6.4 测量指标

**本特性无相关测量指标**（产品文档明确声明）。

> SourcePath: `GWFD-110261 HTTP头增强参考信息_79595496.md` §测量指标

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 头增强字段未插入 | License开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5HTHE01";` 确认开关=打开（ENABLE） |
| 头增强字段未插入 | SA依赖未开启（SA-Basic/SA-Web Browsing License未开） | 检查SA协议族依赖License（见 §1.7）；`LST LICENSESWITCH:LICITEM="LKV3G5SABS01";` 等 |
| 头增强字段未插入 | 规则策略类型不是HEADEN | `LST RULE:RULENAME="rule_test1";` 确认 策略类型=Header Enrichment，策略名称=header_test（非PCC策略组） |
| 头增强字段未插入 | L7Filter/PROTBINDFLOWF未生效 | `LST PROTBINDFLOWF` 确认协议=http+L7FILTER；`SET REFRESHSRV:REFRESHTYPE=ALL;`（系统默认60s后生效，可立即刷新） |
| 头增强字段未插入 | 协议未识别（未配置WELLKNOWNPORT或特征库未加载） | `LST WELLKNOWNPORT` 确认HTTP端口80/8080；`DSP SIGNATUREDB` 确认 Load Finish |
| 头增强字段插入但值错误 | DATATYPE与本地保存的用户信息不匹配 | `DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="...";` 确认用户的MSISDN/IMSI/APN等与规划一致 |
| 头增强字段值未加密但配置了加密 | 字段名称不加密，仅字段取值加密（设计如此） | 抓包确认：例如 `msisdn:` 不加密，仅取值是加密后的字符串；属预期行为 |
| 防欺诈未生效 | ANTIFRAUD未置ENABLE 或 GRAYLIST与预期不符 | `LST HEADEN` 确认"防欺诈标识=使能"；确认 GWFD-110401 License LKV3G5HHAS01 已开 |
| HTTPS报文未做头增强 | 本特性不支持HTTPS（应用限制#8） | HTTPS场景需使用 GWFD-110263 HTTPS头增强（ADD TLSHEADEN） |
| IPv6业务无法访问 | 头增强字段过长导致报文超PMTU | 限制头增强字段长度；调整TCP MSS（建议 TCP MSS ≤ PMTU - 60B - 头增强字段长度） |
| 分片报文未做头增强 | UDG不对分片报文做头增强（应用限制#3/#4） | 调整网络设备MTU避免分片；属预期行为 |
| RTSP报文同时被头增强 | 基于IP触发时不区分协议（场景二） | 改用基于URL触发（场景一）；属预期行为（设计如此） |
| 外置PCEF计费有误差 | 头增强改变报文长度影响外置PCEF计费 | 头增强与计费部署在同一网元；或内置PCEF计费+外置PCEF部署头增强 |

---

## 7. 参考信息

### 7.1 与其他特性的关系（头增强协议族 + 依赖）

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| SA-Basic | GWFD-110101（UDG） | **强依赖**：UDG解析HTTP报文的基础，必须开启 |
| SA-Web Browsing | GWFD-110103（UDG） | **协议依赖**：HTTP/WAP2.0协议解析必需 |
| SA-Mobile | GWFD-110105（UDG） | **条件依赖**：HTTP承载业务（如MMS）解析必需 |
| HTTP头防欺诈 | GWFD-110401（UDG） | **强耦合**：防欺诈开关内嵌于 ADD HEADEN 的 ANTIFRAUD 参数；启用防欺诈必须开启头增强 |
| HTTPS头增强 | GWFD-110263（UDG） | **协议族兄弟**：HTTPS协议的对应实现（ADD TLSHEADEN，TLV格式） |
| RTSP头增强 | GWFD-110262（UDG） | **协议族兄弟**：RTSP协议的对应实现（ADD HEADEN，同HTTP字段格式） |
| NSH头增强 | （业务专题） | **协议族兄弟**：NSH协议的对应实现（独立License） |
| PCC基本功能 | GWFD-020351（UDG） | **配合关系**：头增强规则与计费规则（POLICYTYPE=PCC）可绑定同一UserProfile |
| 增强的ADC基本功能 | GWFD-020357（UDG） | **配合关系**：ADC检测是HTTP解析的前置能力，支撑头增强精确匹配 |
| HTTP智能重定向 | GWFD-110284（UDG） | **配合关系**：重定向执行机制与头增强共用SA解析层 |
| 用户Portal | GWFD-110281（UDG） | **配合关系**：Portal认证可依赖头增强插入的用户信息 |

> SourcePath: `GWFD-110261 HTTP头增强_62736942.md` §与其他特性的交互；`头增强功能之间的差异_10706790.md`

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110261 HTTP头增强_62736942.md` | 适用NF、定义、法律声明、客户价值、应用场景、可获得性（UDG 20.0.0+、License LKV3G5HTHE01）、与其他特性交互（SA-Basic/SA-Web Browsing/SA-Mobile）、对系统影响、应用限制（9条）、原理概述（25字段表、加密算法、编码方式）、特性规格（100动作）、遵循标准（3GPP 23.214/29.244、IETF 2616）、计费与话单、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTP头增强功能/GWFD-110261 HTTP头增强参考信息_79595496.md` | MML命令清单（16条）、告警（无）、软参（13个：BYTE896/BIT316/BIT413/BIT475/BIT569/BIT688/BIT735/BIT861/BIT1006/BIT1030/BIT1307/BYTE833/BIT2517）、测量指标（无） |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTP头增强功能/HTTP头增强原理描述/HTTP头增强原理_10865468.md` | 组网架构、头增强插入字段介绍（25字段含4G/5G映射说明）、业务流程（6步）、触发条件（基于IP/URL/HTTP协议3种）、安全机制（7加密算法+2编码方式） |
| 4 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTP头增强功能/HTTP头增强原理描述/约束限制和系统影响_12764478.md` | 约束限制（9条，含METHODTYPE/IPv6/MTU/分片/外置PCEF/协议版本/加密场景/HTTPS/拼接字段）、系统影响 |
| 5 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTP头增强功能/激活HTTP头增强_13649828.md` | 10步操作流程、数据规划表（License/流过滤器/三四层/七层/头增强字段/加密/计费/规则/UserProfile 共10张表）、完整MML脚本（License+FLOWFILTER+FILTER+L7FILTER+PROTBINDFLOWF+WELLKNOWNPORT+SIGNATUREDB+PARSERDB+HEADEN+URR+URRGROUP+PCCPOLICYGRP+RULE+USERPROFILE+RULEBINDING）、BYTE896软参5G格式插入说明 |
| 6 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/HTTP头增强功能/调测HTTP头增强_21598754.md` | 8步调测流程、LST LICENSESWITCH/DSP SESSIONINFO/LST RULEBINDING/LST RULE/LST PROTBINDFLOWF/LST FILTER/LST L7FILTER/LST HEADEN/LST WELLKNOWNPORT/DSP SIGNATUREDB预期输出样例、抓包验证点、EXP MML配置导出 |
| 7 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/头增强功能概述_04211022.md` | 头增强功能背景（带内in-band vs 带外out-band）、应用场景、价值、支持的协议类型（HTTP/HTTPS/RTSP） |
| 8 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/头增强功能之间的差异_10706790.md` | HTTP/HTTPS/RTSP头增强差异对照表（触发条件/支持协议/交互特性/业务/加密算法/编码/头防欺诈支持） |
| 9 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/特性映射_57402091.md` | 头增强协议族特性映射（GWFD-110261/262/263 → License项对应） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| Header Enrichment | 头增强 | 在HTTP/HTTPS/RTSP/NSH报文头扩展字段插入用户标识信息 |
| HEADEN | （策略类型） | RULE.POLICYTYPE=HEADEN，独立于PCC/SMARTREDIRECT的第4种动作机制 |
| TLV | Type-Length-Value | TLS协议的扩展字段组织格式（HTTPS头增强使用） |
| ANTIFRAUD | 防欺诈标识 | ADD HEADEN 参数，使能HTTP头防欺诈（内嵌GWFD-110401开关） |
| GRAYLIST | 灰名单标识 | ADD HEADEN 参数，ENABLE=只防欺诈不插入头增强 |
| MULTIPARA | 多参数拼接字段 | 头增强插入类型，支持MSISDN/SGSNIP/MSIP拼接（最多3字段×4参数） |
| SUBPROFILE | 用户签约属性 | 华为PCRF/PCF开户存储的用户信息，通过Gx/N4私有信元下发 |
| SNI | Server Name Indication | TLS握手时携带的目标域名（HTTPS头增强触发条件之一） |
| WAP GW | WAP Gateway | WAP网关；UDG可集成WAP GW部分功能（含头增强） |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树/文档清单仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致与笔误，供 Stage 3 横向分析参考。

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | feature_group 归属 | feature-doc-list 归为"头增强"组 | 产品文档路径在"智能策略控制功能"下；业务专题归"UDG头增强功能专题" | 一致（分组语义一致） |
| 2 | POLICYTYPE | 文档清单未明确策略类型 | 产品文档明确 **POLICYTYPE=HEADEN**（调测输出 策略类型=Header Enrichment，PCC策略组名称=NULL）→ HEADEN 是独立于 PCC 的动作机制 | 补全：HEADEN 是第4种POLICYTYPE（与PCC/SMARTREDIRECT/URL过滤并列） |
| 3 | 触发方式 | 文档清单未细化 | 产品文档明确 **3种触发方式**：基于特定IP地址/基于特定URL/基于HTTP协议；基于IP方式会同时影响HTTP/RTSP/HTTPS | 补全 |
| 4 | 协议族关系 | 文档清单未明确 | 业务专题"头增强功能之间的差异"明确 HTTP/HTTPS/RTSP 三协议头增强差异矩阵；HTTPS头增强也支持头防欺诈（差异表显示），RTSP不支持 | 补全：HTTPS防欺诈=支持，RTSP防欺诈=不支持 |
| 5 | 防欺诈位置 | 文档清单将GWFD-110401列为独立特性 | 产品文档明确 防欺诈开关**内嵌于 ADD HEADEN 的 ANTIFRAUD 参数**，不独立配置策略对象 | 补全：强耦合关系 |
| 6 | 加密算法 | 文档清单未列 | 产品文档明确 7种加密算法（MD5/RC4/AES-128/AES-256/RSA-1024/RSA-2048/SHA-256），MD5/RC4/RSA-1024有安全风险不建议使用 | 补全 |
| 7 | 软参数量 | 文档清单未列 | 参考信息列出 **13个软参**（BYTE896/BIT316/BIT413/BIT475/BIT569/BIT688/BIT735/BIT861/BIT1006/BIT1030/BIT1307/BYTE833/BIT2517） | 补全 |
| 8 | License编码差异 | 文档清单License编码 82209777 | 产品文档License控制项 `82209777 LKV3G5HTHE01 HTTP头增强`（编码82209777一致） | 一致 |
| 9 | 现有文档笔误 | （无） | 本次重读产品文档未发现明显笔误（9份文档MML脚本参数一致） | 无 |
| 10 | 5G支持 | 文档清单未明确 | 产品文档明确通过 BYTE896 软参支持5G格式（GPSI/SUPI/PEI），仅对RAT=5G用户生效；4G用户接入5GC时按3GPP TS29.061格式插ULI | 补全 |

---
