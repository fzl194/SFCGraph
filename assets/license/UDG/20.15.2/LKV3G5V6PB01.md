---
id: UDG@20.15.2@License@LKV3G5V6PB01
type: License
name: IPv6承载上下文
nf: UDG
version: 20.15.2
license_code: LKV3G5V6PB01
control_item_id: '82209828'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# IPv6承载上下文

`LKV3G5V6PB01` · 控制项 82209828 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

在系统中控制允许接入的IPv6 PDP上下文数，允许接入的IPv6 PDP上下文数最大值为【IPv6承载上下文数】。

## 实现描述

系统中每激活一个IPv6 PDP上下文，IPv6 PDP上下文数加一；每去激活一个IPv6 PDP上下文，IPv6 PDP上下文数减一。<br>如果系统中已接入的IPv6 PDP上下文达到License中“IPv6 承载上下文数”，新的IPv6 PDP上下文将无法接入到系统。<br>例如：“IPv6 承载上下文数”License为1000；系统中当前已接入的IPv6 PDP上下文数为1000，那么“IPv6 承载上下文数”License全部被占用，则此时新的IPv6 PDP上下文将无法接入到系统。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

UDG<br>网元中IPv6 PDP上下文接入。

## 相关控制项（原文，未解释为边）

N6/Gi/SGi接口IPv6组网

## 对应特性（原文）

GWFD-020401 IPv6承载上下文

## 控制的能力

- [GWFD-020401](feature/UDG/20.15.2/GWFD-020401.md)  — 控制项 82209828

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
