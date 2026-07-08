---
id: UDG@20.15.2@License@LKV3G5SANA01
type: License
name: SA-Network Administration
nf: UDG
version: 20.15.2
license_code: LKV3G5SANA01
control_item_id: '82209765'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SA-Network Administration

`LKV3G5SANA01` · 控制项 82209765 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

SA-Network Administration是指网元支持对Network Administration报文进行业务感知，判断访问内容，感知业务，对不同业务进行不同的计费和动作处理。

## 实现描述

SA（Service Awareness）技术是相对SPI（Shallow Packet Inspection）技术提出。与SPI侧重在L3/L4承载层解析不同的是，SA侧重在L7应用层协议分析，包括L3/L4解析和L7解析。三四层解析、协议识别和业务流程的详细描述请参见GWFD-110101SA-Basic。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

用户进行业务访问，网元对用户的上下行数据包进行协议识别，基于识别的Network Administration子协议类型对Network Administration各种业务进行带宽管理、业务控制或报表统计。

## 相关控制项（原文，未解释为边）

SA-Basic

## 对应特性（原文）

GWFD-110136 SA-Network Administration

## 控制的能力

- [GWFD-110136](feature/UDG/20.15.2/GWFD-110136.md)  — 控制项 82209765

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
