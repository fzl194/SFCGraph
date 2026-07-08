---
id: UDG@20.15.2@License@LKV4BSSFIP01
type: License
name: SFIP基本功能(vCPU)
nf: UDG
version: 20.15.2
license_code: LKV4BSSFIP01
control_item_id: '82207065'
license_domain: SFIP
control_item_type: resource
applicable_nf:
- GW-U
- UPF
status: active
---

# SFIP基本功能(vCPU)

`LKV4BSSFIP01` · 控制项 82207065 · resource · 域 SFIP

## 归属/适用NF（原文）

GW-U/UPF

## 功能描述

控制集成的第三方APP的VM实例总vCPU数量。

## 实现描述

总License量纲是部署第三方应用功能VM实例的总资源池，当此控制量纲耗尽后，不允许实例化新的第三方应用VNF；正在运行的应用VNF也不允许Scale Out。

## 取值范围

0~10000

## 默认值

10

## 应用场景

第三方VNF实例化和运行第三方VNF实例Scale Out。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

第三方应用的实例化<br>第三方应用统一管理入口<br>第三方应用的基础可靠性

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_09019541.md`
