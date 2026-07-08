---
id: UNC@20.15.2@License@LKV3WPRVCC11
type: License
name: SRVCC
nf: UNC
version: 20.15.2
license_code: LKV3WPRVCC11
control_item_id: '82208003'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# SRVCC

`LKV3WPRVCC11` · 控制项 82208003 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

SRVCC（Single Radio Voice Call Continuity）为单语音呼叫持续。在LTE网络部署初期，LTE网络未完全覆盖，当VoLTE用户移动到了LTE未覆盖到的区域，语音业务则需要切换到CS网络（无线侧为GSM/UMTS），SRVCC可以保证在网络切换过程中，正在进行的语音业务不中断。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

本特性应用于EPC网络。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-102003 SRVCC

## 控制的能力

- [WSFD-102003](feature/UNC/20.15.2/WSFD-102003.md)  — 控制项 82208003

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
