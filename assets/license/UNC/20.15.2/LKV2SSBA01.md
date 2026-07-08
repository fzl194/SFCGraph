---
id: UNC@20.15.2@License@LKV2SSBA01
type: License
name: 支持SBA架构
nf: UNC
version: 20.15.2
license_code: LKV2SSBA01
control_item_id: '81203321'
applicable_nf:
- SGSN
- GGSN-C
- MME
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
status: active
---

# 支持SBA架构

`LKV2SSBA01` · 控制项 81203321 ·  · 域 

## 归属/适用NF（原文）

SGSN、GGSN-C、MME、SGW-C/PGW-C、AMF、SMF、NRF、NSSF、SMSF、NCG

## 功能描述

为了适配未来垂直行业多样化以及不确定的要求，5G网络架构进行了变革，将控制面功能抽象成为多个独立的网络服务，以软件化、模块化、服务化的方式来构建网络。每个网络服务和其他服务在业务功能上解耦，并且对外提供服务化接口，可以通过相同的接口向其它调用者提供服务，将多个耦合接口转变为单一服务接口，从而减少了接口数量。这种架构即是SBA（Service Based Architecture），基于服务的架构。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

SBA网络架构是5GC网络的必选架构。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-010000 支持SBA架构

## 控制的能力

- [WSFD-010000](feature/UNC/20.15.2/WSFD-010000.md)  — 控制项 81203321

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568026.md`
