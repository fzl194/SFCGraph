---
id: UNC@20.15.2@License@LKV2FRPH02
type: License
name: 基于HSS/UDM的P-CSCF故障恢复
nf: UNC
version: 20.15.2
license_code: LKV2FRPH02
control_item_id: 82200BNL
applicable_nf:
- MME
status: active
---

# 基于HSS/UDM的P-CSCF故障恢复

`LKV2FRPH02` · 控制项 82200BNL ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

基于HSS的P-CSCF故障恢复是指：S-CSCF检测到Mw接口故障、P-CSCF故障（包括重启、拥塞）时，MME和HSS协同实现VoLTE语音被叫业务快速恢复，减少被叫语音业务中断时长，提升用户体验。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～24000000 SAU

## 默认值

10

## 应用场景

P-CSCF故障场景下，VoLTE被叫业务快速恢复。

## 相关控制项（原文，未解释为边）

VoLTE基础特性

## 对应特性（原文）

WSFD-201205 基于HSS的P-CSCF故障恢复<br>WSFD-221002 基于UDM的VoNR语音故障恢复

## 控制的能力

- [WSFD-201205](feature/UNC/20.15.2/WSFD-201205.md)  — 控制项 82200BNL
- [WSFD-221002](feature/UNC/20.15.2/WSFD-221002.md)  — 控制项 82200BNL

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
