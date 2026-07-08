---
id: UNC@20.15.2@License@LKV2CSFBMP02
type: License
name: MSC Pool场景下的CSFB
nf: UNC
version: 20.15.2
license_code: LKV2CSFBMP02
control_item_id: '82206602'
applicable_nf:
- MME
status: active
---

# MSC Pool场景下的CSFB

`LKV2CSFBMP02` · 控制项 82206602 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

MSC Pool场景下的CSFB功能是CSFB特性的一个增强型功能，当MSC Pool中某个MSC不可用时（如发生故障、升级等），可以下发启动迁移命令，MME将该MSC的状态信息标识为不可用，系统将该MSC上的用户手动迁移到MSC Pool中的其他MSC上。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当MSC Pool中某个MSC不可用时（如发生故障、升级等），可以下发启动迁移命令，MME将该MSC的状态信息标识为不可用，系统将该MSC上的用户手工迁移到MSC Pool其他MSC上，以确保用户能正常附着。

## 相关控制项（原文，未解释为边）

依赖WSFD-102301 基于CSFB的语音业务或WSFD-104408 通过SGs接口实现短消息

## 对应特性（原文）

WSFD-102504 MSC Pool场景下的CSFB

## 控制的能力

- [WSFD-102504](feature/UNC/20.15.2/WSFD-102504.md)  — 控制项 82206602

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
