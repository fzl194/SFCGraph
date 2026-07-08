---
id: UNC@20.15.2@License@LKV3W9DHCP12
type: License
name: DHCP功能
nf: UNC
version: 20.15.2
license_code: LKV3W9DHCP12
control_item_id: '82209430'
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# DHCP功能

`LKV3W9DHCP12` · 控制项 82209430 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

用户所分配的IPv4地址是在PDN/PDU会话激活阶段从企业网或者运营商独立维护的DHCPv4服务器上配置的地址池中获取的动态IP地址。

## 实现描述

系统中每激活一个DHCPv4分配地址的PDN/PDU会话，支持DHCP分配地址功能PDN/PDU会话数的总数加一；每去激活一个DHCPv4分配地址的PDN/PDU会话，DHCP分配地址功能PDN/PDU会话的总数减一。如果系统中已接入的DHCPv4分配地址的PDN/PDU会话数达到License中“DHCP功能”的最大值，新的PDN/PDU会话无法通过DHCPv4分配地址的方式激活。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

DHCPv4地址分配适用于运营商管理大量地址池，也可以用于企业网或者ISP自己管理地址池，供分配IPv4地址使用。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104413 DHCP功能

## 控制的能力

- [WSFD-104413](feature/UNC/20.15.2/WSFD-104413.md)  — 控制项 82209430

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
