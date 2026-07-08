---
id: UNC@20.15.2@License@LKV2SPAS02
type: License
name: Smartphone异常信令节省
nf: UNC
version: 20.15.2
license_code: LKV2SPAS02
control_item_id: '82207537'
applicable_nf:
- SGSN
status: active
---

# Smartphone异常信令节省

`LKV2SPAS02` · 控制项 82207537 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

异常信令节省是指当由于未签约APN、网络故障等原因导致UE激活失败时，UE反复进行激活，从而产生大量异常信令时。<br>UNC<br>可以根据事先配置的抑制策略对UE进行抑制此现象发生，消除由于UE的异常重复激活行为对网络侧的影响。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

GERAN和UTRAN网络中，在Smartphone终端反复激活，产生大量异常信令的情况下，利用异常信令控制功能可以减少网络的信令负荷。

## 相关控制项（原文，未解释为边）

依赖 WSFD-206005 Smartphone控制基础功能

## 对应特性（原文）

WSFD-206006 Smartphone异常信令节省

## 控制的能力

- [WSFD-206006](feature/UNC/20.15.2/WSFD-206006.md)  — 控制项 82207537

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248038.md`
