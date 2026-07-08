---
id: UNC@20.15.2@License@LKV2MIMSI02
type: License
name: 一号多卡功能
nf: UNC
version: 20.15.2
license_code: LKV2MIMSI02
control_item_id: '82206570'
applicable_nf:
- SGSN
- MME
status: active
---

# 一号多卡功能

`LKV2MIMSI02` · 控制项 82206570 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

在移动通信系统中，一号多卡功能（Multi-IMSI）支持一个MSISDN号码对应多张SIM卡或USIM卡，每张卡使用不同的IMSI号码。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

一号多卡功能（Multi-IMSI）支持一个MSISDN号码对应多张SIM卡或USIM卡。<br>- 在MSISDN号码不变的条件下，允许不同的SIM卡或USIM卡同时使用不同的业务，互相之间不会影响和冲突。<br>- 每张SIM卡或USIM卡单独计费，互不影响。<br>- 用户的联系人只用记录一个号码。具体那一张SIM卡或USIM卡处于激活状态，可以由用户决定。<br>华为<br>UNC<br>能够为每个MSISDN号码最多支持10个IMSI号码。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106008 一号多卡功能

## 控制的能力

- [WSFD-106008](feature/UNC/20.15.2/WSFD-106008.md)  — 控制项 82206570

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
