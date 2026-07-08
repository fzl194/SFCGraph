---
id: UNC@20.15.2@License@LKV2VPCU01
type: License
name: 用户群语音策略控制
nf: UNC
version: 20.15.2
license_code: LKV2VPCU01
control_item_id: '82206608'
applicable_nf:
- MME
status: active
---

# 用户群语音策略控制

`LKV2VPCU01` · 控制项 82206608 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

UNC<br>根据终端的漫游属性、是否签约了IMS APN等因素精细化控制是否向终端提供VoLTE基础语音业务，以及在CSFB语音方案和VoLTE语音方案同时可用时的语音业务优选策略。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

以下场景下，请启用本特性：<br>- 运营商需要精细化控制终端用户LTE接入时的语音业务策略，例如：- 因IMS网络的漫游还未开通，不允许外网用户使用VoLTE业务。<br>- 同时部署CSFB和VoLTE语音业务时，如果终端也同时支持这两种语音业务，推荐本网用户优先使用VolTE，VoLTE不可用时才使用CSFB。<br>- 当MME被多个运营商共享的情况下，可以为不同的运营商提供差异化的语音服务。<br>- 运营商部署非GSMA标准要求的IMS域APN，例如，“IMS-X”。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础语音业务

## 对应特性（原文）

WSFD-201002 用户群语音策略控制

## 控制的能力

- [WSFD-201002](feature/UNC/20.15.2/WSFD-201002.md)  — 控制项 82206608

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
