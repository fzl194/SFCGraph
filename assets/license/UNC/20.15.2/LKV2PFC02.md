---
id: UNC@20.15.2@License@LKV2PFC02
type: License
name: PFC(仅用于Gb模式)
nf: UNC
version: 20.15.2
license_code: LKV2PFC02
control_item_id: '82206577'
applicable_nf:
- SGSN
status: active
---

# PFC(仅用于Gb模式)

`LKV2PFC02` · 控制项 82206577 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

PFC（Packet Flow Context）是指通过为同一用户的多个<br>QoS<br>相近的<br>PDP<br>分配相同的PFI（Packet Flow Identifier），实现数据流的捆绑传送。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~12000000 SAU

## 默认值

10

## 应用场景

当<br>无线资源<br>不足，不能保证高优先级用户的无线传输带宽时，建议开启PFC功能，实现数据流的捆绑传送，来提高用户业务体验。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-105101 PFC（仅用于Gb 模式）

## 控制的能力

- [WSFD-105101](feature/UNC/20.15.2/WSFD-105101.md)  — 控制项 82206577

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
