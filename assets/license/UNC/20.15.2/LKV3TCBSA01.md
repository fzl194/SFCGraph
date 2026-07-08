---
id: UNC@20.15.2@License@LKV3TCBSA01
type: License
name: 基于业务感知的带宽控制
nf: UNC
version: 20.15.2
license_code: LKV3TCBSA01
control_item_id: 82200CQU
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# 基于业务感知的带宽控制

`LKV3TCBSA01` · 控制项 82200CQU ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

随着移动宽带网络的不断普及，宽带数据业务得到了飞速的发展。P2P业务、网络游戏、VoIP应用的广泛普及为运营商带来了大批的客户，同时也带来了巨大的烦恼。P2P技术的逐步普及，占用了很大的网络带宽资源，并且很多P2P应用是对网络资源进行“恶意的”占用，导致网络不同程度的出现拥塞。为了确保用户业务正常使用，GGSN-C、PGW-C通过带宽管理对流量进行控制。

## 实现描述

该控制项开启时，允许激活PDP上下文后使用基于业务感知的带宽控制的功能；该控制项关闭时，不允许激活PDP上下文后使用基于业务感知的带宽控制的功能。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

基于业务感知的带宽控制的PDP上下文激活。

## 相关控制项（原文，未解释为边）

- SA-Basic。<br>- 依赖WSFD-109101 PCC基本功能

## 对应特性（原文）

WSFD-211005 基于业务感知的带宽控制

## 控制的能力

- [WSFD-211005](feature/UNC/20.15.2/WSFD-211005.md)  — 控制项 82200CQU

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
