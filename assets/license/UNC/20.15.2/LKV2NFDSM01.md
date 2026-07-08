---
id: UNC@20.15.2@License@LKV2NFDSM01
type: License
name: NF发现-USM
nf: UNC
version: 20.15.2
license_code: LKV2NFDSM01
control_item_id: '81203240'
applicable_nf:
- SMF
status: active
---

# NF发现-USM

`LKV2NFDSM01` · 控制项 81203240 ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

NRF支持NF/NFS服务发现功能，当NF需要某些特定服务时，向NRF请求发现可用服务，NRF基于已注册的NF/NFS进行筛选，将可用NF/NFS发送给NF。NRF支持基于不同选择条件进行特定NF的选择，有助于不同组网方式下的NF选择。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

- 用户签约数据的新增、修改、删除或获取签约数据等相关流程涉及UDM的选择。当运营商规划了多个服务于不同的号段的UDM网络场景下，可以基于号段（supi或gpsi或routing-indicator属性）选择对应UDM。<br>- 策略控制功能相关流程涉及PCF的选择。当运营商规划了多个服务于不同号段的PCF网络场景下，可以基于号段（supi属性）选择对应PCF。<br>- 策略控制功能相关流程涉及PCF的选择。当运营商规划了多个服务于不同DNN的PCF网络场景下，可以基于DNN（dnn属性）选择对应PCF。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

- WSFD-113006 基于号段选择NF<br>- WSFD-113009 基于DNN选择PCF

## 控制的能力

- [WSFD-113006](feature/UNC/20.15.2/WSFD-113006.md)  — 控制项 81203240
- [WSFD-113009](feature/UNC/20.15.2/WSFD-113009.md)  — 控制项 81203240

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568030.md`
