---
id: UDG@20.15.2@License@LKV3G5V6LI01
type: License
name: 逻辑接口支持IPv6
nf: UDG
version: 20.15.2
license_code: LKV3G5V6LI01
control_item_id: '81203214'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 逻辑接口支持IPv6

`LKV3G5V6LI01` · 控制项 81203214 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

在系统中控制逻辑接口支持IPv6功能。

## 实现描述

逻辑接口支持IPV6组网功能受license控制。<br>License不开启时，逻辑接口不支持IPV6组网功能。<br>License开启时，逻辑接口支持IPV6组网功能，支持IPV6功能license控制。

## 取值范围

0~1

## 默认值

1

## 应用场景

用户进行业务IPv6访问，网元通过逻辑接口支持IPv6组网，对用户IPv6业务进行支持。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020405 逻辑接口支持IPv6

## 控制的能力

- [GWFD-020405](feature/UDG/20.15.2/GWFD-020405.md)  — 控制项 81203214

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
