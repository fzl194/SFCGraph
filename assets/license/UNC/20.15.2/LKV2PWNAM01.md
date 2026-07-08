---
id: UNC@20.15.2@License@LKV2PWNAM01
type: License
name: 5G高速承载增值包基本功能-UAM
nf: UNC
version: 20.15.2
license_code: LKV2PWNAM01
control_item_id: 82200JHT
applicable_nf:
- AMF
- MME
status: active
---

# 5G高速承载增值包基本功能-UAM

`LKV2PWNAM01` · 控制项 82200JHT ·  · 域 

## 归属/适用NF（原文）

AMF/MME

## 功能描述

显示系统中接入的NSA&5G用户数。

## 实现描述

AMF/MME系统中每接入一个NSA或5G用户，该License总数加1；每分离一个NSA或5G用户，总数减1。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

AMF/MME中接入的NSA&5G用户数。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848073.md`
