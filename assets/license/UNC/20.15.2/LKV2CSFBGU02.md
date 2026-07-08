---
id: UNC@20.15.2@License@LKV2CSFBGU02
type: License
name: 基于CSFB的语音业务
nf: UNC
version: 20.15.2
license_code: LKV2CSFBGU02
control_item_id: '82205925'
applicable_nf:
- MME
status: active
---

# 基于CSFB的语音业务

`LKV2CSFBGU02` · 控制项 82205925 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

基于CSFB（Circuit Switched Fallback）的语音业务，是一种在不引入IMS的情况下，利用现有的GERAN/UTRAN网络实现语音通话的一种语音解决方案。该方案能充分利用现有网络资源，提升用户体验。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

- 不支持通过PS Handover流程回落到GSM网络。<br>- 要求eNodeB支持Inter-RAT互操作相关特性：RAU、Handover、NACC（Network Assisted Cell Change）。<br>- 只支持一个TA只能属于一个TA LIST，同时一个TA LIST只能属于一个LA的组网场景。

## 相关控制项（原文，未解释为边）

依赖WSFD-104501 LTE和UMTS 网络之间的重选或WSFD-104503 LTE和UMTS PS网络之间的切换或WSFD-104502 LTE和GSM 网络之间的重选

## 对应特性（原文）

WSFD-102301 基于CSFB的语音业务

## 控制的能力

- [WSFD-102301](feature/UNC/20.15.2/WSFD-102301.md)  — 控制项 82205925

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
