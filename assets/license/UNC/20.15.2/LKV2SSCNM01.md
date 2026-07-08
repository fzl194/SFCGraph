---
id: UNC@20.15.2@License@LKV2SSCNM01
type: License
name: 连接数
nf: UNC
version: 20.15.2
license_code: LKV2SSCNM01
control_item_id: '82209902'
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# 连接数

`LKV2SSCNM01` · 控制项 82209902 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C、SMF

## 功能描述

在系统中控制允许对接的UPF、SGW-U、PGW-U数量

## 实现描述

系统中每对接一个UPF、SGW-U或PGW-U，系统连接数加1；每断开一个UPF、SGW-U或PGW-U，系统连接数减1。

## 取值范围

0~4096 SSC

## 默认值

1

## 应用场景

SGW-C、PGW-C、SMF网元中对接SGW-U、PGW-U、UPF。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
