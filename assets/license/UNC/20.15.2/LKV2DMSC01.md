---
id: UNC@20.15.2@License@LKV2DMSC01
type: License
name: 基于SGs和Sv接口的默认MSC选择
nf: UNC
version: 20.15.2
license_code: LKV2DMSC01
control_item_id: '82206559'
applicable_nf:
- MME
status: active
---

# 基于SGs和Sv接口的默认MSC选择

`LKV2DMSC01` · 控制项 82206559 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在基于Sv接口部署SRVCC的场景下，当某些LAC没有在<br>UNC<br>或DNS Server配置对应的FQDN时，会导致MME寻址目标MSC失败，最终导致SRVCC流程失败。此时，<br>UNC<br>将使用LAC=0xFFFF组装FQDN再次尝试DNS域名解析，寻址默认的MSC，提高SRVCC业务的成功率。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

部署SRVCC业务时，LAC配置遗漏或者无法根据LAC解析到目标MSC，造成SRVCC业务失败时，建议启用本特性。<br>部署CSFB业务时，LAI和TAI映射关系配置遗漏，造成CSFB业务失败时，建议启用本特性。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础特性或WSFD-102301 基于CSFB的语音业务

## 对应特性（原文）

WSFD-104405 基于SGs和Sv接口的默认MSC选择

## 控制的能力

- [WSFD-104405](feature/UNC/20.15.2/WSFD-104405.md)  — 控制项 82206559

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
