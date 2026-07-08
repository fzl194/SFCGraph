---
id: UDG@20.15.2@License@LKV3G5MPLS01
type: License
name: MPLS VPN
nf: UDG
version: 20.15.2
license_code: LKV3G5MPLS01
control_item_id: 82200AFQ
license_domain: UDG
control_item_type: resource
applicable_nf:
- PGW-U
- UPF
status: active
---

# MPLS VPN

`LKV3G5MPLS01` · 控制项 82200AFQ · resource · 域 UDG

## 归属/适用NF（原文）

PGW-U、UPF

## 功能描述

BGP/MPLS IP VPN是一种L3VPN（Layer 3 Virtual Private Network）。它使用BGP（Border Gateway Protocol）在服务提供商骨干网上发布VPN路由，使用MPLS（Multiprotocol Label Switch）在服务提供商骨干网上转发VPN报文。这里的IP是指是服务提供商骨干网络是IP网络。

## 实现描述

系统中每激活一个MPLS VPN的PDP上下文，支持MPLS VPN功能PDP上下文数的总数加一；每去激活一个MPLS VPN的PDP上下文，支持MPLS VPN功能PDP上下文数的总数减一。<br>如果系统中已接入的支持MPLS VPN功能的PDP上下文数达到License中“MPLS VPN ”的最大值，无法激活新的MPLS VPN用户。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

- 运营商部署分组交换网，当UDG与其他网元通过Router/Switch/Firewall连接时，为保证更为可靠的传输，可以在相应的接口配置BFD会话。<br>- 当链路中间存在传输设备时，由于实际物理线路分段，一旦链路故障，两端设备需要比较长的时间才能检测到，导致直连路由失效慢，网络中断时间长。如果采用BFD检测，使BFD的会话状态能够影响接口的协议状态变化，就能触发路由快速收敛。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020411 MPLS VPN

## 控制的能力

- [GWFD-020411](feature/UDG/20.15.2/GWFD-020411.md)  — 控制项 82200AFQ

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
