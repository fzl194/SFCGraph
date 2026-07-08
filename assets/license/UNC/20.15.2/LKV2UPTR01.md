---
id: UNC@20.15.2@License@LKV2UPTR01
type: License
name: 用户面转发能力(Mbit/s)
nf: UNC
version: 20.15.2
license_code: LKV2UPTR01
control_item_id: '82206542'
applicable_nf:
- SGSN
status: active
---

# 用户面转发能力(Mbit/s)

`LKV2UPTR01` · 控制项 82206542 ·  · 域 

## 归属/适用NF（原文）

SGSN

## 功能描述

本License控制资源用于对整系统用户面的转发能力加以限制。

## 实现描述

用户面占用带宽的计算方法：当有PDP激活成功时，用户面带宽变为用户面已占用的带宽加上该PDP正在协商的带宽资源；当有PDP去激活完成时，用户面带宽变为已占用的带宽减去该PDP协商的带宽资源。<br>用户面转发带宽License控制系统可以供使用的带宽，如果使用的转发带宽（静态带宽触发）超过License限制，所有用户PDP不允许接入；如果使用的转发带宽（动态带宽触发）超过License限制，则进行License流控，并且不允许3/4类用户PDP接入。

## 取值范围

0～180000 (Mbit/s)

## 默认值

10

## 应用场景

通过本License值来限制用户面带宽。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无（对应基本功能）

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15248050.md`
