---
id: UNC@20.15.2@License@LKV2HPLMN02
type: License
name: 支持多HPLMN功能
nf: UNC
version: 20.15.2
license_code: LKV2HPLMN02
control_item_id: '82205877'
applicable_nf:
- SGSN
- MME
status: active
---

# 支持多HPLMN功能

`LKV2HPLMN02` · 控制项 82205877 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

SGSN/MME支持多HPLMN号，满足运营商组网和规划要求。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

SGSN/MME支持多HPLMN，如果运营商在他的移动网中有多个HPLMN，SGSN/MME支持配置超过一个的HPLMN ID，并且每个HPLMN之间是平等的。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104401 支持多HPLMN功能

## 控制的能力

- [WSFD-104401](feature/UNC/20.15.2/WSFD-104401.md)  — 控制项 82205877

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
