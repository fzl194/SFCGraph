---
id: UNC@20.15.2@License@LKV3W9TBCS12
type: License
name: 基于业务时长的计费
nf: UNC
version: 20.15.2
license_code: LKV3W9TBCS12
control_item_id: '82207991'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# 基于业务时长的计费

`LKV3W9TBCS12` · 控制项 82207991 ·  · 域 

## 归属/适用NF（原文）

GGSN-C/SGW-C/PGW-C/SMF

## 功能描述

基于业务时长的计费是在业务识别解析的基础上，按照该业务的使用时间进行计费。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

当运营商希望区分用户数据流中的内容所属的业务类型，从而配以不同的资费标准，并按用户使用业务的时长向用户收取不同的资费时，可部署本特性。

## 相关控制项（原文，未解释为边）

WSFD-109002 内容计费基本功能

## 对应特性（原文）

WSFD-109003 基于业务时长的计费

## 控制的能力

- [WSFD-109003](feature/UNC/20.15.2/WSFD-109003.md)  — 控制项 82207991

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
