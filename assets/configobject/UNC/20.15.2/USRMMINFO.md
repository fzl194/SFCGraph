---
id: UNC@20.15.2@ConfigObject@USRMMINFO
type: ConfigObject
name: USRMMINFO（网络名称）
nf: UNC
version: 20.15.2
object_name: USRMMINFO
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# USRMMINFO（网络名称）

## 说明

**适用网元：SGSN、MME**

该命令用于添加运营商网络名称。在UE接入 UNC 时，如果需要给UE下发网络名称， UNC 判断UE在本命令配置的用户范围，则优选下发本命令配置的网络名称。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-USRMMINFO]] · ADD USRMMINFO
- [[command/UNC/20.15.2/LST-USRMMINFO]] · LST USRMMINFO
- [[command/UNC/20.15.2/MOD-USRMMINFO]] · MOD USRMMINFO
- [[command/UNC/20.15.2/RMV-USRMMINFO]] · RMV USRMMINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改网络名称(MOD-USRMMINFO)_26305868.md`
- 原始手册：`evidence/UNC/20.15.2/删除网络名称(RMV-USRMMINFO)_72225737.md`
- 原始手册：`evidence/UNC/20.15.2/增加网络名称(ADD-USRMMINFO)_26146058.md`
- 原始手册：`evidence/UNC/20.15.2/查询网络名称(LST-USRMMINFO)_72345659.md`
