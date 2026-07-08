---
id: UNC@20.15.2@License@LKV3WFRFNV01
type: License
name: VoLTE承载故障快速恢复-USM
nf: UNC
version: 20.15.2
license_code: LKV3WFRFNV01
control_item_id: '82208815'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# VoLTE承载故障快速恢复-USM

`LKV3WFRFNV01` · 控制项 82208815 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

随着LTE网络的普及，语音业务会逐步从CS域切换到PS+IMS域。一旦PS网元故障，将会导致用户的语音业务中断，如果运维人员未及时处理故障，UE有可能长时间中断被叫语音业务，影响用户的业务体验。解决故障的关键在于尽快让UE重新附着PS网络。<br>- 在普通场景下，该特性让UE快速附着PS网络，降低MME/SGW-C/PGW-C故障对语音业务的影响。<br>- 在部署了VoLTE语音业务的网络中，MME Pool的组网场景下，用户正在VoLTE语音业务，如果MME故障，Pool内其它MME可以快速接替故障MME上的用户的业务，实现VoLTE承载的快速恢复，确保通话继续。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

- 本特性应用于部署了VoLTE语音业务的MME Pool网络，对VoLTE语音通话可靠性要求高时，比如执警、救援等呼叫业务中不会因为网络故障和操作维护中断，建议开启本特性。<br>- 一般故障/重启场景，建议开启本特性。

## 相关控制项（原文，未解释为边）

WSFD-201201 MME链式备份<br>WSFD-201103 IMS功能<br>WSFD-109101 PCC基本功能

## 对应特性（原文）

WSFD-201204 VoLTE承载故障快速恢复

## 控制的能力

- [WSFD-201204](feature/UNC/20.15.2/WSFD-201204.md)  — 控制项 82208815

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
