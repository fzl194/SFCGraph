---
id: UNC@20.15.2@License@LKV2GWCN03
type: License
name: 基于LTE的网络共享(GWCN)
nf: UNC
version: 20.15.2
license_code: LKV2GWCN03
control_item_id: '82207539'
applicable_nf:
- MME
status: active
---

# 基于LTE的网络共享(GWCN)

`LKV2GWCN03` · 控制项 82207539 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

基于LTE的网络共享GWCN（Gateway Core Network），指GW核心网方式的网络共享。本特性在<br>UNC<br>支持了多HPLMN功能或MVNO功能的前提下，完成核心网方式的网络共享，即不仅共享无线接入网，而且共享核心网的MME设备。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

共享区域的网络（包括eNodeB和MME）由一个运营商建设，该接入网共享给其他几个运营商。共享网络由运营商Operator X建设，该网络共享给运营商Operator A、Operator B和Operator C。X可以是A、B和C中的任何一个或都不是。<br>- 共享的eNodeB仅需和共享的MME相连，和普通组网没有区别。<br>- 共享的MME需要和多个运营商的其他核心网互连。<br>- 共享的MME完成共享区域内UE的服务请求签约到核心网的路由功能。

## 相关控制项（原文，未解释为边）

依赖WSFD-104401 支持多HPLMN功能

## 对应特性（原文）

WSFD-207004 基于LTE的网络共享(GWCN)

## 控制的能力

- [WSFD-207004](feature/UNC/20.15.2/WSFD-207004.md)  — 控制项 82207539

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
