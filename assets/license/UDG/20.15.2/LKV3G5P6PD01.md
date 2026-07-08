---
id: UDG@20.15.2@License@LKV3G5P6PD01
type: License
name: IPv6 Prefix Delegation
nf: UDG
version: 20.15.2
license_code: LKV3G5P6PD01
control_item_id: 82200CKF
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# IPv6 Prefix Delegation

`LKV3G5P6PD01` · 控制项 82200CKF · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

UDG<br>支持为MS/UE分配IPv6 Prefix Delegation地址段（前缀长度大于等于49位且小于64位），让IPv6 MS/UE作为移动路由器为IPv6终端从Prefix Delegation地址段中分配64位前缀，并提供网络接入服务。

## 实现描述

系统中每激活一个IPv6 PD Bearer上下文，IPv6 PD 资源数加一；每去激活一个IPv6 PD Bearer上下文，IPv6 PD 资源数减一。<br>如果系统中已接入的IPv6 PD Bearer上下文达到License中“IPv6 Prefix Delegation”数，新的IPv6 PD Bearer上下文将无法接入到系统。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

UDG<br>提供了IPv6 Prefix Delegation功能 ，支持在IPv6组网条件下通过一台无线设备（MS/UE）将多台终端设备接入网络并与网络侧设备进行双向数据业务的技术方案。

## 相关控制项（原文，未解释为边）

IPv6承载上下文

## 对应特性（原文）

GWFD-020406 IPv6 Prefix Delegation

## 控制的能力

- [GWFD-020406](feature/UDG/20.15.2/GWFD-020406.md)  — 控制项 82200CKF

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
