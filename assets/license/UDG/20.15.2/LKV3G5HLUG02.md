---
id: UDG@20.15.2@License@LKV3G5HLUG02
type: License
name: 支持灰度拨测和发布
nf: UDG
version: 20.15.2
license_code: LKV3G5HLUG02
control_item_id: '81203937'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 支持灰度拨测和发布

`LKV3G5HLUG02` · 控制项 81203937 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制网元是否能进行灰度拨测和发布。

## 实现描述

灰度拨测和发布功能受license控制。<br>- License不开启时，不支持灰度拨测和发布。<br>- License开启时，支持灰度拨测和发布。

## 取值范围

0～1

## 默认值

1

## 应用场景

当需要应用灰度拨测和发布时，开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111252 支持灰度拨测和发布

## 控制的能力

- [GWFD-111252](feature/UDG/20.15.2/GWFD-111252.md)  — 控制项 81203937

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
