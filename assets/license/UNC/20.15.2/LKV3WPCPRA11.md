---
id: UNC@20.15.2@License@LKV3WPCPRA11
type: License
name: 基于指定区域的策略控制-USM
nf: UNC
version: 20.15.2
license_code: LKV3WPCPRA11
control_item_id: '82208348'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# 基于指定区域的策略控制-USM

`LKV3WPCPRA11` · 控制项 82208348 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

基于指定区域的策略控制特性是指基于运营商订阅的PRA（Presence Report Area）区域，当用户进入或离开这些区域时，UNC获得用户当前位置信息并向PCRF/PCF上报，PCRF/PCF根据用户位置状态进行策略决策并发起策略更新，执行不同的服务策略（如特殊计费、套餐、信息推送等），满足运营商基于位置信息的差异化和定制化需求，用户通过签约享受相应服务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

基于指定区域的策略控制特性支持MME在用户进入或离开指定区域时向SGW-C/PGW-C上报位置信息，PCRF/PCF根据此位置信息更新并向SGW-C/PGW-C下发对应的策略，典型应用场景如下。商场、校园、体育场、地铁沿线等需要向用户提供基于位置的计费优惠、套餐服务时，运营商会部署基于指定区域的策略控制。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-211003 基于指定区域的策略控制

## 控制的能力

- [WSFD-106010-1](feature/UNC/20.15.2/WSFD-106010-1.md)  — 控制项 82208348
- [WSFD-211003](feature/UNC/20.15.2/WSFD-211003.md)  — 控制项 82208348

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
