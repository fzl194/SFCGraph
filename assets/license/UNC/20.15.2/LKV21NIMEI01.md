---
id: UNC@20.15.2@License@LKV21NIMEI01
type: License
name: 1/N设备标识检查
nf: UNC
version: 20.15.2
license_code: LKV21NIMEI01
control_item_id: '82206552'
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# 1/N设备标识检查

`LKV21NIMEI01` · 控制项 82206552 ·  · 域 

## 归属/适用NF（原文）

SGSN、MME、AMF

## 功能描述

1/N设备标识检查是指在进行设备标识检查时，如果用户设备标识未发生改变，UNC每N次Attach/注册流程进行一次设备标识检查。该特性在确保用户终端合法性的同时，减少设备标识检查的次数，以降低EIR（Equipment Identity Register）负载。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在网络中开通了<br>“WSFD-103004 设备标识检查”<br>特性，且EIR负载较高的场景，如果运营商需要在确保用户终端合法性的同时降低EIR负载，则建议开通该特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-103004设备标识检查

## 对应特性（原文）

WSFD-103006 1/N设备标识检查

## 控制的能力

- [WSFD-103006](feature/UNC/20.15.2/WSFD-103006.md)  — 控制项 82206552
- [WSFD-103006-1](feature/UNC/20.15.2/WSFD-103006-1.md)  — 控制项 82206552
- [WSFD-103006-2](feature/UNC/20.15.2/WSFD-103006-2.md)  — 控制项 82206552

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
