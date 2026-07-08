---
id: UNC@20.15.2@License@LKV2MOCN02
type: License
name: 网络共享(MOCN)
nf: UNC
version: 20.15.2
license_code: LKV2MOCN02
control_item_id: '82206615'
applicable_nf:
- SGSN
status: active
---

# 网络共享(MOCN)

`LKV2MOCN02` · 控制项 82206615 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

网络共享（MOCN）指MOCN（Multi-Operator Core Network）方式的网络共享，是指各运营商共享无线接入网，而不共享核心网设备的共享方式，有利于节省运营商的投资成本。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当其他运营商需要租用频谱资源，或者需要节约无线网络建设成本的时候，可以将无线网络进行共享，即启用本特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-104204 Gb-flex或WSFD-104203 Iu-flex

## 对应特性（原文）

WSFD-207001 网络共享（MOCN）

## 控制的能力

- [WSFD-207001](feature/UNC/20.15.2/WSFD-207001.md)  — 控制项 82206615

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248038.md`
