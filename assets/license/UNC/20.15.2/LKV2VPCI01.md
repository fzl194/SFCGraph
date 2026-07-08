---
id: UNC@20.15.2@License@LKV2VPCI01
type: License
name: 基于IMEI的语音策略控制
nf: UNC
version: 20.15.2
license_code: LKV2VPCI01
control_item_id: '82207524'
applicable_nf:
- MME
status: active
---

# 基于IMEI的语音策略控制

`LKV2VPCI01` · 控制项 82207524 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

UNC<br>根据终端IMEI（International Mobile Equipment Identity）信息控制是否向某类终端用户提供VoLTE基础语音业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

运营商希望根据终端类型向用户提供VoLTE基础语音业务的场景下，建议开启本特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-201002 用户群语音策略控制

## 对应特性（原文）

WSFD-201004 基于IMEI的语音策略控制

## 控制的能力

- [WSFD-201004](feature/UNC/20.15.2/WSFD-201004.md)  — 控制项 82207524

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
