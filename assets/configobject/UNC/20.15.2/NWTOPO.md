---
id: UNC@20.15.2@ConfigObject@NWTOPO
type: ConfigObject
name: NWTOPO（组网拓扑采集功能开关）
nf: UNC
version: 20.15.2
object_name: NWTOPO
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# NWTOPO（组网拓扑采集功能开关）

## 说明

**适用网元：SGSN、MME**

该命令用于设置是否打开组网拓扑信息采集功能。如果设置为关闭，则组网拓扑采集服务器通过下发组网拓扑采集任务无法获取到对应的组网拓扑信息；如果设置为打开，则组网拓扑采集服务器可通过下发组网拓扑采集任务获取系统的组网拓扑信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NWTOPO]] · LST NWTOPO
- [[command/UNC/20.15.2/SET-NWTOPO]] · SET NWTOPO

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询组网拓扑采集功能开关(LST-NWTOPO)_72226037.md`
- 原始手册：`evidence/UNC/20.15.2/设置组网拓扑采集功能开关（SET-NWTOPO）_26146358.md`
