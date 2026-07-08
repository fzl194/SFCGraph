---
id: UNC@20.15.2@License@LKV2DIFSRV02
type: License
name: 基于ARP的差异化服务
nf: UNC
version: 20.15.2
license_code: LKV2DIFSRV02
control_item_id: '82206913'
applicable_nf:
- SGSN
status: active
---

# 基于ARP的差异化服务

`LKV2DIFSRV02` · 控制项 82206913 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

基于ARP（Allocation/Retention Priority）的差异化服务包含两部分：<br>- 按照用户的ARP定义用户级别，基于用户级别配置拒绝用户接入的系统负荷门限，保证高级别用户的接入；另外，SGSN能传递ARP给BSC、RNC、GGSN，由后者进行相应的差异化处理，从而保证整个差异化服务的提供。<br>- 按照不同用户范围，SGSN向BSC/RNC传递ARP参数时，基于系统设置，可以为不同范围的用户提供不同的ARP，从而保证对不同承载进行差异化的处理。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

随着市场的发展和竞争环境的变化，运营商需要在运营策略上对用户进行细分，为不同需求的用户提供不同等级的服务，差异服务正是为满足运营商的这种需求而提出的。通过差异服务实现特权用户的优先接入，以提供高质量的服务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106303 基于ARP的差异化服务

## 控制的能力

- [WSFD-106303](feature/UNC/20.15.2/WSFD-106303.md)  — 控制项 82206913

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
