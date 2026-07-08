---
id: UNC@20.15.2@License@LKV3W9RBMS12
type: License
name: 支持Routing Behind MS
nf: UNC
version: 20.15.2
license_code: LKV3W9RBMS12
control_item_id: '82207993'
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# 支持Routing Behind MS

`LKV3W9RBMS12` · 控制项 82207993 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

在系统中控制允许接入的Routing Behind MS上下文数。

## 实现描述

系统中每激活一个Routing Behind MS上下文，Routing Behind MS上下文总数加一；每去激活一个Routing Behind MS上下文，Routing Behind MS上下文总数减一。<br>如果系统中已接入的Routing Behind MS上下文数达到License中“Routing Behind MS”的最大值，新的Routing Behind MS上下文将无法接入到系统。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

Routing Behind MS主要服务于企业的移动VPN用户。

## 相关控制项（原文，未解释为边）

依赖WSFD-104410 L2TP VPN

## 对应特性（原文）

WSFD-205101 Routing Behind MS

## 控制的能力

- [WSFD-205101](feature/UNC/20.15.2/WSFD-205101.md)  — 控制项 82207993

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
