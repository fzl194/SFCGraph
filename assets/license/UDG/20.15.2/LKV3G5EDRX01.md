---
id: UDG@20.15.2@License@LKV3G5EDRX01
type: License
name: 5G eDRX模式
nf: UDG
version: 20.15.2
license_code: LKV3G5EDRX01
control_item_id: 82200FYD
license_domain: UDG
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 5G eDRX模式

`LKV3G5EDRX01` · 控制项 82200FYD · resource · 域 UDG

## 归属/适用NF（原文）

UPF

## 功能描述

用于控制5G用户的eDRX功能是否使能。

## 实现描述

系统中申请了此license，支持5G用户的eDRX功能，否则不支持。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

eDRX功能开启后可以有效的降低5G终端的功耗，当应用场景需要低功耗时，可通过购买该项License使能eDRX功能。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110661 5G eDRX模式

## 控制的能力

- [GWFD-110661](feature/UDG/20.15.2/GWFD-110661.md)  — 控制项 82200FYD

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
