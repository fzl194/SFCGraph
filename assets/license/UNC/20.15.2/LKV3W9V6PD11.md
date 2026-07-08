---
id: UNC@20.15.2@License@LKV3W9V6PD11
type: License
name: IPv6 前缀代理
nf: UNC
version: 20.15.2
license_code: LKV3W9V6PD11
control_item_id: '82208006'
applicable_nf:
- GGSN-C
status: active
---

# IPv6 前缀代理

`LKV3W9V6PD11` · 控制项 82208006 ·  · 域 

## 归属/适用NF（原文）

GGSN-C

## 功能描述

支持为MS分配IPv6 Prefix Delegation地址段（前缀长度大于等于49位且小于64位），让IPv6 MS作为移动路由器为IPv6终端从Prefix Delegation地址段中分配64位前缀，并提供网络接入服务。

## 实现描述

系统中每激活一个IPv6 Prefix Delegation用户的PDP上下文，IPv6 Prefix Delegation的总数加一；每去激活一个IPv6 Prefix Delegation用户的上下文，IPv6 Prefix Delegation的总数减一。<br>如果系统中已接入的支持IPv6 Prefix Delegation功能的PDP上下文数达到License中“IPv6 Prefix Delegation”的最大值，新的IPv6 Prefix Delegation用户PDP上下文无法激活成功。

## 取值范围

0～16000000 PDP

## 默认值

10

## 应用场景

我们知道，IPv4用户支持手机后路由功能，即可以为MS分配一个网段，MS作为一个小的路由器，下面再挂多个终端设备。而IPv6 Prefix Delegation特性就是针对Ipv6 用户的这种需求：使Ipv6的MS既可以作为小型的路由器（比如家庭的路由器），又可以作为企业的路由器。这样就对IPv6的前缀长度要求是可变的。<br>因为Ipv6的地址资源较多，所以这个功能在实际应用中比较常用。

## 相关控制项（原文，未解释为边）

依赖<br>WSFD-104001 IPv6承载上下文<br>WSFD-104002 IPv4v6双栈接入

## 对应特性（原文）

WSFD-104004 IPv6 前缀代理

## 控制的能力

- [WSFD-104004](feature/UNC/20.15.2/WSFD-104004.md)  — 控制项 82208006

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
