---
id: UNC@20.15.2@License@LKV2MVSVPSM01
type: License
name: MBB可视化解决方案增值包-USM
nf: UNC
version: 20.15.2
license_code: LKV2MVSVPSM01
control_item_id: 82200FDE
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# MBB可视化解决方案增值包-USM

`LKV2MVSVPSM01` · 控制项 82200FDE ·  · 域 

## 归属/适用NF（原文）

GGSN-C/SGW-C/PGW-C/SMF

## 功能描述

显示系统中接入的2G&3G&4G&5G NSA&5G SA承载数。

## 实现描述

GGSN/GW-C/SMF系统中每激活一个2G或3G或4G或5G NSA或5G SA承载，该License总数加1；每去激活一个2G或3G或4G或5G NSA或5G SA承载，总数减1。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

GGSN/GW-C/SMF中激活2G或3G或4G或5G NSA或5G SA承载。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
