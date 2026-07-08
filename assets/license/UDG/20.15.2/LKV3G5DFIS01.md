---
id: UDG@20.15.2@License@LKV3G5DFIS01
type: License
name: 磁盘故障隔离基本功能
nf: UDG
version: 20.15.2
license_code: LKV3G5DFIS01
control_item_id: '81203220'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 磁盘故障隔离基本功能

`LKV3G5DFIS01` · 控制项 81203220 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

磁盘故障隔离是指将业务Pod和共享磁盘进行解耦，磁盘故障的情况下，Pod运行不受影响，业务不受影响，提升VNF可靠性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

建议现网启用本特性，避免因共享磁盘故障导致业务受损的情况发生。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110482 磁盘故障隔离

## 控制的能力

- [GWFD-110482](feature/UDG/20.15.2/GWFD-110482.md)  — 控制项 81203220

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
