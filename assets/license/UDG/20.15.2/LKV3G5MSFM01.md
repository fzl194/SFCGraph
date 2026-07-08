---
id: UDG@20.15.2@License@LKV3G5MSFM01
type: License
name: 支持内置百万级业务规则库
nf: UDG
version: 20.15.2
license_code: LKV3G5MSFM01
control_item_id: 82200CXK
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 支持内置百万级业务规则库

`LKV3G5MSFM01` · 控制项 82200CXK · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

本特性支持OTT业务规则库，在规则库中可定义IP和端口等百万条过滤条件，<br>UDG<br>通过文件方式加载业务规则库进行规则匹配处理，针对不同业务报文实施不同的计费和策略控制，帮助运营商实现业务的精细化运营。

## 实现描述

OTT业务规则库是通过离线工具将OTT企业提供的IP地址、端口号等信息生成的xml文件，提供业务规则匹配时的过滤条件（filter）。无需再通过命令逐条配置过滤条件，便于统一维护和管理。

## 取值范围

0～16000000

## 默认值

0

## 应用场景

IPv6业务在逐渐成为主流，主流应用部署了上万个IPv6 server，此功能可以用于扩充filter的容量，更好的支持IPv6业务的规则匹配。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110321 支持内置百万级业务规则库

## 控制的能力

- [GWFD-110321](feature/UDG/20.15.2/GWFD-110321.md)  — 控制项 82200CXK

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
