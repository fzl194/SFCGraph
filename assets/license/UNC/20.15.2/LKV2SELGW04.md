---
id: UNC@20.15.2@License@LKV2SELGW04
type: License
name: 基于P-GW锚点选择S-GW
nf: UNC
version: 20.15.2
license_code: LKV2SELGW04
control_item_id: '82206562'
applicable_nf:
- SGSN
- MME
status: active
---

# 基于P-GW锚点选择S-GW

`LKV2SELGW04` · 控制项 82206562 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

UE从MME切换到GnGp SGSN时，MME需要将<br>“Co-located GGSN-PGW FQDN”<br>信元传递给GnGp SGSN。这样，当UE再从GnGp SGSN切换到MME时，MME可以根据GnGp SGSN带回来的<br>“Co-located GGSN-PGW FQDN”<br>选择拓扑最近的S-GW。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当需要根据<br>“Co-located GGSN-PGW FQDN”<br>信元选择拓扑最近的S-GW时，需要开启此特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-205004 S-GW/P-GW 拓扑选择

## 对应特性（原文）

WSFD-205006 基于P-GW锚点选择S-GW

## 控制的能力

- [WSFD-205006](feature/UNC/20.15.2/WSFD-205006.md)  — 控制项 82206562

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
