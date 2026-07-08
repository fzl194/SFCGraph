---
id: UDG@20.15.2@ConfigObject@SECTION
type: ConfigObject
name: SECTION（地址段信息）
nf: UDG
version: 20.15.2
object_name: SECTION
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# SECTION（地址段信息）

## 说明

**适用NF：PGW-U、UPF**

该命令为地址池增加地址段。系统在激活用户时需要为对应的地址池分配地址段，可用该命令配置对应地址池的地址段。

## 操作本对象的命令

- [ADD SECTION](command/UDG/20.15.2/ADD-SECTION.md)
- [LCK SECTION](command/UDG/20.15.2/LCK-SECTION.md)
- [LST SECTION](command/UDG/20.15.2/LST-SECTION.md)
- [MOD SECTION](command/UDG/20.15.2/MOD-SECTION.md)
- [RMV SECTION](command/UDG/20.15.2/RMV-SECTION.md)

## 关联对象

- [POOL](configobject/UDG/20.15.2/POOL.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改地址段信息（MOD-SECTION）_82837118.md`
- 原始手册：`evidence/UDG/20.15.2/删除地址池IP地址段（RMV-SECTION）_82837115.md`
- 原始手册：`evidence/UDG/20.15.2/查询地址池IP地址段（LST-SECTION）_82837116.md`
- 原始手册：`evidence/UDG/20.15.2/添加地址池IP地址段（ADD-SECTION）_82837114.md`
- 原始手册：`evidence/UDG/20.15.2/锁定地址段（LCK-SECTION）_82837117.md`
