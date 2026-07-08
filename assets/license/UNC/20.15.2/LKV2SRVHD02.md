---
id: UNC@20.15.2@License@LKV2SRVHD02
type: License
name: 切换策略控制
nf: UNC
version: 20.15.2
license_code: LKV2SRVHD02
control_item_id: '82207533'
applicable_nf:
- SGSN
status: active
---

# 切换策略控制

`LKV2SRVHD02` · 控制项 82207533 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

切换策略控制就是根据业务级别、用户级别确定用户在2G和3G网络中的切换策略，来引导2G和3G的网络业务承载和网络负荷。切换策略可以由运营商配置。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

根据业务级别、用户级别确定用户激活后会话的切换策略，引导2G和3G的网络业务承载和网络负荷。

## 相关控制项（原文，未解释为边）

PFC（仅用于Gb模式）

## 对应特性（原文）

WSFD-104507 切换策略控制

## 控制的能力

- [WSFD-104507](feature/UNC/20.15.2/WSFD-104507.md)  — 控制项 82207533

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
