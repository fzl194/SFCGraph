---
id: UNC@20.15.2@License@LKV2CSFB04
type: License
name: 基于CSFB的Multi PLMN
nf: UNC
version: 20.15.2
license_code: LKV2CSFB04
control_item_id: '82206604'
applicable_nf:
- MME
status: active
---

# 基于CSFB的Multi PLMN

`LKV2CSFB04` · 控制项 82206604 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

基于CSFB的Multi PLMN，指各运营商共享LTE/EPC网络，而不共享GSM/UMTS网络的共享方式。通过这种方式，各运营商的LTE用户发起语音业务，通过LTE网络回落到各自运营商的GSM/UMTS网络，有利于节省运营商的投资成本。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

空口广播多个或者单个HPLMN，多运营商共享eNodeB或eNodeB+MME设备。

## 相关控制项（原文，未解释为边）

依赖WSFD-102301 基于CSFB的语音业务

## 对应特性（原文）

WSFD-102505 基于CSFB的Multi PLMN

## 控制的能力

- [WSFD-102505](feature/UNC/20.15.2/WSFD-102505.md)  — 控制项 82206604

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
