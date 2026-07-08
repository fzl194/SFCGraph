---
id: UDG@20.15.2@License@LKV3G5EBCS01
type: License
name: 支持事件计费
nf: UDG
version: 20.15.2
license_code: LKV3G5EBCS01
control_item_id: 82200CKE
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 支持事件计费

`LKV3G5EBCS01` · 控制项 82200CKE · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

事件计费是依据用户使用某种数据业务的次数进行计费的一种计费方式，该计费方式与基于流量、时长计费的方式类似，是一种新维度的计费方式。例如，用户访问HTTP业务，根据用户访问URL的次数进行收费，或者按照彩信收发的次数进行收费。

## 实现描述

融合计费通过信用控制会话实时扣费，当PGW-C/SMF上通过配置ADD URR设置业务计费是事件类型，且CHF在消息中下发了事件配额即可进行事件计费。<br>在线计费通过信用控制会话实时扣费，当PGW-C/SMF上通过配置ADD URR设置业务计费是事件类型，且OCS在CC消息中下发了事件配额即可进行事件计费。<br>离线计费通过话单将用户计费信息上报给计费系统BS，当PGW-C/SMF上通过配置ADD URR设置业务计费是事件类型后，即在话单中增加事件计费信息。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

运营商与企业合作推广企业业务，推送彩信给客户，可开启本特性根据彩信的发送次数计费，促进企业和运营商双赢。<br>运营Portal网站或APP也可与运营商开展合作，以访问网站次数计费，达到网站或APP运营推广，同时为运营商增加新的收入增长点。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020306 支持事件计费

## 控制的能力

- [GWFD-020306](feature/UDG/20.15.2/GWFD-020306.md)  — 控制项 82200CKE

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
