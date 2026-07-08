---
id: UNC@20.15.2@License@LKV2NOISDN02
type: License
name: 支持Null-MSISDN
nf: UNC
version: 20.15.2
license_code: LKV2NOISDN02
control_item_id: '82207024'
applicable_nf:
- SGSN
- MME
status: active
---

# 支持Null-MSISDN

`LKV2NOISDN02` · 控制项 82207024 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

支持Null-MSISDN特性是指<br>UNC<br>支持不携带MSISDN（Mobile Station International ISDN Number）的用户进行基本的移动性管理和会话管理业务，如附着、TAU/RAU、激活等。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

对于M2M（Machine to Machine）类型的终端，如果不需要通过MSISDN进行业务，建议开启此特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106012 支持Null-MSISDN

## 控制的能力

- [WSFD-106012](feature/UNC/20.15.2/WSFD-106012.md)  — 控制项 82207024

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
