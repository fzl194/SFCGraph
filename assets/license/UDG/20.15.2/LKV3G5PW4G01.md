---
id: UDG@20.15.2@License@LKV3G5PW4G01
type: License
name: 4G PGW-U基本功能Bearer上下文数
nf: UDG
version: 20.15.2
license_code: LKV3G5PW4G01
control_item_id: '82209845'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
status: active
---

# 4G PGW-U基本功能Bearer上下文数

`LKV3G5PW4G01` · 控制项 82209845 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U

## 功能描述

4G用户接入4G网络、5G NSA/5G SA用户回落4G网络时，控制PGW-U基本接入的Bearer上下文数。

## 实现描述

- 系统中每激活一个4G PGW-U、4G SGW-U与PGW-U合一中的任何一个Bearer上下文，PGW-U基本功能Bearer上下文数加一；每去激活一个4G PGW-U、4G SGW-U与PGW-U合一中的任何一个Bearer上下文，PGW-U基本功能Bearer上下文数减一。<br>- 系统中每激活一个5G PGW-U、5G SGW-U与PGW-U合一、5G UPF中的任何一个Bearer上下文，PGW-U基本功能Bearer上下文数加一；每去激活一个5G PGW-U、5G SGW-U与PGW-U合一、5G UPF中的任何一个Bearer上下文，PGW-U基本功能Bearer上下文数减一。<br>如果系统中上述类型接入的Bearer上下文数，达到License中“4G PGW-U基本功能Bearer上下文数”，且话务峰值已经用完，新的SGW-U上下文将无法接入到系统。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

PGW-U网元中Bearer上下文接入。

## 相关控制项（原文，未解释为边）

4G SGW-U&PGW-U基本功能Bearer上下文数

## 对应特性（原文）

不涉及

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
