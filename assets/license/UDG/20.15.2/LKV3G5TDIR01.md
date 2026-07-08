---
id: UDG@20.15.2@License@LKV3G5TDIR01
type: License
name: TCP/UDP传输分析上报
nf: UDG
version: 20.15.2
license_code: LKV3G5TDIR01
control_item_id: 82200CXP
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# TCP/UDP传输分析上报

`LKV3G5TDIR01` · 控制项 82200CXP · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制报表是否上报TCP/UDP传输分析。

## 实现描述

报表是否产生TCP/UDP相关的单据受该License控制。<br>License不开启时，报表不会产生TCP/UDP的单据。从性能角度看，UDG也不会因为报表做相关统计，这些统计项包含：<br>TCP连接、TCP性能、TCP吞吐量分布、UDP 吞吐量分布、TCP 延迟分布、TCP 吞吐量、TCP 延迟、TCP 丢包率、UDP 性能。<br>License开启时，报表会产生TCP/UDP的单据。

## 取值范围

10~8000000

## 默认值

10

## 应用场景

用户使用报表功能时，通过打开TCP/UDP传输分析，来对TCP/UDP传输业务进行信息收集和上报。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111013 TCP/UDP传输分析上报

## 控制的能力

- [GWFD-111304](feature/UDG/20.15.2/GWFD-111304.md)  — 控制项 82200CXP

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
