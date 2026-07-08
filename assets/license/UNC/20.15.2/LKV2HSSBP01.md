---
id: UNC@20.15.2@License@LKV2HSSBP01
type: License
name: HSS全故障业务逃生
nf: UNC
version: 20.15.2
license_code: LKV2HSSBP01
control_item_id: 82200ENT
applicable_nf:
- MME
status: active
---

# HSS全故障业务逃生

`LKV2HSSBP01` · 控制项 82200ENT ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在系统中控制允许进入HSS故障 Bypass状态的4G&NSA动态用户数。

## 实现描述

MME系统中每有一个4G&NSA用户进入HSS故障 Bypass状态，该License总数加1；每有一个4G&NSA用户退出HSS故障 Bypass状态，总数减1。

## 取值范围

0～12000000 SAU

## 默认值

0

## 应用场景

HSS用于存储用户数据，与MME交互实现鉴权、获取用户签约数据、更新网元注册信息等功能。在与MME对接的所有HSS全部故障的极端场景，将导致大范围业务中断。为了最大程度地保障用户数据业务惯性可用，建议开启本特性减小故障影响范围。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-206102 HSS全故障业务保活

## 控制的能力

- [WSFD-206102](feature/UNC/20.15.2/WSFD-206102.md)  — 控制项 82200ENT

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
