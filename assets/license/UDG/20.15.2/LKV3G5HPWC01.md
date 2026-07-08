---
id: UDG@20.15.2@License@LKV3G5HPWC01
type: License
name: SA-HTTP Pipeline & WAP Concatenation
nf: UDG
version: 20.15.2
license_code: LKV3G5HPWC01
control_item_id: '82209754'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SA-HTTP Pipeline & WAP Concatenation

`LKV3G5HPWC01` · 控制项 82209754 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

SA-HTTP Pipeline是指网元支持对Pipeline模式下的同一个数据流上的每个HTTP业务请求及其对应的响应进行业务感知，按照不同业务进行不同的计费和动作处理。<br>SA-WAP concatenation是指网元支持对Concatenation模式下的同一个数据流上的每个WAP业务请求及其对应的响应进行业务感知，按照不同业务进行不同的计费和动作处理。

## 实现描述

SA（Service Awareness）技术是相对SPI（Shallow Packet Inspection）技术提出。与SPI侧重在L3/L4承载层解析不同的是，SA侧重在L7应用层协议分析，包括L3/L4解析和L7解析。SA在完成三四层解析后继续进行协议识别和七层解析。<br>SA完成用户数据报文的解析、协议识别和内容识别，获得目的URL等有价值的信息，为业务解析和安全防护等特性提供依据。三四层解析、协议识别和业务流程的详细描述请参见GWFD-110101 SA-Basic。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

用户进行业务访问，网元对用户的上下行数据包进行识别解析，基于识别的业务种类或解析到的关键字匹配计费和控制规则，达到区分MS使用的不同业务类型实施不同的计费和控制策略的目的。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- SA-Web Browsing<br>- SA-Mobile

## 对应特性（原文）

GWFD-110102 SA-HTTP Pipeline & WAP Concatenation

## 控制的能力

- [GWFD-110102](feature/UDG/20.15.2/GWFD-110102.md)  — 控制项 82209754

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
