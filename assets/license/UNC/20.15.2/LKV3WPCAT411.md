---
id: UNC@20.15.2@License@LKV3WPCAT411
type: License
name: Category 2/3/4 接入, 150Mbit/s - USM
nf: UNC
version: 20.15.2
license_code: LKV3WPCAT411
control_item_id: '82207994'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# Category 2/3/4 接入, 150Mbit/s - USM

`LKV3WPCAT411` · 控制项 82207994 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

UE Category是LTE终端的接入能力等级，是UE能够支持的一系列无线性能参数的集合。3GPP在协议中给出了各等级UE Category的具体定义。华为<br>UNC<br>支持UE Category 2/3/4相应的接入能力，保证签约的UE Category 2/3/4用户接入网络并使用Category 2/3/4的高速无线宽带业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

当移动运营商开展大流量移动多媒体业务，选择UE Category接入技术，为LTE用户提供高速下行分组业务时，建议开启本特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-101101 Category 2/3/4基础功能

## 对应特性（原文）

WSFD-101201 Category 2/3/4接入，150Mbit/s

## 控制的能力

- [WSFD-101201](feature/UNC/20.15.2/WSFD-101201.md)  — 控制项 82207994

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
