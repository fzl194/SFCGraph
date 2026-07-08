---
id: UNC@20.15.2@License@LKV4W9BNC501
type: License
name: SGW-C&PGW-C 5G NSA基本功能PDP上下文数
nf: UNC
version: 20.15.2
license_code: LKV4W9BNC501
control_item_id: '82209235'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# SGW-C&PGW-C 5G NSA基本功能PDP上下文数

`LKV4W9BNC501` · 控制项 82209235 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

在系统中控制允许接入的SGW-C与PGW-C合一5G NSA基本功能PDP上下文数，允许接入的SGW-C与PGW-C合一5G NSA基本功能PDP上下文数最大值为【SGW-C 5G NSA基本功能PDP上下文数】和【PGW-C 5G NSA基本功能PDP上下文数】之间的较小值+【SGW-C&PGW-C 5G NSA基本功能PDP上下文数】。

## 实现描述

系统中每激活一个SGW-C与PGW-C合一的5G NSA PDP上下文，SGW-C与PGW-C合一5G NSA基本功能PDP上下文数加1；每去激活一个SGW-C与PGW-C合一的5G NSA PDP上下文，SGW-C与PGW-C合一5G NSA基本功能PDP上下文数减1。<br>如果系统中已接入的SGW-C 5G NSA基本功能PDP上下文数达到License中“SGW-C 5G NSA基本功能PDP上下文数”与“SGW-C&PGW-C 5G NSA基本功能PDP上下文数”之和，则新的SGW-C 5G NSA基本功能PDP上下文将无法接入到系统。如果系统中已接入的PGW-C 5G NSA基本功能PDP上下文数达到License中“PGW-C 5G NSA基本功能PDP上下文”与“SGW-C&PGW-C 5G NSA基本功能PDP上下文”之和，则新的PGW-C 5G NSA基本功能PDP上下文将无法接入到系统。SGW-C与PGW-C合一的5G NSA基本功能PDP上下文数即为系统允许接入的SGW-C 5G NSA基本功能PDP上下文数和PGW-C 5G NSA基本功能PDP上下文数的较小值。<br>例如：“SGW-C 5G NSA基本功能PDP上下文数”License为1000，“PGW-C 5G NSA基本功能PDP上下文数”License为1000，“SGW-C&PGW-C 5G NSA基本功能PDP上下文数”License为1000；系统中当前已接入的SGW-C与PGW-C合一的5G NSA基本功能PDP上下文数超过2000，那么“SGW-C&PGW-C 5G NSA基本功能PDP上下文数”License全部被SGW-C与PGW-C合一的5G NSA基本功能PDP上下文占用，“SGW-C 5G NSA基本功能PDP上下文数”License全部被SGW-C与PGW-C合一的5G NSA基本功能PDP上下文占用，“PGW-C 5G NSA基本功能PDP上下文数”License全部被SGW-C与PGW-C合一的5G NSA基本功能PDP上下文占用。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

SGW-C和PGW-C网元中合一PDP上下文NSA接入。

## 相关控制项（原文，未解释为边）

- SGW-C 5G NSA基本功能PDP上下文数<br>- PGW-C 5G NSA基本功能PDP上下文数

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
