---
id: UDG@20.15.2@License@LKV3G5TETH01
type: License
name: Tethering用户识别
nf: UDG
version: 20.15.2
license_code: LKV3G5TETH01
control_item_id: '82209772'
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# Tethering用户识别

`LKV3G5TETH01` · 控制项 82209772 · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

Tethering是指其他设备通过移动电话共享上网，其主要方式有：WiFi、蓝牙、物理连接等。当Tethering用户识别功能开启后，业务报文到达<br>UDG<br>时，<br>UDG<br>侧会判断该业务是否为Tethering业务，如果为Tethering业务，则<br>UDG<br>会根据匹配到的规则进行相应的业务控制与计费。在部署UPCF场景下，若UPCF下发了Tethering状态上报，则<br>UDG<br>还会上报Tethering状态给UPCF。

## 实现描述

在开启Tethering用户识别功能后，可以在<br>UDG<br>上配置是否进行Tethering业务的识别，即在flowfilter中配置tethering-detect参数。如果filter-group配置了tethering-detect参数，则在filter匹配成功时，通过检测报文的TTL值，如果TTL值符合Tethering行为特征值，则表示该业务为Tethering业务；不符合，则表示该业务不是Tethering业务。<br>UDG<br>识别出Tethering业务后，根据匹配到的规则进行相应的业务控制与计费，并进行相应的性能统计；在部署UPCF场景下，<br>UDG<br>也支持向UPCF上报Tethering状态。<br>UPCF可以根据用户的Tethering状态进行相应处理，如当用户未签约Tethering套餐时，可以短信、邮件通知用户，要求在指定时间内升级到专门的Tethering套餐计划，否则会禁止使用Tethering业务等。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

对于部署了Tethering方案的运营商，对Tethering业务会提供专门的套餐，对于未签约Tethering套餐的用户，会限制Tethering业务的使用、或者提醒用户需要进行Tethering业务的签约。通过使用Tethering用户识别功能可以很好的支持该业务需求。

## 相关控制项（原文，未解释为边）

PCC 基本功能

## 对应特性（原文）

GWFD-110143 Tethering用户识别

## 控制的能力

- [GWFD-110143](feature/UDG/20.15.2/GWFD-110143.md)  — 控制项 82209772

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
