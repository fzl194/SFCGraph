---
id: UDG@20.15.2@License@LKV3G5SSDUC1
type: License
name: SA特征库更新管控
nf: UDG
version: 20.15.2
license_code: LKV3G5SSDUC1
control_item_id: '81203996'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SA特征库更新管控

`LKV3G5SSDUC1` · 控制项 81203996 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

支持SA特征库更新功能。

## 实现描述

SA特征库更新功能受license控制，默认开启。<br>- License不开启时，不支持SA特征库更新功能。<br>- License开启时，支持SA特征库更新功能。

## 取值范围

0～1

## 默认值

1

## 应用场景

当需要实时更新SA特征库时，开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111600 SA特征库更新管控

## 控制的能力

- [GWFD-111600](feature/UDG/20.15.2/GWFD-111600.md)  — 控制项 81203996

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
