---
id: UNC@20.15.2@License@LKV2NOHC01
type: License
name: CDMA与LTE的非优化切换
nf: UNC
version: 20.15.2
license_code: LKV2NOHC01
control_item_id: '82207531'
applicable_nf:
- MME
status: active
---

# CDMA与LTE的非优化切换

`LKV2NOHC01` · 控制项 82207531 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

CDMA与LTE的非优化切换特性是指用户从LTE移动到CDMA网络或者从CDMA网络移动到LTE网络时，业务能平滑切换，保证业务的连续性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

用户在CDMA和LTE两种网络间移动时，对于实时性要求不高的数据业务，如浏览、消息业务、文件下载、流媒体等，CDMA和LTE间非优化切换即可支持该类业务的连续性。<br>应用场景包括：<br>- 用户从LTE网络初始接入，切换到CDMA网络场景。<br>- 用户从CDMA网络初始接入，切换到LTE网络场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104504 CDMA与LTE的非优化切换

## 控制的能力

- [WSFD-104504](feature/UNC/20.15.2/WSFD-104504.md)  — 控制项 82207531

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
