---
id: UNC@20.15.2@License@LKV2RINCOR02
type: License
name: 请求信息纠正功能
nf: UNC
version: 20.15.2
license_code: LKV2RINCOR02
control_item_id: '82205928'
applicable_nf:
- SGSN
- MME
status: active
---

# 请求信息纠正功能

`LKV2RINCOR02` · 控制项 82205928 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

在激活PDP上下文/PDN连接的过程中，<br>UNC<br>会检查用户请求的APN、PDP/PDN类型和PDP/PDN地址三元组与HLR/HSS中签约的三元组是否一致，如果两者不一致，则拒绝用户的激活请求。这种不一致通常是用户对手机参数设置或签约数据重复等错误引起的，所以，<br>UNC<br>提供了请求信息纠正的功能，减少由于手机参数设置或签约数据重复等错误造成的激活失败。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

如果某地区的PDP上下文/PDN连接激活成功率低，建议开启请求信息纠正功能。

## 相关控制项（原文，未解释为边）

网关路由选择功能

## 对应特性（原文）

WSFD-106004 请求信息纠正功能

## 控制的能力

- [WSFD-106004](feature/UNC/20.15.2/WSFD-106004.md)  — 控制项 82205928

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088210.md`
