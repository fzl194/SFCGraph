---
id: UNC@20.15.2@License@LKV2NSASAU01
type: License
name: 5G NSA(Opt.3)附着用户数
nf: UNC
version: 20.15.2
license_code: LKV2NSASAU01
control_item_id: '82209133'
applicable_nf:
- MME
status: active
---

# 5G NSA(Opt.3)附着用户数

`LKV2NSASAU01` · 控制项 82209133 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在系统中控制允许接入的5G NSA(Opt.3)动态用户数。

## 实现描述

MME系统中每接入一个5G NSA(Opt.3)用户，5G NSA(Opt.3) 接入用户总数加1；每分离一个5G NSA(Opt.3)用户，5G NSA(Opt.3)接入用户总数减1。如果系统中已接入的5G NSA(Opt.3)动态用户数达到License中“5G NSA(Opt.3)接入用户数”，且话务峰值已经用完，新的5G NSA(Opt.3)用户将无法接入到系统。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

MME网元中5G NSA(Opt.3)用户接入。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 控制的能力

- [WSFD-011501](feature/UNC/20.15.2/WSFD-011501.md)  — 控制项 82209133
- [WSFD-011503](feature/UNC/20.15.2/WSFD-011503.md)  — 控制项 82209133

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
