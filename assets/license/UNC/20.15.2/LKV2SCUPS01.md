---
id: UNC@20.15.2@License@LKV2SCUPS01
type: License
name: 支持CUPS架构
nf: UNC
version: 20.15.2
license_code: LKV2SCUPS01
control_item_id: 82200BER
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# 支持CUPS架构

`LKV2SCUPS01` · 控制项 82200BER ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C、SMF

## 功能描述

CUPS（Control and User Plane Separation）架构即控制面与用户面分离架构，通过提供GGSN-C/SGW-C/PGW-C/SMF和GGSN-U/SGW-U/PGW-U/UPF两种独立的NF形态实现控制面和用户面功能的分离，满足云化场景下控制面和用户面资源的不同要求。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

在以下场景可以使用该特性：<br>- 物联网；<br>- CDN业务；<br>- VoLTE业务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-107001 支持CUPS架构

## 控制的能力

- [WSFD-107001](feature/UNC/20.15.2/WSFD-107001.md)  — 控制项 82200BER

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
