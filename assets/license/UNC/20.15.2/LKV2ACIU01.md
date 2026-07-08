---
id: UNC@20.15.2@License@LKV2ACIU01
type: License
name: 基于APN的接入速率控制
nf: UNC
version: 20.15.2
license_code: LKV2ACIU01
control_item_id: '82207710'
applicable_nf:
- SGSN
status: active
---

# 基于APN的接入速率控制

`LKV2ACIU01` · 控制项 82207710 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

在行业用户的服务器升级或故障排除的时候，由于2G M2M终端设备行为（附着或PDP激活）不可控，可能触发信令风暴，导致GGSN过载。为了保护GGSN，本特性通过APN识别该类M2M用户，并对信令进行流控。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在行业用户的服务器升级、故障排除的操作时，如果有大量的行业终端在同一时间集中进行附着或PDP激活的话，会对GGSN网元造成冲击。运营商希望针对行业终端信令冲击进行抑制，有效保护现网设备的稳定运行。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106302 基于APN的接入速率控制

## 控制的能力

- [WSFD-106302](feature/UNC/20.15.2/WSFD-106302.md)  — 控制项 82207710

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
