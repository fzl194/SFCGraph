---
id: UNC@20.15.2@ConfigObject@SCCPDPC
type: ConfigObject
name: SCCPDPC（SCCP目的信令点）
nf: UNC
version: 20.15.2
object_name: SCCPDPC
object_kind: entity
applicable_nf:
- SGSN
- MME
- SMSF
status: active
---

# SCCPDPC（SCCP目的信令点）

## 说明

**适用网元：SGSN、MME、SMSF**

此命令用于增加SCCP目的信令点。

与本局信令点有SCCP消息交互的信令点都需要在本表中增加数据。

## 操作本对象的命令

- [ADD SCCPDPC](command/UNC/20.15.2/ADD-SCCPDPC.md)
- [DSP SCCPDPC](command/UNC/20.15.2/DSP-SCCPDPC.md)
- [INH SCCPDPC](command/UNC/20.15.2/INH-SCCPDPC.md)
- [LST SCCPDPC](command/UNC/20.15.2/LST-SCCPDPC.md)
- [MOD SCCPDPC](command/UNC/20.15.2/MOD-SCCPDPC.md)
- [RMV SCCPDPC](command/UNC/20.15.2/RMV-SCCPDPC.md)
- [UIN SCCPDPC](command/UNC/20.15.2/UIN-SCCPDPC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCCP目的信令点(MOD-SCCPDPC)_26146320.md`
- 原始手册：`evidence/UNC/20.15.2/删除SCCP目的信令点(RMV-SCCPDPC)_72345919.md`
- 原始手册：`evidence/UNC/20.15.2/增加SCCP目的信令点(ADD-SCCPDPC)_26306130.md`
- 原始手册：`evidence/UNC/20.15.2/显示SCCP目的信令点状态(DSP-SCCPDPC)_26306132.md`
- 原始手册：`evidence/UNC/20.15.2/查询SCCP目的信令点(LST-SCCPDPC)_72225999.md`
- 原始手册：`evidence/UNC/20.15.2/禁止SCCP目的信令点(INH-SCCPDPC)_72345921.md`
- 原始手册：`evidence/UNC/20.15.2/解禁SCCP目的信令点(UIN-SCCPDPC)_26146322.md`
