---
id: UNC@20.15.2@License@LKV2UNCUP02
type: License
name: 5G用户业务连续性保障
nf: UNC
version: 20.15.2
license_code: LKV2UNCUP02
control_item_id: '82209150'
applicable_nf:
- SGSN
status: active
---

# 5G用户业务连续性保障

`LKV2UNCUP02` · 控制项 82209150 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

本特性是指UNC支持NSA用户在2/3G PDP激活选择GGSN时，优先选择到支持DCNR的高速GGSN，从而保证NSA用户从GU网络覆盖区域移动到LTE或NR网络覆盖区域时，始终锚定在高速网关上。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

该特性适用于NSA Option3/3a/3x组网与2/3G组网共存场景，当NSA用户在LTE或NR网络覆盖不到的区域从GU网络接入并激活PDP时，为这些用户优先选择到高速GGSN。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104602 NSA用户业务连续性保障

## 控制的能力

- [WSFD-011501](feature/UNC/20.15.2/WSFD-011501.md)  — 控制项 82209150
- [WSFD-104602](feature/UNC/20.15.2/WSFD-104602.md)  — 控制项 82209150

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
