---
id: UNC@20.15.2@License@LKV2VONRECSM01
type: License
name: VoNR紧急呼叫-USM
nf: UNC
version: 20.15.2
license_code: LKV2VONRECSM01
control_item_id: 82200FEQ
applicable_nf:
- SMF
status: active
---

# VoNR紧急呼叫-USM

`LKV2VONRECSM01` · 控制项 82200FEQ ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

在无线网络部署VoNR（Voice over NR，NR网络语音业务）的前提下，当UE从5G网络接入时，允许其在IMS域注册，在5GC完成语音业务服务。当UE要进行紧急通话时通过VoNR进行紧急呼叫。紧急呼叫是指当用户拨打紧急呼叫号码（如110、120、119）时，系统识别出该呼叫为紧急呼叫，对呼叫做特殊的处理，并将请求转发到紧急呼叫中心PSAP（Public Safety Answering Point）。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Session

## 默认值

10

## 应用场景

当用户遇到反恐、医疗紧急救助、火警或自然灾害救援等情况的时候，在NR网络覆盖下的UE拨打紧急号码连接到紧急呼叫中心PSAP（Public Safety Answering Point）来获得紧急救助。

## 相关控制项（原文，未解释为边）

依赖WSFD-102701 VoNR基础语音业务

## 对应特性（原文）

WSFD-102706 VoNR紧急呼叫

## 控制的能力

- [WSFD-102706](feature/UNC/20.15.2/WSFD-102706.md)  — 控制项 82200FEQ

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
