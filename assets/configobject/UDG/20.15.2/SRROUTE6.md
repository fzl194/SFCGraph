---
id: UDG@20.15.2@ConfigObject@SRROUTE6
type: ConfigObject
name: SRROUTE6（IPv6静态路由）
nf: UDG
version: 20.15.2
object_name: SRROUTE6
object_kind: entity
status: active
---

# SRROUTE6（IPv6静态路由）

## 说明

该命令用于添加IPv6静态路由。

静态路由是一种需要管理员手工配置的特殊路由。

当网络结构比较简单时，只需配置静态路由就可以使网络正常工作。当设备不能使用动态路由协议或者不能建立到达目的网络时，也可以使用静态路由。合理的静态路由可以改进网络性能，并为重要业务保证带宽。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-SRROUTE6]] · ADD SRROUTE6
- [[command/UDG/20.15.2/DSP-SRROUTE6]] · DSP SRROUTE6
- [[command/UDG/20.15.2/LST-SRROUTE6]] · LST SRROUTE6
- [[command/UDG/20.15.2/MOD-SRROUTE6]] · MOD SRROUTE6
- [[command/UDG/20.15.2/RMV-SRROUTE6]] · RMV SRROUTE6

## 关联对象

- [[configobject/UDG/20.15.2/BFDSESSION]] · BFDSESSION
- [[configobject/UDG/20.15.2/GRETUNNEL]] · GRETUNNEL
- [[configobject/UDG/20.15.2/INTERFACE]] · INTERFACE

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPv6静态路由（MOD-SRROUTE6）_00600893.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPv6静态路由（RMV-SRROUTE6）_49960894.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPv6静态路由（ADD-SRROUTE6）_50280922.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPv6静态路由（LST-SRROUTE6）_50281306.md`
- 原始手册：`evidence/UDG/20.15.2/显示IPv6静态路由表（DSP-SRROUTE6）_00840897.md`
