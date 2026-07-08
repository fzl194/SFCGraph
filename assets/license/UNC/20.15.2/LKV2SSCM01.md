---
id: UNC@20.15.2@License@LKV2SSCM01
type: License
name: 支持SSC Mode1
nf: UNC
version: 20.15.2
license_code: LKV2SSCM01
control_item_id: '82209919'
applicable_nf:
- SMF
status: active
---

# 支持SSC Mode1

`LKV2SSCM01` · 控制项 82209919 ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

5G系统支持会话和业务的连续性SSC（Session and Service Continuity）。为了满足不同业务对连续性的不同要求，5G系统支持不同的SSC Mode，一个PDU会话的SSC Mode在该会话的生命周期里保持不变。SSC Mode1提供IP连续性，对于SSC Mode1的PDU会话，网络提供给UE的IP地址保持不变。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

适用于IMS语音等对业务连续性有高要求的应用。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-107015 支持SSC Mode1

## 控制的能力

- [WSFD-107015](feature/UNC/20.15.2/WSFD-107015.md)  — 控制项 82209919

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
