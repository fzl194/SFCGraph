---
id: UDG@20.15.2@License@LKV3G5H2PF01
type: License
name: HTTP2.0协议回落
nf: UDG
version: 20.15.2
license_code: LKV3G5H2PF01
control_item_id: '82209774'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# HTTP2.0协议回落

`LKV3G5H2PF01` · 控制项 82209774 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

HTTP2.0协议回落功能是指<br>UDG<br>支持对HTTP1.x协议升级到HTTP2.0协议的过程进行处理，保持原有的HTTP1.x协议进行数据传输，保证已部署的HTTP1.x业务不受影响。

## 实现描述

UDG<br>解析HTTP1.x升级到HTTP2.0的请求，将请求报文中升级的关键信息进行模糊化处理，使HTTP服务器不感知客户端的协议升级请求，最终保证客户端仍然按照HTTP1.x协议进行业务交互。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

当运营商希望保持已有的HTTP1.x业务不受互联网上HTTP2.0协议升级的影响时，需开启此功能。<br>HTTP1.x业务受互联网上HTTP2.0协议升级影响的场景包括：<br>- 运营商部署的<br>UDG<br>不支持HTTP2.0业务处理；<br>- 运营商部署的<br>UDG<br>支持HTTP2.0业务处理，但是周边网元不具备HTTP2.0处理能力。

## 相关控制项（原文，未解释为边）

SA-Basic

## 对应特性（原文）

GWFD-110202 HTTP2.0协议回落

## 控制的能力

- [GWFD-110202](feature/UDG/20.15.2/GWFD-110202.md)  — 控制项 82209774

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
