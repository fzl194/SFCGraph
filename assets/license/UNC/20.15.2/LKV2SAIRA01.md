---
id: UNC@20.15.2@License@LKV2SAIRA01
type: License
name: 5G SA国际漫游接入用户数-UAM
nf: UNC
version: 20.15.2
license_code: LKV2SAIRA01
control_item_id: 82200ECG
applicable_nf:
- AMF
status: active
---

# 5G SA国际漫游接入用户数-UAM

`LKV2SAIRA01` · 控制项 82200ECG ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

国际漫游是指终端用户在归属运营商网络以外的国家或地区使用业务的场景。5G SA组网场景下，用户离开归属PLMN的覆盖范围时，UNC支持用户从拜访地网络接入使用业务，保证业务的连续性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

运营商之间签订漫游协议，期望支持漫游用户漫入以及本网用户漫出时，可以开启本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-224001 支持SA国际漫游接入

## 控制的能力

- [WSFD-224001](feature/UNC/20.15.2/WSFD-224001.md)  — 控制项 82200ECG

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848073.md`
