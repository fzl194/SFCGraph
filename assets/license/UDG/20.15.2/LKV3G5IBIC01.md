---
id: UDG@20.15.2@License@LKV3G5IBIC01
type: License
name: 智能板订阅和采集
nf: UDG
version: 20.15.2
license_code: LKV3G5IBIC01
control_item_id: '81203781'
license_domain: VAS
control_item_type: function
applicable_nf:
- PCEF
- TDF-U
status: active
---

# 智能板订阅和采集

`LKV3G5IBIC01` · 控制项 81203781 · function · 域 VAS

## 归属/适用NF（原文）

PCEF/TDF-U

## 功能描述

该license作为智能业务分析相关的订阅和数据采集功能总开关，要启用运行于SSU容器上的所有功能时，必须开启本license。

## 实现描述

所有运行于SSU容器上的业务特性都受本license控制。<br>License开启时，则允许SSU容器上智能分析业务运行。<br>License关闭时，不允许SSU容器上智能分析业务运行。

## 取值范围

0 ~ 1

## 默认值

1

## 应用场景

当运营商需要拉起SSU容器进行智能业务分析时，需要开启本功能。

## 相关控制项（原文，未解释为边）

- 智能分析记录生成<br>- 业务全样分析上报<br>- TCP/UDP传输分析上报<br>- 用户实时位置分析上报<br>- 业务实时分析上报<br>- 业务分析上报订阅<br>- 系统级智能分析记录生成

## 对应特性（原文）

GWFD-111283 智能板订阅和采集

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_24455845.md`
