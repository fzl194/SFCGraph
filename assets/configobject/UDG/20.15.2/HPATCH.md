---
id: UDG@20.15.2@ConfigObject@HPATCH
type: ConfigObject
name: HPATCH（热补丁）
nf: UDG
version: 20.15.2
object_name: HPATCH
object_kind: entity
status: active
---

# HPATCH（热补丁）

## 说明

该命令用于删除指定网元微服务进程的热补丁。

> **注意**
> 本命令属于高危命令，执行此命令会删除当前网元微服务的所有热补丁，请谨慎使用。如需使用请联系华为支持协助操作。

> **说明**
> - 该命令在执行后立即生效。
> - 网元ID必须在系统中存在。

## 操作本对象的命令

- [DSP HPATCH](command/UDG/20.15.2/DSP-HPATCH.md)
- [RMV HPATCH](command/UDG/20.15.2/RMV-HPATCH.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除热补丁(RMV-HPATCH)_25343986.md`
- 原始手册：`evidence/UDG/20.15.2/查询热补丁信息(DSP-HPATCH)_13558792.md`
