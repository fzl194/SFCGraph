---
id: UNC@20.15.2@License@LKV2RCON01
type: License
name: 上下文回收管理
nf: UNC
version: 20.15.2
license_code: LKV2RCON01
control_item_id: 82200BNN
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# 上下文回收管理

`LKV2RCON01` · 控制项 82200BNN ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C、SMF

## 功能描述

上下文回收管理是指<br>UNC<br>主动回收PDU会话/EPS承载/PDP上下文资源，包括去激活空闲PDU会话/EPS承载/PDP上下文，以及手动去激活指定的PDU会话/EPS承载/PDP上下文。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

- 去激活空闲PDU会话/EPS承载/PDP上下文。<br>- 手动去激活PDU会话/EPS承载/PDP上下文。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205105 上下文回收管理

## 控制的能力

- [WSFD-205105](feature/UNC/20.15.2/WSFD-205105.md)  — 控制项 82200BNN

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
