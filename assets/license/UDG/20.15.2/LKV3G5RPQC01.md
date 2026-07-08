---
id: UDG@20.15.2@License@LKV3G5RPQC01
type: License
name: QUIC业务分析上报
nf: UDG
version: 20.15.2
license_code: LKV3G5RPQC01
control_item_id: 82200DXM
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# QUIC业务分析上报

`LKV3G5RPQC01` · 控制项 82200DXM · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制报表是否上报QUIC业务流量分析

## 实现描述

报表是否产生QUIC业务流量上报的单据受License控制。<br>License不开启时，报表不会产生QUIC业务流量的单据。<br>License开启时，报表产生QUIC业务流量的单据。

## 取值范围

10~8000000

## 默认值

10

## 应用场景

用户使用报表功能时，通过打开QUIC业务分析上报，来对QUIC业务进行信息收集和上报。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111019 QUIC业务分析上报

## 控制的能力

- [GWFD-111310](feature/UDG/20.15.2/GWFD-111310.md)  — 控制项 82200DXM

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
