---
id: UNC@20.15.2@License@LKV2SPCB02
type: License
name: Smartphone控制基础功能
nf: UNC
version: 20.15.2
license_code: LKV2SPCB02
control_item_id: '82207536'
applicable_nf:
- SGSN
status: active
---

# Smartphone控制基础功能

`LKV2SPCB02` · 控制项 82207536 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

Smartphone控制基础功能包括基于信令行为控制、基于终端类型控制和SmartPaging三个部分：<br>- 基于信令行为的Smartphone控制功能通过分析信令识别Smartphone，系统利用禁止使用Direct Tunnel和禁止启用去激活空闲PDP功能的机制来节省信令资源。<br>- 基于终端类型的Smartphone控制功能通过识别Smartphone终端类型，系统针对不同的智能终端实行差异化策略，利用禁止某一类智能终端使用Direct Tunnel功能的机制来节省信令资源。<br>- SmartPaging功能SGSN解析下行消息中的DSCP(Differentiated Services Code Point)字段，并根据下行数据包的优先级以及设备本身的拥塞情况决定是否下发Paging消息，根据实际情况丢弃低优先级的下行包，确保高优先级的业务正常处理。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在UTRAN网络中，Smartphone的应用使网络信令日益增加，利用Smartphone控制基础功能可以避免网络拥塞和设备过载现象的发生。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-206005 Smartphone控制基础功能

## 控制的能力

- [WSFD-206005](feature/UNC/20.15.2/WSFD-206005.md)  — 控制项 82207536

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248038.md`
