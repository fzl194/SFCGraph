---
id: UNC@20.15.2@License@LKV2ASNRR02
type: License
name: NRF主备容灾-UAM
nf: UNC
version: 20.15.2
license_code: LKV2ASNRR02
control_item_id: '82209944'
applicable_nf:
- AMF
status: active
---

# NRF主备容灾-UAM

`LKV2ASNRR02` · 控制项 82209944 ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

UNC<br>通过跨DC（Data Center）建立NRF主备组，将主用NRF中的业务数据在备用NRF中进行备份，实现对NRF的主备容灾管理。当主用NRF产生故障时，<br>UNC<br>将自动进行倒换操作，备用NRF将接管原主用NRF业务，保证业务的正常进行且数据不会丢失。原主用NRF故障修复后，<br>UNC<br>支持倒回操作，恢复原主用NRF的主用功能。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

10000～12000000

## 默认值

10

## 应用场景

为了避免硬件故障、DC故障或设备遭遇地震海啸等种种原因对本地NRF的正常服务产生影响，运营商需要开启本特性对本地NRF进行异地容灾。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-114001 NRF主备容灾

## 控制的能力

- [WSFD-114001](feature/UNC/20.15.2/WSFD-114001.md)  — 控制项 82209944

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
