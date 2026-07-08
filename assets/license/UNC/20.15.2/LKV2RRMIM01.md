---
id: UNC@20.15.2@License@LKV2RRMIM01
type: License
name: IM类业务资源管控
nf: UNC
version: 20.15.2
license_code: LKV2RRMIM01
control_item_id: '82207544'
applicable_nf:
- SGSN
status: active
---

# IM类业务资源管控

`LKV2RRMIM01` · 控制项 82207544 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

IM<br>（Instant Messaging）类业务<br>无线资源<br>管控是指在无线资源有限的情况下，网络侧识别出IM类业务（例如QQ），并通过GTP-U（GPRS Tunneling Protocol-User plane）和<br>BSSGP<br>（Base Station Subsystem GPRS Protocol）协议头的扩展字段将业务参数传递给无线侧，进而使无线侧对IM类业务进行管理，实现无线资源优化的功能。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

本功能应用于2G网络无线资源有限的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106305 IM类业务资源管控

## 控制的能力

- [WSFD-106305](feature/UNC/20.15.2/WSFD-106305.md)  — 控制项 82207544

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
