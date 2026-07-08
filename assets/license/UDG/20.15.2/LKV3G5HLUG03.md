---
id: UDG@20.15.2@License@LKV3G5HLUG03
type: License
name: 支持灰度升级无损回退
nf: UDG
version: 20.15.2
license_code: LKV3G5HLUG03
control_item_id: '81203938'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 支持灰度升级无损回退

`LKV3G5HLUG03` · 控制项 81203938 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制网元是否能进行灰度升级无损回退。

## 实现描述

灰度升级无损回退功能受license控制，默认开启。<br>- License不开启时，不支持灰度升级无损回退。<br>- License开启时，支持灰度升级无损回退。

## 取值范围

0～1

## 默认值

1

## 应用场景

当需要应用灰度升级无损回退时，开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111253 支持灰度升级无损回退

## 控制的能力

- [GWFD-111253](feature/UDG/20.15.2/GWFD-111253.md)  — 控制项 81203938

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
