---
id: UDG@20.15.2@License@LKV3G5HSHA01
type: License
name: HTTP2.0 Host识别
nf: UDG
version: 20.15.2
license_code: LKV3G5HSHA01
control_item_id: '82209773'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# HTTP2.0 Host识别

`LKV3G5HSHA01` · 控制项 82209773 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

HTTP2.0 Host识别功能是指<br>UDG<br>支持对HTTPS（Hypertext Transfer Protocol over Secure Socket Layer）协议承载的业务进行感知，提取Host并支持匹配，对指定Host的HTTPS业务进行计费与策略控制。

## 实现描述

HTTPS（Hypertext Transfer Protocol over Secure Socket Layer）是基于SSL的HTTP协议传输，是以安全为目标的HTTP通道，它可以保证用户数据加密传输。目前很多业务通过HTTPS协议进行用户验证和数据传输，例如涉及用户隐私的应用：帐户设置、头像设置、个人资料设置等。HTTPS协议的Client-Hello消息中有时会携带扩展属性SNI（Server Name Indication），Certificate消息中会携带id-at-commonName字段。<br>UDG<br>可通过解析以上两个消息对应的字段得到报文携带的Host，并将其同配置的host或者url进行匹配，匹配成功后执行指定的计费与策略控制。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

当运营商期望对指定的域名进行计费与策略控制且业务承载在HTTPS协议上的时候，需要开启本功能。HTTPS属于加密协议，传统的方法不能识别HTTPS业务类型，但如果HTTPS交互的Client-Hello消息中存在SNI或者Certificate消息中存在id-at-commonName的情况，开启本功能，<br>UDG<br>支持HTTPS业务提取Host，运营商可以对HTTPS业务的Host进行计费与策略控制，提高业务套餐包的控制精度，提升用户满意度。<br>由于本特性依赖于HTTPS交互的Client-Hello消息中的SNI以及Certificate消息中的id-at-commonName，所以如果HTTPS交互的Client-Hello消息中不存在SNI且Certificate消息中也不存在id-at-commonName的情况，不适用本特性。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- HTTPS业务地址识别

## 对应特性（原文）

GWFD-110201 HTTP2.0 Host识别

## 控制的能力

- [GWFD-110201](feature/UDG/20.15.2/GWFD-110201.md)  — 控制项 82209773

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
