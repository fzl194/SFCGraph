---
id: UNC@20.15.2@License@LKV3WPWULI11
type: License
name: 基于接入点策略控制
nf: UNC
version: 20.15.2
license_code: LKV3WPWULI11
control_item_id: '82209475'
applicable_nf:
- GGSN-C
- PGW-C
status: active
---

# 基于接入点策略控制

`LKV3WPWULI11` · 控制项 82209475 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C

## 功能描述

基于接入点策略控制特性是指当非可信接入用户的IP或Port发生变更时，GGSN-C、PGW-C将用户新的IP或Port上报给PCRF/CG/Radius Server，PCRF/CG/Radius Server以此为依据判断用户位置，进行差异化处理。

## 实现描述

当非可信用户激活上下文时，基于接入点的策略控制license统计数加一，当去活一个非可信接入用户时，基于接入点的策略控制license统计数减一。如果系统中已激活的非可信用户数达到基于接入点的策略控制的license的数量上限时，非可信接入用户的IP或Port发生变更时，GGSN-C、PGW-C根据license决策不再通知PCRF/CG/Radius Server进行位置更新。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

基于接入点策略控制可以基于WiFi用户位置实施精细化控制，如PCRF根据WiFi用户位置进行差异化策略控制、CG/Radius Server根据WiFi用户位置进行差异化处理。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-109108 基于接入点策略控制

## 控制的能力

- [WSFD-109108](feature/UNC/20.15.2/WSFD-109108.md)  — 控制项 82209475

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
