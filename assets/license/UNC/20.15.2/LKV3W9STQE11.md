---
id: UNC@20.15.2@License@LKV3W9STQE11
type: License
name: 业务触发的QOS保证
nf: UNC
version: 20.15.2
license_code: LKV3W9STQE11
control_item_id: '82208819'
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# 业务触发的QOS保证

`LKV3W9STQE11` · 控制项 82208819 ·  · 域 

## 归属/适用NF（原文）

GGSN-C/PGW-C/SMF

## 功能描述

业务触发的QoS保证是指用户请求了需要特定QoS保障的业务时，UNC根据PCF/PCRF下发的PCC规则或本地配置的静态规则为用户建立专有承载的功能。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 PDP

## 默认值

10

## 应用场景

PCC用户L7业务触发创建专有承载。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-109107 业务触发的QOS保证

## 控制的能力

- [WSFD-109107](feature/UNC/20.15.2/WSFD-109107.md)  — 控制项 82208819

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
