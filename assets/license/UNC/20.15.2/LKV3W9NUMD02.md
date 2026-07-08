---
id: UNC@20.15.2@License@LKV3W9NUMD02
type: License
name: 支持Null-MSISDN
nf: UNC
version: 20.15.2
license_code: LKV3W9NUMD02
control_item_id: '81202798'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# 支持Null-MSISDN

`LKV3W9NUMD02` · 控制项 81202798 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C、SMF

## 功能描述

系统通过该license控制是否支持用户激活时不携带MSISDN。

## 实现描述

系统通过该license控制是否允许用户不携带MSISDN的Create PDP Context Request或者Create Session Request消息接入。系统中申请了此license时，支持用户不携带MSISDN的Create PDP Context Request或者Create Session Request消息接入，否则不支持。

## 取值范围

0～1 SAU

## 默认值

1

## 应用场景

对于M2M（Machine to Machine）类型的终端，如果不需要通过MSISDN进行业务，建议开启此特性。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-106012 支持Null-MSISDN

## 控制的能力

- [WSFD-106012](feature/UNC/20.15.2/WSFD-106012.md)  — 控制项 81202798

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_64048081.md`
