---
id: UNC@20.15.2@ConfigObject@APPLYPREFVALUE
type: ConfigObject
name: APPLYPREFVALUE（BGP路由首选值设置）
nf: UNC
version: 20.15.2
object_name: APPLYPREFVALUE
object_kind: entity
status: active
---

# APPLYPREFVALUE（BGP路由首选值设置）

## 说明

该命令用于增加BGP路由首选值设置。使用ADD APPLYPREFVALUE命令配置优先级后，在不同协议发现到达同一目的地的不同路由时，优先级高的路由协议发现的路由将作为当前的有效路由。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APPLYPREFVALUE]] · ADD APPLYPREFVALUE
- [[command/UNC/20.15.2/LST-APPLYPREFVALUE]] · LST APPLYPREFVALUE
- [[command/UNC/20.15.2/MOD-APPLYPREFVALUE]] · MOD APPLYPREFVALUE
- [[command/UNC/20.15.2/RMV-APPLYPREFVALUE]] · RMV APPLYPREFVALUE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改BGP路由首选值设置（MOD-APPLYPREFVALUE）_49801734.md`
- 原始手册：`evidence/UNC/20.15.2/删除BGP路由首选值设置（RMV-APPLYPREFVALUE）_00440989.md`
- 原始手册：`evidence/UNC/20.15.2/增加BGP路由首选值设置（ADD-APPLYPREFVALUE）_49961906.md`
- 原始手册：`evidence/UNC/20.15.2/查询BGP路由首选值设置（LST-APPLYPREFVALUE）_00441217.md`
