---
id: UDG@20.15.2@License@LKV3G5SNAC01
type: License
name: 智网接入
nf: UDG
version: 20.15.2
license_code: LKV3G5SNAC01
control_item_id: 82200HHW
license_domain: UDG
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 智网接入

`LKV3G5SNAC01` · 控制项 82200HHW · resource · 域 UDG

## 归属/适用NF（原文）

UPF

## 功能描述

通过该license控制允许接入系统中的5G智网接入的IKE会话数，当license资源充足时，系统允许新的用户接入。

## 实现描述

系统中每激活一个5G智网接入的IKE会话时，该license使用量加一；每去激活一个5G智网接入的IKE会话时，该license使用量减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

智家随行用户接入

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-112003 智网接入

## 控制的能力

- [GWFD-112003](feature/UDG/20.15.2/GWFD-112003.md)  — 控制项 82200HHW

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
