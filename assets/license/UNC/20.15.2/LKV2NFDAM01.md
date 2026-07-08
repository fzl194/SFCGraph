---
id: UNC@20.15.2@License@LKV2NFDAM01
type: License
name: NF发现-UAM
nf: UNC
version: 20.15.2
license_code: LKV2NFDAM01
control_item_id: '81203239'
applicable_nf:
- AMF
status: active
---

# NF发现-UAM

`LKV2NFDAM01` · 控制项 81203239 ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

NRF支持NF/NFS服务发现功能，当NF需要某些特定服务时，向NRF请求发现可用服务，NRF基于已注册的NF/NFS进行筛选，将可用NF/NFS发送给NF。NRF支持基于不同选择条件进行特定NF的选择，有助于不同组网方式下的NF选择。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

- UE注册（AMF与上次注册时的AMF不同）、基于N2接口的Handover等流程涉及选择AMF。当运营商部署了不同网络服务场景下，可以基于GUAMI灵活选择对应网络下的AMF。<br>- UE请求PDU Session建立等涉及SMF的选择。当运营商部署了不同网络组网场景下，可以基于签约信息(snssais和dnn属性)灵活选择对应网络下的SMF。<br>- 用户和网络的交互过程中，网络侧和用户需要互相鉴权保证用户合法性和接入网络安全性，其中的鉴权流程涉及AUSF的选择。当运营商规划了多个服务于不同号段的AUSF网络场景下，可以基于号段（supi或routing-indicator属性）选择对应AUSF。<br>- 用户签约数据的新增、修改、删除或获取签约数据等相关流程涉及UDM的选择。当运营商规划了多个服务于不同的号段的UDM网络场景下，可以基于号段（supi或gpsi或routing-indicator属性）选择对应UDM。<br>- 策略控制功能相关流程涉及PCF的选择。当运营商规划了多个服务于不同号段的PCF网络场景下，可以基于号段（supi属性）选择对应PCF。<br>- NRF支持NF/NFS服务发现功能，NF选择流程中，NRF可以支持基于NF位置优选特定区域的NF提供服务。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

- WSFD-113001 基于基本属性选择AMF<br>- WSFD-113002 SMF发现和选择<br>- WSFD-113006 基于号段选择NF<br>- WSFD-113011 基于部署区域选择NF

## 控制的能力

- [WSFD-113001](feature/UNC/20.15.2/WSFD-113001.md)  — 控制项 81203239
- [WSFD-113002](feature/UNC/20.15.2/WSFD-113002.md)  — 控制项 81203239
- [WSFD-113006](feature/UNC/20.15.2/WSFD-113006.md)  — 控制项 81203239
- [WSFD-113011](feature/UNC/20.15.2/WSFD-113011.md)  — 控制项 81203239

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568026.md`
