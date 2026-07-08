---
id: UDG@20.15.2@License@LKV3G5OBCCS1
type: License
name: 小区拥塞优化
nf: UDG
version: 20.15.2
license_code: LKV3G5OBCCS1
control_item_id: 82200FQS
license_domain: VAS
control_item_type: resource
applicable_nf:
- PCEF
- TDF-U
status: active
---

# 小区拥塞优化

`LKV3G5OBCCS1` · 控制项 82200FQS · resource · 域 VAS

## 归属/适用NF（原文）

PCEF/TDF-U

## 功能描述

和NWDAF设备配合在报表系统呈现小区业务流量拥塞情况，并对拥塞小区进行业务进行优化，缓解拥塞状况。

## 实现描述

小区拥塞优化特性受该License控制。<br>License开启时，则使能小区拥塞优化。<br>License关闭时，不使能小区拥塞优化。

## 取值范围

0~ 8000000

## 默认值

10

## 应用场景

当运营商需要对现网小区拥塞情况做分析，并自动进行调整优化时，需要开启本功能。

## 相关控制项（原文，未解释为边）

- 智能分析记录生成<br>- 业务全样分析上报<br>- TCP/UDP传输分析上报<br>- 用户实时位置分析上报<br>- 业务实时分析上报<br>- 业务分析上报订阅<br>- 系统级智能分析记录生成

## 对应特性（原文）

GWFD-111701 拥塞小区分析

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_24575797.md`
