---
id: UDG@20.15.2@License@LKV3G5NOIP01
type: License
name: Non-IP数据传输
nf: UDG
version: 20.15.2
license_code: LKV3G5NOIP01
control_item_id: 82200CKH
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# Non-IP数据传输

`LKV3G5NOIP01` · 控制项 82200CKH · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、 PGW-U、UPF

## 功能描述

此license用来控制是否支持用户进行Non-IP数据传输。

## 实现描述

系统中每激活一个支持Non-IP数据传输上下文，支持Non-IP数据传输上下文数加一；每去激活一个支持Non-IP数据传输上下文，支持Non-IP数据传输上下文数减一。<br>如果系统中已接入的支持Non-IP数据传输上下文达到License中“Non-IP数据传输”数值，新的支持Non-IP数据传输上下文将无法接入到系统。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

用户进行Non-IP数据传输。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110607 Non-IP数据传输

## 控制的能力

- [GWFD-110607](feature/UDG/20.15.2/GWFD-110607.md)  — 控制项 82200CKH

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
