---
id: UNC@20.15.2@License@LKV2NUPCSM01
type: License
name: 5G NSA用户策略控制
nf: UNC
version: 20.15.2
license_code: LKV2NUPCSM01
control_item_id: 82200ESP
applicable_nf:
- SMF
status: active
---

# 5G NSA用户策略控制

`LKV2NUPCSM01` · 控制项 82200ESP ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

终端作为NSA用户时，可以通过SET NSARATVALUE命令设置UNC向周边策略网元发送消息中携带RAT信元为NR类型。

## 实现描述

只有获得了License许可后命令设置才能生效。

## 取值范围

0~16000000

## 默认值

10

## 应用场景

NSA用户差异化计费。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
