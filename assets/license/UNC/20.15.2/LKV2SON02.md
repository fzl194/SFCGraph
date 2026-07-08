---
id: UNC@20.15.2@License@LKV2SON02
type: License
name: eNodeB SON信息传送功能
nf: UNC
version: 20.15.2
license_code: LKV2SON02
control_item_id: '82206558'
applicable_nf:
- MME
status: active
---

# eNodeB SON信息传送功能

`LKV2SON02` · 控制项 82206558 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

SON（Self Organization Network）信息传送功能即通过S1AP协议自动获得相邻eNodeB的X2接口地址用于建立X2连接。eNodeB之间X2切换及eNodeB状态信息通告机制都需要通过X2连接才能传递。<br>SON信息传送功能可以实现网络拓扑配置不再全部依赖于OM的配置，而是由协议流程自动获得配置相关数据。通过eNodeB CONFIGURATION TRANSFER和MME CONFIGURATION TRANSFER消息传递eNodeB的X2接口地址信息，用于eNodeB之间建立X2连接，以简化网络维护，降低配置出错概率。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在全部eNodeB都支持通过SON流程自动发现相邻eNodeB的X2地址的组网中，可启用此功能，以简化网络维护。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104402 eNodeB SON信息传送功能

## 控制的能力

- [WSFD-104402](feature/UNC/20.15.2/WSFD-104402.md)  — 控制项 82206558

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
