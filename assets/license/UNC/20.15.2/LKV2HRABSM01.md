---
id: UNC@20.15.2@License@LKV2HRABSM01
type: License
name: 支持灰度升级无损回退 - USM
nf: UNC
version: 20.15.2
license_code: LKV2HRABSM01
control_item_id: '81203921'
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN-C
status: active
---

# 支持灰度升级无损回退 - USM

`LKV2HRABSM01` · 控制项 81203921 ·  · 域 

## 归属/适用NF（原文）

SMF/SGW-C/PGW-C/GGSN-C

## 功能描述

当网元从低版本升级到高版本过程，第二批次业务POD升级前，存在异常导致无法继续升级或用户取消升级时，支持人工触发业务POD从新版本滚动回退到老版本。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

- 在灰度暂停之后点击“继续”操作之前，存在异常导致无法继续升级或用户取消升级时，人工触发业务POD从新版本滚动回退到老版本。<br>- 在灰度拨测、灰度发布阶段，当识别到版本的业务KPI异常时，人工触发业务POD从新版本滚动回退到老版本。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-227103 支持灰度升级无损回退

## 控制的能力

- [WSFD-227103](feature/UNC/20.15.2/WSFD-227103.md)  — 控制项 81203921

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15408046.md`
