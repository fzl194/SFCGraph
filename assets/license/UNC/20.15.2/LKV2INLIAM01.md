---
id: UNC@20.15.2@License@LKV2INLIAM01
type: License
name: 逻辑接口支持IPV6-UAM
nf: UNC
version: 20.15.2
license_code: LKV2INLIAM01
control_item_id: '81203246'
applicable_nf:
- AMF
status: active
---

# 逻辑接口支持IPV6-UAM

`LKV2INLIAM01` · 控制项 81203246 ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

UNC<br>的逻辑接口支持基于IPv6（Internet Protocol Version 6）技术的组网，即当周边网元支持IPv6时，<br>UNC<br>连接周边网元的逻辑接口的IP地址都可以配置为IPv6地址。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

UNC<br>与周边网元实现业务交互时需要基于IPv6技术组网，逻辑接口的IP地址可以配置为IPv6地址。基于如下场景时，可使用本特性：<br>- 网元间逻辑接口采用IPv6组网。<br>- 解决IPv4地址枯竭问题。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104412 逻辑接口支持IPv6

## 控制的能力

- [WSFD-104412](feature/UNC/20.15.2/WSFD-104412.md)  — 控制项 81203246

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568026.md`
