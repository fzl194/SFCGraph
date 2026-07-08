---
id: UNC@20.15.2@License@LKV2DIRTUN02
type: License
name: 支持Direct Tunnel功能
nf: UNC
version: 20.15.2
license_code: LKV2DIRTUN02
control_item_id: '82206557'
applicable_nf:
- SGSN
status: active
---

# 支持Direct Tunnel功能

`LKV2DIRTUN02` · 控制项 82206557 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

随着3G业务不断的开展，以及HSPA等技术的应用，UMTS网络越来越需要提高用户面处理能力。原有的网络是分别在RNC与SGSN、SGSN与GGSN-U之间建立GTP-U通道的（Indirect Tunnel）。为此，RNC、SGSN以及GGSN-U等网元需要同时增强相应的用户面处理性能，这样会增加运营商的资金投入和运营成本。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~12000000 SAU

## 默认值

10

## 应用场景

为了减少运营商的投资费用和运营费用，以及便于后续的网络扩容，3GPP提出了Direct Tunnel解决方案。Direct Tunnel功能将RNC与SGSN、SGSN与GGSN-U之间用户面的两段隧道（Indirect Tunnel）优化为一段隧道，优化后用户面转发不经过SGSN，而直接在RNC和GGSN-U之间建立GTP-U隧道，通过节省用户面资源降低了运营商的资金投入和运营成本，同时也优化了UMTS网络用户面的性能。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104506 支持Direct Tunnel功能

## 控制的能力

- [WSFD-104506](feature/UNC/20.15.2/WSFD-104506.md)  — 控制项 82206557

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
