---
id: UDG@20.15.2@License@LKV3G5WBIR01
type: License
name: Web业务分析上报
nf: UDG
version: 20.15.2
license_code: LKV3G5WBIR01
control_item_id: 82200CXS
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# Web业务分析上报

`LKV3G5WBIR01` · 控制项 82200CXS · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制报表是否上报Web业务分析。

## 实现描述

报表是否上报Http Response的单据受license控制。<br>License不开启时，报表不产生HTTP Response单据。从性能角度讲，UDG也不应该因为报表做相关的HTTP下行解析。<br>License 开启时，报表产生Http Response 单据。

## 取值范围

10~8000000

## 默认值

10

## 应用场景

用户使用报表功能时，通过打开web业务分析上报，来对Http Response 业务进行信息收集和上报。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111016 Web业务分析上报

## 控制的能力

- [GWFD-111307](feature/UDG/20.15.2/GWFD-111307.md)  — 控制项 82200CXS

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
