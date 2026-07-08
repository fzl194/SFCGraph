---
id: UNC@20.15.2@License@LKV2CSFB05
type: License
name: 基于CSFB的优先语音服务
nf: UNC
version: 20.15.2
license_code: LKV2CSFB05
control_item_id: '82205926'
applicable_nf:
- MME
status: active
---

# 基于CSFB的优先语音服务

`LKV2CSFB05` · 控制项 82205926 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

当GSM/UMTS网络支持eMLPP服务时，MME支持将LTE用户发起的eMLPP业务回落到CS网络中，并且提供高优先级的接入、回落和寻呼功能。<br>eMLPP：增强的多优先级和抢占业务（enhanced Multi Level Precedence and Preemption service），其作用是将呼叫分为几种不同的优先级，较高优先级的呼叫将可能获得更多的能力，例如，抢占信道、快速呼叫等。eMLPP为运营商提供了在运营策略上对用户群进行细分的功能，可满足运营商为不同层次的用户群提供不同等级服务的要求。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在LTE-EPC网络建设初期，原GSM/UMTS网络的eMLPP业务尚未部署在LTE-EPC网络中，通过启用基于CSFB的优先语音服务特性，保证用户体验不变。

## 相关控制项（原文，未解释为边）

依赖WSFD-102301 基于CSFB的语音业务

## 对应特性（原文）

WSFD-102502 基于CSFB的优先语音服务

## 控制的能力

- [WSFD-102502](feature/UNC/20.15.2/WSFD-102502.md)  — 控制项 82205926

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
