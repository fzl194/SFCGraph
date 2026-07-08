---
id: UNC@20.15.2@License@LKV2DAPDP02
type: License
name: 去激活空闲PDP上下文
nf: UNC
version: 20.15.2
license_code: LKV2DAPDP02
control_item_id: '82206613'
applicable_nf:
- SGSN
status: active
---

# 去激活空闲PDP上下文

`LKV2DAPDP02` · 控制项 82206613 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

去激活空闲<br>PDP上下文<br>是指在一个可控的时间内，如果一个PDP上下文没有任何流量，<br>SGSN<br>将会去激活这个空闲PDP上下文。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 PDP

## 默认值

10

## 应用场景

现网存在大量空闲<br>PDP<br>，使得网络资源利用率低，需要开通去激活空闲PDP上下文。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106206 去激活空闲PDP上下文

## 控制的能力

- [WSFD-106206](feature/UNC/20.15.2/WSFD-106206.md)  — 控制项 82206613

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
