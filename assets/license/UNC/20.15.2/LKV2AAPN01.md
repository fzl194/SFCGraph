---
id: UNC@20.15.2@License@LKV2AAPN01
type: License
name: 别名APN-USM
nf: UNC
version: 20.15.2
license_code: LKV2AAPN01
control_item_id: 82200BNM
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# 别名APN-USM

`LKV2AAPN01` · 控制项 82200BNM ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

为了兼容现网中存在使用相同资源的多个APN，提出别名APN的概念。当运营商需要将不同APN的业务都映射到同一APN上或者将某一APN的业务映射到另一APN上时，只需要在<br>UNC<br>上配置APN别名映射，就可以将用户侧传来的APN作为别名APN映射到真实APN上，这样不同的APN可以共用相同的系统资源，从而便于系统资源的分配组合。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

别名APN的应用场景多为：<br>终端上的APN设置多种多样，而运营商对这些终端提供相同的APN业务。如果在<br>UNC<br>上配置众多的APN或者通知用户更改配置，都将提高运营成本。<br>通过别名APN功能，将所有已知的APN都映射为同一个APN进行业务，这样不同的APN可以共用相同的系统资源，从而便于系统资源的分配组合。<br>别名APN主要适用于以下两种场景：<br>- 运营商合并和重组时，为了兼容现网中使用相同资源的多个APN，可将某APN的业务映射到另一APN上。<br>- 网络改建时新规划了APN，为了不影响原规划APN的使用，只需将原规划的APN映射到新规划APN上即可。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-106203 别名APN

## 控制的能力

- [WSFD-106203](feature/UNC/20.15.2/WSFD-106203.md)  — 控制项 82200BNM

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
