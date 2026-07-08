---
id: UNC@20.15.2@ConfigObject@PCSCFRESTOPLCY
type: ConfigObject
name: PCSCFRESTOPLCY（P-CSCF故障恢复策略）
nf: UNC
version: 20.15.2
object_name: PCSCFRESTOPLCY
object_kind: entity
applicable_nf:
- MME
status: active
---

# PCSCFRESTOPLCY（P-CSCF故障恢复策略）

## 说明

**适用网元：MME**

该命令用于增加P-CSCF故障恢复策略配置。

该命令的使用场景：当P-CSCF故障时，可以设置该命令通过承载更新流程刷新故障的P-CSCF，减少IMS会话重建。

## 操作本对象的命令

- [ADD PCSCFRESTOPLCY](command/UNC/20.15.2/ADD-PCSCFRESTOPLCY.md)
- [LST PCSCFRESTOPLCY](command/UNC/20.15.2/LST-PCSCFRESTOPLCY.md)
- [MOD PCSCFRESTOPLCY](command/UNC/20.15.2/MOD-PCSCFRESTOPLCY.md)
- [RMV PCSCFRESTOPLCY](command/UNC/20.15.2/RMV-PCSCFRESTOPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改P-CSCF故障恢复策略(MOD-PCSCFRESTOPLCY)_40761873.md`
- 原始手册：`evidence/UNC/20.15.2/删除P-CSCF故障恢复策略(RMV-PCSCFRESTOPLCY)_05162794.md`
- 原始手册：`evidence/UNC/20.15.2/增加P-CSCF故障恢复策略(ADD-PCSCFRESTOPLCY)_40921453.md`
- 原始手册：`evidence/UNC/20.15.2/查询P-CSCF故障恢复策略(LST-PCSCFRESTOPLCY)_05322582.md`
