---
id: UNC@20.15.2@License@LKV2GWUS01
type: License
name: GW-U选择
nf: UNC
version: 20.15.2
license_code: LKV2GWUS01
control_item_id: 82200BES
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# GW-U选择

`LKV2GWUS01` · 控制项 82200BES ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

UNC可以根据用户接入的APN、位置信息，为用户选择满足指定业务的、地理位置贴近用户的SGW-U/PGW-U。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

- 当运营商为用户的某些业务规划部署专用的SGW-U/PGW-U设备时，可以使用该特性。<br>- 当运营商将SGW-U/PGW-U设备部署到贴近用户的地理位置时，可以使用该特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-107005 GW-U选择

## 控制的能力

- [WSFD-107005](feature/UNC/20.15.2/WSFD-107005.md)  — 控制项 82200BES

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
