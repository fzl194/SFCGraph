---
id: UNC@20.15.2@License@LKV2URSPAM01
type: License
name: 支持URSP功能
nf: UNC
version: 20.15.2
license_code: LKV2URSPAM01
control_item_id: '81204131'
applicable_nf:
- AMF
status: active
---

# 支持URSP功能

`LKV2URSPAM01` · 控制项 81204131 ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

URSP（UE Route Selection Policy，UE路由选择策略）是UE策略的一部分，URSP包括切片选择策略、SSC模式选择策略、DNN选择策略、PDU Session类型选择策略、非无缝卸载指示，以及接入类型偏好，URSP可以用于辅助UE为上行流量选择合适的路由，如在已有PDU Session上传输、或卸载到Non-3GPP接入网络传输，或触发新建一个PDU Session传输，从而应对终端应用对“高速率”、“低时延”等网络体验的特殊要求。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

URSP主要解决的是用户5G应用的特殊场景如VR，AR，智能驾驶等对“超低时延”和“超高速率”等极致体验诉求，此处“特殊场景”主要指对上网体验有非同一般体验的要求，比如高速移动下希望视频0卡顿且画质清晰等。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-211102 支持URSP能力

## 控制的能力

- [WSFD-211102](feature/UNC/20.15.2/WSFD-211102.md)  — 控制项 81204131

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15568026.md`
