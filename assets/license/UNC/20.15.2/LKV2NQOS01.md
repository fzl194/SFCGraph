---
id: UNC@20.15.2@License@LKV2NQOS01
type: License
name: PCC模式的本地QoS策略控制
nf: UNC
version: 20.15.2
license_code: LKV2NQOS01
control_item_id: '82206581'
applicable_nf:
- SGSN
- MME
status: active
---

# PCC模式的本地QoS策略控制

`LKV2NQOS01` · 控制项 82206581 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

EPS网络中，UNC作为S4 SGSN或MME，支持PCC模式下对专有承载的QoS控制。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

GPRS网络中，部署PCC策略场景下，建议部署。<br>EPS网络中，运营商需要对专有承载进行QoS控制，建议部署。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-105105 PCC模式的本地QoS策略控制

## 控制的能力

- [WSFD-105105](feature/UNC/20.15.2/WSFD-105105.md)  — 控制项 82206581

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
