---
id: UNC@20.15.2@License@LKV2VTBR01
type: License
name: VoLTE承载故障快速恢复
nf: UNC
version: 20.15.2
license_code: LKV2VTBR01
control_item_id: '82207529'
applicable_nf:
- MME
status: active
---

# VoLTE承载故障快速恢复

`LKV2VTBR01` · 控制项 82207529 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在部署了VoLTE语音业务的网络中，MME Pool的组网场景下，用户正在VoLTE语音业务，如果MME故障，Pool内其它MME可以快速接替故障MME上的用户的业务，实现VoLTE承载的快速恢复，确保通话继续。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

本特性应用于部署了VoLTE语音业务的MME Pool网络，对VoLTE语音通话可靠性要求高时，比如执警、救援等呼叫业务中不会因为网络故障和操作维护中断，建议开启本特性。

## 相关控制项（原文，未解释为边）

MME链式备份

## 对应特性（原文）

WSFD-201204

## 控制的能力

- [WSFD-201204](feature/UNC/20.15.2/WSFD-201204.md)  — 控制项 82207529

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
