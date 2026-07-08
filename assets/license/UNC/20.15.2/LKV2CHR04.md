---
id: UNC@20.15.2@License@LKV2CHR04
type: License
name: CHR功能-USM
nf: UNC
version: 20.15.2
license_code: LKV2CHR04
control_item_id: 82200CAE
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# CHR功能-USM

`LKV2CHR04` · 控制项 82200CAE ·  · 域 

## 归属/适用NF（原文）

GGSN-C/SGW-C/PGW-C/SMF

## 功能描述

CHR（Call History Record）系统是一种有效、迅速的故障定位系统。它可以记录每个用户在呼叫过程中出现的问题并保存在服务器中。网管部门在需要的时候，可以查询特定用户的呼叫历史记录，迅速定位故障原因。与告警及跟踪系统相比，CHR系统更集中在用户业务流程故障。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

平时运行过程中打开CHR功能，CHR能够记录信令流程故障问题的现场信息，能方便用户对业务故障问题进行分析处理。

## 相关控制项（原文，未解释为边）

无

## 控制的能力

- [WSFD-202001](feature/UNC/20.15.2/WSFD-202001.md)  — 控制项 82200CAE

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
