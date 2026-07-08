---
id: UNC@20.15.2@License@LKV3WNBSL211
type: License
name: NB-IoT连接基本软件第二档 - USM
nf: UNC
version: 20.15.2
license_code: LKV3WNBSL211
control_item_id: '82209434'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# NB-IoT连接基本软件第二档 - USM

`LKV3WNBSL211` · 控制项 82209434 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

在系统中控制允许接入的NB-IoT用户数及每日可以为用户提供的服务次数。

## 实现描述

NB-IoT用户通过Attach、Service Request业务流程接入时，NB-IoT用户发送频率次数加一。发送频率次数为49到144次的NB-IoT用户属于第二档用户。NB-IoT用户发送频率次数在每日凌晨从零开始重新计算。<br>如果NB-IoT第二档用户在一天内的发送频率次数达144且更高档license已经用尽，则该NB-IoT用户的后续Service Request业务流程将会失败。<br>当系统中NB-IoT的PDP上下文数达到所有NB-IoT发送频率基本软件license数之和后就不允许NB-IoT用户接入。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

支持NB-IoT终端用户接入。

## 相关控制项（原文，未解释为边）

NB-IoT平台软件

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63848061.md`
