---
id: UDG@20.15.2@License@LKV3G55GHT01
type: License
name: 5G-A高通量会话
nf: UDG
version: 20.15.2
license_code: LKV3G55GHT01
control_item_id: 82200HTM
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 5G-A高通量会话

`LKV3G55GHT01` · 控制项 82200HTM · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

在系统中控制允许接入的5G-A高通量承载上下文数。

## 实现描述

系统中每激活一个5G-A高通量承载上下文，该License使用量加一。每去激活一个5G-A高通量承载上下文，该License使用量减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

5G-A高通量承载上下文接入

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-112002 5G-A高通量会话

## 控制的能力

- [GWFD-112002](feature/UDG/20.15.2/GWFD-112002.md)  — 控制项 82200HTM

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
