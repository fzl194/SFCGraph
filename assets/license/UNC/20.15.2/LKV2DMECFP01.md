---
id: UNC@20.15.2@License@LKV2DMECFP01
type: License
name: MEC冗余模式故障保护
nf: UNC
version: 20.15.2
license_code: LKV2DMECFP01
control_item_id: 82200BNH
applicable_nf:
- SMF
status: active
---

# MEC冗余模式故障保护

`LKV2DMECFP01` · 控制项 82200BNH ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

MEC冗余模式是指边缘侧UPF采用双主的冗余组网模式。在MEC冗余模式下当其中某个UPF发生故障时，SMF基于N4接口探测实时感知故障，并从与其形成冗余组网的其他UPF中选择一个正常的UPF来快速恢复用户的业务，即“MEC冗余模式故障保护”。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

本特性主要应用于以下两种场景：<br>- 主锚点UPF下沉边缘侧部署，组网上采用双主负荷分担，当其中一个UPF发生故障时，故障UPF上所承载的用户会话无法及时释放，影响用户的正常访问Internet大网和本地DN，以下简称**故障场景1**。部署本特性后SMF能实时感知主锚点UPF的状态，当探测到UPF故障时可以批量去活故障UPF上的用户，用户重新激活时SMF可以为其选择一个正常的UPF，确保用户正常访问Internet大网和本地DN。<br>- ULCL UPF+辅锚点UPF融合部署，组网上采用双主负荷分担，当其中一个UPF发生故障时，大量用户的N4会话滞留在故障UPF上，得不到迁移，影响用户正常访问本地DN，以下简称**故障场景2**。部署本特性后SMF可以实时探测UPF的状态，当探测到UPF故障时可以快速选择一个正常的UPF，并将故障UPF上的用户会话批量迁移到正常的UPF上，确保用户正常访问本地DN。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-108004 MEC冗余模式故障保护

## 控制的能力

- [WSFD-108004](feature/UNC/20.15.2/WSFD-108004.md)  — 控制项 82200BNH

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
