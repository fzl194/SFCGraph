---
id: UNC@20.15.2@License@LKV2MSCMG02
type: License
name: MSC Pool内的用户迁移(Gs接口)
nf: UNC
version: 20.15.2
license_code: LKV2MSCMG02
control_item_id: '81202446'
applicable_nf:
- SGSN
status: active
---

# MSC Pool内的用户迁移(Gs接口)

`LKV2MSCMG02` · 控制项 81202446 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

MSC Pool<br>内的用户迁移（Gs接口）特性是Gs接口的一个增强型功能，当MSC Pool中某个MSC不可用时（如发生故障、升级等），<br>SGSN<br>可以下发启动用户迁移命令，将该MSC的状态信息标识为不可用，然后将该MSC上的用户迁移到MSC Pool中的其他MSC上。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

在MSC Pool组网场景下，如果某个MSC故障或者升级，会导致在该MSC下的用户的附着和位置更新失败或业务中断。为提升用户的联合附着和联合RA/LA更新成功率并减少业务中断时间，可以启用MSC Pool内的用户迁移（基于Gs口）特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-104407 支持Gs接口

## 对应特性（原文）

WSFD-104202 MSC Pool内的用户迁移（Gs接口）

## 控制的能力

- [WSFD-104202](feature/UNC/20.15.2/WSFD-104202.md)  — 控制项 81202446

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967913.md`
