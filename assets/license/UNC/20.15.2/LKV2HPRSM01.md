---
id: UNC@20.15.2@License@LKV2HPRSM01
type: License
name: 基于HSS的P-CSCF故障恢复-USM
nf: UNC
version: 20.15.2
license_code: LKV2HPRSM01
control_item_id: 82200JCN
applicable_nf:
- PGW-C
status: active
---

# 基于HSS的P-CSCF故障恢复-USM

`LKV2HPRSM01` · 控制项 82200JCN ·  · 域 

## 归属/适用NF（原文）

PGW-C

## 功能描述

VoLTE基础语音业务场景下，P-CSCF是用户接入IMS网络的统一入口点，主要负责信令和消息的代理。主叫和被叫的IMS会话消息都会通过P-CSCF。当P-CSCF故障时，由HSS触发P-CSCF故障恢复流程，由MME、HSS、S-CSCF协同实现P-CSCF故障场景下的VoLTE语音快速恢复功能。

## 实现描述

当会话发生基于HSS的P-CSCF重选时，license统计加1；当会话释放时license统计减1。

## 取值范围

0～16000000 Session

## 默认值

10

## 应用场景

P-CSCF故障场景下，VoLTE被叫业务快速恢复。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-201205 基于HSS的P-CSCF故障恢复

## 控制的能力

- [WSFD-201205](feature/UNC/20.15.2/WSFD-201205.md)  — 控制项 82200JCN

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
