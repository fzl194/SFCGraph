---
id: UDG@20.15.2@License@LKV3G5TATC01
type: License
name: Tethering接入终端策略控制
nf: UDG
version: 20.15.2
license_code: LKV3G5TATC01
control_item_id: '81203205'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# Tethering接入终端策略控制

`LKV3G5TATC01` · 控制项 81203205 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

Tethering接入终端策略控制是指当<br>UDG<br>检测到接入前台的后台终端数量超过设定的规格时，如果加载了该功能则可以对Tethering用户下的终端做策略控制，当前仅支持带宽控制。

## 实现描述

License在三四层rule匹配之前，如果加载了Tethering接入终端控制策略License且Tethering终端数量检测的全局开关开启则对TCP流的SYN包进行tcp解析，并通过Tethering用户数终端数量看能否确定该流是属于哪个终端以及是否超规格，设置tethering是否满足tethering detect filter的匹配条件。如果满足tethering detect filter的匹配条件，则在匹配34层rule时，tethering rule参与匹配，否则，tethering rule不参与匹配直接判断为匹配失败。如果34层rule匹配可以精确命中，则直接使用该rule进行策略控制；如果34层rule匹配不能精确命中，则直接使用该rule做临时费率。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

如果Tethering用户识别及Tethering接入终端策略开启，并且开启Tethering用户终端数量检测开关，则网关支持Tethering用户终端数量检测功能，且Tethering用户终端数量超规格后支持做tethering策略控制。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110144 Tethering接入终端策略控制特性概述

## 控制的能力

- [GWFD-110144](feature/UDG/20.15.2/GWFD-110144.md)  — 控制项 81203205

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
