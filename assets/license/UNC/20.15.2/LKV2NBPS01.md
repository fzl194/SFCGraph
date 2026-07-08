---
id: UNC@20.15.2@License@LKV2NBPS01
type: License
name: NB-IoT平台软件
nf: UNC
version: 20.15.2
license_code: LKV2NBPS01
control_item_id: '81202652'
applicable_nf:
- MME
status: active
---

# NB-IoT平台软件

`LKV2NBPS01` · 控制项 81202652 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在系统中控制是否允许接NB-IoT用户接入。

## 实现描述

当NB-IoT用户尝试接入系统时，如果系统未购买“NB-IoT平台软件”，NB-IoT用户将无法接入到系统。

## 取值范围

0～1 UNC

## 默认值

1

## 应用场景

MME网元中NB-IoT用户接入。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 控制的能力

- [WSFD-011601](feature/UNC/20.15.2/WSFD-011601.md)  — 控制项 81202652

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63767913.md`
