---
id: UNC@20.15.2@License@LKV2ARD02
type: License
name: 用户接入控制功能
nf: UNC
version: 20.15.2
license_code: LKV2ARD02
control_item_id: '82206571'
applicable_nf:
- SGSN
- MME
status: active
---

# 用户接入控制功能

`LKV2ARD02` · 控制项 82206571 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

用户接入控制功能是指<br>UNC<br>支持先根据IMSI号段将用户进行分类，再对于每一类用户按照用户属性进行区分而控制用户接入GERAN、UTRAN和E-UTRAN网络。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

- 若运营商希望拒绝某个号段接入GERAN/UTRAN或E-UTRAN系统，则可以启用根据签约ARD控制用户接入特性。<br>- 若运营商希望控制某类用户是否允许接入GERAN/UTRAN或E-UTRAN，但HLR/HSS不支持ARD时，则可以启用根据签约APN控制用户接入特性。<br>- 若运营商已经强制要求对GERAN用户使用SIM卡，UTRAN用户使用USIM卡，并希望对其进行灵活的接入控制，就需要启用按SIM卡/USIM卡控制用户接入特性。<br>- 若运营商对用户使用的APN和SIM卡均不做限制，但不想为CAMEL用户提供服务，则可以启用按Camel签约信息控制用户接入特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106003 用户接入控制功能

## 控制的能力

- [WSFD-106003](feature/UNC/20.15.2/WSFD-106003.md)  — 控制项 82206571

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
