---
id: UNC@20.15.2@License@LKV2LVLR01
type: License
name: 本地VLR
nf: UNC
version: 20.15.2
license_code: LKV2LVLR01
control_item_id: '82207527'
applicable_nf:
- MME
status: active
---

# 本地VLR

`LKV2LVLR01` · 控制项 82207527 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本地VLR是指MME备份用户的签约数据，用户恢复业务过程中取用本地信息，减少MME和HSS之间的流量，降低业务恢复对HSS造成的信令风暴冲击。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～6500000 SAU

## 默认值

10

## 应用场景

当运营商部署MME链式备份特性的场景下，建议启用本特性，降低业务恢复对HSS造成的信令风暴冲击，确保网络的安全运行。

## 相关控制项（原文，未解释为边）

依赖WSFD-201201 MME链式备份

## 对应特性（原文）

WSFD-201202 本地VLR

## 控制的能力

- [WSFD-201202](feature/UNC/20.15.2/WSFD-201202.md)  — 控制项 82207527

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
