---
id: UNC@20.15.2@License@LKV3WPCA1916
type: License
name: Category 19 接入,1.6Gbit/s - USM
nf: UNC
version: 20.15.2
license_code: LKV3WPCA1916
control_item_id: '82209736'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# Category 19 接入,1.6Gbit/s - USM

`LKV3WPCA1916` · 控制项 82209736 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

保证签约的UE Category 19用户以下行带宽最大1.6Gbit/s的速率接入网络并使用业务。

## 实现描述

系统License项中支持UE Category 19接入基本功能项为允许，并且下行带宽最大为1.6Gbit/s的UE Category 19用户激活成功，支持UE Category 19接入, 1.6Gbps的用户上下文数加1。下行带宽最大为1.6Gbit/s的UE Category 19用户去激活成功，支持UE Category 19接入, 1.6Gbps的用户上下文数减1。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

当移动运营商需开展大流量移动多媒体业务时，首选UE Category接入技术，为LTE用户提供高速下行分组业务。

## 相关控制项（原文，未解释为边）

依赖WSFD-101406 Category 19 基础功能

## 对应特性（原文）

WSFD-101506 Category 19 接入,1.6 Gbit/s

## 控制的能力

- [WSFD-101506](feature/UNC/20.15.2/WSFD-101506.md)  — 控制项 82209736

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
