# GWFD-110262 RTSP头增强 知识文档

> 访问限制场景 | 头增强协议族（HTTP/HTTPS/RTSP/NSH）成员 | UDG | 来源：特性概述+实现原理+激活+参考信息+头增强功能专题 | 2026-06-22

---

## 0. 元数据（三层图谱Schema字段，对齐 §9.3）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110262 |
| feature_name | RTSP头增强 |
| feature_group | 头增强 |
| parent_feature_id | -（本特性在配置树无独立父节点；业务上归属"智能策略控制功能 → 头增强控制"分支；头增强协议族父概念见 `UDG头增强功能专题`） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["协议类型(RTSP，仅基于TCP；不支持RTSP over HTTP)", "插入字段(MSISDN/IMSI/IMEI/APN/MSIP/SGSNIP/GGSNIP/ULI/RAT/CHGCHAR/Roaming/USERDEF/User-Profile-alias/SESSIONID/TIMESTAMP/UPIPV4/UPIPV6/MULTIPARA/RANDNUM等，与HTTP头增强基本一致)", "RTSP请求类型(Setup/Play/Pause/Teardown/Options/Describe 6类)", "加密算法(NONE/MD5/RC4/AES-128/AES-256/RSA-1024/RSA-2048/SHA-256)", "编码方式(base64/ASCII/INHERIT)", "触发方式(基于特定IP地址/基于特定URL/基于RTSP协议)", "过滤层级(三四层FILTER vs 七层L7FILTER+PROTBINDFLOWF PROTOCOLNAME=rtsp)", "是否启用头防欺诈(不支持，与HTTP/HTTPS差异)", "灰名单模式(GRAYLIST=ENABLE只防欺诈不插入，但RTSP不支持防欺诈)", "POLICYTYPE=HEADEN（RULE直接引用HEADEN对象，独立于PCC/SMARTREDIRECT）"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-110262-01, EV-FK-AC-110262-02, EV-FK-AC-110262-03, EV-FK-AC-110262-04, EV-FK-AC-110262-05]（P4建evidence-index时确定，先用占位） |
| license_required | `82209778 LKV3G5RTHE01 RTSP头增强` |

---

## 1. 概述

### 1.1 特性定义（是什么）

RTSP（Real Time Streaming Protocol）头增强指对RTSP报文头的内容做增强处理，将用户信息（如APN、IMEI、MSISDN、IMSI等）中的一个或多个信息添加到RTSP报文头，并传递给流媒体服务器Streaming Server。运营商和服务提供商可基于这些信息灵活开展业务和实施控制，例如业务认证、广告宣传、业务推广和账户管理与查询。

**本质**：HTTP头增强的RTSP协议变体。实时流协议在语法和操作上与HTTP/1.1类似，因此RTSP的扩展机制与HTTP的扩展机制基本相同，均采用 `<字段前缀名称: 字段值>` 格式插入扩展字段。

> **法律声明（产品文档原文保留）**：RTSP头增强在RTSP报文头的扩展字段插入特定的用户标识信息，如IMSI/MSISDN/IP地址，存在将用户的个人身份信息泄露的风险。请遵循当地法律允许的目的和范围内启用相应的功能，以确保符合当地通信自由与个人隐私保护相关的法律要求。

> SourcePath: `UDG特性指南/智能策略控制功能/GWFD-110262 RTSP头增强_62388776.md` §定义、§说明
> SourcePath: `RTSP头增强原理_58245161.md` §组网架构（RTSP与HTTP扩展机制相同）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 对RTSP报文头做内容增强处理，将用户信息中的一个或多个添加到RTSP报文头并传递给Streaming Server |
| Streaming Server | 外部流媒体服务器 | 无特殊要求 | 支持对RTSP报文头中增强内容的解析和处理；根据具体用户信息为终端用户返回定制化页面，可用于广告宣传、账户查询、消费提醒、业务推广及业务认证等 |

**applicable_nf_map**（JSON）：
```json
{"UDG": ["PGW-U", "UPF"]}
```

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §可获得性

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 02 | 20.10.0 | 支持插入多参数拼接字段（MULTIPARA，最多3个拼接字段 × 每字段4参数） |
| 01 | 20.0.0 | 首次发布 |

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §发布历史

### 1.4 License

- **License控制项**：`82209778 LKV3G5RTHE01 RTSP头增强`
- 必须获得 License 许可后才能获得该特性的服务。

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §License支持

### 1.5 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 对用户流媒体业务进行认证，只允许签约用户访问专有业务；联合服务提供商进行广告宣传、业务推广等，从而获得相关收益 |
| 用户 | 接收个性化流媒体业务内容，享受专有服务；使用实时便捷的账户管理与查询功能 |

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §客户价值

### 1.6 应用场景

| 场景 | 描述 |
|------|------|
| 流媒体业务访问认证 | Streaming Server部署在数据通信网络中，无法得知用户信息；RTSP头增强将用户信息添加到RTSP报文头传递给Streaming Server，满足运营商针对用户做流媒体业务访问认证的需求 |
| 个性化流媒体服务 | Streaming Server根据用户属性信息向用户返回个性化管理与查询页面以及计费结算 |
| 视频业务定制 | 运营商需要为用户提供自营视频业务，Streaming Server通过头增强字段识别用户身份 |

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §应用场景；`头增强功能之间的差异_10706790.md`（业务=视频）

### 1.7 前置条件与依赖（SA协议族依赖）

| 关系类型 | 相关特性 | License 控制项 | 说明 |
|----------|------|----------------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 LKV3G5SABS01 SA-Basic | **必选**：UDG需对RTSP报文进行解析以执行头增强动作 |
| 依赖 | GWFD-110107 SA-Streaming | 82209759 LKV3G5SAST01 SA-Streaming | **必选**：RTSP流媒体协议解析依赖 |

> 说明：与HTTP/HTTPS头增强不同，RTSP头增强**仅需 SA-Basic + SA-Streaming** 两项SA依赖（HTTP头增强需SA-Basic+SA-Web Browsing+可选SA-Mobile；HTTPS头增强需额外HTTP2.0 Host识别）。

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §与其他特性的交互

### 1.8 对系统的影响

当在UDG上开启RTSP头增强特性后，由于匹配到头增强动作的用户**所有报文**，UDG都需要对其进行报文的解析和RTSP头增强处理，因此：
- 系统处理负荷增加
- 报文转发性能和吞吐量将下降

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §对系统的影响

### 1.9 应用限制

| # | 限制项 | 说明 |
|---|--------|------|
| 1 | IPv6分片 | IPv6报文不支持中间路由器分片，对IPv6报文做RTSP头增强需限制插入字段长度。建议 TCP MSS ≤ PMTU - IPv6首部(40B) - TCP首部(20B) - 头增强字段长度 |
| 2 | MTU过小分片 | 网络设备MTU过小，用户报文到达UDG前被分片，UDG**不对分片报文**进行头增强处理 |
| 3 | RTSP头域分片 | RTSP头域分片的请求报文不支持头增强功能 |
| 4 | 外置PCEF计费误差 | 网络中同时部署外置PCEF与内置PCEF时，若采用外置PCEF计费，内置PCEF上不建议部署RTSP头增强。建议头增强与计费部署在同一网元 |
| 5 | RTSP over HTTP | 用户所访问的流媒体服务器使用**RTSP over HTTP**协议时，UDG**不支持**对这类报文进行头增强处理 |
| 6 | 拼接字段数量 | RTSP头增强最多支持插入**3个拼接字段**，每个拼接字段最多支持**4个参数拼接**（MULTIPARA，仅支持MSISDN、SGSNIP、MSIP作为拼接参数） |

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §应用限制

### 1.10 特性规格

| 规格名称 | 规格指标 |
|----------|----------|
| 支持配置的 Header Enrichment 动作个数（整机） | 100 |

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §特性规格

### 1.11 遵循标准

**本特性不涉及标准约束**（产品文档明确声明，与HTTP/HTTPS头增强不同）。

> 说明：RTSP基于 IETF RFC 2326（RTSP协议），UDG仅支持基于TCP的RTSP。但产品文档"遵循标准"章节明确标注"本特性不涉及标准约束"。

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §遵循标准；`RTSP头增强原理_58245161.md` §RTSP协议栈（RFC 2326）

### 1.12 计费与话单

由于业务处理时都是**先做计费再进行头增强处理**（与规则优先级无关），所以RTSP头增强特性对用户计费无影响，由UDG通过RTSP头增强特性插入的信息不会作为用户上网使用的业务量进行计费统计。

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §计费与话单

---

## 2. 激活（License开启命令）

> 本特性**必须先打开 License 配置开关**才能获得服务。激活即"License开关 + ADD HEADEN + ADD RULE(POLICYTYPE=HEADEN) + 绑定UserProfile"。

打开本特性的 License 配置开关：

```
SET LICENSESWITCH:LICITEM="LKV3G5RTHE01",SWITCH=ENABLE;
```

查询 License 开关状态：

```
LST LICENSESWITCH:LICITEM="LKV3G5RTHE01";
```

> SourcePath: `激活RTSP头增强_60009655.md` §任务示例

---

## 3. 原理

### 3.1 动作机制：HEADEN —— 独立于PCC/SMARTREDIRECT的第4种POLICYTYPE

**核心结论**：RTSP头增强与HTTP头增强共享同一动作机制 —— RULE 中 `POLICYTYPE=HEADEN`，通过 POLICYNAME 参数**直接引用** HEADEN（ADD HEADEN）对象，**不经过** PCCPOLICYGRP。RTSP/HTTP头增强使用同一个 `ADD HEADEN` 命令（HTTPS头增强使用 `ADD TLSHEADEN`），区别仅在协议绑定（PROTBINDFLOWF 的 PROTOCOLNAME=rtsp）。

**POLICYTYPE四轨道并列关系**（与GWFD-110261一致）：

| POLICYTYPE | 动作对象（POLICYNAME引用） | 业务含义 | 典型特性 |
|------------|--------------------------|---------|---------|
| PCC | PCCPOLICYGRP（含URRGROUP计费组） | 三四层匹配 + 计费/带宽策略 | GWFD-020351 PCC基本功能 |
| **HEADEN** | HEADEN（ADD HEADEN / ADD TLSHEADEN） | **报文头增强** | **GWFD-110261/262/263（本族）** |
| SMARTREDIRECT | 重定向对象 | URL/HTTP层重定向 | GWFD-110284 |
| （URL过滤） | CFTEMPLATE / CONTCATEGBIND | URL内容过滤独立动作 | GWFD-110471 |

> SourcePath: `激活RTSP头增强_60009655.md` §表8（RULE POLICYTYPE=HEADEN + POLICYNAME=header_test）

### 3.2 RTSP协议基础（与HTTP的相似性）

#### 3.2.1 RTSP概念

- **RTSP（Real Time Streaming Protocol）**：实时流传输协议，是一种客户端/服务器应用级协议，用来控制数据的实时传输。RTSP是用来建立和控制一个或多个时间同步的连续音视频媒体流的会话协议。通过在客户端和服务器之间传递RTSP会话命令，可以完成请求播放、开始、暂停、查找、快进、快退等VCR（VideoCassette Recorder）控制操作。
- **RTSP协议栈**：IETF RFC 2326规定RTSP可以运行在TCP或UDP协议上，**UDG仅支持基于TCP的RTSP**。
- **RTSP请求格式**：与SIP协议格式类似，首行首先以方法名开始，然后是请求希望去的目的地址，接着是协议版本号：`<Method> <Request-URL> <RTSP-Version>`。

> SourcePath: `RTSP头增强原理_58245161.md` §RTSP概念

#### 3.2.2 UDG支持头增强处理的6类RTSP请求

| RTSP请求 | 含义 |
|---------|------|
| Setup | 客户端向服务器申请媒体流资源，并启动一个RTSP会话 |
| Play | 在Setup所启动会话并分配资源的某个流上开始数据传输 |
| Pause | 暂时停止一个流的数据传输而不释放服务器资源 |
| Teardown | 释放服务器上的流资源，结束RTSP会话 |
| Options | 服务器或客户端互相告知对方可以被接受的选项 |
| Describe | 客户端请求服务器返回媒体对象的描述 |

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §原理概述；`RTSP头增强原理_58245161.md` §RTSP概念

### 3.3 实现原理：RTSP报文头扩展字段插入

实时流协议在语法和操作上与HTTP/1.1类似，因此RTSP的扩展机制与HTTP的扩展机制基本相同。RTSP头增强在RTSP请求报文头中插入运营商规划的自定义字段内容，每一组字段按照 **`<字段前缀名称: 字段值>`** 格式组织插入。

| 组成部分 | 数据来源 | 说明 |
|----------|----------|------|
| 字段前缀名称 | UDG上预先设定的配置（ADD HEADEN 的 PREFIXNAME 参数） | 按运营商需求通过 ADD HEADEN 命令灵活配置 |
| 字段值 | 业务访问用户的具体信息（ADD HEADEN 的 DATATYPE 映射本地保存的用户信息） | 用户相关信息实时插入；灵活可变 |

> SourcePath: `RTSP头增强原理_58245161.md` §组网架构、§头增强支持插入字段概述

### 3.4 支持插入的字段（与HTTP头增强基本一致）

| 字段类型 | 字段值说明 | 加密 |
| --- | --- | --- |
| MSISDN | 用户激活时携带的MSISDN/GPSI | 支持 |
| IMSI | 用户激活时携带的IMSI/SUPI | 支持 |
| IMEI | 国际移动设备标识/永久设备标识（IMEI/PEI）；**依赖SGSN/MME/S-GW是否携带**，不携带则无法插入（**注意：RTSP为4G字段描述，无SMF**） | 支持 |
| SGSN IP | SGSN/S-GW信令面IP地址（IPv4/IPv6） | 支持 |
| SUBPROFILE | 华为PCRF/PCF开户存储的用户信息 | 支持 |
| MS IP | 用户IP地址（IPv4/IPv6） | 支持 |
| APN | 用户激活时所属APN名称（真实APN或请求APN） | 支持 |
| Zone ID | HomeZone签约用户的当前HomeZone信息 | 不支持 |
| Billing Type | 用户相关计费属性信息 | 不支持 |
| CHGCHAR | 从SGSN/MME/SGW-C/SMF获取的用户计费属性 | 支持 |
| RAT | 用户接入网络类型 | 支持 |
| ULI | 用户接入位置信息（SAI/CGI（GPRS/UMTS）或ECGI/TAI（EPC）） | 支持 |
| CHGID | Charging ID | 不支持 |
| Roaming | 漫游属性（home/roaming/visiting） | 支持 |
| SGSN-MCC-MNC | 用户接入的SGSN所属的PLMN（**注意：RTSP为SGSN，无AMF**） | 支持 |
| USERDEF | 运营商自定义字段（最多4个） | 不支持 |
| User-Profile-alias | user-profile别名 | 不支持 |
| MCC | 用户激活时携带的移动国家码 | 不支持 |
| MNC | 用户激活时携带的移动网络码 | 不支持 |
| SESSIONID | AAA服务器Access-Accept消息中Class字段 | 不支持 |
| GGSN IP | GGSN/P-GW信令面IP地址（IPv4/IPv6）（**注意：RTSP为GGSN/P-GW，无SMF**） | 支持 |
| TIMESTAMP | 时间戳 | 支持 |
| UPIPV4 | 用户面网关逻辑接口IPv4地址（优先级 Pa>Sa>N3>S1-U） | 支持 |
| UPIPV6 | 用户面网关逻辑接口IPv6地址（优先级 Pa>Sa>N3>S1-U） | 支持 |
| RANDNUM | 随机数，用于生成MD5/SHA256加密算法盐值 | 不支持 |
| MULTIPARA | 多参数拼接字段（仅支持MSISDN、SGSNIP、MSIP作为拼接参数） | 支持 |

> **与HTTP/HTTPS头增强差异**：RTSP头增强字段描述中 SGSN IP/SGSN-MCC-MNC/GGSN IP 仅提"SGSN/S-GW"和"GGSN/P-GW"，未提"AMF/SMF"（HTTP/HTTPS头增强同时提"SGSN/AMF"和"GGSN/P-GW/SMF"）。ULI 字段 RTSP 仅描述"SAI/CGI/ECGI/TAI"，未提"5GC的EULF/NRLF"。

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §原理概述 表1；`RTSP头增强原理_58245161.md` 表1

### 3.5 三种触发方式（与HTTP头增强一致，协议绑定不同）

| 触发方式 | 过滤条件配置 | FlowFilter配置 | 适用场景 |
|---------|------------|---------------|---------|
| **基于特定IP地址触发** | ADD FILTER（三四层）配置Streaming Server IP/端口；**不配置协议类型** | 仅绑定FILTER，不绑定协议 | 用户通过IP访问特定Streaming Server；**会同时对HTTP/RTSP/HTTPS报文做头增强** |
| **基于特定URL触发** | ADD L7FILTER 配置URL | PROTBINDFLOWF绑定 **rtsp** 协议 + L7Filter | 用户通过URL访问特定Streaming Server |
| **基于RTSP协议触发** | 七层过滤，协议类型=rtsp，**不配置L7Filter** | PROTBINDFLOWF绑定 **rtsp** 协议，不绑L7Filter | 用户访问Streaming Server的RTSP报文触发 |

> **关键差异**：RTSP头增强的 PROTBINDFLOWF 的 PROTOCOLNAME=**rtsp**（HTTP头增强=http，HTTPS头增强=https）；WELLKNOWNPORT 配置端口554（RTSP默认端口）。

### 3.6 安全机制（加密 + 编码）

与HTTP头增强一致：
- **加密算法**：MD5、RC4、AES-128、AES-256、RSA-1024、RSA-2048、SHA-256（MD5/SHA256支持盐值加密；MD5/RC4/RSA-1024有安全风险不建议使用）
- **编码方式**：base64编码（SET BASE64 或 ADD HEADEN CIPHERTXTENCODE=BASE64）、ASCII编码（BIT475软参 或 CIPHERTXTENCODE=ASCII）

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §原理概述

### 3.7 与HTTP头增强的关键差异（防欺诈不支持）

**RTSP头增强不支持头防欺诈**（与HTTP/HTTPS头增强的关键差异）。根据头增强功能差异表：

| 头防欺诈支持 | HTTP头增强 | HTTPS头增强 | **RTSP头增强** |
|------------|-----------|-------------|---------------|
| 支持 | ✅ | ✅ | **❌ 不支持** |

> 说明：虽然 ADD HEADEN 命令本身含 ANTIFRAUD 参数（RTSP与HTTP共用ADD HEADEN命令），但根据头增强功能差异表，RTSP头增强不支持头防欺诈功能。这与RTSP主要用于流媒体控制（非Web计费/认证）的业务场景一致。

> SourcePath: `头增强功能之间的差异_10706790.md` §头防欺诈行

---

## 4. 配置

### 4.1 配置对象总览

RTSP头增强的配置对象与HTTP头增强基本一致（详见 GWFD-110261 §4.1），差异仅在协议绑定参数。关键对象：

| 对象类型 | 命令 | RTSP场景差异 |
|----------|------|------|
| FILTER | ADD FILTER | Streaming Server IP（如 10.10.10.10/11） |
| FLOWFILTER | ADD FLOWFILTER | — |
| FLTBINDFLOWF | ADD FLTBINDFLOWF | — |
| L7FILTER | ADD L7FILTER | URL |
| **PROTBINDFLOWF** | ADD PROTBINDFLOWF | **PROTOCOLNAME=rtsp**（关键差异） |
| WELLKNOWNPORT | ADD WELLKNOWNPORT | **端口554**（RTSP默认端口；HTTP为80/8080） |
| SIGNATUREDB | LOD SIGNATUREDB | — |
| PARSERDB | LOD PARSERDB | — |
| **HEADEN** | **ADD HEADEN** | **与HTTP头增强共用同一命令** |
| URR / URRGROUP | ADD URR / ADD URRGROUP | — |
| PCCPOLICYGRP | ADD PCCPOLICYGRP | — |
| RULE | ADD RULE | **POLICYTYPE=HEADEN** |
| USERPROFILE | ADD USERPROFILE | — |
| RULEBINDING | ADD RULEBINDING | — |

### 4.2 配置流程

```
1. 打开License开关
   SET LICENSESWITCH（LKV3G5RTHE01）

2. 配置流过滤器
   ADD FLOWFILTER

3. 配置过滤条件（三选一或组合）
   ├─ 基于IP：ADD FILTER + ADD FLTBINDFLOWF + SET REFRESHSRV
   ├─ 基于URL：ADD L7FILTER + ADD PROTBINDFLOWF(PROTOCOLNAME=rtsp) + SET REFRESHSRV
   └─ 基于RTSP协议：ADD PROTBINDFLOWF(PROTOCOLNAME=rtsp，无L7FILTER) + SET REFRESHSRV

4. 配置协议识别
   ADD WELLKNOWNPORT（端口554，PROTOCOLNAME=rtsp）+ LOD SIGNATUREDB + LOD PARSERDB

5. 配置头增强动作对象（与HTTP共用ADD HEADEN）
   ADD HEADEN（HEADERENNAME + DATATYPE + PREFIXNAME + ENCRYALGORI）

6. 配置计费属性和策略
   ADD URR + ADD URRGROUP + ADD PCCPOLICYGRP

7. 配置头增强规则（POLICYTYPE=HEADEN）
   ADD RULE（POLICYTYPE=HEADEN + FLOWFILTERNAME + POLICYNAME=header_test）

8. 配置计费规则（POLICYTYPE=PCC，可选）
   ADD RULE（POLICYTYPE=PCC + PRIORITY + POLICYNAME=pg_test）

9. 配置业务策略组合
   ADD USERPROFILE + ADD RULEBINDING
```

> SourcePath: `激活RTSP头增强_60009655.md` §操作流程

### 4.3 关键 MML 命令列表

| 命令 | 用途 |
|------|------|
| SET LICENSESWITCH | 打开License开关（LKV3G5RTHE01） |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FILTER | 增加三四层过滤器（Streaming Server IP） |
| ADD FLTBINDFLOWF | 增加流过滤器的过滤器绑定关系 |
| ADD L7FILTER | 增加七层过滤器（URL） |
| **ADD PROTBINDFLOWF** | **增加流过滤器协议绑定关系（PROTOCOLNAME=rtsp，RTSP关键差异）** |
| ADD WELLKNOWNPORT | 增加知名端口（端口554，PROTOCOLNAME=rtsp） |
| LOD SIGNATUREDB | 加载协议特征库 |
| LOD PARSERDB | 加载协议解析数据库 |
| SET REFRESHSRV | 业务刷新 |
| **ADD HEADEN** | **增加头增强（RTSP与HTTP共用同一命令）** |
| ADD URR / ADD URRGROUP | 配置计费属性 |
| ADD PCCPOLICYGRP | 增加PCC策略组 |
| **ADD RULE** | **增加业务规则（POLICYTYPE=HEADEN）** |
| ADD USERPROFILE | 增加用户模板 |
| ADD RULEBINDING | 增加用户模板和规则的绑定关系 |

> SourcePath: `GWFD-110262 RTSP头增强参考信息_79595497.md` §命令

### 4.4 关键参数说明

#### 4.4.1 ADD HEADEN 关键参数（与HTTP头增强一致）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| HEADERENNAME | header_test | 头增强名称（RTSP与HTTP共用） |
| DATATYPE | APN / IMSI1 / MSIP1 / MSISDN1 等 | 数据类型；**多个字段需多次执行ADD HEADEN** |
| PREFIXNAME | pre-msisdn | RTSP头扩展字段前缀 |
| ENCRYALGORI | NONE / MD5 / AES128 / AES256 / SHA256 等 | 加密算法标识 |
| GRAYLIST | ENABLE / DISABLE | 灰名单标识（ENABLE=只防欺诈不插入；但RTSP不支持防欺诈，此参数在RTSP场景实际无效） |

> SourcePath: `激活RTSP头增强_60009655.md` §表5 头增强插入字段规划数据

#### 4.4.2 ADD WELLKNOWNPORT 关键参数（RTSP协议识别）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| IDENPROTNAME | rtsp_554 | 知名端口名称 |
| **PROTOCOLNAME** | **rtsp** | **协议名称（RTSP关键差异）** |
| PORTOP | EQUAL | 端口范围操作码 |
| STARTPORT | 554 | 起始端口号（RTSP默认端口） |
| PRIORITY | 5 | 优先级（越小越高） |

### 4.5 软参

| 软参 | 说明 |
|------|------|
| BIT2517 | 控制AES CBC算法加密前明文的填充方式 |

> 说明：RTSP头增强参考信息仅列出1个软参（BIT2517），明显少于HTTP头增强的13个软参（RTSP头增强共享HTTP头增强的大部分软参，但参考信息文档仅显式列出BIT2517）。

> SourcePath: `GWFD-110262 RTSP头增强参考信息_79595497.md` §软参

---

## 5. 配置案例

### 5.1 场景一：基于URL触发 + 多字段插入（标准部署）

**场景描述**：运营商Streaming Server需要通过获取用户的APN、IMSI、MSIP、MSISDN给某些用户提供特殊定制业务。UDG将用户上行RTSP报文做头增强，采用基于特定IP地址、基于特定URL或RTSP协议的触发方式，将APN/IMSI/MSIP/MSISDN字段插入用户报文携带给Streaming Server。

**MML命令序列（原样保留产品文档）**：

```
// 打开本特性的License配置开关。
SET LICENSESWITCH: LICITEM="LKV3G5RTHE01",SWITCH=ENABLE;

// 配置流过滤器。
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";

// 配置基于特定IP地址触发RTSP头增强，使用的三四层过滤条件。
ADD FILTER: FILTERNAME="filter_test1", L34PROTTYPE=STRING, L34PROTOCOL=TCP, SVRIPMODE=IP, SVRIP="10.10.10.10", SVRIPMASKTYPE=IPTYPE, SVRIPMASK="0.0.0.0", SVRSTARTPORT=0, SVRENDPORT=65535;
ADD FILTER: FILTERNAME="filter_test2", L34PROTTYPE=STRING, L34PROTOCOL=TCP, SVRIPMODE=IP, SVRIP="10.10.10.11", SVRIPMASKTYPE=IPTYPE, SVRIPMASK="0.0.0.0", SVRSTARTPORT=0, SVRENDPORT=65535;
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test2";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置基于特定URL和RTSP协议触发RTSP头增强，使用七层过滤条件。
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_2",URL="www.example.com";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="rtsp",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置知名端口识别RTSP协议。
ADD WELLKNOWNPORT:IDENPROTNAME="rtsp_554",PROTOCOLNAME="rtsp",PORTOP=EQUAL,STARTPORT=554,PRIORITY=5;

// 通过报文特征库识别协议。
LOD SIGNATUREDB:LOADMODE=LATEST;
LOD PARSERDB:LOADMODE=LATEST;

// 配置RTSP头增强动作属性（4个字段，多次执行ADD HEADEN）。
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=APN,PREFIXNAME="pre-apn", ENCRYALGORI=NONE;
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=IMSI1,PREFIXNAME="pre-imsi",ENCRYALGORI=NONE;
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=MSIP1,PREFIXNAME="pre-msip",ENCRYALGORI=NONE;
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=MSISDN1,PREFIXNAME="pre-msisdn",ENCRYALGORI=NONE;

// 配置RTSP头增强使用的计费属性。
ADD URR:URRNAME="urr01",URRID=1000,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="cp_test",UPURRNAME1="urr01",DOWNURRNAME1="urr01";

// 配置RTSP头增强使用的PCC动作策略组。
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="cp_test";

// 配置RTSP头增强使用的规则（POLICYTYPE=HEADEN）。
ADD RULE:RULENAME="rule_test1",POLICYTYPE=HEADEN,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flowfilter_test",POLICYNAME="header_test";

// 配置计费规则（POLICYTYPE=PCC，与头增强规则共用同一FLOWFILTER）。
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flowfilter_test",PRIORITY=20, POLICYNAME="pg_test";

// 配置RTSP头增强使用的业务策略组合（规则与用户模板的绑定关系）。
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test1";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

> 来源：`激活RTSP头增强_60009655.md` §任务示例（脚本完整保留）

### 5.2 场景二：基于RTSP协议触发变体（不配置URL）

**场景描述**：仅配置协议绑定（PROTOCOLNAME=rtsp），不配置L7Filter。所有RTSP报文触发头增强。

**MML命令序列（相对场景一的差异部分）**：

```
// 配置基于RTSP协议触发RTSP头增强（不配置L7FILTER，仅绑rtsp协议）。
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="rtsp";
SET REFRESHSRV:REFRESHTYPE=ALL;
```

> 来源：`激活RTSP头增强_60009655.md` §任务示例"七层过滤条件（RTSP协议）"部分

### 5.3 场景变体对照表

| 变体 | 核心差异命令 | 关键参数 | 适用场景 |
|------|------------|---------|---------|
| 基于URL触发（场景一） | ADD L7FILTER + ADD PROTBINDFLOWF | URL + PROTOCOLNAME=rtsp | 按URL精确触发 |
| 基于IP触发 | ADD FILTER + ADD FLTBINDFLOWF | Streaming Server IP + 端口0-65535 | 按IP触发；同时影响HTTP/RTSP/HTTPS |
| 基于RTSP协议（场景二） | ADD PROTBINDFLOWF | PROTOCOLNAME=rtsp，无L7FILTER | 按协议触发，不区分URL |
| 多参数拼接 | ADD HEADEN DATATYPE=MULTIPARA | MULTIPARA（最多3字段×4参数） | 多用户信息拼接（20.10.0+） |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

当运营商需要部署RTSP头增强功能时，需对RTSP头增强功能进行调测，确保本功能可以正常使用。

> 适用：PGW-U、UPF。

#### 6.1.2 调测执行步骤（参照HTTP头增强调测流程）

RTSP头增强的调测流程与HTTP头增强基本一致（产品文档调测文档未单独给出RTSP预期输出样例，参照HTTP头增强调测结构）：

1. **查询License开关**：`LST LICENSESWITCH:LICITEM="LKV3G5RTHE01";` 确认开关=打开
2. **打开UDG接入侧/PDN侧镜像接口抓包工具**
3. **测试终端接入网络**：使用规划APN接入
4. **测试终端访问流媒体业务**：访问规划的RTSP URL，查看镜像接口抓包信息
   - SGi/N6镜像接口抓包显示RTSP请求报文中插入了配置的头增强内容，且插入字段值正确 → RTSP头增强功能正常
   - 未插入或字段值有误 → 步骤5
   - 无法访问流媒体 → 调测UDG的流媒体功能（GWFD-110107 SA-Streaming）
5. **查询用户上下文**：`DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="...";` 确认用户MSISDN/IMSI/APN
6. **检查RTSP头增强配置**（见6.1.3）
7. **收集信息并寻求技术支持**：镜像抓包 + `EXP MML` 导出配置 → 联系华为技术支持

> 说明：RTSP头增强调测文档未提供独立的预期输出样例，参照HTTP头增强调测（`调测HTTP头增强_21598754.md`）的输出格式。
> SourcePath: `调测HTTP头增强_21598754.md` §操作步骤（RTSP场景参照）

#### 6.1.3 配置验证命令

| 命令 | 用途 | 验证点 |
|------|------|--------|
| LST LICENSESWITCH | 查询License开关 | LICITEM=LKV3G5RTHE01 是否 打开 |
| DSP SESSIONINFO | 显示用户上下文 | IMSI/MSISDN/APN 与规划值一致 |
| LST RULEBINDING | 查询规则绑定 | 规则名称=rule_test1，策略类型=Header Enrichment |
| LST RULE | 查询规则 | POLICYTYPE=HEADEN，策略名称=header_test，PCC策略组名称=NULL |
| LST PROTBINDFLOWF | 查询协议绑定 | **协议名称=rtsp**（RTSP关键差异），七层过滤器名字=l7filter_test |
| LST FILTER / LST FLTBINDFLOWF | 查询过滤器 | Streaming Server IP、端口 |
| LST L7FILTER | 查询七层过滤器 | URL |
| LST HEADEN | 查询头增强 | 数据类型、前缀名称、加密算法标识 |
| LST WELLKNOWNPORT | 查询知名端口 | **协议名称=rtsp，端口554** |
| DSP SIGNATUREDB | 查询特征库加载状态 | Load Finish |
| EXP MML | 导出MML配置脚本 | 故障信息收集 |

### 6.2 告警参考

**本特性无相关告警**（产品文档明确声明）。

> SourcePath: `GWFD-110262 RTSP头增强参考信息_79595497.md` §告警

### 6.3 测量指标

**本特性无相关测量指标**（产品文档明确声明）。

> SourcePath: `GWFD-110262 RTSP头增强参考信息_79595497.md` §测量指标

### 6.4 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| RTSP头增强字段未插入 | License开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5RTHE01";` 确认开关=打开 |
| RTSP头增强字段未插入 | SA依赖未开启（SA-Basic/SA-Streaming License未开） | 检查SA协议族依赖License（见 §1.7）；`LST LICENSESWITCH:LICITEM="LKV3G5SABS01";` 和 `LKV3G5SAST01` |
| RTSP头增强字段未插入 | 协议绑定错误（PROTOCOLNAME不是rtsp） | `LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test";` 确认协议名称=rtsp |
| RTSP头增强字段未插入 | RTSP协议未识别（未配置WELLKNOWNPORT或特征库未加载） | `LST WELLKNOWNPORT` 确认RTSP端口554；`DSP SIGNATUREDB` 确认 Load Finish |
| RTSP头增强字段未插入 | 规则策略类型不是HEADEN | `LST RULE:RULENAME="rule_test1";` 确认策略类型=Header Enrichment，策略名称=header_test |
| RTSP over HTTP报文未做头增强 | RTSP over HTTP不支持（应用限制#5） | 属预期行为；UDG不支持RTSP over HTTP报文的头增强 |
| UDP上的RTSP报文未做头增强 | UDG仅支持基于TCP的RTSP（RTSP协议栈限制） | 属预期行为；UDG不支持基于UDP的RTSP |
| 头增强字段未插入但规则配置正确 | RTSP请求类型不在支持的6类内 | 确认RTSP请求为 Setup/Play/Pause/Teardown/Options/Describe 之一 |
| IPv6流媒体无法访问 | 头增强字段过长导致报文超PMTU | 限制头增强字段长度；调整TCP MSS（建议 TCP MSS ≤ PMTU - 60B - 头增强字段长度） |
| 分片报文未做头增强 | UDG不对分片报文做头增强（应用限制#2/#3） | 调整网络设备MTU避免分片；属预期行为 |
| HTTP报文同时被RTSP头增强 | 基于IP触发时不区分协议 | 改用基于URL触发；属预期行为（设计如此） |
| 防欺诈未生效 | RTSP头增强不支持防欺诈（差异点） | 属预期行为；防欺诈仅HTTP/HTTPS头增强支持 |

---

## 7. 参考信息

### 7.1 与其他特性的关系（头增强协议族 + 依赖）

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| SA-Basic | GWFD-110101（UDG） | **强依赖**：UDG解析RTSP报文的基础，必须开启 |
| SA-Streaming | GWFD-110107（UDG） | **强依赖**：RTSP流媒体协议解析必需 |
| HTTP头增强 | GWFD-110261（UDG） | **协议族兄弟**：HTTP协议的对应实现（共用ADD HEADEN命令） |
| HTTPS头增强 | GWFD-110263（UDG） | **协议族兄弟**：HTTPS协议的对应实现（ADD TLSHEADEN） |
| NSH头增强 | （业务专题） | **协议族兄弟**：NSH协议的对应实现 |
| PCC基本功能 | GWFD-020351（UDG） | **配合关系**：头增强规则与计费规则可绑定同一UserProfile |
| 增强的ADC基本功能 | GWFD-020357（UDG） | **配合关系**：ADC检测是RTSP解析的前置能力 |
| HTTP智能重定向 | GWFD-110284（UDG） | **配合关系**：重定向执行机制共用SA解析层 |

> SourcePath: `GWFD-110262 RTSP头增强_62388776.md` §与其他特性的交互

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110262 RTSP头增强_62388776.md` | 适用NF、定义、法律声明、客户价值、应用场景、可获得性（UDG 20.0.0+、License LKV3G5RTHE01）、与其他特性交互（SA-Basic/SA-Streaming）、对系统影响、应用限制（6条）、原理概述（25字段表、RTSP与HTTP扩展机制相同、6类RTSP请求、加密算法、编码方式）、特性规格（100动作）、遵循标准（无）、计费与话单、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/RTSP头增强功能/GWFD-110262 RTSP头增强参考信息_79595497.md` | MML命令清单（15条）、告警（无）、软参（BIT2517）、测量指标（无） |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/RTSP头增强功能/RTSP头增强原理描述/RTSP头增强原理_58245161.md` | RTSP概念（协议栈、请求格式）、6类RTSP请求（Setup/Play/Pause/Teardown/Options/Describe）、组网架构、头增强支持插入字段（25字段）、业务流程、触发条件（基于IP/URL/RTSP协议3种）、安全机制 |
| 4 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/RTSP头增强功能/激活RTSP头增强_60009655.md` | 10步操作流程、数据规划表（10张表）、完整MML脚本（License+FLOWFILTER+FILTER+L7FILTER+PROTBINDFLOWF+WELLKNOWNPORT+SIGNATUREDB+PARSERDB+HEADEN+URR+URRGROUP+PCCPOLICYGRP+RULE+USERPROFILE+RULEBINDING）、BYTE896软参5G格式插入说明 |
| 5 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/头增强功能之间的差异_10706790.md` | HTTP/HTTPS/RTSP头增强差异对照表（触发条件/支持协议/交互特性/业务/加密算法/编码/头防欺诈支持） |
| 6 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG头增强功能专题/特性映射_57402091.md` | 头增强协议族特性映射（GWFD-110262 → License LKV3G5RTHE01） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| RTSP | Real Time Streaming Protocol | 实时流传输协议，控制音视频媒体流的会话协议 |
| Streaming Server | 流媒体服务器 | RTSP头增强的业务服务器（对应HTTP的Web Server） |
| VCR | VideoCassette Recorder | RTSP支持的VCR控制操作（播放/暂停/快进/快退等） |
| HEADEN | （策略类型） | RULE.POLICYTYPE=HEADEN，RTSP与HTTP共用 |
| SA-Streaming | Service Awareness-Streaming | 流媒体业务感知，RTSP解析依赖 |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树/文档清单仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致与笔误，供 Stage 3 横向分析参考。

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | feature_group 归属 | feature-doc-list 归为"头增强"组 | 产品文档路径在"智能策略控制功能"下；业务专题归"UDG头增强功能专题/RTSP头增强功能" | 一致（分组语义一致） |
| 2 | 头防欺诈支持 | feature-doc-list 未明确 | 头增强差异表明确 **RTSP头增强不支持头防欺诈**（HTTP/HTTPS支持） | 补全：RTSP不支持防欺诈（与HTTP/HTTPS的关键差异） |
| 3 | POLICYTYPE | 文档清单未明确策略类型 | 产品文档明确 **POLICYTYPE=HEADEN**（RTSP与HTTP共用ADD HEADEN命令） | 补全：RTSP头增强RULE策略类型同为HEADEN |
| 4 | 协议绑定参数 | 文档清单未明确 | 产品文档明确 PROTBINDFLOWF 的 PROTOCOLNAME=**rtsp**（HTTP=http，HTTPS=https） | 补全：RTSP关键差异 |
| 5 | 默认端口 | 文档清单未明确 | 产品文档明确 RTSP默认端口=**554**（WELLKNOWNPORT配置）；HTTP为80/8080；HTTPS为443 | 补全 |
| 6 | RTSP请求类型 | 文档清单未明确 | 产品文档明确 6类RTSP请求做头增强：Setup/Play/Pause/Teardown/Options/Describe | 补全 |
| 7 | RTSP over HTTP | 文档清单未明确 | 产品文档应用限制明确 **不支持RTSP over HTTP** | 补全 |
| 8 | 协议栈 | 文档清单未明确 | 产品文档明确 UDG仅支持**基于TCP的RTSP**（不支持UDP） | 补全 |
| 9 | 遵循标准 | 文档清单未列 | 产品文档明确"本特性**不涉及标准约束**"（与HTTP/HTTPS头增强列出标准不同） | 补全：RTSP头增强无标准约束声明 |
| 10 | 软参数量 | 文档清单未列 | 参考信息仅显式列出 **1个软参**（BIT2517），明显少于HTTP头增强的13个 | 补全：RTSP参考信息文档软参列出较少（实际共享HTTP头增强软参） |
| 11 | 字段5G映射 | 文档清单未明确 | RTSP头增强字段描述中 SGSN IP/SGSN-MCC-MNC/GGSN IP 仅提"SGSN/S-GW"和"GGSN/P-GW"（无AMF/SMF），ULI 仅"SAI/CGI/ECGI/TAI"（无5GC的EULF/NRLF）；与HTTP/HTTPS头增强（含AMF/SMF/EULF/NRLF）存在描述差异 | 补全：RTSP字段描述偏向4G |
| 12 | 现有文档笔误 | （无） | 本次重读产品文档未发现明显笔误（4份文档MML脚本参数一致） | 无 |

---
