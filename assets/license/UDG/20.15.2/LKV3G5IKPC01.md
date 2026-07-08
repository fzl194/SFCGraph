---
id: UDG@20.15.2@License@LKV3G5IKPC01
type: License
name: KPI智能关联
nf: UDG
version: 20.15.2
license_code: LKV3G5IKPC01
control_item_id: 82200ECU
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# KPI智能关联

`LKV3G5IKPC01` · 控制项 82200ECU · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

通过AI智能学习算法，实现KPI指标自动异常检测，快速识别和发现KPI异常问题，并通过多KPI指标智能关联分析，实现KPI异常问题快速定位，提升问题定位效率。

## 实现描述

网元上报话统指标数据，U2020/MAE对话统指标数据进行解析保存，将KPI数据导入到单KPI智能异常检测算法进行预测和智能检测，<br>将单KPI智能异常检测算法的结果导入到多KPI智能关联辅助KPI异常分析算法中进行处理，维护人员依据处理结果快速锁定问题可能原因。

## 取值范围

0～100000

## 默认值

10

## 应用场景

业务运行态下的日常KPI监控。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-110491 KPI智能关联

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
