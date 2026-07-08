---
id: UNC@20.15.2@License@LKV2DIFFSEC01
type: License
name: 差异化服务
nf: UNC
version: 20.15.2
license_code: LKV2DIFFSEC01
control_item_id: 82200FDD
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
status: active
---

# 差异化服务

`LKV2DIFFSEC01` · 控制项 82200FDD ·  · 域 

## 归属/适用NF（原文）

GGSN-C/SGW-C/PGW-C

## 功能描述

基于ARP（Allocation Retention Priority）的差异化服务是指UNC按照用户签约的ARP定义用户级别，并针对不同优先级的用户，提供不同的接入控制策略，保证优先级别高的用户具有优先使用网络资源的权力。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 PDP

## 默认值

10

## 应用场景

随着市场的发展和竞争环境的变化，运营商需要在运营策略上对用户群进行分类，为不同需求的用户群提供不同等级的服务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106303 基于ARP的差异化服务

## 控制的能力

- [WSFD-106303](feature/UNC/20.15.2/WSFD-106303.md)  — 控制项 82200FDD

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
