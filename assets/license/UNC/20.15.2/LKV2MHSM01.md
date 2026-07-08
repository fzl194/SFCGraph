---
id: UNC@20.15.2@License@LKV2MHSM01
type: License
name: 支持多HPLMN功能-USM
nf: UNC
version: 20.15.2
license_code: LKV2MHSM01
control_item_id: '82209970'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# 支持多HPLMN功能-USM

`LKV2MHSM01` · 控制项 82209970 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C、SMF

## 功能描述

HPLMN是SMF的归属PLMN，用于判断接入用户的漫游属性，属于这些PLMN的用户按照本地用户处理。SMF可以配置多个HPLMN，用户接入时可以与每一个HPLMN进行比较，从而判断用户的漫游属性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

在SGW-C/PGW-C和SMF激活的用户都需要按照准确的用户属性来进行计费和业务控制策略等处理。如果运营商有多个PLMN ID，就需要在SGW-C/PGW-C和SMF上配置多个HPLMN，以保证对用户准确的进行计费和业务控制。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104401 支持多HPLMN功能

## 控制的能力

- [WSFD-104401](feature/UNC/20.15.2/WSFD-104401.md)  — 控制项 82209970

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
