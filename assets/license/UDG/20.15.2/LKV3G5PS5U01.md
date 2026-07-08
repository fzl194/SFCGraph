---
id: UDG@20.15.2@License@LKV3G5PS5U01
type: License
name: 5G UPF 基本软件PDU会话数
nf: UDG
version: 20.15.2
license_code: LKV3G5PS5U01
control_item_id: 82200BWY
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 5G UPF 基本软件PDU会话数

`LKV3G5PS5U01` · 控制项 82200BWY · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

在<br>UDG<br>系统中控制允许接入的5G UPF基本软件PDU会话数的上下文数，当License资源充足时，<br>UDG<br>允许新的5G UPF基本软件PDU会话数的上下文接入系统。

## 实现描述

系统每激活一个5G UPF基本软件PDU会话数的上下文，5G UPF基本软件PDU会话数的上下文数加一；每去激活一个5G UPF基本软件PDU会话数上下文，5G UPF基本软件PDU会话数的上下文数减一。<br>如果系统中已激活的5G UPF基本软件PDU会话数的上下文数，达到License中“5G UPF基本软件PDU会话数”，则新的5G UPF基本软件PDU会话数PDP上下文将无法激活。<br>例如：“5G UPF基本软件PDU会话数”License为1000；系统中当前已接入的5G UPF基本软件PDU会话数PDP上下文为1000，则“5G UPF基本软件PDU会话数”License全部被占用，此时新的5G UPF基本软件PDU会话数d的PDP上下文将无法接入到系统。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

UDG<br>网元中SGW-U，PGW-U，UPF形态下的5G UPF基本软件PDU会话数的上下文接入。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

不涉及

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
