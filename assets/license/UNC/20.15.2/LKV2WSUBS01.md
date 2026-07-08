---
id: UNC@20.15.2@License@LKV2WSUBS01
type: License
name: 3G附着用户数
nf: UNC
version: 20.15.2
license_code: LKV2WSUBS01
control_item_id: '82206535'
applicable_nf:
- SGSN
status: active
---

# 3G附着用户数

`LKV2WSUBS01` · 控制项 82206535 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

在系统中控制允许接入的3G动态用户数。

## 实现描述

系统中每接入（包括附着和跨系统RAU）一个3G用户，3G接入用户总数加一；每分离一个3G用户，3G接入用户总数减一。<br>如果系统中已接入的3G用户数达到License中“3G附着用户数”，且话务峰值已经用完，新的3G用户将无法接入到系统。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

SGSN网元中3G用户接入。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
