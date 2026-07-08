---
id: UDG@20.15.2@License@LKV3G5HTSE01
type: License
name: HTTPS头增强
nf: UDG
version: 20.15.2
license_code: LKV3G5HTSE01
control_item_id: '82209779'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# HTTPS头增强

`LKV3G5HTSE01` · 控制项 82209779 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

HTTPS头增强指对HTTPS报文头的内容做增强处理，将用户信息MS IP Address、IMSI、MSISDN、User Defined Value中的一个或多个信息添加到HTTPS报文头并传递给Web Server，运营商和服务提供商可基于这些信息灵活开展业务和实施控制，例如业务认证、广告宣传、业务推广和账户管理与查询。

## 实现描述

UDG<br>对报文进行协议识别和解析处理后，根据报文特征信息进行七层规则匹配，之后根据匹配结果执行策略。当判断出该报文匹配到了HTTPS头增强动作，则在该报文头中插入用户的相关信息，然后发送给Web Server。Web Server接收到报文后获取当前用户的信息，之后根据用户信息进行业务处理。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

Web Server在网络通信过程中，在未开启HTTPS头增强特性情况下，无法感知用户信息，导致运营商无法对用户业务进行精细化控制。在网元上开启HTTPS头增强特性后，用户信息，例如MS IP Address、IMSI、MSISDN、User Defined Value，就可以添加到HTTPS报文头中发送给Web Server，从而满足了运营商根据特定用户进行业务访问认证的需求。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- SA-Web Browsing<br>- SA-Mobile

## 对应特性（原文）

GWFD-110263 HTTPS头增强

## 控制的能力

- [GWFD-110263](feature/UDG/20.15.2/GWFD-110263.md)  — 控制项 82209779

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
