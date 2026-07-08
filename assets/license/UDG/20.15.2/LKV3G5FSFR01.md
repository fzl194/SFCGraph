---
id: UDG@20.15.2@License@LKV3G5FSFR01
type: License
name: 业务全样分析上报
nf: UDG
version: 20.15.2
license_code: LKV3G5FSFR01
control_item_id: 82200CXM
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 业务全样分析上报

`LKV3G5FSFR01` · 控制项 82200CXM · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

控制报表的流抽样率大小。

## 实现描述

流抽样率大小受该License控制。<br>License不开启时，SET RPTGLBCFG命令配置的流抽样率如果大于100，则按100控制；小于等于100则按SET RPTGLBCFG命令配置的参数控制。<br>License开启时，流抽样率大小由SET RPTGLBCFG命令配置。

## 取值范围

10~8000000

## 默认值

10

## 应用场景

用户使用报表功能时，通过打开业务全样分析上报，来取消对流抽样率大小的限制。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-111011 业务全样分析上报

## 控制的能力

- [GWFD-111302](feature/UDG/20.15.2/GWFD-111302.md)  — 控制项 82200CXM

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
