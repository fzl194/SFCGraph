---
id: UDG@20.15.2@License@LKV3G5LBAA01
type: License
name: 基于位置的地址分配
nf: UDG
version: 20.15.2
license_code: LKV3G5LBAA01
control_item_id: 82200BAK
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 基于位置的地址分配

`LKV3G5LBAA01` · 控制项 82200BAK · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

基于位置的地址分配指<br>UDG<br>跟据用户激活的位置LAC（Location Area Code）或TAC（Tracking Area Code）为用户动态分配IP地址，为特定的区域分配特定的IP地址，实现IP地址的精细化管理。

## 实现描述

如果系统中存在“基于位置的地址分配”的license，则支持基于位置的地址分配，当用户发起激活请求时，<br>UDG<br>根据激活请求消息中携带的位置信息TAC/LAC从对应的地址池中为用户分配特定的IP地址。用户IP地址与所在位置区域对应，外部PDN/DN服务器根据用户IP实施相应的控制策略，从而实现IP地址精细管理和业务精细管理

## 取值范围

0～16000000

## 默认值

10

## 应用场景

运营商针对区域进行IP地址规划和管理，如根据区县规划IP地址段，或者提供区域性差异化应用服务时，可以部署基于位置的地址分配功能。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020421 基于位置的地址分配

## 控制的能力

- [GWFD-020421](feature/UDG/20.15.2/GWFD-020421.md)  — 控制项 82200BAK

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
