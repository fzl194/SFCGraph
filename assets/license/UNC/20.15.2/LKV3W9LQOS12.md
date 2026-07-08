---
id: UNC@20.15.2@License@LKV3W9LQOS12
type: License
name: 本地QOS控制
nf: UNC
version: 20.15.2
license_code: LKV3W9LQOS12
control_item_id: '82208342'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
status: active
---

# 本地QOS控制

`LKV3W9LQOS12` · 控制项 82208342 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C

## 功能描述

本地QoS控制是指<br>UNC<br>在本地配置基于全局或APN的QoS策略，对用户携带的QoS进行控制。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

UNC<br>使用本地QoS策略对用户QoS进行控制适用于以下场景：<br>- 用户业务激活时。<br>- 用户在线时发生RAT切换。<br>- 用户漫游属性更新时。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-109203 本地QOS控制

## 控制的能力

- [WSFD-109203](feature/UNC/20.15.2/WSFD-109203.md)  — 控制项 82208342

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
