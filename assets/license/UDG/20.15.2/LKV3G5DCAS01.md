---
id: UDG@20.15.2@License@LKV3G5DCAS01
type: License
name: DNS计费防欺诈
nf: UDG
version: 20.15.2
license_code: LKV3G5DCAS01
control_item_id: '82209787'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# DNS计费防欺诈

`LKV3G5DCAS01` · 控制项 82209787 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

针对黑客通过伪造端口号为53的DNS数据报文的攻击，通过增强的DNS报文识别，判断DNS报文的协议一致性，将真正的用户DNS报文按照原来的规则记为免费，而对伪造的DNS报文按照正常的流量进行计费，实现避免运营商经济损失的目的。

## 实现描述

开通GWFD-110316 DNS计费防欺诈功能，需要购买和加载License项为“82209787 DNS计费防欺诈(每千PDP/Bearer) ”。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

- 用户欠费，访问任何网站都重定向到Portal页面进行充值。为了完成重定向流程，客户端必须完成目的网站的DNS解析流程，才能发起HTTP Get请求，<br>UDG<br>应用重定向规则下发重定向到Portal网站。在此过程中，DNS报文必须免费通过，否则无法完成后续的重定向流程。<br>- 运营商认为DNS报文为非业务报文，通过在<br>UDG<br>配置L3/4：udp server_port=53设置DNS报文免费。DNS欺诈的攻击原理就是利用53端口的DNS不计费特性，通过客户端黑客工具将需要访问的报文封装成53端口的UDP报文，欺诈<br>UDG<br>设备将流量记成免费，然后在伪装的DNS Server上将真实访问的报文取出，作为Proxy代理和业务服务器互通。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- SA-Network Administration<br>- 内容计费基本功能

## 对应特性（原文）

GWFD-110402 DNS计费防欺诈

## 控制的能力

- [GWFD-110402](feature/UDG/20.15.2/GWFD-110402.md)  — 控制项 82209787

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
