---
id: UDG@20.15.2@License@LKV3G5TCSA01
type: License
name: 基于业务感知的带宽控制
nf: UDG
version: 20.15.2
license_code: LKV3G5TCSA01
control_item_id: '82209832'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 基于业务感知的带宽控制

`LKV3G5TCSA01` · 控制项 82209832 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

随着移动宽带网络的不断普及，宽带数据业务得到了飞速的发展。P2P业务、网络游戏、VoIP应用的广泛普及为运营商带来了大批的客户，同时也带来了巨大的烦恼。P2P技术的逐步普及，占用了很大的网络带宽资源，并且很多P2P应用是对网络资源进行“恶意的”占用，导致网络不同程度的出现拥塞。为了确保用户业务正常使用，<br>UDG<br>通过带宽管理对流量进行控制。

## 实现描述

该控制项开启时，允许激活用户后使用基于业务感知的带宽控制的功能；该控制项关闭时，不允许激活PDP上下文后使用基于业务感知的带宽控制的功能。

## 取值范围

10～16000000

## 默认值

10

## 应用场景

通过基于业务感知的带宽控制功能对用户流量根据业务类型进行业务控制和带宽管理。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- PCC基本功能

## 对应特性（原文）

GWFD-110311 基于业务感知的带宽控制

## 控制的能力

- [GWFD-110311](feature/UDG/20.15.2/GWFD-110311.md)  — 控制项 82209832

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
