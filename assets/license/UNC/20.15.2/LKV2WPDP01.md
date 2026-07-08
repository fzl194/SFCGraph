---
id: UNC@20.15.2@License@LKV2WPDP01
type: License
name: 3G PDP数
nf: UNC
version: 20.15.2
license_code: LKV2WPDP01
control_item_id: '82206536'
applicable_nf:
- SGSN
status: active
---

# 3G PDP数

`LKV2WPDP01` · 控制项 82206536 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

在系统中控制允许激活的3G PDP数。

## 实现描述

系统中每激活一个3G PDP，3G激活PDP总数加一；每去激活一个3G PDP，3G激活PDP总数减一。<br>如果系统中已激活的3G PDP数达到License中“3G PDP数”，且话务峰值已经用完，新的3G PDP将无法被激活。

## 取值范围

0～24000000 PDP

## 默认值

10

## 应用场景

SGSN网元中3G PDP激活。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
