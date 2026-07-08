---
id: UDG@20.15.2@License@LKV3G5PCRR01
type: License
name: PCC规则报表
nf: UDG
version: 20.15.2
license_code: LKV3G5PCRR01
control_item_id: 82200DHX
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# PCC规则报表

`LKV3G5PCRR01` · 控制项 82200DHX · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制报表是否上报PCC规则信息

## 实现描述

报表是否上报Rule的单据受License控制。<br>License 不开启时，报表不产生 Rule 单据。<br>License 开启时，报表产生 Rule 单据。

## 取值范围

0~8000000

## 默认值

10

## 应用场景

用户使用报表功能时，通过打开PCC规则信息上报，来对Rule业务进行信息收集和上报。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111018 PCC规则报表

## 控制的能力

- [GWFD-111309](feature/UDG/20.15.2/GWFD-111309.md)  — 控制项 82200DHX

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
