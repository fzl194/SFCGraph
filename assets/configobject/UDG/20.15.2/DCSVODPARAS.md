---
id: UDG@20.15.2@ConfigObject@DCSVODPARAS
type: ConfigObject
name: DCSVODPARAS（DCS点播参数）
nf: UDG
version: 20.15.2
object_name: DCSVODPARAS
object_kind: global_setting
status: active
---

# DCSVODPARAS（DCS点播参数）

## 说明

该命令用于设置DCS点播参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | HOTUPDATEFREQ | SYSMAXHOTNESS | HOTDECAYRATE | L0ADDHOTTHRES | L2MAXDISKSIZE | DISKSTARTAGING | DISKAGINGSIZE | METASTARTAGING | METAAGINGSIZE | OBJAGINGPERD |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | 100 | 20000 | 50 | 95 | 14336 | 500 | 300 | 95 | 2000 | 168 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DCSVODPARAS]] · LST DCSVODPARAS
- [[command/UDG/20.15.2/SET-DCSVODPARAS]] · SET DCSVODPARAS

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DCS点播参数（LST-DCSVODPARAS）_11535957.md`
- 原始手册：`evidence/UDG/20.15.2/设置DCS点播参数（SET-DCSVODPARAS）_76289646.md`
