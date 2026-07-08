---
id: UNC@20.15.2@License@LKV2NFASM01
type: License
name: NF认证-USM
nf: UNC
version: 20.15.2
license_code: LKV2NFASM01
control_item_id: '81203237'
applicable_nf:
- SMF
status: active
---

# NF认证-USM

`LKV2NFASM01` · 控制项 81203237 ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

此license控制以下两个特性：<br>安全层面考虑，NF请求提供某种服务时需要获取授权，以预防和降低权限提升风险。5GC网络的NF间的服务化接口采用Oauth2.0动态Token授权，授权方式为Client Credentials。Token可以理解为NF请求访问某服务使用的短期令牌，当且仅当手持令牌时，才能获取所需服务。NF首次申请服务进行服务发现后，向NRF申请Access Token，然后携带此Access Token进行后续对应业务请求。Access Token失效或请求的服务发生变化时，NF请求方会申请新的Access Token。<br>NF服务消费者请求提供服务，携带从NRF获取的Access Token向NF服务提供者进行业务请求时，NF服务提供者首先对NF服务消费者进行认证，确保Access Token的完整性和合法性后，再提供服务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

- NF首次请求提供某种服务（例如PDU会话建立，AMF请求SMF的服务建立会话）时，需要首先获取Token授权，NRF向NF提供Access Token后，NF进行后续NF认证和对应业务服务。<br>- Access Token失效或NF申请的服务范围变化或有新的服务提供方NF却无可用Access Token，NF请求方也会申请新的Token。<br>- NF请求提供服务时，需要携带NRF授权的Access Token，进行NF认证，进而支撑后续完成业务服务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

- WSFD-112001 NF Token管理<br>- WSFD-112002 支持NF认证

## 控制的能力

- [WSFD-112001](feature/UNC/20.15.2/WSFD-112001.md)  — 控制项 81203237
- [WSFD-112002](feature/UNC/20.15.2/WSFD-112002.md)  — 控制项 81203237

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568030.md`
