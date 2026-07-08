---
id: UNC@20.15.2@ConfigObject@USRLOCATION
type: ConfigObject
name: USRLOCATION（用户位置）
nf: UNC
version: 20.15.2
object_name: USRLOCATION
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# USRLOCATION（用户位置）

## 说明

**适用NF：PGW-C、SMF**

该命令用于增加用户位置信息，实现基于位置的带宽管理或TCP小区拥塞检测功能。当需要将多个位置信息组合起来对外呈现时，可将其绑定到同一位置组。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-USRLOCATION]] · ADD USRLOCATION
- [[command/UNC/20.15.2/LST-USRLOCATION]] · LST USRLOCATION
- [[command/UNC/20.15.2/MOD-USRLOCATION]] · MOD USRLOCATION
- [[command/UNC/20.15.2/RMV-USRLOCATION]] · RMV USRLOCATION

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户位置（MOD-USRLOCATION）_09897144.md`
- 原始手册：`evidence/UNC/20.15.2/删除用户位置（RMV-USRLOCATION）_09897145.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户位置（ADD-USRLOCATION）_09897143.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户位置（LST-USRLOCATION）_09897146.md`
