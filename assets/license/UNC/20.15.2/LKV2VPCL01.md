---
id: UNC@20.15.2@License@LKV2VPCL01
type: License
name: 基于区域的语音策略控制
nf: UNC
version: 20.15.2
license_code: LKV2VPCL01
control_item_id: '82207032'
applicable_nf:
- MME
status: active
---

# 基于区域的语音策略控制

`LKV2VPCL01` · 控制项 82207032 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

UNC<br>根据用户所在的位置区域的E-UTRAN是否支持VoLTE语音业务，控制是否允许用户使用VoLTE基础语音业务和紧急呼叫业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

启用了<br>“VoLTE基础语音业务”<br>，且<br>UNC<br>覆盖的位置区域中，只有部分E-UTRAN支持VoLTE语音业务时，建议同时启用本特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础语音业务

## 对应特性（原文）

WSFD-201005 基于区域的语音策略控制

## 控制的能力

- [WSFD-201005](feature/UNC/20.15.2/WSFD-201005.md)  — 控制项 82207032

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
