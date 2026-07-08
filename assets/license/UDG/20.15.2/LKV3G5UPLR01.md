---
id: UDG@20.15.2@License@LKV3G5UPLR01
type: License
name: 用户面负载信息上报
nf: UDG
version: 20.15.2
license_code: LKV3G5UPLR01
control_item_id: 82200DEQ
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 用户面负载信息上报

`LKV3G5UPLR01` · 控制项 82200DEQ · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

用户面负载信息上报是指<br>UDG<br>支持上报当前的网元负荷。

## 实现描述

用户负载上报的全量信息内嵌在PFCP请求或者响应消息中，不需要触发额外的信令。<br>License不开启时，不进行用户负载信息上报。<br>License开启时，根据阈值配置进行用户负载信息上报。

## 取值范围

10~16000000

## 默认值

10

## 应用场景

用户进行业务访问，<br>UDG<br>进行用户负载信息上报。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020154 用户面负载信息上报

## 控制的能力

- [GWFD-020154](feature/UDG/20.15.2/GWFD-020154.md)  — 控制项 82200DEQ

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
