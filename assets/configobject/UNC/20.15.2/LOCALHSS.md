---
id: UNC@20.15.2@ConfigObject@LOCALHSS
type: ConfigObject
name: LOCALHSS（本地HSS）
nf: UNC
version: 20.15.2
object_name: LOCALHSS
object_kind: entity
applicable_nf:
- MME
status: active
---

# LOCALHSS（本地HSS）

## 说明

**适用网元：MME**

该命令用于增加本地HSS配置，HSS通过HSS主机名唯一标识。运营商可以通过比较本地HSS与用户签约信息所在的HSS的主机名，来判断用户是本网本地用户还是本网异地用户。

本地HSS配置用于“基于位置的IP地址重分配”功能。

## 操作本对象的命令

- [ADD LOCALHSS](command/UNC/20.15.2/ADD-LOCALHSS.md)
- [LST LOCALHSS](command/UNC/20.15.2/LST-LOCALHSS.md)
- [MOD LOCALHSS](command/UNC/20.15.2/MOD-LOCALHSS.md)
- [RMV LOCALHSS](command/UNC/20.15.2/RMV-LOCALHSS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改本地HSS(MOD-LOCALHSS)_26146080.md`
- 原始手册：`evidence/UNC/20.15.2/删除本地HSS(RMV-LOCALHSS)_72345679.md`
- 原始手册：`evidence/UNC/20.15.2/增加本地HSS(ADD-LOCALHSS)_26305888.md`
- 原始手册：`evidence/UNC/20.15.2/查询本地HSS(LST-LOCALHSS)_72225759.md`
