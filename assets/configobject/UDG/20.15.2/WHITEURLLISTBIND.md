---
id: UDG@20.15.2@ConfigObject@WHITEURLLISTBIND
type: ConfigObject
name: WHITEURLLISTBIND（用户模板的URL白名单列表）
nf: UDG
version: 20.15.2
object_name: WHITEURLLISTBIND
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# WHITEURLLISTBIND（用户模板的URL白名单列表）

## 说明

**适用NF：PGW-U、UPF**

该命令用于设置用户模板的URL白名单列表。配置该URL白名单列表后，用户进行内容计费的在线计费时，如果匹配的费率组的配额不足，用户报文会触发SMF/UPF 向OCS发送配额请求消息，如果OCS返回的是重定向处理，并且业务报文的URL匹配了其中配置的URL，用户业务可以正常访问URL，无需进行重定向处理。

## 操作本对象的命令

- [[command/UDG/20.15.2/RMV-WHITEURLLISTBIND]] · RMV WHITEURLLISTBIND
- [[command/UDG/20.15.2/SET-WHITEURLLISTBIND]] · SET WHITEURLLISTBIND

## 证据

- 原始手册：`evidence/UDG/20.15.2/WHITEURLLISTBIND.md`
- 原始手册：`evidence/UDG/20.15.2/WHITEURLLISTBIND.md`
