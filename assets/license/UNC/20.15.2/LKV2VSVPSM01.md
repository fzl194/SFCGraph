---
id: UNC@20.15.2@License@LKV2VSVPSM01
type: License
name: USM语音解决方案增值包-USM
nf: UNC
version: 20.15.2
license_code: LKV2VSVPSM01
control_item_id: 82200FDF
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# USM语音解决方案增值包-USM

`LKV2VSVPSM01` · 控制项 82200FDF ·  · 域 

## 归属/适用NF（原文）

SGW-C/PGW-C/SMF

## 功能描述

显示系统中接入的4G&5G NSA承载数。

## 实现描述

GW-C/SMF系统中每激活一个4G或5G NSA承载，该License总数加1；每去激活一个4G或5G NSA承载，总数减1。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

GW-C/SMF中激活4G或5G NSA承载。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
