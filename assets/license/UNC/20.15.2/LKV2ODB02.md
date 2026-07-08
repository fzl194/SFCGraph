---
id: UNC@20.15.2@License@LKV2ODB02
type: License
name: 支持ODB
nf: UNC
version: 20.15.2
license_code: LKV2ODB02
control_item_id: '82206154'
applicable_nf:
- SGSN
- MME
status: active
---

# 支持ODB

`LKV2ODB02` · 控制项 82206154 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

通过对ODB（Operator Determined Barring）参数的设置限制一些用户的业务和服务。<br>用户在HLR中签约时，指定该用户的ODB特性，指明该用户哪些业务需要禁止。HLR会将用户的ODB信息作为签约数据的一部分插入到MME中。MME根据自身处理能力，结合签约ODB特性，进行相应的业务的禁止或者允许。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

通过设置ODB参数限制一些用户的业务和服务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106005 支持ODB

## 控制的能力

- [WSFD-106005](feature/UNC/20.15.2/WSFD-106005.md)  — 控制项 82206154

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
