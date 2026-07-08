---
id: UNC@20.15.2@License@LKV2UDMVTR01
type: License
name: 基于UDM的VoNR语音故障恢复
nf: UNC
version: 20.15.2
license_code: LKV2UDMVTR01
control_item_id: 82200DHD
applicable_nf:
- SMF
status: active
---

# 基于UDM的VoNR语音故障恢复

`LKV2UDMVTR01` · 控制项 82200DHD ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

在系统中控制允许进行P-CSCF故障恢复的会话数。

## 实现描述

SMF系统中每激活一个VONR会话时，该License总数加1。每去激活一个VONR会话时，该License总数减1。

## 取值范围

0～16000000 Session

## 默认值

10

## 应用场景

P-CSCF故障场景下，VoNR被叫业务快速恢复。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-221002 基于UDM的VoNR语音故障恢复

## 控制的能力

- [WSFD-221002](feature/UNC/20.15.2/WSFD-221002.md)  — 控制项 82200DHD

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
