---
id: UNC@20.15.2@License@LKV2BADCF01
type: License
name: ADC基本功能
nf: UNC
version: 20.15.2
license_code: LKV2BADCF01
control_item_id: 82200BNK
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# ADC基本功能

`LKV2BADCF01` · 控制项 82200BNK ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

为运营商对业务精细化控制的要求，引入ADC（Application Detection and Control）功能，检测应用并向PCRF/PCF上报应用标识、流信息以及应用的起始或者结束事件。PCRF/PCF根据上报的信息下发PCC策略，UNC基于PCC策略进行业务控制、计费和承载管理。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 PDP

## 默认值

10000

## 应用场景

UNC网元中使用ADC基本功能的动态PCC用户接入。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-109102 ADC基本功能

## 控制的能力

- [WSFD-109102](feature/UNC/20.15.2/WSFD-109102.md)  — 控制项 82200BNK

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
