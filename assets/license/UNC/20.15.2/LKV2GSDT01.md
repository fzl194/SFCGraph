---
id: UNC@20.15.2@License@LKV2GSDT01
type: License
name: NB-IoT基于SGs接口的短消息
nf: UNC
version: 20.15.2
license_code: LKV2GSDT01
control_item_id: '82208411'
applicable_nf:
- MME
status: active
---

# NB-IoT基于SGs接口的短消息

`LKV2GSDT01` · 控制项 82208411 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本特性支持NB-IoT终端发起EPS网络的短消息传输。NB-IoT终端可以不用发起联合的EPS/IMSI附着，只需附着到EPS网络通过MME与MSC的交互实现短消息数据传输业务，丰富了NB-IoT的数传方式。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当某些NB-IoT终端仅发起EPS附着，并且附着消息中Additional update type信元中携带“SMS only”时，部署本特性，实现短消息数据传输业务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215104 NB-IoT基于SGs接口的短消息

## 控制的能力

- [WSFD-215104](feature/UNC/20.15.2/WSFD-215104.md)  — 控制项 82208411

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
