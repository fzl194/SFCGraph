---
id: UNC@20.15.2@License@LKV2EFEC01
type: License
name: EPS Fallback紧急呼叫
nf: UNC
version: 20.15.2
license_code: LKV2EFEC01
control_item_id: 82200BNC
applicable_nf:
- AMF
status: active
---

# EPS Fallback紧急呼叫

`LKV2EFEC01` · 控制项 82200BNC ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

本特性是指在无线网络没有部署VoNR（Voice over NR，NR网络语音业务），当UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行紧急呼叫时，会回落到4G网络通过VoLTE进行通话。在不部署VoNR的情况下提供5G网络的语音解决方案。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

10000～12000000 SAU

## 默认值

10

## 应用场景

运营商在无线网络不部署VoNR的情况下，并且需要提供紧急呼叫服务时开通本特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-102702 EPS Fallback

## 对应特性（原文）

WSFD-102703 EPS Fallback紧急呼叫

## 控制的能力

- [WSFD-102703](feature/UNC/20.15.2/WSFD-102703.md)  — 控制项 82200BNC

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
