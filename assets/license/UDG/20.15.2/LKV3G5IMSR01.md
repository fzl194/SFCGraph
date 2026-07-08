---
id: UDG@20.15.2@License@LKV3G5IMSR01
type: License
name: P-CSCF故障时IMS业务恢复
nf: UDG
version: 20.15.2
license_code: LKV3G5IMSR01
control_item_id: 82200AFH
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# P-CSCF故障时IMS业务恢复

`LKV3G5IMSR01` · 控制项 82200AFH · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

对于IMS（IP Multimedia Subsystem）用户，当其使用的P-CSCF出现故障时需要尽快检测并将新的P-CSCF list返回给UE，UE选择新的P-CSCF重新发起注册，及时避免用户的主被叫业务的丢失

## 实现描述

License中P-CSCF故障时IMS业务恢复功能PDP上下文数大于0时，<br>UDG<br>支持实时监测P-CSCF的连接状态。当发现P-CSCF故障时，会根据配置重新选择P-CSCF并向UE发送更新P-CSCF地址的请求；License中P-CSCF故障时IMS业务恢复功能PDP上下文数为0时，<br>UDG<br>不支持在P-CSCF故障时通知UE更新P-CSCF地址。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

针对IMS用户监测P-CSCF连接状态，当P-CSCF配置变化或发生故障时选择可用的P-CSCF通知UE，减少业务损失。

## 相关控制项（原文，未解释为边）

- 支持IMS接入<br>- PCC基本功能

## 对应特性（原文）

GWFD-020253 P-CSCF故障时IMS业务恢复特性概述

## 控制的能力

- [GWFD-020253](feature/UDG/20.15.2/GWFD-020253.md)  — 控制项 82200AFH

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
