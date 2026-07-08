---
id: UNC@20.15.2@License@LKV2VONRSM01
type: License
name: VoNR基础语音业务-USM
nf: UNC
version: 20.15.2
license_code: LKV2VONRSM01
control_item_id: 82200ELP
applicable_nf:
- SMF
status: active
---

# VoNR基础语音业务-USM

`LKV2VONRSM01` · 控制项 82200ELP ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

VoNR即Voice over NR，UE在NR覆盖下，采用VoNR技术直接在NR上拨打电话，专用QoS Flow也在NR上建立。通话过程中，如果UE移动到LTE网络覆盖下，EPC和5GC会负责把整个IMS DNN平滑到LTE中，并确保给终端分配的IP地址以及P-CSCF的地址不变，使得IMS并不感知。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

用户通过NR接入，进行语音业务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-102701 VoNR基础语音业务

## 控制的能力

- [WSFD-102701](feature/UNC/20.15.2/WSFD-102701.md)  — 控制项 82200ELP

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
