---
id: UNC@20.15.2@ConfigObject@RESTOUSRCTXNUM
type: ConfigObject
name: RESTOUSRCTXNUM（容灾用户数）
nf: UNC
version: 20.15.2
object_name: RESTOUSRCTXNUM
object_kind: query_target
applicable_nf:
- MME
status: active
---

# RESTOUSRCTXNUM（容灾用户数）

## 说明

**适用网元：MME**

本命令用于查询系统内备份用户的数量。查询输出结果为查询时刻的备份用户数量。

输出结果分为2个报告，1个报表显示对应RU名称、进程的备份用户数；1个报表显示系统内总的备份用户数。

## 操作本对象的命令

- [DSP RESTOUSRCTXNUM](command/UNC/20.15.2/DSP-RESTOUSRCTXNUM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示容灾用户数(DSP-RESTOUSRCTXNUM)_72345719.md`
