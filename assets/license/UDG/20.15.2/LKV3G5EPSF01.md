---
id: UDG@20.15.2@License@LKV3G5EPSF01
type: License
name: EPS Fallback
nf: UDG
version: 20.15.2
license_code: LKV3G5EPSF01
control_item_id: '82209874'
license_domain: UDG
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# EPS Fallback

`LKV3G5EPSF01` · 控制项 82209874 · resource · 域 UDG

## 归属/适用NF（原文）

UPF

## 功能描述

在不部署VoNR的情况下提供5G网络的语音解决方案。

## 实现描述

在无线网络没有部署VoNR（Voice over NR，NR网络语音业务），当UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行通话时，会回落到4G网络通过VoLTE进行通话。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

运营商在无线网络不部署VoNR的情况下，并且需要提供语音解决方案时。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020282 EPS Fallback

## 控制的能力

- [GWFD-020282](feature/UDG/20.15.2/GWFD-020282.md)  — 控制项 82209874

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
