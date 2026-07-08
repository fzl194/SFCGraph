---
id: UNC@20.15.2@License@LKV3W9IMSR11
type: License
name: P-CSCF故障时IMS业务恢复
nf: UNC
version: 20.15.2
license_code: LKV3W9IMSR11
control_item_id: '82208005'
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# P-CSCF故障时IMS业务恢复

`LKV3W9IMSR11` · 控制项 82208005 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C、SMF

## 功能描述

PGW-U/UPF采用ICMP的方式，周期性的检测P-CSCF状态，当检测到PGW-U/UPF与P-CSCF链接状态异常时，上报给PGW-C/SMF。PGW-C/SMF将一对状态正常的P-CSCF地址推送给UE，UE从中选择一个P-CSCF地址，重新发起IMS业务，从而保证IMS业务自动恢复。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

部署IMS网络场景下，为了保证用户的IMS业务能够及时恢复，建议开启此特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础语音业务

## 对应特性（原文）

WSFD-102202 P-CSCF故障时IMS业务恢复

## 控制的能力

- [WSFD-102202](feature/UNC/20.15.2/WSFD-102202.md)  — 控制项 82208005

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
