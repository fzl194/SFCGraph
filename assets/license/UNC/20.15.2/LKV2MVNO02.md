---
id: UNC@20.15.2@License@LKV2MVNO02
type: License
name: MVNO
nf: UNC
version: 20.15.2
license_code: LKV2MVNO02
control_item_id: '82207540'
applicable_nf:
- SGSN
status: active
---

# MVNO

`LKV2MVNO02` · 控制项 82207540 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

MVNO（Mobile Virtual Network Operator）是指利用MNO（Mobile Network Operator）授权的网络资源，提供业务（包括MNO提供的业务以及MVNO自己定制的业务），并对授权的资源进行维护的虚拟移动运营商。本特性是指MNO授权GSM/UMTS网络资源。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

一个运营商需要租借另外一个运营商资源提供业务的情况下，需要启用本特性。典型的场景为：<br>- 一个无移动牌照的企业，通过租用移动运营商的网络，实现移动业务。<br>- 一个拥有牌照的移动运营商，通过租用其他运营商的网络提供相关的业务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-207005 MVNO

## 控制的能力

- [WSFD-207005](feature/UNC/20.15.2/WSFD-207005.md)  — 控制项 82207540

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248038.md`
