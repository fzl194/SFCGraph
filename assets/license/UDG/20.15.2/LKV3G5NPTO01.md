---
id: UDG@20.15.2@License@LKV3G5NPTO01
type: License
name: 网络加速卡流量加速单元
nf: UDG
version: 20.15.2
license_code: LKV3G5NPTO01
control_item_id: 82200EBL
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 网络加速卡流量加速单元

`LKV3G5NPTO01` · 控制项 82200EBL · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

网络加速卡流量加速。

## 实现描述

License开启时，提升单刀片转发性能，提升系统吞吐量。<br>NP按照可使用的最大资源数进行加速（使用率100%）。

## 取值范围

1~128

## 默认值

1

## 应用场景

当客户需要提升单刀片转发性能，提升系统吞吐量时，需要开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

- GWFD-111201 网络加速卡流量加速单元

## 控制的能力

- [GWFD-111201](feature/UDG/20.15.2/GWFD-111201.md)  — 控制项 82200EBL

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
