---
id: UNC@20.15.2@License@LKV2ASLSR01
type: License
name: 跨域互联互通-AMF
nf: UNC
version: 20.15.2
license_code: LKV2ASLSR01
control_item_id: 82200CAH
applicable_nf:
- AMF
status: active
---

# 跨域互联互通-AMF

`LKV2ASLSR01` · 控制项 82200CAH ·  · 域 

## 归属/适用NF（原文）

AMF

## 功能描述

UE进行跨区域移动时，当UE新所在区域的UPF超出了原来SMF的服务范围，此时需要在接入的AMF和原SMF之间插入能够为当前服务区域提供服务的I-SMF（Intermediate SMF），以保证用户会话业务的连续性。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

大型运营商网络（规划多个SMF共同支持网络所有TAI），为了保证跨区域用户会话业务的连续性，建议使用本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205012 跨域互联互通

## 控制的能力

- [WSFD-205012](feature/UNC/20.15.2/WSFD-205012.md)  — 控制项 82200CAH

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63848073.md`
