---
id: UNC@20.15.2@License@LKV2VCA01
type: License
name: VoLTE连续性保障
nf: UNC
version: 20.15.2
license_code: LKV2VCA01
control_item_id: '82209698'
applicable_nf:
- MME
status: active
---

# VoLTE连续性保障

`LKV2VCA01` · 控制项 82209698 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本特性禁止5G用户在VoLTE通话过程中进行从LTE网络向5G网络的切换，从而保障VoLTE的通话质量及连续性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当5G用户在VoLTE通话过程中从LTE网络覆盖区移动到LTE和5G网络共覆盖区时需要开启本特性来保证通话的连续性及通话质量。

## 相关控制项（原文，未解释为边）

- LTE和5G网络间重选<br>- LTE和5G网络间切换

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
