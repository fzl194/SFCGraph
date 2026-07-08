---
id: UNC@20.15.2@License@LKV2SUPCHG02
type: License
name: SuperCharger功能
nf: UNC
version: 20.15.2
license_code: LKV2SUPCHG02
control_item_id: '82206549'
applicable_nf:
- SGSN
status: active
---

# SuperCharger功能

`LKV2SUPCHG02` · 控制项 82206549 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

SuperCharger功能是一种用户漫游出SGSN或长时间分离后，SGSN仍然保留该用户的签约数据而不删除的一种机制。Super-Charger特性可以减少SGSN与HLR之间的信令交互。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

SuperCharger功能基于位置更新流程实现，用于减少移动性管理过程中网元间的信令流量，主要适用于：<br>- 大城市SGSN密度较高。<br>- 每个SGSN需要管理大量用户。<br>- 用户经常在各SGSN之间移动。如：SGSN A服务于用户住所区，SGSN B服务于用户办公区，用户早上从住所移动到办公地点，晚上从办公地点移动到住所。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106304 SuperCharger功能

## 控制的能力

- [WSFD-106304](feature/UNC/20.15.2/WSFD-106304.md)  — 控制项 82206549

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
