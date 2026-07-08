---
id: UNC@20.15.2@License@LKV2NRGL01
type: License
name: LTE和GSM 网络之间的重选-USM
nf: UNC
version: 20.15.2
license_code: LKV2NRGL01
control_item_id: 82200BNE
applicable_nf:
- GGSN-C
- PGW-C
- SGW-C
status: active
---

# LTE和GSM 网络之间的重选-USM

`LKV2NRGL01` · 控制项 82200BNE ·  · 域 

## 归属/适用NF（原文）

GGSN-C/PGW-C/SGW-C

## 功能描述

- LTE到GSM的网络重选UE移动出LTE和GSM的重叠覆盖区进入单GSM的覆盖区后，执行小区重选，发起RAU（路由区更新）过程，驻留到GSM小区。<br>- GSM到LTE的网络重选UE从单GSM网络覆盖区移动到LTE和GSM的重叠覆盖区后，LTE具有高优先级，执行小区重选，发起TAU（跟踪区更新）过程，驻留到LTE小区。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

支持LTE和UMTS网络之间的重选。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104502 LTE和GSM 网络之间的重选

## 控制的能力

- [WSFD-104502](feature/UNC/20.15.2/WSFD-104502.md)  — 控制项 82200BNE

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
