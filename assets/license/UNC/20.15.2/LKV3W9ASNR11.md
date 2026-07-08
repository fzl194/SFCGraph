---
id: UNC@20.15.2@License@LKV3W9ASNR11
type: License
name: ASN漫游计费
nf: UNC
version: 20.15.2
license_code: LKV3W9ASNR11
control_item_id: '82209618'
applicable_nf:
- GGSN-C
- PGW-C
status: active
---

# ASN漫游计费

`LKV3W9ASNR11` · 控制项 82209618 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C

## 功能描述

ASN漫游计费，是指GGSN/PGW-C获取到对端SGSN/SGW-C网元配置的ASN值，将SGSN/SGW-C所在的BGP路由的自治系统号（ASNAutonomous System Number）作为漫游用户标识，通过Gy接口的CCR消息携带给OCS服务器，目的是对不同PLMN内的用户采用不同的费率进行计费。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

GGSN/PGW-C对漫游用户进行计费有两种方式：<br>- 根据漫游SGSN/SGW-C的激活请求消息中携带的RAI、ULI信元标识出用户当前接入的PLMN，进而上报给计费系统进行漫游计费。<br>- 在GGSN/PGW-C本地建立可漫游的其他PLMN网络所有SGSN/SGW-C的IP地址与PLMN映射表，漫游用户激活时，根据激活请求消息中携带的SGSN/SGW-C查找用户当前接入的PLMN，进而上报给计费系统进行漫游计费。<br>但是，上面两种方式实现的时候会有诸多限制而不能进行漫游计费，如：<br>- 有的漫游SGSN/SGW-C的激活请求消息不支持携带RAI、ULI信元。<br>- 无法获取到可漫游的其他PLMN网络所有SGSN/SGW-C的IP地址，或者这些SGSN/SGW-C IP地址经常改动，维护不方便。<br>这样的情况下，又有漫游计费需求，则可以采用ASN漫游计费。

## 相关控制项（原文，未解释为边）

WSFD-109001 Gy/Diameter在线计费

## 对应特性（原文）

WSFD-109006 ASN漫游计费特性

## 控制的能力

- [WSFD-109006](feature/UNC/20.15.2/WSFD-109006.md)  — 控制项 82209618

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
