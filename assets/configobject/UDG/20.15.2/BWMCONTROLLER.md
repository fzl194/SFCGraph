---
id: UDG@20.15.2@ConfigObject@BWMCONTROLLER
type: ConfigObject
name: BWMCONTROLLER（带宽管理控制器）
nf: UDG
version: 20.15.2
object_name: BWMCONTROLLER
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# BWMCONTROLLER（带宽管理控制器）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置一个bwm控制器，设置保证带宽、峰值速率、五元组个数、业务等级规格、用户公平使能、工作模式、最大丢包率、丢包率差值、保障模式等相关参数。如果期望基于业务流做CAR或SHAPING带宽控制，或限制业务流数，使用此命令进行配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-BWMCONTROLLER]] · ADD BWMCONTROLLER
- [[command/UDG/20.15.2/LST-BWMCONTROLLER]] · LST BWMCONTROLLER
- [[command/UDG/20.15.2/MOD-BWMCONTROLLER]] · MOD BWMCONTROLLER
- [[command/UDG/20.15.2/RMV-BWMCONTROLLER]] · RMV BWMCONTROLLER

## 关联对象

- [[configobject/UDG/20.15.2/BWMRULE]] · BWMRULE

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改带宽管理控制器（MOD-BWMCONTROLLER）_82837461.md`
- 原始手册：`evidence/UDG/20.15.2/删除带宽管理控制器（RMV-BWMCONTROLLER）_82837462.md`
- 原始手册：`evidence/UDG/20.15.2/增加带宽管理控制器（ADD-BWMCONTROLLER）_82837460.md`
- 原始手册：`evidence/UDG/20.15.2/查询带宽管理控制器（LST-BWMCONTROLLER）_82837463.md`
