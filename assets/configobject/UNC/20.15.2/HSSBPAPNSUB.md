---
id: UNC@20.15.2@ConfigObject@HSSBPAPNSUB
type: ConfigObject
name: HSSBPAPNSUB（HSS BYPASS最小APN签约数据配置）
nf: UNC
version: 20.15.2
object_name: HSSBPAPNSUB
object_kind: entity
applicable_nf:
- MME
status: active
---

# HSSBPAPNSUB（HSS BYPASS最小APN签约数据配置）

## 说明

**适用网元：MME**

此命令用于新增最小APN签约数据群组对应的最小APN签约数据。

用户处于HSS BYPASS状态之后，无法从HSS获取用户签约数据，如果系统内无用户历史签约数据，使用该命令手动配置用户最小APN签约数据，保证业务惯性运行。

## 操作本对象的命令

- [ADD HSSBPAPNSUB](command/UNC/20.15.2/ADD-HSSBPAPNSUB.md)
- [LST HSSBPAPNSUB](command/UNC/20.15.2/LST-HSSBPAPNSUB.md)
- [MOD HSSBPAPNSUB](command/UNC/20.15.2/MOD-HSSBPAPNSUB.md)
- [RMV HSSBPAPNSUB](command/UNC/20.15.2/RMV-HSSBPAPNSUB.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改HSS-BYPASS最小APN签约数据配置-(MOD-HSSBPAPNSUB)_63705566.md`
- 原始手册：`evidence/UNC/20.15.2/删除HSS-BYPASS最小APN签约数据配置-(RMV-HSSBPAPNSUB)_63865462.md`
- 原始手册：`evidence/UNC/20.15.2/增加HSS-BYPASS最小APN签约数据配置-(ADD-HSSBPAPNSUB)_11385437.md`
- 原始手册：`evidence/UNC/20.15.2/查询HSS-BYPASS最小APN签约数据配置-(LST-HSSBPAPNSUB)_64025366.md`
