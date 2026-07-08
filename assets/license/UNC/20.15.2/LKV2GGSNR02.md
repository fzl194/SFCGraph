---
id: UNC@20.15.2@License@LKV2GGSNR02
type: License
name: 网关路由选择功能
nf: UNC
version: 20.15.2
license_code: LKV2GGSNR02
control_item_id: '82206153'
applicable_nf:
- SGSN
- MME
status: active
---

# 网关路由选择功能

`LKV2GGSNR02` · 控制项 82206153 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

网关路由选择功能是指用户激活PDP上下文或者创建EPS缺省承载时，选择GGSN/PGW-C路由的方法，支持的功能有如下三点：<br>- 支持根据指定的IP地址或Hostname、HSS签约数据或APN域名选择GGSN/PGW-C路由。<br>- 支持根据DNS域名后缀选择特定的DNS服务器，进而解析到特定的GGSN/PGW-C。<br>- 支持多GGSN/PGW-C路由功能，即UNC通过主备方式和负荷分担方式能够选择超过两个的GGSN/PGW-C来提供分组业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在激活PDP上下文和创建EPS缺省承载的流程中，用户需要选择GGSN/PGW-C完成业务流程。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205001 网关路由选择功能

## 控制的能力

- [WSFD-205001](feature/UNC/20.15.2/WSFD-205001.md)  — 控制项 82206153

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
