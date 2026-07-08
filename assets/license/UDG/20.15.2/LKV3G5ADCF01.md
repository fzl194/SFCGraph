---
id: UDG@20.15.2@License@LKV3G5ADCF01
type: License
name: 增强的ADC基本功能
nf: UDG
version: 20.15.2
license_code: LKV3G5ADCF01
control_item_id: 82200AFK
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 增强的ADC基本功能

`LKV3G5ADCF01` · 控制项 82200AFK · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

在系统中控制允许接入的具有增强的ADC基本功能上下文数。

## 实现描述

用户激活时，如果增强的ADC基本功能的License没有用尽，该用户可以激活为具有ADC功能用户。系统中每激活一个具有ADC功能的上下文，增强的ADC基本功能上下文数加一；每去激活一个具有ADC功能的上下文，支持基于ADC功能上下文数减一。<br>用户激活时，如果增强的ADC基本功能的License用尽，该用户激活成功，不具有ADC功能。<br>当GTPv1用户发起二次上下文创建时，若ADC功能的License用尽，开启ADC功能的二次上下文创建失败。<br>当GTPv2用户发起默认承载创建时，若ADC功能的License用尽，默认承载创建成功，但不开启ADC功能。<br>当GTPv2用户发起专有承载创建时，若ADC功能的License用尽，开启ADC功能的专有承载创建失败。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

UDG<br>网元中使用增强的ADC基本功能的用户接入。

## 相关控制项（原文，未解释为边）

PCC基本功能

## 对应特性（原文）

GWFD-020357 增强的ADC基本功能

## 控制的能力

- [GWFD-020357](feature/UDG/20.15.2/GWFD-020357.md)  — 控制项 82200AFK

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
