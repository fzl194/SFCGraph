---
id: UDG@20.15.2@ConfigObject@BWMUSERGROUP
type: ConfigObject
name: BWMUSERGROUP（带宽管理用户组）
nf: UDG
version: 20.15.2
object_name: BWMUSERGROUP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# BWMUSERGROUP（带宽管理用户组）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加一个带宽管理用户组，并指定其业务类型和优先级。带宽管理用户组分三种，分别是全局用户组、默认用户组和具体用户组。全局用户组为系统默认配置，当运营商需要做基于整机的带宽控制时，则在全局用户组下配置全局带宽管理规则；当运营商希望做精细地带宽控制，则使用该命令增加一个默认、或具体用户组，用户组下可以绑定带宽管理规则，当对应用户组的用户业务匹配该规则时，执行相应的带宽控制策略。

## 操作本对象的命令

- [ADD BWMUSERGROUP](command/UDG/20.15.2/ADD-BWMUSERGROUP.md)
- [LST BWMUSERGROUP](command/UDG/20.15.2/LST-BWMUSERGROUP.md)
- [MOD BWMUSERGROUP](command/UDG/20.15.2/MOD-BWMUSERGROUP.md)
- [RMV BWMUSERGROUP](command/UDG/20.15.2/RMV-BWMUSERGROUP.md)

## 关联对象

- [APNBINDBWMUSRG](configobject/UDG/20.15.2/APNBINDBWMUSRG.md)
- [BWMRULE](configobject/UDG/20.15.2/BWMRULE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改带宽管理用户组（MOD-BWMUSERGROUP）_82837469.md`
- 原始手册：`evidence/UDG/20.15.2/删除带宽管理用户组（RMV-BWMUSERGROUP）_86526876.md`
- 原始手册：`evidence/UDG/20.15.2/增加带宽管理用户组（ADD-BWMUSERGROUP）_82837468.md`
- 原始手册：`evidence/UDG/20.15.2/查询带宽管理用户组（LST-BWMUSERGROUP）_82837471.md`
