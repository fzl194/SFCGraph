---
id: UDG@20.15.2@License@LKV3G5TWMP01
type: License
name: 支持TWAMP
nf: UDG
version: 20.15.2
license_code: LKV3G5TWMP01
control_item_id: 82200DHF
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- UPF
status: active
---

# 支持TWAMP

`LKV3G5TWMP01` · 控制项 82200DHF · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U/UPF

## 功能描述

通过该license控制是否支持TWAMP。

## 实现描述

该license控制是否支持TWAMP基本功能。该License项为功能项， License中支持TWAMP基本功能开启时，系统启动SGW-U/UPF和eNodeB/gNodeB间的链路质量探测，链路质量统计结果以性能指标统计方式上报到U2020/MAE。也可以检测SGW-U/UPF到传输路径上支持TWAMP功能的节点间的链路质量。

## 取值范围

0～8000

## 默认值

0

## 应用场景

当运营商需要监测SGW-U/UPF到eNodeB/gNodeB，或者SGW-U/UPF到传输路径上节点间的链路质量，对链路上的丢包、时延、抖动等状态信息进行观测，也用于上述链路上出现丢包、时延、抖动等网络问题时，进行问题的快速定位定界。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110911 支持TWAMP

## 控制的能力

- [GWFD-110921](feature/UDG/20.15.2/GWFD-110921.md)  — 控制项 82200DHF

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
