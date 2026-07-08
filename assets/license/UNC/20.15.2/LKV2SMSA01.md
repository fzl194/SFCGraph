---
id: UNC@20.15.2@License@LKV2SMSA01
type: License
name: 支持微服务架构
nf: UNC
version: 20.15.2
license_code: LKV2SMSA01
control_item_id: '81203323'
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

# 支持微服务架构

`LKV2SMSA01` · 控制项 81203323 ·  · 域 

## 归属/适用NF（原文）

SGSN、GGSN-C、MME、SGW-C/PGW-C、AMF、SMF、NRF、NSSF、SMSF、NCG

## 功能描述

微服务架构（Microservice Architect）是一种架构模式，它提倡将单体架构的应用划分成一组小的服务，服务之间互相协调、互相配合，为用户提供最终价值。每个服务运行在其独立的进程中，服务与服务间采用轻量级的通信机制互相沟通。每个服务都围绕着具体业务进行构建，并且能够被独立的部署到生产环境、类生产环境等。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

微服务架构是5G Core网络的必选架构。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-010003 支持微服务架构

## 控制的能力

- [WSFD-010003](feature/UNC/20.15.2/WSFD-010003.md)  — 控制项 81203323

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568026.md`
