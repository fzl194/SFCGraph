---
id: UNC@20.15.2@ConfigObject@RESTOUSRSEG
type: ConfigObject
name: RESTOUSRSEG（容灾用户号段参数）
nf: UNC
version: 20.15.2
object_name: RESTOUSRSEG
object_kind: entity
applicable_nf:
- MME
status: active
---

# RESTOUSRSEG（容灾用户号段参数）

## 说明

**适用网元：MME**

此命令用于增加容灾用户号段参数配置。当“WSFD-201201 MME链式备份”功能仅对指定用户范围内的用户生效，即 [设置容灾功能(SET RESTOFUNC)](../容灾功能管理/设置容灾功能(SET RESTOFUNC)_72345713.md) 的“号段匹配（RESTOSEG）”参数设置为“YES”时，通过此命令增加功能生效的用户范围。

## 操作本对象的命令

- [ADD RESTOUSRSEG](command/UNC/20.15.2/ADD-RESTOUSRSEG.md)
- [LST RESTOUSRSEG](command/UNC/20.15.2/LST-RESTOUSRSEG.md)
- [MOD RESTOUSRSEG](command/UNC/20.15.2/MOD-RESTOUSRSEG.md)
- [RMV RESTOUSRSEG](command/UNC/20.15.2/RMV-RESTOUSRSEG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改容灾用户号段参数-(MOD-RESTOUSRSEG)_10474089.md`
- 原始手册：`evidence/UNC/20.15.2/删除容灾用户号段参数-(RMV-RESTOUSRSEG)_63473978.md`
- 原始手册：`evidence/UNC/20.15.2/增加容灾用户号段参数-(ADD-RESTOUSRSEG)_10674069.md`
- 原始手册：`evidence/UNC/20.15.2/查询容灾用户号段参数-(LST-RESTOUSRSEG)_10554145.md`
