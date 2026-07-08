---
id: UNC@20.15.2@License@LKV2SAUSC01
type: License
name: 5G UE信令控制
nf: UNC
version: 20.15.2
license_code: LKV2SAUSC01
control_item_id: 82200CQT
applicable_nf:
- AMF
status: active
---

# 5G UE信令控制

`LKV2SAUSC01` · 控制项 82200CQT ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

5G UE信令控制是指在Smartphone反复发送Registration Request、PDU Session Establishment Request、Service Request消息的场景下，当某一消息达到设定的阈值时，AMF可以根据已配置的基于终端类型、信令流程的控制策略对UE的异常行为进行抑制，减轻由于UE的异常行为对网络侧的影响，有效地减少网络中的异常信令，提升网络可用性和可靠性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

5G SA网络中，在终端反复发送Registration Request、PDU Session Establishment Request、Service Request，产生大量异常信令的情况下，利用异常信令控制功能可以减少网络的信令负荷。<br>UE反复发送Registration Request消息原因有很多，主要可以分两类：用户原因和网络原因。<br>- 用户原因有用户未签约、用户非法接入、用户欠费停机、用户漫游受限等。<br>- 网络原因有UDM、NRF设备短暂故障或拥塞，由于网元故障导致的导致频繁接入。<br>UE反复发送PDU Session Establishment Request消息原因主要有：<br>- 用户原因（如用户欠费）导致承载建立失败。<br>- 周边网元故障（SMF、PCF等）导致承载建立失败。<br>- 上层应用业务故障，导致的终端自动反复承载建立成功/去活。<br>智能终端的快速休眠和永久在线会导致Service Request消息激增。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-206008 5G UE信令控制

## 控制的能力

- [WSFD-206008](feature/UNC/20.15.2/WSFD-206008.md)  — 控制项 82200CQT

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848073.md`
