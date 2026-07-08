---
id: UNC@20.15.2@ConfigObject@IMSIBINDUP
type: ConfigObject
name: IMSIBINDUP（用户和UPF的绑定关系）
nf: UNC
version: 20.15.2
object_name: IMSIBINDUP
object_kind: binding
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
status: active
---

# IMSIBINDUP（用户和UPF的绑定关系）

## 说明

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加用户和UPF的绑定关系，在拨测场景下需要增加用户IMSI和UPF的绑定关系，系统支持添加一个用户和UPF的绑定关系，同时也支持添加连续IMSI号段用户和UPF的绑定关系。

## 操作本对象的命令

- [ADD IMSIBINDUP](command/UNC/20.15.2/ADD-IMSIBINDUP.md)
- [LST IMSIBINDUP](command/UNC/20.15.2/LST-IMSIBINDUP.md)
- [MOD IMSIBINDUP](command/UNC/20.15.2/MOD-IMSIBINDUP.md)
- [RMV IMSIBINDUP](command/UNC/20.15.2/RMV-IMSIBINDUP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户和UPF的绑定关系（MOD-IMSIBINDUP）_09651498.md`
- 原始手册：`evidence/UNC/20.15.2/删除用户和UPF的绑定关系（RMV-IMSIBINDUP）_09653627.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户和UPF的绑定关系（ADD-IMSIBINDUP）_09654380.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户和UPF的绑定关系（LST-IMSIBINDUP）_09651580.md`
