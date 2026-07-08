---
id: UDG@20.15.2@License@LKV3G5EXPR01
type: License
name: 体验信息采集
nf: UDG
version: 20.15.2
license_code: LKV3G5EXPR01
control_item_id: 82200HHV
license_domain: UDG
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 体验信息采集

`LKV3G5EXPR01` · 控制项 82200HHV · resource · 域 UDG

## 归属/适用NF（原文）

UPF

## 功能描述

通过该license控制体验信息采集功能是否使能。

## 实现描述

重点保障用户，全球通用户和普通体验用户需要上报体验信息，称为体验用户。当用户从非体验用户变成体验用户，该License使用量加一。当用户从体验用户变成非体验用户，该License减一。当体验用户去活，该License减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

支持对用户进行业务体验分析。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111284 体验信息采集

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
