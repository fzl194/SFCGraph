---
id: UNC@20.15.2@License@LKV2QCIE02
type: License
name: 基于用户等级的QCI扩展
nf: UNC
version: 20.15.2
license_code: LKV2QCIE02
control_item_id: '82206579'
applicable_nf:
- MME
status: active
---

# 基于用户等级的QCI扩展

`LKV2QCIE02` · 控制项 82206579 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

支持QoS的网络能够识别每种应用所对应的数据包，采用QCI对其进行分类，以提供更好的服务。没有分类，网络则无法确定对特殊数据包进行何种处理。QCI扩展起分类作用。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当网络侧下发扩展QCI，而手机终端只支持标准的QCI时，MME为了处理该情况进行扩展QCI向标准QCI的转换。与其他MME、SGW、ENB交互时，将扩展QCI透传。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-105103 基于用户等级的QCI扩展

## 控制的能力

- [WSFD-105103](feature/UNC/20.15.2/WSFD-105103.md)  — 控制项 82206579

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
