---
id: UDG@20.15.2@License@LKV3G5SNAP01
type: License
name: 5G SA&NSA 基本软件PDU会话数
nf: UDG
version: 20.15.2
license_code: LKV3G5SNAP01
control_item_id: 82200CGH
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 5G SA&NSA 基本软件PDU会话数

`LKV3G5SNAP01` · 控制项 82200CGH · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

在系统中允许接入的5G SA用户与5G NSA用户合一基本软件PDU会话数。允许接入的PDU会话数最大值为【5G SGW-U基本软件PDU会话数】+【5G PGW-U基本软件PDU会话数】+ 【5G UPF 基本软件PDU会话数】。

## 实现描述

系统中每激活5G PGW-U、5G SGW-U和5G UPF中任何一个PDU会话，5G SA&NSA 基本软件PDU会话数会加一，每去活5G PGW-U、5G SGW-U和5G UPF中任何一个PDU会话，5G SA&NSA 基本软件PDU会话数会减一。<br>如果系统中已激活的5G PGW-U PDU会话数达到License“5G SA&NSA 基本软件PDU会话数”且话务峰值已经用完，则新的5G PGW-U会话将无法接入到系统。如果系统中已激活的5G SGW-U PDU会话数达到License“5G SA&NSA 基本软件PDU会话数”且话务峰值已经用完，则新的5G SGW-U会话将无法接入到系统。如果系统中已激活的UPF会话数达到License中“5G UPF 基本软件PDU会话数”与“5G SA&NSA 基本软件PDU会话数”之和且话务峰值已经用完，则新的UPF会话将无法接入到系统。SA&NSA + UPF的PDU 会话数 = SA用户数； 同时，SA&NSA 可以接入NSA用户。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

运营商部署5G SA&NSA用户接入。

## 相关控制项（原文，未解释为边）

5G SGW-U基本软件PDU会话数<br>5G PGW-U基本软件PDU会话数<br>5G UPF 基本软件PDU会话数

## 对应特性（原文）

不涉及

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
