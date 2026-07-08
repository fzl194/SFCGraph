---
id: UDG@20.15.2@License@LKV3G5CPPT01
type: License
name: 用户Portal
nf: UDG
version: 20.15.2
license_code: LKV3G5CPPT01
control_item_id: '82209780'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 用户Portal

`LKV3G5CPPT01` · 控制项 82209780 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

用户Portal即个人门户网站，对用户的信息进行管理，包括业务的订购管理、帐户管理、费用管理。网元支持在终端上线后被自动重定向到个人门户网站，然后通过个人门户网站访问各种业务。

## 实现描述

GPRS/UMTS网络中，Captive Portal的业务流程如下所示：<br>- MS发起HTTP业务前，先发起TCP连接建立报文。TCP连接建立报文的目的IP地址为目标服务器的IP地址，目的端口号为80。当TCP连接建立报文到达UDG后，UDG允许其通过，建立起了MS和目标服务器间的TCP连接。<br>- TCP连接建立后，MS发起HTTP业务。当MS发送的HTTP Get或者Post报文到达UDG，UDG会将报文与本地预设的强制网络门户值进行匹配，并进行重定向。<br>- UDG对HTTP报文先进行SA解析，并根据SA解析结果进行L7匹配处理。根据L7匹配的策略进行处理，策略中包括计费属性或actionlist。UDG执行actionlist中的用户Portal处理。<br>- 用户Portal处理会构建HTTP回复报文，并将报文发送到MS。该回复报文用于通知MS此HTTP业务必须重定向到负荷分担模式下选择的Portal Server。HTTP回复报文中的返回码可以在UDG上全局配置，其值可设置为301、302或303。用户报文重定向后，UDG根据captive mode配置启动定时器，进入non-captive模式。在定时器超时前，UDG不进行重定向操作并允许用户正常接入业务。<br>- UDG构造一个TCP断开报文，即TCP RST报文，并将该报文发给MS，通知MS断开目标服务器。<br>- 为了避免半连接，UDG会给目标服务器发送一个TCP RST报文。<br>- MS根据UDG回复的重定向报文中的URL，自动获取DNS，然后自动发起到Portal Server的TCP连接。<br>- MS与Portal Server正常进行HTTP交互。<br>- 在non-captive模式下，MS与Web Server进行正常的HTTP交互。<br>- MS再次访问Web Server，先发起TCP建链。<br>- MS发出URL请求到Web Server。<br>- UDG进行SA解析，按照步骤 3的处理，在执行用户Portal时，发现定时器超时，网元让用户进入captive模式，到Web Server的访问将会再次进行用户Portal处理，即网元按配置时间的间隔进行重定向操作。后续HTTP请求会再次被重定向，用户报文重定向后，UDG再次启动captive mode定时器。<br>EPC网络中，Captive Portal的业务流程如下所示：<br>- UE发起HTTP业务前，先发起TCP连接建立报文。TCP连接建立报文的目的IP地址为目标服务器的IP地址，目的端口号为80。当TCP连接建立报文到达UDG后，UDG允许其通过，建立起了UE和目标服务器间的TCP连接。<br>- TCP连接建立后，UE发起HTTP业务。当UE发送的HTTP Get或者Post报文到达UDG，UDG会将报文与本地预设的强制网络门户值进行匹配，并进行重定向。<br>- UDG对HTTP报文先进行SA解析，并根据SA解析结果进行L7匹配处理。根据L7匹配的策略进行处理，策略中包括计费属性或actionlist。UDG执行actionlist中的用户Portal处理。<br>- 用户Portal处理会构建HTTP回复报文，并将报文发送到UE。该回复报文用于通知UE此HTTP业务必须重定向到负荷分担模式下选择的Portal Server。HTTP回复报文中的返回码可以在UDG上全局配置，其值可设置为301、302或303。用户报文重定向后，UDG根据captive mode配置启动定时器，进入non-captive模式。在定时器超时前，UDG不进行重定向操作并允许用户正常接入业务。<br>- UDG构造一个TCP断开报文，即TCP RST报文，并将该报文发给UE，通知UE断开目标服务器。<br>- 为了避免半连接，UDG会给目标服务器发送一个TCP RST报文。<br>- UE根据UDG回复的重定向报文中的URL，自动获取DNS，然后自动发起到Portal Server的TCP连接。<br>- UE与Portal Server正常进行HTTP交互。<br>- 在non-captive模式下，UE与Web Server进行正常的HTTP交互。<br>- UE再次访问Web Server，先发起TCP建链。<br>- UE发出URL请求到Web Server。<br>- UDG进行SA解析，按照步骤 3的处理，在执行用户Portal时，发现定时器超时，UDG让用户进入captive模式，到Web Server的访问将会再次进行用户Portal处理，即UDG按配置时间的间隔进行重定向操作。后续HTTP请求会再次被重定向，用户报文重定向后，UDG再次启动captive mode定时器。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

用户Portal特性可应用于广告或新闻订阅推送。当用户访问某些网站时，先自动重定向到Portal Server，Portal Server推送广告或订阅新闻给用户进行浏览，后续用户可以正常进行业务访问。<br>当手机访问Web Server，用户在captive模式和non-captive模式之间进行切换，重复这样的交互完成业务访问。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- SA-Web Browsing<br>- SA-Mobile

## 对应特性（原文）

GWFD-110281 用户Portal

## 控制的能力

- [GWFD-110281](feature/UDG/20.15.2/GWFD-110281.md)  — 控制项 82209780

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
