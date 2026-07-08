---
id: UNC@20.15.2@License@LKV2CHR03
type: License
name: CHR功能-UAM
nf: UNC
version: 20.15.2
license_code: LKV2CHR03
control_item_id: 82200CAD
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# CHR功能-UAM

`LKV2CHR03` · 控制项 82200CAD ·  · 域 

## 归属/适用NF（原文）

SGSN/MME/AMF

## 功能描述

CHR（Call History Record）系统是一种有效、迅速的故障定位系统。它可以记录每个用户在呼叫过程中出现的问题并保存在服务器中。与告警及跟踪系统相比，CHR系统更集中在用户业务流程故障。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

平时运行过程中打开CHR功能，CHR能够记录用户在UAMF内的业务流程信息，并将记录上报到服务器保存，用于后期分析。

## 相关控制项（原文，未解释为边）

无

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848073.md`
