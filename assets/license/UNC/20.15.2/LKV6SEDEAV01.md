---
id: UNC@20.15.2@License@LKV6SEDEAV01
type: License
name: 计算资源可靠性可定义
nf: UNC
version: 20.15.2
license_code: LKV6SEDEAV01
control_item_id: '81202576'
applicable_nf:
- SGSN
- GGSN-C
- MME
- SGW-C
- PGW-C
- AMF
- SMF
status: active
---

# 计算资源可靠性可定义

`LKV6SEDEAV01` · 控制项 81202576 ·  · 域 

## 归属/适用NF（原文）

SGSN、GGSN-C、MME、SGW-C/PGW-C、AMF、SMF

## 功能描述

计算资源可靠性可定义是指对VNF基础可靠性功能特性的增强，系统允许M（M>=2）个Pod同时故障，进一步提高系统可靠性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1 UNC

## 默认值

1

## 应用场景

为满足多个Pod同时故障时，业务不受损，进一步提升VNF的可靠性，建议部署本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-209001 业务处理单元可靠性可定义

## 控制的能力

- [WSFD-209001](feature/UNC/20.15.2/WSFD-209001.md)  — 控制项 81202576

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088190.md`
