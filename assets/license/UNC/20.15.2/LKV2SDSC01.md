---
id: UNC@20.15.2@License@LKV2SDSC01
type: License
name: 基于区域的SMF选择
nf: UNC
version: 20.15.2
license_code: LKV2SDSC01
control_item_id: 82200CAF
applicable_nf:
- AMF
status: active
---

# 基于区域的SMF选择

`LKV2SDSC01` · 控制项 82200CAF ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

PDU会话建立过程中，涉及AMF选择SMF，在SMF的选择过程中，AMF支持选择特定区域（服务范围）的SMF。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

例如大型企业业务会基于同一DNN多区域部署SMF，在企业用户接入进行业务时 ，可以使用本特性实现AMF就近选择服务于此区域（服务范围）的SMF，减少信令时延，提升用户体验。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205010 基于服务区域的SMF选择

## 控制的能力

- [WSFD-205010](feature/UNC/20.15.2/WSFD-205010.md)  — 控制项 82200CAF

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848073.md`
