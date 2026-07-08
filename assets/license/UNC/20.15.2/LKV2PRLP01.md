---
id: UNC@20.15.2@License@LKV2PRLP01
type: License
name: 本地P-GW的PDN重建
nf: UNC
version: 20.15.2
license_code: LKV2PRLP01
control_item_id: '82207534'
applicable_nf:
- MME
status: active
---

# 本地P-GW的PDN重建

`LKV2PRLP01` · 控制项 82207534 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

UE在网络在中移动，可能造成S-GW与P-GW不属于同一区域。启用本特性后，系统可以在对用户业务无影响的前提下，为UE重新选择本地P-GW进行业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

- 不同区域S-GW和P-GW之间的迂回流量较多，占用了原本就不丰富的移动承载网络资源。<br>- VoLTE用户在移动过程中出现S-GW与P-GW不在同一区域的情况时，存在语音传输迂回，影响用户体验。

## 相关控制项（原文，未解释为边）

依赖WSFD-205004 S-GW/P-GW 拓扑选择

## 对应特性（原文）

WSFD-205007 本地P-GW的PDN重建

## 控制的能力

- [WSFD-205007](feature/UNC/20.15.2/WSFD-205007.md)  — 控制项 82207534

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
