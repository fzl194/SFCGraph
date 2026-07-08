---
id: UNC@20.15.2@License@LKV2UDMBPMM01
type: License
name: UDM全故障业务逃生-UAM
nf: UNC
version: 20.15.2
license_code: LKV2UDMBPMM01
control_item_id: 82200EEX
applicable_nf:
- AMF
status: active
---

# UDM全故障业务逃生-UAM

`LKV2UDMBPMM01` · 控制项 82200EEX ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

在系统中控制进入UDM故障 Bypass状态的5G动态用户数。

## 实现描述

AMF系统中每有一个5G SA用户进入UDM故障 Bypass状态，该License总数加1；每有一个5G SA用户退出UDM故障 Bypass状态，总数减1。

## 取值范围

0～12000000 SAU

## 默认值

0

## 应用场景

UDM用于存储用户数据，与AMF交互实现鉴权、获取用户签约数据、进行位置更新注册网元信息等功能。在与AMF对接的所有UDM同时故障的极端场景，将导致大范围业务中断。为了最大程度地保障业务可用性，可以开启本特性减小故障影响范围。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-206101 UDM全故障业务保活

## 控制的能力

- [WSFD-206101](feature/UNC/20.15.2/WSFD-206101.md)  — 控制项 82200EEX

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848073.md`
