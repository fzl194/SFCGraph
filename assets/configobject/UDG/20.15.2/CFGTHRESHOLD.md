---
id: UDG@20.15.2@ConfigObject@CFGTHRESHOLD
type: ConfigObject
name: CFGTHRESHOLD（配置对象告警阈值）
nf: UDG
version: 20.15.2
object_name: CFGTHRESHOLD
object_kind: entity
status: active
---

# CFGTHRESHOLD（配置对象告警阈值）

## 说明

该命令用于增加配置对象告警阈值。系统通过检测配置对象当前记录数与配置对象最大记录数的比值是否大于配置对象告警阈值决定是否上报“ALM-135602215 配置数量超阈值”。

> **说明**
> 配置对象的告警阈值最大数量取决于系统实际配置对象数量，最大支持100000。

## 操作本对象的命令

- [ADD CFGTHRESHOLD](command/UDG/20.15.2/ADD-CFGTHRESHOLD.md)
- [LST CFGTHRESHOLD](command/UDG/20.15.2/LST-CFGTHRESHOLD.md)
- [MOD CFGTHRESHOLD](command/UDG/20.15.2/MOD-CFGTHRESHOLD.md)
- [RMV CFGTHRESHOLD](command/UDG/20.15.2/RMV-CFGTHRESHOLD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改配置对象告警阈值(MOD-CFGTHRESHOLD)_36569360.md`
- 原始手册：`evidence/UDG/20.15.2/删除配置对象告警阈值(RMV-CFGTHRESHOLD)_72490293.md`
- 原始手册：`evidence/UDG/20.15.2/增加配置对象告警阈值(ADD-CFGTHRESHOLD)_72647329.md`
- 原始手册：`evidence/UDG/20.15.2/查询配置对象告警阈值(LST-CFGTHRESHOLD)_72648877.md`
