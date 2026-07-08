---
id: UDG@20.15.2@License@LKV3G5FSHP01
type: License
name: 基于智能Shaping的组级带宽控制
nf: UDG
version: 20.15.2
license_code: LKV3G5FSHP01
control_item_id: 82200FNS
license_domain: UDG
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 基于智能Shaping的组级带宽控制

`LKV3G5FSHP01` · 控制项 82200FNS · resource · 域 UDG

## 归属/适用NF（原文）

UPF

## 功能描述

UDG<br>支持基于智能Shaping的组级带宽控制功能。

## 实现描述

UDG通过基于Shaping的分级带宽管控，使整形后的用户报文出口速率稳定，自动模式下可以基于每个优先级业务的分布自动调整业务的出口带宽，保障高低优先级业务的调度公平，支持基于用户公平的调度能力，避免直接丢包对用户体验产生影响，同时对流量速率进行判断是否进行缓存，提升产品性能；<br>UDG<br>通过license对该功能进行控制。

## 取值范围

10～16000000

## 默认值

10

## 应用场景

适用于用户业务占用大量网络带宽资源，造成带宽拥塞，需要区分多种业务等级实现流量整形，业务体验可控，并保障用户调度公平的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110313 基于智能Shaping的组级带宽控制

## 控制的能力

- [GWFD-110313](feature/UDG/20.15.2/GWFD-110313.md)  — 控制项 82200FNS

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
