---
id: UNC@20.15.2@ConfigObject@APNPOLICYMODE
type: ConfigObject
name: APNPOLICYMODE（基于APN的策略接口的选择方式）
nf: UNC
version: 20.15.2
object_name: APNPOLICYMODE
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# APNPOLICYMODE（基于APN的策略接口的选择方式）

## 说明

![](增加基于APN的策略接口的选择方式（ADD APNPOLICYMODE）_72001541.assets/notice_3.0-zh-cn_2.png)

配置基于APN的策略接口的选择方式不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加基于APN的策略接口的选择方式。

## 操作本对象的命令

- [ADD APNPOLICYMODE](command/UNC/20.15.2/ADD-APNPOLICYMODE.md)
- [LST APNPOLICYMODE](command/UNC/20.15.2/LST-APNPOLICYMODE.md)
- [MOD APNPOLICYMODE](command/UNC/20.15.2/MOD-APNPOLICYMODE.md)
- [RMV APNPOLICYMODE](command/UNC/20.15.2/RMV-APNPOLICYMODE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于APN的策略接口的选择方式（MOD-APNPOLICYMODE）_96242548.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于APN的策略接口的选择方式（RMV-APNPOLICYMODE）_96242744.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于APN的策略接口的选择方式（ADD-APNPOLICYMODE）_72001541.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于APN的策略接口的选择方式（LST-APNPOLICYMODE）_96242078.md`
