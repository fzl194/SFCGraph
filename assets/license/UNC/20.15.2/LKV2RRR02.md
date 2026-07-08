---
id: UNC@20.15.2@License@LKV2RRR02
type: License
name: 区域漫游限制
nf: UNC
version: 20.15.2
license_code: LKV2RRR02
control_item_id: '82206572'
applicable_nf:
- SGSN
- MME
status: active
---

# 区域漫游限制

`LKV2RRR02` · 控制项 82206572 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

区域漫游限制是指<br>UNC<br>根据用户当前所在的位置、签约ZC信息及本地配置策略，控制是否允许用户进行漫游。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

若运营商希望控制某类用户是否允许接入E-UTRAN，则可以启用根据签约ZC进行漫游控制的特性。<br>若运营商希望控制某类用户是否允许接入E-UTRAN，但HLR/HSS不支持ZC时，则可以启用根据本地配置策略进行漫游控制的特性。

## 相关控制项（原文，未解释为边）

区域漫游限制

## 对应特性（原文）

WSFD-105003 区域漫游限制

## 控制的能力

- [WSFD-105003](feature/UNC/20.15.2/WSFD-105003.md)  — 控制项 82206572

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
