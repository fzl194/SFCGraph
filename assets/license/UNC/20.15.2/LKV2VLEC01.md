---
id: UNC@20.15.2@License@LKV2VLEC01
type: License
name: VoLTE紧急呼叫
nf: UNC
version: 20.15.2
license_code: LKV2VLEC01
control_item_id: '82206606'
applicable_nf:
- MME
status: active
---

# VoLTE紧急呼叫

`LKV2VLEC01` · 控制项 82206606 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

当用户遇到反恐、医疗紧急救助、火警或自然灾害救援等情况的时候，用户可以使用在LTE网络覆盖下的UE拨打紧急号码连接到公共安全应答点PSAP（Public Safety Answering Point）来获得紧急救助。<br>无线侧识别紧急号码后，在消息中添加紧急标识传递给网络侧，网络侧根据紧急标识将UE接入到紧急APN中，为UE分配紧急呼叫资源，保证紧急业务的接入。在通话过程中，UE移动出LTE覆盖后，能够通过SRVCC流程将紧急呼叫切换到G/U的电路域。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当用户遇到反恐、医疗紧急救助、火警或自然灾害救援等情况的时候，用户可以使用在LTE网络覆盖下的UE拨打紧急号码连接到紧急呼叫中心PSAP（Public Safety Answering Point）来获得紧急救助。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础语音业务

## 对应特性（原文）

WSFD-102101 VoLTE紧急呼叫

## 控制的能力

- [WSFD-102101](feature/UNC/20.15.2/WSFD-102101.md)  — 控制项 82206606

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
