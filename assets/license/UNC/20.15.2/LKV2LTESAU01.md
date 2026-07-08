---
id: UNC@20.15.2@License@LKV2LTESAU01
type: License
name: 4G附着用户数
nf: UNC
version: 20.15.2
license_code: LKV2LTESAU01
control_item_id: '82205870'
applicable_nf:
- MME
status: active
---

# 4G附着用户数

`LKV2LTESAU01` · 控制项 82205870 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在系统中控制允许接入的4G动态用户数。

## 实现描述

MME系统中每接入一个4G用户，4G接入用户总数加1；每分离一个4G用户，4G接入用户总数减1。<br>如果系统中已接入的4G动态用户数达到License中“4G接入用户数”，且话务峰值已经用完，新的4G用户将无法接入到系统。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

MME网元中4G用户接入。

## 相关控制项（原文，未解释为边）

NAS信令加密与完整性保护

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
