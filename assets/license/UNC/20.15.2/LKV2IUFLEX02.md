---
id: UNC@20.15.2@License@LKV2IUFLEX02
type: License
name: Iu-flex
nf: UNC
version: 20.15.2
license_code: LKV2IUFLEX02
control_item_id: '82206554'
applicable_nf:
- SGSN
status: active
---

# Iu-flex

`LKV2IUFLEX02` · 控制项 82206554 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

Iu-flex（Intra-domain connection of RAN nodes to multiple CN nodes）是指一个RAN（Radio Access Network）可以通过Iu接口同时连接多个CS或PS CN（Core Network）节点，多个CS或PS CN节点形成一个池区域，UE在同一池区域内漫游时无需改变服务CN节点。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~12000000 SAU

## 默认值

10

## 应用场景

当组网中存在多组CN节点，并且这些CN节点所服务的<br>LA<br>（Location Area）/<br>RA<br>（Routing Area）有重叠区域时，为了实现负荷分担和容灾，减少区域中SGSN间频繁的<br>路由区更新<br>和切换，可以采用Iu-flex组网模式。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104203 Iu-flex

## 控制的能力

- [WSFD-104203](feature/UNC/20.15.2/WSFD-104203.md)  — 控制项 82206554

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
