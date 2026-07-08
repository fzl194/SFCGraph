---
id: UDG@20.15.2@License@LKV4NATBSS01
type: License
name: NAT基本功能(Mbps)
nf: UDG
version: 20.15.2
license_code: LKV4NATBSS01
control_item_id: 82200DAB
license_domain: VAS
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# NAT基本功能(Mbps)

`LKV4NATBSS01` · 控制项 82200DAB · resource · 域 VAS

## 归属/适用NF（原文）

UPF

## 功能描述

NAT（Network Address Translation），即网络地址转换，可以帮助运营商将用户的私网IP转化为公网IP，实现用户业务访问，同时提供攻击防范功能，保障运营商及用户的正常业务不受网络攻击影响。

## 实现描述

当NAT上总流量连续五分钟达到License值的90%时，产生ALM-100046 资源达到LICENSE扩容门限告警；连续五分钟降到License值的80%时，恢复License资源即将用完告警。<br>当NAT一年内出现第十次业务高峰期（DSP LICENSEPEAK查询结果有10条记录），且NAT上总流量大于License值时，产生ALM-100049 资源达到LICENSE限制值告警；连续五分钟小于License值时，此告警恢复。

## 取值范围

0~8000000

## 默认值

10

## 应用场景

为了解决运营商的私网用户无法上网的问题，<br>UDG<br>集成NAT功能帮助运营商私网用户进行源地址转换，实现网络访问。同时保护用户正常上网，避免受到恶意攻击。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_24575797.md`
