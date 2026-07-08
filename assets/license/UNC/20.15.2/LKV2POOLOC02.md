---
id: UNC@20.15.2@License@LKV2POOLOC02
type: License
name: MME 过载控制
nf: UNC
version: 20.15.2
license_code: LKV2POOLOC02
control_item_id: '82206556'
applicable_nf:
- MME
status: active
---

# MME 过载控制

`LKV2POOLOC02` · 控制项 82206556 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

UNC<br>设备作为MME逻辑网元运行时，当<br>UNC<br>过载时向eNodeB发送Overload Start消息，通知eNodeB拒绝UE新建连接，从而减少网络侧信令冲击。当<br>UNC<br>从过载状态恢复到正常状态后向eNodeB发送Overload Stop消息，通知eNodeB允许UE接入，继续为UE提供服务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在非MME POOL组网场景下，可以启用过载控制功能避免过载后整系统故障。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104102 MME过载控制

## 控制的能力

- [WSFD-104102](feature/UNC/20.15.2/WSFD-104102.md)  — 控制项 82206556

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
