---
id: UNC@20.15.2@License@LKV2NFBSM01
type: License
name: NRF基本功能-USM
nf: UNC
version: 20.15.2
license_code: LKV2NFBSM01
control_item_id: '81203234'
applicable_nf:
- SMF
status: active
---

# NRF基本功能-USM

`LKV2NFBSM01` · 控制项 81203234 ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

5GC网络采用服务化架构，将控制面功能抽象成为多个独立的网络功能（Network Function，以下简称NF），每个NF支持多个服务（Network Function Service，以下简称NFS）。<br>NRF负责所有NF/NFS的自动化管理，NF/NFS启动后，与NRF之间有注册、去注册、更新、状态订阅和状态通知消息交互，实现5GC网络服务自治理。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

- NF首次上线提供网络服务时，需要先向NRF注册。<br>- NF优雅下电时，需要去注册。<br>- 已注册的NF/NFS Profile发生变化，如NF通过软件升级的方式更新能力，扩展NFS，NF状态发生变化，NF服务的切片发生了变化，NF可访问授权范围发生变化等等，都会向NRF发起NF更新流程。<br>- NF希望了解其他NF/NFS的注册或更新或去注册变化，可以向NRF订阅此NF/NFS的状态信息。<br>- NF希望了解其他NF/NFS的注册或更新或去注册变化，并已经向NRF订阅此NF/NFS的状态信息，当被订阅的NF/NFS状态变化时，NRF会发送对应的订阅通知。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

- WSFD-111001 NF注册<br>- WSFD-111002 NF去注册<br>- WSFD-111003 NF更新<br>- WSFD-111004 NF状态订阅<br>- WSFD-111005 NF状态通知

## 控制的能力

- [WSFD-111001](feature/UNC/20.15.2/WSFD-111001.md)  — 控制项 81203234
- [WSFD-111002](feature/UNC/20.15.2/WSFD-111002.md)  — 控制项 81203234
- [WSFD-111003](feature/UNC/20.15.2/WSFD-111003.md)  — 控制项 81203234
- [WSFD-111004](feature/UNC/20.15.2/WSFD-111004.md)  — 控制项 81203234
- [WSFD-111005](feature/UNC/20.15.2/WSFD-111005.md)  — 控制项 81203234

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568030.md`
