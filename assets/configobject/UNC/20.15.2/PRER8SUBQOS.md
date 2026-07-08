---
id: UNC@20.15.2@ConfigObject@PRER8SUBQOS
type: ConfigObject
name: PRER8SUBQOS（Pre-R8签约QoS配置）
nf: UNC
version: 20.15.2
object_name: PRER8SUBQOS
object_kind: entity
applicable_nf:
- GGSN
status: active
---

# PRER8SUBQOS（Pre-R8签约QoS配置）

## 说明

**适用NF：GGSN**

该命令用于配置用户的签约QoS属性。当APN下使能COA功能时，RADIUS鉴权服务器会下发用户QoS索引，UNC根据索引匹配到subscriber-qos配置，用来进行用户QoS的协商控制，主动调整带宽等。如果RADIUS鉴权服务器没有下发用户QoS索引，则根据APN下绑定的qos-profile下的用户QoS索引进行用户QoS的协商控制、调整带宽等。

## 操作本对象的命令

- [ADD PRER8SUBQOS](command/UNC/20.15.2/ADD-PRER8SUBQOS.md)
- [LST PRER8SUBQOS](command/UNC/20.15.2/LST-PRER8SUBQOS.md)
- [MOD PRER8SUBQOS](command/UNC/20.15.2/MOD-PRER8SUBQOS.md)
- [RMV PRER8SUBQOS](command/UNC/20.15.2/RMV-PRER8SUBQOS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Pre-R8签约QoS配置（MOD-PRER8SUBQOS）_09652556.md`
- 原始手册：`evidence/UNC/20.15.2/删除Pre-R8签约QoS配置（RMV-PRER8SUBQOS）_09653173.md`
- 原始手册：`evidence/UNC/20.15.2/增加Pre-R8签约QoS配置（ADD-PRER8SUBQOS）_09653616.md`
- 原始手册：`evidence/UNC/20.15.2/查询Pre-R8签约QoS配置（LST-PRER8SUBQOS）_09653203.md`
