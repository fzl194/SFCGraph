---
id: UNC@20.15.2@License@LKV2TOTSUBAM01
type: License
name: 总用户数
nf: UNC
version: 20.15.2
license_code: LKV2TOTSUBAM01
control_item_id: 82200FSJ
applicable_nf:
- AMF
- MME
- SGSN
status: active
---

# 总用户数

`LKV2TOTSUBAM01` · 控制项 82200FSJ ·  · 域 

## 归属/适用NF（原文）

AMF/MME/SGSN

## 功能描述

显示系统中接入的2G&3G&4G&NB-IoT&5G NSA(Opt.3)&5G用户数。

## 实现描述

AMF/MME/SGSN系统中每接入一个2G&3G&4G&NB-IoT&5G NSA(Opt.3)&5G用户，该License总数加1；每分离一个2G&3G&4G&NB-IoT&5G NSA(Opt.3)&5G用户，总数减1。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

AMF/MME/SGSN中接入的2G&3G&4G&NB-IoT&5G NSA(Opt.3)&5G用户数。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
