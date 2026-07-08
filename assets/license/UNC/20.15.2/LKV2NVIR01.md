---
id: UNC@20.15.2@License@LKV2NVIR01
type: License
name: 网络语音业务信息上报功能
nf: UNC
version: 20.15.2
license_code: LKV2NVIR01
control_item_id: '82206609'
applicable_nf:
- MME
status: active
---

# 网络语音业务信息上报功能

`LKV2NVIR01` · 控制项 82206609 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

网络语音业务信息上报功能可以提供LTE网络中所有用户语音业务的CHR（Call History Record），CHR中包含语音业务流程的相关信息（例如，流程发生的时间、流程时长、位置、失败原因值等）。运营商可以通过这些信息快速定位故障原因，或对业务质量进行分析以提升服务质量。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在网络中部署了LTE语音业务的场景下，建议开通该特性，以提升语音业务故障定位效率和网络服务质量。

## 相关控制项（原文，未解释为边）

依赖WSFD-110708 VoLTE基础语音业务或WSFD-110702 基于CSFB的语音业务

## 对应特性（原文）

WSFD-201003 网络语音业务信息上报功能

## 控制的能力

- [WSFD-201003](feature/UNC/20.15.2/WSFD-201003.md)  — 控制项 82206609

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
