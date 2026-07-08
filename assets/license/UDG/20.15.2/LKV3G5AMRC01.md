---
id: UDG@20.15.2@License@LKV3G5AMRC01
type: License
name: 基于APN的eMTC终端接入速率控制
nf: UDG
version: 20.15.2
license_code: LKV3G5AMRC01
control_item_id: 82200CKM
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# 基于APN的eMTC终端接入速率控制

`LKV3G5AMRC01` · 控制项 82200CKM · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U

## 功能描述

基于APN的eMTC终端接入速率控制在P-GW上配置速率门限，用于控制该UE的某PDN连接单位时间内上行和下行数据包的数目。

## 实现描述

系统中申请了此license，支持基于APN的eMTC终端接入速率控制，否则不支持。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

本特性应用于eMTC控制面优化（Control Plane Optimization）和用户面优化（User Plane Optimization）数据传输中，用于限制终端的数据传输速率，在终端异常情况下可以防止网络拥塞而影响业务，提升整网的可靠性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110646 基于APN的eMTC终端接入速率控制

## 控制的能力

- [GWFD-110646](feature/UDG/20.15.2/GWFD-110646.md)  — 控制项 82200CKM

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
