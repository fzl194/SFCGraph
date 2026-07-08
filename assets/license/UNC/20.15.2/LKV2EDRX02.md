---
id: UNC@20.15.2@License@LKV2EDRX02
type: License
name: eMTC eDRX模式
nf: UNC
version: 20.15.2
license_code: LKV2EDRX02
control_item_id: '82207719'
applicable_nf:
- MME
status: active
---

# eMTC eDRX模式

`LKV2EDRX02` · 控制项 82207719 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本特性通过在网元间传递eDRX（Extended Discontinuous Reception）信元并计算出合理的寻呼时机来缩短对移动性、实时性较低的eMTC终端的监控寻呼信道时长，从而减少网络信令负荷，节省终端耗电量，延长电池使用寿命。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

对使用电池供电、实时性要求较低的eMTC终端可开启eDRX模式，如：智能抄表业务中的电表、智能工业中的传感器、智能宠物健康中的颈环等。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-216002 eMTC eDRX模式

## 控制的能力

- [WSFD-216002](feature/UNC/20.15.2/WSFD-216002.md)  — 控制项 82207719

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
