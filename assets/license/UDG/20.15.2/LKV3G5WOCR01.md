---
id: UDG@20.15.2@License@LKV3G5WOCR01
type: License
name: 基于小区负荷上报的无线资源优化
nf: UDG
version: 20.15.2
license_code: LKV3G5WOCR01
control_item_id: 82200DHW
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
status: active
---

# 基于小区负荷上报的无线资源优化

`LKV3G5WOCR01` · 控制项 82200DHW · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U

## 功能描述

本控制项控制基于小区负荷上报的无线资源。

## 实现描述

用户是否支持小区拥塞上报受License控制。<br>License不开启时，用户面用户均不能支持小区拥塞信息上报功能；<br>License开启时，即可使用户能够支持小区拥塞信息上报功能。

## 取值范围

0~16000000

## 默认值

10

## 应用场景

RAN侧进行小区拥塞状态监测，通过数据报文中的GTP-U扩展头实时将小区拥塞级别信息上报给PGW-U。PCRF/PCF可以综合相关信息基于小区拥塞级别下发规则给PGW-C/SMF进行策略控制。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110332 基于小区负荷上报的无线资源优化

## 控制的能力

- [GWFD-110332](feature/UDG/20.15.2/GWFD-110332.md)  — 控制项 82200DHW

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
