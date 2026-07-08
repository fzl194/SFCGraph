---
id: UDG@20.15.2@License@LKV3G5CUFM01
type: License
name: CU Full Mesh组网
nf: UDG
version: 20.15.2
license_code: LKV3G5CUFM01
control_item_id: '82209861'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# CU Full Mesh组网

`LKV3G5CUFM01` · 控制项 82209861 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

UDG<br>支持CU Full Mesh功能，对允许偶联的最大连接数进行限制，一旦超过该数量限制，将不再允许新的SMF接入。

## 实现描述

CU Full Mesh组网License数大于0时，<br>UDG<br>允许与SMF建立偶联，每与一个SMF建立连接，License使用量加一，偶联释放后，License使用量减一。当使用量达到或超过申请的License数时，依据License控制原则，对新接入的SMF进行限制，不再允许新的SMF接入。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

针对多SMF接入场景，可通过该License控制可连接的最大SMF数，避免因为偶联数过多导致的用户资源和网络通讯负载过高。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020161 CU Full Mesh组网

## 控制的能力

- [GWFD-020161](feature/UDG/20.15.2/GWFD-020161.md)  — 控制项 82209861

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
