---
id: UDG@20.15.2@License@LKV3G5DTTL01
type: License
name: Direct Tunnel功能
nf: UDG
version: 20.15.2
license_code: LKV3G5DTTL01
control_item_id: 82200BLC
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
status: active
---

# Direct Tunnel功能

`LKV3G5DTTL01` · 控制项 82200BLC · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U

## 功能描述

Direct Tunnel功能将RNC与SGSN、SGSN与PGW-C之间用户面的两段隧道（Two Tunnel）优化为一段隧道，优化后用户面转发不经过SGSN，而直接在RNC和PGW-U之间建立GTP-U隧道。

## 实现描述

License中Direct tunnel资源项为允许时，Direct tunnel功能生效；否则不生效。

## 取值范围

0～1

## 默认值

1

## 应用场景

需要直接在RNC和PGW-U之间建立GTP-U隧道。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020422 Direct Tunnel功能概述

## 控制的能力

- [GWFD-020422](feature/UDG/20.15.2/GWFD-020422.md)  — 控制项 82200BLC

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
