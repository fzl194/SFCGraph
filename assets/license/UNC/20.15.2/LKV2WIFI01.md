---
id: UNC@20.15.2@License@LKV2WIFI01
type: License
name: LTE和WiFi 网络之间的切换
nf: UNC
version: 20.15.2
license_code: LKV2WIFI01
control_item_id: '82206567'
applicable_nf:
- MME
status: active
---

# LTE和WiFi 网络之间的切换

`LKV2WIFI01` · 控制项 82206567 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

LTE和WiFi（Wireless Fidelity） 网络之间的切换特性是指用户从LTE网络移动到WiFi网络或者从WiFi网络移动到LTE网络时，业务能平滑切换，保证业务的连续性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

用户在WiFi和LTE两种网络间移动时，可支持例如VoWIFI语音等业务的连续性和紧急呼叫的连续性。<br>应用场景包括：<br>- 用户从LTE网络初始接入，切换到WiFi网络场景。<br>- 用户从WiFi网络初始接入，切换到LTE网络场景。<br>- 用户从WiFi网络初始接入，在紧急呼叫下切换到LTE网络场景。<br>- 用户从LTE网络初始接入，在紧急呼叫下切换到WiFi网络场景。<br>- UE从GSM/UMTS网络切换到LTE网络后再切换到WiFi场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104505 LTE和WiFi 网络之间的切换

## 控制的能力

- [WSFD-104505](feature/UNC/20.15.2/WSFD-104505.md)  — 控制项 82206567

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
