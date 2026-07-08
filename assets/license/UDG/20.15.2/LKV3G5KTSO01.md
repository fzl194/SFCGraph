---
id: UDG@20.15.2@License@LKV3G5KTSO01
type: License
name: 基于综合KPI的扩容能力增强
nf: UDG
version: 20.15.2
license_code: LKV3G5KTSO01
control_item_id: '81203221'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 基于综合KPI的扩容能力增强

`LKV3G5KTSO01` · 控制项 81203221 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

支持基于综合KPI的扩容能力增强。

## 实现描述

UDG对业务关键KPI进行监控并转换成业务资源占用率上报到VNFM。VNFM根据收到的业务资源占用率和提前设置的扩容阈值条件触发扩容处理。

## 取值范围

0～1

## 默认值

1

## 应用场景

希望根据业务变化情况进行容量的弹性扩容的情况下，可开通此特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110501 基于综合KPI的扩容能力增强

## 控制的能力

- [GWFD-110501](feature/UDG/20.15.2/GWFD-110501.md)  — 控制项 81203221

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
