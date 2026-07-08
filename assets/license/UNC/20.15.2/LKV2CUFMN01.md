---
id: UNC@20.15.2@License@LKV2CUFMN01
type: License
name: CU FullMesh组网
nf: UNC
version: 20.15.2
license_code: LKV2CUFMN01
control_item_id: '82209930'
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# CU FullMesh组网

`LKV2CUFMN01` · 控制项 82209930 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

Full Mesh组网包括SMF/UPF Full Mesh、PGW-C/PGW-U Full Mesh、GGSN-C/GGSN-U Full Mesh组网。<br>- SMF/UPF Full Mesh组网是指SMF与UPF支持多对多组网，也就是一个SMF支持对接多个UPF，一个UPF也支持对接多个SMF，这样无论是SMF故障还是UPF故障，都不影响其余设备正常工作的。<br>- PGW-C/PGW-U Full Mesh组网是指PGW-C与PGW-U支持多对多组网，也就是一个PGW-C支持对接多个PGW-U，一个PGW-U也支持对接多个PGW-C，这样无论是PGW-C故障还是PGW-U故障，都不影响其余设备正常工作的。<br>- GGSN-C/GGSN-U Full Mesh组网是指GGSN-C与GGSN-U支持多对多组网，也就是一个GGSN-C支持对接多个GGSN-U，一个GGSN-U也支持对接多个GGSN-C，这样无论是GGSN-C故障还是GGSN-U故障，都不影响其余设备正常工作的。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

需要提高网络可靠性，减少冗余资源时，可参考本功能进行组网部署。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-213001 CU FullMesh组网

## 控制的能力

- [WSFD-213001](feature/UNC/20.15.2/WSFD-213001.md)  — 控制项 82209930
- [WSFD-225002](feature/UNC/20.15.2/WSFD-225002.md)  — 控制项 82209930

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63967933.md`
