---
id: UNC@20.15.2@ConfigObject@SCCPDPCSHR
type: ConfigObject
name: SCCPDPCSHR（DPC多点负荷分担记录）
nf: UNC
version: 20.15.2
object_name: SCCPDPCSHR
object_kind: entity
applicable_nf:
- SGSN
- MME
- SMSF
status: active
---

# SCCPDPCSHR（DPC多点负荷分担记录）

## 说明

**适用网元：SGSN、MME、SMSF**

此命令用于增加SCCP目的信令点多点负荷分担记录。在SCCP目的信令点表中负荷分担类型为多点负荷分担方式的目的信令点都需要在本表中增加数据。SCCP目的信令点表的相关信息请参考 [**ADD SCCPDPC**](../SCCP目的信令点/增加SCCP目的信令点(ADD SCCPDPC)_26306130.md) 命令。

## 操作本对象的命令

- [ADD SCCPDPCSHR](command/UNC/20.15.2/ADD-SCCPDPCSHR.md)
- [LST SCCPDPCSHR](command/UNC/20.15.2/LST-SCCPDPCSHR.md)
- [RMV SCCPDPCSHR](command/UNC/20.15.2/RMV-SCCPDPCSHR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DPC多点负荷分担记录(RMV-SCCPDPCSHR)_72345923.md`
- 原始手册：`evidence/UNC/20.15.2/增加DPC多点负荷分担记录(ADD-SCCPDPCSHR)_26306134.md`
- 原始手册：`evidence/UNC/20.15.2/查询DPC多点负荷分担记录(LST-SCCPDPCSHR)_26146324.md`
