---
id: UDG@20.15.2@ConfigObject@APPLYPREFERENCE
type: ConfigObject
name: APPLYPREFERENCE（路由优先级设置）
nf: UDG
version: 20.15.2
object_name: APPLYPREFERENCE
object_kind: entity
status: active
---

# APPLYPREFERENCE（路由优先级设置）

## 说明

该命令用于添加路由优先级设置，设备上同时运行多种路由协议时，存在各个路由协议之间路由信息共享和选择的问题，所以为每一种路由协议指定了一个缺省的优先级。在不同的路由协议发现去往同一目的地的多条路由时，优先级高的协议发现的路由将被选中以转发IP报文。

## 操作本对象的命令

- [ADD APPLYPREFERENCE](command/UDG/20.15.2/ADD-APPLYPREFERENCE.md)
- [LST APPLYPREFERENCE](command/UDG/20.15.2/LST-APPLYPREFERENCE.md)
- [MOD APPLYPREFERENCE](command/UDG/20.15.2/MOD-APPLYPREFERENCE.md)
- [RMV APPLYPREFERENCE](command/UDG/20.15.2/RMV-APPLYPREFERENCE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改路由优先级设置（MOD-APPLYPREFERENCE）_00601285.md`
- 原始手册：`evidence/UDG/20.15.2/删除路由优先级设置（RMV-APPLYPREFERENCE）_49962034.md`
- 原始手册：`evidence/UDG/20.15.2/增加路由优先级设置（ADD-APPLYPREFERENCE）_49961170.md`
- 原始手册：`evidence/UDG/20.15.2/查询路由优先级设置（LST-APPLYPREFERENCE）_00841549.md`
