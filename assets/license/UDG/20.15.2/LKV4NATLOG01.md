---
id: UDG@20.15.2@License@LKV4NATLOG01
type: License
name: 溯源日志上报(Mbps)
nf: UDG
version: 20.15.2
license_code: LKV4NATLOG01
control_item_id: 82200DAC
license_domain: VAS
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 溯源日志上报(Mbps)

`LKV4NATLOG01` · 控制项 82200DAC · resource · 域 VAS

## 归属/适用NF（原文）

UPF

## 功能描述

为了对用户上网过程中的NAT转换进行溯源，NAT支持生成转换日志，并支持将其上报至日志服务器供运营商查看。

## 实现描述

总License量纲是“溯源日志上报(Mbps)”，该License项个数与“NAT基本功能(Mbps)”一致。<br>如果License打开，溯源日志上报功能可用；<br>如果License关闭，溯源日志上报功能不可用。

## 取值范围

0~8000000

## 默认值

10

## 应用场景

在设备正常运行期间，若运营商需要查看NAT转换的记录，了解用户地址的转换信息，则需开启本特性。

## 相关控制项（原文，未解释为边）

NAT基本功能(Mbps)

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_24575797.md`
