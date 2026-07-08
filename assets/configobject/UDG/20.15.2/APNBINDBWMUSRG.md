---
id: UDG@20.15.2@ConfigObject@APNBINDBWMUSRG
type: ConfigObject
name: APNBINDBWMUSRG（带宽管理用户组APN绑定）
nf: UDG
version: 20.15.2
object_name: APNBINDBWMUSRG
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# APNBINDBWMUSRG（带宽管理用户组APN绑定）

## 说明

**适用NF：PGW-U、UPF**

该命令用于将某个APN的用户加入一个带宽管理用户组。当运营商希望对特定APN下的用户进行带宽控制时，需要将该APN绑定到包含带宽控制策略的用户组下，该命令就是完成绑定的功能。

## 操作本对象的命令

- [ADD APNBINDBWMUSRG](command/UDG/20.15.2/ADD-APNBINDBWMUSRG.md)
- [LST APNBINDBWMUSRG](command/UDG/20.15.2/LST-APNBINDBWMUSRG.md)
- [RMV APNBINDBWMUSRG](command/UDG/20.15.2/RMV-APNBINDBWMUSRG.md)

## 关联对象

- [APN](configobject/UDG/20.15.2/APN.md)
- [BWMUSERGROUP](configobject/UDG/20.15.2/BWMUSERGROUP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除带宽管理用户组APN绑定（RMV-APNBINDBWMUSRG）_86526866.md`
- 原始手册：`evidence/UDG/20.15.2/增加带宽管理用户组APN绑定（ADD-APNBINDBWMUSRG）_82837487.md`
- 原始手册：`evidence/UDG/20.15.2/查询带宽管理用户组APN绑定（LST-APNBINDBWMUSRG）_82837489.md`
