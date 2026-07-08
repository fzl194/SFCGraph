---
id: UDG@20.15.2@License@LKV3G5SARS01
type: License
name: 业务分析上报订阅
nf: UDG
version: 20.15.2
license_code: LKV3G5SARS01
control_item_id: 82200EAJ
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# 业务分析上报订阅

`LKV3G5SARS01` · 控制项 82200EAJ · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U

## 功能描述

要支持订阅接口下发业务策略和配置，必须使用SET RPTGLBCFG业务报表全局开关打开订阅策略开关和订阅配置开关，且必须有该License

## 实现描述

报表是否支持订阅接口下发业务策略和配置，受该License控制。<br>License不开启时，SET RPTGLBCFG中订阅策略开关和订阅配置开关不会生效。<br>License开启，并且SET RPTGLBCFG中订阅策略开关和订阅配置开关打开，报表才支持订阅接口下发业务策略和配置。

## 取值范围

10~8000000

## 默认值

10

## 应用场景

用户使用报表功能时，通过打开业务分析上报订阅，以及订阅策略开关和订阅配置开关，来订阅策略和配置。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111021 业务分析上报订阅

## 控制的能力

- [GWFD-111311](feature/UDG/20.15.2/GWFD-111311.md)  — 控制项 82200EAJ

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
