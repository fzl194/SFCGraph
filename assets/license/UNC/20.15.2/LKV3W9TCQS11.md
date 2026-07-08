---
id: UNC@20.15.2@License@LKV3W9TCQS11
type: License
name: 会话类QOS保证
nf: UNC
version: 20.15.2
license_code: LKV3W9TCQS11
control_item_id: '82207987'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
status: active
---

# 会话类QOS保证

`LKV3W9TCQS11` · 控制项 82207987 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C

## 功能描述

会话类QoS保证是指<br>UNC<br>在用户数据传输时通过识别会话类业务，进而通过流分类、QoS标记、带宽控制、高优先级队列发送等手段保证会话类业务的数据转发满足其QoS需求。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

VOIP、视频电话、视频会议等基于IP网络的会话业务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-109202 会话类QOS保证

## 控制的能力

- [WSFD-109202](feature/UNC/20.15.2/WSFD-109202.md)  — 控制项 82207987

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
