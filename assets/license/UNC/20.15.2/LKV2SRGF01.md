---
id: UNC@20.15.2@License@LKV2SRGF01
type: License
name: S-GW/P-GW故障下的业务恢复
nf: UNC
version: 20.15.2
license_code: LKV2SRGF01
control_item_id: '82207528'
applicable_nf:
- MME
status: active
---

# S-GW/P-GW故障下的业务恢复

`LKV2SRGF01` · 控制项 82207528 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在S-GW/P-GW故障或重启场景下，MME能感知网关故障，协助用户及时恢复VoLTE语音业务，实现网关设备的容灾功能。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

运营商部署<br>[WSFD-102001 VoLTE基础语音业务](../../../../UNC特性指南/语音功能/WSFD-102001 VoLTE基础语音业务_67023607.md)<br>或<br>[WSFD-102101 VoLTE紧急呼叫](../../../../UNC特性指南/语音功能/WSFD-102101 VoLTE紧急呼叫_70014690.md)<br>后，S-GW/P-GW故障或重启会使用户VoLTE业务受阻，影响用户体验。启用本特性后，可为用户快速恢复VoLTE业务，提升用户体验。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-201203 S-GW/P-GW故障下的业务恢复

## 控制的能力

- [WSFD-201203](feature/UNC/20.15.2/WSFD-201203.md)  — 控制项 82207528

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
