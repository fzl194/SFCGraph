---
id: UDG@20.15.2@License@LKV4SSTAPP02
type: License
name: 第三方应用智能运维(vCPU)
nf: UDG
version: 20.15.2
license_code: LKV4SSTAPP02
control_item_id: '82207652'
license_domain: SFIP
control_item_type: resource
applicable_nf:
- GW-U
- UPF
status: active
---

# 第三方应用智能运维(vCPU)

`LKV4SSTAPP02` · 控制项 82207652 · resource · 域 SFIP

## 归属/适用NF（原文）

GW-U/UPF

## 功能描述

第三方应用智能运维(vCPU)包括的功能项有智能Scaling、第三方应用升级。<br>- 智能Scaling：UDG定时收集第三方应用VNF内部的负荷，当负荷高于设置阈值时，UDG触发指定第三方应用VNF资源的增加操作。<br>- 第三方应用升级：UDG为不同的第三方应用提供统一的升级功能，支持VNF、VDU、app插件等粒度的升级。

## 实现描述

总License量纲是“第三方应用智能运维(vCPU)”，该License项个数与“SFIP基本功能(vCPU)”一致。<br>如果License打开，第三方应用智能运维(vCPU)特性可用，<br>UDG<br>可以对第三方应用实例进行镜像/软件升级、自动scaling；<br>如果License关闭，或者License文件过期后，第三方应用智能运维(vCPU)特性不可用，镜像/软件升级、自动scaling功能均不可用。

## 取值范围

0~10000

## 默认值

10

## 应用场景

第三方应用升级：应用于第三方应用的软件包、插件包等升级场景。

## 相关控制项（原文，未解释为边）

SFIP基本功能(vCPU)

## 对应特性（原文）

第三方应用智能运维

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_09019541.md`
