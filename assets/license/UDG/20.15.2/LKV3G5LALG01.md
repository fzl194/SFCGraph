---
id: UDG@20.15.2@License@LKV3G5LALG01
type: License
name: 轻量化ALG-1 PDU Session
nf: UDG
version: 20.15.2
license_code: LKV3G5LALG01
control_item_id: 82200EQC
license_domain: UDG
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 轻量化ALG-1 PDU Session

`LKV3G5LALG01` · 控制项 82200EQC · resource · 域 UDG

## 归属/适用NF（原文）

UPF

## 功能描述

支持轻量化ALG功能

## 实现描述

系统中每激活一个需要进行轻量化业务的会话时，该License使用量加一；每去激活一个进行轻量化业务的会话时，该License使用量减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

用户进行轻量化业务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020531 通用DNN漫游分流

## 控制的能力

- [GWFD-020531](feature/UDG/20.15.2/GWFD-020531.md)  — 控制项 82200EQC

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
