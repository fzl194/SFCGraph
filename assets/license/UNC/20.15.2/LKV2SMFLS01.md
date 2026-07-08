---
id: UNC@20.15.2@License@LKV2SMFLS01
type: License
name: 本地PDU会话重建-SMF
nf: UNC
version: 20.15.2
license_code: LKV2SMFLS01
control_item_id: 82200CJR
applicable_nf:
- SMF
status: active
---

# 本地PDU会话重建-SMF

`LKV2SMFLS01` · 控制项 82200CJR ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

UE在移动过程中，可能会出现AMF与SMF不在同一区域（例如，不同省份）的情况，可能会出现AMF和SMF不在同一区域需要插入I-SMF的情况，导致I-SMF和SMF管理下的UPF之间的迂回流量增加，业务时延也会增加。AMF支持本地SMF重选特性可以识别AMF与SMF不在同一区域的PDU会话连接，并在对用户业务无影响的前提下，为UE重新选择与AMF同区域的本地SMF进行业务。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

建议在以下场景开通该特性：不同区域AMF和SMF之间的迂回流量较多，占用了原本就不丰富的移动承载网络资源。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205011 本地PDU会话重建

## 控制的能力

- [WSFD-205011](feature/UNC/20.15.2/WSFD-205011.md)  — 控制项 82200CJR

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
