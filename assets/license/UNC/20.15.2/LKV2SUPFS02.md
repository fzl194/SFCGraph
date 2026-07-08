---
id: UNC@20.15.2@License@LKV2SUPFS02
type: License
name: 公私网协同访问
nf: UNC
version: 20.15.2
license_code: LKV2SUPFS02
control_item_id: 82200DDS
applicable_nf:
- SMF
status: active
---

# 公私网协同访问

`LKV2SUPFS02` · 控制项 82200DDS ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

SMF支持用户通过同一个DNN（Data Network Name）访问公网和私网业务，同时私网之间业务隔离。SMF将为用户优先选择主锚点、辅锚点和UL CL UPF合一部署的UPF，分别建立到主锚点和辅锚点UPF的N4会话，同时访问公网和私网业务。SMF针对不同用户策略配置不同DNAI（Data Network Access Identifier），UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别不同的辅锚点N4会话，实现私网之间业务隔离。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

当为某工业园区建网络，希望接入园区的用户可以使用同一个DNN访问公网以及私网业务并且私网之间业务隔离，可以使用该特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-223002 公私网协同访问

## 控制的能力

- [WSFD-223002](feature/UNC/20.15.2/WSFD-223002.md)  — 控制项 82200DDS

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
