---
id: UNC@20.15.2@License@LKV2DNAS01
type: License
name: 基于信令面的数据传输
nf: UNC
version: 20.15.2
license_code: LKV2DNAS01
control_item_id: '82207029'
applicable_nf:
- MME
status: active
---

# 基于信令面的数据传输

`LKV2DNAS01` · 控制项 82207029 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

IoT终端数据收发频率低、数据包较小且多数情况为单向发送（例如智能抄表）。本特性是3GPP协议针对此类业务定义的控制面优化功能CP-CIoT（Control Plane Cellular Internet of Thing），实现了数据包在终端和MME之间通过NAS消息传递，在MME和SGW-C间通过S11-U口传递，上、下行数传过程中无需频繁建立E-RAB，从而提升数传效率，节省不必要的信令开销。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

IoT海量连接的趋势和IoT终端节能省电是运营商发展IoT业务过程总面临的两大问题。海量连接会增加网络信令开销，能否提升终端节能省电直接影响运营商的业务竞争力。<br>本特性实现了通过NAS信令携带业务数据包，避免RAN侧反复建立、释放E-RAB，实现节省信令开销。同时由于与网络交互的消息数减少，终端功耗也得以降低，从而延长了电池使用寿命。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215101 基于信令面的数据传输

## 控制的能力

- [WSFD-215101](feature/UNC/20.15.2/WSFD-215101.md)  — 控制项 82207029

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
