---
id: UNC@20.15.2@License@LKV2NRUL01
type: License
name: LTE和UMTS 网络之间的重选-USM
nf: UNC
version: 20.15.2
license_code: LKV2NRUL01
control_item_id: 82200BND
applicable_nf:
- GGSN-C
- PGW-C
- SGW-C
status: active
---

# LTE和UMTS 网络之间的重选-USM

`LKV2NRUL01` · 控制项 82200BND ·  · 域 

## 归属/适用NF（原文）

GGSN-C/PGW-C/SGW-C

## 功能描述

- LTE到UMTS的网络重选UE移动出LTE和UMTS的重叠覆盖区进入单UMTS的覆盖区后，执行小区重选，发起RAU（路由区更新）过程，驻留到UMTS小区。<br>- UMTS到LTE的网络重选UE移动到LTE和UMTS的重叠覆盖区后，LTE具有高优先级，执行小区重选，发起TAU（跟踪区更新）过程，驻留到LTE小区。

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

WSFD-104501 LTE和UMTS 网络之间的重选

## 控制的能力

- [WSFD-104501](feature/UNC/20.15.2/WSFD-104501.md)  — 控制项 82200BND

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
