---
id: UDG@20.15.2@License@LKV3G5TBCS01
type: License
name: 基于业务时长的计费
nf: UDG
version: 20.15.2
license_code: LKV3G5TBCS01
control_item_id: '82209823'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 基于业务时长的计费

`LKV3G5TBCS01` · 控制项 82209823 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

基于业务时长的计费是在业务识别解析的基础上，针对该业务使用时长进行计费。本控制项控制支持业务时长计费功能Bearer上下文数。

## 实现描述

该License项未用尽时，允许激活业务时长计费的Bearer上下文；该License项用尽时，或者License文件过期后，不允许激活业务时长计费的Bearer上下文。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

基于业务时长计费的用户Bearer上下文激活。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020302 基于业务时长的计费

## 控制的能力

- [GWFD-020302](feature/UDG/20.15.2/GWFD-020302.md)  — 控制项 82209823

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
