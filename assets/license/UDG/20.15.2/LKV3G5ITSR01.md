---
id: UDG@20.15.2@License@LKV3G5ITSR01
type: License
name: IM类业务无线资源管控
nf: UDG
version: 20.15.2
license_code: LKV3G5ITSR01
control_item_id: 82200BLD
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
status: active
---

# IM类业务无线资源管控

`LKV3G5ITSR01` · 控制项 82200BLD · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U

## 功能描述

IM（Instant Messaging）类业务无线资源管控是指在无线资源有限的情况下，UDG识别出IM类业务（例如QQ、MSN），并通过IP报文中的DSCP字段或GTP-U扩展头将业务参数传递给无线侧，进而使无线侧对IM类业务进行管控，实现无线资源优化的目的。

## 实现描述

通过SA功能识别出IM业务，并加以标识。两种管控方式的标识方式不同：DSCP（Differentiated Services Code Point）方式下通过Remark功能修改用户报文的DSCP值标识出该业务。GTP-U+BSSGP（Base Station Subsystem GPRS Protocol）方式下在用户报文的GTP-U扩展头中增加一个字段标识出该业务。将含有业务标识的报文传递给SGSN。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

应用于GPRS/UMTS网络无线资源有限的场景。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- SA-IM<br>- PCC基本功能

## 对应特性（原文）

GWFD-020359 IM类业务无线资源管控

## 控制的能力

- [GWFD-020359](feature/UDG/20.15.2/GWFD-020359.md)  — 控制项 82200BLD

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
