---
id: UNC@20.15.2@License@LKV2GPDP01
type: License
name: 2.5G PDP数
nf: UNC
version: 20.15.2
license_code: LKV2GPDP01
control_item_id: '82206534'
applicable_nf:
- SGSN
status: active
---

# 2.5G PDP数

`LKV2GPDP01` · 控制项 82206534 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

在系统中控制允许激活的2.5G PDP数。

## 实现描述

系统中每激活一个2.5G PDP，2.5G激活PDP总数加一；每去激活一个2.5G PDP，2.5G激活PDP总数减一。<br>如果系统中已激活的2.5G PDP数达到License中“2.5G PDP数”，且话务峰值已经用完，新的2.5G PDP将无法被激活。

## 取值范围

0～24000000 PDP

## 默认值

10

## 应用场景

SGSN网元中2.5G PDP激活。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
