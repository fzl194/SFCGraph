---
id: UNC@20.15.2@License@LKV3WPVVLE11
type: License
name: 基于VoLTE的优先语音服务-USM
nf: UNC
version: 20.15.2
license_code: LKV3WPVVLE11
control_item_id: '82208359'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# 基于VoLTE的优先语音服务-USM

`LKV3WPVVLE11` · 控制项 82208359 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

基于VoLTE的优先语音服务是允许特定签约者或者其他被授权者优先获取网络资源，尤其是在网络拥塞或者紧急状况下时，及时完成救助、调度管理等工作。特定签约者可以是政府授权的个人、紧急事务处理官员或者其它授权者。在标准中称这类有优先接入权限的人为服务用户(Service User)，多媒体优先业务支持端到端的优先处理机制。<br>基于VoLTE的优先语音服务业务包括EPC-MPS和IMS-MPS两种业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

基于VoLTE的优先语音服务特性从触发方式分有两种：Always-on MPS业务和On-Demand MPS业务。从业务方式分有两种：MPS-EPS业务和MPS-IMS业务。两种分类方法交叉一共有四种应用场景。<br>- Always-On MPS-EPS用户在EPS-HSS中签约了基于VoLTE的优先语音服务业务，在用户接入、以及承载资源处理都给予高优先级处理。<br>- On-Demand MPS-EPS用户没有在EPS-HSS中签约基于VoLTE的优先语音服务业务，用户在激活过程中，由网络侧根据策略临时给予高优先级的PS网络资源使用权限。<br>- Always-On MPS-IMS用户在EPS-HSS和IMS-HSS中签约了基于VoLTE的优先语音服务业务，在用户接入、以及IMS信令或者数据承载资源创建时都给予高优先级处理。<br>- On-Demand MPS-IMS用户没有在EPS-HSS中签约基于VoLTE的优先语音服务业务，用户在激活过程中，由网络侧根据策略临时给予高优先级的IMS网络资源使用权限。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础语音业务

## 对应特性（原文）

WSFD-102004 基于VoLTE的优先语音服务

## 控制的能力

- [WSFD-102004](feature/UNC/20.15.2/WSFD-102004.md)  — 控制项 82208359

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
