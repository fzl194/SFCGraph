---
id: UDG@20.15.2@ConfigObject@PUREFWDUSER
type: ConfigObject
name: PUREFWDUSER（纯转发用户配置）
nf: UDG
version: 20.15.2
object_name: PUREFWDUSER
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# PUREFWDUSER（纯转发用户配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令通过MSISDN、IMSI设置指定用户进行纯转发，纯转发用户走快速转发流程。

纯转发指不对该MSISDN、IMSI进行计费或7层业务解析，直接将报文进行转发。

该命令用于提升UPF数传定位定界自证能力。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-PUREFWDUSER]] · ADD PUREFWDUSER
- [[command/UDG/20.15.2/LST-PUREFWDUSER]] · LST PUREFWDUSER
- [[command/UDG/20.15.2/RMV-PUREFWDUSER]] · RMV PUREFWDUSER

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除纯转发用户配置（RMV-PUREFWDUSER）_20788153.md`
- 原始手册：`evidence/UDG/20.15.2/显示纯转发用户配置（LST-PUREFWDUSER）_33110040.md`
- 原始手册：`evidence/UDG/20.15.2/设置指定用户进行纯转发（ADD-PUREFWDUSER）_33458112.md`
