---
id: UDG@20.15.2@License@LKV3G5UHBA10
type: License
name: 5G超高带宽承载接入 10Gbps峰值速率
nf: UDG
version: 20.15.2
license_code: LKV3G5UHBA10
control_item_id: 82200EAE
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 5G超高带宽承载接入 10Gbps峰值速率

`LKV3G5UHBA10` · 控制项 82200EAE · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

允许签约的5G用户以下行带宽最大10Gbps的速率接入网络并使用业务。

## 实现描述

系统License项中<br>“5G超高带宽基本功能 10Gbps峰值速率”<br>为可用，并且下行带宽最大为10Gbps的5G用户激活成功，则此License资源项加1。下行带宽最大为10Gbps的5G用户去激活成功，则此License资源项减1。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

当移动运营商需开展5G业务时，首选此项接入技术。

## 相关控制项（原文，未解释为边）

5G超高带宽基本功能 10Gbps峰值速率

## 对应特性（原文）

GWFD-110558 5G超高带宽承载接入,10Gbps峰值速率

## 控制的能力

- [GWFD-110558](feature/UDG/20.15.2/GWFD-110558.md)  — 控制项 82200EAE

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
