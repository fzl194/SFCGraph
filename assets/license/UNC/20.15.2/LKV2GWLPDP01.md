---
id: UNC@20.15.2@License@LKV2GWLPDP01
type: License
name: 2.5G/3G/4G公共PDP/承载数
nf: UNC
version: 20.15.2
license_code: LKV2GWLPDP01
control_item_id: '82206541'
applicable_nf:
- SGSN
- MME
status: active
---

# 2.5G/3G/4G公共PDP/承载数

`LKV2GWLPDP01` · 控制项 82206541 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

在系统中控制允许激活的2.5G&3G&4G公共承载数。

## 实现描述

系统中每激活一个2.5G或3G或4G承载，2.5G&3G&4G公共承载数加1；每去激活一个2.5G或3G或4G承载，总数减1。

## 取值范围

0～24000000 Bearer

## 默认值

10

## 应用场景

SGSN/MME中激活2.5G或3G或4G承载。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
