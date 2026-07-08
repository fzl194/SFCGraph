---
id: UDG@20.15.2@ConfigObject@MEASRST
type: ConfigObject
name: MEASRST（测量结果文件）
nf: UDG
version: 20.15.2
object_name: MEASRST
object_kind: action
status: active
---

# MEASRST（测量结果文件）

## 说明

该命令用于导出网元的测量结果文件。

> **说明**
> 该命令最多支持同时下发4个并发导出任务，建议不同的任务导出到不同的目标目录下。
>
> 如果下发的并发任务存在导出相同名称的话统结果文件，且目标目录相同，会出现并发任务之间上传文件冲突，只有最后一个任务可全部导出成功，其他任务可能呈现部分文件导出失败。
>
> 在升级场景下，为兼容低版本需要，系统会在对接SFTP时针对安全算法使用兼容方式处理。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-MEASRST]] · DSP MEASRST
- [[command/UDG/20.15.2/EXP-MEASRST]] · EXP MEASRST
- [[command/UDG/20.15.2/LST-MEASRST]] · LST MEASRST

## 证据

- 原始手册：`evidence/UDG/20.15.2/MEASRST.md`
- 原始手册：`evidence/UDG/20.15.2/MEASRST.md`
- 原始手册：`evidence/UDG/20.15.2/MEASRST.md`
