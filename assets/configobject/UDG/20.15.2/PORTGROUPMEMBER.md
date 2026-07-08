---
id: UDG@20.15.2@ConfigObject@PORTGROUPMEMBER
type: ConfigObject
name: PORTGROUPMEMBER（端口组成员）
nf: UDG
version: 20.15.2
object_name: PORTGROUPMEMBER
object_kind: entity
status: active
---

# PORTGROUPMEMBER（端口组成员）

## 说明

该命令用于增加端口组成员，通过命令ADD PORTGROUP创建端口组后，端口组中并不包含任何成员接口，此时，可以通过该命令向端口组中添加接口，这样在进行端口组的配置时，系统才会自动到端口组绑定的所有成员接口下，完成接口批量配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-PORTGROUPMEMBER]] · ADD PORTGROUPMEMBER
- [[command/UDG/20.15.2/LST-PORTGROUPMEMBER]] · LST PORTGROUPMEMBER
- [[command/UDG/20.15.2/RMV-PORTGROUPMEMBER]] · RMV PORTGROUPMEMBER

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除端口组成员（RMV-PORTGROUPMEMBER）_00841193.md`
- 原始手册：`evidence/UDG/20.15.2/增加端口组成员（ADD-PORTGROUPMEMBER）_00866713.md`
- 原始手册：`evidence/UDG/20.15.2/查询端口组成员配置（LST-PORTGROUPMEMBER）_49961894.md`
