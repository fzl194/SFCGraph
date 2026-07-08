---
id: UNC@20.15.2@License@LKV2IMSIPP01
type: License
name: IMSI隐私保护
nf: UNC
version: 20.15.2
license_code: LKV2IMSIPP01
control_item_id: '82209909'
applicable_nf:
- AMF
status: active
---

# IMSI隐私保护

`LKV2IMSIPP01` · 控制项 82209909 ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

5G网络中，SUPI（Subscription Permanent Identifier）是UE的永久身份标识，包含IMSI或者NAI（Network Access Identifier）。UE通过归属网络的公共密钥加密SUPI生成SUCI（Subscription Concealed Identifier），从而实现IMSI隐私保护。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

10000～12000000 SAU

## 默认值

10

## 应用场景

- 当UE进行初始注册时，在初始注册请求消息中携带SUCI。<br>- 当UE收到AMF发送的身份识别请求时，在身份响应消息中携带SUCI。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-103007 IMSI隐私保护

## 控制的能力

- [WSFD-103007](feature/UNC/20.15.2/WSFD-103007.md)  — 控制项 82209909

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
