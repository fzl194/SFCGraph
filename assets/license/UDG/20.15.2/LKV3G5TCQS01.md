---
id: UDG@20.15.2@License@LKV3G5TCQS01
type: License
name: 会话类QoS保证
nf: UDG
version: 20.15.2
license_code: LKV3G5TCQS01
control_item_id: '82209827'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
status: active
---

# 会话类QoS保证

`LKV3G5TCQS01` · 控制项 82209827 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U

## 功能描述

会话类QoS保证是指<br>UDG<br>在用户数据传输时通过流分类、QoS标记、带宽控制、高优先级队列发送等手段保证会话类业务的数据转发。

## 实现描述

License中会话类QoS保证资源项为允许时，会话类QoS保证功能生效；否则不生效。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

VOIP、视频电话、视频会议等基于IP网络的会话。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020381 会话类QoS保证

## 控制的能力

- [GWFD-020381](feature/UDG/20.15.2/GWFD-020381.md)  — 控制项 82209827

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
