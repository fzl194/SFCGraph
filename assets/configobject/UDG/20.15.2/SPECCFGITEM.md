---
id: UDG@20.15.2@ConfigObject@SPECCFGITEM
type: ConfigObject
name: SPECCFGITEM（产品内部需要调整规格比例的项目）
nf: UDG
version: 20.15.2
object_name: SPECCFGITEM
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SPECCFGITEM（产品内部需要调整规格比例的项目）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](增加产品内部需要调整规格比例的项目（ADD SPECCFGITEM）_07739899.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此命令配置不正确可能导致业务资源不足引发告警以及用户业务受损，或者触发系统内存不足导致进程复位或者虚机复位，需要评估清楚风险后再操作。

该命令用于配置产品资源规格的调整范围，当默认的资源规格不满足业务应用场景时，在资源富余的前提下，可通过此命令对资源规格的范围进行调整。

## 操作本对象的命令

- [ADD SPECCFGITEM](command/UDG/20.15.2/ADD-SPECCFGITEM.md)
- [LST SPECCFGITEM](command/UDG/20.15.2/LST-SPECCFGITEM.md)
- [MOD SPECCFGITEM](command/UDG/20.15.2/MOD-SPECCFGITEM.md)
- [RMV SPECCFGITEM](command/UDG/20.15.2/RMV-SPECCFGITEM.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改产品内部需要调整规格比例的项目（MOD-SPECCFGITEM）_55657468.md`
- 原始手册：`evidence/UDG/20.15.2/删除产品内部需要调整规格比例的项目（RMV-SPECCFGITEM）_07854139.md`
- 原始手册：`evidence/UDG/20.15.2/增加产品内部需要调整规格比例的项目（ADD-SPECCFGITEM）_07739899.md`
- 原始手册：`evidence/UDG/20.15.2/查询产品内部需要调整规格比例的项目（LST-SPECCFGITEM）_55895152.md`
