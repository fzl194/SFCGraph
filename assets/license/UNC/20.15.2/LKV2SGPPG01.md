---
id: UNC@20.15.2@License@LKV2SGPPG01
type: License
name: 基于分组的智能寻呼 - UAM
nf: UNC
version: 20.15.2
license_code: LKV2SGPPG01
control_item_id: 82200JAM
applicable_nf:
- AMF
status: active
---

# 基于分组的智能寻呼 - UAM

`LKV2SGPPG01` · 控制项 82200JAM ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

UNC基于终端签约的DNN、切片信息以及终端请求的寻呼概率下发配置的PEIPS分组信息，NG-RAN和终端使用PEIPS分组信息，减少在RRC_IDLE和RRC_INACTIVE状态下寻呼，降低终端功耗。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

对实时性要求较低的M2M终端建议开启基于分组的智能寻呼功能，减少寻呼开销，实现终端节电。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-206010 基于分组的智能寻呼

## 控制的能力

- [WSFD-206010](feature/UNC/20.15.2/WSFD-206010.md)  — 控制项 82200JAM

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848073.md`
