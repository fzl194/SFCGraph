---
id: UDG@20.15.2@License@LKV3G5VRSR01
type: License
name: VoNR业务质量上报
nf: UDG
version: 20.15.2
license_code: LKV3G5VRSR01
control_item_id: 82200FCH
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# VoNR业务质量上报

`LKV3G5VRSR01` · 控制项 82200FCH · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

本控制项控制允许支持VoNR业务质量上报功能。如果开启VoNR业务质量上报功能，<br>UDG<br>针对VoNR业务进行质量分析和相关性能指标的统计，同时生成VoNR业务质量报表记录，通过Grp接口将报表记录上报到CloudUDN进行VoNR业务质量分析，实现VoNR业务质量可视化。

## 实现描述

VoNR业务质量上报受该Liense控制。<br>License不开启时，不支持VoNR业务质量上报。<br>License开启时，支持VoNR业务质量上报。

## 取值范围

10~8000000

## 默认值

10

## 应用场景

当运营商需要分析统计网络中的VoNR业务质量时，需要开启VoNR业务质量上报功能实现VoNR业务质量可视。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111315 VoNR业务质量上报

## 控制的能力

- [GWFD-111315](feature/UDG/20.15.2/GWFD-111315.md)  — 控制项 82200FCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
