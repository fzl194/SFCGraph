---
id: UDG@20.15.2@License@LKV3G5HP3W01
type: License
name: HTTP3.0 Host识别
nf: UDG
version: 20.15.2
license_code: LKV3G5HP3W01
control_item_id: 82200FCJ
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# HTTP3.0 Host识别

`LKV3G5HP3W01` · 控制项 82200FCJ · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

按照用户数控制HTTP3.0 Host识别功能。

## 实现描述

系统申请了此License并且License有剩余时，可以使用HTTP3.0 Host识别功能；如果License关闭或者License无剩余，则不能使用HTTP3.0 Host识别功能。<br>每对一个用户使用HTTP3.0 Host识别功能进行差异化计费或业务控制，License数量减一。<br>在License值即将耗尽或耗尽时，上报告警，分别为License资源即将用完或License资源用完，告警ID分别为告警ID ALM-100046和ALM-100049。

## 取值范围

0～1600000

## 默认值

10

## 应用场景

当需要对HTTP3.0协议中报文进行差异化计费或业务控制时，开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110251 HTTP3.0 Host识别

## 控制的能力

- [GWFD-110251](feature/UDG/20.15.2/GWFD-110251.md)  — 控制项 82200FCJ

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
