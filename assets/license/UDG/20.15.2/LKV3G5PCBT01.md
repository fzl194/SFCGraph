---
id: UDG@20.15.2@License@LKV3G5PCBT01
type: License
name: 基于累计流量的策略控制
nf: UDG
version: 20.15.2
license_code: LKV3G5PCBT01
control_item_id: 82200AFM
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 基于累计流量的策略控制

`LKV3G5PCBT01` · 控制项 82200AFM · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

基于累计流量的策略控制是针对用户在一段时间内的会话级累计流量进行策略控制，当会话级累计流量达到预先设置的阈值时，改变计费和控制策略，如：改变计费的费率，阻塞用户业务或降低业务速率。

## 实现描述

该License项未用尽时，允许激活承载上下文后使用基于累计流量的策略控制的功能；该License项用尽时，或者License文件过期后，不允许激活承载上下文后使用基于累计流量的策略控制的功能。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

基于累计流量的策略控制的承载上下文激活。

## 相关控制项（原文，未解释为边）

PCC基本功能

## 对应特性（原文）

GWFD-020353 基于累计流量的策略控制

## 控制的能力

- [GWFD-020353](feature/UDG/20.15.2/GWFD-020353.md)  — 控制项 82200AFM

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
