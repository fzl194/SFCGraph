---
id: UDG@20.15.2@License@LKV3G5IACR01
type: License
name: 告警智能关联基本功能
nf: UDG
version: 20.15.2
license_code: LKV3G5IACR01
control_item_id: '81203413'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 告警智能关联基本功能

`LKV3G5IACR01` · 控制项 81203413 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

对因闪断等原因产生链路类告警（告警源来自同一个网元或来自不同的网元），采用智能相关性算法进行分析，并进行归类压缩呈现，减少大量链路类告警造成的维护工作浪费，提升告警分析处理效率。

## 实现描述

网元上报告警数据，U2020/MAE将告警数据解析保存并导入到告警智能压缩算法中，分别进行闪断和频次分析、相关性分析、归并同类告警等处理。通过对不同场景下的告警进行智能压缩处理，并在告警台上处理结果，有效提升维护人员告警分析处理效率。

## 取值范围

0～1

## 默认值

1

## 应用场景

业务运行态下的日常告警监控。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110492 告警智能关联

## 控制的能力

- [GWFD-110492](feature/UDG/20.15.2/GWFD-110492.md)  — 控制项 81203413

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
