---
id: UNC@20.15.2@License@LKV2MCR01
type: License
name: MME链式备份
nf: UNC
version: 20.15.2
license_code: LKV2MCR01
control_item_id: '82207526'
applicable_nf:
- MME
status: active
---

# MME链式备份

`LKV2MCR01` · 控制项 82207526 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

部署VoLTE语音业务的网络中，MME Pool的组网场景下，由于系统升级、设备掉电等因素导致MME故障时，Pool内其它的MME可以快速接替故障MME上用户的业务，确保VoLTE语音主叫或被叫快速恢复，实现MME设备容灾功能。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～6500000 SAU

## 默认值

10

## 应用场景

本特性应用于部署了VoLTE语音业务的MME Pool网络，以提升VoLTE语音业务可靠性。<br>如果只购买“MME链式备份”的License，未购买“本地VLR”的License，“MME链式备份”特性只对VoLTE用户生效；如果同时购买“MME链式备份”和“本地VLR”的License，“MME链式备份”特性对4G用户生效。是否已购买“MME链式备份”、“本地VLR”的License，请执行<br>**DSP LICENSE**<br>命令查看，生效的资源总数请执行<br>**DSP LICRES**<br>命令查看。

## 相关控制项（原文，未解释为边）

依赖WSFD-110004 MME Pool

## 对应特性（原文）

WSFD-201201 MME链式备份

## 控制的能力

- [WSFD-201201](feature/UNC/20.15.2/WSFD-201201.md)  — 控制项 82207526

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
