---
id: UNC@20.15.2@ConfigObject@HSSBPUSRSUB
type: ConfigObject
name: HSSBPUSRSUB（HSS BYPASS最小用户签约数据配置）
nf: UNC
version: 20.15.2
object_name: HSSBPUSRSUB
object_kind: entity
applicable_nf:
- MME
status: active
---

# HSSBPUSRSUB（HSS BYPASS最小用户签约数据配置）

## 说明

**适用网元：MME**

此命令用于新增HSS BYPASS最小用户签约数据配置。

用户处于HSS BYPASS状态之后，无法从HSS获取用户签约数据，如果系统内无用户历史签约数据，使用该命令手动配置用户最小签约数据，保证业务惯性运行。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-HSSBPUSRSUB]] · ADD HSSBPUSRSUB
- [[command/UNC/20.15.2/LST-HSSBPUSRSUB]] · LST HSSBPUSRSUB
- [[command/UNC/20.15.2/MOD-HSSBPUSRSUB]] · MOD HSSBPUSRSUB
- [[command/UNC/20.15.2/RMV-HSSBPUSRSUB]] · RMV HSSBPUSRSUB

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改HSS-BYPASS最小用户签约数据配置-(MOD-HSSBPUSRSUB)_63689568.md`
- 原始手册：`evidence/UNC/20.15.2/删除HSS-BYPASS最小用户签约数据配置-(RMV-HSSBPUSRSUB)_64009372.md`
- 原始手册：`evidence/UNC/20.15.2/增加HSS-BYPASS最小用户签约数据配置-(ADD-HSSBPUSRSUB)_11529413.md`
- 原始手册：`evidence/UNC/20.15.2/查询HSS-BYPASS最小用户签约数据配置-(LST-HSSBPUSRSUB)_63849436.md`
