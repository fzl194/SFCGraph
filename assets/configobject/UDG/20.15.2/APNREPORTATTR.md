---
id: UDG@20.15.2@ConfigObject@APNREPORTATTR
type: ConfigObject
name: APNREPORTATTR（ApnReportAttr配置）
nf: UDG
version: 20.15.2
object_name: APNREPORTATTR
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# APNREPORTATTR（ApnReportAttr配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置性能统计使用的APN类型、头增强使用的APN类型、业务报表使用的APN类型以及支持拥塞控制的APN类型。修改此命令的perf统计APN之前，先去活原来的APN下的所有用户。

## 操作本对象的命令

- [LST APNREPORTATTR](command/UDG/20.15.2/LST-APNREPORTATTR.md)
- [SET APNREPORTATTR](command/UDG/20.15.2/SET-APNREPORTATTR.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ApnReportAttr配置（LST-APNREPORTATTR）_16615230.md`
- 原始手册：`evidence/UDG/20.15.2/设置ApnReportAttr配置（SET-APNREPORTATTR）_16615169.md`
