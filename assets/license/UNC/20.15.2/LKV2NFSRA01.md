---
id: UNC@20.15.2@License@LKV2NFSRA01
type: License
name: NF业务可靠性保障
nf: UNC
version: 20.15.2
license_code: LKV2NFSRA01
control_item_id: 82200BAH
applicable_nf:
- SMF
status: active
---

# NF业务可靠性保障

`LKV2NFSRA01` · 控制项 82200BAH ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

NF业务可靠性是指两个或多个PCF组成一个PCF Group，当某个PCF故障时，SMF会为新建会话或已有会话选择状态正常的PCF，恢复业务，提高业务可靠性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

当一个SMF对接多个PCF时，可通过本特性提升PCF故障场景下的业务可靠性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-213002 NF业务可靠性保障

## 控制的能力

- [WSFD-213002](feature/UNC/20.15.2/WSFD-213002.md)  — 控制项 82200BAH

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
