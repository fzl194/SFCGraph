---
id: UDG@20.15.2@License@LKV3G5USQA01
type: License
name: 超高带宽UDP业务质量分析
nf: UDG
version: 20.15.2
license_code: LKV3G5USQA01
control_item_id: 82200BVB
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# 超高带宽UDP业务质量分析

`LKV3G5USQA01` · 控制项 82200BVB · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

网络中诸多故障处理类别中，数传问题的定位难度最大，复杂度也最高。数传异常多半会伴随一些异常现象或者异常报文，以这些异常作为切入点，进行有效的分析，可以达到快速定位的目的，并指导进一步的故障分析。<br>超高带宽UDP业务质量分析特性支持针对UDP业务进行传输层质量分析，辅助维护人员发现UDP层传输质量的问题和定位定界。

## 实现描述

UDG支持针对超高带宽用户的UDP流量分析手段，用来定位UDP数传问题。UDG在业务转发过程中自动分析出业务流的丢包、乱序、时延等指标，上报指标结果，详细跟踪可参考“创建UDG用户质量分析任务”。

## 取值范围

0～1

## 默认值

1

## 应用场景

当需要分析用户业务质量，定位UDP数传问题时，可部署本特性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110582 超高带宽UDP业务质量分析

## 控制的能力

- [GWFD-110582](feature/UDG/20.15.2/GWFD-110582.md)  — 控制项 82200BVB

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
