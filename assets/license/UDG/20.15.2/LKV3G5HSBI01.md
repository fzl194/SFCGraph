---
id: UDG@20.15.2@License@LKV3G5HSBI01
type: License
name: HTTPS业务行为识别
nf: UDG
version: 20.15.2
license_code: LKV3G5HSBI01
control_item_id: '82209789'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# HTTPS业务行为识别

`LKV3G5HSBI01` · 控制项 82209789 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

要支持HTTPS业务行为识别必须有该License。

## 实现描述

License开启时，指纹识别和证书检查的开关才有效。License不开启时，指纹识别和证书检查的开关不生效。

## 取值范围

0~16000000

## 默认值

10

## 应用场景

当用户需要HTTPS业务行为识别功能时，需要开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

- GWFD-110404 HTTPS业务行为识别

## 控制的能力

- [GWFD-110404](feature/UDG/20.15.2/GWFD-110404.md)  — 控制项 82209789

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
