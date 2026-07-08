---
id: UNC@20.15.2@License@LKV2SMAP01
type: License
name: AMF Pool用户迁移
nf: UNC
version: 20.15.2
license_code: LKV2SMAP01
control_item_id: 82200BAG
applicable_nf:
- AMF
status: active
---

# AMF Pool用户迁移

`LKV2SMAP01` · 控制项 82200BAG ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

根据AMF Pool内各AMF的负载情况，操作人员通过EMS（Element Management System）下发启动迁移命令，将负载过高或需要升级的AMF上的用户迁移到AMF Pool中的其他AMF上，从而实现实时、动态地调整AMF Pool内的负荷分布。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

10000～16000000 SAU

## 默认值

10

## 应用场景

AMF Pool组网场景下，AMF Pool组网要求Pool区内的gNodeB与所有AMF全互联，不建议AMF覆盖Pool外的gNodeB，否则用户迁移功能不可用，且管理复杂。AMF Pool区内包含完整的TA和TA List。

## 相关控制项（原文，未解释为边）

依赖WSFD-104301 AMF Pool

## 对应特性（原文）

WSFD-104302 AMF Pool用户迁移

## 控制的能力

- [WSFD-104302](feature/UNC/20.15.2/WSFD-104302.md)  — 控制项 82200BAG

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
