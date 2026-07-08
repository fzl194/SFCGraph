---
id: UNC@20.15.2@ConfigObject@WEEKDAY
type: ConfigObject
name: WEEKDAY（计费星期表）
nf: UNC
version: 20.15.2
object_name: WEEKDAY
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# WEEKDAY（计费星期表）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置计费星期表记录，配置指定每周的费率类型为工作日或周末。

UNC支持费率时间段配置，即可以根据不同费率类型（包括节假日、工作日和周末三种费率类型）的时间段来配置不同的费率。节假日的配置见命令：ADD FESTIVAL。

配置本命令后，当用户持续在线，会出现跨费率类型的切换。切换的时间点为00:00:00。如用户在星期五和星期六两天持续在线，星期六的0点时会发生费率类型切换。本配置只对离线计费费率切换生效。

周日期配置有优先级关系，当计费属性的星期配置在生效的情况下，系统首先使用计费属性配置的星期配置，如果计费属性的星期配置未配置，则使用全局配置的星期配置。全局配置中周日期配置的默认值是周一到周五为workday，周六周日为weekend。

## 操作本对象的命令

- [ADD WEEKDAY](command/UNC/20.15.2/ADD-WEEKDAY.md)
- [LST WEEKDAY](command/UNC/20.15.2/LST-WEEKDAY.md)
- [MOD WEEKDAY](command/UNC/20.15.2/MOD-WEEKDAY.md)
- [RMV WEEKDAY](command/UNC/20.15.2/RMV-WEEKDAY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改计费星期表（MOD-WEEKDAY）_09896832.md`
- 原始手册：`evidence/UNC/20.15.2/删除计费星期表（RMV-WEEKDAY）_09896833.md`
- 原始手册：`evidence/UNC/20.15.2/查询计费星期表（LST-WEEKDAY）_09896834.md`
- 原始手册：`evidence/UNC/20.15.2/配置计费星期表（ADD-WEEKDAY）_09896831.md`
