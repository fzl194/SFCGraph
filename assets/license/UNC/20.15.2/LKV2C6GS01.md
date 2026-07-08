---
id: UNC@20.15.2@License@LKV2C6GS01
type: License
name: Category 6 网关选择
nf: UNC
version: 20.15.2
license_code: LKV2C6GS01
control_item_id: '82206563'
applicable_nf:
- SGSN
- MME
status: active
---

# Category 6 网关选择

`LKV2C6GS01` · 控制项 82206563 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

Category 6网关选择功能，是指在<br>UNC<br>上为特定类型的终端配置IMEI-TAC库，系统通过匹配终端IMEI和IMEI-TAC库，识别终端类型。在使用APN（Access Point Name）进行DNS（Domain Name Service）解析寻址网关前，将为特定类型终端定制的LABEL信息加入到APN-NI和APN-OI之间，然后将扩展的APN发送到DNS服务器解析，为这些终端用户选择定制网关，提供差异化服务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

当运营商希望对某些终端选择高速网关，为用户提供差异化服务时，建议启用本特性。

## 相关控制项（原文，未解释为边）

依赖<br>WSFD-101401 Category 6基础功能<br>WSFD-205004 S-GW/P-GW 拓扑选择<br>WSFD-205006 基于P-GW锚点选择S-GW<br>WSFD-205007 本地P-GW的PDN重建

## 对应特性（原文）

WSFD-205008 Category 6网关选择

## 控制的能力

- [WSFD-205008](feature/UNC/20.15.2/WSFD-205008.md)  — 控制项 82206563

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
