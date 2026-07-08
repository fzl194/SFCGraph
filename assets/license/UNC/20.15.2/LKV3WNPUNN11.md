---
id: UNC@20.15.2@License@LKV3WNPUNN11
type: License
name: PCRF免升级
nf: UNC
version: 20.15.2
license_code: LKV3WNPUNN11
control_item_id: '81203082'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# PCRF免升级

`LKV3WNPUNN11` · 控制项 81203082 ·  · 域 

## 归属/适用NF（原文）

SGW-C/PGW-C

## 功能描述

在部署NB-IoT业务时，现有的PCRF设备可能由于未升级无法识别NB-IoT接入类型而拒绝NB-IoT用户接入。为了解决该问题，本特性实现了PCRF免升级即可支持NB-IoT用户接入，节省了PCRF设备升级的开销。

## 实现描述

LICENSE项中PCRF免升级功能项为允许时，PCRF免升级功能生效，否则不生效。

## 取值范围

0～1 UNC

## 默认值

1

## 应用场景

在部署NB-IoT业务时，如果现有的PCRF设备不支持NB-IoT用户接入，需要开启该特性。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-215302 PCRF免升级

## 控制的能力

- [WSFD-215302](feature/UNC/20.15.2/WSFD-215302.md)  — 控制项 81203082

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848081.md`
