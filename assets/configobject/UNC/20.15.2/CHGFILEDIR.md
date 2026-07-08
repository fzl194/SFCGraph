---
id: UNC@20.15.2@ConfigObject@CHGFILEDIR
type: ConfigObject
name: CHGFILEDIR（切换话单文件的工作目录）
nf: UNC
version: 20.15.2
object_name: CHGFILEDIR
object_kind: action
applicable_nf:
- SGSN
status: active
---

# CHGFILEDIR（切换话单文件的工作目录）

## 说明

**适用网元：SGSN**

该命令用于切换话单文件的工作目录。用户的话单文件被保存在磁盘的CDR目录下，该目录下有CDR1和CDR2两个子目录，其中一个子目录是工作目录，无法发往CG的话单将被写入该工作目录下的话单文件。为了防止话单文件的操作冲突，工作目录下的话单文件不能进行导入导出操作。因此用户需要对磁盘上的话单文件进行导入导出操作前，需要通过 [**DSP CHGFILEDIR**](显示话单文件的工作目录(DSP CHGFILEDIR)_26145362.md) 命令查询希望进行导入导出操作的目录是否属于工作目录，如果是，需要执行本命令切换话单文件的工作目录，然后再针对非工作目录执行话单文件的导入导出操作。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-CHGFILEDIR]] · DSP CHGFILEDIR
- [[command/UNC/20.15.2/SWP-CHGFILEDIR]] · SWP CHGFILEDIR

## 证据

- 原始手册：`evidence/UNC/20.15.2/CHGFILEDIR.md`
- 原始手册：`evidence/UNC/20.15.2/CHGFILEDIR.md`
