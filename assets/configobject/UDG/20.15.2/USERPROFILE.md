---
id: UDG@20.15.2@ConfigObject@USERPROFILE
type: ConfigObject
name: USERPROFILE（用户模板）
nf: UDG
version: 20.15.2
object_name: USERPROFILE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# USERPROFILE（用户模板）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加用户模板。用户模板可用于设置Alias Marking功能是否开启，防范攻击功能是否开启，免费业务是否进行在线、离线计费，用户实时位置信息是否上报到报表服务器，UserProfile级别的监控属性，预留配置属性等功能。

## 操作本对象的命令

- [ADD USERPROFILE](command/UDG/20.15.2/ADD-USERPROFILE.md)
- [LCK USERPROFILE](command/UDG/20.15.2/LCK-USERPROFILE.md)
- [LST USERPROFILE](command/UDG/20.15.2/LST-USERPROFILE.md)
- [MOD USERPROFILE](command/UDG/20.15.2/MOD-USERPROFILE.md)
- [RMV USERPROFILE](command/UDG/20.15.2/RMV-USERPROFILE.md)

## 关联对象

- [EXTENDPROP](configobject/UDG/20.15.2/EXTENDPROP.md)
- [RULEBINDING](configobject/UDG/20.15.2/RULEBINDING.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改用户模板（MOD-USERPROFILE）_82837280.md`
- 原始手册：`evidence/UDG/20.15.2/删除用户模板（RMV-USERPROFILE）_82837285.md`
- 原始手册：`evidence/UDG/20.15.2/增加用户模板（ADD-USERPROFILE）_82837279.md`
- 原始手册：`evidence/UDG/20.15.2/查询用户模板（LST-USERPROFILE）_82837286.md`
- 原始手册：`evidence/UDG/20.15.2/设置用户模板的锁定（LCK-USERPROFILE）_97358675.md`
