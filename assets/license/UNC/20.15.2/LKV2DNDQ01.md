---
id: UNC@20.15.2@License@LKV2DNDQ01
type: License
name: 基于信令面数据传输的Qos差异化控制
nf: UNC
version: 20.15.2
license_code: LKV2DNDQ01
control_item_id: '82208416'
applicable_nf:
- MME
status: active
---

# 基于信令面数据传输的Qos差异化控制

`LKV2DNDQ01` · 控制项 82208416 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

NB-IoT终端采用信令面方式（CP-CIoT）进行数据传输时，由于eNodeB上没有建立RAB承载，eNodeB上无法获得终端的QoS信息，也就不能对终端进行差异化控制。本特性中eNodeB可向MME发送Retrieve UE information消息请求UE的QoS信息，MME收到消息后，在UE Information Transfer消息中将终端的QoS信息发送给eNodeB，便于eNodeB根据QoS信息决定NB-IoT终端信令调度的优先级。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

随着NB-IoT终端市场的发展和竞争环境的变化，对于基于CP-CIoT数据传输方式的终端，运营商需要在运营策略上对终端进行细分，为不同需求的NB-IoT终端提供不同等级的服务，通过部署此特性实现对终端用户的差异化服务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215105 基于信令面数据传输的Qos差异化控制

## 控制的能力

- [WSFD-215105](feature/UNC/20.15.2/WSFD-215105.md)  — 控制项 82208416

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
