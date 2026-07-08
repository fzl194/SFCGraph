---
id: UNC@20.15.2@License@LKV2IMSIQOS02
type: License
name: 基于IMSI号段的QoS控制
nf: UNC
version: 20.15.2
license_code: LKV2IMSIQOS02
control_item_id: '82206580'
applicable_nf:
- SGSN
- MME
status: active
---

# 基于IMSI号段的QoS控制

`LKV2IMSIQOS02` · 控制项 82206580 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

能够基于IMSI号段控制用户QoS。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

- 运营商签署了漫游协议但是没有签署业务层协议。<br>- 运营商签署了漫游协议和业务层协议，并需要对这些运营商进行控制。<br>- 运营商共用同一个网络。此时，本特性可以用于区分不同运营商提供的业务。<br>- 移动虚拟运营商与网络运营商签署了协议。此时，本特性可以用于区分两者的业务。<br>- WCDMA/GSM/EDGE运营商签署了GPRS（不包括EDGE）的协议。此时，运营商可以选择为没有WCDMA覆盖，或WCDMA覆盖不足，或只为满足自身用户需求的区域提供高速率业务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-105104 基于IMSI号段的Qos控制

## 控制的能力

- [WSFD-105104](feature/UNC/20.15.2/WSFD-105104.md)  — 控制项 82206580

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
