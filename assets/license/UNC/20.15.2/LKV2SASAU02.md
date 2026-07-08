---
id: UNC@20.15.2@License@LKV2SASAU02
type: License
name: 5G SA承载数
nf: UNC
version: 20.15.2
license_code: LKV2SASAU02
control_item_id: '82209899'
applicable_nf:
- SMF
status: active
---

# 5G SA承载数

`LKV2SASAU02` · 控制项 82209899 ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

在系统中控制允许激活的5G SA承载数。

## 实现描述

系统中每激活一个5G SA承载，5G SA承载数加1；每去激活一个5G SA承载，总数减1。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

SMF中激活5G SA承载。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
