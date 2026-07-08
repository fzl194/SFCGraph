---
id: UDG@20.15.2@License@LKV3G5L2TP01
type: License
name: L2TP VPN
nf: UDG
version: 20.15.2
license_code: LKV3G5L2TP01
control_item_id: 82200BVC
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# L2TP VPN

`LKV3G5L2TP01` · 控制项 82200BVC · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

利用L2TP协议在<br>UDG<br>与LNS之间建立L2TP VPN，从而实现用户接入企业网。

## 实现描述

UDG<br>解GTP封装后获得原始IP报文，然后作为LAC（L2TP Access Concentrator）为IP报文添加PPP封装，通过与企业网之间建立的二层L2TP隧道，将PPP报文发送到企业网。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

PGW-U、UPF实现PPP再生。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020412 L2TP VPN

## 控制的能力

- [GWFD-020412](feature/UDG/20.15.2/GWFD-020412.md)  — 控制项 82200BVC

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
