---
id: UNC@20.15.2@ConfigObject@DMFOVERCODE
type: ConfigObject
name: DMFOVERCODE（触发重选路由的错误码）
nf: UNC
version: 20.15.2
object_name: DMFOVERCODE
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMFOVERCODE（触发重选路由的错误码）

## 说明

**适用网元：SGSN、MME**

该命令用于配置Diameter链路上会触发重选路由的错误码。使用 [**SET DMFUNC**](../Diameter参数/设置Diameter配置(SET DMFUNC)_72225949.md) 命令打开 “重选路由功能开关” （ **SET DMFUNC: FAILOVER=YES;** ），启用重选路由功能后，若系统收到对端响应的错误码和本命令配置的错误码匹配，则会重新选择其他Diameter路由。若未配置该错误码，则不会重选路由。

## 操作本对象的命令

- [ADD DMFOVERCODE](command/UNC/20.15.2/ADD-DMFOVERCODE.md)
- [LST DMFOVERCODE](command/UNC/20.15.2/LST-DMFOVERCODE.md)
- [RMV DMFOVERCODE](command/UNC/20.15.2/RMV-DMFOVERCODE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除触发重选路由的错误码(RMV-DMFOVERCODE)_72225973.md`
- 原始手册：`evidence/UNC/20.15.2/增加触发重选路由的错误码(ADD-DMFOVERCODE)_26146294.md`
- 原始手册：`evidence/UNC/20.15.2/查询触发重选路由的错误码(LST-DMFOVERCODE)_26306106.md`
