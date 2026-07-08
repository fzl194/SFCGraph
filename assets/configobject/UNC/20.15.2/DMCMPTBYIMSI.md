---
id: UNC@20.15.2@ConfigObject@DMCMPTBYIMSI
type: ConfigObject
name: DMCMPTBYIMSI（IMSI对应的Diameter兼容性）
nf: UNC
version: 20.15.2
object_name: DMCMPTBYIMSI
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMCMPTBYIMSI（IMSI对应的Diameter兼容性）

## 说明

**适用网元：SGSN、MME**

该命令用于设置Diameter兼容性参数，用于保证网元间支持信元的兼容性。

该命令支持针对外网用户、本网用户、IMSI号段来配置兼容性参数。

## 操作本对象的命令

- [ADD DMCMPTBYIMSI](command/UNC/20.15.2/ADD-DMCMPTBYIMSI.md)
- [LST DMCMPTBYIMSI](command/UNC/20.15.2/LST-DMCMPTBYIMSI.md)
- [MOD DMCMPTBYIMSI](command/UNC/20.15.2/MOD-DMCMPTBYIMSI.md)
- [RMV DMCMPTBYIMSI](command/UNC/20.15.2/RMV-DMCMPTBYIMSI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMSI对应的Diameter兼容性(MOD-DMCMPTBYIMSI)_26306110.md`
- 原始手册：`evidence/UNC/20.15.2/删除IMSI对应的Diameter兼容性(RMV-DMCMPTBYIMSI)_72345899.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMSI对应的Diameter兼容性(ADD-DMCMPTBYIMSI)_72225977.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMSI对应的Diameter兼容性(LST-DMCMPTBYIMSI)_26146300.md`
