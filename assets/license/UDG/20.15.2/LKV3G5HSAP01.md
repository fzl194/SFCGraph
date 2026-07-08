---
id: UDG@20.15.2@License@LKV3G5HSAP01
type: License
name: HTTPS 业务地址识别
nf: UDG
version: 20.15.2
license_code: LKV3G5HSAP01
control_item_id: '82209775'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# HTTPS 业务地址识别

`LKV3G5HSAP01` · 控制项 82209775 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

HTTPS业务地址识别是指UDG支持对HTTPS（Hypertext Transfer Protocol over Secure Socket Layer）协议承载的业务进行感知，识别业务内容，对指定的HTTPS业务进行计费与策略控制。

## 实现描述

- HTTPS（Hypertext Transfer Protocol over Secure Socket Layer）是基于SSL的HTTP协议传输，是以安全为目标的HTTP通道，它可以保证用户数据加密传输。目前很多业务通过HTTPS协议进行用户验证和数据传输，例如涉及用户隐私的应用：帐户设置、头像设置、个人资料设置等。由于HTTPS属于加密传输，UDG无法直接通过SA特性识别，可通过解析DNS报文获得的Server IP进行识别，具体描述如下。<br>- 用户访问HTTP业务时，客户端在建立HTTP连接前会发起DNS域名（Domain）解析流程，以获取服务器的IP，然后向该IP发起建链请求。通过解析DNS响应报文，可以获得Domain与Server IP的映射关系。<br>- 利用此原理，UDG在本地通过命令filter预先配置HTTPS业务的域名。用户访问该域名的HTTPS业务时，首先会发起该域名的DNS解析请求，UDG解析DNS响应报文获取域名对应的Server IP，通过此过程自学习域名与Server IP的映射关系。对于后续经过UDG的报文（包括HTTPS加密报文），以Server IP为过滤条件进行匹配，符合过滤条件的报文识别为特定的业务类型。<br>- 实际中，很多业务服务器IP会动态变化，可在UDG上通过命令domain-ip-agetime设置Server IP的老化时间，保证业务域名与Server IP映射关系的定期更新。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

- HTTPS属于加密协议，传统的方法不能识别HTTPS业务类型。UDG支持HTTPS业务的识别，扩大设备业务识别范围，运营商可以对HTTPS业务进行计费与策略控制。<br>- 运营商推出的一些业务套餐包（例如Facebook Zero）中会涉及HTTPS类的业务，例如用户通过HTTPS登录Facebook网站，UDG支持HTTPS业务的识别可以提高业务套餐包的控制精度，提升用户满意度。<br>- UDG不支持使用HTTPS://IP访问方式的HTTPS业务地址识别。由于本特性依赖于DNS域名解析，而通过IP直接访问业务时没有域名解析过程，因此不适用。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- SA-Network Administration

## 对应特性（原文）

GWFD-110203 HTTPS业务地址识别

## 控制的能力

- [GWFD-110203](feature/UDG/20.15.2/GWFD-110203.md)  — 控制项 82209775

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
