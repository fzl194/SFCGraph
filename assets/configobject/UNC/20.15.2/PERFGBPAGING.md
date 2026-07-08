---
id: UNC@20.15.2@ConfigObject@PERFGBPAGING
type: ConfigObject
name: PERFGBPAGING（Gb接口寻呼数据）
nf: UNC
version: 20.15.2
object_name: PERFGBPAGING
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# PERFGBPAGING（Gb接口寻呼数据）

## 说明

**适用网元：SGSN**

该命令用于增加2G寻呼配置参数，用于Gb模式路由区号话统上报的对象。指定路由区Gb模式附着流程，指定路由区Gb模式分离流程测量，指定路由区Gb模式SGSN内路由跟新，指定路由区Gb模式SGSN间路由更新，指定路由区Gb模式分组寻呼，指定路由区Gb模式无线资源，指定路由区Gb模式会话资源，路由区2G会话业务测量和Gb MOCN模式下基本流程测量话统测量单元下的指标上报时必需知道所要上报的LAI和RAC，否则无法上报。因此，需要通过该命令手动增加动态上报的LAI和RAC。

## 操作本对象的命令

- [ADD PERFGBPAGING](command/UNC/20.15.2/ADD-PERFGBPAGING.md)
- [LST PERFGBPAGING](command/UNC/20.15.2/LST-PERFGBPAGING.md)
- [RMV PERFGBPAGING](command/UNC/20.15.2/RMV-PERFGBPAGING.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Gb接口寻呼数据(RMV-PERFGBPAGING)_72345791.md`
- 原始手册：`evidence/UNC/20.15.2/增加Gb接口寻呼数据(ADD-PERFGBPAGING)_26306002.md`
- 原始手册：`evidence/UNC/20.15.2/查询Gb接口寻呼数据(LST-PERFGBPAGING)_26146192.md`
