---
id: UNC@20.15.2@License@LKV2DVSS01
type: License
name: 基于SRVCC的数据语音双切换
nf: UNC
version: 20.15.2
license_code: LKV2DVSS01
control_item_id: '82206607'
applicable_nf:
- MME
status: active
---

# 基于SRVCC的数据语音双切换

`LKV2DVSS01` · 控制项 82206607 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

当用户在LTE网络进行语音和数据业务并需要切换至UMTS网络时，为了保证语音与数据业务均不中断，产品提供了基于SRVCC的数据语音双切换解决方案。该方案在进行SRVCC语音切换的同时，也会发起数据业务到UMTS网络的切换。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当用户从LTE网络移出，到UMTS网络时，需要保证用户的语音和数据业务均不中断时，建议启用本特性，提升用户体验。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础语音业务

## 对应特性（原文）

WSFD-201001 基于SRVCC的数据语音双切换

## 控制的能力

- [WSFD-201001](feature/UNC/20.15.2/WSFD-201001.md)  — 控制项 82206607

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
