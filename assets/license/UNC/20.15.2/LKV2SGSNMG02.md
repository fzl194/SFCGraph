---
id: UNC@20.15.2@License@LKV2SGSNMG02
type: License
name: SGSN Pool用户迁移
nf: UNC
version: 20.15.2
license_code: LKV2SGSNMG02
control_item_id: '82206553'
applicable_nf:
- SGSN
status: active
---

# SGSN Pool用户迁移

`LKV2SGSNMG02` · 控制项 82206553 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

SGSN<br>Pool用户迁移特性是在SGSN Pool组网中，当用户在Pool内的SGSN上分布不均衡时，通过手工方式将部分用户从一个SGSN迁移到另一个SGSN上，从而实现对SGSN Pool内这些SGSN的维护而不影响用户业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~12000000 SAU

## 默认值

10

## 应用场景

SGSN Pool内SGSN之间用户的迁移可以应用于如下的场景：<br>- 迁移全部用户<br>- 迁移部分用户<br>- 迁移指定RNC/BSC下的用户<br>- 迁移指定的用户<br>- 基于MSISDN号段迁移用户（不推荐）

## 相关控制项（原文，未解释为边）

依赖WSFD-104204 Gb-flex或WSFD-104203 Iu-flex

## 对应特性（原文）

WSFD-104201 SGSN Pool用户迁移

## 控制的能力

- [WSFD-104201](feature/UNC/20.15.2/WSFD-104201.md)  — 控制项 82206553

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
