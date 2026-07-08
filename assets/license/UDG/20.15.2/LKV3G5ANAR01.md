---
id: UDG@20.15.2@License@LKV3G5ANAR01
type: License
name: 重点用户质差监测和保障
nf: UDG
version: 20.15.2
license_code: LKV3G5ANAR01
control_item_id: 82200HHU
license_domain: UDG
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 重点用户质差监测和保障

`LKV3G5ANAR01` · 控制项 82200HHU · resource · 域 UDG

## 归属/适用NF（原文）

UPF

## 功能描述

通过license控制重点用户质差监测和保障功能是否使能。

## 实现描述

系统中如果用户从非重点保障用户变成重点保障用户，该License使用量加一。当用户从重点保障用户变成非重点保障用户，该License使用量减一。当重点保障用户去活，该License减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

保障用户访问特定业务时的高质量网络。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111286 重点用户质差监测和保障

## 控制的能力

- [GWFD-111286](feature/UDG/20.15.2/GWFD-111286.md)  — 控制项 82200HHU

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
