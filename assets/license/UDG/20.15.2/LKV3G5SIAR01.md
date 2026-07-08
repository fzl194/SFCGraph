---
id: UDG@20.15.2@License@LKV3G5SIAR01
type: License
name: 系统级智能分析记录生成
nf: UDG
version: 20.15.2
license_code: LKV3G5SIAR01
control_item_id: 82200EAK
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# 系统级智能分析记录生成

`LKV3G5SIAR01` · 控制项 82200EAK · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U

## 功能描述

控制报表是否上报系统资源使用数据。

## 实现描述

报表是否上报系统资源使用数据受该License控制。<br>License不开启时，报表不会上报系统资源使用数据。<br>License开启时，报表会上报系统资源使用数据。

## 取值范围

10~8000000

## 默认值

10

## 应用场景

用户使用报表功能时，通过打开系统级智能分析记录生成，来对系统资源使用进行信息收集和上报

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111022 系统级智能分析记录生成

## 控制的能力

- [GWFD-111312](feature/UDG/20.15.2/GWFD-111312.md)  — 控制项 82200EAK

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
