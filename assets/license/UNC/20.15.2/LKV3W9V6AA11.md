---
id: UNC@20.15.2@License@LKV3W9V6AA11
type: License
name: DHCPv6地址分配
nf: UNC
version: 20.15.2
license_code: LKV3W9V6AA11
control_item_id: '82209423'
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# DHCPv6地址分配

`LKV3W9V6AA11` · 控制项 82209423 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

用户所分配的IPv6地址是在PDN/PDU会话激活阶段从企业网或者运营商独立维护的DHCPv6服务器上配置的地址池中获取的动态IPv6地址。

## 实现描述

系统中每激活一个DHCPv6分配地址的PDN/PDU会话，支持DHCPv6分配地址功能PDN/PDU会话数的总数加一；每去激活一个DHCPv6分配地址的PDN/PDU会话，DHCPv6分配地址功能PDN/PDU会话的总数减一。如果系统中已接入的DHCPv6分配地址的PDN/PDU会话数达到License中“DHCPv6地址分配”的最大值，新的PDN/PDU会话无法通过DHCPv6分配地址的方式激活。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

DHCPv6地址分配适用于运营商管理大量地址池，也可以用于企业网或者ISP自己管理地址池，供分配IPv6地址使用。

## 相关控制项（原文，未解释为边）

WSFD-104001 IPv6承载上下文

## 对应特性（原文）

WSFD-104005 DHCPv6地址分配

## 控制的能力

- [WSFD-104005](feature/UNC/20.15.2/WSFD-104005.md)  — 控制项 82209423

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
