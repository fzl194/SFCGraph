---
id: UNC@20.15.2@ConfigObject@TSTPCFSEL
type: ConfigObject
name: TSTPCFSEL（拨测用户与PCF服务区的绑定关系）
nf: UNC
version: 20.15.2
object_name: TSTPCFSEL
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# TSTPCFSEL（拨测用户与PCF服务区的绑定关系）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置用户和PCF服务区的绑定关系。一般用于拨测场景，将指定IMSI的用户激活到指定的PCF服务区上，测试PCF的基本功能。

## 操作本对象的命令

- [ADD TSTPCFSEL](command/UNC/20.15.2/ADD-TSTPCFSEL.md)
- [LST TSTPCFSEL](command/UNC/20.15.2/LST-TSTPCFSEL.md)
- [MOD TSTPCFSEL](command/UNC/20.15.2/MOD-TSTPCFSEL.md)
- [RMV TSTPCFSEL](command/UNC/20.15.2/RMV-TSTPCFSEL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改拨测用户与PCF服务区的绑定关系（MOD-TSTPCFSEL）_70462589.md`
- 原始手册：`evidence/UNC/20.15.2/删除拨测用户与PCF服务区的绑定关系（RMV-TSTPCFSEL）_70382393.md`
- 原始手册：`evidence/UNC/20.15.2/增加拨测用户与PCF服务区的绑定关系（ADD-TSTPCFSEL）_70462529.md`
- 原始手册：`evidence/UNC/20.15.2/查询拨测用户与PCF服务区的绑定关系（LST-TSTPCFSEL）_70462569.md`
