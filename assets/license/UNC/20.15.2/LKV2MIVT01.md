---
id: UNC@20.15.2@License@LKV2MIVT01
type: License
name: VoLTE一号多卡
nf: UNC
version: 20.15.2
license_code: LKV2MIVT01
control_item_id: '82206610'
applicable_nf:
- MME
status: active
---

# VoLTE一号多卡

`LKV2MIVT01` · 控制项 82206610 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在移动通信系统中，一号多卡功能（Multi-IMSI）支持一个MSISDN号码对应多张USIM（UMTS Subscriber Identify Module）卡，每张卡使用不同的IMSI号码。<br>VoLTE一号多卡功能支持不同卡在LTE网络切换至GSM/UMTS网络进行语音业务时语音呼叫的连续性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

运营商同时部署了一号多卡和VoLTE语音业务时，为保证一号多卡用户LTE到GSM/UMTS网络切换时语音业务的连续性，需要启用。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础语音业务和WSFD-106008 一号多卡功能

## 对应特性（原文）

WSFD-201101 VoLTE一号多卡

## 控制的能力

- [WSFD-201101](feature/UNC/20.15.2/WSFD-201101.md)  — 控制项 82206610

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
