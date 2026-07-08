---
id: UNC@20.15.2@License@LKV2SELGW03
type: License
name: S-GW/P-GW 拓扑选择
nf: UNC
version: 20.15.2
license_code: LKV2SELGW03
control_item_id: '82205919'
applicable_nf:
- SGSN
- MME
status: active
---

# S-GW/P-GW 拓扑选择

`LKV2SELGW03` · 控制项 82205919 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

UNC<br>可以智能的选择一个综合性的S-GW/P-GW，也可以从物理拓扑结构上选择最近的S-GW或者P-GW。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

激活PDP上下文场景中使用。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205004 S-GW/P-GW拓扑选择

## 控制的能力

- [WSFD-205004](feature/UNC/20.15.2/WSFD-205004.md)  — 控制项 82205919

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
