---
id: UNC@20.15.2@License@LKV2GEA302
type: License
name: 支持GPRS加密功能:GEA-3(仅用于Gb模式)
nf: UNC
version: 20.15.2
license_code: LKV2GEA302
control_item_id: '82206548'
applicable_nf:
- SGSN
status: active
---

# 支持GPRS加密功能:GEA-3(仅用于Gb模式)

`LKV2GEA302` · 控制项 82206548 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

GEA（GPRS Encryption Algorithm）是对LLC（Logic Link Control）层传递的用户数据进行加密的一种算法，加密范围从SGSN到MS，用来保证数据传输的安全性。加密处理的数据部分主要包括LLC帧所携带的信息域和校验域。GEA分为三种类型：GEA-1、GEA-2和GEA-3。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~12000000 SAU

## 默认值

10

## 应用场景

应用于2G网络。

## 相关控制项（原文，未解释为边）

依赖<br>2G&3G网络用户身份保密性功能

## 对应特性（原文）

WSFD-103003 支持GPRS 加密功能：GEA-3（仅用于Gb 模式）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
