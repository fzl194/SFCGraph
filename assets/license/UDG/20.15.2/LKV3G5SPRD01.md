---
id: UDG@20.15.2@License@LKV3G5SPRD01
type: License
name: 业务处理单元可靠性可定义
nf: UDG
version: 20.15.2
license_code: LKV3G5SPRD01
control_item_id: 82200ECT
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 业务处理单元可靠性可定义

`LKV3G5SPRD01` · 控制项 82200ECT · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

部署N个Pod已能满足业务规格需要，为保证多个Pod同时故障的情况下业务不受损，需要多部署M个Pod。N+M个Pod同时承载业务，当其中X（1<X<=M）个Pod故障时，VNF通过业务迁移，使其他N+M-X个Pod承担故障Pod的业务，确保系统处理规格不下降。

## 实现描述

加载了支持本特性的license文件，本特性即可生效，无需进行配置。

## 取值范围

0～100000

## 默认值

10

## 应用场景

为满足多个Pod同时故障时，业务不受损，进一步提升VNF的可靠性，建议部署本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110481 业务处理单元可靠性可定义

## 控制的能力

- [GWFD-110481](feature/UDG/20.15.2/GWFD-110481.md)  — 控制项 82200ECT

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
