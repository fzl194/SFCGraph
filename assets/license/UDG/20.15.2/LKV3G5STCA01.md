---
id: UDG@20.15.2@License@LKV3G5STCA01
type: License
name: 移动VPN智能分流园区接入
nf: UDG
version: 20.15.2
license_code: LKV3G5STCA01
control_item_id: 82200GCJ
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 移动VPN智能分流园区接入

`LKV3G5STCA01` · 控制项 82200GCJ · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

移动VPN方案中，使用UPF的智能分流能力完成双域用户同时访问Internet和园区业务。

## 实现描述

开启License可使双域用户同时访问Internet和园区业务。系统下发动态分流规则支持用户访问Internet或者企业内网，系统从动态规则中识别园区。

## 取值范围

0～12000（园区）

## 默认值

3

## 应用场景

用于2B2C场景下，满足大学校园和政务办公等场景的用户同时访问Internet和2B企业园区，提供广覆盖、低时延、高可靠、大带宽的优质网络传输服务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020531 通用DNN漫游分流

## 控制的能力

- [GWFD-020531](feature/UDG/20.15.2/GWFD-020531.md)  — 控制项 82200GCJ

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
