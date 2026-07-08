---
id: UDG@20.15.2@ConfigObject@HIGHRISKPERIOD
type: ConfigObject
name: HIGHRISKPERIOD（高危时间段提示状态）
nf: UDG
version: 20.15.2
object_name: HIGHRISKPERIOD
object_kind: global_setting
status: active
---

# HIGHRISKPERIOD（高危时间段提示状态）

## 说明

本命令用于设置高危时间段提示状态、高危时间段和高危命令提示信息。

> **说明**
> - 该命令中参数“高危时间段提示状态”的初始设定值为“OFF(关闭)”。
> - 高危时间段提示状态默认关闭，通过**SET HIGHRISKPERIOD**命令开启高危时间段提示状态开关后，用户在此时间段执行系统中所有高危命令时，弹框中会新增用户在“提示信息”参数中所设置的提示信息。
> - 该命令执行后仅在网元OM Portal的MML界面生效，不支持在网管界面生效。

## 操作本对象的命令

- [LST HIGHRISKPERIOD](command/UDG/20.15.2/LST-HIGHRISKPERIOD.md)
- [SET HIGHRISKPERIOD](command/UDG/20.15.2/SET-HIGHRISKPERIOD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询高危时间段提示状态（LST-HIGHRISKPERIOD）_15404818.md`
- 原始手册：`evidence/UDG/20.15.2/设置高危时间段提示状态（SET-HIGHRISKPERIOD）_15084970.md`
