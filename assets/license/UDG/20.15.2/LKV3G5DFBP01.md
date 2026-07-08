---
id: UDG@20.15.2@License@LKV3G5DFBP01
type: License
name: 双故障Bypass
nf: UDG
version: 20.15.2
license_code: LKV3G5DFBP01
control_item_id: 82200HHX
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 双故障Bypass

`LKV3G5DFBP01` · 控制项 82200HHX · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

通过该license控制IMSBYPASS功能是否使能。

## 实现描述

系统中如果用户为IMS用户，SMF没有创建动态语音专载，当语音业务承载通过业务触发状态创建时，则当前该License使用量加一，当SMF创建了动态语音专载，如果该用户执行+1操作，则会将当前该License使用量减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

中国广电没有2/3G打底网，PCF/PCRF合设部署，在语音PCF/PCRF故障后，4/5G语音主被叫业务将不可用。语音PCF/PCRF双故障后，4/5G语音主被叫惯性运行。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-112000 双故障Bypass

## 控制的能力

- [GWFD-112000](feature/UDG/20.15.2/GWFD-112000.md)  — 控制项 82200HHX

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
