---
id: UDG@20.15.2@License@LKV3G5DNSO01
type: License
name: DNS纠错
nf: UDG
version: 20.15.2
license_code: LKV3G5DNSO01
control_item_id: '82209782'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# DNS纠错

`LKV3G5DNSO01` · 控制项 82209782 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

用户通过浏览器上网时，DNS服务器解析该用户访问的域名，并通过DNS应答消息将用户浏览器请求的域名对应的IP地址返回给用户浏览器，用户浏览器根据IP地址通过发送HTTP报文来访问网站服务器。<br>如果用户在上网浏览时输入错误的域名，使DNS服务器无法解析该域名获得对应的IP地址，DNS服务器会向用户返回DNS域名查询失败的应答消息，用户浏览器根据应答消息显示出错页面，从而影响用户的业务体验。<br>为解决上述问题，<br>UDG<br>引入DNS纠错功能。<br>UDG<br>截获DNS服务器返回的失败应答消息，并根据预先制定的策略构造一个新的DNS应答报文给用户，报文中域名对应的地址设置为第三方Platform（如搜索引擎）的IP地址，引导用户访问第三方Platform，由第三方Platform向用户提供指导和帮助，提升用户的上网体验。

## 实现描述

DNS纠错的业务交互过程如下：<br>终端浏览网页，发起DNS查询请求，例如访问域名www.example.com。<br>DNS服务器解析该域名，发现查询不到该域名，则返回查询失败给<br>UDG<br>。<br>UDG<br>判断DNS查询失败，则根据DNS返回的错误信息构造一个新的DNS查询成功响应消息给终端，该响应消息中域名对应的地址设置为第三方Platform的IP地址。<br>终端发起HTTP请求到第三方Platform，HTTP请求报文的目的IP是第三方Platform，URL是www.example.com，第三方Platform返回HTTP响应给终端。<br>DNS纠错规则匹配过程：<br>对于使用本地策略的非PCC用户或使用预定义策略的PCC用户访问Internet时，<br>UDG<br>对DNS报文进行rule匹配，判断是否对该DNS报文进行DNS纠错。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

用户输入错误域名时进行DNS纠错。如终端用户访问internet时输入错误的域名，DNS解析该域名并返回解析失败响应报文，<br>UDG<br>检测到该响应报文为域名出错报文，则根据预先制定的策略构造新的DNS应答报文，将报文中域名对应的地址设置为第三方Platform（如搜索引擎）的IP地址，引导用户访问第三方Platform，从而协助用户继续访问业务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110283 DNS纠错

## 控制的能力

- [GWFD-110283](feature/UDG/20.15.2/GWFD-110283.md)  — 控制项 82209782

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
