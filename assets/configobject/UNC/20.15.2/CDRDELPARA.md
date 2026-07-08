---
id: UNC@20.15.2@ConfigObject@CDRDELPARA
type: ConfigObject
name: CDRDELPARA（话单删除参数）
nf: UNC
version: 20.15.2
object_name: CDRDELPARA
object_kind: entity
applicable_nf:
- NCG
status: active
---

# CDRDELPARA（话单删除参数）

## 说明

![](修改话单删除参数（MOD CDRDELPARA）_51174269.assets/notice_3.0-zh-cn_2.png)

如果设置删除时间为业务忙时，可能会对业务产生影响，建议设置删除时间为系统闲时。

**适用NF：NCG**

该命令用于修改话单删除、话单备份和话单分发任务的话单删除开始时间和话单删除时间间隔，它包含修改和查询命令，防止在NCG业务忙碌时进行过期删除任务时可能导致IO较高，对NCG业务产生影响。

执行命令之前，可执行 [**LST CDRDELPARA**](查询话单删除参数（LST CDRDELPARA）_51174270.md) 命令查询当前各任务设置的话单删除参数。

## 操作本对象的命令

- [LST CDRDELPARA](command/UNC/20.15.2/LST-CDRDELPARA.md)
- [MOD CDRDELPARA](command/UNC/20.15.2/MOD-CDRDELPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改话单删除参数（MOD-CDRDELPARA）_51174269.md`
- 原始手册：`evidence/UNC/20.15.2/查询话单删除参数（LST-CDRDELPARA）_51174270.md`
