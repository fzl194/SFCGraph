---
id: UDG@20.15.2@License@LKV3G5RUCF01
type: License
name: 关联URL核减
nf: UDG
version: 20.15.2
license_code: LKV3G5RUCF01
control_item_id: 82200AFJ
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 关联URL核减

`LKV3G5RUCF01` · 控制项 82200AFJ · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

本控制项控制允许支持关联URL核减功能的用户PDP上下文激活数。关联URL核减功能是指将HTTP类协议头中的referer字段作为关联URL进行计费。当浏览器向WEB服务器发送请求的时候，一般会带上referer字段，服务器通过该字段可以了解到该请求的链接页面。基于referer字段能够将链接页面关联到主页面的原理，可以实现两者之间的关联计费，将对链接页面的访问也计入主页面的流量中。

## 实现描述

该License项开启时，SA解析组件解析出报文的referer字段，<br>UDG<br>使用报文的referer字段与l7-filter中的URL进行匹配，如果匹配成功则此报文的流量计入l7-filter的费率中，如果未匹配上再使用Request-url进行匹配。<br>系统中每激活一个需要做关联URL核减的PDP上下文，关联URL核减功能PDP上下文数加一；每去激活一个需要做关联URL核减的PDP上下文，关联URL核减功能PDP上下文数减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

通过指定网页链接的广告和图片信息，其URL与该网页不一致，也需计入该网页的流量范围，但是这些URL列表会动态变化，无法预先捕捉且不能在<br>UDG<br>上静态配置，此时<br>UDG<br>的关联URL核减功能就会基于referer字段实现这些URL与该网页的关联。关联URL核减功能可以用于页面统计、防盗链（可以在apache中进行设置，不是从指定页面链接的请求一律拒绝）等。

## 相关控制项（原文，未解释为边）

- 内容计费基本功能<br>- SA-Web Browsing

## 对应特性（原文）

GWFD-020304 关联URL核减

## 控制的能力

- [GWFD-020304](feature/UDG/20.15.2/GWFD-020304.md)  — 控制项 82200AFJ

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
