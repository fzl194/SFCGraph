---
id: UDG@20.15.2@License@LKV3G5MDRX01
type: License
name: eMTC eDRX模式
nf: UDG
version: 20.15.2
license_code: LKV3G5MDRX01
control_item_id: 82200CKL
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# eMTC eDRX模式

`LKV3G5MDRX01` · 控制项 82200CKL · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U

## 功能描述

物联网终端绝大多数都需要实现低功耗的需求，在省电方面提出了省电模式和扩展的DRX两个关键技术。此license进行eMTC用户的eDRX功能控制，从而将极大节省终端的功耗。

## 实现描述

系统中申请了此license，支持eMTC用户的eDRX功能，否则不支持。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

UDG支持eMTC用户的eDRX功能时，相关终端在非数据发送周期内进入深度睡眠工作模式，并延长传统的不连续接收周期，从而将极大节省终端的功耗。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110641 eMTC eDRX模式

## 控制的能力

- [GWFD-110641](feature/UDG/20.15.2/GWFD-110641.md)  — 控制项 82200CKL

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
