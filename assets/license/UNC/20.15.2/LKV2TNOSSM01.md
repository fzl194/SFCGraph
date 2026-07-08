---
id: UNC@20.15.2@License@LKV2TNOSSM01
type: License
name: 总会话数
nf: UNC
version: 20.15.2
license_code: LKV2TNOSSM01
control_item_id: 82200JFN
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# 总会话数

`LKV2TNOSSM01` · 控制项 82200JFN ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C、SMF

## 功能描述

在系统中控制允许激活的总会话数。

## 实现描述

GGSN-C/SGW-C/PGW-C/SMF系统中每激活一个2G/3G/4G/5G/NSA/NB-IoT会话时，该License总数加1，每激活一个多DNN会话时，该License总数加2。每去激活一个2G/3G/4G/5G/NSA/NB-IoT会话时，总数减1，每去激活一个多DNN会话时，该License总数减2。

## 取值范围

0～16000000 Session

## 默认值

10

## 应用场景

GGSN-C/SGW-C/PGW-C/SMF控制总会话数量。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
