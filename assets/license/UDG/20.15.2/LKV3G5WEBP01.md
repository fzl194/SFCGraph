---
id: UDG@20.15.2@License@LKV3G5WEBP01
type: License
name: Web Proxy
nf: UDG
version: 20.15.2
license_code: LKV3G5WEBP01
control_item_id: '82209781'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# Web Proxy

`LKV3G5WEBP01` · 控制项 82209781 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

网元可以把用户的浏览页面请求进行IP重定向到指定代理服务器，通过代理服务器实现网络访问加速或病毒防护。

## 实现描述

Web Proxy的业务流程如下所示：<br>- 浏览网页前，UE向<br>UDG<br>发送要求建立连接的TCP SYN报文。TCP SYN报文触发<br>UDG<br>匹配rule成功，此时，如果rule中配置有web-porxy动作，则<br>UDG<br>执行Web Proxy重定向动作，将目的IP地址转换为代理服务器的IP地址。<br>- UDG<br>将建立连接的TCP SYN报文发送给代理服务器。<br>- 代理服务器收到报文，接受请求并向<br>UDG<br>回应TCP ACK报文。<br>- UDG<br>将源IP地址转换为Web服务器的IP地址，向UE回应TCP ACK报文。<br>- UE发起HTTP请求。目的IP地址为Web服务器IP地址。<br>- UDG<br>将目的IP地址转换为代理服务器的IP地址，将HTTP请求发送到代理服务器，目的IP地址为代理服务器的IP地址。<br>- 可选：代理服务器与Web服务器进行交互，并执行HTTP代理处理功能。<br>- 代理服务器给<br>UDG<br>回复HTTP响应消息，源IP地址为代理服务器的地址。<br>- UDG<br>将源IP地址转换为Web服务器的IP地址，给UE发送一个响应消息。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

通过Web Proxy功能提高用户访问网页的速度或实现病毒防护。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110282 Web Proxy

## 控制的能力

- [GWFD-110282](feature/UDG/20.15.2/GWFD-110282.md)  — 控制项 82209781

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
