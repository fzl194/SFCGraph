---
id: UNC@20.15.2@ConfigObject@SGSNDNS
type: ConfigObject
name: SGSNDNS（SGSN DNS域名策略）
nf: UNC
version: 20.15.2
object_name: SGSNDNS
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SGSNDNS（SGSN DNS域名策略）

## 说明

**适用网元：SGSN、MME**

该命令用于增加SGSN DNS域名策略配置，即设置在Inter Attach/RAU/Suspend/Relocation流程中，MME或SGSN选择对端SGSN所采用的域名格式。

## 操作本对象的命令

- [ADD SGSNDNS](command/UNC/20.15.2/ADD-SGSNDNS.md)
- [LST SGSNDNS](command/UNC/20.15.2/LST-SGSNDNS.md)
- [MOD SGSNDNS](command/UNC/20.15.2/MOD-SGSNDNS.md)
- [RMV SGSNDNS](command/UNC/20.15.2/RMV-SGSNDNS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SGSN-DNS域名策略(MOD-SGSNDNS)_26305772.md`
- 原始手册：`evidence/UNC/20.15.2/删除SGSN-DNS域名策略(RMV-SGSNDNS)_72225641.md`
- 原始手册：`evidence/UNC/20.15.2/增加SGSN-DNS域名策略(ADD-SGSNDNS)_26145962.md`
- 原始手册：`evidence/UNC/20.15.2/查询SGSN-DNS域名策略(LST-SGSNDNS)_72345563.md`
