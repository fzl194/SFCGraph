---
id: UNC@20.15.2@ConfigObject@HSSINFO
type: ConfigObject
name: HSSINFO（HSS信息）
nf: UNC
version: 20.15.2
object_name: HSSINFO
object_kind: action
applicable_nf:
- SGSN
- MME
status: active
---

# HSSINFO（HSS信息）

## 说明

**适用网元：SGSN、MME**

该命令用于模拟HSS RESET流程，将注册在该HSS的用户“SGSN Location Information Confirmed in HLR/HSS”或“MME Location Information Confirmed in HLR/HSS”标识和自学习主机名等与HSS相关的信息置为无效。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-HSSINFO]] · CLR HSSINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/HSSINFO.md`
