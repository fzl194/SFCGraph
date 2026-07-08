---
id: UDG@20.15.2@License@LKV3G5HCAS01
type: License
name: HTTP计费防欺诈
nf: UDG
version: 20.15.2
license_code: LKV3G5HCAS01
control_item_id: '82209788'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# HTTP计费防欺诈

`LKV3G5HCAS01` · 控制项 82209788 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

针对黑客通过工具伪造Host字段和url字段的攻击方法，通过自学习Host 和对应的IP地址关系表，在免费流量匹配的时候，增加目的IP地址的校验，如果报文的目的地址是Host对应的IP地址，则认为是正常报文，匹配免费费率；否则对于不满足免费费率条件，按照正常流量进行计费，实现避免运营商经济损失的目的。

## 实现描述

开通HTTP计费防欺诈功能，需要购买和加载License项为“HTTP计费防欺诈”

## 取值范围

0～16000000

## 默认值

10

## 应用场景

针对HTTP浏览类业务生效，对HTTPS和非浏览类业务无效。<br>运营商为了吸引用户，推出了各种优惠费率或免费的业务套餐包，这类套餐的用户报文中会包含相同的关键字。这些特征被非法工具利用后，将用户正常计费业务报文构造成伪套餐包特征的报文。在HTTP Host字段中携带套餐包Host信息，真实的URL填写在HTTP Path字段、Referer字段或者其他扩展字段中，通过代理服务器来访问真实的网页地址，达到骗取优惠费率或者免费上网的目的。

## 相关控制项（原文，未解释为边）

- SA-Network Administration<br>- SA-Web Browsing<br>- 内容计费基本功能

## 对应特性（原文）

GWFD-110403 HTTP计费防欺诈

## 控制的能力

- [GWFD-110403](feature/UDG/20.15.2/GWFD-110403.md)  — 控制项 82209788

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
