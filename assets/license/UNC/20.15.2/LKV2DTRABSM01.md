---
id: UNC@20.15.2@License@LKV2DTRABSM01
type: License
name: 支持灰度拨测和发布 - USM
nf: UNC
version: 20.15.2
license_code: LKV2DTRABSM01
control_item_id: '81203920'
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN-C
status: active
---

# 支持灰度拨测和发布 - USM

`LKV2DTRABSM01` · 控制项 81203920 ·  · 域 

## 归属/适用NF（原文）

SMF/SGW-C/PGW-C/GGSN-C

## 功能描述

在完成首批次业务Pod升级后，暂停升级过程，引流指定用户的业务到新版本的业务Pod进行新版本的业务状态观测和功能验证，便于提前发现局点升级问题，减少业务影响规模。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

对网元进行在线升级操作时，通过拨测或小批量现网用户迁移到新版本Pod来提前识别和验证现网局点配置是否影响在线升级。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-227102 支持灰度拨测和发布

## 控制的能力

- [WSFD-227102](feature/UNC/20.15.2/WSFD-227102.md)  — 控制项 81203920

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15408046.md`
