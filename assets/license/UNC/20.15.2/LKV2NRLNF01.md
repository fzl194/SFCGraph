---
id: UNC@20.15.2@License@LKV2NRLNF01
type: License
name: NRF分层组网
nf: UNC
version: 20.15.2
license_code: LKV2NRLNF01
control_item_id: '81203251'
applicable_nf:
- NRF
status: active
---

# NRF分层组网

`LKV2NRLNF01` · 控制项 81203251 ·  · 域 

## 归属/适用NF（原文）

NRF

## 功能描述

NRF分层网络中，跨NRF的服务发现、订阅/通知、Token请求涉及递归查询和，迭代查询：<br>- 通过递归查询，请求方NF所属NRF逐级向上级NRF发起请求，直到最终得到所需的NF/NFS列表。<br>- 通过迭代查询，NRF查询出目标NRF后，指示前一级NRF直接向目标NRF发起请求。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～1

## 默认值

1

## 应用场景

低层NRF首次上线提供网络服务时，需要先向高层NRF注册。<br>低层NRF优雅下电时，需要向其归属的上一层NRF去注册。<br>若已注册的低层NRF Profile发生变化，如NRF通过软件升级的方式更新能力等，则此时低层NRF会向其注册的高层NRF发起更新。<br>递归查询跨度小，且不要求高层NRF有处理<br>[重定向](../../../../UNC特性指南/网络自治功能/WSFD-214000 NRF分层组网/WSFD-214005 支持NF迭代查询_67546535.md#ZH-CN_TOPIC_0167546535__li135965455288)<br>功能，当运营商网络中NRF不具备处理<br>[重定向](../../../../UNC特性指南/网络自治功能/WSFD-214000 NRF分层组网/WSFD-214005 支持NF迭代查询_67546535.md#ZH-CN_TOPIC_0167546535__li135965455288)<br>功能或希望对高层NRF性能影响较小时，建议采用递归查询方式。<br>迭代查询要求高层sNRF具备处理<br>[重定向](../../../../UNC特性指南/网络自治功能/WSFD-214000 NRF分层组网/WSFD-214005 支持NF迭代查询_67546535.md#ZH-CN_TOPIC_0167546535__li135965455288)<br>功能，迭代查询的查询结果可以缓存，更适用于多次相同NF服务发现的场景。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

- WSFD-214001 支持L-NRF注册<br>- WSFD-214002 支持L-NRF去注册<br>- WSFD-214003 支持L-NRF更新<br>- WSFD-214004 支持NF递归查询<br>- WSFD-214005 支持NF迭代查询

## 控制的能力

- [WSFD-214001](feature/UNC/20.15.2/WSFD-214001.md)  — 控制项 81203251
- [WSFD-214002](feature/UNC/20.15.2/WSFD-214002.md)  — 控制项 81203251
- [WSFD-214003](feature/UNC/20.15.2/WSFD-214003.md)  — 控制项 81203251
- [WSFD-214004](feature/UNC/20.15.2/WSFD-214004.md)  — 控制项 81203251
- [WSFD-214005](feature/UNC/20.15.2/WSFD-214005.md)  — 控制项 81203251

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15408078.md`
