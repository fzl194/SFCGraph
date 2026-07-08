---
id: UDG@20.15.2@License@LKV3G5IPSM01
type: License
name: 基于基站粒度的IPSQM
nf: UDG
version: 20.15.2
license_code: LKV3G5IPSM01
control_item_id: 82200DHV
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
status: active
---

# 基于基站粒度的IPSQM

`LKV3G5IPSM01` · 控制项 82200DHV · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U

## 功能描述

本控制项控制基于基站粒度进行IPSQM整形的吞吐量。

## 实现描述

当License资源充足时，所有符合基于基站粒度的IPSQM功能的用户流量，都会经过IPSQM整形处理，并将整形转发和丢弃的流量统计到基于基站粒度的IPSQM整形吞吐量中。

## 取值范围

0~8000000(Mbps)

## 默认值

10(Mbps)

## 应用场景

在承载网采用微波技术的情况下，基站和UPF之间的链路是网络带宽瓶颈。另外，微波带宽会随天气而变化，带宽不稳定，需要对基站进行静态整形。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110941 基于基站粒度的IPSQM

## 控制的能力

- [GWFD-110941](feature/UDG/20.15.2/GWFD-110941.md)  — 控制项 82200DHV

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
