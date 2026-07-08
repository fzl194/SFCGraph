---
id: UNC@20.15.2@License@LKV2PHBL5
type: License
name: LTE和5G网络间切换
nf: UNC
version: 20.15.2
license_code: LKV2PHBL5
control_item_id: '82209697'
applicable_nf:
- MME
status: active
---

# LTE和5G网络间切换

`LKV2PHBL5` · 控制项 82209697 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本特性支持用户在5G网络和EPC网络间的切换，使得用户可以在5G和4G网络之间切换，保持业务连续性。<br>- LTE到5G SA网络的切换5G无线与LTE共存的情况下，UE在LTE网络进行业务，当UE移动到5G无线网络覆盖范围等情况下，eNodeB可能会触发UE切换到5G无线网络，以便为UE提供更好的服务。<br>- 5G SA到LTE网络的切换5G无线与LTE共存的情况下，UE在5G无线网络进行业务，当LTE网络的覆盖（信号）优于5G无线网络时，5G (R)AN会触发UE切换到LTE网络。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

5G用户在LTE网络和5G网络间进行切换时，为了保障业务连续性，需要开通本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104511 LTE与5G SA网络间切换

## 控制的能力

- [WSFD-104511](feature/UNC/20.15.2/WSFD-104511.md)  — 控制项 82209697

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
