---
id: UNC@20.15.2@License@LKV2HUNN01
type: License
name: HSS免升级
nf: UNC
version: 20.15.2
license_code: LKV2HUNN01
control_item_id: '81202653'
applicable_nf:
- MME
status: active
---

# HSS免升级

`LKV2HUNN01` · 控制项 81202653 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

在HSS未升级不支持NB-IoT终端接入、无法进行Non-IP数据传输的情况下，通过配置使MME发送给HSS可以识别的消息和信元，保证NB-IoT终端成功接入网络。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1 UNC

## 默认值

1

## 应用场景

NB-IoT技术广泛应用于多种行业，如智能抄表、智能照明、智能垃圾桶、智能宠物健康跟踪、智能农业等，而在诸多行业和业务中，运营商需要确认部署NB-IoT后对周边网元的诉求和影响，开销很大，且有不确定性。<br>当需要HSS在不升级的情况下，就可以支持NB-IoT用户的接入并可以采用Non-IP Data Over NAS进行数据传输时，建议开启本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215301 HSS免升级

## 控制的能力

- [WSFD-215301](feature/UNC/20.15.2/WSFD-215301.md)  — 控制项 81202653

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_64048053.md`
