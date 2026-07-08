---
id: UNC@20.15.2@License@LKV3W9SBWL11
type: License
name: SGSN的黑白名单
nf: UNC
version: 20.15.2
license_code: LKV3W9SBWL11
control_item_id: '82208355'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
status: active
---

# SGSN的黑白名单

`LKV3W9SBWL11` · 控制项 82208355 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C

## 功能描述

SGSN的黑白名单是指设定一个IP地址范围，禁止或允许该IP地址范围内的SGSN接入。

## 实现描述

License中SGSN的黑白名单功能项为允许时，SGSN的黑白名单功能生效；否则不生效。

## 取值范围

0～16000000 PDP

## 默认值

10

## 应用场景

当运营商部署分组交换网，新增GGSN或SGSN，以及SGSN的IP地址变更时，需要在GGSN上配置SGSN的黑白名单，用来对SGSN进行接入控制。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-104509 SGSN的黑白名单

## 控制的能力

- [WSFD-104509](feature/UNC/20.15.2/WSFD-104509.md)  — 控制项 82208355

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
