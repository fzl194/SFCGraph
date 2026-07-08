---
id: UDG@20.15.2@License@LKV4EN4SCY01
type: License
name: 内置安全增强(Mbps)
nf: UDG
version: 20.15.2
license_code: LKV4EN4SCY01
control_item_id: 82200EYC
license_domain: VAS
control_item_type: resource
applicable_nf:
- UPF
status: active
---

# 内置安全增强(Mbps)

`LKV4EN4SCY01` · 控制项 82200EYC · resource · 域 VAS

## 归属/适用NF（原文）

UPF

## 功能描述

内置安全增强提供安全防护功能，为经过NAT设备的流量提供防DDOS、单包攻击、报文过滤等安全保护能力。

## 实现描述

当NAT上做安全防护的总流量连续五分钟达到License值的80%时，产生ALM-100046 资源达到LICENSE扩容门限告警；连续五分钟降到License值的70%时，恢复License资源即将用完告警。

## 取值范围

0~8000000

## 默认值

10

## 应用场景

当UPF位于边缘站点，连接无线移动用户、本地园区网络、第三方APP网络时，可以通过内置NAT，向UPF多种部署形态组网提供状态防火墙、多安全域路由转发能力。

## 相关控制项（原文，未解释为边）

NAT基本功能(Mbps)

## 对应特性（原文）

无

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_24575797.md`
