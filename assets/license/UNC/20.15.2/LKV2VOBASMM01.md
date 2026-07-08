---
id: UNC@20.15.2@License@LKV2VOBASMM01
type: License
name: 语音解决方案增值包基本功能-UAM
nf: UNC
version: 20.15.2
license_code: LKV2VOBASMM01
control_item_id: 82200EEB
applicable_nf:
- MME
status: active
---

# 语音解决方案增值包基本功能-UAM

`LKV2VOBASMM01` · 控制项 82200EEB ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在系统中控制允许接入的VoLTE+EPS Fallback用户数。

## 实现描述

MME系统中每接入一个VoLTE或EPS Fallback用户，该License总数加1；每分离一个VoLTE用户或ESP Fallback用户，总数减1。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

MME网元中接入VoLTE或EPS Fallback语音用户。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
