---
id: UNC@20.15.2@License@LKV2PCDTO01
type: License
name: 基于动态规则的分流策略控制
nf: UNC
version: 20.15.2
license_code: LKV2PCDTO01
control_item_id: 82200DHA
applicable_nf:
- SMF
status: active
---

# 基于动态规则的分流策略控制

`LKV2PCDTO01` · 控制项 82200DHA ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

为满足企业数据安全（如数据不出园区）或者提升用户其他方面的一些体验（大带宽、低时延等）这个应用服务（如某企业为员工提供手机打卡应用服务）可以针对一个用户或一个用户群定义一些分流策略，当用户进入某个区域范围（TA list）时，AF通过用户数据包头增强或UE访问App时主动携带位置信息感知用户位置变化，当发现用户进入到规定区域范围内，则通过NEF触发网络侧将分流规则和选择辅锚点UPF用的DNAI下发给SMF，SMF基于用户当前位置选择UL CL UPF，基于动态获取的DNAI选择辅锚点UPF，最终在用户会话中插入到UL CL UPF和辅锚点UPF的N4会话，并向UL CL UPF下发动态获取到的分流规则。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

某工业园区域Local Area中部署了智能打卡业务，希望当员工进入Local Area后在使用手机App进行打卡时基于UL CL分流将员工打卡数据信息流通过UL CL分流的方式导入到部署在本地DN侧的智能打卡业务App。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-223004 基于动态规则的分流策略控制

## 控制的能力

- [WSFD-223004](feature/UNC/20.15.2/WSFD-223004.md)  — 控制项 82200DHA

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
