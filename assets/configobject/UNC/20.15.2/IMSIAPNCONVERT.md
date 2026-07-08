---
id: UNC@20.15.2@ConfigObject@IMSIAPNCONVERT
type: ConfigObject
name: IMSIAPNCONVERT（APNNI转换配置）
nf: UNC
version: 20.15.2
object_name: IMSIAPNCONVERT
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IMSIAPNCONVERT（APNNI转换配置）

## 说明

**适用网元：SGSN、MME**

该命令用于增加别名APN（Access Point Name）转换配置。如果用户激活请求消息中携带的APN和本配置命令“OLDAPN（请求APNNI）”匹配，则用户激活请求消息中携带的APN将被替换为“NEWAPN（转换APNNI）”后再进行签约数据匹配。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IMSIAPNCONVERT]] · ADD IMSIAPNCONVERT
- [[command/UNC/20.15.2/LST-IMSIAPNCONVERT]] · LST IMSIAPNCONVERT
- [[command/UNC/20.15.2/MOD-IMSIAPNCONVERT]] · MOD IMSIAPNCONVERT
- [[command/UNC/20.15.2/RMV-IMSIAPNCONVERT]] · RMV IMSIAPNCONVERT

## 证据

- 原始手册：`evidence/UNC/20.15.2/IMSIAPNCONVERT.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIAPNCONVERT.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIAPNCONVERT.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIAPNCONVERT.md`
