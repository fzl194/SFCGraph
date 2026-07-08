---
id: UNC@20.15.2@License@LKV2GSUE02
type: License
name: 基于UE接入能力选择网关
nf: UNC
version: 20.15.2
license_code: LKV2GSUE02
control_item_id: '82205920'
applicable_nf:
- SGSN
- MME
status: active
---

# 基于UE接入能力选择网关

`LKV2GSUE02` · 控制项 82205920 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

UNC<br>可以根据UE的接入能力选择GGSN/PGW-C。这样可以保证GERAN/UTRAN和E-UTRAN之间互操作的成功率。随着拥有接入能力的UE数量的增多，传统的GGSN可以平滑地切换到GGSN/PGW-C。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

适用于传统GGSN和新部署的合建GGSN/P-GW并存的组网场景，也适用于新部署的独立P-GW和合建GGSN/P-GW并存的组网场景。

## 相关控制项（原文，未解释为边）

- 请求信息纠正功能<br>- 别名APN<br>- 用户接入控制功能

## 对应特性（原文）

WSFD-205005 基于UE接入能力选择网关

## 控制的能力

- [WSFD-205005](feature/UNC/20.15.2/WSFD-205005.md)  — 控制项 82205920

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
