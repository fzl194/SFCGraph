---
id: UDG@20.15.2@License@LKV3G5VDSA01
type: License
name: IPv4v6双栈接入
nf: UDG
version: 20.15.2
license_code: LKV3G5VDSA01
control_item_id: '82209829'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# IPv4v6双栈接入

`LKV3G5VDSA01` · 控制项 82209829 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

IPv6是解决IPv4地址耗尽问题的根本解决方案，但是由于现有IPv4用户存量很大，现网大部分还不支持IPv6应用，使得现网从IPv4向IPv6演进的难度较大。为了保证用户和业务平稳过渡，预计整个演进周期将是个长期的过程，也就是说IPv6将会与IPv4长期共存。双栈是IPv6过渡的基础，当网络演进到后期，终端和业务大部分都是IPv6的时候，可以逐步关闭IPv4，只给用户分配IPv6地址，以此实现现网向IPv6的平滑演进，能够充分保护运营商现网的投资。

## 实现描述

系统中每激活一个IPv4v6双栈PDP上下文，IPv4v6双栈PDP上下文数加一；每去激活一个IPv4v6双栈PDP上下文，IPv4v6双栈PDP上下文数减一。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

UDG<br>网元中IPv4v6 双栈PDP上下文接入。

## 相关控制项（原文，未解释为边）

N6/Gi/SGi接口IPv6组网

## 对应特性（原文）

GWFD-020403 IPv4v6双栈接入

## 控制的能力

- [GWFD-020403](feature/UDG/20.15.2/GWFD-020403.md)  — 控制项 82209829

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
