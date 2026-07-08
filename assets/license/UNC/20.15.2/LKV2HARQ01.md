---
id: UNC@20.15.2@License@LKV2HARQ01
type: License
name: 支持2 HARQ终端 接入
nf: UNC
version: 20.15.2
license_code: LKV2HARQ01
control_item_id: '82208415'
applicable_nf:
- MME
status: active
---

# 支持2 HARQ终端 接入

`LKV2HARQ01` · 控制项 82208415 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本特性支持2 HARQ类型的终端接入。当需要对基于CP-CIoT数据传输方式的终端的上下行速率控制时，MME可通过UE Information Transfer消息将信元UE Radio capability发送给eNodeB，eNodeB将根据该信元判断终端类型，并对其进行上下行速率控制。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

网络中存在支持2HARQ特性的NB-IoT终端，且该类终端所使用的业务需要较大的上下行速率，需要部署此特性。支持2HARQ的终端相比普通NB-IoT终端，支持更高的上下行速率，此场景下部署此特性可以提升上下行数据速率。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215502 支持2 HARQ终端接入

## 控制的能力

- [WSFD-215502](feature/UNC/20.15.2/WSFD-215502.md)  — 控制项 82208415

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
