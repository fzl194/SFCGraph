---
id: UNC@20.15.2@License@LKV2SMECFP01
type: License
name: MEC单点模式故障保护
nf: UNC
version: 20.15.2
license_code: LKV2SMECFP01
control_item_id: 82200BNJ
applicable_nf:
- SMF
status: active
---

# MEC单点模式故障保护

`LKV2SMECFP01` · 控制项 82200BNJ ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

MEC单点模式是指位于边缘侧的“<br>**ULCL UPF+辅锚点UPF**<br>”的共部署节点只有一个，没有和它形成双主/多主负荷分担的其他UPF。该模式下当该单节点UPF故障，SMF能够感知故障并将该UPF从用户会话中删除，此时用户可通过<br>**主锚点UPF**<br>来访问本地DN和Internet大网。<br>ULCL UPF+辅锚点UPF表示ULCL UPF和辅锚点UPF共部署节点，以下用“<br>**ULCL UPF+辅锚点UPF**<br>”来表示。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

“ULCL UPF+辅锚点UPF”单节点部署场景下，单节点UPF发生故障会对用户访问本地DN的业务造成中断，影响用户体验。<br>部署本特性后，在单节点UPF故障场景下SMF能感知故障并实现用户通过主锚点UPF来访问本地DN和Internet大网，确保用户业务实时通畅。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-108005 MEC单点模式故障保护

## 控制的能力

- [WSFD-108005](feature/UNC/20.15.2/WSFD-108005.md)  — 控制项 82200BNJ

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
