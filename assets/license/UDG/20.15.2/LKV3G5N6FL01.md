---
id: UDG@20.15.2@License@LKV3G5N6FL01
type: License
name: N4/N6故障联动
nf: UDG
version: 20.15.2
license_code: LKV3G5N6FL01
control_item_id: '81203754'
license_domain: UDG
control_item_type: function
applicable_nf:
- PGW-U
- UPF
status: active
---

# N4/N6故障联动

`LKV3G5N6FL01` · 控制项 81203754 · function · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

在系统中控制N6路径故障N4联动上报功能。

## 实现描述

N6路径故障N4联动上报功能受此license控制。<br>License不开启时，系统不能通过N4接口将N6路径状态上报控制面。<br>License开启时，系统能通过N4接口将N6路径状态上报控制面。

## 取值范围

0~1

## 默认值

1

## 应用场景

当需要系统探测到N6路径状态并通过N4接口上报控制面时，开启此License。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-021407 快速业务恢复

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
