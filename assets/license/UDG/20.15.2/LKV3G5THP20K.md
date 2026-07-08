---
id: UDG@20.15.2@License@LKV3G5THP20K
type: License
name: 平均速率20kbps的Bearer上下文数
nf: UDG
version: 20.15.2
license_code: LKV3G5THP20K
control_item_id: '82209852'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 平均速率20kbps的Bearer上下文数

`LKV3G5THP20K` · 控制项 82209852 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

平均速率20kbps的Bearer上下文数指整个设备传输用户数据时的单用户的吞吐量。

## 实现描述

当设备上整机流量连续五分钟达到License值 * license指定速率的90%时，产生License资源即将用完告警，告警ID ALM-100046；连续五分钟降到License值* license指定速率的80%时，恢复License资源即将用完告警。<br>当设备上整机流量连续五分钟达到License值* license指定速率时，产生License资源用完告警，告警ID ALM-100049；连续五分钟降到90%时此告警恢复。<br>当设备上整机流量超过License值* license指定速率并产生License用完告警后，设备将限制PDP上下文的接入。<br>该license与“整机吞吐量”、“平均速率50kbps的Bearer上下文数”、“平均速率100kbps的Bearer上下文数”、“平均速率200kbps的Bearer上下文数”、“平均速率500kbps的Bearer上下文数” license不同时存在。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

应用于需要控制单用户吞吐量的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

不涉及

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
