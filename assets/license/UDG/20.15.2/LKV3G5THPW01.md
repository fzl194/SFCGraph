---
id: UDG@20.15.2@License@LKV3G5THPW01
type: License
name: 整机吞吐量（Mbps）
nf: UDG
version: 20.15.2
license_code: LKV3G5THPW01
control_item_id: '82209851'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 整机吞吐量（Mbps）

`LKV3G5THPW01` · 控制项 82209851 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

整机吞吐量指整个设备传输用户数据时的吞吐量。

## 实现描述

当设备上整机流量连续五分钟达到License值的90%时，产生License资源即将用完告警，告警ID ALM-100046；连续五分钟降到License值的80%时，恢复License资源即将用完告警。<br>当设备上整机流量连续五分钟达到License值时，产生License资源用完告警，告警ID ALM-100049；连续五分钟降到90%时此告警恢复。<br>当设备上整机流量超过License值并产生License用完告警后，设备将限制PDP上下文的接入。

## 取值范围

0～8000000 (Mbps)

## 默认值

10(Mbps)

## 应用场景

应用于需要控制整机吞吐量的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

不涉及

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
