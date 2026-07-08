---
id: UNC@20.15.2@License@LKV3WMTPRC11
type: License
name: 基于服务PLMN的eMTC终端接入速率控制
nf: UNC
version: 20.15.2
license_code: LKV3WMTPRC11
control_item_id: '82209415'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# 基于服务PLMN的eMTC终端接入速率控制

`LKV3WMTPRC11` · 控制项 82209415 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

基于服务PLMN的eMTC终端接入速率控制在MME上配置速率门限，提升用户体验，优化网络效率。

## 实现描述

基于服务PLMN的eMTC终端接入速率控制是在MME上配置速率门限，发给UE和SGW-C/PGW-C，SGW-C/PGW-C根据MME发来的速率控制信息，产生数据包的控制速率，对于超过门限的数据包进行丢包处理，未超过门限的数据包进行正常的转发处理。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

本特性应用于eMTC控制面优化（Control Plane Optimization）数据传输中，用于限制终端的数据传输速率，在终端异常情况下可以防止网络拥塞而影响业务，提升整网的可靠性。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-216105 基于服务PLMN的eMTC终端接入速率控制

## 控制的能力

- [WSFD-216105](feature/UNC/20.15.2/WSFD-216105.md)  — 控制项 82209415

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
