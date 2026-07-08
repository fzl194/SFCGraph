---
id: UNC@20.15.2@ConfigObject@ISMFDNAI
type: ConfigObject
name: ISMFDNAI（I-SMF支持的DNAI）
nf: UNC
version: 20.15.2
object_name: ISMFDNAI
object_kind: entity
applicable_nf:
- SMF
status: active
---

# ISMFDNAI（I-SMF支持的DNAI）

## 说明

**适用NF：SMF**

该命令用于增加I-SMF支持的DNAI。I-SMF支持的DNAI有两种类型：DNN级别和整系统级别。DNN级别的DNAI仅对激活该DNN的PDU会话生效。整系统级别DNAI对所有PDU会话均生效。

在I-SMF插入或改变流程中I-SMF会将整系统DNAI以及用户当前会话DNN所关联的DNAI发送给锚点SMF，锚点SMF会在响应消息中将协商出的会话DNAI携带给I-SMF。当用户位置移动时，如果用户在新的区域需要进行UL CL/BP分流，I-SMF会根据从锚点SMF获取的DNAI为用户插入UL CL/BP UPF和辅锚点UPF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ISMFDNAI]] · ADD ISMFDNAI
- [[command/UNC/20.15.2/LST-ISMFDNAI]] · LST ISMFDNAI
- [[command/UNC/20.15.2/MOD-ISMFDNAI]] · MOD ISMFDNAI
- [[command/UNC/20.15.2/RMV-ISMFDNAI]] · RMV ISMFDNAI

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改I-SMF支持的DNAI（MOD-ISMFDNAI）_47720781.md`
- 原始手册：`evidence/UNC/20.15.2/删除I-SMF支持的DNAI（RMV-ISMFDNAI）_47600749.md`
- 原始手册：`evidence/UNC/20.15.2/增加I-SMF支持的DNAI（ADD-ISMFDNAI）_01120970.md`
- 原始手册：`evidence/UNC/20.15.2/查询I-SMF支持的DNAI（LST-ISMFDNAI）_01480778.md`
