---
id: UDG@20.15.2@License@LKV3G5HTHE01
type: License
name: HTTP头增强
nf: UDG
version: 20.15.2
license_code: LKV3G5HTHE01
control_item_id: '82209777'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# HTTP头增强

`LKV3G5HTHE01` · 控制项 82209777 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

HTTP头增强指对HTTP报文头的内容做增强处理，将用户信息APN、MS IP Address、IMSI、Hashed-IMSI、MSISDN、Hashed-MSISDN、User Defined Value中的一个或多个信息添加到HTTP报文头并传递给Web Server，运营商和服务提供商可基于这些信息灵活开展业务和实施控制，例如业务认证、广告宣传、业务推广和账户管理与查询。

## 实现描述

可以按照如下两种方式使能HTTP头增强特性：<br>- 基于特定IP地址触发HTTP头增强当用户通过IP地址方式访问特定Web Server时，可触发HTTP头增强。在网元上配置三四层计费规则，不配置L7FILTER，并在三四层动作链中添加Header Enrichment动作。网元的报文头增强处理只针对用户的HTTP报文进行，当选用基于特定IP地址触发HTTP头增强的触发方式时，如果非HTTP协议的业务流匹配到包含了Header Enrichment动作的三四层计费规则，不会进行HTTP头增强的报文处理。<br>- 基于特定URL触发HTTP头增强当用户通过URL方式访问特定Web Server时，可触发HTTP头增强。在网元上配置七层计费规则，配置L7FILTER，并在七层动作链中添加Header Enrichment动作。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

由于Web Server通常部署在纯粹的数据通信网络中，因此在未开启HTTP头增强特性时，Web Server无法得知具体用户的相关信息，运营商无法对用户的业务访问进行控制。而当在网元上开启HTTP头增强特性后，用户的相关信息APN、MS IP Address、IMSI、Hashed-IMSI、MSISDN、Hashed-MSISDN、User Defined Value中的一个或多个信息就可以由<br>UDG<br>添加到HTTP报文头中传递给Web Server，从而很好的满足了运营商针对用户做业务访问认证的需求。<br>除了可以支持业务访问认证外，如果运营商或服务提供商的Web Server需要用户的属性信息来向用户返回个性化管理与查询页面，以及计费结算，HTTP头增强特性也可以很好的满足该业务需求。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- SA-Web Browsing<br>- SA-Mobile

## 对应特性（原文）

GWFD-110261 HTTP头增强

## 控制的能力

- [GWFD-110261](feature/UDG/20.15.2/GWFD-110261.md)  — 控制项 82209777

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
