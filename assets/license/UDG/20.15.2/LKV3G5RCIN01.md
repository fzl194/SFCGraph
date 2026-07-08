---
id: UDG@20.15.2@License@LKV3G5RCIN01
type: License
name: 计费信息实时提醒
nf: UDG
version: 20.15.2
license_code: LKV3G5RCIN01
control_item_id: '82209826'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 计费信息实时提醒

`LKV3G5RCIN01` · 控制项 82209826 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

本控制项控制允许使用计费信息实时提醒功能的Bearer上下文数，计费信息实时提醒是针对在线计费用户使用业务过程中，给用户提供界面友好的页面型实时消费提醒功能，包括用户首次上网欢迎页面、上网过程流量提醒页面、余额不足充值页面，该控制项控制允许使用该功能的最大Bearer上下文数。

## 实现描述

该License项未用尽时，允许激活的用户使用该功能，可以做一次重定向功能，SMF发送的N4消息中携带有效信元，并且携带的信元值标识需要做实时提醒功能时，可以使用的Bearer数减少1，如果SMF下发N4消息，携带有效信元，且值标识不需要做重定向，并且之前该Bearer标识使用过，则允许使用的Bearer数加1。该License项用尽时，或者License文件过期后，不允许激活的用户使用一次重定向功能。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

支持一次重定向的用户激活成功。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020356 计费信息实时提醒

## 控制的能力

- [GWFD-020356](feature/UDG/20.15.2/GWFD-020356.md)  — 控制项 82209826

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
