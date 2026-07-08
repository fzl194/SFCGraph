---
id: UNC@20.15.2@License@LKV2CSCR01
type: License
name: CSFB被叫恢复
nf: UNC
version: 20.15.2
license_code: LKV2CSCR01
control_item_id: '82206601'
applicable_nf:
- MME
status: active
---

# CSFB被叫恢复

`LKV2CSCR01` · 控制项 82206601 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在CSFB特性的POOL组网中，当MME网元或MSC网元故障时，在UE进行被叫业务时，被叫寻呼可以通过同一POOL内的其它正常MME网元或MSC网元下达给无线侧。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

本特性应用于Pool组网场景下，用户进行CSFB被叫呼叫时，如果MME或MSC故障，通过本特性功能可以将业务触发到Pool内其它可用的MME或MSC上，保证语音业务不中断。

## 相关控制项（原文，未解释为边）

依赖WSFD-102301 基于CSFB的语音业务

## 对应特性（原文）

WSFD-102503 CSFB被叫恢复

## 控制的能力

- [WSFD-102503](feature/UNC/20.15.2/WSFD-102503.md)  — 控制项 82206601

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
