---
id: UNC@20.15.2@License@LKV2UNCCOA1
type: License
name: 支持CoA功能
nf: UNC
version: 20.15.2
license_code: LKV2UNCCOA1
control_item_id: 82200DAY
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# 支持CoA功能

`LKV2UNCCOA1` · 控制项 82200DAY ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

授权修改CoA（Change-of-Authorization）是由AAA Server主动下发修改授权参数的消息，用于修改用户带宽使用策略等。<br>GGSN/PGW-C/SMF支持通过AAA Server下发的修改授权参数的消息，实现对用户业务流的限制，从而保证在业务高峰期网络负载均衡。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

网络中同时部署PCRF/PCF和AAA Server，通过AAA Server下发策略规则后GGSN/PGW-C/SMF转发给PCRF/PCF，然后由PCRF/PCF决定最终策略规则下给用户。<br>网络中同时部署PCRF/PCF和AAA Server，但是用户上下文的PCC功能未能通过AAA鉴权响应消息指示功能关闭，此时GGSN/PGW-C/SMF将AAA下发的策略作为缺省策略信息携带给PCRF/PCF，作为PCRF/PCF决策最终策略的判断依据，GGSN/PGW-C/SMF最终执行PCRF/PCF的响应消息中携带的策略进行计费策略控制。

## 相关控制项（原文，未解释为边）

WSFD-011306 Radius功能

## 对应特性（原文）

WSFD-109005 支持CoA功能

## 控制的能力

- [WSFD-109005](feature/UNC/20.15.2/WSFD-109005.md)  — 控制项 82200DAY

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
