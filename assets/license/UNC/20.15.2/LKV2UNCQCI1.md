---
id: UNC@20.15.2@License@LKV2UNCQCI1
type: License
name: QCI 扩展
nf: UNC
version: 20.15.2
license_code: LKV2UNCQCI1
control_item_id: 82200DBA
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# QCI 扩展

`LKV2UNCQCI1` · 控制项 82200DBA ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C、SMF

## 功能描述

QCI（QoS Class Identifier）为QoS分类识别码，用于表示资源分配、分组调度的优先级，每个QCI代表了不同业务的QoS指标，例如资源类型、优先级、时延、分组丢失率等。QCI在各个网元中传递，避免协商和传递大量具体的QoS 参数。QCI包括“标准QCI”和“扩展QCI”两大类，3GPP规范定义了标准QCI以及对应QoS指标和业务类型。<br>UNC支持QCI 扩展功能，运营商可以自定义多个扩展QCI，对不同的用户或者业务类别设置不同的扩展QCI，以提供面向用户和业务的差异化服务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

基于业务的差异化控制<br>业务差分是指不同业务类型之间的QoS差别，比如流媒体业务和普通浏览业务的差异，主要体现在时延、丢包率、带宽及资源分配性质（GBR、non-GBR）等。不同类型的业务对时延、丢包、带宽及资源分配等有不同的需求。<br>例如，支付类业务在标准QCI中未定义，运营商可以规划扩展QCI 128用于支付类业务。

## 相关控制项（原文，未解释为边）

WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）<br>WSFD-102602 LTE一键通（适用于PGW-C/SGW-C）<br>WSFD-105103 基于用户等级的QCI扩展

## 对应特性（原文）

WSFD-109204 QCI 扩展

## 控制的能力

- [WSFD-109204](feature/UNC/20.15.2/WSFD-109204.md)  — 控制项 82200DBA

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
