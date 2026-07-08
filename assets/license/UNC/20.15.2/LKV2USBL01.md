---
id: UNC@20.15.2@License@LKV2USBL01
type: License
name: UPF选择
nf: UNC
version: 20.15.2
license_code: LKV2USBL01
control_item_id: '82209917'
applicable_nf:
- SMF
status: active
---

# UPF选择

`LKV2USBL01` · 控制项 82209917 ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

UNC<br>可以根据用户接入的DNN、切片和位置信息，为用户选择满足指定业务的、地理位置贴近用户的UPF，还可以结合UPF的分流能力、接口能力、是否支持与EPS的互通、权重来选择UPF。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

在以下场景可以使用该特性：<br>- 当运营商为用户的某些业务规划部署专用的UPF设备时；<br>- 当运营商将UPF设备部署到贴近用户的地理位置时；<br>- 当多UPF间的负载不均衡时。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-107010 UPF选择

## 控制的能力

- [WSFD-107010](feature/UNC/20.15.2/WSFD-107010.md)  — 控制项 82209917

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
