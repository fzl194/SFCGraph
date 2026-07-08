---
id: UNC@20.15.2@ConfigObject@ADDRPOOL
type: ConfigObject
name: ADDRPOOL（地址池）
nf: UNC
version: 20.15.2
object_name: ADDRPOOL
object_kind: entity
applicable_nf:
- GGSN
- SMF
- PGW-C
status: active
---

# ADDRPOOL（地址池）

## 说明

**适用NF：GGSN、SMF、PGW-C**

该命令用于为UNC上激活本地分配地址用户或者UDM、Radius和DHCP分配地址的用户创建对应的地址池。

## 操作本对象的命令

- [ADD ADDRPOOL](command/UNC/20.15.2/ADD-ADDRPOOL.md)
- [LCK ADDRPOOL](command/UNC/20.15.2/LCK-ADDRPOOL.md)
- [LST ADDRPOOL](command/UNC/20.15.2/LST-ADDRPOOL.md)
- [MOD ADDRPOOL](command/UNC/20.15.2/MOD-ADDRPOOL.md)
- [RMV ADDRPOOL](command/UNC/20.15.2/RMV-ADDRPOOL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改地址池（MOD-ADDRPOOL）_64343893.md`
- 原始手册：`evidence/UNC/20.15.2/删除地址池（RMV-ADDRPOOL）_09654433.md`
- 原始手册：`evidence/UNC/20.15.2/增加地址池（ADD-ADDRPOOL）_09653289.md`
- 原始手册：`evidence/UNC/20.15.2/查询地址池（LST-ADDRPOOL）_09652305.md`
- 原始手册：`evidence/UNC/20.15.2/锁定_解锁地址池（LCK-ADDRPOOL）_64343873.md`
