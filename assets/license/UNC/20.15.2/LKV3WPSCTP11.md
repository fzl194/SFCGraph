---
id: UNC@20.15.2@License@LKV3WPSCTP11
type: License
name: SCTP
nf: UNC
version: 20.15.2
license_code: LKV3WPSCTP11
control_item_id: '82208353'
applicable_nf:
- GGSN-C
- PGW-C
status: active
---

# SCTP

`LKV3WPSCTP11` · 控制项 82208353 ·  · 域 

## 归属/适用NF（原文）

GGSN-C/PGW-C

## 功能描述

SCTP（Stream Control Transmission Protocol）是IETF RFC2960制定的面向连接的基于不可靠传输业务协议（如IP）之上的可靠的数据包传输协议。SCTP对TCP的缺陷进行了完善，使得信令传输具有更高的可靠性和更优的实时性。<br>GGSN/PGW-C支持SCTP功能，用于承载某些应用消息，如Diameter应用消息。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

当用户希望通过SCTP协议来增强网络、组网的可靠性和安全性时，可以使用该特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104508 SCTP

## 控制的能力

- [WSFD-104508](feature/UNC/20.15.2/WSFD-104508.md)  — 控制项 82208353

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
