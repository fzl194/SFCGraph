---
id: UNC@20.15.2@License@LKV3W9DOCH12
type: License
name: Gy/Diameter在线计费
nf: UNC
version: 20.15.2
license_code: LKV3W9DOCH12
control_item_id: '82207989'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
status: active
---

# Gy/Diameter在线计费

`LKV3W9DOCH12` · 控制项 82207989 ·  · 域 

## 归属/适用NF（原文）

GGSN-C/SGW-C/PGW-C

## 功能描述

在线计费是GGSN/PGW-C对移动数据用户使用网络资源进行实时计费的功能。当用户发起数据业务时，OCS将用户账户金额转换成流量、时长后通过GGSN/PGW-C下发给UDG，用户访问业务的过程中，OCS实时跟踪配额的使用情况，配额耗尽时终止业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

网络中规划通过OCS进行实时的用户配额管理，保障用户的计费信息及时、准确的上报给计费中心。

## 相关控制项（原文，未解释为边）

依赖<br>WSFD-104508 SCTP<br>WSFD-109002 内容计费基本功能<br>WSFD-109004 基于业务流量的计费<br>WSFD-109003 基于业务时长的计费

## 对应特性（原文）

WSFD-109001 Gy/Diameter在线计费

## 控制的能力

- [WSFD-109001](feature/UNC/20.15.2/WSFD-109001.md)  — 控制项 82207989

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
