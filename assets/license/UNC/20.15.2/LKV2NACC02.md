---
id: UNC@20.15.2@License@LKV2NACC02
type: License
name: NACC
nf: UNC
version: 20.15.2
license_code: LKV2NACC02
control_item_id: '82206565'
applicable_nf:
- SGSN
- MME
status: active
---

# NACC

`LKV2NACC02` · 控制项 82206565 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

为了快速重选小区，UE需要在执行小区改变前了解目标小区的系统信息。如果目标小区属于不同的eNodeB，系统信息需要在不同的eNodeB之间传递。这种情况下，系统信息被包含在RAN-INFORMATION消息中，通过MME转发给目标的eNodeB。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当用户在进行数据传输过程中发起eNodeB之间的小区重选时，网络辅助小区重选NACC（Network Assisted Cell Change）功能可以大大降低小区重选的时延，提高QoS性能。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104406 NACC

## 控制的能力

- [WSFD-104406](feature/UNC/20.15.2/WSFD-104406.md)  — 控制项 82206565

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
