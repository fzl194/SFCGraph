---
id: UNC@20.15.2@License@LKV2PCPRSM01
type: License
name: 基于预定义规则的分流策略控制(4G)
nf: UNC
version: 20.15.2
license_code: LKV2PCPRSM01
control_item_id: 82200EDR
applicable_nf:
- SMF
status: active
---

# 基于预定义规则的分流策略控制(4G)

`LKV2PCPRSM01` · 控制项 82200EDR ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

3GPP定义了UL CL(Uplink Classifier)功能，通过上行分流器（即UL CL UPF）实现根据用户业务流特征将访问本地网络的数据分流到本地DN，将访问Internet数据分流到公网，从而实现对用户本地业务数据的分流控制。<br>当用户从4G网络接入或者从5G网络进入到4G网络时，网络侧支持用户在不换卡、不换号的基础上通过UL CL的方式同时访问本地DN和Internet。在此过程中网络侧基于预定义规则向UL CL UPF下发分流策略用于控制数据报文到本地DC和Internet的分发，即“基于预定义规则的分流策略控制(4G)”

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

在UL CL双域分流场景下，当用户从4G网络接入，或者当用户从5G网络进入4G网络时，如果4G网络不支持UL CL分流，行业用户就无法正常访问行业服务。<br>部署本特性后，当园区的5G信号覆盖不完善，用户直接从4G网络接入，或者从5G网络回落到4G网络，可确保用户在签约的范围内基于UL CL正常访问行业服务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-223101 基于预定义规则的分流策略控制(4G)

## 控制的能力

- [WSFD-223101](feature/UNC/20.15.2/WSFD-223101.md)  — 控制项 82200EDR

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
