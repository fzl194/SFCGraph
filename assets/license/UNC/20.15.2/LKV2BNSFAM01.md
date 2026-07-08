---
id: UNC@20.15.2@License@LKV2BNSFAM01
type: License
name: 支持基于NSSAI选择切片-UAM
nf: UNC
version: 20.15.2
license_code: LKV2BNSFAM01
control_item_id: '82209922'
applicable_nf:
- AMF
status: active
---

# 支持基于NSSAI选择切片-UAM

`LKV2BNSFAM01` · 控制项 82209922 ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

UE发起Registration注册时，AMF判断如果不能为UE提供切片服务，则查询NSSF获取可提供切片服务的AMF的信息，NSSF同时返回为UE分配的切片配置信息。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

10000～12000000 SAU

## 默认值

10

## 应用场景

在基于切片部署组网内，需要开启本特性，以保证5GC当初始AMF无法判断或者判断自己无法为UE提供切片服务，需要向NSSF进行查询获取切片配置信息。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-110001 支持基于NSSAI选择切片

## 控制的能力

- [WSFD-110001](feature/UNC/20.15.2/WSFD-110001.md)  — 控制项 82209922

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
