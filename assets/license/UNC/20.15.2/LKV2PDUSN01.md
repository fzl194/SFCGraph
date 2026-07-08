---
id: UNC@20.15.2@License@LKV2PDUSN01
type: License
name: AMF PDU会话数
nf: UNC
version: 20.15.2
license_code: LKV2PDUSN01
control_item_id: 82200BWA
applicable_nf:
- AMF
status: active
---

# AMF PDU会话数

`LKV2PDUSN01` · 控制项 82200BWA ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

在系统中控制允许接入的AMF PDU会话数量

## 实现描述

系统中每接入一个PDU会话，AMF PDU会话数加1；每断开一个PDU会话，AMF PDU会话数减1。

## 取值范围

10000~24000000 Session

## 默认值

10

## 应用场景

AMF需要控制接入PDU会话数量时

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
