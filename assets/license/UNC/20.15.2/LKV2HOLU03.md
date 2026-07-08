---
id: UNC@20.15.2@License@LKV2HOLU03
type: License
name: LTE和UMTS PS网络之间的切换-USM
nf: UNC
version: 20.15.2
license_code: LKV2HOLU03
control_item_id: 82200BNF
applicable_nf:
- GGSN-C
- PGW-C
- SGW-C
status: active
---

# LTE和UMTS PS网络之间的切换-USM

`LKV2HOLU03` · 控制项 82200BNF ·  · 域 

## 归属/适用NF（原文）

GGSN-C/PGW-C/SGW-C

## 功能描述

- LTE到UMTS PS网络的切换UMTS与LTE共存的情况下，UE在LTE网络进行业务，当UMTS网络的覆盖（信号）优于LTE网络时，或者在eNodeB负荷较重等情况下，eNodeB会触发UE切换到UMTS网络。<br>- UMTS到LTE网络的切换UMTS与LTE共存的情况下，UE在UMTS网络进行业务，当UE移动到LTE覆盖范围等情况下，RNC可能会触发UE切换到LTE网络，以便为UE提供更好的服务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

- 支持UE从LTE到UMTS PS网络的切换。<br>- 支持UE从UMTS到LTE网络的切换。

## 相关控制项（原文，未解释为边）

依赖WSFD-104501 LTE和UMTS网络之间的重选

## 对应特性（原文）

WSFD-104503 LTE和UMTS PS网络之间的切换

## 控制的能力

- [WSFD-104503](feature/UNC/20.15.2/WSFD-104503.md)  — 控制项 82200BNF

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
