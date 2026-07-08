---
id: UNC@20.15.2@License@LKV4W9BNPC51
type: License
name: PGW-C 5G NSA基本功能PDP上下文数
nf: UNC
version: 20.15.2
license_code: LKV4W9BNPC51
control_item_id: '82209234'
applicable_nf:
- PGW-C
status: active
---

# PGW-C 5G NSA基本功能PDP上下文数

`LKV4W9BNPC51` · 控制项 82209234 ·  · 域 

## 归属/适用NF（原文）

PGW-C

## 功能描述

在系统中控制允许接入的PGW-C 5G NSA基本功能PDP上下文数，允许接入的PGW-C 5G NSA基本功能PDP上下文数最大值为【PGW-C 5G NSA基本功能PDP上下文数】+【SGW-C&PGW-C 5G NSA基本功能PDP上下文数】。

## 实现描述

系统中每激活一个PGW-C的5G NSA PDP上下文，PGW-C 5G NSA基本功能PDP上下文数加1；每去激活一个PGW-C的5G NSA PDP上下文，PGW-C 5G NSA基本功能PDP上下文数减1。<br>如果系统中已接入的PGW-C的5G NSA基本功能PDP上下文数加上SGW-C与PGW-C合一的5G NSA基本功能PDP上下文数，达到License中“PGW-C 5G NSA基本功能PDP上下文数”、“SGW-C&PGW-C 5G NSA基本功能PDP上下文数”，新的PGW-C 5G NSA基本功能PDP上下文将无法接入到系统。<br>例如：“PGW-C 5G NSA基本功能PDP上下文数”License为1000，“SGW-C&PGW-C 5G NSA基本功能PDP上下文数”License为1000；系统中当前已接入的PGW-C的5G NSA基本功能PDP上下文数超过2000，那么“SGW-C&PGW-C 5G NSA基本功能PDP上下文数”License全部被PGW-C的5G NSA基本功能PDP上下文占用。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

PGW-C网元中PDP上下文NSA接入。

## 相关控制项（原文，未解释为边）

- SGW-C&PGW-C 5G NSA基本功能PDP上下文数

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
