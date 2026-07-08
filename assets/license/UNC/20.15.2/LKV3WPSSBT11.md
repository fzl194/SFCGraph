---
id: UNC@20.15.2@License@LKV3WPSSBT11
type: License
name: 基于延迟定时器的信令拥塞控制
nf: UNC
version: 20.15.2
license_code: LKV3WPSSBT11
control_item_id: '82209408'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# 基于延迟定时器的信令拥塞控制

`LKV3WPSSBT11` · 控制项 82209408 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

大量终端集中接入移动网络时，容易导致移动网络拥塞，影响数据用户业务。此license进行NB-IoT用户相关的信令拥塞控制，以避免出现网络风暴。

## 实现描述

系统中申请了此license，支持NB-IoT用户延迟定时器的信令拥塞控制，否则不支持。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

支持NB-IoT用户延迟定时器的信令拥塞控制时，在自身系统拥塞，或者周边网元拥塞时，可以减少对设备的信令冲击，提高整网的可靠性。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-215201 基于延时定时器的信令拥塞控制

## 控制的能力

- [WSFD-215201](feature/UNC/20.15.2/WSFD-215201.md)  — 控制项 82209408

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
