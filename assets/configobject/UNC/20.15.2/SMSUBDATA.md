---
id: UNC@20.15.2@ConfigObject@SMSUBDATA
type: ConfigObject
name: SMSUBDATA（签约数据纠正参数）
nf: UNC
version: 20.15.2
object_name: SMSUBDATA
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SMSUBDATA（签约数据纠正参数）

## 说明

**适用网元：SGSN、MME**

该命令用于增加一条签约数据修改的记录，修改IMSI号段、PDP TYPE、APN匹配的用户群的签约数据类型。使用该命令时建议设置软参DWORD_EX26 BIT13的值为1。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SMSUBDATA]] · ADD SMSUBDATA
- [[command/UNC/20.15.2/LST-SMSUBDATA]] · LST SMSUBDATA
- [[command/UNC/20.15.2/MOD-SMSUBDATA]] · MOD SMSUBDATA
- [[command/UNC/20.15.2/RMV-SMSUBDATA]] · RMV SMSUBDATA

## 证据

- 原始手册：`evidence/UNC/20.15.2/SMSUBDATA.md`
- 原始手册：`evidence/UNC/20.15.2/SMSUBDATA.md`
- 原始手册：`evidence/UNC/20.15.2/SMSUBDATA.md`
- 原始手册：`evidence/UNC/20.15.2/SMSUBDATA.md`
