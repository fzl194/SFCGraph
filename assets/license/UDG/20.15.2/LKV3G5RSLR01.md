---
id: UDG@20.15.2@License@LKV3G5RSLR01
type: License
name: 用户实时位置分析上报
nf: UDG
version: 20.15.2
license_code: LKV3G5RSLR01
control_item_id: 82200CXQ
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 用户实时位置分析上报

`LKV3G5RSLR01` · 控制项 82200CXQ · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制报表是否上报用户实时位置分析。

## 实现描述

报表是否产生用户实时位置的单据受该License控制。<br>License不开启时，报表不会产生用户实时位置的单据。<br>License开启时，报表会产生用户实时位置的单据。

## 取值范围

10~8000000

## 默认值

10

## 应用场景

用户使用报表功能时，通过打开用户实时位置分析，来对用户实时位置分析业务进行信息收集和上报。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111014 用户实时位置分析上报

## 控制的能力

- [GWFD-111305](feature/UDG/20.15.2/GWFD-111305.md)  — 控制项 82200CXQ

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
