---
id: UNC@20.15.2@License@LKV2EFBAM01
type: License
name: EPS Fallback-UAM
nf: UNC
version: 20.15.2
license_code: LKV2EFBAM01
control_item_id: '82209907'
applicable_nf:
- AMF
status: active
---

# EPS Fallback-UAM

`LKV2EFBAM01` · 控制项 82209907 ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

在无线网络没有部署VoNR（Voice over NR，NR网络语音业务），当UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行通话时，会回落到4G网络通过VoLTE进行通话。在不部署VoNR的情况下提供5G网络的语音解决方案。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

10000～12000000 SAU

## 默认值

10

## 应用场景

运营商在无线网络不部署VoNR的情况下，并且需要提供语音解决方案时开通本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-102702 EPS Fallback

## 控制的能力

- [WSFD-102702](feature/UNC/20.15.2/WSFD-102702.md)  — 控制项 82209907

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
