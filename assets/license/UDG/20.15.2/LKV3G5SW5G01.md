---
id: UDG@20.15.2@License@LKV3G5SW5G01
type: License
name: 5G SGW-U基本功能Bearer上下文数
nf: UDG
version: 20.15.2
license_code: LKV3G5SW5G01
control_item_id: '82209849'
license_domain: UDG
control_item_type: resource
status: active
---

# 5G SGW-U基本功能Bearer上下文数

`LKV3G5SW5G01` · 控制项 82209849 · resource · 域 UDG

## 功能描述

在系统中控制允许接入的5G SGW-U基本功能Bearer上下文数，允许接入的5G SGW-U基本功能Bearer上下文数最大值为【5G SGW-U基本功能Bearer上下文数】+【5G SGW-U&PGW-U基本功能Bearer上下文数】。<br>5G SGW-U用户专指5G NSA用户。

## 实现描述

系统中每激活一个SGW-U的Bearer上下文，SGW-U基本功能Bearer上下文数加一；每去激活一个SGW-U的Bearer上下文，SGW-U基本功能Bearer上下文数减一。<br>如果系统中已接入的SGW-U的Bearer上下文数加上SGW-U与PGW-U合一的Bearer上下文数，达到License中“5G SGW-U基本功能Bearer上下文数”、“5G SGW-U&PGW-U基本功能Bearer上下文数”，且话务峰值已经用完，新的SGW-U上下文将无法接入到系统。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

SGW-U网元中 Bearer上下文接入。

## 相关控制项（原文，未解释为边）

5G SGW-U&PGW-U基本功能Bearer上下文数

## 对应特性（原文）

不涉及

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
