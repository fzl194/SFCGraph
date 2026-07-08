---
id: UNC@20.15.2@License@LKV2NBFQ02
type: License
name: NB-IoT连接基本软件第二档
nf: UNC
version: 20.15.2
license_code: LKV2NBFQ02
control_item_id: '82207362'
applicable_nf:
- MME
status: active
---

# NB-IoT连接基本软件第二档

`LKV2NBFQ02` · 控制项 82207362 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在系统中控制允许接入的NB-IoT用户数及每日可以为用户提供的服务次数。

## 实现描述

本License表示系统可以为每用户每天提供不超过144次服务，所能提供服务的用户数为本License购买的数量。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

MME网元中NB-IoT用户接入。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 控制的能力

- [WSFD-011601](feature/UNC/20.15.2/WSFD-011601.md)  — 控制项 82207362

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
