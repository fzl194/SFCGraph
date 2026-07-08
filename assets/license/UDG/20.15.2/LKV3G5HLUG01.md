---
id: UDG@20.15.2@License@LKV3G5HLUG01
type: License
name: 灰度升级解决方案增值包基本功能
nf: UDG
version: 20.15.2
license_code: LKV3G5HLUG01
control_item_id: '81203630'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 灰度升级解决方案增值包基本功能

`LKV3G5HLUG01` · 控制项 81203630 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制网元是否能进行在线升级。

## 实现描述

在线升级流程受license控制。<br>- License不开启时，在线升级失败。<br>- License开启时，在线升级可正常进行。

## 取值范围

0～1

## 默认值

1

## 应用场景

当需要应用在线升级时，开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111251 在线升级

## 控制的能力

- [GWFD-111251](feature/UDG/20.15.2/GWFD-111251.md)  — 控制项 81203630

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
