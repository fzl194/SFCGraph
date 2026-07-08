---
id: UNC@20.15.2@License@LKV2LTESAU02
type: License
name: 4G承载数
nf: UNC
version: 20.15.2
license_code: LKV2LTESAU02
control_item_id: '82205871'
applicable_nf:
- MME
status: active
---

# 4G承载数

`LKV2LTESAU02` · 控制项 82205871 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在系统中控制允许激活的4G承载数。

## 实现描述

系统中每激活一个4G承载，4G承载数加1；每去激活一个4G承载，总数减1。

## 取值范围

0～24000000 Bearer

## 默认值

10

## 应用场景

MME中激活4G承载。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
