---
id: UDG@20.15.2@License@LKV3G5SRQS01
type: License
name: 支持Reflective QoS
nf: UDG
version: 20.15.2
license_code: LKV3G5SRQS01
control_item_id: '82209870'
license_domain: UDG
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 支持Reflective QoS

`LKV3G5SRQS01` · 控制项 82209870 · resource · 域 UDG

## 归属/适用NF（原文）

UPF

## 功能描述

在没有SMF通过信令提供QoS规则的情况下，UE可以通过反射QoS将上行用户面数据映射到QoS流上。

## 实现描述

系统中每激活一个包含Reflective QoS 功能的Bearer上下文，该功能Bearer上下文数加一；每去激活一个包含Reflective QoS功能Bearer上下文，该功能的Bearer上下文数减一。

## 取值范围

0～1

## 默认值

1

## 应用场景

支持UE上行数据映射到QoS流上。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020101 支持Reflective QoS

## 控制的能力

- [GWFD-020101](feature/UDG/20.15.2/GWFD-020101.md)  — 控制项 82209870

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
