---
id: UDG@20.15.2@License@LKV3G5SURD01
type: License
name: 业务处理单元可靠性可定义基本功能
nf: UDG
version: 20.15.2
license_code: LKV3G5SURD01
control_item_id: '81203219'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 业务处理单元可靠性可定义基本功能

`LKV3G5SURD01` · 控制项 81203219 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

部署N个VM已能满足业务规格需要，为保证多个VM同时故障的情况下业务不受损，需要多部署M个VM。N+M个VM同时承载业务，当其中X（1<X<=M）个VM故障时，VNF通过业务迁移和CSDB_VNFC推送，使其他N+M-X个VM承担故障VM的业务，确保系统处理规格不下降。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~1

## 默认值

1

## 应用场景

为满足多个VM同时故障时，业务不受损，进一步提升VNF的可靠性，建议部署本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110481 业务处理单元可靠性可定义

## 控制的能力

- [GWFD-110481](feature/UDG/20.15.2/GWFD-110481.md)  — 控制项 81203219

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
