---
id: UNC@20.15.2@License@LKV2POFT01
type: License
name: 固定终端寻呼优化
nf: UNC
version: 20.15.2
license_code: LKV2POFT01
control_item_id: '82206600'
applicable_nf:
- SGSN
status: active
---

# 固定终端寻呼优化

`LKV2POFT01` · 控制项 82206600 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

固定终端是指固定位置接入的M2M（Machine To Machine）终端（如电子水表）。固定终端寻呼优化特性通过调整READY定时器增加固定终端Ready状态时长，延缓由Ready状态转为Standby状态，从而减少固定终端状态的变迁，减少寻呼开销。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当固定终端频繁的在Ready状态和Standby状态转换，带来大量的寻呼消耗时，配置READY定时器时长参数，<br>UNC<br>将该固定终端的定时器时长调整为配置值。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-206004 固定终端寻呼优化

## 控制的能力

- [WSFD-206004](feature/UNC/20.15.2/WSFD-206004.md)  — 控制项 82206600

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248038.md`
