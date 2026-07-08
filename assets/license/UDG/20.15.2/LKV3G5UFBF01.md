---
id: UDG@20.15.2@License@LKV3G5UFBF01
type: License
name: URL过滤基本功能
nf: UDG
version: 20.15.2
license_code: LKV3G5UFBF01
control_item_id: 82200FCP
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# URL过滤基本功能

`LKV3G5UFBF01` · 控制项 82200FCP · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

按照用户数控制内容过滤功能。

## 实现描述

用户激活或更新时，如果用户的内容过滤开关打开并且License有剩余时，则允许激活或更新流程做内容过滤功能；如果License无剩余，则不允许做内容过滤功能。<br>当一个用户激活或更新为内容过滤用户时，License使用加一。<br>在License值即将耗尽或耗尽时，上报告警，分别为License资源即将用完或License资源用完，告警ID分别为告警ID ALM-100046和ALM-100049。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

当用户使用内容过滤时，开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110471 URL过滤基本功能

## 控制的能力

- [GWFD-110471](feature/UDG/20.15.2/GWFD-110471.md)  — 控制项 82200FCP

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
