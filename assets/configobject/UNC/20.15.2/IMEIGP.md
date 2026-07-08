---
id: UNC@20.15.2@ConfigObject@IMEIGP
type: ConfigObject
name: IMEIGP（IMEI群组）
nf: UNC
version: 20.15.2
object_name: IMEIGP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IMEIGP（IMEI群组）

## 说明

**适用网元：SGSN、MME**

此命令用于增加IMEI群组记录，为IMEI群组成员提供群组标识等信息，以群粒度进行业务策略控制。需要结合 [**ADD IMEIGPMEM**](../IMEI群组成员管理/增加IMEI群组成员(ADD IMEIGPMEM)_26305568.md) 命令配置成员信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IMEIGP]] · ADD IMEIGP
- [[command/UNC/20.15.2/LST-IMEIGP]] · LST IMEIGP
- [[command/UNC/20.15.2/MOD-IMEIGP]] · MOD IMEIGP
- [[command/UNC/20.15.2/RMV-IMEIGP]] · RMV IMEIGP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMEI群组(MOD-IMEIGP)_26305566.md`
- 原始手册：`evidence/UNC/20.15.2/删除IMEI群组(RMV-IMEIGP)_72345357.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMEI群组(ADD-IMEIGP)_72225435.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMEI群组(LST-IMEIGP)_26145758.md`
