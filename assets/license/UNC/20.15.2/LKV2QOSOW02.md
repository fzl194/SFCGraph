---
id: UNC@20.15.2@License@LKV2QOSOW02
type: License
name: QoS覆盖
nf: UNC
version: 20.15.2
license_code: LKV2QOSOW02
control_item_id: '82206545'
applicable_nf:
- SGSN
status: active
---

# QoS覆盖

`LKV2QOSOW02` · 控制项 82206545 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

QoS覆盖是将指定用户签约的QoS速率改写成特定值，在HLR向SGSN插入签约数据时，SGSN根据定义的QoS转换规则把Rel5或者Rel99版本的QoS数据转换为Rel7版本的QoS。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~12000000

## 默认值

10

## 应用场景

SGSN、GGSN、RNC、UE等网元支持Rel7格式的QoS，但是HLR只支持Rel5或者更早版本的QoS，通过QoS转换特性可以在不升级HLR的情况下使用HSPA+功能。

## 相关控制项（原文，未解释为边）

影响WSFD-101303 HSDPA扩展包3，16M-32M或WSFD-101308 HSUPA扩展包2，8M-12M

## 对应特性（原文）

WSFD-105001 QoS覆盖

## 控制的能力

- [WSFD-105001](feature/UNC/20.15.2/WSFD-105001.md)  — 控制项 82206545

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
