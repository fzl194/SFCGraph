---
id: UDG@20.15.2@License@LKV3G5NBSP01
type: License
name: NB-IoT SGW-U&PGW-U基本功能Bearer上下文数
nf: UDG
version: 20.15.2
license_code: LKV3G5NBSP01
control_item_id: 82200CKU
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# NB-IoT SGW-U&PGW-U基本功能Bearer上下文数

`LKV3G5NBSP01` · 控制项 82200CKU · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U

## 功能描述

在系统中控制允许接入的SGW-U与PGW-U合一基本功能Bearer上下文数，允许接入的SGW-U与PGW-U合一基本功能Bearer上下文数最大值为【SGW-U基本功能Bearer上下文数】和【PGW-U基本功能Bearer上下文数】之间的较小值+【SGW-U&PGW-U基本功能Bearer上下文数】。

## 实现描述

系统中每激活一个SGW-U与PGW-U合一的Bearer上下文，SGW-U与PGW-U合一基本功能Bearer上下文数加一；每去激活一个SGW-U与PGW-U合一的Bearer上下文，SGW-U与PGW-U合一基本功能Bearer上下文数减一。<br>如果系统中已接入的SGW-U上下文数达到License中“SGW-U基本功能Bearer上下文数”与“SGW-U&PGW-U基本功能Bearer上下文数”之和，且话务峰值已经用完，则新的SGW-U上下文将无法接入到系统。如果系统中已接入的PGW-U上下文数达到License中“PGW-U基本功能Bearer上下文数”与“SGW-U&PGW-U基本功能Bearer上下文数”之和，且话务峰值已经用完，则新的PGW-U上下文将无法接入到系统。SGW-U与PGW-U合一的上下文数即为系统允许接入的SGW-U上下文数和PGW-U上下文数的较小值。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

NB-IoT SGW-U和PGW-U网元中合一Bearer上下文接入。

## 相关控制项（原文，未解释为边）

- NB-IoT SGW-U基本功能Bearer上下文数<br>- NB-IoT PGW-U基本功能Bearer上下文数

## 对应特性（原文）

GWFD-010296 NB-IoT终端标准接入

## 控制的能力

- [GWFD-010296](feature/UDG/20.15.2/GWFD-010296.md)  — 控制项 82200CKU

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
