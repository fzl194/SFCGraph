---
id: UNC@20.15.2@License@LKV2ALIASAPN02
type: License
name: 别名APN
nf: UNC
version: 20.15.2
license_code: LKV2ALIASAPN02
control_item_id: '82207546'
applicable_nf:
- SGSN
- MME
status: active
---

# 别名APN

`LKV2ALIASAPN02` · 控制项 82207546 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

别名APN是为了网络业务扩展需要，将一个特定的APN映射为多个不同的别名APN，或为了网络业务合并的需要，将多个特定的APN映射为一个指定的别名APN，使用别名APN替代协商的APN发起DNS解析，以便屏蔽用户APN的差异以及降低用户关于APN的配置要求。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

现网中存在使用相同资源的多个APN的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106203 别名APN

## 控制的能力

- [WSFD-106203](feature/UNC/20.15.2/WSFD-106203.md)  — 控制项 82207546

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
