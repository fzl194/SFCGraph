---
id: UNC@20.15.2@License@LKV3WPCSCF11
type: License
name: 基于PCRF的P-CSCF故障恢复
nf: UNC
version: 20.15.2
license_code: LKV3WPCSCF11
control_item_id: '82208383'
applicable_nf:
- PGW-C
status: active
---

# 基于PCRF的P-CSCF故障恢复

`LKV3WPCSCF11` · 控制项 82208383 ·  · 域 

## 归属/适用NF（原文）

PGW-C

## 功能描述

UNC基于PCRF的VoLTE业务快速恢复处理指当PGW-C收到PCRF发送的携带PCSCF-Restoration-Indication信元的Re-Authentication Request（RAR）消息时，重新选择一对正常的P-CSCF地址推送给UE，UE从中选择一个新的P-CSCF地址，重新发起IMS业务，从而保证IMS业务自动恢复。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

P-CSCF故障或者重启后会导致丢失用户信息。对于用户主叫场景，兼容性比较好的终端可以自行重新注册完成主叫业务恢复。对于用户被叫场景，当用户不进行主叫且IMS注册定时器没有超时时，用户的被叫是一直失败的，用户体验较差。通过引入基于PCRF/PCF的VoLTE业务快速恢复特性解决上述问题。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-102203 基于PCRF/PCF的VoLTE业务快速恢复

## 控制的能力

- [WSFD-102203](feature/UNC/20.15.2/WSFD-102203.md)  — 控制项 82208383

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
