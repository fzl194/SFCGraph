---
id: UDG@20.15.2@License@LKV3G5WOFR01
type: License
name: 基于业务流标识的无线资源优化
nf: UDG
version: 20.15.2
license_code: LKV3G5WOFR01
control_item_id: 82200DHE
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 基于业务流标识的无线资源优化

`LKV3G5WOFR01` · 控制项 82200DHE · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

在系统中控制允许接入的具有业务流标识的无线资源优化功能的承载数

## 实现描述

系统中每激活一个具有业务流标识的无线资源优化功能的承载，基于业务流标识的无线资源优化对应的承载数加一；每去激活一个具有业务流标识的无线资源优化功能的承载，基于业务流标识的无线资源优化对应的承载数减一。

## 取值范围

0~16000000

## 默认值

10

## 应用场景

根据license状态，控制本地用户是否可以激活为具有业务流标识的无线资源优化功能的用户。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110331 基于业务流标识的无线资源优化

## 控制的能力

- [GWFD-110331](feature/UDG/20.15.2/GWFD-110331.md)  — 控制项 82200DHE

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
