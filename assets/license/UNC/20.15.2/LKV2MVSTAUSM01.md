---
id: UNC@20.15.2@License@LKV2MVSTAUSM01
type: License
name: 通用DNN漫游分流
nf: UNC
version: 20.15.2
license_code: LKV2MVSTAUSM01
control_item_id: 82200GCE
applicable_nf:
- SMF
status: active
---

# 通用DNN漫游分流

`LKV2MVSTAUSM01` · 控制项 82200GCE ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

某行业的业务服务部署在行业总部所在的区域内，希望其职员可以通过终端，在归属地、省内其他区域、省外区域都能够随时访问行业内部业务和Internet。<br>5G Core通过通用DNN的漫游特性，为终端用户签约通用DNN和专用DNN，通过专用DNN访问行业内部业务，通过通用DNN访问Internet。可以满足用户在归属地同时访问行业内部业务和Internet，并且在跨地市、跨省漫游场景下，仍然能够保持业务不中断。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～100000 园区

## 默认值

0

## 应用场景

相较于UL CL分流，在智能分流场景下，终端用户不仅能在本地市访问行业内部业务，当用户漫游到省内其他地市或其他省份时，也可以访问行业内部业务。但是对于用户来说，经常存在出差到外地且需要访问行业内部业务的场景。通过在终端安装VPN软件等方式虽然支持通过Internet访问行业内部业务，但是存在操作繁琐、业务不流畅等问题。<br>部署本特性后，可满足终端用户在本地市、省内跨地市、跨省漫游场景下的同时访问行业内部业务和Internet。

## 相关控制项（原文，未解释为边）

WSFD-109101 PCC基本功能<br>WSFD-107010 UPF选择<br>WSFD-205012 跨域互联互通<br>WSFD-106203 别名APN

## 对应特性（原文）

WSFD-228002 基于通用DNN的漫游分特性概述

## 控制的能力

- [WSFD-228002](feature/UNC/20.15.2/WSFD-228002.md)  — 控制项 82200GCE

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
