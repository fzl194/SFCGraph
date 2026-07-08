---
id: UNC@20.15.2@ConfigObject@GBAUTHCIPH
type: ConfigObject
name: GBAUTHCIPH（Gb模式用户安全参数）
nf: UNC
version: 20.15.2
object_name: GBAUTHCIPH
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GBAUTHCIPH（Gb模式用户安全参数）

## 说明

**适用网元：SGSN**

该命令用于增加2G鉴权加密的配置。 UNC 可以结合运营商的配置要求和协议规范决定是否使用鉴权加密。针对SGSN节点可能遇到的所有需要鉴权的流程， UNC 均设置了开关加以控制，运营商可以通过配置决定这些流程是否需要鉴权。

## 操作本对象的命令

- [ADD GBAUTHCIPH](command/UNC/20.15.2/ADD-GBAUTHCIPH.md)
- [LST GBAUTHCIPH](command/UNC/20.15.2/LST-GBAUTHCIPH.md)
- [MOD GBAUTHCIPH](command/UNC/20.15.2/MOD-GBAUTHCIPH.md)
- [RMV GBAUTHCIPH](command/UNC/20.15.2/RMV-GBAUTHCIPH.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Gb模式用户安全参数（MOD-GBAUTHCIPH）_26305454.md`
- 原始手册：`evidence/UNC/20.15.2/删除Gb模式用户安全参数(RMV-GBAUTHCIPH)_72225323.md`
- 原始手册：`evidence/UNC/20.15.2/增加Gb模式用户安全参数（ADD-GBAUTHCIPH）_26145642.md`
- 原始手册：`evidence/UNC/20.15.2/查询Gb模式用户安全参数(LST-GBAUTHCIPH)_72345241.md`
