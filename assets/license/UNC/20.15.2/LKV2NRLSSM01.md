---
id: UNC@20.15.2@License@LKV2NRLSSM01
type: License
name: LTE与5G SA网络重选-USM
nf: UNC
version: 20.15.2
license_code: LKV2NRLSSM01
control_item_id: '82209912'
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# LTE与5G SA网络重选-USM

`LKV2NRLSSM01` · 控制项 82209912 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C、SMF

## 功能描述

- LTE到5G SA网络的重选<br>UE移动出LTE覆盖区进入5G无线的覆盖区域，执行小区重选，发起移动注册更新流程，驻留在5G小区。<br>- 5G SA网络到LTE的重选<br>UE移动出5G无线覆盖区进入LTE的覆盖区域，执行小区重选，发起TAU（跟踪区更新）流程，驻留在LTE小区。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

5G用户在LTE网络和5G网络间进行重选时，为了保障业务连续性，需要开通本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104510 LTE与5G SA网络重选

## 控制的能力

- [WSFD-104510](feature/UNC/20.15.2/WSFD-104510.md)  — 控制项 82209912

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
