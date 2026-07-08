---
id: UDG@20.15.2@License@LKV3G5RVCC01
type: License
name: SRVCC
nf: UDG
version: 20.15.2
license_code: LKV3G5RVCC01
control_item_id: '82209831'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# SRVCC

`LKV3G5RVCC01` · 控制项 82209831 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U

## 功能描述

SRVCC功能支持用户从E-UTRAN到只有UTRAN/GERAN接入环境时，语音无缝切换。

## 实现描述

如果系统中存在“SRVCC”的License，则接入的PDP支持SRVCC功能，当用户从4G分组域切换到2、3G电路域时，可以保持通话不断

## 取值范围

0～16000000

## 默认值

10

## 应用场景

支持用户的语音无缝切换。

## 相关控制项（原文，未解释为边）

- 支持IMS接入<br>- PCC基本功能

## 对应特性（原文）

GWFD-020252 SRVCC

## 控制的能力

- [GWFD-020252](feature/UDG/20.15.2/GWFD-020252.md)  — 控制项 82209831

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
