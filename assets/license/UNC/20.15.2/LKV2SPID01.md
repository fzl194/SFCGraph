---
id: UNC@20.15.2@License@LKV2SPID01
type: License
name: 基于SPID的UE驻留和切换策略管理
nf: UNC
version: 20.15.2
license_code: LKV2SPID01
control_item_id: '82207381'
applicable_nf:
- SGSN
- MME
status: active
---

# 基于SPID的UE驻留和切换策略管理

`LKV2SPID01` · 控制项 82207381 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

3GPP协议中定义了SPID（Subscriber Profile ID for RAT/Frequency Selection Priority），它定义了一组频段及其优先级。这个信元可以由用户签约信息指定，也可以由<br>UNC<br>指定，传递到无线侧之后，可以用于灵活控制终端的行为策略，例如指定终端驻留和切换频段的优先级等。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

GUL（GSM/UMTS/LTE）多模终端，使用绝对优先级进行小区重选，会优选LTE接入，其次是GSM/UMTS网络。用户根据绝对优先级先尝试接入LTE网络，如用户未签约LTE业务，被核心网拒绝后，会再次通过UMTS接入，但是由于此类终端每次都会先尝试LTE再尝试GSM/UMTS网络，导致耗电量比其他用户耗电量高。运营商希望控制此类终端接入的网络类型以解决耗电量高的问题。<br>LTE部署初期不支持语音，语音为主的用户只能回落到UMTS网络进行语音业务，但是通过UMTS网络进行语音，接入时延增加1～2秒。运营商希望针对此类以语音业务为主的GUL多模终端，优先驻留在GU网络以解决接入时延的问题。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106207 基于SPID的UE驻留和切换策略管理

## 控制的能力

- [WSFD-106207](feature/UNC/20.15.2/WSFD-106207.md)  — 控制项 82207381

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
