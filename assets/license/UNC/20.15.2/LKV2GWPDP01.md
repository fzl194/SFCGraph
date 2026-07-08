---
id: UNC@20.15.2@License@LKV2GWPDP01
type: License
name: 2.5G/3G公共PDP数
nf: UNC
version: 20.15.2
license_code: LKV2GWPDP01
control_item_id: '82206538'
applicable_nf:
- SGSN
status: active
---

# 2.5G/3G公共PDP数

`LKV2GWPDP01` · 控制项 82206538 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

在系统中控制允许激活的2.5G/3G公共PDP数，允许激活的2.5G PDP总数最大值为【2.5G PDP数】+【公共PDP数】；允许激活的3G PDP总数最大值为【3G PDP数】+【公共PDP数】。

## 实现描述

当2.5G激活PDP总数达到License中的“2.5G PDP数”后，系统中每激活一个2.5G PDP，公共PDP数加一；每去激活一个2.5G PDP，公共PDP数减一。<br>当3G激活PDP总数达到License中的“3G PDP数”后，系统中每激活一个3G PDP，公共PDP数加一；每去激活一个3G PDP，公共PDP数减一。<br>如果系统中已激活的2.5G PDP数达到License中“2.5G PDP数”、“公共PDP数”（需要减去已经被3G PDP占用的数量）之和，新的2.5G PDP将无法被激活。<br>如果系统中已激活的3G PDP数达到License中“3G PDP数”、“公共PDP数”（需要减去已经被2.5G PDP占用的数量）之和，新的3G PDP将无法被激活。<br>“公共PDP数”指2.5G/3G公共PDP数。

## 取值范围

0～24000000 PDP

## 默认值

10

## 应用场景

SGSN网元中2.5G或3G PDP激活。

## 相关控制项（原文，未解释为边）

- 2.5G PDP数<br>- 3G PDP数

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
