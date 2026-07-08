---
id: UNC@20.15.2@License@LKV2SMS02
type: License
name: SMS over GPRS/EDGE/WCDMA
nf: UNC
version: 20.15.2
license_code: LKV2SMS02
control_item_id: '82207548'
applicable_nf:
- SGSN
status: active
---

# SMS over GPRS/EDGE/WCDMA

`LKV2SMS02` · 控制项 82207548 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

SMS over GPRS/EDGE/WCDMA是指SGSN通过分组域为移动用户提供收发短消息的业务。SMS（Short Message Service）是电信业务的一种，它允许用户通过SMC（Short Message Center）发送和接收字符信息。SMS可以由电路域或分组域进行承载。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当某地区经常因为话务高峰期无线接口通道资源不足，而导致短消息延迟时，建议开启SMS over GPRS/EDGE/WCDMA特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106202 SMS over GPRS/EDGE/WCDMA

## 控制的能力

- [WSFD-106202](feature/UNC/20.15.2/WSFD-106202.md)  — 控制项 82207548

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
