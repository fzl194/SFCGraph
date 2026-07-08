---
id: UNC@20.15.2@License@LKV2NSASAU02
type: License
name: 5G NSA(Opt.3)承载数
nf: UNC
version: 20.15.2
license_code: LKV2NSASAU02
control_item_id: '82209135'
applicable_nf:
- MME
status: active
---

# 5G NSA(Opt.3)承载数

`LKV2NSASAU02` · 控制项 82209135 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在系统中控制允许激活的5G NSA(Opt.3)承载数。

## 实现描述

系统中每激活一个5G NSA(Opt.3)承载数，5G NSA(Opt.3)承载数加1；每去激活一个5G NSA(Opt.3)承载数，总数减1。

## 取值范围

0～24000000 Bearer

## 默认值

10

## 应用场景

MME网元中激活5G NSA(Opt.3)承载。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 控制的能力

- [WSFD-011501](feature/UNC/20.15.2/WSFD-011501.md)  — 控制项 82209135

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
