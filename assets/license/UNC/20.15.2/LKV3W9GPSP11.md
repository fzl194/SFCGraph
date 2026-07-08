---
id: UNC@20.15.2@License@LKV3W9GPSP11
type: License
name: GGSN/P-GW信令代理
nf: UNC
version: 20.15.2
license_code: LKV3W9GPSP11
control_item_id: '81202991'
applicable_nf:
- GGSN-C
- PGW-C
status: active
---

# GGSN/P-GW信令代理

`LKV3W9GPSP11` · 控制项 81202991 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C

## 功能描述

关口局的GGSN/P-GW在漫游用户的整个激活过程中作为中间转发站的角色，即作为GGSN/P-GW代理（GGSN/P-GW Proxy），将漫游用户的激活请求消息路由到归属地的GGSN/P-GW，由归属地GGSN/P-GW直接处理漫游用户的激活请求以及随后的各种业务，从而解决了漫游用户无法使用某些归属地特殊业务的问题。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

0

## 应用场景

当运营商需要GGSN/P-GW承担Proxy的作用，将漫游用户的激活上下文请求消息路由到归属地的GGSN/P-GW，由归属地GGSN/P-GW直接处理漫游用户的激活请求以及随后的各种业务时，需要配置GGSN/P-GW信令代理特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205107 GGSN/P-GW信令代理

## 控制的能力

- [WSFD-205107](feature/UNC/20.15.2/WSFD-205107.md)  — 控制项 81202991

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15408046.md`
