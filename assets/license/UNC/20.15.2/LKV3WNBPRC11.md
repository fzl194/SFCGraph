---
id: UNC@20.15.2@License@LKV3WNBPRC11
type: License
name: 基于服务PLMN的NB-IoT终端接入速率控制
nf: UNC
version: 20.15.2
license_code: LKV3WNBPRC11
control_item_id: '82209410'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# 基于服务PLMN的NB-IoT终端接入速率控制

`LKV3WNBPRC11` · 控制项 82209410 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

基于服务PLMN的NB-IoT终端接入速率控制在MME上配置速率门限，并发给UE和SGW-C/PGW-C，用于控制UE和SGW-C/PGW-C单位时间内上行和下行数据包的数目。

## 实现描述

系统中申请了此license，支持基于APN的NB-IoT终端接入速率控制，否则不支持。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

本特性应用于NB-IoT控制面优化（Control Plane Optimization）数据传输中，用于限制终端的数据传输速率，在终端异常情况下可以防止网络拥塞而影响业务，提升整网的可靠性。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-215205 基于服务PLMN的NB-IoT终端接入速率控制

## 控制的能力

- [WSFD-215205](feature/UNC/20.15.2/WSFD-215205.md)  — 控制项 82209410

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
