---
id: UNC@20.15.2@License@LKV2CELP01
type: License
name: 基于eNodeB覆盖等级的寻呼
nf: UNC
version: 20.15.2
license_code: LKV2CELP01
control_item_id: '82207028'
applicable_nf:
- MME
status: active
---

# 基于eNodeB覆盖等级的寻呼

`LKV2CELP01` · 控制项 82207028 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

基于eNodeB覆盖等级的寻呼，指MME根据eNodeB上报的推荐寻呼的eNodeB进行寻呼优化，并在寻呼消息中将eNodeB上报的推荐寻呼的小区和小区覆盖等级通过寻呼辅助信息传给eNodeB，用以基于eNodeB覆盖等级的寻呼。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当有不同覆盖等级的小区接入系统时，开启本特性的MME与eNodeB配合可以有效寻呼不同覆盖等级小区下的用户，提高系统容量和寻呼效率。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215202 基于eNodeB覆盖等级的寻呼

## 控制的能力

- [WSFD-215202](feature/UNC/20.15.2/WSFD-215202.md)  — 控制项 82207028

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
