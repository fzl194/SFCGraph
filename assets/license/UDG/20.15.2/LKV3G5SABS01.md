---
id: UDG@20.15.2@License@LKV3G5SABS01
type: License
name: SA-Basic
nf: UDG
version: 20.15.2
license_code: LKV3G5SABS01
control_item_id: '82209749'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SA-Basic

`LKV3G5SABS01` · 控制项 82209749 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

SA-Basic是SA的基本功能，包括三四层解析、协议识别和七层解析，支持对报文进行业务感知，判断访问内容，感知业务，对不同业务进行不同的计费和动作处理。

## 实现描述

SA（Service Awareness）技术是相对SPI（Shallow Packet Inspection）技术提出。与SPI侧重在L3/L4承载层解析不同的是，SA侧重在L7应用层协议分析，包括L3/L4解析和L7解析。SA在完成三四层解析后继续进行协议识别和七层解析。<br>SA完成用户数据报文的解析、协议识别和内容识别，获得目的URL等有价值的信息，为业务解析和安全防护等特性提供依据。SA对用户数据报文的解析按如下顺序进行：<br>- 三四层解析三四层解析是一种浅度报文检测技术，SA的实现以此为基础，在完成三四层解析后继续进行协议识别和七层解析。获取到报文的以下相关信息：- 源IP地址<br>- 目的IP地址<br>- IP协议类型（TCP/UDP/ICMP等）<br>- 源端口号范围（起始端口号～结束端口号）<br>- 目的端口号范围（起始端口号～结束端口号）<br>- 协议识别协议识别是报文深度解析的基础，只有在识别出用户报文的协议后，才能够对报文做精确的深度解析。可以根据知名端口或者特征字识别出报文的协议。<br>- 七层解析网元识别出报文协议后，进行七层规则匹配，对报文实施不同的计费和控制策略。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

用户进行业务访问，网元对用户的上下行数据包进行识别解析，并基于识别解析结果对业务进行带宽管理、业务控制或报表统计。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110101 SA-Basic

## 控制的能力

- [GWFD-110101](feature/UDG/20.15.2/GWFD-110101.md)  — 控制项 82209749

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
