---
id: UDG@20.15.2@License@LKV3G5SBTS01
type: License
name: 基于业务的Shaping
nf: UDG
version: 20.15.2
license_code: LKV3G5SBTS01
control_item_id: 82200AFN
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 基于业务的Shaping

`LKV3G5SBTS01` · 控制项 82200AFN · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

UDG<br>支持基于业务的Shaping功能。

## 实现描述

当用户业务转发速率超出设定带宽时对超出报文进行适当缓存延迟转发，保证转发速率不超过配置带宽；<br>UDG<br>通过license对支持该功能的用户数进行控制。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

通过基于业务的Shaping功能对用户的业务流量进行整形控制，使用户的报文以较均匀的速度发送。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020354 基于业务的Shaping

## 控制的能力

- [GWFD-020354](feature/UDG/20.15.2/GWFD-020354.md)  — 控制项 82200AFN

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
