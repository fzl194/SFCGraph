---
id: UDG@20.15.2@License@LKV3G5VLEF01
type: License
name: VoLTE基础语音业务
nf: UDG
version: 20.15.2
license_code: LKV3G5VLEF01
control_item_id: '82209873'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# VoLTE基础语音业务

`LKV3G5VLEF01` · 控制项 82209873 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

在<br>UDG<br>系统中控制允许接入的VoLTE基础语音服务功能PDP上下文数，当License资源充足时，<br>UDG<br>允许新的VoLTE的基础语音服务功能PDP上下文接入系统。

## 实现描述

PCRF上签约VoLTE基础语音服务功能用户，从Gx接口下发给对应的策略信息（QCI/ARP）。网关在承载创建、更新、寻呼时将其传递给AMF。<br>系统中每激活一个VoLTE基础语音服务功能PDP上下文，VoLTE基础语音服务功能PDP上下文数加一；每去激活一个VoLTE基础语音服务功能PDP上下文，VoLTE基础语音服务功能PDP上下文数减一。<br>如果系统中已激活的VoLTE基础语音服务功能PDP上下文数，达到License中“VoLTE基础语音服务”，则新的VoLTE基础语音服务功能PDP上下文将无法激活。激活失败原因值填写73“No resources available”。<br>例如：“VoLTE基础语音服务”License为1000；系统中当前已接入的VoLTE基础语音服务功能PDP上下文为1000，则“VoLTE基础语音服务”License全部被占用，此时新的VoLTE基础语音服务功能PDP上下文将无法接入到系统。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

UDG<br>网元中SGW-U，PGW-U，UPF形态下的基于VoLTE的优先语音服务上下文接入。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020251 VoLTE基础语音业务

## 控制的能力

- [GWFD-020251](feature/UDG/20.15.2/GWFD-020251.md)  — 控制项 82209873

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
