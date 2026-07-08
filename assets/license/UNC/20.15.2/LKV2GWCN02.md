---
id: UNC@20.15.2@License@LKV2GWCN02
type: License
name: 网络共享(GWCN)
nf: UNC
version: 20.15.2
license_code: LKV2GWCN02
control_item_id: '82207708'
applicable_nf:
- SGSN
status: active
---

# 网络共享(GWCN)

`LKV2GWCN02` · 控制项 82207708 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

本特性在<br>UNC<br>支持了多HPLMN功能或MVNO功能的前提下，完成无线网络的共享，即不仅共享<br>无线接入网<br>，而且共享核心网的SGSN设备。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

该场景的主要特征如下：<br>- 共享区域的网络（包括RAN和SGSN/MSC）由一个运营商建设，该网络共享给其他几个运营商。<br>- 共享的RAN仅需和共享的SGSN/MSC相连，和普通组网没有区别。<br>- 共享的SGSN/MSC需要和多个运营商的其他核心网互连。<br>- 共享的SGSN/MSC完成共享区域内UE的服务请求到相应核心网的路由功能。

## 相关控制项（原文，未解释为边）

互斥WSFD-207001 网络共享（MOCN）<br>依赖WSFD-104401 支持多HPLMN功能或WSFD-210004 MVNO

## 对应特性（原文）

WSFD-207002 网络共享（GWCN）

## 控制的能力

- [WSFD-207002](feature/UNC/20.15.2/WSFD-207002.md)  — 控制项 82207708

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248038.md`
