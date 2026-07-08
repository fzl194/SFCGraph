---
id: UNC@20.15.2@License@LKV4W9BNSC01
type: License
name: SGW-C 4G基本功能Bearer数
nf: UNC
version: 20.15.2
license_code: LKV4W9BNSC01
control_item_id: '82208017'
applicable_nf:
- SGW-C
status: active
---

# SGW-C 4G基本功能Bearer数

`LKV4W9BNSC01` · 控制项 82208017 ·  · 域 

## 归属/适用NF（原文）

SGW-C

## 功能描述

在系统中控制允许接入的SGW-C基本功能PDP上下文数，允许接入的SGW-C基本功能PDP上下文数最大值为【SGW-C-4G基本功能PDP上下文数】+【SGW-C&PGW-C 4G基本功能PDP上下文数】。

## 实现描述

系统中每激活一个SGW-C的PDP上下文，SGW-C基本功能PDP上下文数加1；每去激活一个SGW-C的PDP上下文，SGW-C基本功能PDP上下文数减1。<br>如果系统中已接入的SGW-C的PDP上下文数加上SGW-C与PGW-C合一的PDP上下文数，达到License中“SGW-C-4G基本功能PDP上下文数”、“SGW-C&PGW-C 4G基本功能PDP上下文数”，新的SGW-C上下文将无法接入到系统。<br>例如：“SGW-C-4G基本功能PDP上下文数”License为1000，“SGW-C&PGW-C 4G基本功能PDP上下文数”License为1000；系统中当前已接入的SGW-C的PDP上下文数超过2000，那么“SGW-C&PGW-C 4G基本功能PDP上下文数”License全部被SGW-C的PDP上下文占用。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

SGW-C网元中PDP上下文接入。

## 相关控制项（原文，未解释为边）

SGW-C&PGW-C 4G基本功能PDP上下文数

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15408090.md`
