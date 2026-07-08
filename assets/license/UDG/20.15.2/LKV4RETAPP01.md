---
id: UDG@20.15.2@License@LKV4RETAPP01
type: License
name: 第三方应用实例可靠性增强(vCPU)
nf: UDG
version: 20.15.2
license_code: LKV4RETAPP01
control_item_id: '82207066'
license_domain: SFIP
control_item_type: resource
applicable_nf:
- GW-U
- UPF
status: active
---

# 第三方应用实例可靠性增强(vCPU)

`LKV4RETAPP01` · 控制项 82207066 · resource · 域 SFIP

## 归属/适用NF（原文）

GW-U/UPF

## 功能描述

“第三方应用实例可靠性增强(vCPU)”是控制第三方APP故障检测功能是否可用，统计的是所有集成APP的vCPU，用来控制第三方故障检测功能。

## 实现描述

总License量纲是“第三方应用实例可靠性增强(vCPU)”，该License项个数与“SFIP基本功能(vCPU)”一致。<br>如果License开关打开，第三方应用实例可靠性功能可用，<br>UDG<br>检测第三方应用实例的健康状态（包括插件心跳等）和故障信息；将故障状态及时上报并进行故障隔离。<br>如果License开关关闭，第三方应用实例可靠性功能不可用，<br>UDG<br>只保留NFVI层的故障检测结果。

## 取值范围

0~10000

## 默认值

10

## 应用场景

系统对第三方应用实例故障状态进行检测，对于影响用户业务访问的第三方用于实例进行隔离。

## 相关控制项（原文，未解释为边）

SFIP基本功能(vCPU)

## 对应特性（原文）

第三方应用实例可靠性增强

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_09019541.md`
