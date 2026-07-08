---
id: UNC@20.15.2@License@LKV2NVEC01
type: License
name: VoLTE紧急呼叫的定位(NI-LR)
nf: UNC
version: 20.15.2
license_code: LKV2NVEC01
control_item_id: '82207701'
applicable_nf:
- MME
status: active
---

# VoLTE紧急呼叫的定位(NI-LR)

`LKV2NVEC01` · 控制项 82207701 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在用户发起VoLTE紧急呼叫过程中，为用户提供服务的PLMN内部发起NI-LR（Network Induced Location Request）流程，主动上报用户位置信息到紧急呼叫中心，从而快速定位移动用户位置，及时实施救援等活动。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当用户拨打紧急呼叫号码时，可能因为情况情急或者环境恶劣，无法准确提供有效的位置信息，影响救援速度和成功率。部署该功能后，呼叫中心能够快速获取紧急呼叫用户有效的位置信息，并实施救援活动，保障用户的生命和财产安全。在网络中部署了VoLTE紧急呼叫功能时，建议开启本特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-102101 VoLTE紧急呼叫和WSFD-106401 位置定位服务(LCS)

## 对应特性（原文）

WSFD-102102 VoLTE紧急呼叫的定位(NI-LR)

## 控制的能力

- [WSFD-102102](feature/UNC/20.15.2/WSFD-102102.md)  — 控制项 82207701

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
