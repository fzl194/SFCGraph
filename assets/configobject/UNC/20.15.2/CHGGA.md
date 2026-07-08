---
id: UNC@20.15.2@ConfigObject@CHGGA
type: ConfigObject
name: CHGGA（计费Ga接口参数状态）
nf: UNC
version: 20.15.2
object_name: CHGGA
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# CHGGA（计费Ga接口参数状态）

## 说明

![](设置计费Ga接口参数(SET CHGGA)_26145378.assets/notice_3.0-zh-cn_2.png)

计费参数的错误修改可能导致计费中心无法正确计费，需谨慎修改。 本命令部分参数的修改需要复位CDP才能生效，部分参数需要复位SPP和GTP才能生效，详细请参见命令联机帮助。

**适用网元：SGSN**

该命令用于设置计费Ga接口参数，包括SGSN生成话单的协议版本等参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-CHGGA]] · DSP CHGGA
- [[command/UNC/20.15.2/LST-CHGGA]] · LST CHGGA
- [[command/UNC/20.15.2/SET-CHGGA]] · SET CHGGA

## 证据

- 原始手册：`evidence/UNC/20.15.2/CHGGA.md`
- 原始手册：`evidence/UNC/20.15.2/CHGGA.md`
- 原始手册：`evidence/UNC/20.15.2/CHGGA.md`
