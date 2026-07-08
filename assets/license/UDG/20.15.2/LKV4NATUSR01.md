---
id: UDG@20.15.2@License@LKV4NATUSR01
type: License
name: 溯源日志携带用户标志(Mbps)
nf: UDG
version: 20.15.2
license_code: LKV4NATUSR01
control_item_id: 82200DAD
license_domain: VAS
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 溯源日志携带用户标志(Mbps)

`LKV4NATUSR01` · 控制项 82200DAD · resource · 域 VAS

## 归属/适用NF（原文）

UPF

## 功能描述

NAT生成的溯源日志可携带用户信息（包含IMSI和MSISDN）通过安全加密通道上报至日志服务器供运营商查看。

## 实现描述

总License量纲是“溯源日志携带用户标志(Mbps)”，该License项个数与“NAT基本功能(Mbps)”一致。<br>如果License打开，溯源日志携带用户标志功能可用；<br>如果License关闭，溯源日志携带用户标志功能不可用。

## 取值范围

0~8000000

## 默认值

10

## 应用场景

普通的NAT溯源日志仅携带日期、源IP地址、源端口号、转换后IP地址及转换后端口号等信息，无法精确定位准确用户的转换过程，若运营商需要查看更多日志信息，则需要开启本特性，使生成的NAT溯源日志携带用户信息。

## 相关控制项（原文，未解释为边）

溯源日志上报(Mbps)

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_24575797.md`
