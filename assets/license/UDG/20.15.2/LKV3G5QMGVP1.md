---
id: UDG@20.15.2@License@LKV3G5QMGVP1
type: License
name: VVIP用户质差监测和保障
nf: UDG
version: 20.15.2
license_code: LKV3G5QMGVP1
control_item_id: 82200FQR
license_domain: VAS
control_item_type: resource
applicable_nf:
- PCEF
- TDF-U
status: active
---

# VVIP用户质差监测和保障

`LKV3G5QMGVP1` · 控制项 82200FQR · resource · 域 VAS

## 归属/适用NF（原文）

PCEF/TDF-U

## 功能描述

对订阅了VVIP套餐的用户进行业务质量分析，在发生质差时通过创建专载等方式进行业务质量保障。

## 实现描述

VVIP业务质差检测和保障特性受该License控制。<br>License开启时，则使能业务质差检测和保障特性。<br>License关闭时，不使能业务质差检测和保障特性。

## 取值范围

0~ 8000000

## 默认值

10

## 应用场景

当运营商需要对特定用户做业务质量分析，并对质差场景做业务保障时，需要开启本功能。

## 相关控制项（原文，未解释为边）

- 智能分析记录生成<br>- 业务全样分析上报<br>- TCP/UDP传输分析上报<br>- 用户实时位置分析上报<br>- 业务实时分析上报<br>- 业务分析上报订阅<br>- 系统级智能分析记录生成

## 对应特性（原文）

GWFD-111286 VVIP用户质差监测和保障

## 控制的能力

- [GWFD-111286](feature/UDG/20.15.2/GWFD-111286.md)  — 控制项 82200FQR

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_24575797.md`
