---
id: UNC@20.15.2@License@LKV2EDRX01
type: License
name: NB-IoT eDRX模式
nf: UNC
version: 20.15.2
license_code: LKV2EDRX01
control_item_id: '82207382'
applicable_nf:
- MME
status: active
---

# NB-IoT eDRX模式

`LKV2EDRX01` · 控制项 82207382 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本特性通过传递网元间eDRX（Extended Discontinuous Reception）信元的传递并计算出合理的寻呼时机来缩短对移动性、实时性较低的M2M终端（如表类、传感器、健康手环和颈环等）的监控寻呼信道时长，从而减少网络信令负荷，节省终端耗电量，延长电池使用寿命。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

对未使用交流供电、实时性要求较低的M2M终端可开启eDRX模式，如：智能抄表业务中的电表、智能工业中的传感器、智能宠物健康中的颈环等。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215002 NB-IoT eDRX模式

## 控制的能力

- [WSFD-215002](feature/UNC/20.15.2/WSFD-215002.md)  — 控制项 82207382

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
