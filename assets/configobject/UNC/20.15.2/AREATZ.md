---
id: UNC@20.15.2@ConfigObject@AREATZ
type: ConfigObject
name: AREATZ（区域时区参数）
nf: UNC
version: 20.15.2
object_name: AREATZ
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# AREATZ（区域时区参数）

## 说明

**适用网元：SGSN、MME**

此命令用于增加区域时区记录。即增加特定区域与时区标识的映射关系。该时区标识对应的时区和夏令时信息通过 [**ADD TZLST**](../多时区参数/增加多时区参数(ADD TZLST)_26305400.md) 命令配置。

## 操作本对象的命令

- [ADD AREATZ](command/UNC/20.15.2/ADD-AREATZ.md)
- [LST AREATZ](command/UNC/20.15.2/LST-AREATZ.md)
- [MOD AREATZ](command/UNC/20.15.2/MOD-AREATZ.md)
- [RMV AREATZ](command/UNC/20.15.2/RMV-AREATZ.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改区域时区参数(MOD-AREATZ)_72345185.md`
- 原始手册：`evidence/UNC/20.15.2/删除区域时区参数(RMV-AREATZ)_26305398.md`
- 原始手册：`evidence/UNC/20.15.2/增加区域时区参数(ADD-AREATZ)_72225267.md`
- 原始手册：`evidence/UNC/20.15.2/查询区域时区参数(LST-AREATZ)_26145588.md`
