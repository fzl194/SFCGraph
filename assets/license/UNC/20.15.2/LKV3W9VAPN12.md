---
id: UNC@20.15.2@License@LKV3W9VAPN12
type: License
name: 虚拟APN
nf: UNC
version: 20.15.2
license_code: LKV3W9VAPN12
control_item_id: '82207939'
applicable_nf:
- GGSN-C
- SGW-C
- PGW-C
- SMF
status: active
---

# 虚拟APN

`LKV3W9VAPN12` · 控制项 82207939 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、SGW-C、PGW-C、SMF

## 功能描述

为了降低用户使用分组业务的难度，同时减少移动运营商网络管理的复杂度和成本，需要寻找一种能够让用户通过一个APN可以访问所有业务的方法，这就是虚拟APN（Virtual APN）技术。<br>用户请求的不同业务接入不同的网络，最终是通过APN来区分的。因此虚拟APN作为<br>UNC<br>的一个重要功能，就是要求能对使用虚拟APN激活的用户，能根据用户实际的签约和业务请求情况，映射到真实的APN，<br>UNC<br>根据真实APN进行相应的激活和接入网络的鉴权认证处理，并将数据包转发到相应的网络。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

该特性主要应用于以下场景中：<br>- 终端上都设置为一个APN，但是运营商需要对不同的终端属性提供不同的业务，如果通知用户在使用不同业务的时候更改配置，对于用户和运营商来说，操作和管理复杂。<br>- EPC网络中，虚拟APN只是对用户、MME、HSS、DNS来说是虚拟APN，PGW-C使用真实APN。对于采用虚拟APN激活但是进行不同业务的用户，PGW-C可以为其分配不同的资源：在不同的地址池中分配地址，进行不同的鉴权认证方式，依据业务进行相应的QoS协商，分配不同的DNS资源等。<br>- 5G网络中，虚拟APN只是对用户、AMF、UDM、DNS来说是虚拟APN，SMF使用真实APN。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-205102 虚拟APN

## 控制的能力

- [WSFD-205102](feature/UNC/20.15.2/WSFD-205102.md)  — 控制项 82207939

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
