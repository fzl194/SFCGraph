---
id: UDG@20.15.2@License@LKV3G5STQE01
type: License
name: 业务触发的QoS保证
nf: UDG
version: 20.15.2
license_code: LKV3G5STQE01
control_item_id: 82200AFP
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# 业务触发的QoS保证

`LKV3G5STQE01` · 控制项 82200AFP · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

业务触发的QoS保证是指用户请求了需要特定QoS保障的业务时，<br>UDG<br>根据PGW-C/SMF下发的PCC预定义规则为用户建立专有承载/专有QoS Flow的功能。

## 实现描述

EPC/5GC网络以EPS承载/QoS Flow为粒度进行QoS控制，即映射到同一个EPS承载/QoS Flow的业务流使用同一级别的报文转发机制（如调度策略、队列管理策略、速率整形策略等）。当需要提供不同的报文转发机制时，需要使用不同的EPS承载/QoS Flow。<br>当用户请求的业务数据流到达时，PGW-U/UPF基于匹配的预定义规则向PGW-C/SMF上报QoS事件，PGW-C/SMF基于QoS策略发起专有承载激活/专有QoS Flow建立流程。专有承载激活/专有QoS Flow建立成功后，用户即可在特定的QoS保证下进行请求的数据业务。<br>当用户请求的业务数据流到达时，PGW-U/UPF基于匹配的预定义规则向PGW-C/SMF上报QoS事件，PGW-C/SMF基于QoS策略（QoS参数变更时）发起专有承载更新/专有QoS Flow更新流程。<br>当用户长时间未访问业务时，PGW-U/UPF会向PGW-C/SMF上报QoS事件，从而删除相关承载/QoS Flow。专有承载/专有QoS Flow去激活成功后，用户即不能使用该数据业务。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

当用户访问的业务需要特定的QoS保障时，<br>UDG<br>根据PGW-C/SMF下发的预定义规则触发专有承载/专有QoS Flow的创建，以满足业务需要。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- PCC基本功能

## 对应特性（原文）

GWFD-020358 业务触发的QoS保证

## 控制的能力

- [GWFD-020358](feature/UDG/20.15.2/GWFD-020358.md)  — 控制项 82200AFP

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
