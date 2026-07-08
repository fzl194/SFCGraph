---
id: UDG@20.15.2@ConfigObject@INTERFACE
type: ConfigObject
name: INTERFACE（接口）
nf: UDG
version: 20.15.2
object_name: INTERFACE
object_kind: entity
status: active
---

# INTERFACE（接口）

## 说明

该命令用于创建逻辑接口并初始化该接口的相关配置，逻辑接口是指能够实现数据交换功能但物理上不存在、需要通过配置建立的接口，包括Loopback接口、NULL0接口等。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-INTERFACE]] · ADD INTERFACE
- [[command/UDG/20.15.2/LST-INTERFACE]] · LST INTERFACE
- [[command/UDG/20.15.2/MOD-INTERFACE]] · MOD INTERFACE
- [[command/UDG/20.15.2/OPR-INTERFACE]] · OPR INTERFACE
- [[command/UDG/20.15.2/RMV-INTERFACE]] · RMV INTERFACE

## 关联对象

- [[configobject/UDG/20.15.2/BFDSESSION]] · BFDSESSION
- [[configobject/UDG/20.15.2/ETHSUBIF]] · ETHSUBIF
- [[configobject/UDG/20.15.2/GRETUNNEL]] · GRETUNNEL
- [[configobject/UDG/20.15.2/IFIPV4ADDRESS]] · IFIPV4ADDRESS
- [[configobject/UDG/20.15.2/IFIPV6ADDRESS]] · IFIPV6ADDRESS
- [[configobject/UDG/20.15.2/IFIPV6ENABLE]] · IFIPV6ENABLE
- [[configobject/UDG/20.15.2/IPBINDVPN]] · IPBINDVPN
- [[configobject/UDG/20.15.2/SRROUTE]] · SRROUTE
- [[configobject/UDG/20.15.2/SRROUTE6]] · SRROUTE6

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改接口（MOD-INTERFACE）_50281674.md`
- 原始手册：`evidence/UDG/20.15.2/删除接口（RMV-INTERFACE）_50281434.md`
- 原始手册：`evidence/UDG/20.15.2/增加接口（ADD-INTERFACE）_49960870.md`
- 原始手册：`evidence/UDG/20.15.2/查询接口（LST-INTERFACE）_49801850.md`
- 原始手册：`evidence/UDG/20.15.2/设置接口维护状态（OPR-INTERFACE）_50121206.md`
