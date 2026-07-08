---
id: UDG@20.15.2@License@LKV3G5RBMS01
type: License
name: 支持Routing Behind MS
nf: UDG
version: 20.15.2
license_code: LKV3G5RBMS01
control_item_id: 82200CKP
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 支持Routing Behind MS

`LKV3G5RBMS01` · 控制项 82200CKP · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

Routing Behind MS应用于移动VPN网络，通过一台无线设备（MS/UE）将多台终端设备接入网络并与网络侧设备进行双向数据业务。

## 实现描述

系统中每激活一个Routing Behind MS Bearer上下文，Routing Behind MS 资源数加一；每去激活一个Routing Behind MS Bearer上下文，Routing Behind MS 资源数减一。<br>如果系统中已接入的Routing Behind MS Bearer上下文达到License中“Routing Behind MS”数，新的Routing Behind MS Bearer上下文将无法接入到系统。

## 取值范围

0～20000

## 默认值

10

## 应用场景

Routing Behind MS主要服务于企业的移动VPN用户，<br>UDG<br>网元支持基于APN控制Routing Behind MS功能使能。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110910 支持Routing Behind MS

## 控制的能力

- [GWFD-110910](feature/UDG/20.15.2/GWFD-110910.md)  — 控制项 82200CKP

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
