---
id: UNC@20.15.2@License@LKV3GWUISL01
type: License
name: GW-U故障隔离
nf: UNC
version: 20.15.2
license_code: LKV3GWUISL01
control_item_id: 82200CQY
applicable_nf:
- GGSN-C
- PGW-C
- SGW-C
status: active
---

# GW-U故障隔离

`LKV3GWUISL01` · 控制项 82200CQY ·  · 域 

## 归属/适用NF（原文）

GGSN-C/PGW-C/SGW-C

## 功能描述

GW-U故障隔离是指当某个业务区内的SGW-U/PGW-U/GGSN-U全部发生故障时，SGW-C/PGW-C/GGSN-C能将故障的SGW-U/PGW-U/GGSN-U全部隔离，从而保证用户业务正常进行。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

PGW-C/SGW-C/GGSN-C对接多个业务区的PGW-U/SGW-U/GGSN-U，当某个业务区内的PGW-U/SGW-U/GGSN-U全部故障时，需要支持GW-U的故障隔离功能。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-213004GW-U故障隔离

## 控制的能力

- [WSFD-213004](feature/UNC/20.15.2/WSFD-213004.md)  — 控制项 82200CQY

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
