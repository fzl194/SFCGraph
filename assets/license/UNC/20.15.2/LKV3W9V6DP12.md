---
id: UNC@20.15.2@License@LKV3W9V6DP12
type: License
name: IPv6 SA
nf: UNC
version: 20.15.2
license_code: LKV3W9V6DP12
control_item_id: '82207983'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# IPv6 SA

`LKV3W9V6DP12` · 控制项 82207983 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C、SMF

## 功能描述

IPv6 SA特性指通过对IPv6用户的上下行报文进行业务感知，判断访问内容，感知IPv6业务，对不同IPv6业务进行不同的计费和动作处理。本控制项控制IPv6 SA(每PDP)。

## 实现描述

IPv6 SA完成IPv6用户数据报文的解析、协议识别和内容识别，获得目的URL等有价值的信息，为带宽管理和安全防护等特性提供依据。<br>IPv6 SA的详细原理请参见SA-Basic功能描述，不同点在于以下几方面要支持IPv6：<br>- GGSN-C、SGW-C、PGW-C支持对IPv6用户报文进行L34过滤和解析，区分不同IPv6业务，对不同IPv6业务进行不同的计费和动作处理。L34层匹配主要是针对IP层和TCP/UDP传输层的特征进行匹配，所以L34层匹配与IP版本强相关。在IPv6的情况下，五元组中的ms-IP和server-IP应该都是IPv6格式，匹配时也应该只匹配IPv6 Filter。<br>- GGSN-C、SGW-C、PGW-C支持对IPv6用户报文进行L7过滤和解析，区分不同IPv6业务，对不同IPv6业务进行不同的计费和动作处理。L7层匹配则是对传输层以上的层的特征进行匹配。若HTTP/WAP等协议携带了URL信息，则GGSN-C、SGW-C、PGW-C识别这些协议之后，可能需要对URL进行解析和匹配才能区分出真正的业务。URL通常与IP版本无关的，但是其中可能存在文本形式的IP地址，比如Host字段，此时就要求GGSN-C、SGW-C、PGW-C能够支持解析该URL，区分不同IPv6业务，对不同IPv6业务进行策略控制。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

- IPv6 SA是一个基本的支撑功能，IPv6内容计费、IPv6 URL重定向、IPv6 Web Proxy、IPv6 Captive Portal和IPv6 基于业务感知的带宽控制都需要使用IPv6 SA功能。<br>- 用户进行IPv6业务访问，GGSN-C、SGW-C、PGW-C对IPv6用户的上下行报文进行识别解析，基于识别的IPv6业务种类或解析到的关键字匹配计费和控制规则，达到区分不同IPv6业务类型实施不同的计费和控制策略的目的。计费和控制策略包括IPv6内容计费、IPv6 URL重定向、IPv6 Web Proxy、IPv6 Captive Portal和IPv6 基于业务感知的带宽控制。

## 相关控制项（原文，未解释为边）

- SA-Basic。<br>- IPv6承载上下文。<br>- Gi/SGi接口IPv6组网。

## 对应特性（原文）

WSFD-109103 IPv6 SA

## 控制的能力

- [WSFD-109103](feature/UNC/20.15.2/WSFD-109103.md)  — 控制项 82207983

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
