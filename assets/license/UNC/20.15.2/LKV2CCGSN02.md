---
id: UNC@20.15.2@License@LKV2CCGSN02
type: License
name: 基于计费属性选择网关
nf: UNC
version: 20.15.2
license_code: LKV2CCGSN02
control_item_id: '82206560'
applicable_nf:
- SGSN
- MME
status: active
---

# 基于计费属性选择网关

`LKV2CCGSN02` · 控制项 82206560 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

基于计费属性选择<br>网关<br>，是指<br>UNC<br>在使用<br>APN<br>（Access Point Name）进行<br>DNS<br>(Domain Name Service)解析获取网关<br>IP<br>地址前，首先通过APN定制方法在原APN中加入用户计费信息（CC），然后再对定制后的APN进行DNS解析从而获取相应的网关地址。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

基于计费属性选择网关特性用于多个GGSN/PGW-C组网，有部分GGSN/PGW-C不支持预付费的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205002 基于计费属性选择网关

## 控制的能力

- [WSFD-205002](feature/UNC/20.15.2/WSFD-205002.md)  — 控制项 82206560

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
