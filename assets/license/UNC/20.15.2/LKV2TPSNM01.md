---
id: UNC@20.15.2@License@LKV2TPSNM01
type: License
name: NRF每秒事务数
nf: UNC
version: 20.15.2
license_code: LKV2TPSNM01
control_item_id: '82209903'
applicable_nf:
- NRF
status: active
---

# NRF每秒事务数

`LKV2TPSNM01` · 控制项 82209903 ·  · 域 

## 归属/适用NF（原文）

NRF

## 功能描述

在系统中控制允许接入的消息对数量

## 实现描述

NF与NRF之间的每秒消息交互次数，一个来回（请求与回应、订阅与通知）记为1TPS。

## 取值范围

1~100000 TPS

## 默认值

1000

## 应用场景

NRF与其他NF的交互。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967909.md`
