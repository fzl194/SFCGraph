---
id: UDG@20.15.2@ConfigObject@EDNS
type: ConfigObject
name: EDNS
nf: UDG
version: 20.15.2
object_name: EDNS
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# EDNS

## 说明

**适用NF：PGW-U、UPF**

该命令用于添加EDNS的相关配置。配置EDNS功能，可以将用户相关信息插入DNS协议内部，传递给Web服务器。Web服务器获取到这些信息以后可以用于支持更多的DNS请求业务。

## 操作本对象的命令

- [ADD EDNS](command/UDG/20.15.2/ADD-EDNS.md)
- [LST EDNS](command/UDG/20.15.2/LST-EDNS.md)
- [MOD EDNS](command/UDG/20.15.2/MOD-EDNS.md)
- [RMV EDNS](command/UDG/20.15.2/RMV-EDNS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改EDNS（MOD-EDNS）_83909785.md`
- 原始手册：`evidence/UDG/20.15.2/删除EDNS（RMV-EDNS）_83909786.md`
- 原始手册：`evidence/UDG/20.15.2/增加EDNS（ADD-EDNS）_83909784.md`
- 原始手册：`evidence/UDG/20.15.2/查询EDNS（LST-EDNS）_83909787.md`
