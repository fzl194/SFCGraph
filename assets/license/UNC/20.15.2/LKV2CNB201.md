---
id: UNC@20.15.2@License@LKV2CNB201
type: License
name: 支持Category NB2 接入 - UAM
nf: UNC
version: 20.15.2
license_code: LKV2CNB201
control_item_id: '82208414'
applicable_nf:
- MME
status: active
---

# 支持Category NB2 接入 - UAM

`LKV2CNB201` · 控制项 82208414 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本特性支持Category NB2类型的终端接入。当需要对基于CP-CIoT数据传输方式的终端的上下行速率控制时，MME可通过UE Information Transfer消息将信元UE Radio capability发送给eNodeB，eNodeB根据该信元判断终端类型，并对其进行上下行速率控制。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

基于CP-CIoT数据传输方式的Category NB2类型终端接入网络时部署此特性。例如如下场景：Category NB2先汇聚了多个真实的终端，作为一个GateWay以NB-IoT技术连接到eNodeB，因此Category NB2要求带宽比较大，此场景下部署此特性可对该终端进行数据传输优化，提升上下行数据速率。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215501 支持Category NB2 接入

## 控制的能力

- [WSFD-215501](feature/UNC/20.15.2/WSFD-215501.md)  — 控制项 82208414

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
