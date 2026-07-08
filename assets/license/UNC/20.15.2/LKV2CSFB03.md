---
id: UNC@20.15.2@License@LKV2CSFB03
type: License
name: Flash CSFB with RIM
nf: UNC
version: 20.15.2
license_code: LKV2CSFB03
control_item_id: '82206603'
applicable_nf:
- MME
status: active
---

# Flash CSFB with RIM

`LKV2CSFB03` · 控制项 82206603 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

LTE用户以Combined Attach或者Combined TAU方式接入到MME系统后，当UE因为CSFB业务需要而回落到GSM/UMTS网络时，MME支持UE通过eNodeB发起RIM（RAN Information Management）流程来预先获取到需要回落到目标网络的无线参数，使UE能够快速的切入到目标网络，减少呼叫时延。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在CSFB回落场景下，eNodeB通知UE向CS网络注册时，UE会先探测空口获取GSM/UMTS目标小区无线参数。如果需要节省这个过程来降低回落时延，可以开启此特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-102301 基于CSFB的语音业务和WSFD-104406 NACC

## 对应特性（原文）

WSFD-102506 Flash CSFB with RIM

## 控制的能力

- [WSFD-102506](feature/UNC/20.15.2/WSFD-102506.md)  — 控制项 82206603

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
