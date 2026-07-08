---
id: UDG@20.15.2@License@LKV3G5UHBG01
type: License
name: 5G超高带宽承载接入-1Gbps 保障速率
nf: UDG
version: 20.15.2
license_code: LKV3G5UHBG01
control_item_id: 82200ETE
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 5G超高带宽承载接入-1Gbps 保障速率

`LKV3G5UHBG01` · 控制项 82200ETE · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

允许签约的5G用户以下行带宽不超过1Gbps速率接入网络时被识别为高速用户。

## 实现描述

系统License项中“5G超高带宽承载接入-1Gbps保障速率”为可用，并且下行带宽不超过1Gbps的5G用户被识别为高速用户，则此License资源项加1。下行带宽不超过1Gbps的5G高速用户去激活成功，则此License资源项减1。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

当运营商开展5G业务，使用超高带宽功能时，开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111401 5G超高带宽承载接入，1Gbps保障速率

## 控制的能力

- [GWFD-111401](feature/UDG/20.15.2/GWFD-111401.md)  — 控制项 82200ETE

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
