---
id: UNC@20.15.2@ConfigObject@IMSIAPNBINDUP
type: ConfigObject
name: IMSIAPNBINDUP（APN下用户和UPF的绑定关系配置）
nf: UNC
version: 20.15.2
object_name: IMSIAPNBINDUP
object_kind: binding
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
status: active
---

# IMSIAPNBINDUP（APN下用户和UPF的绑定关系配置）

## 说明

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加APN下用户和UPF的绑定关系，在拨测场景下需要增加APN下用户IMSI和UPF的绑定关系，同一个APN下系统支持添加一个用户和UPF的绑定关系，同时也支持添加连续IMSI号段用户和UPF的绑定关系。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IMSIAPNBINDUP]] · ADD IMSIAPNBINDUP
- [[command/UNC/20.15.2/LST-IMSIAPNBINDUP]] · LST IMSIAPNBINDUP
- [[command/UNC/20.15.2/MOD-IMSIAPNBINDUP]] · MOD IMSIAPNBINDUP
- [[command/UNC/20.15.2/RMV-IMSIAPNBINDUP]] · RMV IMSIAPNBINDUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN下用户和UPF的绑定关系配置（MOD-IMSIAPNBINDUP）_21861977.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN下用户和UPF的绑定关系配置（RMV-IMSIAPNBINDUP）_21861989.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN下用户和UPF的绑定关系配置（ADD-IMSIAPNBINDUP）_21742329.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN下用户和UPF的绑定关系配置（LST-IMSIAPNBINDUP）_75982844.md`
