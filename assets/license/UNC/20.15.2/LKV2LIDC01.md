---
id: UNC@20.15.2@License@LKV2LIDC01
type: License
name: 逻辑接口DSCP配置
nf: UNC
version: 20.15.2
license_code: LKV2LIDC01
control_item_id: '82205927'
applicable_nf:
- SGSN
- MME
status: active
---

# 逻辑接口DSCP配置

`LKV2LIDC01` · 控制项 82205927 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

逻辑接口DSCP配置特性是指SGSN/MME在组网的时候针对不同的接口可设置不同的DSCP值。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

通过调整DSCP值改变不同接口上IP报文的优先级，提高数据传输可靠性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-105004 逻辑接口DSCP配置

## 控制的能力

- [WSFD-105004](feature/UNC/20.15.2/WSFD-105004.md)  — 控制项 82205927

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
