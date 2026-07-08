---
id: UNC@20.15.2@License@LKV3WMTARC11
type: License
name: 基于APN的eMTC终端接入速率控制
nf: UNC
version: 20.15.2
license_code: LKV3WMTARC11
control_item_id: '82209414'
applicable_nf:
- PGW-C
status: active
---

# 基于APN的eMTC终端接入速率控制

`LKV3WMTARC11` · 控制项 82209414 ·  · 域 

## 归属/适用NF（原文）

PGW-C

## 功能描述

基于APN的eMTC终端接入速率控制在PGW-C上配置速率门限，用于控制该UE的某PDN连接单位时间内上行和下行数据包的数目。

## 实现描述

基于APN的eMTC终端接入速率控制是在PGW-C上配置速率门限，对超过速率门限的数据包进行丢弃处理。PGW-C使用PCO/ePCO信元将基于APN的eMTC终端接入速率控制参数发送给UE，用于控制该UE的某PDN连接单位时间内上行和下行数据包的数目。MME/SGW-C支持转发UE和PGW-C之间速率控制参数的消息。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

用户在附着后短时间内发送一定的数据包后退网，当该用户再次入网时之前发送的数据包不会被PGW-C统计到单位时间内发送的数据包内，PGW-C重新开始进行该用户的速率控制计时和计数。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-216104 基于APN的eMTC终端接入速率控制

## 控制的能力

- [WSFD-216104](feature/UNC/20.15.2/WSFD-216104.md)  — 控制项 82209414

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
