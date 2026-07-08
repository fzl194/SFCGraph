---
id: UNC@20.15.2@License@LKV2DTUSR02
type: License
name: 主动分离未激活用户
nf: UNC
version: 20.15.2
license_code: LKV2DTUSR02
control_item_id: '82206612'
applicable_nf:
- SGSN
status: active
---

# 主动分离未激活用户

`LKV2DTUSR02` · 控制项 82206612 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

当用户通过附着或路由区更新流程接入到本SGSN后，如果在指定时长没有PDP（Packet Data Protocol）激活，则认为该用户为非活动用户对用户进行分离操作，以释放此类用户的空闲资源，支持更多的用户。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

本特性适用于某一网络中许多用户签约了GPRS业务，但是几乎不使用该业务的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106205 主动分离未激活用户

## 控制的能力

- [WSFD-106205](feature/UNC/20.15.2/WSFD-106205.md)  — 控制项 82206612

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
