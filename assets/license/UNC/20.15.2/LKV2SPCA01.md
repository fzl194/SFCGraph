---
id: UNC@20.15.2@License@LKV2SPCA01
type: License
name: 终端侧二次PDP上下文激活
nf: UNC
version: 20.15.2
license_code: LKV2SPCA01
control_item_id: '82206543'
applicable_nf:
- SGSN
status: active
---

# 终端侧二次PDP上下文激活

`LKV2SPCA01` · 控制项 82206543 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

SGSN支持用户发起的二次PDP上下文激活。二次PDP上下文激活是为了重用已激活的PDP上下文资源，如APN和PDP地址。二次激活的会话与一次会话的不同在于采用了不同的QoS。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~12000000 SAU

## 默认值

10

## 应用场景

当用户在终端上运行多个应用程序，且使用单APN与IP地址时，因为不同业务使用不同QoS等级的承载，需要使用终端侧二次PDP上下文激活功能。例如：用户需要一边浏览网页，一边下载文件时，主PDP用于浏览网页，二次PDP用于传送媒体流。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106001 终端侧二次PDP上下文激活

## 控制的能力

- [WSFD-106001](feature/UNC/20.15.2/WSFD-106001.md)  — 控制项 82206543

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
