---
id: UNC@20.15.2@License@LKV2ASCC01
type: License
name: 基于APN的信令拥塞控制
nf: UNC
version: 20.15.2
license_code: LKV2ASCC01
control_item_id: '82207033'
applicable_nf:
- SGSN
- MME
status: active
---

# 基于APN的信令拥塞控制

`LKV2ASCC01` · 控制项 82207033 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

基于APN的信令拥塞控制功能是指<br>UNC<br>通过不同的APN来标识不同类型的M2M业务，对引起拥塞的M2M终端进行相关的信令拥塞控制，以避免出现网络风暴。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当M2M终端频繁发起信令流程时，可能导致网络拥塞。基于APN的信令拥塞控制功能对引起拥塞的APN进行相关的拥塞控制。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-206003 基于APN的信令拥塞控制

## 控制的能力

- [WSFD-206003](feature/UNC/20.15.2/WSFD-206003.md)  — 控制项 82207033

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
