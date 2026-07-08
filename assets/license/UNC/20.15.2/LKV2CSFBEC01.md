---
id: UNC@20.15.2@License@LKV2CSFBEC01
type: License
name: CSFB紧急呼叫
nf: UNC
version: 20.15.2
license_code: LKV2CSFBEC01
control_item_id: '82206156'
applicable_nf:
- MME
status: active
---

# CSFB紧急呼叫

`LKV2CSFBEC01` · 控制项 82206156 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

LTE用户以Combined Attach或者Combined TAU方式接入到MME系统后，当UE以紧急呼叫方式发起CSFB主叫业务时，MME将紧急呼叫标识通过eNodeB传递给CS域，使CS域在系统拥塞的场景下优先处理CSFB紧急呼叫业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

紧急呼叫业务为用户的人身和财产安全提供保障，网络部署中都需要激活该特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-102301 基于CSFB的语音业务

## 对应特性（原文）

WSFD-102501 CSFB紧急呼叫

## 控制的能力

- [WSFD-102501](feature/UNC/20.15.2/WSFD-102501.md)  — 控制项 82206156

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
