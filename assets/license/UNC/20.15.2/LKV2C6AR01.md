---
id: UNC@20.15.2@License@LKV2C6AR01
type: License
name: Category 6 接入, 300Mbit/s - UAM
nf: UNC
version: 20.15.2
license_code: LKV2C6AR01
control_item_id: '82206583'
applicable_nf:
- MME
status: active
---

# Category 6 接入, 300Mbit/s - UAM

`LKV2C6AR01` · 控制项 82206583 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

UE Category是LTE终端的接入能力等级，是UE能够支持的一系列无线性能参数的集合。3GPP在协议中给出了各等级UE Category的具体定义。华为<br>UNC<br>支持UE Category 6相应的接入能力，保证签约的UE Category 6用户接入网络并使用Category 6的高速无线宽带业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当移动运营商开展大流量移动多媒体业务，选择UE Category接入技术，为LTE用户提供高速下行分组业务时，建议开启本特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-101401 Category 6基础功能

## 对应特性（原文）

WSFD-101501 Category 6接入，300Mbit/s

## 控制的能力

- [WSFD-101501](feature/UNC/20.15.2/WSFD-101501.md)  — 控制项 82206583

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
