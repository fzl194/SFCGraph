---
id: UDG@20.15.2@License@LKV4ISCFUN02
type: License
name: Traffic Steering基本功能(Mbps)
nf: UDG
version: 20.15.2
license_code: LKV4ISCFUN02
control_item_id: '82207650'
license_domain: SFIP
control_item_type: resource
applicable_nf:
- GW-U
- UPF
status: active
---

# Traffic Steering基本功能(Mbps)

`LKV4ISCFUN02` · 控制项 82207650 · resource · 域 SFIP

## 归属/适用NF（原文）

GW-U/UPF

## 功能描述

控制流串接功能特性

## 实现描述

该License资源项未用尽时，则使能流串接功能特性；<br>该License项用尽时，或者License文件过期后，流串接功能特性受控，业务老流维持现有串接特性不变，所有业务新流bypass。

## 取值范围

0~8000000

## 默认值

10

## 应用场景

开启流串接功能，业务流量上送自研或者三方APP，增值业务。

## 相关控制项（原文，未解释为边）

SFIP基本功能(vCPU)

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_09019541.md`
