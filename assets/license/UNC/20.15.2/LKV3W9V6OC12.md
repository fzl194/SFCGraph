---
id: UNC@20.15.2@License@LKV3W9V6OC12
type: License
name: IPv6 在线计费
nf: UNC
version: 20.15.2
license_code: LKV3W9V6OC12
control_item_id: '82208001'
applicable_nf:
- GGSN-C
- PGW-C
status: active
---

# IPv6 在线计费

`LKV3W9V6OC12` · 控制项 82208001 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C

## 功能描述

UNC支持对IPv6用户/IPv4v6双栈用户的数据流进行在线计费，包括内容计费和非内容计费。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

- IPv6在线非内容计费：不区分业务类型进行统一费率计费。<br>- IPv6在线内容计费：区分业务类型采取不同的费率计费。

## 相关控制项（原文，未解释为边）

依赖WSFD-104001 IPv6承载上下文和WSFD-109001 Gy/Diameter在线计费

## 对应特性（原文）

WSFD-104003 IPv6 在线计费

## 控制的能力

- [WSFD-104003](feature/UNC/20.15.2/WSFD-104003.md)  — 控制项 82208001

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
