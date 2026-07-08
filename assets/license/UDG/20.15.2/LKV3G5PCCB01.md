---
id: UDG@20.15.2@License@LKV3G5PCCB01
type: License
name: PCC 基本功能
nf: UDG
version: 20.15.2
license_code: LKV3G5PCCB01
control_item_id: '82209825'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# PCC 基本功能

`LKV3G5PCCB01` · 控制项 82209825 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

SGW-U/PGW-U/UPF支持智能策略控制功能

## 实现描述

UDG<br>支持SGW-C/PGW-C/SMF通过下发PCC策略来实现策略和计费控制。当UE接入网络后，SGW-C/PGW-C/SMF通过N4接口给SGW-U/PGW-U/UPF下发PCC策略，SGW-U/PGW-U/UPF对使用PCC策略的用户进行控制。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

运营商部署PCC用户接入。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020351 PCC基本功能

## 控制的能力

- [GWFD-020351](feature/UDG/20.15.2/GWFD-020351.md)  — 控制项 82209825

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
