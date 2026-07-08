---
id: UNC@20.15.2@License@LKV2CA26SM02
type: License
name: Category 20~26接入,3.5Gbit/s-USM
nf: UNC
version: 20.15.2
license_code: LKV2CA26SM02
control_item_id: 82200EET
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# Category 20~26接入,3.5Gbit/s-USM

`LKV2CA26SM02` · 控制项 82200EET ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

保证签约的UE Category 20~26用户以下行带宽最大3.5Gbit/s的速率接入网络并使用业务。

## 实现描述

系统License项中支持UE Category 20~26接入基本功能项为允许，并且下行带宽最大为3.5Gbit/s的UE Category 20~26用户激活成功，支持UE Category 20~26接入, 3.5Gbps的用户上下文数加1。下行带宽最大为3.5Gbit/s的UE Category 20~26用户去激活成功，支持UE Category 20~26接入, 3.5Gbps的用户上下文数减1。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

当移动运营商需开展大流量移动多媒体业务时，首选UE Category接入技术，为LTE用户提供高速下行分组业务。

## 相关控制项（原文，未解释为边）

依赖WSFD-101407 Category 20~26 基础功能

## 对应特性（原文）

WSFD-101507 Category 20~26 接入,3.5 Gbit/s

## 控制的能力

- [WSFD-101507](feature/UNC/20.15.2/WSFD-101507.md)  — 控制项 82200EET

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
