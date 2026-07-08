---
id: UNC@20.15.2@License@LKV2AARC01
type: License
name: 基于APN的NB-IoT终端接入速率控制
nf: UNC
version: 20.15.2
license_code: LKV2AARC01
control_item_id: '82207714'
applicable_nf:
- MME
status: active
---

# 基于APN的NB-IoT终端接入速率控制

`LKV2AARC01` · 控制项 82207714 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

IoT（Internet of Things）业务在正常场景下，终端发送的都是低频率数据包，但在终端异常场景（如超时重发等）下，可能在短时间大频率发送数据包，此时可能会导致网络拥塞并影响业务运行，所以3GPP协议引入终端发送数据的速率控制机制。MME接收网关侧的速率控制参数并过PCO/EPCO信元携带给终端，用于控制该终端的某PDN连接单位时间内上行和下行数据包的数目。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

本特性应用于NB-IoT控制面优化（Control Plane Optimization）和用户面优化（User Plane Optimization）数据传输中，用于限制终端的数据传输速率，在终端异常情况下可以防止网络拥塞而影响业务，提升整网的可靠性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215204 基于APN的NB-IoT终端接入速率控制

## 控制的能力

- [WSFD-215204](feature/UNC/20.15.2/WSFD-215204.md)  — 控制项 82207714

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
