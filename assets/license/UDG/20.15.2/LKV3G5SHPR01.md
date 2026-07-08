---
id: UDG@20.15.2@License@LKV3G5SHPR01
type: License
name: HTTP智能重定向
nf: UDG
version: 20.15.2
license_code: LKV3G5SHPR01
control_item_id: '82209783'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# HTTP智能重定向

`LKV3G5SHPR01` · 控制项 82209783 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

HTTP智能重定向功能是<br>UDG<br>通过修改HTTP响应报文，将匹配到HTTP智能重定向规则的访问重定向到第三方PlatForm。

## 实现描述

MS/UE发起HTTP Get Request，消息携带初始访问的URL。<br>UDG<br>进行七层解析和规则匹配，如果业务流为HTTP协议，方法为GET，并且匹配上<br>UDG<br>配置的HTTP智能重定向规则中的URL，则<br>UDG<br>缓存MS/UE的初始请求URL。<br>UDG<br>向HTTP服务器转发MS/UE的HTTP请求。<br>由于MS/UE的初始请求URL填写不正确或不存在等原因，HTTP服务器给<br>UDG<br>返回失败响应消息，消息携带error code（错误码）和content type。<br>UDG<br>对HTTP响应报文中进行解析，并对响应报文中的错误码进行判断。<br>如果HTTP响应报文中携带的错误码、content type、URL、user-agent以及url-postfix等与<br>UDG<br>配置匹配，则<br>UDG<br>构造重定向报文，报文包括：第三方PlatForm URL，并根据配置决定是否携带请求的初始请求URL、MSISDN、IMEI、IMSI和用户IP。<br>UDG<br>送HTTP Response给MS/UE<br>MS/UE发起HTTP Get Request，消息携带第三方PlatForm URL、初始请求URL、MSISDN、IMEI、IMSI和用户IP。<br>UDG<br>向第三方PlatForm转发MS/UE的HTTP请求。<br>第三方PlatForm返回成功响应。用户可以正常访问第三方PlatForm。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

用户请求的初始URL不正确时，应用HTTP智能重定向。<br>用户请求的初始URL不正确，通过HTTP智能重定向功能，<br>UDG<br>将用户重定向到正确的URL或者第三方PlatForm。<br>对特定URL进行过滤时，应用HTTP智能重定向。<br>配置URL过滤，通过HTTP智能重定向功能，<br>UDG<br>将用户重定向到第三方PlatForm。<br>对特定HTTP访问内容的类型进行过滤时，应用HTTP智能重定向。<br>配置特定HTTP访问内容的类型(content-type)过滤条件，通过HTTP智能重定向功能，<br>UDG<br>将用户重定向到第三方PlatForm。<br>对URL后缀（扩展名）页面类型进行过滤时，应用HTTP智能重定向。<br>配置URL后缀名（扩展名）的页面类型(url-postfix)过滤条件，通过HTTP智能重定向功能，<br>UDG<br>将用户重定向到第三方PlatForm。<br>对终端使用的浏览器类型进行过滤时，应用HTTP智能重定向。<br>配置终端使用的浏览器类型(user agent)过滤条件，通过HTTP智能重定向功能，<br>UDG<br>将用户重定向到第三方PlatForm。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110284 HTTP智能重定向

## 控制的能力

- [GWFD-110284](feature/UDG/20.15.2/GWFD-110284.md)  — 控制项 82209783

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
