---
id: UNC@20.15.2@ConfigObject@RAPAGINGRULE
type: ConfigObject
name: RAPAGINGRULE（基于路由区的寻呼参数设置）
nf: UNC
version: 20.15.2
object_name: RAPAGINGRULE
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# RAPAGINGRULE（基于路由区的寻呼参数设置）

## 说明

**适用网元：SGSN**

本命令用于增加基于路由区的2/3G寻呼参数，优先级高于整系统设置的2G( [**SET GMM**](../MM协议参数管理/Gb模式MM协议参数/设置Gb模式MM协议参数(SET GMM)_72345121.md) )和3G( [**SET PMM**](../MM协议参数管理/Iu模式MM协议参数/设置Iu模式MM协议参数(SET PMM)_26305336.md) )寻呼策略。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RAPAGINGRULE]] · ADD RAPAGINGRULE
- [[command/UNC/20.15.2/LST-RAPAGINGRULE]] · LST RAPAGINGRULE
- [[command/UNC/20.15.2/MOD-RAPAGINGRULE]] · MOD RAPAGINGRULE
- [[command/UNC/20.15.2/RMV-RAPAGINGRULE]] · RMV RAPAGINGRULE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于路由区的寻呼参数设置(MOD-RAPAGINGRULE)_26305340.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于路由区的寻呼参数设置(RMV-RAPAGINGRULE)_72225209.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于路由区的寻呼参数设置(ADD-RAPAGINGRULE)_26145528.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于路由区的寻呼参数设置(LST-RAPAGINGRULE)_72345127.md`
