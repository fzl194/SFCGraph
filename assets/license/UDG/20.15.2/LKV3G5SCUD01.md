---
id: UDG@20.15.2@License@LKV3G5SCUD01
type: License
name: 基于上下行解耦的视频承载信令控制
nf: UDG
version: 20.15.2
license_code: LKV3G5SCUD01
control_item_id: 82200EBQ
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 基于上下行解耦的视频承载信令控制

`LKV3G5SCUD01` · 控制项 82200EBQ · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

控制是否支持上下行解耦的视频承载信令控制功能

## 实现描述

系统中每激活一个上下行解耦承载/QoS流，则此License资源数加一；每去激活一个上下行解耦承载/QoS流，则此License资源数减一。

## 取值范围

0~16000000

## 默认值

10

## 应用场景

当用户需要支持上下行解耦的视频承载信令控制功能时，需要开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110302 基于上下行解耦的视频承载信令控制

## 控制的能力

- [GWFD-110302](feature/UDG/20.15.2/GWFD-110302.md)  — 控制项 82200EBQ

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
