---
id: UDG@20.15.2@ConfigObject@WHITEURLLIST
type: ConfigObject
name: WHITEURLLIST（URL白名单）
nf: UDG
version: 20.15.2
object_name: WHITEURLLIST
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# WHITEURLLIST（URL白名单）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置白名单及白名单下的URL。用户在进行内容计费的在线计费时，如果匹配到的费率组的配额不足，会触发向OCS申请配额，如果此时OCS下发重定向处理，正常情况下，业务会进行重定向处理，如果配置了白名单，并且用户访问的URL匹配上白名单，业务可以正常访问URL，不需要进行重定向处理。在其他场景下，则白名单功能不起作用。

## 操作本对象的命令

- [ADD WHITEURLLIST](command/UDG/20.15.2/ADD-WHITEURLLIST.md)
- [LST WHITEURLLIST](command/UDG/20.15.2/LST-WHITEURLLIST.md)
- [RMV WHITEURLLIST](command/UDG/20.15.2/RMV-WHITEURLLIST.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除URL白名单（RMV-WHITEURLLIST）_82837394.md`
- 原始手册：`evidence/UDG/20.15.2/增加URL白名单（ADD-WHITEURLLIST）_82837393.md`
- 原始手册：`evidence/UDG/20.15.2/查询URL白名单（LST-WHITEURLLIST）_82837395.md`
