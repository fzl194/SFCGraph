---
id: UNC@20.15.2@License@LKV2CA26SM01
type: License
name: Category 20~26基础功能-USM
nf: UNC
version: 20.15.2
license_code: LKV2CA26SM01
control_item_id: '81203646'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# Category 20~26基础功能-USM

`LKV2CA26SM01` · 控制项 81203646 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

网关通过该license控制是否支持UE Category 20~26 接入基本功能。

## 实现描述

网关通过该license控制是否支持UE Category 20~26 接入基本功能。该License项为功能项， License中支持UE Category 20~26 接入基本功能开启时，网关可以保证签约的UE Category 20~26用户接入网络并使用业务。

## 取值范围

0～1 UNC

## 默认值

1

## 应用场景

当移动运营商需开展大流量移动多媒体业务时，首选UE Category接入技术，为LTE用户提供高速下行分组业务。

## 相关控制项（原文，未解释为边）

依赖WSFD-101406 Category 19 基础功能

## 对应特性（原文）

WSFD-101407 Category 20~26 基础功能

## 控制的能力

- [WSFD-101407](feature/UNC/20.15.2/WSFD-101407.md)  — 控制项 81203646

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568018.md`
