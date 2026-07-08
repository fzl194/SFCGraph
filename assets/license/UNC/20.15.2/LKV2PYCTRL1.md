---
id: UNC@20.15.2@License@LKV2PYCTRL1
type: License
name: 基于实时位置信息的策略控制功能-USM
nf: UNC
version: 20.15.2
license_code: LKV2PYCTRL1
control_item_id: 82200DAW
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# 基于实时位置信息的策略控制功能-USM

`LKV2PYCTRL1` · 控制项 82200DAW ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C、SMF

## 功能描述

当需要根据用户实时位置进行策略控制时，GGSN/SGW-C/PGW-C/SMF向SGSN/MME/AMF下发位置事件上报请求，SGSN/MME/AMF向RAN侧请求位置上报。当用户位置发生变化时，RAN侧将实时位置信息上报给SGSN/MME/AMF，并经GGSN/SGW-C/PGW-C/SMF传递给PCRF/PCF。PCRF/PCF综合用户位置、使用流量、网络状态等进行策略决策并发起策略更新，GGSN/SGW-C/PGW-C/SMF根据最新的策略触发相应变更流程。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

基于位置上报的实时策略控制可以对指定区域进行实时管控，也可以对用户设定区域，在区域内外可以按照用户、业务类型等方式进行差异化控制，提高热点地区整体用户体验。例如，在热点地区禁止P2P业务，保证HTTP浏览类业务的带宽，以降低小区的拥塞压力；如对家用无线路由器，限制用户的移动范围，当用户移出签约范围后采用不同的策略控制或阻塞其业务。

## 相关控制项（原文，未解释为边）

WSFD-109101 PCC基本功能<br>WSFD-106403 小区位置信息上报功能（S11接口）<br>WSFD-106405 NG-RAN的位置上报

## 对应特性（原文）

WSFD-211002 基于实时位置的策略控制

## 控制的能力

- [WSFD-211002](feature/UNC/20.15.2/WSFD-211002.md)  — 控制项 82200DAW

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
