---
id: UDG@20.15.2@License@LKV4TCPBSS01
type: License
name: TCP优化功能
nf: UDG
version: 20.15.2
license_code: LKV4TCPBSS01
control_item_id: 82200DLL
license_domain: VAS
control_item_type: resource
applicable_nf:
- PCEF
- TDF-U
status: active
---

# TCP优化功能

`LKV4TCPBSS01` · 控制项 82200DLL · resource · 域 VAS

## 归属/适用NF（原文）

PCEF/TDF-U

## 功能描述

在系统中控制允许接入vTCP_OPT优化功能的吞吐量。

## 实现描述

当设备上vTCP_OPT优化流量超过License值时，产生License资源即将用完告警，告警为“ALM-100046 资源达到LICENSE扩容门限”。<br>单日使用超限记为一个峰值日，三个连续峰值日记为一个峰值周期；如果累计达到十个峰值周期，并且vTCP_OPT优化流量仍然超过License值，vTCP_OPT优化功能受控，业务老流保持不变，新流bypass，产生License资源用完告警，告警为“ALM-100049 资源达到LICENSE限制值”。

## 取值范围

0～8000000(Mbps)

## 默认值

10

## 应用场景

应用于需要部署vTCP_OPT优化功能的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_24575797.md`
