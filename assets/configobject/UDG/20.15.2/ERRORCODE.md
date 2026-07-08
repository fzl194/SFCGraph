---
id: UDG@20.15.2@ConfigObject@ERRORCODE
type: ConfigObject
name: ERRORCODE（错误码）
nf: UDG
version: 20.15.2
object_name: ERRORCODE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# ERRORCODE（错误码）

## 说明

**适用NF：PGW-U、UPF**

此命令用于配置错误码信息。运营商可以根据报文中错误码进行不同的重定向动作处理。

## 操作本对象的命令

- [ADD ERRORCODE](command/UDG/20.15.2/ADD-ERRORCODE.md)
- [LST ERRORCODE](command/UDG/20.15.2/LST-ERRORCODE.md)
- [RMV ERRORCODE](command/UDG/20.15.2/RMV-ERRORCODE.md)

## 关联对象

- [DNSOVERWRITING](configobject/UDG/20.15.2/DNSOVERWRITING.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除错误码（RMV-ERRORCODE）_09678506.md`
- 原始手册：`evidence/UDG/20.15.2/增加错误码（ADD-ERRORCODE）_09678504.md`
- 原始手册：`evidence/UDG/20.15.2/查询错误码（LST-ERRORCODE）_09678507.md`
