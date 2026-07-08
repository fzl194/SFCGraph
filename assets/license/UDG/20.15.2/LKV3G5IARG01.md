---
id: UDG@20.15.2@License@LKV3G5IARG01
type: License
name: 智能分析记录生成
nf: UDG
version: 20.15.2
license_code: LKV3G5IARG01
control_item_id: 82200CXL
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 智能分析记录生成

`LKV3G5IARG01` · 控制项 82200CXL · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

要开启报表功能，必须使用SET RPTGLBCFG GLOBALSWITCH打开全局业务报表上报开关，且有该License。<br>要统计报表总流量的速率，必须有该License。

## 实现描述

通过计算统计时间内报表业务统计的流量 / 报表业务统计时间得出，速率值(量纲：Mbps)。<br>当设备上整机流量连续五分钟达到License值的90%时，产生License资源即将用完告警，告警ID ALM-100046；连续五分钟降到License值的80%时，恢复License资源即将用完告警。<br>当设备上整机流量连续五分钟达到License值时，产生License资源用完告警，告警ID ALM-100049；连续五分钟降到90%时此告警恢复。<br>当设备上整机流量超过License值并产生License用完告警后，设备将限制一定比例的PDP上下文的接入。<br>限制的PDP上下文比例=（当前流量－License阈值流量）*5*100 / License阈值流量。

## 取值范围

10～8000000

## 默认值

10

## 应用场景

要打开报表功能总的License开关，统计报表业务总流量速率时候，需要打开该License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111010 智能分析记录生成

## 控制的能力

- [GWFD-111301](feature/UDG/20.15.2/GWFD-111301.md)  — 控制项 82200CXL

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
