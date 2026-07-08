---
id: UDG@20.15.2@License@LKV3G5SMRB01
type: License
name: 支持媒体中继基本功能
nf: UDG
version: 20.15.2
license_code: LKV3G5SMRB01
control_item_id: 82200JDR
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 支持媒体中继基本功能

`LKV3G5SMRB01` · 控制项 82200JDR · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

支持媒体中继签约用户接入，使用媒体中继功能，未申请License时用户接入成功，无法使用媒体中继功能。

## 实现描述

系统中每激活一个媒体中继用户，该License使用量加一。每去激活一个媒体中继用户，该License使用量减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

媒体中继用户接入

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-113005 支持媒体中继基本功能

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
