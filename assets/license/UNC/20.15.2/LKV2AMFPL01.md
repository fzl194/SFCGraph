---
id: UNC@20.15.2@License@LKV2AMFPL01
type: License
name: AMF Pool
nf: UNC
version: 20.15.2
license_code: LKV2AMFPL01
control_item_id: '82209910'
applicable_nf:
- AMF
status: active
---

# AMF Pool

`LKV2AMFPL01` · 控制项 82209910 ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

AMF Pool是指多个AMF同时为相同的无线区域服务，Pool内的AMF与相应区域内所有gNodeB连接。Pool内AMF之间实现资源共享、业务负荷分担。gNodeB探测AMF的设备状态（是否可用）并获取AMF的负荷权重，根据设备状态及负荷权重来及时调整Pool的负荷均衡策略。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

10000～12000000 SAU

## 默认值

10

## 应用场景

当组网中存在多DC部署AMF时，为了实现负荷分担和容灾，减少区域中AMF间频繁的位置更新和切换，可以采用AMF Pool组网。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-104301 AMF Pool

## 控制的能力

- [WSFD-104301](feature/UNC/20.15.2/WSFD-104301.md)  — 控制项 82209910

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248054.md`
