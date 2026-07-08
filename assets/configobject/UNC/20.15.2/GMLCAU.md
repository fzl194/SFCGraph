---
id: UNC@20.15.2@ConfigObject@GMLCAU
type: ConfigObject
name: GMLCAU（GMLC权限配置）
nf: UNC
version: 20.15.2
object_name: GMLCAU
object_kind: entity
applicable_nf:
- MME
status: active
---

# GMLCAU（GMLC权限配置）

## 说明

**适用网元：MME**

此命令用于增加GMLC权限配置。配置指定的GMLC的定位权限信息，MME根据该权限信息来实现对GMLC发起的定位请求的接入控制。

对GMLC的接入权限进行控制，允许/禁止定位请求，只允许接入指定的客户端类型、LCS业务类型的定位请求。

## 操作本对象的命令

- [ADD GMLCAU](command/UNC/20.15.2/ADD-GMLCAU.md)
- [LST GMLCAU](command/UNC/20.15.2/LST-GMLCAU.md)
- [RMV GMLCAU](command/UNC/20.15.2/RMV-GMLCAU.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GMLC权限配置(RMV-GMLCAU)_72225473.md`
- 原始手册：`evidence/UNC/20.15.2/增加GMLC权限配置(ADD-GMLCAU)_26145794.md`
- 原始手册：`evidence/UNC/20.15.2/查询GMLC权限配置(LST-GMLCAU)_26305604.md`
