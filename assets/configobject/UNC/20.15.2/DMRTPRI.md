---
id: UNC@20.15.2@ConfigObject@DMRTPRI
type: ConfigObject
name: DMRTPRI（Diameter域路由优先级权重）
nf: UNC
version: 20.15.2
object_name: DMRTPRI
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMRTPRI（Diameter域路由优先级权重）

## 说明

**适用网元：SGSN、MME**

该命令用于修改Diameter域路由优先级和权重，当Diameter域路由配置中 “选路模式” 是 “SELMODE_MASTER_SLAVE(主从)” 、 “SELMODE_PRIORITY_WEIGHT(优先级权重)” 或者 “SELMODE_IMSI_PRIORITY(IMSI指定优选)” 时，修改域路由中的对端优先级。当Diameter域路由配置中 “选路模式” 是 “SELMODE_PRIORITY_WEIGHT(优先级权重)” 时，修改域路由中的对端权重。

## 操作本对象的命令

- [LST DMRTPRI](command/UNC/20.15.2/LST-DMRTPRI.md)
- [MOD DMRTPRI](command/UNC/20.15.2/MOD-DMRTPRI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter域路由优先级权重(MOD-DMRTPRI)_72345887.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter域路由优先级权重(LST-DMRTPRI)_26146288.md`
