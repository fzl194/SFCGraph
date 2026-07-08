---
id: UNC@20.15.2@License@LKV2MMEMG02
type: License
name: MME Pool用户迁移
nf: UNC
version: 20.15.2
license_code: LKV2MMEMG02
control_item_id: '82205876'
applicable_nf:
- MME
status: active
---

# MME Pool用户迁移

`LKV2MMEMG02` · 控制项 82205876 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

一个MME的用户可以迁移到其他MME上。因此，当用户在其他MME上接入的时候原来的服务可以继续使用。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

- MME升级前，待升级的MME需要迁移MME上所有的用户到其他MME上。<br>- MME升级完成，其他MME上部分用户需要迁移回原来的MME。<br>- 当MME Pool中某MME发生故障时，eNodeB识别该MME故障后，eNodeB会将本来由该MME提供服务的用户发起的新业务转移到Pool中其他有效的MME上。

## 相关控制项（原文，未解释为边）

依赖WSFD-104101 MME Pool

## 对应特性（原文）

WSFD-104103 MME Pool用户迁移

## 控制的能力

- [WSFD-104103](feature/UNC/20.15.2/WSFD-104103.md)  — 控制项 82205876

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
