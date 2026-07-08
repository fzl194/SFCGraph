---
id: UDG@20.15.2@License@LKV3G5OVBC01
type: License
name: UPF过载限速
nf: UDG
version: 20.15.2
license_code: LKV3G5OVBC01
control_item_id: '81204033'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# UPF过载限速

`LKV3G5OVBC01` · 控制项 81204033 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

支持UPF过载限速功能。

## 实现描述

此License开启，UPF业务节点CPU过载后支持主动通过QoS控制减少用户上下行最大带宽，降低端到端流量，减少UPF业务节点负载。

## 取值范围

0～1

## 默认值

1

## 应用场景

运营商根据实际网络容灾情况选择使用该license。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111700 UPF过载限速

## 控制的能力

- [GWFD-111700](feature/UDG/20.15.2/GWFD-111700.md)  — 控制项 81204033

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
