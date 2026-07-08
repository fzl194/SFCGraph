---
id: UNC@20.15.2@License@LKV2GSINTF02
type: License
name: 支持Gs接口
nf: UNC
version: 20.15.2
license_code: LKV2GSINTF02
control_item_id: '82206566'
applicable_nf:
- SGSN
status: active
---

# 支持Gs接口

`LKV2GSINTF02` · 控制项 82206566 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

Gs接口是MSC/VLR和SGSN之间的接口，可在MSC/VLR和SGSN的数据库之间建立起关联。通过Gs接口，可以在SGSN和MSC/VLR之间协调每个同时附着到GPRS和非GPRS业务的UE的位置信息，同时也可用于通过SGSN来完成一些CS相关的流程。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

本特性应用于可同时支持GPRS和非GPRS业务的网络并且用户设置允许使用这两种业务的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104407 支持Gs接口

## 控制的能力

- [WSFD-104407](feature/UNC/20.15.2/WSFD-104407.md)  — 控制项 82206566

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
