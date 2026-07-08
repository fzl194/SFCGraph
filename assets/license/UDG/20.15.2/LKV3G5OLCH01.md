---
id: UDG@20.15.2@License@LKV3G5OLCH01
type: License
name: 在线计费
nf: UDG
version: 20.15.2
license_code: LKV3G5OLCH01
control_item_id: '82209821'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 在线计费

`LKV3G5OLCH01` · 控制项 82209821 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

在线计费是一种实时计费，当用户发起数据业务时，在线计费系统根据用户信息和用户帐户中的情况授权是否下发该用户进行分组数据业务的配额（流量、时间或事件），并实时跟踪用户对所购资源的使用情况，从帐户余额中扣除当前消耗的配额，帐户资金用尽时终止用户业务。本控制项控制在线计费对应的Bearer上下文数。

## 实现描述

当用户激活在线计费的Bearer上下文时，“在线计费功能Bearer上下文数”加一，当去活一个在线计费的Bearer上下文，“在线计费功能Bearer上下文数”减一。<br>如果系统中已激活的在线计费功能Bearer上下文数达到License中“在线计费”，新的在线计费Bearer上下文将无法激活。<br>例如：“在线计费”License为200，系统中当前已激活的在线计费Bearer上下文数为200，则此时新的在线计费Bearer上下文将无法激活。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

在线计费用户Bearer上下文激活。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020300 在线计费

## 控制的能力

- [GWFD-020300](feature/UDG/20.15.2/GWFD-020300.md)  — 控制项 82209821

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
