---
id: UDG@20.15.2@ConfigObject@PROTOCOLDEFINE
type: ConfigObject
name: PROTOCOLDEFINE（自定义协议）
nf: UDG
version: 20.15.2
object_name: PROTOCOLDEFINE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# PROTOCOLDEFINE（自定义协议）

## 说明

**适用NF：PGW-U、UPF**

该命令用来定义自定义协议类型，可以配置自定义协议所属协议大类，带服务器IP地址、端口范围、或HOST值的过滤器，以及协议识别匹配时的优先级，通过该命令的设置，系统可以根据设置的IP地址、端口或HOST值识别出7层协议类型。

## 操作本对象的命令

- [ADD PROTOCOLDEFINE](command/UDG/20.15.2/ADD-PROTOCOLDEFINE.md)
- [LST PROTOCOLDEFINE](command/UDG/20.15.2/LST-PROTOCOLDEFINE.md)
- [MOD PROTOCOLDEFINE](command/UDG/20.15.2/MOD-PROTOCOLDEFINE.md)
- [RMV PROTOCOLDEFINE](command/UDG/20.15.2/RMV-PROTOCOLDEFINE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改自定义协议（MOD-PROTOCOLDEFINE）_82837328.md`
- 原始手册：`evidence/UDG/20.15.2/删除自定义协议（RMV-PROTOCOLDEFINE）_82837329.md`
- 原始手册：`evidence/UDG/20.15.2/增加自定义协议（ADD-PROTOCOLDEFINE）_82837327.md`
- 原始手册：`evidence/UDG/20.15.2/查询自定义协议（LST-PROTOCOLDEFINE）_82837330.md`
