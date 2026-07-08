---
id: UDG@20.15.2@ConfigObject@UPBINDBWMUSRG
type: ConfigObject
name: UPBINDBWMUSRG（带宽管理用户组User Profile绑定）
nf: UDG
version: 20.15.2
object_name: UPBINDBWMUSRG
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# UPBINDBWMUSRG（带宽管理用户组User Profile绑定）

## 说明

**适用NF：PGW-U、UPF**

该命令用于将绑定某个UserProfile的用户加入一个带宽管理用户组。当运营商希望对特定UserProfile下的用户进行带宽控制时，需要将该UserProfile绑定到包含带宽控制策略的用户组下，该命令就是完成绑定的功能。

## 操作本对象的命令

- [ADD UPBINDBWMUSRG](command/UDG/20.15.2/ADD-UPBINDBWMUSRG.md)
- [LST UPBINDBWMUSRG](command/UDG/20.15.2/LST-UPBINDBWMUSRG.md)
- [RMV UPBINDBWMUSRG](command/UDG/20.15.2/RMV-UPBINDBWMUSRG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除带宽管理用户组User-Profile绑定（RMV-UPBINDBWMUSRG）_82837492.md`
- 原始手册：`evidence/UDG/20.15.2/增加带宽管理用户组User-Profile绑定（ADD-UPBINDBWMUSRG）_82837491.md`
- 原始手册：`evidence/UDG/20.15.2/查询带宽管理用户组User-Profile绑定（LST-UPBINDBWMUSRG）_82837493.md`
