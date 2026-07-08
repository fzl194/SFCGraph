---
id: UDG@20.15.2@License@LKV3G5E2ET01
type: License
name: 端到端用户跟踪
nf: UDG
version: 20.15.2
license_code: LKV3G5E2ET01
control_item_id: '81203447'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 端到端用户跟踪

`LKV3G5E2ET01` · 控制项 81203447 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

端到端用户跟踪是指同时在多个网元上对指定用户进行呼叫信令跟踪，各个网元将跟踪结果发送到指定的设备。

## 实现描述

LICENSE中端到端用户跟踪项为允许时，端到端用户跟踪功能生效；否则不生效。

## 取值范围

0～1

## 默认值

1

## 应用场景

运营商部署端到端用户跟踪。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020451 端到端用户跟踪

## 控制的能力

- [GWFD-020451](feature/UDG/20.15.2/GWFD-020451.md)  — 控制项 81203447
- [GWFD-020451-1](feature/UDG/20.15.2/GWFD-020451-1.md)  — 控制项 81203447
- [GWFD-020451-2](feature/UDG/20.15.2/GWFD-020451-2.md)  — 控制项 81203447

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
