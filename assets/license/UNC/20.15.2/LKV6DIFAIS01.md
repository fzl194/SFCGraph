---
id: UNC@20.15.2@License@LKV6DIFAIS01
type: License
name: 磁盘故障隔离
nf: UNC
version: 20.15.2
license_code: LKV6DIFAIS01
control_item_id: '81202579'
applicable_nf:
- SGSN
- MME
- GGSN-C
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- SMSF
status: active
---

# 磁盘故障隔离

`LKV6DIFAIS01` · 控制项 81202579 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME/GGSN-C/SGW-C/PGW-C/AMF/SMF/NRF/NSSF/SMSF

## 功能描述

磁盘故障隔离（存储Bypass）是指将业务节点和存储设备进行解耦，当存储设备故障不可用后，业务节点运行不受影响，业务不受影响，提供受限运维功能，提升NF可靠性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1 UNC

## 默认值

1

## 应用场景

存储设备通过网络和计算节点连接，其中导致存储设备整体故障的因素很多，包括供电中断、网络中断、网络拥塞丢包等，都会导致存储异常。对于5G Core网元，大部分业务都对存储依赖很低，存储设备故障如果保证业务不受损，可以大大提升产品竞争力。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-209002 磁盘故障隔离

## 控制的能力

- [WSFD-209002](feature/UNC/20.15.2/WSFD-209002.md)  — 控制项 81202579

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088190.md`
