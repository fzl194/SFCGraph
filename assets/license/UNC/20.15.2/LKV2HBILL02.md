---
id: UNC@20.15.2@License@LKV2HBILL02
type: License
name: 支持热计费功能
nf: UNC
version: 20.15.2
license_code: LKV2HBILL02
control_item_id: '82206574'
applicable_nf:
- SGSN
status: active
---

# 支持热计费功能

`LKV2HBILL02` · 控制项 82206574 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

SGSN可以根据自身的配置或HLR中签约的计费属性确定用户是否采用热计费，若采用热计费，在话单中打上热计费标志，传给CG。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

SGSN采用热计费。

## 相关控制项（原文，未解释为边）

依赖WSFD-011201 支持离线计费

## 对应特性（原文）

WSFD-011202 支持热计费功能

## 控制的能力

- [WSFD-011202](feature/UNC/20.15.2/WSFD-011202.md)  — 控制项 82206574

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
