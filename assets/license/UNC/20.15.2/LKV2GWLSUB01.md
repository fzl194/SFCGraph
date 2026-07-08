---
id: UNC@20.15.2@License@LKV2GWLSUB01
type: License
name: 2.5G/3G/4G公共附着用户数
nf: UNC
version: 20.15.2
license_code: LKV2GWLSUB01
control_item_id: '82206540'
applicable_nf:
- SGSN
- MME
status: active
---

# 2.5G/3G/4G公共附着用户数

`LKV2GWLSUB01` · 控制项 82206540 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

在系统中控制允许接入的2.5G&3G&4G动态用户数。

## 实现描述

SGSN/MME系统中每接入一个2.5G或3G或4G用户，2.5G&3G&4G公共附着用户总数加1；每分离一个2.5G或3G或4G用户，2.5G&3G&4G公共附着用户总数减1。<br>如果系统中已接入的2.5G&3G&4G公共附着动态用户数达到License中“2.5G&3G&4G公共附着用户数”，且话务峰值已经用完，新的用户将无法接入到系统。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

SGSN/MME网元中2.5G或3G或4G用户接入。

## 相关控制项（原文，未解释为边）

NAS信令加密与完整性保护

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
