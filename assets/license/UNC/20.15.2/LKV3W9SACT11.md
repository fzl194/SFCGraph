---
id: UNC@20.15.2@License@LKV3W9SACT11
type: License
name: 支持用户发起的二次激活
nf: UNC
version: 20.15.2
license_code: LKV3W9SACT11
control_item_id: '82208356'
applicable_nf:
- GGSN-C
status: active
---

# 支持用户发起的二次激活

`LKV3W9SACT11` · 控制项 82208356 ·  · 域 

## 归属/适用NF（原文）

GGSN-C

## 功能描述

二次PDP上下文就是使用相同APN和IP地址的PDP上下文。GGSN支持用户发起的二次PDP上下文激活。二次激活的PDP上下文与一次PDP上下文的不同在于采用了不同的QoS。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

在用户已经激活了至少一个PDP上下文的基础上，再次发起二次PDP上下文激活请求消息给GGSN。 例如，从已经打开的网页中下载视频。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205104 支持用户发起的二次激活

## 控制的能力

- [WSFD-205104](feature/UNC/20.15.2/WSFD-205104.md)  — 控制项 82208356

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
