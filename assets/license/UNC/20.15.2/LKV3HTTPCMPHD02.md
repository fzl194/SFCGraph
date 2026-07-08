---
id: UNC@20.15.2@License@LKV3HTTPCMPHD02
type: License
name: 支持HTTP头压缩字典-USM
nf: UNC
version: 20.15.2
license_code: LKV3HTTPCMPHD02
control_item_id: 82200CQR
applicable_nf:
- SMF
status: active
---

# 支持HTTP头压缩字典-USM

`LKV3HTTPCMPHD02` · 控制项 82200CQR ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

HTTP请求和响应消息都是由状态行、请求/响应头部、消息主体三部分组成的。 一般而言，消息主体都会经过gzip压缩，或者本身传输的就是压缩过后的二进制文件（如图片、音频等），但是状态行和头部多是没有经过任何压缩，而是直接以纯文本的方式进行传输的。<br>随着请求数量越来越多，头部的流量也越来越多，并且在建立初次链接之后的链接也要发送user-agent等信息，非常浪费。因此，HTTP2.0提出了对请求和响应的头部进行压缩，这种压缩方式就是HAPCK。通过压缩，头部大小可以减少很多。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

希望在HTTP<br>动态<br>头压缩<br>字典<br>更新时，UNC定时且主动上报HTTP<br>动态<br>头压缩<br>字典<br>，可开通此特性。

## 相关控制项（原文，未解释为边）

WSFD-202001 CHR功能-USM

## 对应特性（原文）

WSFD-202002 支持HTTP头压缩字典

## 控制的能力

- [WSFD-202002](feature/UNC/20.15.2/WSFD-202002.md)  — 控制项 82200CQR

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
