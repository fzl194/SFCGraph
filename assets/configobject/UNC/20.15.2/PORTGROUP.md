---
id: UNC@20.15.2@ConfigObject@PORTGROUP
type: ConfigObject
name: PORTGROUP（端口组）
nf: UNC
version: 20.15.2
object_name: PORTGROUP
object_kind: entity
status: active
---

# PORTGROUP（端口组）

## 说明

通常，设备的接口数比较多，并且很多接口具有相同的配置。如果对这些接口进行逐个配置，不但操作繁琐，而且容易输入错误。为解决此问题，可以通过该命创建一个端口组，然后将需要执行相同配置命令的接口加入到该端口组，在端口组视图下配置命令时，系统会自动到端口组绑定的所有成员接口下执行这些命令行，完成接口批量配置。

## 操作本对象的命令

- [ADD PORTGROUP](command/UNC/20.15.2/ADD-PORTGROUP.md)
- [LST PORTGROUP](command/UNC/20.15.2/LST-PORTGROUP.md)
- [RMV PORTGROUP](command/UNC/20.15.2/RMV-PORTGROUP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除端口组（RMV-PORTGROUP）_00441253.md`
- 原始手册：`evidence/UNC/20.15.2/增加端口组（ADD-PORTGROUP）_00600409.md`
- 原始手册：`evidence/UNC/20.15.2/查询端口组配置（LST-PORTGROUP）_49962022.md`
