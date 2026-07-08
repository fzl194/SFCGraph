---
id: UNC@20.15.2@License@LKV2MPVPN01
type: License
name: MPLS VPN
nf: UNC
version: 20.15.2
license_code: LKV2MPVPN01
control_item_id: '81203325'
applicable_nf:
- SGSN
- MME
- SGW-C
- PGW-C
- AMF
- SMF
status: active
---

# MPLS VPN

`LKV2MPVPN01` · 控制项 81203325 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME/SGW-C/PGW-C/AMF/SMF

## 功能描述

MPLS VPN是一种L3VPN（Layer 3 Virtual Private Network），它使用BGP（Border Gateway Protocol）在服务提供商骨干网上发布VPN路由，使用MPLS（Multiprotocol Label Switch）在服务提供商骨干网上转发VPN报文。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

FENIX<br>支持的MPLS VPN的典型组网有以下几种：<br>- Intranet<br>- Extranet<br>- Hub&Spoke<br>- 跨域VPN<br>- Multi-VPN-Instance CE<br>- VPN与Internet互联

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104411 MPLS VPN

## 控制的能力

- [WSFD-104411](feature/UNC/20.15.2/WSFD-104411.md)  — 控制项 81203325

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568026.md`
